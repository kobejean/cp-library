import cp_library.__header__
import cp_library.perf.__header__
import time
import json
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Tuple, Callable, Optional
from dataclasses import dataclass
from pathlib import Path

@dataclass
class BenchmarkConfig:
    """Configuration for a benchmark run"""
    name: str
    iterations: int = 10
    warmup: int = 2
    timeout: float = 60.0  # seconds
    save_results: bool = True
    plot_results: bool = True
    output_dir: str = "./benchmark_results"

@dataclass
class TestCase:
    """A single test case with parameters and data"""
    name: str
    params: Dict[str, Any]
    data: Any
    expected: Optional[Any] = None

@dataclass
class BenchmarkResult:
    """Result from running a single benchmark"""
    test_case: TestCase
    implementation: str
    time_ms: float
    memory_mb: float = 0.0
    correct: bool = True
    error: Optional[str] = None
    
class Benchmark(ABC):
    """Base class for benchmarks"""
    
    def __init__(self, config: BenchmarkConfig):
        self.config = config
        self.results: List[BenchmarkResult] = []
        
    @abstractmethod
    def generate_test_cases(self, param_grid: Dict[str, List[Any]]) -> List[TestCase]:
        """Generate test cases from parameter grid"""
        pass
    
    @abstractmethod
    def get_implementations(self) -> Dict[str, Callable]:
        """Return dict of implementation name -> function"""
        pass
    
    def validate_result(self, expected: Any, actual: Any) -> bool:
        """Validate if result is correct"""
        return expected == actual
    
    def measure_time(self, func: Callable, *args, **kwargs) -> Tuple[Any, float]:
        """Measure execution time of a function"""
        # Warmup
        for _ in range(self.config.warmup):
            func(*args, **kwargs)
        
        # Actual measurement
        start = time.perf_counter()
        for _ in range(self.config.iterations):
            result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000 / self.config.iterations
        
        return result, elapsed_ms
    
    def run(self, param_grid: Dict[str, List[Any]]):
        """Run the benchmark"""
        test_cases = self.generate_test_cases(param_grid)
        implementations = self.get_implementations()
        
        print(f"Running {self.config.name}")
        print(f"Test cases: {len(test_cases)}, Implementations: {len(implementations)}")
        print("-" * 80)
        
        for test_case in test_cases:
            print(f"\nTest: {test_case.name}")
            
            # Get reference result if not provided
            if test_case.expected is None and implementations:
                ref_impl = next(iter(implementations.values()))
                test_case.expected, _ = self.measure_time(ref_impl, test_case.data)
            
            for impl_name, impl_func in implementations.items():
                try:
                    result, time_ms = self.measure_time(impl_func, test_case.data)
                    correct = self.validate_result(test_case.expected, result)
                    
                    bench_result = BenchmarkResult(
                        test_case=test_case,
                        implementation=impl_name,
                        time_ms=time_ms,
                        correct=correct
                    )
                    self.results.append(bench_result)
                    
                    print(f"  {impl_name:<20} {time_ms:>10.3f} ms  {'✓' if correct else '✗'}")
                    
                except Exception as e:
                    bench_result = BenchmarkResult(
                        test_case=test_case,
                        implementation=impl_name,
                        time_ms=float('inf'),
                        correct=False,
                        error=str(e)
                    )
                    self.results.append(bench_result)
                    print(f"  {impl_name:<20} ERROR: {str(e)[:50]}")
        
        if self.config.save_results:
            self.save_results()
        
        if self.config.plot_results:
            self.plot_results()
    
    def save_results(self):
        """Save results to JSON file"""
        Path(self.config.output_dir).mkdir(parents=True, exist_ok=True)
        
        data = []
        for r in self.results:
            data.append({
                'test_case': r.test_case.name,
                'params': r.test_case.params,
                'implementation': r.implementation,
                'time_ms': r.time_ms,
                'correct': r.correct,
                'error': r.error
            })
        
        filename = f"{self.config.output_dir}/{self.config.name}_{int(time.time())}.json"
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"\nResults saved to {filename}")
    
    def plot_results(self):
        """Create visualizations of results"""
        try:
            from .plotters import BenchmarkPlotter
            plotter = BenchmarkPlotter()
            plotter.plot_results(self.results, self.config)
        except ImportError as e:
            print(f"Plotting skipped: {e}")
            print("To enable plotting, install: pip install matplotlib pandas")
        except Exception as e:
            print(f"Plotting failed: {e}")