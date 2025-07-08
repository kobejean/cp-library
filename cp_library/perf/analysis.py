import cp_library.__header__
import cp_library.perf.__header__
"""Advanced analysis tools for benchmark results"""

from typing import List, Dict, Any
import json
import statistics
from pathlib import Path

class BenchmarkAnalyzer:
    """Analyze and compare benchmark results"""
    
    def __init__(self, results_file: str = None, results_data: List = None):
        if results_file:
            with open(results_file, 'r') as f:
                self.results = json.load(f)
        elif results_data:
            self.results = results_data
        else:
            raise ValueError("Must provide either results_file or results_data")
    
    def group_by_implementation(self) -> Dict[str, List[Dict]]:
        """Group results by implementation"""
        grouped = {}
        for result in self.results:
            impl = result['implementation']
            if impl not in grouped:
                grouped[impl] = []
            grouped[impl].append(result)
        return grouped
    
    def group_by_operation(self) -> Dict[str, List[Dict]]:
        """Group results by operation"""
        grouped = {}
        for result in self.results:
            if 'params' in result and 'operation' in result['params']:
                op = result['params']['operation']
                if op not in grouped:
                    grouped[op] = []
                grouped[op].append(result)
        return grouped
    
    def group_by_size(self) -> Dict[int, List[Dict]]:
        """Group results by size"""
        grouped = {}
        for result in self.results:
            if 'params' in result and 'size' in result['params']:
                size = result['params']['size']
                if size not in grouped:
                    grouped[size] = []
                grouped[size].append(result)
        return grouped
    
    def find_best_implementation(self, operation: str = None, size: int = None) -> Dict[str, Any]:
        """Find best implementation for given constraints"""
        filtered = self.results
        
        if operation:
            filtered = [r for r in filtered if r.get('params', {}).get('operation') == operation]
        if size:
            filtered = [r for r in filtered if r.get('params', {}).get('size') == size]
        
        if not filtered:
            return None
        
        # Group by implementation and calculate averages
        impl_times = {}
        for result in filtered:
            if result.get('error') or result.get('time_ms') == float('inf'):
                continue
            impl = result['implementation']
            if impl not in impl_times:
                impl_times[impl] = []
            impl_times[impl].append(result['time_ms'])
        
        # Calculate statistics
        impl_stats = {}
        for impl, times in impl_times.items():
            if times:
                impl_stats[impl] = {
                    'mean': statistics.mean(times),
                    'std': statistics.stdev(times) if len(times) > 1 else 0,
                    'min': min(times),
                    'max': max(times),
                    'count': len(times)
                }
        
        # Find best
        if impl_stats:
            best_impl = min(impl_stats.keys(), key=lambda k: impl_stats[k]['mean'])
            return {
                'implementation': best_impl,
                'stats': impl_stats[best_impl],
                'all_stats': impl_stats
            }
        
        return None
    
    def calculate_speedup_matrix(self, baseline: str = None) -> Dict[str, Dict[str, float]]:
        """Calculate speedup matrix between implementations"""
        impls = set(r['implementation'] for r in self.results)
        
        if baseline and baseline not in impls:
            baseline = None
        
        if not baseline:
            # Use slowest as baseline
            impl_times = {}
            for impl in impls:
                times = [r['time_ms'] for r in self.results 
                        if r['implementation'] == impl and not r.get('error')]
                if times:
                    impl_times[impl] = statistics.mean(times)
            baseline = max(impl_times.keys(), key=lambda k: impl_times[k]) if impl_times else list(impls)[0]
        
        # Calculate pairwise speedups
        speedup_matrix = {}
        for impl_a in impls:
            speedup_matrix[impl_a] = {}
            for impl_b in impls:
                if impl_a == impl_b:
                    speedup_matrix[impl_a][impl_b] = 1.0
                else:
                    # Get comparable results (same operation and size)
                    speedups = []
                    for result_a in self.results:
                        if result_a['implementation'] != impl_a or result_a.get('error'):
                            continue
                        
                        # Find matching result for impl_b
                        for result_b in self.results:
                            if (result_b['implementation'] == impl_b and 
                                not result_b.get('error') and
                                result_a.get('params') == result_b.get('params')):
                                
                                if result_a['time_ms'] > 0:
                                    speedup = result_b['time_ms'] / result_a['time_ms']
                                    speedups.append(speedup)
                                break
                    
                    speedup_matrix[impl_a][impl_b] = statistics.mean(speedups) if speedups else 0.0
        
        return speedup_matrix
    
    def analyze_scaling(self) -> Dict[str, Dict[str, float]]:
        """Analyze how implementations scale with size"""
        scaling_analysis = {}
        
        by_impl = self.group_by_implementation()
        
        for impl, results in by_impl.items():
            # Group by operation
            op_results = {}
            for result in results:
                if result.get('error') or not result.get('params'):
                    continue
                op = result['params'].get('operation', 'unknown')
                if op not in op_results:
                    op_results[op] = []
                op_results[op].append((result['params']['size'], result['time_ms']))
            
            scaling_analysis[impl] = {}
            
            for op, size_times in op_results.items():
                if len(size_times) < 2:
                    continue
                
                # Sort by size
                size_times.sort()
                
                # Calculate scaling factor (rough estimate)
                sizes = [st[0] for st in size_times]
                times = [st[1] for st in size_times]
                
                # Simple linear regression to estimate scaling
                if len(sizes) >= 2:
                    # Calculate log-log slope for complexity estimation
                    import math
                    log_sizes = [math.log(s) for s in sizes if s > 0]
                    log_times = [math.log(t) for t in times if t > 0]
                    
                    if len(log_sizes) >= 2:
                        # Simple slope calculation
                        n = len(log_sizes)
                        slope = (n * sum(x*y for x,y in zip(log_sizes, log_times)) - 
                                sum(log_sizes) * sum(log_times)) / (n * sum(x*x for x in log_sizes) - sum(log_sizes)**2)
                        
                        scaling_analysis[impl][op] = {
                            'complexity_exponent': slope,
                            'size_range': (min(sizes), max(sizes)),
                            'time_range': (min(times), max(times))
                        }
        
        return scaling_analysis
    
    def generate_summary_report(self) -> str:
        """Generate a comprehensive summary report"""
        report = ["BENCHMARK ANALYSIS REPORT", "="*50, ""]
        
        # Basic stats
        total_results = len(self.results)
        implementations = len(set(r['implementation'] for r in self.results))
        operations = len(set(r.get('params', {}).get('operation', 'unknown') for r in self.results))
        
        report.extend([
            f"Total results: {total_results}",
            f"Implementations tested: {implementations}",
            f"Operations tested: {operations}",
            ""
        ])
        
        # Best implementation per operation
        operations_tested = set(r.get('params', {}).get('operation') for r in self.results if r.get('params'))
        operations_tested.discard(None)
        
        if operations_tested:
            report.extend(["Best Implementation by Operation:", "-"*40])
            for op in sorted(operations_tested):
                best = self.find_best_implementation(operation=op)
                if best:
                    impl = best['implementation']
                    time_ms = best['stats']['mean']
                    report.append(f"{op:<15} {impl:<20} {time_ms:.3f} ms")
            report.append("")
        
        # Scaling analysis
        scaling = self.analyze_scaling()
        if scaling:
            report.extend(["Complexity Analysis:", "-"*40])
            for impl, ops in scaling.items():
                if ops:
                    report.append(f"{impl}:")
                    for op, data in ops.items():
                        exp = data['complexity_exponent']
                        if exp < 0.5:
                            complexity = "O(1) or sub-linear"
                        elif exp < 1.2:
                            complexity = "O(n)"
                        elif exp < 1.8:
                            complexity = "O(n log n)"
                        elif exp < 2.2:
                            complexity = "O(n²)"
                        else:
                            complexity = f"O(n^{exp:.1f})"
                        report.append(f"  {op}: {complexity}")
                    report.append("")
        
        return "\n".join(report)


def compare_benchmark_files(file1: str, file2: str) -> str:
    """Compare two benchmark result files"""
    analyzer1 = BenchmarkAnalyzer(results_file=file1)
    analyzer2 = BenchmarkAnalyzer(results_file=file2)
    
    report = [f"COMPARISON: {Path(file1).name} vs {Path(file2).name}", "="*60, ""]
    
    # Find common operations and implementations
    ops1 = set(r.get('params', {}).get('operation') for r in analyzer1.results)
    ops2 = set(r.get('params', {}).get('operation') for r in analyzer2.results)
    common_ops = ops1 & ops2
    
    impls1 = set(r['implementation'] for r in analyzer1.results)
    impls2 = set(r['implementation'] for r in analyzer2.results)
    common_impls = impls1 & impls2
    
    report.extend([
        f"Common operations: {len(common_ops)}",
        f"Common implementations: {len(common_impls)}",
        ""
    ])
    
    # Compare performance for common operations
    if common_ops and common_impls:
        report.extend(["Performance Comparison:", "-"*30])
        report.append(f"{'Operation':<15} {'Implementation':<15} {'File1 (ms)':<12} {'File2 (ms)':<12} {'Speedup':<10}")
        report.append("-"*70)
        
        for op in sorted(common_ops):
            for impl in sorted(common_impls):
                best1 = analyzer1.find_best_implementation(operation=op)
                best2 = analyzer2.find_best_implementation(operation=op)
                
                if (best1 and best2 and 
                    impl in best1['all_stats'] and impl in best2['all_stats']):
                    time1 = best1['all_stats'][impl]['mean']
                    time2 = best2['all_stats'][impl]['mean']
                    speedup = time1 / time2 if time2 > 0 else 0
                    
                    report.append(f"{op:<15} {impl:<15} {time1:<12.3f} {time2:<12.3f} {speedup:<10.2f}x")
    
    return "\n".join(report)