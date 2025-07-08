from cp_library.perf.benchmark import Benchmark, BenchmarkConfig, TestCase
from cp_library.perf.generators import create_generator
from cp_library.alg.iter.rank.irank_fn import irank
from cp_library.alg.iter.rank.irank_multi_fn import irank as irank_multi
from itertools import product
from typing import Dict, List, Any, Callable, Tuple

class RankingBenchmark(Benchmark):
    """Benchmark for comparing ranking algorithm implementations"""
    
    def generate_test_cases(self, param_grid: Dict[str, List[Any]]) -> List[TestCase]:
        """Generate test cases from parameter grid"""
        test_cases = []
        
        # Extract parameters
        param_names = list(param_grid.keys())
        param_values = [param_grid[name] for name in param_names]
        
        for values in product(*param_values):
            params = dict(zip(param_names, values))
            
            # Generate data based on distribution parameter
            size = params['size']
            distribution = params['distribution']
            
            # Use the generator factory
            generator = create_generator(distribution)
            data = generator.generate(size=size)
            
            # Create descriptive name
            name = f"size={size}, dist={distribution}, distinct={params.get('distinct', False)}"
            
            test_cases.append(TestCase(
                name=name,
                params=params,
                data={'data': data, 'distinct': params.get('distinct', False)}
            ))
        
        return test_cases
    
    def get_implementations(self) -> Dict[str, Callable]:
        """Return implementations to benchmark"""
        return {
            'irank': lambda data, distinct=False: irank(data.copy(), distinct=distinct),
            'irank_multi': lambda data, distinct=False: irank_multi(data.copy(), distinct=distinct)
        }
    
    def measure_time(self, func: Callable, test_data: Dict) -> Tuple[Any, float]:
        """Override to handle dict test data"""
        import time
        
        # Warmup
        for _ in range(self.config.warmup):
            func(**test_data)
        
        # Actual measurement
        start = time.perf_counter()
        for _ in range(self.config.iterations):
            result = func(**test_data)
        elapsed_ms = (time.perf_counter() - start) * 1000 / self.config.iterations
        
        return result, elapsed_ms

def run_ranking_benchmark():
    """Run a comprehensive ranking algorithm benchmark"""
    
    # Configure benchmark
    config = BenchmarkConfig(
        name="ranking_algorithms",
        iterations=10,
        warmup=2,
        save_results=True,
        plot_results=False,  # Set to True if matplotlib is installed
        output_dir="./benchmark_results/ranking"
    )
    
    # Create benchmark instance
    benchmark = RankingBenchmark(config)
    
    # Define parameter grid
    param_grid = {
        'size': [100, 1000, 10000, 50000],
        'distribution': ['random', 'sorted', 'reverse', 'duplicates', 'almost_sorted', 'plateau'],
        'distinct': [True, False]
    }
    
    # Run benchmark
    benchmark.run(param_grid)
    
    # Print summary statistics
    print_summary(benchmark.results)

def print_summary(results):
    """Print summary statistics from benchmark results"""
    from collections import defaultdict
    import statistics
    
    # Group results by implementation
    impl_times = defaultdict(list)
    
    for result in results:
        if result.time_ms != float('inf'):
            impl_times[result.implementation].append(result.time_ms)
    
    print("\n" + "="*60)
    print("SUMMARY STATISTICS")
    print("="*60)
    
    print(f"\n{'Implementation':<20} {'Mean (ms)':<12} {'Std Dev':<12} {'Min':<12} {'Max':<12} {'Samples':<10}")
    print("-"*80)
    
    for impl, times in impl_times.items():
        if times:
            mean_time = statistics.mean(times)
            std_time = statistics.stdev(times) if len(times) > 1 else 0
            min_time = min(times)
            max_time = max(times)
            
            print(f"{impl:<20} {mean_time:<12.3f} {std_time:<12.3f} {min_time:<12.3f} {max_time:<12.3f} {len(times):<10}")
    
    # Calculate speedup ratios
    if len(impl_times) == 2:
        impls = list(impl_times.keys())
        impl1_mean = statistics.mean(impl_times[impls[0]])
        impl2_mean = statistics.mean(impl_times[impls[1]])
        speedup = impl1_mean / impl2_mean
        
        faster = impls[1] if speedup > 1 else impls[0]
        ratio = max(speedup, 1/speedup)
        
        print(f"\n{faster} is {ratio:.2f}x faster on average")

if __name__ == "__main__":
    run_ranking_benchmark()