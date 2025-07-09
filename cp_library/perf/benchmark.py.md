---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/perf/plotters.py
    title: cp_library/perf/plotters.py
  _extendedRequiredBy:
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
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 426, in generic_visit\n    self.visit(item)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/ast.py\"\
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 64, in visit_ImportFrom\n    raise NotImplementedError(\"Relative imports\
    \ are not supported\")\nNotImplementedError: Relative imports are not supported\n"
  code: "import cp_library.__header__\nimport cp_library.perf.__header__\nimport time\n\
    import json\nfrom abc import ABC, abstractmethod\nfrom typing import Any, Dict,\
    \ List, Tuple, Callable, Optional\nfrom dataclasses import dataclass\nfrom pathlib\
    \ import Path\n\n@dataclass\nclass BenchmarkConfig:\n    \"\"\"Configuration for\
    \ a benchmark run\"\"\"\n    name: str\n    iterations: int = 10\n    warmup:\
    \ int = 2\n    timeout: float = 60.0  # seconds\n    save_results: bool = True\n\
    \    plot_results: bool = True\n    output_dir: str = \"./benchmark_results\"\n\
    \n@dataclass\nclass TestCase:\n    \"\"\"A single test case with parameters and\
    \ data\"\"\"\n    name: str\n    params: Dict[str, Any]\n    data: Any\n    expected:\
    \ Optional[Any] = None\n\n@dataclass\nclass BenchmarkResult:\n    \"\"\"Result\
    \ from running a single benchmark\"\"\"\n    test_case: TestCase\n    implementation:\
    \ str\n    time_ms: float\n    memory_mb: float = 0.0\n    correct: bool = True\n\
    \    error: Optional[str] = None\n    \nclass Benchmark(ABC):\n    \"\"\"Base\
    \ class for benchmarks\"\"\"\n    \n    def __init__(self, config: BenchmarkConfig):\n\
    \        self.config = config\n        self.results: List[BenchmarkResult] = []\n\
    \        \n    @abstractmethod\n    def generate_test_cases(self, param_grid:\
    \ Dict[str, List[Any]]) -> List[TestCase]:\n        \"\"\"Generate test cases\
    \ from parameter grid\"\"\"\n        pass\n    \n    @abstractmethod\n    def\
    \ get_implementations(self) -> Dict[str, Callable]:\n        \"\"\"Return dict\
    \ of implementation name -> function\"\"\"\n        pass\n    \n    def validate_result(self,\
    \ expected: Any, actual: Any) -> bool:\n        \"\"\"Validate if result is correct\"\
    \"\"\n        return expected == actual\n    \n    def measure_time(self, func:\
    \ Callable, *args, **kwargs) -> Tuple[Any, float]:\n        \"\"\"Measure execution\
    \ time of a function\"\"\"\n        # Warmup\n        for _ in range(self.config.warmup):\n\
    \            func(*args, **kwargs)\n        \n        # Actual measurement\n \
    \       start = time.perf_counter()\n        for _ in range(self.config.iterations):\n\
    \            result = func(*args, **kwargs)\n        elapsed_ms = (time.perf_counter()\
    \ - start) * 1000 / self.config.iterations\n        \n        return result, elapsed_ms\n\
    \    \n    def run(self, param_grid: Dict[str, List[Any]]):\n        \"\"\"Run\
    \ the benchmark\"\"\"\n        test_cases = self.generate_test_cases(param_grid)\n\
    \        implementations = self.get_implementations()\n        \n        print(f\"\
    Running {self.config.name}\")\n        print(f\"Test cases: {len(test_cases)},\
    \ Implementations: {len(implementations)}\")\n        print(\"-\" * 80)\n    \
    \    \n        for test_case in test_cases:\n            print(f\"\\nTest: {test_case.name}\"\
    )\n            \n            # Get reference result if not provided\n        \
    \    if test_case.expected is None and implementations:\n                ref_impl\
    \ = next(iter(implementations.values()))\n                test_case.expected,\
    \ _ = self.measure_time(ref_impl, test_case.data)\n            \n            for\
    \ impl_name, impl_func in implementations.items():\n                try:\n   \
    \                 result, time_ms = self.measure_time(impl_func, test_case.data)\n\
    \                    correct = self.validate_result(test_case.expected, result)\n\
    \                    \n                    bench_result = BenchmarkResult(\n \
    \                       test_case=test_case,\n                        implementation=impl_name,\n\
    \                        time_ms=time_ms,\n                        correct=correct\n\
    \                    )\n                    self.results.append(bench_result)\n\
    \                    \n                    print(f\"  {impl_name:<20} {time_ms:>10.3f}\
    \ ms  {'\u2713' if correct else '\u2717'}\")\n                    \n         \
    \       except Exception as e:\n                    bench_result = BenchmarkResult(\n\
    \                        test_case=test_case,\n                        implementation=impl_name,\n\
    \                        time_ms=float('inf'),\n                        correct=False,\n\
    \                        error=str(e)\n                    )\n               \
    \     self.results.append(bench_result)\n                    print(f\"  {impl_name:<20}\
    \ ERROR: {str(e)[:50]}\")\n        \n        if self.config.save_results:\n  \
    \          self.save_results()\n        \n        if self.config.plot_results:\n\
    \            self.plot_results()\n    \n    def save_results(self):\n        \"\
    \"\"Save results to JSON file\"\"\"\n        Path(self.config.output_dir).mkdir(parents=True,\
    \ exist_ok=True)\n        \n        data = []\n        for r in self.results:\n\
    \            data.append({\n                'test_case': r.test_case.name,\n \
    \               'params': r.test_case.params,\n                'implementation':\
    \ r.implementation,\n                'time_ms': r.time_ms,\n                'correct':\
    \ r.correct,\n                'error': r.error\n            })\n        \n   \
    \     filename = f\"{self.config.output_dir}/{self.config.name}_{int(time.time())}.json\"\
    \n        with open(filename, 'w') as f:\n            json.dump(data, f, indent=2)\n\
    \        print(f\"\\nResults saved to {filename}\")\n    \n    def plot_results(self):\n\
    \        \"\"\"Create visualizations of results\"\"\"\n        try:\n        \
    \    from .plotters import BenchmarkPlotter\n            plotter = BenchmarkPlotter()\n\
    \            plotter.plot_results(self.results, self.config)\n        except ImportError\
    \ as e:\n            print(f\"Plotting skipped: {e}\")\n            print(\"To\
    \ enable plotting, install: pip install matplotlib pandas\")\n        except Exception\
    \ as e:\n            print(f\"Plotting failed: {e}\")"
  dependsOn:
  - cp_library/perf/plotters.py
  isVerificationFile: false
  path: cp_library/perf/benchmark.py
  requiredBy:
  - cp_library/perf/simple_plots.py
  - cp_library/perf/examples/simple_usage.py
  - cp_library/perf/examples/rank_benchmark.py
  - perf/bool_list_benchmark.py
  - perf/rank_perf.py
  timestamp: '2025-07-09 08:31:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/benchmark.py
layout: document
redirect_from:
- /library/cp_library/perf/benchmark.py
- /library/cp_library/perf/benchmark.py.html
title: cp_library/perf/benchmark.py
---
