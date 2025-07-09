"""
Declarative benchmark framework with minimal boilerplate.

Features:
- Decorator-based benchmark registration
- Automatic data generation and validation
- Built-in timing with warmup
- Configurable operations and sizes
- JSON results and matplotlib plotting
"""

import time
import json
import statistics
from typing import Dict, List, Any, Callable, Union
from dataclasses import dataclass
from pathlib import Path
from collections import defaultdict

@dataclass
class BenchmarkConfig:
    """Configuration for benchmark runs"""
    name: str
    sizes: List[int] = None
    operations: List[str] = None
    iterations: int = 10
    warmup: int = 2
    output_dir: str = "./output/benchmark_results"
    save_results: bool = True
    plot_results: bool = True
    plot_scale: str = "loglog"  # Options: "loglog", "linear", "semilogx", "semilogy"
    
    def __post_init__(self):
        if self.sizes is None:
            self.sizes = [100, 1000, 10000, 100000]
        if self.operations is None:
            self.operations = ['default']

class Benchmark:
    """Declarative benchmark framework using decorators"""
    
    def __init__(self, config: BenchmarkConfig):
        self.config = config
        self.data_generators = {}
        self.implementations = {}
        self.validators = {}
        self.results = []
        
    def data_generator(self, name: str = "default"):
        """Decorator to register data generator"""
        def decorator(func):
            self.data_generators[name] = func
            return func
        return decorator
    
    def implementation(self, name: str, operations: Union[str, List[str]] = None):
        """Decorator to register implementation"""
        if operations is None:
            operations = ['default']
        elif isinstance(operations, str):
            operations = [operations]
            
        def decorator(func):
            for op in operations:
                if op not in self.implementations:
                    self.implementations[op] = {}
                self.implementations[op][name] = func
            return func
        return decorator
    
    def validator(self, operation: str = "default"):
        """Decorator to register custom validator"""
        def decorator(func):
            self.validators[operation] = func
            return func
        return decorator
    
    def measure_time(self, func: Callable, data: Any) -> tuple[Any, float]:
        """Measure execution time with warmup"""
        # Warmup runs
        for _ in range(self.config.warmup):
            try:
                func(data)
            except Exception:
                # If warmup fails, let the main measurement handle the error
                break
        
        # Actual measurement
        start = time.perf_counter()
        for _ in range(self.config.iterations):
            result = func(data)
        elapsed_ms = (time.perf_counter() - start) * 1000 / self.config.iterations
        
        return result, elapsed_ms
    
    def validate_result(self, expected: Any, actual: Any, operation: str) -> bool:
        """Validate result using custom validator or default comparison"""
        if operation in self.validators:
            return self.validators[operation](expected, actual)
        return expected == actual
    
    def run(self):
        """Run all benchmarks"""
        print(f"Running {self.config.name}")
        print(f"Sizes: {self.config.sizes}")
        print(f"Operations: {self.config.operations}")
        print("="*80)
        
        for size in self.config.sizes:
            for operation in self.config.operations:
                print(f"\nOperation: {operation}, Size: {size}")
                print("-" * 50)
                
                # Generate test data
                generator = self.data_generators.get(operation, 
                                                   self.data_generators.get('default'))
                if not generator:
                    raise ValueError(f"No data generator for operation: {operation}")
                
                test_data = generator(size, operation)
                
                # Get implementations for this operation
                impls = self.implementations.get(operation, {})
                if not impls:
                    print(f"No implementations for operation: {operation}")
                    continue
                
                # Run reference implementation first
                ref_name, ref_impl = next(iter(impls.items()))
                expected_result, _ = self.measure_time(ref_impl, test_data)
                
                # Run all implementations
                for impl_name, impl_func in impls.items():
                    try:
                        result, time_ms = self.measure_time(impl_func, test_data)
                        correct = self.validate_result(expected_result, result, operation)
                        
                        # Store result
                        self.results.append({
                            'operation': operation,
                            'size': size,
                            'implementation': impl_name,
                            'time_ms': time_ms,
                            'correct': correct,
                            'error': None
                        })
                        
                        status = "OK" if correct else "FAIL"
                        print(f"  {impl_name:<20} {time_ms:>8.3f} ms  {status}")
                        
                    except Exception as e:
                        self.results.append({
                            'operation': operation,
                            'size': size,
                            'implementation': impl_name,
                            'time_ms': float('inf'),
                            'correct': False,
                            'error': str(e)
                        })
                        print(f"  {impl_name:<20} ERROR: {str(e)[:40]}")
        
        # Save and plot results
        if self.config.save_results:
            self._save_results()
        
        if self.config.plot_results:
            self._plot_results()
        
        # Print summary
        self._print_summary()
    
    def _save_results(self):
        """Save results to JSON"""
        output_dir = Path(self.config.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        filename = output_dir / f"{self.config.name}_{int(time.time())}.json"
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"\nResults saved to {filename}")
    
    def _plot_results(self):
        """Generate plots using matplotlib if available"""
        try:
            import matplotlib.pyplot as plt
            
            output_dir = Path(self.config.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Group and prepare data for plotting
            data_by_op = self._group_results_by_operation()
            
            # Create plots for each operation
            for operation, operation_data in data_by_op.items():
                self._create_performance_plot(plt, operation, operation_data, output_dir)
                
        except ImportError:
            print("Matplotlib not available - skipping plots")
        except Exception as e:
            print(f"Plotting failed: {e}")
    
    def _group_results_by_operation(self) -> Dict[str, Dict[int, List[Dict[str, Any]]]]:
        """Group results by operation and size for plotting"""
        data_by_op = defaultdict(lambda: defaultdict(list))
        for r in self.results:
            if r['time_ms'] != float('inf') and r['correct']:
                data_by_op[r['operation']][r['size']].append({
                    'implementation': r['implementation'],
                    'time_ms': r['time_ms']
                })
        return data_by_op
    
    def _create_performance_plot(self, plt, operation: str, operation_data: Dict[int, List[Dict[str, Any]]], output_dir: Path):
        """Create a performance plot for a single operation"""
        sizes = sorted(operation_data.keys())
        implementations = set()
        for size_data in operation_data.values():
            for entry in size_data:
                implementations.add(entry['implementation'])
        
        implementations = sorted(implementations)
        
        plt.figure(figsize=(10, 6))
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
                plt.plot(impl_sizes, impl_times, 'o-', label=impl)
        
        plt.xlabel('Input Size')
        plt.ylabel('Time (ms)')
        plt.title(f'{self.config.name} - {operation} Operation')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Apply the configured scaling
        if self.config.plot_scale == "loglog":
            plt.loglog()
        elif self.config.plot_scale == "linear":
            pass  # Default linear scale
        elif self.config.plot_scale == "semilogx":
            plt.semilogx()
        elif self.config.plot_scale == "semilogy":
            plt.semilogy()
        else:
            # Default to loglog if invalid option
            plt.loglog()
        
        plot_file = output_dir / f"{self.config.name}_{operation}_performance.png"
        plt.savefig(plot_file, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Plot saved: {plot_file}")
    
    def _print_summary(self):
        """Print performance summary"""
        print("\n" + "="*80)
        print("PERFORMANCE SUMMARY")
        print("="*80)
        
        # Group by operation
        by_operation = defaultdict(lambda: defaultdict(list))
        for r in self.results:
            if r['error'] is None and r['time_ms'] != float('inf'):
                by_operation[r['operation']][r['implementation']].append(r['time_ms'])
        
        print(f"{'Operation':<15} {'Best Implementation':<20} {'Avg Time (ms)':<15} {'Speedup':<10}")
        print("-" * 70)
        
        for op, impl_times in sorted(by_operation.items()):
            # Calculate averages
            avg_times = [(impl, statistics.mean(times)) 
                        for impl, times in impl_times.items()]
            avg_times.sort(key=lambda x: x[1])
            
            if avg_times:
                best_impl, best_time = avg_times[0]
                worst_time = avg_times[-1][1]
                speedup = worst_time / best_time if best_time > 0 else 0
                
                print(f"{op:<15} {best_impl:<20} {best_time:<15.3f} {speedup:<10.1f}x")


