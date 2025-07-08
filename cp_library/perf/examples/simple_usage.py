"""Simple example of using the benchmarking framework"""

from cp_library.perf.benchmark import Benchmark, BenchmarkConfig, TestCase
from cp_library.perf.generators import RandomArrayGenerator, SortedArrayGenerator
from typing import Dict, List, Any, Callable

class SimpleSortBenchmark(Benchmark):
    """Example benchmark comparing different sorting approaches"""
    
    def generate_test_cases(self, param_grid: Dict[str, List[Any]]) -> List[TestCase]:
        test_cases = []
        
        for size in param_grid['size']:
            # Random data
            random_gen = RandomArrayGenerator()
            test_cases.append(TestCase(
                name=f"random_size_{size}",
                params={'size': size, 'type': 'random'},
                data=random_gen.generate(size)
            ))
            
            # Sorted data
            sorted_gen = SortedArrayGenerator()
            test_cases.append(TestCase(
                name=f"sorted_size_{size}",
                params={'size': size, 'type': 'sorted'},
                data=sorted_gen.generate(size)
            ))
            
            # Reverse sorted
            reverse_gen = SortedArrayGenerator(reverse=True)
            test_cases.append(TestCase(
                name=f"reverse_size_{size}",
                params={'size': size, 'type': 'reverse'},
                data=reverse_gen.generate(size)
            ))
        
        return test_cases
    
    def get_implementations(self) -> Dict[str, Callable]:
        """Different sorting implementations to compare"""
        return {
            'builtin_sort': lambda data: sorted(data),
            'list_sort': lambda data: (data.copy(), data.sort())[0],
            'custom_sort': lambda data: self._custom_sort(data.copy())
        }
    
    def _custom_sort(self, data):
        """Example custom sorting implementation"""
        # Simple selection sort for demonstration
        n = len(data)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
        return data

def main():
    """Run the example benchmark"""
    
    # Create configuration
    config = BenchmarkConfig(
        name="sorting_example",
        iterations=5,
        warmup=1,
        save_results=True,
        plot_results=False,  # Set to True if you have matplotlib
        output_dir="./benchmark_results/example"
    )
    
    # Create and run benchmark
    benchmark = SimpleSortBenchmark(config)
    
    # Small sizes for the example
    param_grid = {
        'size': [10, 50, 100, 500]
    }
    
    benchmark.run(param_grid)
    
    # Access results programmatically
    print("\nAccessing results programmatically:")
    for result in benchmark.results[:5]:  # First 5 results
        if result.error is None:
            print(f"  {result.test_case.name}: {result.implementation} = {result.time_ms:.3f}ms")

if __name__ == "__main__":
    main()