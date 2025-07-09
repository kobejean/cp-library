# CP Library Performance Benchmarking Framework

A flexible benchmarking framework for competitive programming algorithms with minimal boilerplate.

## Features

- **Class-based design** for easy extension
- **Built-in data generators** for common test patterns
- **Automatic result validation** 
- **Performance visualization** (optional, requires matplotlib)
- **Parameter grid testing**
- **JSON result export**

## Quick Start

```python
from cp_library.perf.benchmark import Benchmark, BenchmarkConfig, TestCase
from cp_library.perf.generators import RandomArrayGenerator

class MyBenchmark(Benchmark):
    def generate_test_cases(self, param_grid):
        # Generate test cases from parameters
        pass
    
    def get_implementations(self):
        # Return dict of implementation functions
        return {
            'impl1': lambda data: my_algorithm1(data),
            'impl2': lambda data: my_algorithm2(data)
        }

# Run benchmark
config = BenchmarkConfig(name="my_benchmark")
benchmark = MyBenchmark(config)
benchmark.run({'size': [100, 1000, 10000]})
```

## Data Generators

Built-in generators for common data patterns:

- `RandomArrayGenerator` - Random integers
- `SortedArrayGenerator` - Sorted sequences
- `DuplicatesArrayGenerator` - Arrays with many duplicates
- `DistributionArrayGenerator` - Normal, exponential, etc.
- `PlateauArrayGenerator` - Arrays with plateaus
- `AlmostSortedArrayGenerator` - Nearly sorted arrays
- `PermutationGenerator` - Random permutations

## Examples

See `examples/` directory for complete examples:
- `simple_usage.py` - Basic sorting benchmark
- `rank_benchmark.py` - Complex ranking algorithm comparison

## Configuration Options

```python
config = BenchmarkConfig(
    name="benchmark_name",
    iterations=10,          # Timing iterations
    warmup=2,              # Warmup iterations
    timeout=60.0,          # Timeout in seconds
    save_results=True,     # Save to JSON
    plot_results=True,     # Generate plots (requires matplotlib)
    output_dir="./results" # Output directory
)
```

## Extending the Framework

1. **Custom Generators**: Subclass `DataGenerator`
2. **Custom Validators**: Override `validate_result()` 
3. **Custom Plotting**: Override `plot_results()`
4. **Custom Metrics**: Add fields to `BenchmarkResult`