---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "\"\"\"\nPlotting utilities for benchmark results.\nHandles both matplotlib\
    \ and ASCII plotting with consistent interface.\n\"\"\"\n\nimport statistics\n\
    from typing import Dict, List, Any\nfrom pathlib import Path\nfrom collections\
    \ import defaultdict\n\n\nclass BenchmarkPlotter:\n    \"\"\"Creates plots from\
    \ benchmark results\"\"\"\n    \n    def __init__(self, plot_scale: str = \"loglog\"\
    ):\n        self.plot_scale = plot_scale\n    \n    def create_plots(self, results:\
    \ List[Dict[str, Any]], config) -> None:\n        \"\"\"Create all plots for benchmark\
    \ results\"\"\"\n        try:\n            import matplotlib.pyplot as plt\n \
    \           self._create_matplotlib_plots(plt, results, config)\n        except\
    \ ImportError:\n            print(\"Matplotlib not available - using ASCII plots\"\
    )\n            self._create_ascii_plots(results, config)\n        except Exception\
    \ as e:\n            print(f\"Plotting failed: {e}\")\n    \n    def _group_results_by_operation(self,\
    \ results: List[Dict[str, Any]]) -> Dict[str, Dict[int, List[Dict[str, Any]]]]:\n\
    \        \"\"\"Group results by operation and size for plotting\"\"\"\n      \
    \  data_by_op = defaultdict(lambda: defaultdict(list))\n        for r in results:\n\
    \            if r['time_ms'] != float('inf') and r['correct']:\n             \
    \   data_by_op[r['operation']][r['size']].append({\n                    'implementation':\
    \ r['implementation'],\n                    'time_ms': r['time_ms']\n        \
    \        })\n        return data_by_op\n    \n    def _create_matplotlib_plots(self,\
    \ plt, results: List[Dict[str, Any]], config) -> None:\n        \"\"\"Create matplotlib\
    \ plots\"\"\"\n        output_dir = Path(config.output_dir)\n        output_dir.mkdir(parents=True,\
    \ exist_ok=True)\n        \n        # Group and prepare data for plotting\n  \
    \      data_by_op = self._group_results_by_operation(results)\n        \n    \
    \    # Create plots for each operation\n        for operation, operation_data\
    \ in data_by_op.items():\n            self._create_performance_plot(plt, operation,\
    \ operation_data, output_dir, config.name)\n            self._create_speedup_plot(plt,\
    \ operation, operation_data, output_dir, config.name)\n    \n    def _create_performance_plot(self,\
    \ plt, operation: str, operation_data: Dict[int, List[Dict[str, Any]]], output_dir:\
    \ Path, benchmark_name: str):\n        \"\"\"Create performance plot for a single\
    \ operation\"\"\"\n        sizes = sorted(operation_data.keys())\n        implementations\
    \ = set()\n        for size_data in operation_data.values():\n            for\
    \ entry in size_data:\n                implementations.add(entry['implementation'])\n\
    \        \n        implementations = sorted(implementations)\n        \n     \
    \   # Collect all timing data\n        all_data = {}\n        for impl in implementations:\n\
    \            impl_times = []\n            impl_sizes = []\n            for size\
    \ in sizes:\n                times = [entry['time_ms'] for entry in operation_data[size]\
    \ \n                        if entry['implementation'] == impl]\n            \
    \    if times:\n                    impl_times.append(statistics.mean(times))\n\
    \                    impl_sizes.append(size)\n            \n            if impl_times:\n\
    \                all_data[impl] = (impl_sizes, impl_times)\n        \n       \
    \ # Create performance plot\n        plt.figure(figsize=(10, 6))\n        for\
    \ impl, (impl_sizes, impl_times) in all_data.items():\n            plt.plot(impl_sizes,\
    \ impl_times, 'o-', label=impl)\n        \n        plt.xlabel('Input Size')\n\
    \        plt.ylabel('Time (ms)')\n        plt.title(f'{benchmark_name} - {operation}\
    \ Operation')\n        plt.legend()\n        plt.grid(True, alpha=0.3)\n     \
    \   \n        self._apply_scaling(plt)\n        \n        plot_file = output_dir\
    \ / f\"{benchmark_name}_{operation}_performance.png\"\n        plt.savefig(plot_file,\
    \ dpi=300, bbox_inches='tight')\n        plt.close()\n        print(f\"Plot saved:\
    \ {plot_file}\")\n    \n    def _create_speedup_plot(self, plt, operation: str,\
    \ operation_data: Dict[int, List[Dict[str, Any]]], output_dir: Path, benchmark_name:\
    \ str):\n        \"\"\"Create speedup plot for a single operation\"\"\"\n    \
    \    sizes = sorted(operation_data.keys())\n        implementations = set()\n\
    \        for size_data in operation_data.values():\n            for entry in size_data:\n\
    \                implementations.add(entry['implementation'])\n        \n    \
    \    implementations = sorted(implementations)\n        \n        if len(implementations)\
    \ <= 1:\n            return  # Need at least 2 implementations for speedup\n \
    \       \n        # Collect all timing data\n        all_data = {}\n        for\
    \ impl in implementations:\n            impl_times = []\n            impl_sizes\
    \ = []\n            for size in sizes:\n                times = [entry['time_ms']\
    \ for entry in operation_data[size] \n                        if entry['implementation']\
    \ == impl]\n                if times:\n                    impl_times.append(statistics.mean(times))\n\
    \                    impl_sizes.append(size)\n            \n            if impl_times:\n\
    \                all_data[impl] = (impl_sizes, impl_times)\n        \n       \
    \ # Create speedup plot (relative to first implementation)\n        baseline_impl\
    \ = implementations[0]\n        baseline_sizes, baseline_times = all_data[baseline_impl]\n\
    \        \n        plt.figure(figsize=(10, 6))\n        for impl, (impl_sizes,\
    \ impl_times) in all_data.items():\n            speedups = []\n            speedup_sizes\
    \ = []\n            \n            # Calculate speedup relative to baseline for\
    \ each size\n            for size, time in zip(impl_sizes, impl_times):\n    \
    \            if size in baseline_sizes:\n                    baseline_idx = baseline_sizes.index(size)\n\
    \                    baseline_time = baseline_times[baseline_idx]\n          \
    \          if time > 0:\n                        speedup = baseline_time / time\n\
    \                        speedups.append(speedup)\n                        speedup_sizes.append(size)\n\
    \            \n            if speedups:\n                plt.plot(speedup_sizes,\
    \ speedups, 'o-', label=impl)\n        \n        plt.xlabel('Input Size')\n  \
    \      plt.ylabel(f'Speedup (relative to {baseline_impl})')\n        plt.title(f'{benchmark_name}\
    \ - {operation} Operation Speedup')\n        plt.legend()\n        plt.grid(True,\
    \ alpha=0.3)\n        plt.axhline(y=1.0, color='k', linestyle='--', alpha=0.5,\
    \ label='Baseline')\n        \n        # Apply scaling (semilogx for speedup plots)\n\
    \        if self.plot_scale in [\"loglog\", \"semilogx\"]:\n            plt.semilogx()\n\
    \        elif self.plot_scale == \"semilogy\":\n            plt.semilogx()  #\
    \ Only log x-axis for speedup plots\n        # else: linear scale (default)\n\
    \        \n        speedup_plot_file = output_dir / f\"{benchmark_name}_{operation}_speedup.png\"\
    \n        plt.savefig(speedup_plot_file, dpi=300, bbox_inches='tight')\n     \
    \   plt.close()\n        print(f\"Speedup plot saved: {speedup_plot_file}\")\n\
    \    \n    def _apply_scaling(self, plt):\n        \"\"\"Apply the configured\
    \ scaling to the plot\"\"\"\n        if self.plot_scale == \"loglog\":\n     \
    \       plt.loglog()\n        elif self.plot_scale == \"linear\":\n          \
    \  pass  # Default linear scale\n        elif self.plot_scale == \"semilogx\"\
    :\n            plt.semilogx()\n        elif self.plot_scale == \"semilogy\":\n\
    \            plt.semilogy()\n        else:\n            # Default to loglog if\
    \ invalid option\n            plt.loglog()\n    \n    def _create_ascii_plots(self,\
    \ results: List[Dict[str, Any]], config) -> None:\n        \"\"\"Create ASCII\
    \ plots when matplotlib is not available\"\"\"\n        if not results:\n    \
    \        return\n        \n        output_dir = Path(config.output_dir)\n    \
    \    output_dir.mkdir(parents=True, exist_ok=True)\n        \n        print(f\"\
    \\nGenerating ASCII plots in {output_dir}/\")\n        \n        # Group by operation\
    \ for ASCII plots\n        data_by_op = self._group_results_by_operation(results)\n\
    \        \n        for operation, operation_data in data_by_op.items():\n    \
    \        self._create_ascii_size_plot(operation_data, operation, config.name,\
    \ output_dir)\n            self._create_ascii_comparison_table(operation_data,\
    \ operation, config.name, output_dir)\n    \n    def _create_ascii_size_plot(self,\
    \ operation_data: Dict[int, List[Dict[str, Any]]], operation: str, name: str,\
    \ output_dir: Path):\n        \"\"\"Create ASCII plot of performance vs size\"\
    \"\"\n        # Group by implementation and size\n        impl_data = {}\n   \
    \     for size, entries in operation_data.items():\n            for entry in entries:\n\
    \                impl = entry['implementation']\n                time_ms = entry['time_ms']\n\
    \                \n                if impl not in impl_data:\n               \
    \     impl_data[impl] = {}\n                if size not in impl_data[impl]:\n\
    \                    impl_data[impl][size] = []\n                impl_data[impl][size].append(time_ms)\n\
    \        \n        # Calculate averages\n        for impl in impl_data:\n    \
    \        for size in impl_data[impl]:\n                impl_data[impl][size] =\
    \ sum(impl_data[impl][size]) / len(impl_data[impl][size])\n        \n        #\
    \ Create ASCII plot\n        plot_lines = []\n        plot_lines.append(f\"Performance\
    \ vs Size - {name} - {operation}\")\n        plot_lines.append(\"=\" * 60)\n \
    \       plot_lines.append(\"\")\n        \n        if impl_data:\n           \
    \ # Get all sizes\n            all_sizes = set()\n            for impl in impl_data:\n\
    \                all_sizes.update(impl_data[impl].keys())\n            all_sizes\
    \ = sorted(all_sizes)\n            \n            # Create table\n            plot_lines.append(f\"\
    {'Size':<12} \" + \"\".join(f\"{impl:<15}\" for impl in impl_data.keys()))\n \
    \           plot_lines.append(\"-\" * (12 + 15 * len(impl_data)))\n          \
    \  \n            for size in all_sizes:\n                line = f\"{size:<12}\
    \ \"\n                for impl in impl_data.keys():\n                    time_val\
    \ = impl_data[impl].get(size, 0)\n                    line += f\"{time_val:<15.3f}\"\
    \n                plot_lines.append(line)\n        \n        # Save to file\n\
    \        filename = output_dir / f\"{name}_{operation}_size_plot.txt\"\n     \
    \   with open(filename, 'w') as f:\n            f.write('\\n'.join(plot_lines))\n\
    \        print(f\"ASCII plot saved: {filename}\")\n    \n    def _create_ascii_comparison_table(self,\
    \ operation_data: Dict[int, List[Dict[str, Any]]], operation: str, name: str,\
    \ output_dir: Path):\n        \"\"\"Create comparison table for ASCII output\"\
    \"\"\n        # Flatten all entries\n        all_entries = []\n        for entries\
    \ in operation_data.values():\n            all_entries.extend(entries)\n     \
    \   \n        # Group by implementation\n        impl_times = {}\n        for\
    \ entry in all_entries:\n            impl = entry['implementation']\n        \
    \    if impl not in impl_times:\n                impl_times[impl] = []\n     \
    \       impl_times[impl].append(entry['time_ms'])\n        \n        # Calculate\
    \ statistics\n        stats = {}\n        for impl, times in impl_times.items():\n\
    \            stats[impl] = {\n                'mean': sum(times) / len(times),\n\
    \                'min': min(times),\n                'max': max(times),\n    \
    \            'count': len(times)\n            }\n        \n        # Create comparison\
    \ table\n        table_lines = []\n        table_lines.append(f\"Implementation\
    \ Comparison - {name} - {operation}\")\n        table_lines.append(\"=\" * 70)\n\
    \        table_lines.append(\"\")\n        table_lines.append(f\"{'Implementation':<20}\
    \ {'Mean (ms)':<12} {'Min (ms)':<12} {'Max (ms)':<12} {'Count':<8}\")\n      \
    \  table_lines.append(\"-\" * 68)\n        \n        for impl, stat in stats.items():\n\
    \            table_lines.append(\n                f\"{impl:<20} {stat['mean']:<12.3f}\
    \ {stat['min']:<12.3f} \"\n                f\"{stat['max']:<12.3f} {stat['count']:<8}\"\
    \n            )\n        \n        # Calculate speedup if 2 implementations\n\
    \        if len(stats) == 2:\n            impls = list(stats.keys())\n       \
    \     ratio = stats[impls[0]]['mean'] / stats[impls[1]]['mean']\n            faster\
    \ = impls[1] if ratio > 1 else impls[0]\n            speedup = max(ratio, 1/ratio)\n\
    \            \n            table_lines.append(\"\")\n            table_lines.append(f\"\
    {faster} is {speedup:.2f}x faster on average\")\n        \n        # Save to file\n\
    \        filename = output_dir / f\"{name}_{operation}_comparison.txt\"\n    \
    \    with open(filename, 'w') as f:\n            f.write('\\n'.join(table_lines))\n\
    \        print(f\"Comparison table saved: {filename}\")\n"
  code: "\"\"\"\nPlotting utilities for benchmark results.\nHandles both matplotlib\
    \ and ASCII plotting with consistent interface.\n\"\"\"\n\nimport statistics\n\
    from typing import Dict, List, Any\nfrom pathlib import Path\nfrom collections\
    \ import defaultdict\n\n\nclass BenchmarkPlotter:\n    \"\"\"Creates plots from\
    \ benchmark results\"\"\"\n    \n    def __init__(self, plot_scale: str = \"loglog\"\
    ):\n        self.plot_scale = plot_scale\n    \n    def create_plots(self, results:\
    \ List[Dict[str, Any]], config) -> None:\n        \"\"\"Create all plots for benchmark\
    \ results\"\"\"\n        try:\n            import matplotlib.pyplot as plt\n \
    \           self._create_matplotlib_plots(plt, results, config)\n        except\
    \ ImportError:\n            print(\"Matplotlib not available - using ASCII plots\"\
    )\n            self._create_ascii_plots(results, config)\n        except Exception\
    \ as e:\n            print(f\"Plotting failed: {e}\")\n    \n    def _group_results_by_operation(self,\
    \ results: List[Dict[str, Any]]) -> Dict[str, Dict[int, List[Dict[str, Any]]]]:\n\
    \        \"\"\"Group results by operation and size for plotting\"\"\"\n      \
    \  data_by_op = defaultdict(lambda: defaultdict(list))\n        for r in results:\n\
    \            if r['time_ms'] != float('inf') and r['correct']:\n             \
    \   data_by_op[r['operation']][r['size']].append({\n                    'implementation':\
    \ r['implementation'],\n                    'time_ms': r['time_ms']\n        \
    \        })\n        return data_by_op\n    \n    def _create_matplotlib_plots(self,\
    \ plt, results: List[Dict[str, Any]], config) -> None:\n        \"\"\"Create matplotlib\
    \ plots\"\"\"\n        output_dir = Path(config.output_dir)\n        output_dir.mkdir(parents=True,\
    \ exist_ok=True)\n        \n        # Group and prepare data for plotting\n  \
    \      data_by_op = self._group_results_by_operation(results)\n        \n    \
    \    # Create plots for each operation\n        for operation, operation_data\
    \ in data_by_op.items():\n            self._create_performance_plot(plt, operation,\
    \ operation_data, output_dir, config.name)\n            self._create_speedup_plot(plt,\
    \ operation, operation_data, output_dir, config.name)\n    \n    def _create_performance_plot(self,\
    \ plt, operation: str, operation_data: Dict[int, List[Dict[str, Any]]], output_dir:\
    \ Path, benchmark_name: str):\n        \"\"\"Create performance plot for a single\
    \ operation\"\"\"\n        sizes = sorted(operation_data.keys())\n        implementations\
    \ = set()\n        for size_data in operation_data.values():\n            for\
    \ entry in size_data:\n                implementations.add(entry['implementation'])\n\
    \        \n        implementations = sorted(implementations)\n        \n     \
    \   # Collect all timing data\n        all_data = {}\n        for impl in implementations:\n\
    \            impl_times = []\n            impl_sizes = []\n            for size\
    \ in sizes:\n                times = [entry['time_ms'] for entry in operation_data[size]\
    \ \n                        if entry['implementation'] == impl]\n            \
    \    if times:\n                    impl_times.append(statistics.mean(times))\n\
    \                    impl_sizes.append(size)\n            \n            if impl_times:\n\
    \                all_data[impl] = (impl_sizes, impl_times)\n        \n       \
    \ # Create performance plot\n        plt.figure(figsize=(10, 6))\n        for\
    \ impl, (impl_sizes, impl_times) in all_data.items():\n            plt.plot(impl_sizes,\
    \ impl_times, 'o-', label=impl)\n        \n        plt.xlabel('Input Size')\n\
    \        plt.ylabel('Time (ms)')\n        plt.title(f'{benchmark_name} - {operation}\
    \ Operation')\n        plt.legend()\n        plt.grid(True, alpha=0.3)\n     \
    \   \n        self._apply_scaling(plt)\n        \n        plot_file = output_dir\
    \ / f\"{benchmark_name}_{operation}_performance.png\"\n        plt.savefig(plot_file,\
    \ dpi=300, bbox_inches='tight')\n        plt.close()\n        print(f\"Plot saved:\
    \ {plot_file}\")\n    \n    def _create_speedup_plot(self, plt, operation: str,\
    \ operation_data: Dict[int, List[Dict[str, Any]]], output_dir: Path, benchmark_name:\
    \ str):\n        \"\"\"Create speedup plot for a single operation\"\"\"\n    \
    \    sizes = sorted(operation_data.keys())\n        implementations = set()\n\
    \        for size_data in operation_data.values():\n            for entry in size_data:\n\
    \                implementations.add(entry['implementation'])\n        \n    \
    \    implementations = sorted(implementations)\n        \n        if len(implementations)\
    \ <= 1:\n            return  # Need at least 2 implementations for speedup\n \
    \       \n        # Collect all timing data\n        all_data = {}\n        for\
    \ impl in implementations:\n            impl_times = []\n            impl_sizes\
    \ = []\n            for size in sizes:\n                times = [entry['time_ms']\
    \ for entry in operation_data[size] \n                        if entry['implementation']\
    \ == impl]\n                if times:\n                    impl_times.append(statistics.mean(times))\n\
    \                    impl_sizes.append(size)\n            \n            if impl_times:\n\
    \                all_data[impl] = (impl_sizes, impl_times)\n        \n       \
    \ # Create speedup plot (relative to first implementation)\n        baseline_impl\
    \ = implementations[0]\n        baseline_sizes, baseline_times = all_data[baseline_impl]\n\
    \        \n        plt.figure(figsize=(10, 6))\n        for impl, (impl_sizes,\
    \ impl_times) in all_data.items():\n            speedups = []\n            speedup_sizes\
    \ = []\n            \n            # Calculate speedup relative to baseline for\
    \ each size\n            for size, time in zip(impl_sizes, impl_times):\n    \
    \            if size in baseline_sizes:\n                    baseline_idx = baseline_sizes.index(size)\n\
    \                    baseline_time = baseline_times[baseline_idx]\n          \
    \          if time > 0:\n                        speedup = baseline_time / time\n\
    \                        speedups.append(speedup)\n                        speedup_sizes.append(size)\n\
    \            \n            if speedups:\n                plt.plot(speedup_sizes,\
    \ speedups, 'o-', label=impl)\n        \n        plt.xlabel('Input Size')\n  \
    \      plt.ylabel(f'Speedup (relative to {baseline_impl})')\n        plt.title(f'{benchmark_name}\
    \ - {operation} Operation Speedup')\n        plt.legend()\n        plt.grid(True,\
    \ alpha=0.3)\n        plt.axhline(y=1.0, color='k', linestyle='--', alpha=0.5,\
    \ label='Baseline')\n        \n        # Apply scaling (semilogx for speedup plots)\n\
    \        if self.plot_scale in [\"loglog\", \"semilogx\"]:\n            plt.semilogx()\n\
    \        elif self.plot_scale == \"semilogy\":\n            plt.semilogx()  #\
    \ Only log x-axis for speedup plots\n        # else: linear scale (default)\n\
    \        \n        speedup_plot_file = output_dir / f\"{benchmark_name}_{operation}_speedup.png\"\
    \n        plt.savefig(speedup_plot_file, dpi=300, bbox_inches='tight')\n     \
    \   plt.close()\n        print(f\"Speedup plot saved: {speedup_plot_file}\")\n\
    \    \n    def _apply_scaling(self, plt):\n        \"\"\"Apply the configured\
    \ scaling to the plot\"\"\"\n        if self.plot_scale == \"loglog\":\n     \
    \       plt.loglog()\n        elif self.plot_scale == \"linear\":\n          \
    \  pass  # Default linear scale\n        elif self.plot_scale == \"semilogx\"\
    :\n            plt.semilogx()\n        elif self.plot_scale == \"semilogy\":\n\
    \            plt.semilogy()\n        else:\n            # Default to loglog if\
    \ invalid option\n            plt.loglog()\n    \n    def _create_ascii_plots(self,\
    \ results: List[Dict[str, Any]], config) -> None:\n        \"\"\"Create ASCII\
    \ plots when matplotlib is not available\"\"\"\n        if not results:\n    \
    \        return\n        \n        output_dir = Path(config.output_dir)\n    \
    \    output_dir.mkdir(parents=True, exist_ok=True)\n        \n        print(f\"\
    \\nGenerating ASCII plots in {output_dir}/\")\n        \n        # Group by operation\
    \ for ASCII plots\n        data_by_op = self._group_results_by_operation(results)\n\
    \        \n        for operation, operation_data in data_by_op.items():\n    \
    \        self._create_ascii_size_plot(operation_data, operation, config.name,\
    \ output_dir)\n            self._create_ascii_comparison_table(operation_data,\
    \ operation, config.name, output_dir)\n    \n    def _create_ascii_size_plot(self,\
    \ operation_data: Dict[int, List[Dict[str, Any]]], operation: str, name: str,\
    \ output_dir: Path):\n        \"\"\"Create ASCII plot of performance vs size\"\
    \"\"\n        # Group by implementation and size\n        impl_data = {}\n   \
    \     for size, entries in operation_data.items():\n            for entry in entries:\n\
    \                impl = entry['implementation']\n                time_ms = entry['time_ms']\n\
    \                \n                if impl not in impl_data:\n               \
    \     impl_data[impl] = {}\n                if size not in impl_data[impl]:\n\
    \                    impl_data[impl][size] = []\n                impl_data[impl][size].append(time_ms)\n\
    \        \n        # Calculate averages\n        for impl in impl_data:\n    \
    \        for size in impl_data[impl]:\n                impl_data[impl][size] =\
    \ sum(impl_data[impl][size]) / len(impl_data[impl][size])\n        \n        #\
    \ Create ASCII plot\n        plot_lines = []\n        plot_lines.append(f\"Performance\
    \ vs Size - {name} - {operation}\")\n        plot_lines.append(\"=\" * 60)\n \
    \       plot_lines.append(\"\")\n        \n        if impl_data:\n           \
    \ # Get all sizes\n            all_sizes = set()\n            for impl in impl_data:\n\
    \                all_sizes.update(impl_data[impl].keys())\n            all_sizes\
    \ = sorted(all_sizes)\n            \n            # Create table\n            plot_lines.append(f\"\
    {'Size':<12} \" + \"\".join(f\"{impl:<15}\" for impl in impl_data.keys()))\n \
    \           plot_lines.append(\"-\" * (12 + 15 * len(impl_data)))\n          \
    \  \n            for size in all_sizes:\n                line = f\"{size:<12}\
    \ \"\n                for impl in impl_data.keys():\n                    time_val\
    \ = impl_data[impl].get(size, 0)\n                    line += f\"{time_val:<15.3f}\"\
    \n                plot_lines.append(line)\n        \n        # Save to file\n\
    \        filename = output_dir / f\"{name}_{operation}_size_plot.txt\"\n     \
    \   with open(filename, 'w') as f:\n            f.write('\\n'.join(plot_lines))\n\
    \        print(f\"ASCII plot saved: {filename}\")\n    \n    def _create_ascii_comparison_table(self,\
    \ operation_data: Dict[int, List[Dict[str, Any]]], operation: str, name: str,\
    \ output_dir: Path):\n        \"\"\"Create comparison table for ASCII output\"\
    \"\"\n        # Flatten all entries\n        all_entries = []\n        for entries\
    \ in operation_data.values():\n            all_entries.extend(entries)\n     \
    \   \n        # Group by implementation\n        impl_times = {}\n        for\
    \ entry in all_entries:\n            impl = entry['implementation']\n        \
    \    if impl not in impl_times:\n                impl_times[impl] = []\n     \
    \       impl_times[impl].append(entry['time_ms'])\n        \n        # Calculate\
    \ statistics\n        stats = {}\n        for impl, times in impl_times.items():\n\
    \            stats[impl] = {\n                'mean': sum(times) / len(times),\n\
    \                'min': min(times),\n                'max': max(times),\n    \
    \            'count': len(times)\n            }\n        \n        # Create comparison\
    \ table\n        table_lines = []\n        table_lines.append(f\"Implementation\
    \ Comparison - {name} - {operation}\")\n        table_lines.append(\"=\" * 70)\n\
    \        table_lines.append(\"\")\n        table_lines.append(f\"{'Implementation':<20}\
    \ {'Mean (ms)':<12} {'Min (ms)':<12} {'Max (ms)':<12} {'Count':<8}\")\n      \
    \  table_lines.append(\"-\" * 68)\n        \n        for impl, stat in stats.items():\n\
    \            table_lines.append(\n                f\"{impl:<20} {stat['mean']:<12.3f}\
    \ {stat['min']:<12.3f} \"\n                f\"{stat['max']:<12.3f} {stat['count']:<8}\"\
    \n            )\n        \n        # Calculate speedup if 2 implementations\n\
    \        if len(stats) == 2:\n            impls = list(stats.keys())\n       \
    \     ratio = stats[impls[0]]['mean'] / stats[impls[1]]['mean']\n            faster\
    \ = impls[1] if ratio > 1 else impls[0]\n            speedup = max(ratio, 1/ratio)\n\
    \            \n            table_lines.append(\"\")\n            table_lines.append(f\"\
    {faster} is {speedup:.2f}x faster on average\")\n        \n        # Save to file\n\
    \        filename = output_dir / f\"{name}_{operation}_comparison.txt\"\n    \
    \    with open(filename, 'w') as f:\n            f.write('\\n'.join(table_lines))\n\
    \        print(f\"Comparison table saved: {filename}\")"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/perf/plotting.py
  requiredBy: []
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/plotting.py
layout: document
redirect_from:
- /library/cp_library/perf/plotting.py
- /library/cp_library/perf/plotting.py.html
title: cp_library/perf/plotting.py
---
