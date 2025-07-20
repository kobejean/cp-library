"""
Plot rendering implementations following Open/Closed Principle.
"""

import statistics
from collections import defaultdict
from pathlib import Path
from typing import List, Dict, Any
from cp_library.perf.interfaces import PlotRenderer, BenchmarkResult


class PlotDataProcessor:
    """Utility class for processing benchmark data for plotting"""
    
    @staticmethod
    def group_by_operation(results: List[BenchmarkResult]) -> Dict[str, List[BenchmarkResult]]:
        """Group results by operation"""
        grouped = defaultdict(list)
        for result in results:
            if result.error is None and result.time_ms != float('inf'):
                grouped[result.operation].append(result)
        return dict(grouped)
    
    @staticmethod
    def group_by_implementation_and_size(results: List[BenchmarkResult]) -> Dict[str, Dict[int, float]]:
        """Group results by implementation and size"""
        grouped = defaultdict(lambda: defaultdict(float))
        for result in results:
            if result.error is None and result.time_ms != float('inf'):
                grouped[result.implementation][result.size] = result.time_ms
        return dict(grouped)
    
    @staticmethod
    def calculate_statistics(results: List[BenchmarkResult]) -> Dict[str, Dict[str, float]]:
        """Calculate statistics for each implementation"""
        impl_times = defaultdict(list)
        for result in results:
            if result.error is None and result.time_ms != float('inf'):
                impl_times[result.implementation].append(result.time_ms)
        
        stats = {}
        for impl, times in impl_times.items():
            if times:
                stats[impl] = {
                    'mean': statistics.mean(times),
                    'min': min(times),
                    'max': max(times),
                    'count': len(times)
                }
        return stats


class MatplotlibRenderer(PlotRenderer):
    """Matplotlib-based plot renderer"""
    
    def __init__(self, plot_scale: str = "loglog"):
        self.plot_scale = plot_scale
        self._matplotlib_available = None
    
    def can_render(self) -> bool:
        """Check if matplotlib is available"""
        if self._matplotlib_available is None:
            try:
                import matplotlib.pyplot as plt
                self._matplotlib_available = True
            except ImportError:
                self._matplotlib_available = False
        return self._matplotlib_available
    
    def create_plots(self, results: List[BenchmarkResult], config: Any) -> None:
        """Create matplotlib plots from benchmark results"""
        if not self.can_render():
            return
        
        import matplotlib.pyplot as plt
        
        operations = PlotDataProcessor.group_by_operation(results)
        output_dir = Path(getattr(config, 'output_dir', './output/benchmark_results'))
        name = getattr(config, 'name', 'benchmark')
        
        for operation, op_results in operations.items():
            self._create_performance_plot(plt, op_results, operation, output_dir, name)
            self._create_speedup_plot(plt, op_results, operation, output_dir, name)
    
    def _create_performance_plot(self, plt, results: List[BenchmarkResult], 
                                operation: str, output_dir: Path, name: str) -> None:
        """Create performance vs size plot"""
        data = PlotDataProcessor.group_by_implementation_and_size(results)
        
        plt.figure(figsize=(10, 6))
        
        for impl, size_times in data.items():
            sizes = sorted(size_times.keys())
            times = [size_times[size] for size in sizes]
            plt.plot(sizes, times, marker='o', label=impl)
        
        if self.plot_scale == "loglog":
            plt.loglog()
        elif self.plot_scale == "semilogx":
            plt.semilogx()
        elif self.plot_scale == "semilogy":
            plt.semilogy()
        
        plt.xlabel('Size')
        plt.ylabel('Time (ms)')
        plt.title(f'Performance vs Size - {name} - {operation}')
        plt.legend()
        plt.grid(True)
        
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = output_dir / f"{name}_{operation}_performance.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Plot saved: {filename}")
    
    def _create_speedup_plot(self, plt, results: List[BenchmarkResult], 
                           operation: str, output_dir: Path, name: str) -> None:
        """Create speedup vs size line plot"""
        data = PlotDataProcessor.group_by_implementation_and_size(results)
        
        if len(data) < 2:
            return  # Need at least 2 implementations for speedup
        
        # Get all sizes and sort them
        all_sizes = set()
        for size_times in data.values():
            all_sizes.update(size_times.keys())
        sizes = sorted(all_sizes)
        
        # Find baseline (slowest implementation at each size)
        baseline_times = {}
        for size in sizes:
            size_times = []
            for impl, impl_data in data.items():
                if size in impl_data:
                    size_times.append(impl_data[size])
            if size_times:
                baseline_times[size] = max(size_times)  # Slowest time as baseline
        
        plt.figure(figsize=(10, 6))
        
        # Plot speedup line for each implementation
        for impl, size_times in data.items():
            impl_sizes = []
            speedups = []
            
            for size in sizes:
                if size in size_times and size in baseline_times:
                    speedup = baseline_times[size] / size_times[size]
                    impl_sizes.append(size)
                    speedups.append(speedup)
            
            if impl_sizes:  # Only plot if we have data
                plt.plot(impl_sizes, speedups, marker='o', label=impl, linewidth=2)
        
        if self.plot_scale == "loglog":
            plt.loglog()
        elif self.plot_scale == "semilogx":
            plt.semilogx()
        elif self.plot_scale == "semilogy":
            plt.semilogy()
        
        plt.xlabel('Size')
        plt.ylabel('Speedup (relative to slowest)')
        plt.title(f'Speedup vs Size - {name} - {operation}')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Add horizontal line at speedup = 1.0
        plt.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5, label='Baseline')
        
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = output_dir / f"{name}_{operation}_speedup.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Plot saved: {filename}")


class ASCIIRenderer(PlotRenderer):
    """ASCII-based plot renderer (fallback when matplotlib unavailable)"""
    
    def can_render(self) -> bool:
        """ASCII renderer is always available"""
        return True
    
    def create_plots(self, results: List[BenchmarkResult], config: Any) -> None:
        """Create ASCII plots from benchmark results"""
        operations = PlotDataProcessor.group_by_operation(results)
        output_dir = Path(getattr(config, 'output_dir', './output/benchmark_results'))
        name = getattr(config, 'name', 'benchmark')
        
        print("\nGenerating ASCII plots in", output_dir)
        
        for operation, op_results in operations.items():
            self._create_ascii_performance_plot(op_results, operation, output_dir, name)
            self._create_ascii_speedup_plot(op_results, operation, output_dir, name)
            self._create_ascii_comparison_table(op_results, operation, output_dir, name)
    
    def _create_ascii_performance_plot(self, results: List[BenchmarkResult], 
                                     operation: str, output_dir: Path, name: str) -> None:
        """Create ASCII performance vs size plot"""
        data = PlotDataProcessor.group_by_implementation_and_size(results)
        
        if not data:
            return
        
        # Get all sizes and sort them
        all_sizes = set()
        for size_times in data.values():
            all_sizes.update(size_times.keys())
        sizes = sorted(all_sizes)
        
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = output_dir / f"{name}_{operation}_size_plot.txt"
        
        with open(filename, 'w') as f:
            f.write(f"Performance vs Size - {name} - {operation}\n")
            f.write("=" * 60 + "\n\n")
            
            # Header
            header = f"{'Size':<12}"
            for impl in sorted(data.keys()):
                header += f"{impl:<15}"
            f.write(header + "\n")
            f.write("-" * len(header) + "\n")
            
            # Data rows
            for size in sizes:
                row = f"{size:<12}"
                for impl in sorted(data.keys()):
                    time_val = data[impl].get(size, 0)
                    if time_val > 0:
                        row += f"{time_val:<15.3f}"
                    else:
                        row += f"{'---':<15}"
                f.write(row + "\n")
        
        print(f"ASCII plot saved: {filename}")
    
    def _create_ascii_speedup_plot(self, results: List[BenchmarkResult], 
                                 operation: str, output_dir: Path, name: str) -> None:
        """Create ASCII speedup vs size plot"""
        data = PlotDataProcessor.group_by_implementation_and_size(results)
        
        if len(data) < 2:
            return  # Need at least 2 implementations for speedup
        
        # Get all sizes and sort them
        all_sizes = set()
        for size_times in data.values():
            all_sizes.update(size_times.keys())
        sizes = sorted(all_sizes)
        
        # Find baseline (slowest implementation at each size)
        baseline_times = {}
        for size in sizes:
            size_times = []
            for impl, impl_data in data.items():
                if size in impl_data:
                    size_times.append(impl_data[size])
            if size_times:
                baseline_times[size] = max(size_times)  # Slowest time as baseline
        
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = output_dir / f"{name}_{operation}_speedup_plot.txt"
        
        with open(filename, 'w') as f:
            f.write(f"Speedup vs Size - {name} - {operation}\n")
            f.write("=" * 60 + "\n\n")
            
            # Header
            header = f"{'Size':<12}"
            for impl in sorted(data.keys()):
                header += f"{impl:<15}"
            f.write(header + "\n")
            f.write("-" * len(header) + "\n")
            
            # Data rows
            for size in sizes:
                if size not in baseline_times:
                    continue
                
                row = f"{size:<12}"
                for impl in sorted(data.keys()):
                    if size in data[impl]:
                        speedup = baseline_times[size] / data[impl][size]
                        row += f"{speedup:<15.2f}"
                    else:
                        row += f"{'---':<15}"
                f.write(row + "\n")
        
        print(f"ASCII speedup plot saved: {filename}")
    
    def _create_ascii_comparison_table(self, results: List[BenchmarkResult], 
                                     operation: str, output_dir: Path, name: str) -> None:
        """Create ASCII comparison table"""
        stats = PlotDataProcessor.calculate_statistics(results)
        
        if not stats:
            return
        
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = output_dir / f"{name}_{operation}_comparison.txt"
        
        with open(filename, 'w') as f:
            f.write(f"Implementation Comparison - {name} - {operation}\n")
            f.write("=" * 70 + "\n\n")
            
            # Header
            header = f"{'Implementation':<20} {'Mean (ms)':<12} {'Min (ms)':<12} {'Max (ms)':<12} {'Count':<8}"
            f.write(header + "\n")
            f.write("-" * len(header) + "\n")
            
            # Sort by mean time
            sorted_stats = sorted(stats.items(), key=lambda x: x[1]['mean'])
            
            # Data rows
            for impl, stat in sorted_stats:
                row = (f"{impl:<20} {stat['mean']:<12.3f} {stat['min']:<12.3f} "
                      f"{stat['max']:<12.3f} {stat['count']:<8}")
                f.write(row + "\n")
        
        print(f"Comparison table saved: {filename}")


class CompositeRenderer(PlotRenderer):
    """Composite renderer that tries matplotlib first, falls back to ASCII"""
    
    def __init__(self, plot_scale: str = "loglog"):
        self.matplotlib_renderer = MatplotlibRenderer(plot_scale)
        self.ascii_renderer = ASCIIRenderer()
    
    def can_render(self) -> bool:
        """Composite renderer can always render (ASCII fallback)"""
        return True
    
    def create_plots(self, results: List[BenchmarkResult], config: Any) -> None:
        """Create plots using matplotlib if available, ASCII otherwise"""
        if self.matplotlib_renderer.can_render():
            self.matplotlib_renderer.create_plots(results, config)
        else:
            print("Matplotlib not available - using ASCII plots")
            self.ascii_renderer.create_plots(results, config)