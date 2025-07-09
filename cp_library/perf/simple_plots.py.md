---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/perf/benchmark.py
    title: cp_library/perf/benchmark.py
  - icon: ':warning:'
    path: cp_library/perf/plotters.py
    title: cp_library/perf/plotters.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 101, in bundle\n    return bundler.update(path)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 154, in update\n    self.process_file(path)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 24, in process_file\n    self.bundled_code[file_path] = self.process_imports(tree,\
    \ file_path, source, file_is_top_level)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 102, in process_imports\n    processor.visit(tree)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 426, in generic_visit\n    self.visit(item)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 426, in generic_visit\n    self.visit(item)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 426, in generic_visit\n    self.visit(item)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 64, in visit_ImportFrom\n    raise NotImplementedError(\"Relative imports\
    \ are not supported\")\nNotImplementedError: Relative imports are not supported\n"
  code: "import cp_library.__header__\nimport cp_library.perf.__header__\n\"\"\"Simple\
    \ ASCII plotting for when matplotlib is not available\"\"\"\n\nfrom typing import\
    \ List, Dict, Any\nfrom pathlib import Path\nimport json\n\nclass ASCIIPlotter:\n\
    \    \"\"\"Create simple ASCII plots when matplotlib is not available\"\"\"\n\
    \    \n    def plot_results(self, results: List, config):\n        \"\"\"Create\
    \ ASCII plots for benchmark results\"\"\"\n        if not results:\n         \
    \   return\n            \n        # Convert results to data\n        data = []\n\
    \        for r in results:\n            if r.time_ms != float('inf'):\n      \
    \          row = {\n                    'implementation': r.implementation,\n\
    \                    'time_ms': r.time_ms,\n                    'test_case': r.test_case.name\n\
    \                }\n                row.update(r.test_case.params)\n         \
    \       data.append(row)\n        \n        if not data:\n            return\n\
    \        \n        # Create output directory\n        output_dir = Path(config.output_dir)\n\
    \        output_dir.mkdir(parents=True, exist_ok=True)\n        \n        print(f\"\
    \\nGenerating ASCII plots in {output_dir}/\")\n        \n        # Create size\
    \ vs performance plot\n        if any('size' in row for row in data):\n      \
    \      self._create_size_plot(data, config.name, output_dir)\n        \n     \
    \   # Create implementation comparison\n        self._create_comparison_table(data,\
    \ config.name, output_dir)\n    \n    def _create_size_plot(self, data: List[Dict],\
    \ name: str, output_dir: Path):\n        \"\"\"Create ASCII plot of performance\
    \ vs size\"\"\"\n        # Group by implementation and size\n        impl_data\
    \ = {}\n        for row in data:\n            if 'size' in row:\n            \
    \    impl = row['implementation']\n                size = row['size']\n      \
    \          time_ms = row['time_ms']\n                \n                if impl\
    \ not in impl_data:\n                    impl_data[impl] = {}\n              \
    \  if size not in impl_data[impl]:\n                    impl_data[impl][size]\
    \ = []\n                impl_data[impl][size].append(time_ms)\n        \n    \
    \    # Calculate averages\n        for impl in impl_data:\n            for size\
    \ in impl_data[impl]:\n                impl_data[impl][size] = sum(impl_data[impl][size])\
    \ / len(impl_data[impl][size])\n        \n        # Create ASCII plot\n      \
    \  plot_lines = []\n        plot_lines.append(f\"Performance vs Size - {name}\"\
    )\n        plot_lines.append(\"=\" * 50)\n        plot_lines.append(\"\")\n  \
    \      \n        if impl_data:\n            # Get all sizes\n            all_sizes\
    \ = set()\n            for impl in impl_data:\n                all_sizes.update(impl_data[impl].keys())\n\
    \            all_sizes = sorted(all_sizes)\n            \n            # Create\
    \ table\n            plot_lines.append(f\"{'Size':<12} \" + \"\".join(f\"{impl:<15}\"\
    \ for impl in impl_data.keys()))\n            plot_lines.append(\"-\" * (12 +\
    \ 15 * len(impl_data)))\n            \n            for size in all_sizes:\n  \
    \              line = f\"{size:<12} \"\n                for impl in impl_data.keys():\n\
    \                    time_val = impl_data[impl].get(size, 0)\n               \
    \     line += f\"{time_val:<15.3f}\"\n                plot_lines.append(line)\n\
    \        \n        # Save to file\n        filename = output_dir / f\"{name}_size_plot.txt\"\
    \n        with open(filename, 'w') as f:\n            f.write('\\n'.join(plot_lines))\n\
    \        print(f\"ASCII plot saved: {filename}\")\n    \n    def _create_comparison_table(self,\
    \ data: List[Dict], name: str, output_dir: Path):\n        \"\"\"Create comparison\
    \ table\"\"\"\n        # Group by implementation\n        impl_times = {}\n  \
    \      for row in data:\n            impl = row['implementation']\n          \
    \  if impl not in impl_times:\n                impl_times[impl] = []\n       \
    \     impl_times[impl].append(row['time_ms'])\n        \n        # Calculate statistics\n\
    \        stats = {}\n        for impl, times in impl_times.items():\n        \
    \    stats[impl] = {\n                'mean': sum(times) / len(times),\n     \
    \           'min': min(times),\n                'max': max(times),\n         \
    \       'count': len(times)\n            }\n        \n        # Create comparison\
    \ table\n        table_lines = []\n        table_lines.append(f\"Implementation\
    \ Comparison - {name}\")\n        table_lines.append(\"=\" * 60)\n        table_lines.append(\"\
    \")\n        table_lines.append(f\"{'Implementation':<20} {'Mean (ms)':<12} {'Min\
    \ (ms)':<12} {'Max (ms)':<12} {'Count':<8}\")\n        table_lines.append(\"-\"\
    \ * 68)\n        \n        for impl, stat in stats.items():\n            table_lines.append(\n\
    \                f\"{impl:<20} {stat['mean']:<12.3f} {stat['min']:<12.3f} \"\n\
    \                f\"{stat['max']:<12.3f} {stat['count']:<8}\"\n            )\n\
    \        \n        # Calculate speedup if 2 implementations\n        if len(stats)\
    \ == 2:\n            impls = list(stats.keys())\n            ratio = stats[impls[0]]['mean']\
    \ / stats[impls[1]]['mean']\n            faster = impls[1] if ratio > 1 else impls[0]\n\
    \            speedup = max(ratio, 1/ratio)\n            \n            table_lines.append(\"\
    \")\n            table_lines.append(f\"{faster} is {speedup:.2f}x faster on average\"\
    )\n        \n        # Save to file\n        filename = output_dir / f\"{name}_comparison.txt\"\
    \n        with open(filename, 'w') as f:\n            f.write('\\n'.join(table_lines))\n\
    \        print(f\"Comparison table saved: {filename}\")\n\n# Enhanced benchmark\
    \ class that falls back to ASCII plots\ndef enhanced_plot_results(self):\n   \
    \ \"\"\"Enhanced plot_results method with ASCII fallback\"\"\"\n    try:\n   \
    \     from .plotters import BenchmarkPlotter\n        plotter = BenchmarkPlotter()\n\
    \        plotter.plot_results(self.results, self.config)\n    except ImportError:\n\
    \        # Fall back to ASCII plots\n        ascii_plotter = ASCIIPlotter()\n\
    \        ascii_plotter.plot_results(self.results, self.config)\n        print(\"\
    Used ASCII plots (install matplotlib/pandas for visual plots)\")\n    except Exception\
    \ as e:\n        print(f\"Plotting failed: {e}\")\n\n# Monkey patch the Benchmark\
    \ class\nif __name__ != \"__main__\":\n    from .benchmark import Benchmark\n\
    \    Benchmark.plot_results = enhanced_plot_results"
  dependsOn:
  - cp_library/perf/plotters.py
  - cp_library/perf/benchmark.py
  isVerificationFile: false
  path: cp_library/perf/simple_plots.py
  requiredBy: []
  timestamp: '2025-07-09 08:31:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/simple_plots.py
layout: document
redirect_from:
- /library/cp_library/perf/simple_plots.py
- /library/cp_library/perf/simple_plots.py.html
title: cp_library/perf/simple_plots.py
---
