"""Updated ranking benchmark using the cp_library.perf framework"""

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig, TestCase
from cp_library.perf.generators import (
    RandomArrayGenerator, SortedArrayGenerator, DuplicatesArrayGenerator,
    DistributionArrayGenerator, PlateauArrayGenerator, AlmostSortedArrayGenerator
)
from cp_library.alg.iter.rank.irank_fn import irank
from cp_library.alg.iter.rank.irank_multi_fn import irank as irank_multi
from typing import Dict, List, Any, Callable, Tuple
import time

class RankingBenchmark(Benchmark):
    """Extended benchmark for ranking algorithms with all original test cases"""
    
    def generate_test_cases(self, param_grid: Dict[str, List[Any]]) -> List[TestCase]:
        test_cases = []
        
        # Very large random datasets
        test_cases.extend([
            TestCase(
                name="Very large random",
                params={'size': 50000, 'distribution': 'random'},
                data={'data': RandomArrayGenerator(1, 100000).generate(50000), 'distinct': False}
            ),
            TestCase(
                name="Huge random",
                params={'size': 100000, 'distribution': 'random'},
                data={'data': RandomArrayGenerator(1, 1000000).generate(100000), 'distinct': False}
            ),
        ])
        
        # Large sorted datasets
        test_cases.extend([
            TestCase(
                name="Very large sorted",
                params={'size': 50000, 'distribution': 'sorted'},
                data={'data': SortedArrayGenerator().generate(50000), 'distinct': False}
            ),
            TestCase(
                name="Huge sorted",
                params={'size': 100000, 'distribution': 'sorted'},
                data={'data': SortedArrayGenerator().generate(100000), 'distinct': False}
            ),
        ])
        
        # Pathological cases
        test_cases.extend([
            TestCase(
                name="Large mostly duplicates",
                params={'size': 50000, 'distribution': 'duplicates'},
                data={'data': DuplicatesArrayGenerator(100).generate(50000), 'distinct': False}
            ),
            TestCase(
                name="Huge few values",
                params={'size': 100000, 'distribution': 'duplicates'},
                data={'data': DuplicatesArrayGenerator(10).generate(100000), 'distinct': False}
            ),
        ])
        
        # Real-world-like distributions
        test_cases.extend([
            TestCase(
                name="Normal distribution",
                params={'size': 50000, 'distribution': 'normal'},
                data={'data': DistributionArrayGenerator('normal').generate(50000, mean=5000, std=1000), 'distinct': False}
            ),
            TestCase(
                name="Exponential-like",
                params={'size': 50000, 'distribution': 'exponential'},
                data={'data': DistributionArrayGenerator('exponential').generate(50000, rate=0.001), 'distinct': False}
            ),
        ])
        
        # Edge cases with larger data
        test_cases.extend([
            TestCase(
                name="Large alternating",
                params={'size': 50000, 'distribution': 'alternating'},
                data={'data': [i if i % 2 == 0 else 100000 - i for i in range(50000)], 'distinct': False}
            ),
            TestCase(
                name="Large plateau",
                params={'size': 50000, 'distribution': 'plateau'},
                data={'data': PlateauArrayGenerator(2).generate(50000), 'distinct': False}
            ),
        ])
        
        # Add distinct=True versions for some cases
        for test_case in test_cases[:5]:  # First 5 test cases
            distinct_case = TestCase(
                name=test_case.name + " (distinct)",
                params={**test_case.params, 'distinct': True},
                data={**test_case.data, 'distinct': True}
            )
            test_cases.append(distinct_case)
        
        return test_cases
    
    def get_implementations(self) -> Dict[str, Callable]:
        return {
            'irank': lambda data, distinct=False: irank(data.copy(), distinct=distinct),
            'irank_multi': lambda data, distinct=False: irank_multi(data.copy(), distinct=distinct)
        }
    
    def measure_time(self, func: Callable, test_data: Dict) -> Tuple[Any, float]:
        """Override to handle dict test data and adjust iterations for large data"""
        # Adjust iterations based on data size
        data_size = len(test_data['data'])
        iterations = max(1, 50 // (data_size // 1000)) if data_size > 1000 else self.config.iterations
        
        # Warmup
        for _ in range(min(self.config.warmup, 1)):
            func(**test_data)
        
        # Actual measurement
        start = time.perf_counter()
        for _ in range(iterations):
            result = func(**test_data)
        elapsed_ms = (time.perf_counter() - start) * 1000 / iterations
        
        return result, elapsed_ms

class ScalingAnalysisBenchmark(Benchmark):
    """Analyze how performance scales with input size"""
    
    def generate_test_cases(self, param_grid: Dict[str, List[Any]]) -> List[TestCase]:
        test_cases = []
        sizes = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000]
        
        for size in sizes:
            test_cases.append(TestCase(
                name=f"scaling_size_{size}",
                params={'size': size},
                data={'data': RandomArrayGenerator(1, size).generate(size), 'distinct': False}
            ))
        
        return test_cases
    
    def get_implementations(self) -> Dict[str, Callable]:
        return {
            'irank': lambda data, distinct=False: irank(data.copy(), distinct=distinct),
            'irank_multi': lambda data, distinct=False: irank_multi(data.copy(), distinct=distinct)
        }
    
    def measure_time(self, func: Callable, test_data: Dict) -> Tuple[Any, float]:
        """Single iteration for scaling test"""
        start = time.perf_counter()
        result = func(**test_data)
        elapsed_ms = (time.perf_counter() - start) * 1000
        return result, elapsed_ms
    
    def run(self, param_grid: Dict[str, List[Any]]):
        """Override to add scaling analysis output"""
        super().run(param_grid)
        
        print("\nScaling Analysis:")
        print(f"{'Size':<10} {'irank (ms)':<15} {'multi (ms)':<15} {'irank/n':<15} {'multi/n':<15}")
        print("-" * 70)
        
        # Group results by size
        size_results = {}
        for result in self.results:
            size = result.test_case.params['size']
            if size not in size_results:
                size_results[size] = {}
            size_results[size][result.implementation] = result.time_ms
        
        for size in sorted(size_results.keys()):
            times = size_results[size]
            if 'irank' in times and 'irank_multi' in times:
                time1 = times['irank']
                time2 = times['irank_multi']
                time_per_n1 = time1 / size
                time_per_n2 = time2 / size
                
                print(f"{size:<10} {time1:<15.3f} {time2:<15.3f} {time_per_n1:<15.6f} {time_per_n2:<15.6f}")

def run_all_benchmarks():
    """Run all benchmark suites"""
    
    print("=" * 80)
    print("EXTENDED RANKING BENCHMARK")
    print("=" * 80)
    
    # Extended benchmark
    config1 = BenchmarkConfig(
        name="ranking_extended",
        iterations=5,
        warmup=2,
        save_results=True,
        plot_results=True,
        output_dir="./benchmark_results/ranking"
    )
    
    benchmark1 = RankingBenchmark(config1)
    benchmark1.run({})  # Empty grid since we manually create test cases
    
    # Memory usage estimate
    print("\nMemory Usage Estimate:")
    print(f"{'Size':<10} {'Input (MB)':<12} {'Est. Peak (MB)':<15}")
    print("-" * 40)
    
    for size in [10000, 50000, 100000, 500000]:
        input_mb = size * 8 / (1024 * 1024)  # 8 bytes per integer
        peak_mb = input_mb * 3  # Rough estimate
        print(f"{size:<10} {input_mb:<12.2f} {peak_mb:<15.2f}")
    
    print("\n" + "=" * 80)
    print("SCALING ANALYSIS")
    print("=" * 80)
    
    # Scaling analysis
    config2 = BenchmarkConfig(
        name="ranking_scaling",
        iterations=1,
        warmup=0,
        save_results=True,
        plot_results=True,
        output_dir="./output/benchmark_results/ranking"
    )
    
    benchmark2 = ScalingAnalysisBenchmark(config2)
    benchmark2.run({})

if __name__ == "__main__":
    run_all_benchmarks()