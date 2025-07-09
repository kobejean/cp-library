---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/perf/benchmark.py
    title: cp_library/perf/benchmark.py
  - icon: ':warning:'
    path: cp_library/perf/examples/rank_benchmark.py
    title: cp_library/perf/examples/rank_benchmark.py
  - icon: ':warning:'
    path: cp_library/perf/examples/simple_usage.py
    title: cp_library/perf/examples/simple_usage.py
  - icon: ':warning:'
    path: cp_library/perf/simple_plots.py
    title: cp_library/perf/simple_plots.py
  - icon: ':warning:'
    path: perf/bool_list_benchmark.py
    title: perf/bool_list_benchmark.py
  - icon: ':warning:'
    path: perf/rank_perf.py
    title: perf/rank_perf.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nfrom typing import List, Dict, Optional\nfrom pathlib import Path\n\ntry:\n\
    \    import matplotlib.pyplot as plt\n    import pandas as pd\n    HAS_PLOTTING\
    \ = True\nexcept ImportError:\n    HAS_PLOTTING = False\n\nclass BenchmarkPlotter:\n\
    \    \"\"\"Plotting utilities for benchmark results\"\"\"\n    \n    def __init__(self):\n\
    \        if not HAS_PLOTTING:\n            raise ImportError(\"Plotting requires\
    \ matplotlib and pandas. Install with: pip install matplotlib pandas\")\n    \n\
    \    def plot_results(self, results: List, config):\n        \"\"\"Create standard\
    \ plots for benchmark results\"\"\"\n        if not results:\n            return\n\
    \        \n        # Convert results to DataFrame\n        data = []\n       \
    \ for r in results:\n            if r.time_ms != float('inf'):\n             \
    \   row = {\n                    'implementation': r.implementation,\n       \
    \             'time_ms': r.time_ms,\n                    'test_case': r.test_case.name\n\
    \                }\n                row.update(r.test_case.params)\n         \
    \       data.append(row)\n        \n        if not data:\n            print(\"\
    No valid results to plot\")\n            return\n        \n        df = pd.DataFrame(data)\n\
    \        \n        # Create output directory\n        output_dir = Path(config.output_dir)\n\
    \        output_dir.mkdir(parents=True, exist_ok=True)\n        \n        print(f\"\
    \\nGenerating plots in {output_dir}/\")\n        \n        # Plot 1: Performance\
    \ vs Size (if size parameter exists)\n        if 'size' in df.columns:\n     \
    \       self._plot_size_performance(df, config.name, output_dir)\n        \n \
    \       # Plot 2: Implementation comparison\n        self._plot_implementation_comparison(df,\
    \ config.name, output_dir)\n        \n        # Plot 3: Distribution analysis\
    \ (if multiple test distributions)\n        if 'distribution' in df.columns:\n\
    \            self._plot_distribution_analysis(df, config.name, output_dir)\n \
    \       \n        # Plot 4: Scaling analysis with complexity curves\n        if\
    \ 'size' in df.columns:\n            self._plot_complexity_analysis(df, config.name,\
    \ output_dir)\n        \n        # Plot 5: Speedup comparison\n        self._plot_speedup_comparison(df,\
    \ config.name, output_dir)\n    \n    def _plot_size_performance(self, df: pd.DataFrame,\
    \ name: str, output_dir: Path):\n        \"\"\"Plot performance vs input size\"\
    \"\"\n        plt.figure(figsize=(10, 6))\n        \n        for impl in df['implementation'].unique():\n\
    \            impl_data = df[df['implementation'] == impl]\n            \n    \
    \        # Group by size and calculate mean time\n            avg_times = impl_data.groupby('size')['time_ms'].agg(['mean',\
    \ 'std'])\n            \n            plt.errorbar(\n                avg_times.index,\n\
    \                avg_times['mean'],\n                yerr=avg_times['std'],\n\
    \                marker='o',\n                label=impl,\n                capsize=5\n\
    \            )\n        \n        plt.xlabel('Input Size')\n        plt.ylabel('Time\
    \ (ms)')\n        plt.title(f'{name} - Performance vs Size')\n        plt.legend()\n\
    \        plt.grid(True, alpha=0.3)\n        plt.xscale('log')\n        plt.yscale('log')\n\
    \        \n        filename = output_dir / f\"{name}_size_performance.png\"\n\
    \        plt.savefig(filename, dpi=150, bbox_inches='tight')\n        plt.close()\n\
    \        print(f\"Plot saved: {filename}\")\n    \n    def _plot_implementation_comparison(self,\
    \ df: pd.DataFrame, name: str, output_dir: Path):\n        \"\"\"Plot implementation\
    \ comparison\"\"\"\n        plt.figure(figsize=(12, 6))\n        \n        # Calculate\
    \ average time for each implementation\n        impl_stats = df.groupby('implementation')['time_ms'].agg(['mean',\
    \ 'std', 'min', 'max'])\n        \n        # Bar plot\n        x = range(len(impl_stats))\n\
    \        plt.bar(x, impl_stats['mean'], yerr=impl_stats['std'], capsize=5, alpha=0.7)\n\
    \        plt.xticks(x, impl_stats.index, rotation=45)\n        plt.ylabel('Time\
    \ (ms)')\n        plt.title(f'{name} - Implementation Comparison')\n        plt.grid(True,\
    \ axis='y', alpha=0.3)\n        \n        # Add value labels\n        for i, (idx,\
    \ row) in enumerate(impl_stats.iterrows()):\n            plt.text(i, row['mean'],\
    \ f'{row[\"mean\"]:.2f}', ha='center', va='bottom')\n        \n        filename\
    \ = output_dir / f\"{name}_implementation_comparison.png\"\n        plt.savefig(filename,\
    \ dpi=150, bbox_inches='tight')\n        plt.close()\n        print(f\"Plot saved:\
    \ {filename}\")\n    \n    def _plot_distribution_analysis(self, df: pd.DataFrame,\
    \ name: str, output_dir: Path):\n        \"\"\"Plot performance across different\
    \ data distributions\"\"\"\n        plt.figure(figsize=(12, 8))\n        \n  \
    \      distributions = df['distribution'].unique()\n        implementations =\
    \ df['implementation'].unique()\n        \n        # Create grouped bar plot\n\
    \        n_dist = len(distributions)\n        n_impl = len(implementations)\n\
    \        width = 0.8 / n_impl\n        \n        for i, impl in enumerate(implementations):\n\
    \            impl_data = df[df['implementation'] == impl]\n            avg_times\
    \ = impl_data.groupby('distribution')['time_ms'].mean()\n            \n      \
    \      x = [j + i * width for j in range(n_dist)]\n            plt.bar(x, [avg_times.get(d,\
    \ 0) for d in distributions], \n                   width=width, label=impl, alpha=0.8)\n\
    \        \n        plt.xlabel('Data Distribution')\n        plt.ylabel('Time (ms)')\n\
    \        plt.title(f'{name} - Performance by Data Distribution')\n        plt.xticks([j\
    \ + width * (n_impl - 1) / 2 for j in range(n_dist)], \n                   distributions,\
    \ rotation=45)\n        plt.legend()\n        plt.grid(True, axis='y', alpha=0.3)\n\
    \        \n        filename = output_dir / f\"{name}_distribution_analysis.png\"\
    \n        plt.savefig(filename, dpi=150, bbox_inches='tight')\n        plt.close()\n\
    \        print(f\"Plot saved: {filename}\")\n    \n    def create_speedup_heatmap(self,\
    \ df: pd.DataFrame, base_impl: str, name: str, output_dir: Path):\n        \"\"\
    \"Create heatmap showing speedup ratios\"\"\"\n        # Pivot data to create\
    \ matrix\n        pivot_data = df.pivot_table(\n            values='time_ms',\n\
    \            index='test_case',\n            columns='implementation',\n     \
    \       aggfunc='mean'\n        )\n        \n        # Calculate speedup ratios\
    \ relative to base implementation\n        if base_impl in pivot_data.columns:\n\
    \            speedup = pivot_data.div(pivot_data[base_impl], axis=0)\n       \
    \     \n            plt.figure(figsize=(10, 8))\n            plt.imshow(speedup.values,\
    \ aspect='auto', cmap='RdYlGn')\n            plt.colorbar(label=f'Speedup vs {base_impl}')\n\
    \            \n            # Add text annotations\n            for i in range(len(speedup.index)):\n\
    \                for j in range(len(speedup.columns)):\n                    plt.text(j,\
    \ i, f'{speedup.values[i, j]:.2f}',\n                            ha='center',\
    \ va='center')\n            \n            plt.xticks(range(len(speedup.columns)),\
    \ speedup.columns, rotation=45)\n            plt.yticks(range(len(speedup.index)),\
    \ speedup.index)\n            plt.title(f'{name} - Speedup Heatmap')\n       \
    \     plt.tight_layout()\n            \n            filename = output_dir / f\"\
    {name}_speedup_heatmap.png\"\n            plt.savefig(filename, dpi=150)\n   \
    \         plt.close()\n            print(f\"Plot saved: {filename}\")\n    \n\
    \    def _plot_complexity_analysis(self, df: pd.DataFrame, name: str, output_dir:\
    \ Path):\n        \"\"\"Plot performance vs size with complexity reference lines\"\
    \"\"\n        plt.figure(figsize=(12, 8))\n        \n        for impl in df['implementation'].unique():\n\
    \            impl_data = df[df['implementation'] == impl]\n            \n    \
    \        if 'size' in impl_data.columns:\n                # Group by size and\
    \ calculate mean time\n                avg_times = impl_data.groupby('size')['time_ms'].mean()\n\
    \                sizes = avg_times.index.values\n                times = avg_times.values\n\
    \                \n                plt.loglog(sizes, times, 'o-', label=impl,\
    \ linewidth=2, markersize=6)\n        \n        # Add complexity reference lines\n\
    \        if len(df['size'].unique()) > 2:\n            min_size = df['size'].min()\n\
    \            max_size = df['size'].max()\n            ref_sizes = [s for s in\
    \ [100, 1000, 10000, 100000] if min_size <= s <= max_size]\n            \n   \
    \         if ref_sizes:\n                base_time = 0.001  # 1 microsecond base\
    \ time\n                \n                # O(n) reference\n                linear_times\
    \ = [base_time * s / ref_sizes[0] for s in ref_sizes]\n                plt.loglog(ref_sizes,\
    \ linear_times, '--', alpha=0.5, color='gray', label='O(n)')\n               \
    \ \n                # O(n log n) reference  \n                nlogn_times = [base_time\
    \ * s * 20 / (ref_sizes[0] * 20) for s in ref_sizes]  # log approximation\n  \
    \              plt.loglog(ref_sizes, nlogn_times, ':', alpha=0.5, color='gray',\
    \ label='O(n log n)')\n        \n        plt.xlabel('Input Size')\n        plt.ylabel('Time\
    \ (ms)')\n        plt.title(f'{name} - Complexity Analysis')\n        plt.legend()\n\
    \        plt.grid(True, alpha=0.3)\n        \n        filename = output_dir /\
    \ f\"{name}_complexity_analysis.png\"\n        plt.savefig(filename, dpi=150,\
    \ bbox_inches='tight')\n        plt.close()\n        print(f\"Plot saved: {filename}\"\
    )\n    \n    def _plot_speedup_comparison(self, df: pd.DataFrame, name: str, output_dir:\
    \ Path):\n        \"\"\"Plot speedup ratios between implementations\"\"\"\n  \
    \      implementations = df['implementation'].unique()\n        \n        if len(implementations)\
    \ < 2:\n            return\n        \n        plt.figure(figsize=(12, 6))\n  \
    \      \n        # Use first implementation as baseline\n        baseline = implementations[0]\n\
    \        \n        for i, other_impl in enumerate(implementations[1:], 1):\n \
    \           speedups = []\n            test_cases = []\n            \n       \
    \     # Calculate speedup for each test case\n            for test_case in df['test_case'].unique():\n\
    \                baseline_time = df[(df['implementation'] == baseline) & \n  \
    \                               (df['test_case'] == test_case)]['time_ms'].mean()\n\
    \                other_time = df[(df['implementation'] == other_impl) & \n   \
    \                            (df['test_case'] == test_case)]['time_ms'].mean()\n\
    \                \n                if baseline_time > 0 and other_time > 0:\n\
    \                    speedup = baseline_time / other_time\n                  \
    \  speedups.append(speedup)\n                    test_cases.append(test_case)\n\
    \            \n            if speedups:\n                x = range(len(speedups))\n\
    \                bars = plt.bar([xi + i*0.4 for xi in x], speedups, \n       \
    \                       width=0.4, label=f'{other_impl} vs {baseline}', alpha=0.7)\n\
    \                \n                # Add horizontal line at 1.0 (no speedup)\n\
    \                plt.axhline(y=1.0, color='red', linestyle='--', alpha=0.5)\n\
    \                \n                # Color bars based on speedup\n           \
    \     for bar, speedup in zip(bars, speedups):\n                    if speedup\
    \ > 1.0:\n                        bar.set_color('green')\n                   \
    \ else:\n                        bar.set_color('red')\n        \n        plt.xlabel('Test\
    \ Cases')\n        plt.ylabel('Speedup Ratio')\n        plt.title(f'{name} - Speedup\
    \ Comparison')\n        plt.xticks([xi + 0.2 for xi in range(len(test_cases))],\
    \ \n                   [tc[:20] + '...' if len(tc) > 20 else tc for tc in test_cases],\
    \ \n                   rotation=45, ha='right')\n        plt.legend()\n      \
    \  plt.grid(True, axis='y', alpha=0.3)\n        plt.tight_layout()\n        \n\
    \        filename = output_dir / f\"{name}_speedup_comparison.png\"\n        plt.savefig(filename,\
    \ dpi=150, bbox_inches='tight')\n        plt.close()\n        print(f\"Plot saved:\
    \ {filename}\")\n"
  code: "import cp_library.__header__\nimport cp_library.perf.__header__\nfrom typing\
    \ import List, Dict, Optional\nfrom pathlib import Path\n\ntry:\n    import matplotlib.pyplot\
    \ as plt\n    import pandas as pd\n    HAS_PLOTTING = True\nexcept ImportError:\n\
    \    HAS_PLOTTING = False\n\nclass BenchmarkPlotter:\n    \"\"\"Plotting utilities\
    \ for benchmark results\"\"\"\n    \n    def __init__(self):\n        if not HAS_PLOTTING:\n\
    \            raise ImportError(\"Plotting requires matplotlib and pandas. Install\
    \ with: pip install matplotlib pandas\")\n    \n    def plot_results(self, results:\
    \ List, config):\n        \"\"\"Create standard plots for benchmark results\"\"\
    \"\n        if not results:\n            return\n        \n        # Convert results\
    \ to DataFrame\n        data = []\n        for r in results:\n            if r.time_ms\
    \ != float('inf'):\n                row = {\n                    'implementation':\
    \ r.implementation,\n                    'time_ms': r.time_ms,\n             \
    \       'test_case': r.test_case.name\n                }\n                row.update(r.test_case.params)\n\
    \                data.append(row)\n        \n        if not data:\n          \
    \  print(\"No valid results to plot\")\n            return\n        \n       \
    \ df = pd.DataFrame(data)\n        \n        # Create output directory\n     \
    \   output_dir = Path(config.output_dir)\n        output_dir.mkdir(parents=True,\
    \ exist_ok=True)\n        \n        print(f\"\\nGenerating plots in {output_dir}/\"\
    )\n        \n        # Plot 1: Performance vs Size (if size parameter exists)\n\
    \        if 'size' in df.columns:\n            self._plot_size_performance(df,\
    \ config.name, output_dir)\n        \n        # Plot 2: Implementation comparison\n\
    \        self._plot_implementation_comparison(df, config.name, output_dir)\n \
    \       \n        # Plot 3: Distribution analysis (if multiple test distributions)\n\
    \        if 'distribution' in df.columns:\n            self._plot_distribution_analysis(df,\
    \ config.name, output_dir)\n        \n        # Plot 4: Scaling analysis with\
    \ complexity curves\n        if 'size' in df.columns:\n            self._plot_complexity_analysis(df,\
    \ config.name, output_dir)\n        \n        # Plot 5: Speedup comparison\n \
    \       self._plot_speedup_comparison(df, config.name, output_dir)\n    \n   \
    \ def _plot_size_performance(self, df: pd.DataFrame, name: str, output_dir: Path):\n\
    \        \"\"\"Plot performance vs input size\"\"\"\n        plt.figure(figsize=(10,\
    \ 6))\n        \n        for impl in df['implementation'].unique():\n        \
    \    impl_data = df[df['implementation'] == impl]\n            \n            #\
    \ Group by size and calculate mean time\n            avg_times = impl_data.groupby('size')['time_ms'].agg(['mean',\
    \ 'std'])\n            \n            plt.errorbar(\n                avg_times.index,\n\
    \                avg_times['mean'],\n                yerr=avg_times['std'],\n\
    \                marker='o',\n                label=impl,\n                capsize=5\n\
    \            )\n        \n        plt.xlabel('Input Size')\n        plt.ylabel('Time\
    \ (ms)')\n        plt.title(f'{name} - Performance vs Size')\n        plt.legend()\n\
    \        plt.grid(True, alpha=0.3)\n        plt.xscale('log')\n        plt.yscale('log')\n\
    \        \n        filename = output_dir / f\"{name}_size_performance.png\"\n\
    \        plt.savefig(filename, dpi=150, bbox_inches='tight')\n        plt.close()\n\
    \        print(f\"Plot saved: {filename}\")\n    \n    def _plot_implementation_comparison(self,\
    \ df: pd.DataFrame, name: str, output_dir: Path):\n        \"\"\"Plot implementation\
    \ comparison\"\"\"\n        plt.figure(figsize=(12, 6))\n        \n        # Calculate\
    \ average time for each implementation\n        impl_stats = df.groupby('implementation')['time_ms'].agg(['mean',\
    \ 'std', 'min', 'max'])\n        \n        # Bar plot\n        x = range(len(impl_stats))\n\
    \        plt.bar(x, impl_stats['mean'], yerr=impl_stats['std'], capsize=5, alpha=0.7)\n\
    \        plt.xticks(x, impl_stats.index, rotation=45)\n        plt.ylabel('Time\
    \ (ms)')\n        plt.title(f'{name} - Implementation Comparison')\n        plt.grid(True,\
    \ axis='y', alpha=0.3)\n        \n        # Add value labels\n        for i, (idx,\
    \ row) in enumerate(impl_stats.iterrows()):\n            plt.text(i, row['mean'],\
    \ f'{row[\"mean\"]:.2f}', ha='center', va='bottom')\n        \n        filename\
    \ = output_dir / f\"{name}_implementation_comparison.png\"\n        plt.savefig(filename,\
    \ dpi=150, bbox_inches='tight')\n        plt.close()\n        print(f\"Plot saved:\
    \ {filename}\")\n    \n    def _plot_distribution_analysis(self, df: pd.DataFrame,\
    \ name: str, output_dir: Path):\n        \"\"\"Plot performance across different\
    \ data distributions\"\"\"\n        plt.figure(figsize=(12, 8))\n        \n  \
    \      distributions = df['distribution'].unique()\n        implementations =\
    \ df['implementation'].unique()\n        \n        # Create grouped bar plot\n\
    \        n_dist = len(distributions)\n        n_impl = len(implementations)\n\
    \        width = 0.8 / n_impl\n        \n        for i, impl in enumerate(implementations):\n\
    \            impl_data = df[df['implementation'] == impl]\n            avg_times\
    \ = impl_data.groupby('distribution')['time_ms'].mean()\n            \n      \
    \      x = [j + i * width for j in range(n_dist)]\n            plt.bar(x, [avg_times.get(d,\
    \ 0) for d in distributions], \n                   width=width, label=impl, alpha=0.8)\n\
    \        \n        plt.xlabel('Data Distribution')\n        plt.ylabel('Time (ms)')\n\
    \        plt.title(f'{name} - Performance by Data Distribution')\n        plt.xticks([j\
    \ + width * (n_impl - 1) / 2 for j in range(n_dist)], \n                   distributions,\
    \ rotation=45)\n        plt.legend()\n        plt.grid(True, axis='y', alpha=0.3)\n\
    \        \n        filename = output_dir / f\"{name}_distribution_analysis.png\"\
    \n        plt.savefig(filename, dpi=150, bbox_inches='tight')\n        plt.close()\n\
    \        print(f\"Plot saved: {filename}\")\n    \n    def create_speedup_heatmap(self,\
    \ df: pd.DataFrame, base_impl: str, name: str, output_dir: Path):\n        \"\"\
    \"Create heatmap showing speedup ratios\"\"\"\n        # Pivot data to create\
    \ matrix\n        pivot_data = df.pivot_table(\n            values='time_ms',\n\
    \            index='test_case',\n            columns='implementation',\n     \
    \       aggfunc='mean'\n        )\n        \n        # Calculate speedup ratios\
    \ relative to base implementation\n        if base_impl in pivot_data.columns:\n\
    \            speedup = pivot_data.div(pivot_data[base_impl], axis=0)\n       \
    \     \n            plt.figure(figsize=(10, 8))\n            plt.imshow(speedup.values,\
    \ aspect='auto', cmap='RdYlGn')\n            plt.colorbar(label=f'Speedup vs {base_impl}')\n\
    \            \n            # Add text annotations\n            for i in range(len(speedup.index)):\n\
    \                for j in range(len(speedup.columns)):\n                    plt.text(j,\
    \ i, f'{speedup.values[i, j]:.2f}',\n                            ha='center',\
    \ va='center')\n            \n            plt.xticks(range(len(speedup.columns)),\
    \ speedup.columns, rotation=45)\n            plt.yticks(range(len(speedup.index)),\
    \ speedup.index)\n            plt.title(f'{name} - Speedup Heatmap')\n       \
    \     plt.tight_layout()\n            \n            filename = output_dir / f\"\
    {name}_speedup_heatmap.png\"\n            plt.savefig(filename, dpi=150)\n   \
    \         plt.close()\n            print(f\"Plot saved: {filename}\")\n    \n\
    \    def _plot_complexity_analysis(self, df: pd.DataFrame, name: str, output_dir:\
    \ Path):\n        \"\"\"Plot performance vs size with complexity reference lines\"\
    \"\"\n        plt.figure(figsize=(12, 8))\n        \n        for impl in df['implementation'].unique():\n\
    \            impl_data = df[df['implementation'] == impl]\n            \n    \
    \        if 'size' in impl_data.columns:\n                # Group by size and\
    \ calculate mean time\n                avg_times = impl_data.groupby('size')['time_ms'].mean()\n\
    \                sizes = avg_times.index.values\n                times = avg_times.values\n\
    \                \n                plt.loglog(sizes, times, 'o-', label=impl,\
    \ linewidth=2, markersize=6)\n        \n        # Add complexity reference lines\n\
    \        if len(df['size'].unique()) > 2:\n            min_size = df['size'].min()\n\
    \            max_size = df['size'].max()\n            ref_sizes = [s for s in\
    \ [100, 1000, 10000, 100000] if min_size <= s <= max_size]\n            \n   \
    \         if ref_sizes:\n                base_time = 0.001  # 1 microsecond base\
    \ time\n                \n                # O(n) reference\n                linear_times\
    \ = [base_time * s / ref_sizes[0] for s in ref_sizes]\n                plt.loglog(ref_sizes,\
    \ linear_times, '--', alpha=0.5, color='gray', label='O(n)')\n               \
    \ \n                # O(n log n) reference  \n                nlogn_times = [base_time\
    \ * s * 20 / (ref_sizes[0] * 20) for s in ref_sizes]  # log approximation\n  \
    \              plt.loglog(ref_sizes, nlogn_times, ':', alpha=0.5, color='gray',\
    \ label='O(n log n)')\n        \n        plt.xlabel('Input Size')\n        plt.ylabel('Time\
    \ (ms)')\n        plt.title(f'{name} - Complexity Analysis')\n        plt.legend()\n\
    \        plt.grid(True, alpha=0.3)\n        \n        filename = output_dir /\
    \ f\"{name}_complexity_analysis.png\"\n        plt.savefig(filename, dpi=150,\
    \ bbox_inches='tight')\n        plt.close()\n        print(f\"Plot saved: {filename}\"\
    )\n    \n    def _plot_speedup_comparison(self, df: pd.DataFrame, name: str, output_dir:\
    \ Path):\n        \"\"\"Plot speedup ratios between implementations\"\"\"\n  \
    \      implementations = df['implementation'].unique()\n        \n        if len(implementations)\
    \ < 2:\n            return\n        \n        plt.figure(figsize=(12, 6))\n  \
    \      \n        # Use first implementation as baseline\n        baseline = implementations[0]\n\
    \        \n        for i, other_impl in enumerate(implementations[1:], 1):\n \
    \           speedups = []\n            test_cases = []\n            \n       \
    \     # Calculate speedup for each test case\n            for test_case in df['test_case'].unique():\n\
    \                baseline_time = df[(df['implementation'] == baseline) & \n  \
    \                               (df['test_case'] == test_case)]['time_ms'].mean()\n\
    \                other_time = df[(df['implementation'] == other_impl) & \n   \
    \                            (df['test_case'] == test_case)]['time_ms'].mean()\n\
    \                \n                if baseline_time > 0 and other_time > 0:\n\
    \                    speedup = baseline_time / other_time\n                  \
    \  speedups.append(speedup)\n                    test_cases.append(test_case)\n\
    \            \n            if speedups:\n                x = range(len(speedups))\n\
    \                bars = plt.bar([xi + i*0.4 for xi in x], speedups, \n       \
    \                       width=0.4, label=f'{other_impl} vs {baseline}', alpha=0.7)\n\
    \                \n                # Add horizontal line at 1.0 (no speedup)\n\
    \                plt.axhline(y=1.0, color='red', linestyle='--', alpha=0.5)\n\
    \                \n                # Color bars based on speedup\n           \
    \     for bar, speedup in zip(bars, speedups):\n                    if speedup\
    \ > 1.0:\n                        bar.set_color('green')\n                   \
    \ else:\n                        bar.set_color('red')\n        \n        plt.xlabel('Test\
    \ Cases')\n        plt.ylabel('Speedup Ratio')\n        plt.title(f'{name} - Speedup\
    \ Comparison')\n        plt.xticks([xi + 0.2 for xi in range(len(test_cases))],\
    \ \n                   [tc[:20] + '...' if len(tc) > 20 else tc for tc in test_cases],\
    \ \n                   rotation=45, ha='right')\n        plt.legend()\n      \
    \  plt.grid(True, axis='y', alpha=0.3)\n        plt.tight_layout()\n        \n\
    \        filename = output_dir / f\"{name}_speedup_comparison.png\"\n        plt.savefig(filename,\
    \ dpi=150, bbox_inches='tight')\n        plt.close()\n        print(f\"Plot saved:\
    \ {filename}\")"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/perf/plotters.py
  requiredBy:
  - cp_library/perf/benchmark.py
  - cp_library/perf/simple_plots.py
  - cp_library/perf/examples/simple_usage.py
  - cp_library/perf/examples/rank_benchmark.py
  - perf/bool_list_benchmark.py
  - perf/rank_perf.py
  timestamp: '2025-07-09 08:31:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/plotters.py
layout: document
redirect_from:
- /library/cp_library/perf/plotters.py
- /library/cp_library/perf/plotters.py.html
title: cp_library/perf/plotters.py
---
