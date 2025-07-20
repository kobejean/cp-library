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
import sys
import argparse
from typing import List, Any, Callable, Union
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
    progressive: bool = True  # Show results operation by operation across sizes
    # Profiling mode
    profile_mode: bool = False
    profile_size: int = None
    profile_operation: str = None
    profile_implementation: str = None
    
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
        self.setups = {}
        self.results = []
    
    def profile(self, operation: str = None, size: int = None, implementation: str = None):
        """Create a profiling version of this benchmark"""
        profile_config = BenchmarkConfig(
            name=f"{self.config.name}_profile",
            sizes=self.config.sizes,
            operations=self.config.operations,
            profile_mode=True,
            profile_operation=operation,
            profile_size=size,
            profile_implementation=implementation,
            save_results=False,
            plot_results=False
        )
        
        profile_benchmark = Benchmark(profile_config)
        profile_benchmark.data_generators = self.data_generators
        profile_benchmark.implementations = self.implementations
        profile_benchmark.validators = self.validators
        profile_benchmark.setups = self.setups
        
        return profile_benchmark
    
    def parse_args(self):
        """Parse command line arguments for profiling mode"""
        parser = argparse.ArgumentParser(
            description=f"Benchmark {self.config.name} with optional profiling mode",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  # Normal benchmark mode
  python benchmark.py
  
  # Profile specific operation and implementation
  python benchmark.py --profile --operation random_access --implementation grid
  
  # Profile with specific size
  python benchmark.py --profile --size 1000000
  
  # Profile all implementations of an operation
  python benchmark.py --profile --operation construction
"""
        )
        
        parser.add_argument('--profile', action='store_true',
                          help='Run in profiling mode (minimal overhead for profilers)')
        parser.add_argument('--operation', type=str, 
                          help=f'Operation to profile. Options: {", ".join(self.config.operations)}')
        parser.add_argument('--size', type=int,
                          help=f'Size to profile. Options: {", ".join(map(str, self.config.sizes))}')
        parser.add_argument('--implementation', type=str,
                          help='Specific implementation to profile (default: all)')
        
        args = parser.parse_args()
        
        # If profile mode requested, return a profiling benchmark
        if args.profile:
            return self.profile(
                operation=args.operation,
                size=args.size,
                implementation=args.implementation
            )
        
        # Otherwise return self for normal mode
        return self
        
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
    
    def setup(self, name: str, operations: Union[str, List[str]] = None):
        """Decorator to register setup function that runs before timing"""
        if operations is None:
            operations = ['default']
        elif isinstance(operations, str):
            operations = [operations]
            
        def decorator(func):
            for op in operations:
                if op not in self.setups:
                    self.setups[op] = {}
                self.setups[op][name] = func
            return func
        return decorator
    
    def measure_time(self, func: Callable, data: Any, setup_func: Callable = None) -> tuple[Any, float]:
        """Measure execution time with warmup and optional setup"""
        from cp_library.perf.timing import BenchmarkTimer
        timer = BenchmarkTimer(self.config.iterations, self.config.warmup)
        return timer.measure_time(func, data, setup_func)
    
    def validate_result(self, expected: Any, actual: Any, operation: str) -> bool:
        """Validate result using custom validator or default comparison"""
        if operation in self.validators:
            return self.validators[operation](expected, actual)
        return expected == actual
    
    def run(self):
        """Run all benchmarks"""
        if self.config.profile_mode:
            self._run_profile_mode()
        else:
            self._run_normal_mode()
    
    def _run_normal_mode(self):
        """Run normal benchmark mode"""
        print(f"Running {self.config.name}")
        print(f"Sizes: {self.config.sizes}")
        print(f"Operations: {self.config.operations}")
        print("="*80)
        
        # Always show progressive results: operation by operation across all sizes
        for operation in self.config.operations:
            for size in self.config.sizes:
                self._run_single(operation, size)
        
        # Save and plot results
        if self.config.save_results:
            self._save_results()
        
        if self.config.plot_results:
            self._plot_results()
        
        # Print summary
        self._print_summary()
    
    def _run_profile_mode(self):
        """Run profiling mode with minimal overhead for use with vmprof"""
        operation = self.config.profile_operation or self.config.operations[0]
        size = self.config.profile_size or max(self.config.sizes)
        impl_name = self.config.profile_implementation
        
        print(f"PROFILING MODE: {self.config.name}")
        print(f"Operation: {operation}, Size: {size}")
        if impl_name:
            print(f"Implementation: {impl_name}")
        print("="*80)
        print("Run with vmprof: vmprof --web " + ' '.join(sys.argv))
        print("="*80)
        
        # Generate test data
        generator = self.data_generators.get(operation, self.data_generators.get('default'))
        if not generator:
            raise ValueError(f"No data generator for operation: {operation}")
        
        test_data = generator(size, operation)
        
        # Get implementations
        impls = self.implementations.get(operation, {})
        if not impls:
            raise ValueError(f"No implementations for operation: {operation}")
        
        # Filter to specific implementation if requested
        if impl_name:
            if impl_name not in impls:
                raise ValueError(f"Implementation '{impl_name}' not found for operation '{operation}'")
            impls = {impl_name: impls[impl_name]}
        
        # Run with minimal overhead - no timing, no validation
        for name, func in impls.items():
            print(f"\nRunning {name}...")
            sys.stdout.flush()
            
            # Setup if needed
            setup_func = self.setups.get(operation, {}).get(name)
            if setup_func:
                data = setup_func(test_data)
            else:
                data = test_data
            
            # Run the actual function (this is what vmprof will profile)
            result = func(data)
            print(f"Completed {name}, result checksum: {result}")
            sys.stdout.flush()
    
    def _run_single(self, operation: str, size: int):
        """Run a single operation/size combination"""
        print(f"\nOperation: {operation}, Size: {size}")
        print("-" * 50)
        sys.stdout.flush()
        
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
            return
        
        # Get setup functions for this operation
        setups = self.setups.get(operation, {})
        
        # Run reference implementation first
        ref_name, ref_impl = next(iter(impls.items()))
        ref_setup = setups.get(ref_name)
        expected_result, _ = self.measure_time(ref_impl, test_data, ref_setup)
        
        # Run all implementations
        for impl_name, impl_func in impls.items():
            try:
                setup_func = setups.get(impl_name)
                result, time_ms = self.measure_time(impl_func, test_data, setup_func)
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
                sys.stdout.flush()
                
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
                sys.stdout.flush()
    
    def _save_results(self):
        """Save results to JSON"""
        output_dir = Path(self.config.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        filename = output_dir / f"{self.config.name}_{int(time.time())}.json"
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"\nResults saved to {filename}")
    
    def _plot_results(self):
        """Generate plots using the plotting module"""
        from cp_library.perf.plotting import BenchmarkPlotter
        plotter = BenchmarkPlotter(self.config.plot_scale)
        plotter.create_plots(self.results, self.config)
    
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


