"""
Declarative benchmark framework with minimal boilerplate.
Refactored to follow SOLID principles for better maintainability and extensibility.

Features:
- Decorator-based benchmark registration
- Automatic data generation and validation
- Built-in timing with warmup
- Configurable operations and sizes
- JSON results and matplotlib plotting
- Reduced timing overhead with post-timing checksums
- Pluggable renderers and output managers
- Dependency injection for extensibility
"""

import statistics
from dataclasses import dataclass
from typing import List, Optional
from collections import defaultdict

from cp_library.perf.interfaces import (
    BenchmarkRegistry, BenchmarkOrchestrator, TimerInterface, 
    PlotRenderer, OutputManager, BenchmarkResult
)
from cp_library.perf.registry import BenchmarkRegistryImpl
from cp_library.perf.orchestrator import BenchmarkOrchestratorImpl
from cp_library.perf.timing import BenchmarkTimer
from cp_library.perf.output import JSONOutputManager, NoOpOutputManager
from cp_library.perf.renderers import CompositeRenderer
from cp_library.perf.cli import BenchmarkCLI, CLIConfig


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
    # Profiling mode (maintained for backward compatibility)
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
    """
    Declarative benchmark framework using dependency injection and composition.
    Follows SOLID principles for maintainability and extensibility.
    
    Backward compatible with existing benchmarks while providing enhanced functionality.
    """
    
    def __init__(self, 
                 config: BenchmarkConfig,
                 registry: BenchmarkRegistry = None,
                 timer: TimerInterface = None,
                 renderer: PlotRenderer = None,
                 output_manager: OutputManager = None):
        self.config = config
        
        # Dependency injection with sensible defaults for backward compatibility
        self.registry = registry or BenchmarkRegistryImpl()
        self.timer = timer or BenchmarkTimer(config.iterations, config.warmup)
        self.renderer = renderer or CompositeRenderer(config.plot_scale)
        self.output_manager = output_manager or (
            JSONOutputManager(config.output_dir) if config.save_results else NoOpOutputManager()
        )
        
        # Create orchestrator with injected dependencies
        self.orchestrator = BenchmarkOrchestratorImpl(
            self.registry, 
            self.timer, 
            self.output_manager if config.save_results else None
        )
        
        self.cli = BenchmarkCLI(config.name, config.operations, config.sizes)
        self.results: List[BenchmarkResult] = []
    
    def parse_args(self):
        """Parse command line arguments and return configured benchmark"""
        cli_config = self.cli.parse_args()
        self.cli.validate_args(cli_config)
        
        if cli_config.profile_mode:
            return self.create_profile_benchmark(
                cli_config.operation,
                cli_config.size,
                cli_config.implementation
            )
        
        # Apply filters for normal mode
        if cli_config.operation:
            self.config.operations = [cli_config.operation]
        if cli_config.size:
            self.config.sizes = [cli_config.size]
        
        return self
    
    def create_profile_benchmark(self, operation: str = None, size: int = None, implementation: str = None):
        """Create a benchmark configured for profiling mode"""
        profile_config = BenchmarkConfig(
            name=f"{self.config.name}_profile",
            sizes=[size] if size else [max(self.config.sizes)],
            operations=[operation] if operation else [self.config.operations[0]],
            iterations=1,  # Single iteration for profiling
            warmup=0,      # No warmup for profiling
            save_results=False,
            plot_results=False,
            profile_mode=True,
            profile_operation=operation,
            profile_size=size,
            profile_implementation=implementation
        )
        
        # Create profile benchmark with no-op output manager
        profile_benchmark = Benchmark(
            profile_config,
            self.registry,
            BenchmarkTimer(1, 0),  # Minimal timing for profiling
            None,  # No plotting in profile mode
            NoOpOutputManager()
        )
        
        # If specific implementation requested, filter it
        if implementation:
            profile_benchmark._filter_implementation = implementation
        
        return profile_benchmark
    
    def profile(self, operation: str = None, size: int = None, implementation: str = None):
        """Create a profiling version of this benchmark (backward compatibility)"""
        return self.create_profile_benchmark(operation, size, implementation)
    
    def run(self):
        """Run benchmarks with the configured strategy"""
        if hasattr(self, '_filter_implementation') or self.config.profile_mode:
            self._run_profile_mode()
        else:
            self._run_normal_mode()
    
    def _run_normal_mode(self):
        """Run normal benchmark mode"""
        print(f"Running {self.config.name}")
        print(f"Sizes: {self.config.sizes}")
        print(f"Operations: {self.config.operations}")
        print("="*80)
        
        # Execute benchmarks
        self.results = self.orchestrator.run_benchmarks(
            self.config.operations, 
            self.config.sizes
        )
        
        # Generate plots if enabled
        if self.config.plot_results and self.renderer:
            self.renderer.create_plots(self.results, self.config)
        
        # Print summary
        self._print_summary()
    
    def _run_profile_mode(self):
        """Run profiling mode with minimal overhead"""
        operation = self.config.operations[0]
        size = self.config.sizes[0]
        impl_name = getattr(self, '_filter_implementation', None)
        
        print(f"PROFILING MODE: {self.config.name}")
        print(f"Operation: {operation}, Size: {size}")
        if impl_name:
            print(f"Implementation: {impl_name}")
        print("="*80)
        print("Run with vmprof: vmprof --web " + ' '.join(__import__('sys').argv))
        print("="*80)
        
        # Generate test data
        generator = self.registry.get_data_generator(operation)
        if not generator:
            raise ValueError(f"No data generator for operation: {operation}")
        
        test_data = generator.generate(size, operation)
        
        # Get implementations
        impls = self.registry.get_implementations(operation)
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
            __import__('sys').stdout.flush()
            
            # Setup if needed
            setup_func = self.registry.get_setup(operation, name)
            if setup_func:
                data = setup_func(test_data)
            else:
                data = test_data
            
            # Run the actual function (this is what vmprof will profile)
            result = func(data)
            print(f"Completed {name}, result checksum: {result}")
            __import__('sys').stdout.flush()
    
    def _print_summary(self):
        """Print performance summary"""
        print("\n" + "="*80)
        print("PERFORMANCE SUMMARY")
        print("="*80)
        
        # Group by operation and size
        by_operation_size = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
        for r in self.results:
            if r.error is None and r.time_ms != float('inf'):
                by_operation_size[r.operation][r.size][r.implementation] = r.time_ms
        
        print(f"{'Operation':<15} {'Best Implementation':<20} {'Avg Time (ms)':<15} {'Speedup':<10}")
        print("-" * 70)
        
        for op in sorted(by_operation_size.keys()):
            # For each operation, only compare implementations on sizes where ALL implementations ran
            common_times = defaultdict(list)
            
            for size, impl_times in by_operation_size[op].items():
                # Get all implementations that have results for this operation
                all_impls = set()
                for s in by_operation_size[op].values():
                    all_impls.update(s.keys())
                
                # Only include this size if all implementations have results
                if len(impl_times) == len(all_impls):
                    for impl, time_ms in impl_times.items():
                        common_times[impl].append(time_ms)
            
            # Calculate averages only on common sizes
            if common_times:
                avg_times = [(impl, statistics.mean(times)) 
                            for impl, times in common_times.items()]
                avg_times.sort(key=lambda x: x[1])
                
                if avg_times:
                    best_impl, best_time = avg_times[0]
                    worst_time = avg_times[-1][1]
                    speedup = worst_time / best_time if best_time > 0 else 0
                    
                    print(f"{op:<15} {best_impl:<20} {best_time:<15.3f} {speedup:<10.1f}x")
    
    # Decorator methods for backward compatibility
    def data_generator(self, name: str = "default"):
        """Decorator to register data generator"""
        return self.registry.data_generator(name)
    
    def implementation(self, name: str, operations=None):
        """Decorator to register implementation"""
        return self.registry.implementation(name, operations)
    
    def validator(self, operation: str = "default"):
        """Decorator to register validator"""
        return self.registry.validator(operation)
    
    def setup(self, name: str, operations=None):
        """Decorator to register setup function"""
        return self.registry.setup(name, operations)
    
    # Backward compatibility methods
    def measure_time(self, func, data, setup_func=None):
        """Measure execution time (backward compatibility)"""
        return self.timer.measure_time(func, data, setup_func)
    
    def validate_result(self, expected, actual, operation):
        """Validate result (backward compatibility)"""
        validator = self.registry.get_validator(operation)
        return validator.validate(expected, actual)