"""
Plotting utilities for benchmark results.
Handles both matplotlib and ASCII plotting with consistent interface.
"""

import statistics
from typing import Dict, List, Any
from pathlib import Path
from collections import defaultdict


class BenchmarkPlotter:
    """Creates plots from benchmark results"""
    
    def __init__(self, plot_scale: str = "loglog"):
        self.plot_scale = plot_scale
    
    def create_plots(self, results: List[Dict[str, Any]], config) -> None:
        """Create all plots for benchmark results"""
        try:
            import matplotlib.pyplot as plt
            self._create_matplotlib_plots(plt, results, config)
        except ImportError:
            print("Matplotlib not available - using ASCII plots")
            self._create_ascii_plots(results, config)
        except Exception as e:
            print(f"Plotting failed: {e}")
    
    def _group_results_by_operation(self, results: List[Dict[str, Any]]) -> Dict[str, Dict[int, List[Dict[str, Any]]]]:
        """Group results by operation and size for plotting"""
        data_by_op = defaultdict(lambda: defaultdict(list))
        for r in results:
            if r['time_ms'] != float('inf') and r['correct']:
                data_by_op[r['operation']][r['size']].append({
                    'implementation': r['implementation'],
                    'time_ms': r['time_ms']
                })
        return data_by_op
    
    def _create_matplotlib_plots(self, plt, results: List[Dict[str, Any]], config) -> None:
        """Create matplotlib plots"""
        output_dir = Path(config.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Group and prepare data for plotting
        data_by_op = self._group_results_by_operation(results)
        
        # Create plots for each operation
        for operation, operation_data in data_by_op.items():
            self._create_performance_plot(plt, operation, operation_data, output_dir, config.name)
            self._create_speedup_plot(plt, operation, operation_data, output_dir, config.name)
    
    def _create_performance_plot(self, plt, operation: str, operation_data: Dict[int, List[Dict[str, Any]]], output_dir: Path, benchmark_name: str):
        """Create performance plot for a single operation"""
        sizes = sorted(operation_data.keys())
        implementations = set()
        for size_data in operation_data.values():
            for entry in size_data:
                implementations.add(entry['implementation'])
        
        implementations = sorted(implementations)
        
        # Collect all timing data
        all_data = {}
        for impl in implementations:
            impl_times = []
            impl_sizes = []
            for size in sizes:
                times = [entry['time_ms'] for entry in operation_data[size] 
                        if entry['implementation'] == impl]
                if times:
                    impl_times.append(statistics.mean(times))
                    impl_sizes.append(size)
            
            if impl_times:
                all_data[impl] = (impl_sizes, impl_times)
        
        # Create performance plot
        plt.figure(figsize=(10, 6))
        for impl, (impl_sizes, impl_times) in all_data.items():
            plt.plot(impl_sizes, impl_times, 'o-', label=impl)
        
        plt.xlabel('Input Size')
        plt.ylabel('Time (ms)')
        plt.title(f'{benchmark_name} - {operation} Operation')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        self._apply_scaling(plt)
        
        plot_file = output_dir / f"{benchmark_name}_{operation}_performance.png"
        plt.savefig(plot_file, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Plot saved: {plot_file}")
    
    def _create_speedup_plot(self, plt, operation: str, operation_data: Dict[int, List[Dict[str, Any]]], output_dir: Path, benchmark_name: str):
        """Create speedup plot for a single operation"""
        sizes = sorted(operation_data.keys())
        implementations = set()
        for size_data in operation_data.values():
            for entry in size_data:
                implementations.add(entry['implementation'])
        
        implementations = sorted(implementations)
        
        if len(implementations) <= 1:
            return  # Need at least 2 implementations for speedup
        
        # Collect all timing data
        all_data = {}
        for impl in implementations:
            impl_times = []
            impl_sizes = []
            for size in sizes:
                times = [entry['time_ms'] for entry in operation_data[size] 
                        if entry['implementation'] == impl]
                if times:
                    impl_times.append(statistics.mean(times))
                    impl_sizes.append(size)
            
            if impl_times:
                all_data[impl] = (impl_sizes, impl_times)
        
        # Create speedup plot (relative to first implementation)
        baseline_impl = implementations[0]
        baseline_sizes, baseline_times = all_data[baseline_impl]
        
        plt.figure(figsize=(10, 6))
        for impl, (impl_sizes, impl_times) in all_data.items():
            speedups = []
            speedup_sizes = []
            
            # Calculate speedup relative to baseline for each size
            for size, time in zip(impl_sizes, impl_times):
                if size in baseline_sizes:
                    baseline_idx = baseline_sizes.index(size)
                    baseline_time = baseline_times[baseline_idx]
                    if time > 0:
                        speedup = baseline_time / time
                        speedups.append(speedup)
                        speedup_sizes.append(size)
            
            if speedups:
                plt.plot(speedup_sizes, speedups, 'o-', label=impl)
        
        plt.xlabel('Input Size')
        plt.ylabel(f'Speedup (relative to {baseline_impl})')
        plt.title(f'{benchmark_name} - {operation} Operation Speedup')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.axhline(y=1.0, color='k', linestyle='--', alpha=0.5, label='Baseline')
        
        # Apply scaling (semilogx for speedup plots)
        if self.plot_scale in ["loglog", "semilogx"]:
            plt.semilogx()
        elif self.plot_scale == "semilogy":
            plt.semilogx()  # Only log x-axis for speedup plots
        # else: linear scale (default)
        
        speedup_plot_file = output_dir / f"{benchmark_name}_{operation}_speedup.png"
        plt.savefig(speedup_plot_file, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Speedup plot saved: {speedup_plot_file}")
    
    def _apply_scaling(self, plt):
        """Apply the configured scaling to the plot"""
        if self.plot_scale == "loglog":
            plt.loglog()
        elif self.plot_scale == "linear":
            pass  # Default linear scale
        elif self.plot_scale == "semilogx":
            plt.semilogx()
        elif self.plot_scale == "semilogy":
            plt.semilogy()
        else:
            # Default to loglog if invalid option
            plt.loglog()
    
    def _create_ascii_plots(self, results: List[Dict[str, Any]], config) -> None:
        """Create ASCII plots when matplotlib is not available"""
        if not results:
            return
        
        output_dir = Path(config.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\nGenerating ASCII plots in {output_dir}/")
        
        # Group by operation for ASCII plots
        data_by_op = self._group_results_by_operation(results)
        
        for operation, operation_data in data_by_op.items():
            self._create_ascii_size_plot(operation_data, operation, config.name, output_dir)
            self._create_ascii_comparison_table(operation_data, operation, config.name, output_dir)
    
    def _create_ascii_size_plot(self, operation_data: Dict[int, List[Dict[str, Any]]], operation: str, name: str, output_dir: Path):
        """Create ASCII plot of performance vs size"""
        # Group by implementation and size
        impl_data = {}
        for size, entries in operation_data.items():
            for entry in entries:
                impl = entry['implementation']
                time_ms = entry['time_ms']
                
                if impl not in impl_data:
                    impl_data[impl] = {}
                if size not in impl_data[impl]:
                    impl_data[impl][size] = []
                impl_data[impl][size].append(time_ms)
        
        # Calculate averages
        for impl in impl_data:
            for size in impl_data[impl]:
                impl_data[impl][size] = sum(impl_data[impl][size]) / len(impl_data[impl][size])
        
        # Create ASCII plot
        plot_lines = []
        plot_lines.append(f"Performance vs Size - {name} - {operation}")
        plot_lines.append("=" * 60)
        plot_lines.append("")
        
        if impl_data:
            # Get all sizes
            all_sizes = set()
            for impl in impl_data:
                all_sizes.update(impl_data[impl].keys())
            all_sizes = sorted(all_sizes)
            
            # Create table
            plot_lines.append(f"{'Size':<12} " + "".join(f"{impl:<15}" for impl in impl_data.keys()))
            plot_lines.append("-" * (12 + 15 * len(impl_data)))
            
            for size in all_sizes:
                line = f"{size:<12} "
                for impl in impl_data.keys():
                    time_val = impl_data[impl].get(size, 0)
                    line += f"{time_val:<15.3f}"
                plot_lines.append(line)
        
        # Save to file
        filename = output_dir / f"{name}_{operation}_size_plot.txt"
        with open(filename, 'w') as f:
            f.write('\n'.join(plot_lines))
        print(f"ASCII plot saved: {filename}")
    
    def _create_ascii_comparison_table(self, operation_data: Dict[int, List[Dict[str, Any]]], operation: str, name: str, output_dir: Path):
        """Create comparison table for ASCII output"""
        # Flatten all entries
        all_entries = []
        for entries in operation_data.values():
            all_entries.extend(entries)
        
        # Group by implementation
        impl_times = {}
        for entry in all_entries:
            impl = entry['implementation']
            if impl not in impl_times:
                impl_times[impl] = []
            impl_times[impl].append(entry['time_ms'])
        
        # Calculate statistics
        stats = {}
        for impl, times in impl_times.items():
            stats[impl] = {
                'mean': sum(times) / len(times),
                'min': min(times),
                'max': max(times),
                'count': len(times)
            }
        
        # Create comparison table
        table_lines = []
        table_lines.append(f"Implementation Comparison - {name} - {operation}")
        table_lines.append("=" * 70)
        table_lines.append("")
        table_lines.append(f"{'Implementation':<20} {'Mean (ms)':<12} {'Min (ms)':<12} {'Max (ms)':<12} {'Count':<8}")
        table_lines.append("-" * 68)
        
        for impl, stat in stats.items():
            table_lines.append(
                f"{impl:<20} {stat['mean']:<12.3f} {stat['min']:<12.3f} "
                f"{stat['max']:<12.3f} {stat['count']:<8}"
            )
        
        # Calculate speedup if 2 implementations
        if len(stats) == 2:
            impls = list(stats.keys())
            ratio = stats[impls[0]]['mean'] / stats[impls[1]]['mean']
            faster = impls[1] if ratio > 1 else impls[0]
            speedup = max(ratio, 1/ratio)
            
            table_lines.append("")
            table_lines.append(f"{faster} is {speedup:.2f}x faster on average")
        
        # Save to file
        filename = output_dir / f"{name}_{operation}_comparison.txt"
        with open(filename, 'w') as f:
            f.write('\n'.join(table_lines))
        print(f"Comparison table saved: {filename}")