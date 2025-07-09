import cp_library.__header__
import cp_library.perf.__header__
"""Simple ASCII plotting for when matplotlib is not available"""

from typing import List, Dict, Any
from pathlib import Path
import json

class ASCIIPlotter:
    """Create simple ASCII plots when matplotlib is not available"""
    
    def plot_results(self, results: List, config):
        """Create ASCII plots for benchmark results"""
        if not results:
            return
            
        # Convert results to data
        data = []
        for r in results:
            if r.time_ms != float('inf'):
                row = {
                    'implementation': r.implementation,
                    'time_ms': r.time_ms,
                    'test_case': r.test_case.name
                }
                row.update(r.test_case.params)
                data.append(row)
        
        if not data:
            return
        
        # Create output directory
        output_dir = Path(config.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\nGenerating ASCII plots in {output_dir}/")
        
        # Create size vs performance plot
        if any('size' in row for row in data):
            self._create_size_plot(data, config.name, output_dir)
        
        # Create implementation comparison
        self._create_comparison_table(data, config.name, output_dir)
    
    def _create_size_plot(self, data: List[Dict], name: str, output_dir: Path):
        """Create ASCII plot of performance vs size"""
        # Group by implementation and size
        impl_data = {}
        for row in data:
            if 'size' in row:
                impl = row['implementation']
                size = row['size']
                time_ms = row['time_ms']
                
                if impl not in impl_data:
                    impl_data[impl] = {}
                if size not in impl_data[impl]:
                    impl_data[impl][size] = []
                impl_data[impl][size].append(time_ms)
        
        # Calculate averages
        for impl in impl_data:
            for size in impl_data[impl]:
                impl_data[impl][size] = sum(impl_data[impl][size]) / len(impl_data[impl][size])
        
        # Create ASCII plot
        plot_lines = []
        plot_lines.append(f"Performance vs Size - {name}")
        plot_lines.append("=" * 50)
        plot_lines.append("")
        
        if impl_data:
            # Get all sizes
            all_sizes = set()
            for impl in impl_data:
                all_sizes.update(impl_data[impl].keys())
            all_sizes = sorted(all_sizes)
            
            # Create table
            plot_lines.append(f"{'Size':<12} " + "".join(f"{impl:<15}" for impl in impl_data.keys()))
            plot_lines.append("-" * (12 + 15 * len(impl_data)))
            
            for size in all_sizes:
                line = f"{size:<12} "
                for impl in impl_data.keys():
                    time_val = impl_data[impl].get(size, 0)
                    line += f"{time_val:<15.3f}"
                plot_lines.append(line)
        
        # Save to file
        filename = output_dir / f"{name}_size_plot.txt"
        with open(filename, 'w') as f:
            f.write('\n'.join(plot_lines))
        print(f"ASCII plot saved: {filename}")
    
    def _create_comparison_table(self, data: List[Dict], name: str, output_dir: Path):
        """Create comparison table"""
        # Group by implementation
        impl_times = {}
        for row in data:
            impl = row['implementation']
            if impl not in impl_times:
                impl_times[impl] = []
            impl_times[impl].append(row['time_ms'])
        
        # Calculate statistics
        stats = {}
        for impl, times in impl_times.items():
            stats[impl] = {
                'mean': sum(times) / len(times),
                'min': min(times),
                'max': max(times),
                'count': len(times)
            }
        
        # Create comparison table
        table_lines = []
        table_lines.append(f"Implementation Comparison - {name}")
        table_lines.append("=" * 60)
        table_lines.append("")
        table_lines.append(f"{'Implementation':<20} {'Mean (ms)':<12} {'Min (ms)':<12} {'Max (ms)':<12} {'Count':<8}")
        table_lines.append("-" * 68)
        
        for impl, stat in stats.items():
            table_lines.append(
                f"{impl:<20} {stat['mean']:<12.3f} {stat['min']:<12.3f} "
                f"{stat['max']:<12.3f} {stat['count']:<8}"
            )
        
        # Calculate speedup if 2 implementations
        if len(stats) == 2:
            impls = list(stats.keys())
            ratio = stats[impls[0]]['mean'] / stats[impls[1]]['mean']
            faster = impls[1] if ratio > 1 else impls[0]
            speedup = max(ratio, 1/ratio)
            
            table_lines.append("")
            table_lines.append(f"{faster} is {speedup:.2f}x faster on average")
        
        # Save to file
        filename = output_dir / f"{name}_comparison.txt"
        with open(filename, 'w') as f:
            f.write('\n'.join(table_lines))
        print(f"Comparison table saved: {filename}")

# Enhanced benchmark class that falls back to ASCII plots
def enhanced_plot_results(self):
    """Enhanced plot_results method with ASCII fallback"""
    try:
        from .plotters import BenchmarkPlotter
        plotter = BenchmarkPlotter()
        plotter.plot_results(self.results, self.config)
    except ImportError:
        # Fall back to ASCII plots
        ascii_plotter = ASCIIPlotter()
        ascii_plotter.plot_results(self.results, self.config)
        print("Used ASCII plots (install matplotlib/pandas for visual plots)")
    except Exception as e:
        print(f"Plotting failed: {e}")

# Monkey patch the Benchmark class
if __name__ != "__main__":
    from .benchmark import Benchmark
    Benchmark.plot_results = enhanced_plot_results