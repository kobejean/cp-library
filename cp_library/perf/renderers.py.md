---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/perf/interfaces.py
    title: cp_library/perf/interfaces.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/perf/benchmark.py
    title: cp_library/perf/benchmark.py
  - icon: ':warning:'
    path: perf/bit2.py
    title: perf/bit2.py
  - icon: ':warning:'
    path: perf/bit6.py
    title: perf/bit6.py
  - icon: ':warning:'
    path: perf/bool_list.py
    title: perf/bool_list.py
  - icon: ':warning:'
    path: perf/bytearray_decode.py
    title: perf/bytearray_decode.py
  - icon: ':warning:'
    path: perf/csr.py
    title: perf/csr.py
  - icon: ':warning:'
    path: perf/csr2.py
    title: perf/csr2.py
  - icon: ':warning:'
    path: perf/csr6.py
    title: perf/csr6.py
  - icon: ':warning:'
    path: perf/deque.py
    title: perf/deque.py
  - icon: ':warning:'
    path: perf/edge_list.py
    title: perf/edge_list.py
  - icon: ':warning:'
    path: perf/grid.py
    title: perf/grid.py
  - icon: ':warning:'
    path: perf/heap_csr.py
    title: perf/heap_csr.py
  - icon: ':warning:'
    path: perf/heap_view.py
    title: perf/heap_view.py
  - icon: ':warning:'
    path: perf/list2.py
    title: perf/list2.py
  - icon: ':warning:'
    path: perf/list6.py
    title: perf/list6.py
  - icon: ':warning:'
    path: perf/list_view.py
    title: perf/list_view.py
  - icon: ':warning:'
    path: perf/mlist.py
    title: perf/mlist.py
  - icon: ':warning:'
    path: perf/que.py
    title: perf/que.py
  - icon: ':warning:'
    path: perf/rank.py
    title: perf/rank.py
  - icon: ':warning:'
    path: perf/segtree2.py
    title: perf/segtree2.py
  - icon: ':warning:'
    path: perf/segtree6.py
    title: perf/segtree6.py
  - icon: ':warning:'
    path: perf/view2.py
    title: perf/view2.py
  - icon: ':warning:'
    path: perf/view6.py
    title: perf/view6.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "\"\"\"\nPlot rendering implementations following Open/Closed Principle.\n\
    \"\"\"\n\nimport statistics\nfrom collections import defaultdict\nfrom pathlib\
    \ import Path\nfrom typing import List, Dict, Any\n\"\"\"\nInterfaces for the\
    \ benchmark framework following SOLID principles.\n\"\"\"\n\nfrom abc import ABC,\
    \ abstractmethod\nfrom typing import Any, Callable, Dict, List, Optional, Union\n\
    from dataclasses import dataclass\n\n\n@dataclass\nclass BenchmarkResult:\n  \
    \  \"\"\"Immutable benchmark result value object\"\"\"\n    operation: str\n \
    \   size: int\n    implementation: str\n    time_ms: float\n    correct: bool\n\
    \    error: Optional[str] = None\n\n\nclass TimerInterface(ABC):\n    \"\"\"Interface\
    \ for timing implementations\"\"\"\n    \n    @abstractmethod\n    def measure_time(self,\
    \ func: Callable, data: Any, setup_func: Callable = None) -> tuple[Any, float]:\n\
    \        \"\"\"Measure execution time of a function\"\"\"\n        pass\n\n\n\
    class PlotRenderer(ABC):\n    \"\"\"Interface for plot rendering implementations\"\
    \"\"\n    \n    @abstractmethod\n    def can_render(self) -> bool:\n        \"\
    \"\"Check if this renderer is available\"\"\"\n        pass\n    \n    @abstractmethod\n\
    \    def create_plots(self, results: List[BenchmarkResult], config: Any) -> None:\n\
    \        \"\"\"Create plots from benchmark results\"\"\"\n        pass\n\n\nclass\
    \ ResultValidator(ABC):\n    \"\"\"Interface for result validation strategies\"\
    \"\"\n    \n    @abstractmethod\n    def validate(self, expected: Any, actual:\
    \ Any) -> bool:\n        \"\"\"Validate benchmark result\"\"\"\n        pass\n\
    \n\nclass DataGenerator(ABC):\n    \"\"\"Interface for data generation strategies\"\
    \"\"\n    \n    @abstractmethod\n    def generate(self, size: int, operation:\
    \ str) -> Any:\n        \"\"\"Generate test data for given size and operation\"\
    \"\"\n        pass\n\n\nclass OutputManager(ABC):\n    \"\"\"Interface for output\
    \ management\"\"\"\n    \n    @abstractmethod\n    def save_results(self, results:\
    \ List[BenchmarkResult], config: Any) -> None:\n        \"\"\"Save benchmark results\"\
    \"\"\n        pass\n\n\nclass BenchmarkRegistry(ABC):\n    \"\"\"Interface for\
    \ benchmark component registration\"\"\"\n    \n    @abstractmethod\n    def register_implementation(self,\
    \ name: str, func: Callable, operations: List[str]) -> None:\n        \"\"\"Register\
    \ a benchmark implementation\"\"\"\n        pass\n    \n    @abstractmethod\n\
    \    def register_data_generator(self, name: str, generator: DataGenerator) ->\
    \ None:\n        \"\"\"Register a data generator\"\"\"\n        pass\n    \n \
    \   @abstractmethod\n    def register_validator(self, operation: str, validator:\
    \ ResultValidator) -> None:\n        \"\"\"Register a result validator\"\"\"\n\
    \        pass\n    \n    @abstractmethod\n    def register_setup(self, name: str,\
    \ setup_func: Callable, operations: List[str]) -> None:\n        \"\"\"Register\
    \ a setup function\"\"\"\n        pass\n\n\nclass BenchmarkOrchestrator(ABC):\n\
    \    \"\"\"Interface for benchmark execution orchestration\"\"\"\n    \n    @abstractmethod\n\
    \    def run_benchmarks(self, operations: List[str], sizes: List[int]) -> List[BenchmarkResult]:\n\
    \        \"\"\"Execute benchmarks and return results\"\"\"\n        pass\n\n\n\
    class PlotDataProcessor:\n    \"\"\"Utility class for processing benchmark data\
    \ for plotting\"\"\"\n    \n    @staticmethod\n    def group_by_operation(results:\
    \ List[BenchmarkResult]) -> Dict[str, List[BenchmarkResult]]:\n        \"\"\"\
    Group results by operation\"\"\"\n        grouped = defaultdict(list)\n      \
    \  for result in results:\n            if result.error is None and result.time_ms\
    \ != float('inf'):\n                grouped[result.operation].append(result)\n\
    \        return dict(grouped)\n    \n    @staticmethod\n    def group_by_implementation_and_size(results:\
    \ List[BenchmarkResult]) -> Dict[str, Dict[int, float]]:\n        \"\"\"Group\
    \ results by implementation and size\"\"\"\n        grouped = defaultdict(lambda:\
    \ defaultdict(float))\n        for result in results:\n            if result.error\
    \ is None and result.time_ms != float('inf'):\n                grouped[result.implementation][result.size]\
    \ = result.time_ms\n        return dict(grouped)\n    \n    @staticmethod\n  \
    \  def calculate_statistics(results: List[BenchmarkResult]) -> Dict[str, Dict[str,\
    \ float]]:\n        \"\"\"Calculate statistics for each implementation\"\"\"\n\
    \        impl_times = defaultdict(list)\n        for result in results:\n    \
    \        if result.error is None and result.time_ms != float('inf'):\n       \
    \         impl_times[result.implementation].append(result.time_ms)\n        \n\
    \        stats = {}\n        for impl, times in impl_times.items():\n        \
    \    if times:\n                stats[impl] = {\n                    'mean': statistics.mean(times),\n\
    \                    'min': min(times),\n                    'max': max(times),\n\
    \                    'count': len(times)\n                }\n        return stats\n\
    \n\nclass MatplotlibRenderer(PlotRenderer):\n    \"\"\"Matplotlib-based plot renderer\"\
    \"\"\n    \n    def __init__(self, plot_scale: str = \"loglog\"):\n        self.plot_scale\
    \ = plot_scale\n        self._matplotlib_available = None\n    \n    def can_render(self)\
    \ -> bool:\n        \"\"\"Check if matplotlib is available\"\"\"\n        if self._matplotlib_available\
    \ is None:\n            try:\n                import matplotlib.pyplot as plt\n\
    \                self._matplotlib_available = True\n            except ImportError:\n\
    \                self._matplotlib_available = False\n        return self._matplotlib_available\n\
    \    \n    def create_plots(self, results: List[BenchmarkResult], config: Any)\
    \ -> None:\n        \"\"\"Create matplotlib plots from benchmark results\"\"\"\
    \n        if not self.can_render():\n            return\n        \n        import\
    \ matplotlib.pyplot as plt\n        \n        operations = PlotDataProcessor.group_by_operation(results)\n\
    \        output_dir = Path(getattr(config, 'output_dir', './output/benchmark_results'))\n\
    \        name = getattr(config, 'name', 'benchmark')\n        \n        for operation,\
    \ op_results in operations.items():\n            self._create_performance_plot(plt,\
    \ op_results, operation, output_dir, name)\n            self._create_speedup_plot(plt,\
    \ op_results, operation, output_dir, name)\n    \n    def _create_performance_plot(self,\
    \ plt, results: List[BenchmarkResult], \n                                operation:\
    \ str, output_dir: Path, name: str) -> None:\n        \"\"\"Create performance\
    \ vs size plot\"\"\"\n        data = PlotDataProcessor.group_by_implementation_and_size(results)\n\
    \        \n        plt.figure(figsize=(10, 6))\n        \n        for impl, size_times\
    \ in data.items():\n            sizes = sorted(size_times.keys())\n          \
    \  times = [size_times[size] for size in sizes]\n            plt.plot(sizes, times,\
    \ marker='o', label=impl)\n        \n        if self.plot_scale == \"loglog\"\
    :\n            plt.loglog()\n        elif self.plot_scale == \"semilogx\":\n \
    \           plt.semilogx()\n        elif self.plot_scale == \"semilogy\":\n  \
    \          plt.semilogy()\n        \n        plt.xlabel('Size')\n        plt.ylabel('Time\
    \ (ms)')\n        plt.title(f'Performance vs Size - {name} - {operation}')\n \
    \       plt.legend()\n        plt.grid(True)\n        \n        output_dir.mkdir(parents=True,\
    \ exist_ok=True)\n        filename = output_dir / f\"{name}_{operation}_performance.png\"\
    \n        plt.savefig(filename, dpi=300, bbox_inches='tight')\n        plt.close()\n\
    \        print(f\"Plot saved: {filename}\")\n    \n    def _create_speedup_plot(self,\
    \ plt, results: List[BenchmarkResult], \n                           operation:\
    \ str, output_dir: Path, name: str) -> None:\n        \"\"\"Create speedup vs\
    \ size line plot\"\"\"\n        data = PlotDataProcessor.group_by_implementation_and_size(results)\n\
    \        \n        if len(data) < 2:\n            return  # Need at least 2 implementations\
    \ for speedup\n        \n        # Get all sizes and sort them\n        all_sizes\
    \ = set()\n        for size_times in data.values():\n            all_sizes.update(size_times.keys())\n\
    \        sizes = sorted(all_sizes)\n        \n        # Find baseline (slowest\
    \ implementation at each size)\n        baseline_times = {}\n        for size\
    \ in sizes:\n            size_times = []\n            for impl, impl_data in data.items():\n\
    \                if size in impl_data:\n                    size_times.append(impl_data[size])\n\
    \            if size_times:\n                baseline_times[size] = max(size_times)\
    \  # Slowest time as baseline\n        \n        plt.figure(figsize=(10, 6))\n\
    \        \n        # Plot speedup line for each implementation\n        for impl,\
    \ size_times in data.items():\n            impl_sizes = []\n            speedups\
    \ = []\n            \n            for size in sizes:\n                if size\
    \ in size_times and size in baseline_times:\n                    speedup = baseline_times[size]\
    \ / size_times[size]\n                    impl_sizes.append(size)\n          \
    \          speedups.append(speedup)\n            \n            if impl_sizes:\
    \  # Only plot if we have data\n                plt.plot(impl_sizes, speedups,\
    \ marker='o', label=impl, linewidth=2)\n        \n        if self.plot_scale ==\
    \ \"loglog\":\n            plt.loglog()\n        elif self.plot_scale == \"semilogx\"\
    :\n            plt.semilogx()\n        elif self.plot_scale == \"semilogy\":\n\
    \            plt.semilogy()\n        \n        plt.xlabel('Size')\n        plt.ylabel('Speedup\
    \ (relative to slowest)')\n        plt.title(f'Speedup vs Size - {name} - {operation}')\n\
    \        plt.legend()\n        plt.grid(True, alpha=0.3)\n        \n        #\
    \ Add horizontal line at speedup = 1.0\n        plt.axhline(y=1.0, color='gray',\
    \ linestyle='--', alpha=0.5, label='Baseline')\n        \n        output_dir.mkdir(parents=True,\
    \ exist_ok=True)\n        filename = output_dir / f\"{name}_{operation}_speedup.png\"\
    \n        plt.savefig(filename, dpi=300, bbox_inches='tight')\n        plt.close()\n\
    \        print(f\"Plot saved: {filename}\")\n\n\nclass ASCIIRenderer(PlotRenderer):\n\
    \    \"\"\"ASCII-based plot renderer (fallback when matplotlib unavailable)\"\"\
    \"\n    \n    def can_render(self) -> bool:\n        \"\"\"ASCII renderer is always\
    \ available\"\"\"\n        return True\n    \n    def create_plots(self, results:\
    \ List[BenchmarkResult], config: Any) -> None:\n        \"\"\"Create ASCII plots\
    \ from benchmark results\"\"\"\n        operations = PlotDataProcessor.group_by_operation(results)\n\
    \        output_dir = Path(getattr(config, 'output_dir', './output/benchmark_results'))\n\
    \        name = getattr(config, 'name', 'benchmark')\n        \n        print(\"\
    \\nGenerating ASCII plots in\", output_dir)\n        \n        for operation,\
    \ op_results in operations.items():\n            self._create_ascii_performance_plot(op_results,\
    \ operation, output_dir, name)\n            self._create_ascii_speedup_plot(op_results,\
    \ operation, output_dir, name)\n            self._create_ascii_comparison_table(op_results,\
    \ operation, output_dir, name)\n    \n    def _create_ascii_performance_plot(self,\
    \ results: List[BenchmarkResult], \n                                     operation:\
    \ str, output_dir: Path, name: str) -> None:\n        \"\"\"Create ASCII performance\
    \ vs size plot\"\"\"\n        data = PlotDataProcessor.group_by_implementation_and_size(results)\n\
    \        \n        if not data:\n            return\n        \n        # Get all\
    \ sizes and sort them\n        all_sizes = set()\n        for size_times in data.values():\n\
    \            all_sizes.update(size_times.keys())\n        sizes = sorted(all_sizes)\n\
    \        \n        output_dir.mkdir(parents=True, exist_ok=True)\n        filename\
    \ = output_dir / f\"{name}_{operation}_size_plot.txt\"\n        \n        with\
    \ open(filename, 'w') as f:\n            f.write(f\"Performance vs Size - {name}\
    \ - {operation}\\n\")\n            f.write(\"=\" * 60 + \"\\n\\n\")\n        \
    \    \n            # Header\n            header = f\"{'Size':<12}\"\n        \
    \    for impl in sorted(data.keys()):\n                header += f\"{impl:<15}\"\
    \n            f.write(header + \"\\n\")\n            f.write(\"-\" * len(header)\
    \ + \"\\n\")\n            \n            # Data rows\n            for size in sizes:\n\
    \                row = f\"{size:<12}\"\n                for impl in sorted(data.keys()):\n\
    \                    time_val = data[impl].get(size, 0)\n                    if\
    \ time_val > 0:\n                        row += f\"{time_val:<15.3f}\"\n     \
    \               else:\n                        row += f\"{'---':<15}\"\n     \
    \           f.write(row + \"\\n\")\n        \n        print(f\"ASCII plot saved:\
    \ {filename}\")\n    \n    def _create_ascii_speedup_plot(self, results: List[BenchmarkResult],\
    \ \n                                 operation: str, output_dir: Path, name: str)\
    \ -> None:\n        \"\"\"Create ASCII speedup vs size plot\"\"\"\n        data\
    \ = PlotDataProcessor.group_by_implementation_and_size(results)\n        \n  \
    \      if len(data) < 2:\n            return  # Need at least 2 implementations\
    \ for speedup\n        \n        # Get all sizes and sort them\n        all_sizes\
    \ = set()\n        for size_times in data.values():\n            all_sizes.update(size_times.keys())\n\
    \        sizes = sorted(all_sizes)\n        \n        # Find baseline (slowest\
    \ implementation at each size)\n        baseline_times = {}\n        for size\
    \ in sizes:\n            size_times = []\n            for impl, impl_data in data.items():\n\
    \                if size in impl_data:\n                    size_times.append(impl_data[size])\n\
    \            if size_times:\n                baseline_times[size] = max(size_times)\
    \  # Slowest time as baseline\n        \n        output_dir.mkdir(parents=True,\
    \ exist_ok=True)\n        filename = output_dir / f\"{name}_{operation}_speedup_plot.txt\"\
    \n        \n        with open(filename, 'w') as f:\n            f.write(f\"Speedup\
    \ vs Size - {name} - {operation}\\n\")\n            f.write(\"=\" * 60 + \"\\\
    n\\n\")\n            \n            # Header\n            header = f\"{'Size':<12}\"\
    \n            for impl in sorted(data.keys()):\n                header += f\"\
    {impl:<15}\"\n            f.write(header + \"\\n\")\n            f.write(\"-\"\
    \ * len(header) + \"\\n\")\n            \n            # Data rows\n          \
    \  for size in sizes:\n                if size not in baseline_times:\n      \
    \              continue\n                \n                row = f\"{size:<12}\"\
    \n                for impl in sorted(data.keys()):\n                    if size\
    \ in data[impl]:\n                        speedup = baseline_times[size] / data[impl][size]\n\
    \                        row += f\"{speedup:<15.2f}\"\n                    else:\n\
    \                        row += f\"{'---':<15}\"\n                f.write(row\
    \ + \"\\n\")\n        \n        print(f\"ASCII speedup plot saved: {filename}\"\
    )\n    \n    def _create_ascii_comparison_table(self, results: List[BenchmarkResult],\
    \ \n                                     operation: str, output_dir: Path, name:\
    \ str) -> None:\n        \"\"\"Create ASCII comparison table\"\"\"\n        stats\
    \ = PlotDataProcessor.calculate_statistics(results)\n        \n        if not\
    \ stats:\n            return\n        \n        output_dir.mkdir(parents=True,\
    \ exist_ok=True)\n        filename = output_dir / f\"{name}_{operation}_comparison.txt\"\
    \n        \n        with open(filename, 'w') as f:\n            f.write(f\"Implementation\
    \ Comparison - {name} - {operation}\\n\")\n            f.write(\"=\" * 70 + \"\
    \\n\\n\")\n            \n            # Header\n            header = f\"{'Implementation':<20}\
    \ {'Mean (ms)':<12} {'Min (ms)':<12} {'Max (ms)':<12} {'Count':<8}\"\n       \
    \     f.write(header + \"\\n\")\n            f.write(\"-\" * len(header) + \"\\\
    n\")\n            \n            # Sort by mean time\n            sorted_stats\
    \ = sorted(stats.items(), key=lambda x: x[1]['mean'])\n            \n        \
    \    # Data rows\n            for impl, stat in sorted_stats:\n              \
    \  row = (f\"{impl:<20} {stat['mean']:<12.3f} {stat['min']:<12.3f} \"\n      \
    \                f\"{stat['max']:<12.3f} {stat['count']:<8}\")\n             \
    \   f.write(row + \"\\n\")\n        \n        print(f\"Comparison table saved:\
    \ {filename}\")\n\n\nclass CompositeRenderer(PlotRenderer):\n    \"\"\"Composite\
    \ renderer that tries matplotlib first, falls back to ASCII\"\"\"\n    \n    def\
    \ __init__(self, plot_scale: str = \"loglog\"):\n        self.matplotlib_renderer\
    \ = MatplotlibRenderer(plot_scale)\n        self.ascii_renderer = ASCIIRenderer()\n\
    \    \n    def can_render(self) -> bool:\n        \"\"\"Composite renderer can\
    \ always render (ASCII fallback)\"\"\"\n        return True\n    \n    def create_plots(self,\
    \ results: List[BenchmarkResult], config: Any) -> None:\n        \"\"\"Create\
    \ plots using matplotlib if available, ASCII otherwise\"\"\"\n        if self.matplotlib_renderer.can_render():\n\
    \            self.matplotlib_renderer.create_plots(results, config)\n        else:\n\
    \            print(\"Matplotlib not available - using ASCII plots\")\n       \
    \     self.ascii_renderer.create_plots(results, config)\n"
  code: "\"\"\"\nPlot rendering implementations following Open/Closed Principle.\n\
    \"\"\"\n\nimport statistics\nfrom collections import defaultdict\nfrom pathlib\
    \ import Path\nfrom typing import List, Dict, Any\nfrom cp_library.perf.interfaces\
    \ import PlotRenderer, BenchmarkResult\n\n\nclass PlotDataProcessor:\n    \"\"\
    \"Utility class for processing benchmark data for plotting\"\"\"\n    \n    @staticmethod\n\
    \    def group_by_operation(results: List[BenchmarkResult]) -> Dict[str, List[BenchmarkResult]]:\n\
    \        \"\"\"Group results by operation\"\"\"\n        grouped = defaultdict(list)\n\
    \        for result in results:\n            if result.error is None and result.time_ms\
    \ != float('inf'):\n                grouped[result.operation].append(result)\n\
    \        return dict(grouped)\n    \n    @staticmethod\n    def group_by_implementation_and_size(results:\
    \ List[BenchmarkResult]) -> Dict[str, Dict[int, float]]:\n        \"\"\"Group\
    \ results by implementation and size\"\"\"\n        grouped = defaultdict(lambda:\
    \ defaultdict(float))\n        for result in results:\n            if result.error\
    \ is None and result.time_ms != float('inf'):\n                grouped[result.implementation][result.size]\
    \ = result.time_ms\n        return dict(grouped)\n    \n    @staticmethod\n  \
    \  def calculate_statistics(results: List[BenchmarkResult]) -> Dict[str, Dict[str,\
    \ float]]:\n        \"\"\"Calculate statistics for each implementation\"\"\"\n\
    \        impl_times = defaultdict(list)\n        for result in results:\n    \
    \        if result.error is None and result.time_ms != float('inf'):\n       \
    \         impl_times[result.implementation].append(result.time_ms)\n        \n\
    \        stats = {}\n        for impl, times in impl_times.items():\n        \
    \    if times:\n                stats[impl] = {\n                    'mean': statistics.mean(times),\n\
    \                    'min': min(times),\n                    'max': max(times),\n\
    \                    'count': len(times)\n                }\n        return stats\n\
    \n\nclass MatplotlibRenderer(PlotRenderer):\n    \"\"\"Matplotlib-based plot renderer\"\
    \"\"\n    \n    def __init__(self, plot_scale: str = \"loglog\"):\n        self.plot_scale\
    \ = plot_scale\n        self._matplotlib_available = None\n    \n    def can_render(self)\
    \ -> bool:\n        \"\"\"Check if matplotlib is available\"\"\"\n        if self._matplotlib_available\
    \ is None:\n            try:\n                import matplotlib.pyplot as plt\n\
    \                self._matplotlib_available = True\n            except ImportError:\n\
    \                self._matplotlib_available = False\n        return self._matplotlib_available\n\
    \    \n    def create_plots(self, results: List[BenchmarkResult], config: Any)\
    \ -> None:\n        \"\"\"Create matplotlib plots from benchmark results\"\"\"\
    \n        if not self.can_render():\n            return\n        \n        import\
    \ matplotlib.pyplot as plt\n        \n        operations = PlotDataProcessor.group_by_operation(results)\n\
    \        output_dir = Path(getattr(config, 'output_dir', './output/benchmark_results'))\n\
    \        name = getattr(config, 'name', 'benchmark')\n        \n        for operation,\
    \ op_results in operations.items():\n            self._create_performance_plot(plt,\
    \ op_results, operation, output_dir, name)\n            self._create_speedup_plot(plt,\
    \ op_results, operation, output_dir, name)\n    \n    def _create_performance_plot(self,\
    \ plt, results: List[BenchmarkResult], \n                                operation:\
    \ str, output_dir: Path, name: str) -> None:\n        \"\"\"Create performance\
    \ vs size plot\"\"\"\n        data = PlotDataProcessor.group_by_implementation_and_size(results)\n\
    \        \n        plt.figure(figsize=(10, 6))\n        \n        for impl, size_times\
    \ in data.items():\n            sizes = sorted(size_times.keys())\n          \
    \  times = [size_times[size] for size in sizes]\n            plt.plot(sizes, times,\
    \ marker='o', label=impl)\n        \n        if self.plot_scale == \"loglog\"\
    :\n            plt.loglog()\n        elif self.plot_scale == \"semilogx\":\n \
    \           plt.semilogx()\n        elif self.plot_scale == \"semilogy\":\n  \
    \          plt.semilogy()\n        \n        plt.xlabel('Size')\n        plt.ylabel('Time\
    \ (ms)')\n        plt.title(f'Performance vs Size - {name} - {operation}')\n \
    \       plt.legend()\n        plt.grid(True)\n        \n        output_dir.mkdir(parents=True,\
    \ exist_ok=True)\n        filename = output_dir / f\"{name}_{operation}_performance.png\"\
    \n        plt.savefig(filename, dpi=300, bbox_inches='tight')\n        plt.close()\n\
    \        print(f\"Plot saved: {filename}\")\n    \n    def _create_speedup_plot(self,\
    \ plt, results: List[BenchmarkResult], \n                           operation:\
    \ str, output_dir: Path, name: str) -> None:\n        \"\"\"Create speedup vs\
    \ size line plot\"\"\"\n        data = PlotDataProcessor.group_by_implementation_and_size(results)\n\
    \        \n        if len(data) < 2:\n            return  # Need at least 2 implementations\
    \ for speedup\n        \n        # Get all sizes and sort them\n        all_sizes\
    \ = set()\n        for size_times in data.values():\n            all_sizes.update(size_times.keys())\n\
    \        sizes = sorted(all_sizes)\n        \n        # Find baseline (slowest\
    \ implementation at each size)\n        baseline_times = {}\n        for size\
    \ in sizes:\n            size_times = []\n            for impl, impl_data in data.items():\n\
    \                if size in impl_data:\n                    size_times.append(impl_data[size])\n\
    \            if size_times:\n                baseline_times[size] = max(size_times)\
    \  # Slowest time as baseline\n        \n        plt.figure(figsize=(10, 6))\n\
    \        \n        # Plot speedup line for each implementation\n        for impl,\
    \ size_times in data.items():\n            impl_sizes = []\n            speedups\
    \ = []\n            \n            for size in sizes:\n                if size\
    \ in size_times and size in baseline_times:\n                    speedup = baseline_times[size]\
    \ / size_times[size]\n                    impl_sizes.append(size)\n          \
    \          speedups.append(speedup)\n            \n            if impl_sizes:\
    \  # Only plot if we have data\n                plt.plot(impl_sizes, speedups,\
    \ marker='o', label=impl, linewidth=2)\n        \n        if self.plot_scale ==\
    \ \"loglog\":\n            plt.loglog()\n        elif self.plot_scale == \"semilogx\"\
    :\n            plt.semilogx()\n        elif self.plot_scale == \"semilogy\":\n\
    \            plt.semilogy()\n        \n        plt.xlabel('Size')\n        plt.ylabel('Speedup\
    \ (relative to slowest)')\n        plt.title(f'Speedup vs Size - {name} - {operation}')\n\
    \        plt.legend()\n        plt.grid(True, alpha=0.3)\n        \n        #\
    \ Add horizontal line at speedup = 1.0\n        plt.axhline(y=1.0, color='gray',\
    \ linestyle='--', alpha=0.5, label='Baseline')\n        \n        output_dir.mkdir(parents=True,\
    \ exist_ok=True)\n        filename = output_dir / f\"{name}_{operation}_speedup.png\"\
    \n        plt.savefig(filename, dpi=300, bbox_inches='tight')\n        plt.close()\n\
    \        print(f\"Plot saved: {filename}\")\n\n\nclass ASCIIRenderer(PlotRenderer):\n\
    \    \"\"\"ASCII-based plot renderer (fallback when matplotlib unavailable)\"\"\
    \"\n    \n    def can_render(self) -> bool:\n        \"\"\"ASCII renderer is always\
    \ available\"\"\"\n        return True\n    \n    def create_plots(self, results:\
    \ List[BenchmarkResult], config: Any) -> None:\n        \"\"\"Create ASCII plots\
    \ from benchmark results\"\"\"\n        operations = PlotDataProcessor.group_by_operation(results)\n\
    \        output_dir = Path(getattr(config, 'output_dir', './output/benchmark_results'))\n\
    \        name = getattr(config, 'name', 'benchmark')\n        \n        print(\"\
    \\nGenerating ASCII plots in\", output_dir)\n        \n        for operation,\
    \ op_results in operations.items():\n            self._create_ascii_performance_plot(op_results,\
    \ operation, output_dir, name)\n            self._create_ascii_speedup_plot(op_results,\
    \ operation, output_dir, name)\n            self._create_ascii_comparison_table(op_results,\
    \ operation, output_dir, name)\n    \n    def _create_ascii_performance_plot(self,\
    \ results: List[BenchmarkResult], \n                                     operation:\
    \ str, output_dir: Path, name: str) -> None:\n        \"\"\"Create ASCII performance\
    \ vs size plot\"\"\"\n        data = PlotDataProcessor.group_by_implementation_and_size(results)\n\
    \        \n        if not data:\n            return\n        \n        # Get all\
    \ sizes and sort them\n        all_sizes = set()\n        for size_times in data.values():\n\
    \            all_sizes.update(size_times.keys())\n        sizes = sorted(all_sizes)\n\
    \        \n        output_dir.mkdir(parents=True, exist_ok=True)\n        filename\
    \ = output_dir / f\"{name}_{operation}_size_plot.txt\"\n        \n        with\
    \ open(filename, 'w') as f:\n            f.write(f\"Performance vs Size - {name}\
    \ - {operation}\\n\")\n            f.write(\"=\" * 60 + \"\\n\\n\")\n        \
    \    \n            # Header\n            header = f\"{'Size':<12}\"\n        \
    \    for impl in sorted(data.keys()):\n                header += f\"{impl:<15}\"\
    \n            f.write(header + \"\\n\")\n            f.write(\"-\" * len(header)\
    \ + \"\\n\")\n            \n            # Data rows\n            for size in sizes:\n\
    \                row = f\"{size:<12}\"\n                for impl in sorted(data.keys()):\n\
    \                    time_val = data[impl].get(size, 0)\n                    if\
    \ time_val > 0:\n                        row += f\"{time_val:<15.3f}\"\n     \
    \               else:\n                        row += f\"{'---':<15}\"\n     \
    \           f.write(row + \"\\n\")\n        \n        print(f\"ASCII plot saved:\
    \ {filename}\")\n    \n    def _create_ascii_speedup_plot(self, results: List[BenchmarkResult],\
    \ \n                                 operation: str, output_dir: Path, name: str)\
    \ -> None:\n        \"\"\"Create ASCII speedup vs size plot\"\"\"\n        data\
    \ = PlotDataProcessor.group_by_implementation_and_size(results)\n        \n  \
    \      if len(data) < 2:\n            return  # Need at least 2 implementations\
    \ for speedup\n        \n        # Get all sizes and sort them\n        all_sizes\
    \ = set()\n        for size_times in data.values():\n            all_sizes.update(size_times.keys())\n\
    \        sizes = sorted(all_sizes)\n        \n        # Find baseline (slowest\
    \ implementation at each size)\n        baseline_times = {}\n        for size\
    \ in sizes:\n            size_times = []\n            for impl, impl_data in data.items():\n\
    \                if size in impl_data:\n                    size_times.append(impl_data[size])\n\
    \            if size_times:\n                baseline_times[size] = max(size_times)\
    \  # Slowest time as baseline\n        \n        output_dir.mkdir(parents=True,\
    \ exist_ok=True)\n        filename = output_dir / f\"{name}_{operation}_speedup_plot.txt\"\
    \n        \n        with open(filename, 'w') as f:\n            f.write(f\"Speedup\
    \ vs Size - {name} - {operation}\\n\")\n            f.write(\"=\" * 60 + \"\\\
    n\\n\")\n            \n            # Header\n            header = f\"{'Size':<12}\"\
    \n            for impl in sorted(data.keys()):\n                header += f\"\
    {impl:<15}\"\n            f.write(header + \"\\n\")\n            f.write(\"-\"\
    \ * len(header) + \"\\n\")\n            \n            # Data rows\n          \
    \  for size in sizes:\n                if size not in baseline_times:\n      \
    \              continue\n                \n                row = f\"{size:<12}\"\
    \n                for impl in sorted(data.keys()):\n                    if size\
    \ in data[impl]:\n                        speedup = baseline_times[size] / data[impl][size]\n\
    \                        row += f\"{speedup:<15.2f}\"\n                    else:\n\
    \                        row += f\"{'---':<15}\"\n                f.write(row\
    \ + \"\\n\")\n        \n        print(f\"ASCII speedup plot saved: {filename}\"\
    )\n    \n    def _create_ascii_comparison_table(self, results: List[BenchmarkResult],\
    \ \n                                     operation: str, output_dir: Path, name:\
    \ str) -> None:\n        \"\"\"Create ASCII comparison table\"\"\"\n        stats\
    \ = PlotDataProcessor.calculate_statistics(results)\n        \n        if not\
    \ stats:\n            return\n        \n        output_dir.mkdir(parents=True,\
    \ exist_ok=True)\n        filename = output_dir / f\"{name}_{operation}_comparison.txt\"\
    \n        \n        with open(filename, 'w') as f:\n            f.write(f\"Implementation\
    \ Comparison - {name} - {operation}\\n\")\n            f.write(\"=\" * 70 + \"\
    \\n\\n\")\n            \n            # Header\n            header = f\"{'Implementation':<20}\
    \ {'Mean (ms)':<12} {'Min (ms)':<12} {'Max (ms)':<12} {'Count':<8}\"\n       \
    \     f.write(header + \"\\n\")\n            f.write(\"-\" * len(header) + \"\\\
    n\")\n            \n            # Sort by mean time\n            sorted_stats\
    \ = sorted(stats.items(), key=lambda x: x[1]['mean'])\n            \n        \
    \    # Data rows\n            for impl, stat in sorted_stats:\n              \
    \  row = (f\"{impl:<20} {stat['mean']:<12.3f} {stat['min']:<12.3f} \"\n      \
    \                f\"{stat['max']:<12.3f} {stat['count']:<8}\")\n             \
    \   f.write(row + \"\\n\")\n        \n        print(f\"Comparison table saved:\
    \ {filename}\")\n\n\nclass CompositeRenderer(PlotRenderer):\n    \"\"\"Composite\
    \ renderer that tries matplotlib first, falls back to ASCII\"\"\"\n    \n    def\
    \ __init__(self, plot_scale: str = \"loglog\"):\n        self.matplotlib_renderer\
    \ = MatplotlibRenderer(plot_scale)\n        self.ascii_renderer = ASCIIRenderer()\n\
    \    \n    def can_render(self) -> bool:\n        \"\"\"Composite renderer can\
    \ always render (ASCII fallback)\"\"\"\n        return True\n    \n    def create_plots(self,\
    \ results: List[BenchmarkResult], config: Any) -> None:\n        \"\"\"Create\
    \ plots using matplotlib if available, ASCII otherwise\"\"\"\n        if self.matplotlib_renderer.can_render():\n\
    \            self.matplotlib_renderer.create_plots(results, config)\n        else:\n\
    \            print(\"Matplotlib not available - using ASCII plots\")\n       \
    \     self.ascii_renderer.create_plots(results, config)"
  dependsOn:
  - cp_library/perf/interfaces.py
  isVerificationFile: false
  path: cp_library/perf/renderers.py
  requiredBy:
  - cp_library/perf/benchmark.py
  - perf/bool_list.py
  - perf/view2.py
  - perf/heap_view.py
  - perf/list_view.py
  - perf/mlist.py
  - perf/que.py
  - perf/list6.py
  - perf/grid.py
  - perf/edge_list.py
  - perf/csr.py
  - perf/bit6.py
  - perf/deque.py
  - perf/segtree2.py
  - perf/view6.py
  - perf/csr6.py
  - perf/segtree6.py
  - perf/csr2.py
  - perf/bit2.py
  - perf/rank.py
  - perf/list2.py
  - perf/heap_csr.py
  - perf/bytearray_decode.py
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/renderers.py
layout: document
redirect_from:
- /library/cp_library/perf/renderers.py
- /library/cp_library/perf/renderers.py.html
title: cp_library/perf/renderers.py
---
