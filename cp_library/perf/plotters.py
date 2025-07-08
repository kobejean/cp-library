import cp_library.__header__
import cp_library.perf.__header__
from typing import List, Dict, Optional
from pathlib import Path

try:
    import matplotlib.pyplot as plt
    import pandas as pd
    HAS_PLOTTING = True
except ImportError:
    HAS_PLOTTING = False

class BenchmarkPlotter:
    """Plotting utilities for benchmark results"""
    
    def __init__(self):
        if not HAS_PLOTTING:
            raise ImportError("Plotting requires matplotlib and pandas. Install with: pip install matplotlib pandas")
    
    def plot_results(self, results: List, config):
        """Create standard plots for benchmark results"""
        if not results:
            return
        
        # Convert results to DataFrame
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
            print("No valid results to plot")
            return
        
        df = pd.DataFrame(data)
        
        # Create output directory
        output_dir = Path(config.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\nGenerating plots in {output_dir}/")
        
        # Plot 1: Performance vs Size (if size parameter exists)
        if 'size' in df.columns:
            self._plot_size_performance(df, config.name, output_dir)
        
        # Plot 2: Implementation comparison
        self._plot_implementation_comparison(df, config.name, output_dir)
        
        # Plot 3: Distribution analysis (if multiple test distributions)
        if 'distribution' in df.columns:
            self._plot_distribution_analysis(df, config.name, output_dir)
        
        # Plot 4: Scaling analysis with complexity curves
        if 'size' in df.columns:
            self._plot_complexity_analysis(df, config.name, output_dir)
        
        # Plot 5: Speedup comparison
        self._plot_speedup_comparison(df, config.name, output_dir)
    
    def _plot_size_performance(self, df: pd.DataFrame, name: str, output_dir: Path):
        """Plot performance vs input size"""
        plt.figure(figsize=(10, 6))
        
        for impl in df['implementation'].unique():
            impl_data = df[df['implementation'] == impl]
            
            # Group by size and calculate mean time
            avg_times = impl_data.groupby('size')['time_ms'].agg(['mean', 'std'])
            
            plt.errorbar(
                avg_times.index,
                avg_times['mean'],
                yerr=avg_times['std'],
                marker='o',
                label=impl,
                capsize=5
            )
        
        plt.xlabel('Input Size')
        plt.ylabel('Time (ms)')
        plt.title(f'{name} - Performance vs Size')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.xscale('log')
        plt.yscale('log')
        
        filename = output_dir / f"{name}_size_performance.png"
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"Plot saved: {filename}")
    
    def _plot_implementation_comparison(self, df: pd.DataFrame, name: str, output_dir: Path):
        """Plot implementation comparison"""
        plt.figure(figsize=(12, 6))
        
        # Calculate average time for each implementation
        impl_stats = df.groupby('implementation')['time_ms'].agg(['mean', 'std', 'min', 'max'])
        
        # Bar plot
        x = range(len(impl_stats))
        plt.bar(x, impl_stats['mean'], yerr=impl_stats['std'], capsize=5, alpha=0.7)
        plt.xticks(x, impl_stats.index, rotation=45)
        plt.ylabel('Time (ms)')
        plt.title(f'{name} - Implementation Comparison')
        plt.grid(True, axis='y', alpha=0.3)
        
        # Add value labels
        for i, (idx, row) in enumerate(impl_stats.iterrows()):
            plt.text(i, row['mean'], f'{row["mean"]:.2f}', ha='center', va='bottom')
        
        filename = output_dir / f"{name}_implementation_comparison.png"
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"Plot saved: {filename}")
    
    def _plot_distribution_analysis(self, df: pd.DataFrame, name: str, output_dir: Path):
        """Plot performance across different data distributions"""
        plt.figure(figsize=(12, 8))
        
        distributions = df['distribution'].unique()
        implementations = df['implementation'].unique()
        
        # Create grouped bar plot
        n_dist = len(distributions)
        n_impl = len(implementations)
        width = 0.8 / n_impl
        
        for i, impl in enumerate(implementations):
            impl_data = df[df['implementation'] == impl]
            avg_times = impl_data.groupby('distribution')['time_ms'].mean()
            
            x = [j + i * width for j in range(n_dist)]
            plt.bar(x, [avg_times.get(d, 0) for d in distributions], 
                   width=width, label=impl, alpha=0.8)
        
        plt.xlabel('Data Distribution')
        plt.ylabel('Time (ms)')
        plt.title(f'{name} - Performance by Data Distribution')
        plt.xticks([j + width * (n_impl - 1) / 2 for j in range(n_dist)], 
                   distributions, rotation=45)
        plt.legend()
        plt.grid(True, axis='y', alpha=0.3)
        
        filename = output_dir / f"{name}_distribution_analysis.png"
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"Plot saved: {filename}")
    
    def create_speedup_heatmap(self, df: pd.DataFrame, base_impl: str, name: str, output_dir: Path):
        """Create heatmap showing speedup ratios"""
        # Pivot data to create matrix
        pivot_data = df.pivot_table(
            values='time_ms',
            index='test_case',
            columns='implementation',
            aggfunc='mean'
        )
        
        # Calculate speedup ratios relative to base implementation
        if base_impl in pivot_data.columns:
            speedup = pivot_data.div(pivot_data[base_impl], axis=0)
            
            plt.figure(figsize=(10, 8))
            plt.imshow(speedup.values, aspect='auto', cmap='RdYlGn')
            plt.colorbar(label=f'Speedup vs {base_impl}')
            
            # Add text annotations
            for i in range(len(speedup.index)):
                for j in range(len(speedup.columns)):
                    plt.text(j, i, f'{speedup.values[i, j]:.2f}',
                            ha='center', va='center')
            
            plt.xticks(range(len(speedup.columns)), speedup.columns, rotation=45)
            plt.yticks(range(len(speedup.index)), speedup.index)
            plt.title(f'{name} - Speedup Heatmap')
            plt.tight_layout()
            
            filename = output_dir / f"{name}_speedup_heatmap.png"
            plt.savefig(filename, dpi=150)
            plt.close()
            print(f"Plot saved: {filename}")
    
    def _plot_complexity_analysis(self, df: pd.DataFrame, name: str, output_dir: Path):
        """Plot performance vs size with complexity reference lines"""
        plt.figure(figsize=(12, 8))
        
        for impl in df['implementation'].unique():
            impl_data = df[df['implementation'] == impl]
            
            if 'size' in impl_data.columns:
                # Group by size and calculate mean time
                avg_times = impl_data.groupby('size')['time_ms'].mean()
                sizes = avg_times.index.values
                times = avg_times.values
                
                plt.loglog(sizes, times, 'o-', label=impl, linewidth=2, markersize=6)
        
        # Add complexity reference lines
        if len(df['size'].unique()) > 2:
            min_size = df['size'].min()
            max_size = df['size'].max()
            ref_sizes = [s for s in [100, 1000, 10000, 100000] if min_size <= s <= max_size]
            
            if ref_sizes:
                base_time = 0.001  # 1 microsecond base time
                
                # O(n) reference
                linear_times = [base_time * s / ref_sizes[0] for s in ref_sizes]
                plt.loglog(ref_sizes, linear_times, '--', alpha=0.5, color='gray', label='O(n)')
                
                # O(n log n) reference  
                nlogn_times = [base_time * s * 20 / (ref_sizes[0] * 20) for s in ref_sizes]  # log approximation
                plt.loglog(ref_sizes, nlogn_times, ':', alpha=0.5, color='gray', label='O(n log n)')
        
        plt.xlabel('Input Size')
        plt.ylabel('Time (ms)')
        plt.title(f'{name} - Complexity Analysis')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        filename = output_dir / f"{name}_complexity_analysis.png"
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"Plot saved: {filename}")
    
    def _plot_speedup_comparison(self, df: pd.DataFrame, name: str, output_dir: Path):
        """Plot speedup ratios between implementations"""
        implementations = df['implementation'].unique()
        
        if len(implementations) < 2:
            return
        
        plt.figure(figsize=(12, 6))
        
        # Use first implementation as baseline
        baseline = implementations[0]
        
        for i, other_impl in enumerate(implementations[1:], 1):
            speedups = []
            test_cases = []
            
            # Calculate speedup for each test case
            for test_case in df['test_case'].unique():
                baseline_time = df[(df['implementation'] == baseline) & 
                                 (df['test_case'] == test_case)]['time_ms'].mean()
                other_time = df[(df['implementation'] == other_impl) & 
                               (df['test_case'] == test_case)]['time_ms'].mean()
                
                if baseline_time > 0 and other_time > 0:
                    speedup = baseline_time / other_time
                    speedups.append(speedup)
                    test_cases.append(test_case)
            
            if speedups:
                x = range(len(speedups))
                bars = plt.bar([xi + i*0.4 for xi in x], speedups, 
                              width=0.4, label=f'{other_impl} vs {baseline}', alpha=0.7)
                
                # Add horizontal line at 1.0 (no speedup)
                plt.axhline(y=1.0, color='red', linestyle='--', alpha=0.5)
                
                # Color bars based on speedup
                for bar, speedup in zip(bars, speedups):
                    if speedup > 1.0:
                        bar.set_color('green')
                    else:
                        bar.set_color('red')
        
        plt.xlabel('Test Cases')
        plt.ylabel('Speedup Ratio')
        plt.title(f'{name} - Speedup Comparison')
        plt.xticks([xi + 0.2 for xi in range(len(test_cases))], 
                   [tc[:20] + '...' if len(tc) > 20 else tc for tc in test_cases], 
                   rotation=45, ha='right')
        plt.legend()
        plt.grid(True, axis='y', alpha=0.3)
        plt.tight_layout()
        
        filename = output_dir / f"{name}_speedup_comparison.png"
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"Plot saved: {filename}")