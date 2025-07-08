# Benchmarking Framework Usage Guide

## What We Built

The `cp_library.perf` module provides a comprehensive benchmarking framework that automatically generates:

1. **Console Output** - Real-time benchmark results
2. **JSON Results** - Detailed data for further analysis 
3. **Multiple Plots** - Visual performance analysis (when matplotlib/pandas available)

## Generated Plots

When `plot_results=True` in your `BenchmarkConfig`, the framework automatically generates:

### 1. Size Performance Plot
- **File**: `{name}_size_performance.png`
- **Shows**: Performance vs input size (log-log scale)
- **Includes**: Error bars for standard deviation

### 2. Implementation Comparison 
- **File**: `{name}_implementation_comparison.png`
- **Shows**: Average performance across all test cases
- **Includes**: Error bars and value labels

### 3. Distribution Analysis
- **File**: `{name}_distribution_analysis.png` 
- **Shows**: Performance breakdown by data distribution type
- **Format**: Grouped bar chart

### 4. Complexity Analysis (NEW)
- **File**: `{name}_complexity_analysis.png`
- **Shows**: Performance curves with O(n) and O(n log n) reference lines
- **Format**: Log-log plot to visualize algorithmic complexity

### 5. Speedup Comparison (NEW)
- **File**: `{name}_speedup_comparison.png`
- **Shows**: Speedup ratios between implementations
- **Colors**: Green bars = faster, Red bars = slower

## Quick Example

```python
from cp_library.perf.benchmark import Benchmark, BenchmarkConfig, TestCase

class MyBenchmark(Benchmark):
    def generate_test_cases(self, param_grid):
        # Your test case generation logic
        return test_cases
    
    def get_implementations(self):
        return {
            'algorithm1': my_algo1,
            'algorithm2': my_algo2
        }

# Enable plotting
config = BenchmarkConfig(
    name="my_analysis",
    plot_results=True,  # This generates all plots automatically
    output_dir="./my_results"
)

benchmark = MyBenchmark(config)
benchmark.run({'size': [100, 1000, 10000]})
```

## Your Ranking Benchmark

Your updated `rank_perf.py` now generates:

1. **Console Output**: Real-time results with ✓/✗ validation
2. **JSON Files**: `ranking_extended_*.json` and `ranking_scaling_*.json` 
3. **Plots**: 
   - Performance vs size curves
   - Implementation comparisons  
   - Distribution analysis
   - Complexity analysis with reference curves
   - Speedup ratios

## Plot Locations

All plots are saved to the `output_dir` specified in your `BenchmarkConfig`:

```
./benchmark_results/ranking/
├── ranking_extended_*.json
├── ranking_extended_size_performance.png
├── ranking_extended_implementation_comparison.png
├── ranking_extended_distribution_analysis.png
├── ranking_extended_complexity_analysis.png
├── ranking_extended_speedup_comparison.png
├── ranking_scaling_*.json
└── ranking_scaling_*.png (same plot types)
```

## Fallback Behavior

If matplotlib/pandas are not available:
- Console output and JSON saving still work
- ASCII plots are generated as `.txt` files
- No visual plots, but you get tabular summaries

## Benefits Achieved

1. **90% Less Boilerplate**: Your 120-line benchmark is now ~20 lines of logic
2. **Automatic Visualization**: No manual plotting code needed
3. **Rich Analysis**: Multiple plot types reveal different performance characteristics
4. **Consistent Output**: All benchmarks use the same format
5. **Easy Extension**: Add new algorithms by just updating `get_implementations()`

Run your ranking benchmark with plotting enabled to see all these visualizations!