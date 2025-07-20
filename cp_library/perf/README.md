# CP Library Performance Benchmarking Framework

A declarative benchmarking framework for competitive programming algorithms with minimal boilerplate.

## Features

- **Decorator-based API** - Register implementations, data generators, and setup functions using decorators
- **Automatic timing and validation** - Built-in timing with warmup and result validation
- **Dual plotting support** - Matplotlib plots with ASCII fallback when unavailable  
- **Performance and speedup plots** - Both absolute performance and relative speedup analysis
- **Profiling integration** - Built-in support for vmprof and other profilers
- **JSON result export** - Save detailed results for further analysis
- **Modular architecture** - Separate modules for timing, plotting, and checksum utilities

## Architecture

The framework consists of several focused modules:

- **`benchmark.py`** - Core benchmark orchestration and decorator API
- **`timing.py`** - Timing and measurement utilities
- **`plotting.py`** - Unified plotting interface (matplotlib + ASCII fallback)
- **`checksum.py`** - Common checksum patterns for result validation

## Quick Start

```python
from cp_library.perf.benchmark import Benchmark, BenchmarkConfig

# Configure benchmark
config = BenchmarkConfig(
    name="my_benchmark",
    sizes=[1000, 10000, 100000],
    operations=['construction', 'access', 'sorting'],
    iterations=10,
    warmup=3,
    output_dir="./output/benchmark_results/my_benchmark"
)

# Create benchmark instance
benchmark = Benchmark(config)

# Register data generator
@benchmark.data_generator("default")
def generate_data(size: int, operation: str):
    data = [random.randint(1, 1000000) for _ in range(size)]
    return {
        'data': data,
        'size': size
    }

# Register implementations
@benchmark.implementation("algorithm1", ["construction", "access", "sorting"])
def impl_algorithm1(data):
    # Your implementation here
    result = my_algorithm1(data['data'])
    return len(result)  # Return checksum

@benchmark.implementation("algorithm2", ["construction", "access", "sorting"]) 
def impl_algorithm2(data):
    # Your implementation here
    result = my_algorithm2(data['data'])
    return len(result)  # Return checksum

# Register setup functions for operations that modify data
@benchmark.setup("algorithm1", ["sorting"])
def setup_algorithm1_sort(data):
    # Copy data before sorting to ensure fair comparison
    new_data = data.copy()
    new_data['data'] = data['data'].copy()
    return new_data

# Run benchmark
if __name__ == "__main__":
    runner = benchmark.parse_args()
    runner.run()
```

## Generated Output

The framework automatically generates:

### 1. Console Output
- Real-time progress with timing results
- Validation status (OK/FAIL) for each implementation
- Performance summary with best implementation and speedup ratios

### 2. Performance Plots
- **`{name}_{operation}_performance.png`** - Absolute timing vs input size
- **`{name}_{operation}_speedup.png`** - Relative speedup compared to first implementation

### 3. JSON Results
- **`{name}_{timestamp}.json`** - Detailed results for further analysis

### 4. ASCII Fallback
- **`{name}_{operation}_size_plot.txt`** - ASCII performance table
- **`{name}_{operation}_comparison.txt`** - Implementation comparison table

## Configuration Options

```python
config = BenchmarkConfig(
    name="benchmark_name",         # Required: benchmark name
    sizes=[100, 1000, 10000],      # Input sizes to test
    operations=['op1', 'op2'],     # Operations to benchmark
    iterations=10,                 # Timing iterations per test
    warmup=3,                      # Warmup iterations
    output_dir="./results",        # Output directory
    save_results=True,             # Save JSON results
    plot_results=True,             # Generate plots
    plot_scale="loglog",           # Plot scaling: "loglog", "linear", "semilogx", "semilogy"
    
    # Profiling mode (use with --profile flag)
    profile_mode=False,            # Enable profiling mode
    profile_size=None,             # Specific size for profiling
    profile_operation=None,        # Specific operation for profiling  
    profile_implementation=None    # Specific implementation for profiling
)
```

## Profiling Support

Run benchmarks with profiling support:

```bash
# Normal benchmark
python my_benchmark.py

# Profile specific operation and implementation  
python my_benchmark.py --profile --operation sorting --implementation algorithm1

# Profile with specific size
python my_benchmark.py --profile --size 1000000

# Profile all implementations of an operation
python my_benchmark.py --profile --operation construction
```

## Utilities

### Checksum Functions

```python
from cp_library.perf.checksum import xor_checksum, tuple_checksum

# Use in implementation functions
@benchmark.implementation("my_impl", "access")
def my_implementation(data):
    results = []
    for item in data['items']:
        result = process(item)
        results.append(result)
    return xor_checksum(*results)  # Return validation checksum
```

### Custom Timing

```python
from cp_library.perf.timing import BenchmarkTimer

timer = BenchmarkTimer(iterations=10, warmup=3)
result, time_ms = timer.measure_time(my_function, test_data)
```

### Custom Plotting

```python
from cp_library.perf.plotting import BenchmarkPlotter

plotter = BenchmarkPlotter(plot_scale="loglog")
plotter.create_plots(results, config)
```

## Examples

See the `/perf/` directory for complete examples:
- `list2.py` - Multichannel list benchmarks
- `view2.py` - Array view benchmarks  
- `segtree2.py` - Segment tree benchmarks
- `csr2.py` - Compressed sparse row benchmarks

## Best Practices

1. **Use descriptive names** for implementations and operations
2. **Return consistent checksums** from implementation functions for validation
3. **Use setup functions** for operations that modify data to ensure fair comparisons
4. **Test with multiple sizes** to understand scaling behavior
5. **Use profiling mode** to identify performance bottlenecks