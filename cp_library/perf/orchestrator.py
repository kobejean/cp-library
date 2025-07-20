"""
Benchmark orchestrator implementation following Single Responsibility Principle.
"""

import sys
from typing import List
from .interfaces import (
    BenchmarkOrchestrator, BenchmarkRegistry, BenchmarkResult, 
    TimerInterface, OutputManager
)


class BenchmarkOrchestratorImpl(BenchmarkOrchestrator):
    """Implementation of benchmark execution orchestration"""
    
    def __init__(self, 
                 registry: BenchmarkRegistry,
                 timer: TimerInterface,
                 output_manager: OutputManager = None):
        self.registry = registry
        self.timer = timer
        self.output_manager = output_manager
        self.results: List[BenchmarkResult] = []
    
    def run_benchmarks(self, operations: List[str], sizes: List[int]) -> List[BenchmarkResult]:
        """Execute benchmarks and return results"""
        self.results = []
        
        for operation in operations:
            for size in sizes:
                self._run_single(operation, size)
        
        if self.output_manager:
            self.output_manager.save_results(self.results, None)
        
        return self.results
    
    def _run_single(self, operation: str, size: int) -> None:
        """Run a single operation/size combination"""
        print(f"\nOperation: {operation}, Size: {size}")
        print("-" * 50)
        sys.stdout.flush()
        
        # Generate test data
        generator = self.registry.get_data_generator(operation)
        if not generator:
            raise ValueError(f"No data generator for operation: {operation}")
        
        test_data = generator.generate(size, operation)
        
        # Get implementations for this operation
        impls = self.registry.get_implementations(operation)
        if not impls:
            print(f"No implementations for operation: {operation}")
            return
        
        # Run reference implementation first (find first non-skipped implementation)
        expected_result = None
        ref_name = None
        for impl_name, impl_func in impls.items():
            setup_func = self.registry.get_setup(operation, impl_name)
            result, _ = self.timer.measure_time(impl_func, test_data, setup_func)
            if result is not None:
                expected_result = result
                ref_name = impl_name
                break
        
        # If all implementations return None, skip this operation/size combination
        if expected_result is None:
            print("  All implementations skipped")
            return
        
        # Get validator for this operation
        validator = self.registry.get_validator(operation)
        
        # Run all implementations
        for impl_name, impl_func in impls.items():
            try:
                setup_func = self.registry.get_setup(operation, impl_name)
                result, time_ms = self.timer.measure_time(impl_func, test_data, setup_func)
                
                # Check if implementation returned None to skip
                if result is None:
                    print(f"  {impl_name:<20} SKIPPED")
                    sys.stdout.flush()
                    continue
                
                correct = validator.validate(expected_result, result)
                
                # Store result
                benchmark_result = BenchmarkResult(
                    operation=operation,
                    size=size,
                    implementation=impl_name,
                    time_ms=time_ms,
                    correct=correct
                )
                self.results.append(benchmark_result)
                
                status = "OK" if correct else "FAIL"
                print(f"  {impl_name:<20} {time_ms:>8.3f} ms  {status}")
                sys.stdout.flush()
                
            except Exception as e:
                # Get a meaningful error message
                error_msg = str(e) if str(e) else f"{type(e).__name__}: {repr(e)}"
                
                benchmark_result = BenchmarkResult(
                    operation=operation,
                    size=size,
                    implementation=impl_name,
                    time_ms=float('inf'),
                    correct=False,
                    error=error_msg
                )
                self.results.append(benchmark_result)
                print(f"  {impl_name:<20} ERROR: {error_msg[:40]}")
                sys.stdout.flush()