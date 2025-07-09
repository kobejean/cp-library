---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/perf/benchmark.py
    title: cp_library/perf/benchmark.py
  - icon: ':warning:'
    path: cp_library/perf/generators.py
    title: cp_library/perf/generators.py
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
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 80, in visit_ImportFrom\n    self.process_module(node, module_path, file_is_top_level,\
    \ from_import=True, import_names=node.names)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 92, in process_module\n    imported_code = self.bundler.import_file(module_path,\
    \ is_top_level)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 31, in import_file\n    self.process_file(file_path, is_top_level)\n  File\
    \ \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
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
  code: "\"\"\"Simple example of using the benchmarking framework\"\"\"\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig, TestCase\nfrom cp_library.perf.generators\
    \ import RandomArrayGenerator, SortedArrayGenerator\nfrom typing import Dict,\
    \ List, Any, Callable\n\nclass SimpleSortBenchmark(Benchmark):\n    \"\"\"Example\
    \ benchmark comparing different sorting approaches\"\"\"\n    \n    def generate_test_cases(self,\
    \ param_grid: Dict[str, List[Any]]) -> List[TestCase]:\n        test_cases = []\n\
    \        \n        for size in param_grid['size']:\n            # Random data\n\
    \            random_gen = RandomArrayGenerator()\n            test_cases.append(TestCase(\n\
    \                name=f\"random_size_{size}\",\n                params={'size':\
    \ size, 'type': 'random'},\n                data=random_gen.generate(size)\n \
    \           ))\n            \n            # Sorted data\n            sorted_gen\
    \ = SortedArrayGenerator()\n            test_cases.append(TestCase(\n        \
    \        name=f\"sorted_size_{size}\",\n                params={'size': size,\
    \ 'type': 'sorted'},\n                data=sorted_gen.generate(size)\n       \
    \     ))\n            \n            # Reverse sorted\n            reverse_gen\
    \ = SortedArrayGenerator(reverse=True)\n            test_cases.append(TestCase(\n\
    \                name=f\"reverse_size_{size}\",\n                params={'size':\
    \ size, 'type': 'reverse'},\n                data=reverse_gen.generate(size)\n\
    \            ))\n        \n        return test_cases\n    \n    def get_implementations(self)\
    \ -> Dict[str, Callable]:\n        \"\"\"Different sorting implementations to\
    \ compare\"\"\"\n        return {\n            'builtin_sort': lambda data: sorted(data),\n\
    \            'list_sort': lambda data: (data.copy(), data.sort())[0],\n      \
    \      'custom_sort': lambda data: self._custom_sort(data.copy())\n        }\n\
    \    \n    def _custom_sort(self, data):\n        \"\"\"Example custom sorting\
    \ implementation\"\"\"\n        # Simple selection sort for demonstration\n  \
    \      n = len(data)\n        for i in range(n):\n            min_idx = i\n  \
    \          for j in range(i + 1, n):\n                if data[j] < data[min_idx]:\n\
    \                    min_idx = j\n            data[i], data[min_idx] = data[min_idx],\
    \ data[i]\n        return data\n\ndef main():\n    \"\"\"Run the example benchmark\"\
    \"\"\n    \n    # Create configuration\n    config = BenchmarkConfig(\n      \
    \  name=\"sorting_example\",\n        iterations=5,\n        warmup=1,\n     \
    \   save_results=True,\n        plot_results=False,  # Set to True if you have\
    \ matplotlib\n        output_dir=\"./benchmark_results/example\"\n    )\n    \n\
    \    # Create and run benchmark\n    benchmark = SimpleSortBenchmark(config)\n\
    \    \n    # Small sizes for the example\n    param_grid = {\n        'size':\
    \ [10, 50, 100, 500]\n    }\n    \n    benchmark.run(param_grid)\n    \n    #\
    \ Access results programmatically\n    print(\"\\nAccessing results programmatically:\"\
    )\n    for result in benchmark.results[:5]:  # First 5 results\n        if result.error\
    \ is None:\n            print(f\"  {result.test_case.name}: {result.implementation}\
    \ = {result.time_ms:.3f}ms\")\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/perf/generators.py
  - cp_library/perf/plotters.py
  isVerificationFile: false
  path: cp_library/perf/examples/simple_usage.py
  requiredBy: []
  timestamp: '2025-07-09 08:31:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/examples/simple_usage.py
layout: document
redirect_from:
- /library/cp_library/perf/examples/simple_usage.py
- /library/cp_library/perf/examples/simple_usage.py.html
title: cp_library/perf/examples/simple_usage.py
---
