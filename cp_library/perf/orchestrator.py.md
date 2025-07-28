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
    , line 64, in visit_ImportFrom\n    raise NotImplementedError(\"Relative imports\
    \ are not supported\")\nNotImplementedError: Relative imports are not supported\n"
  code: "\"\"\"\nBenchmark orchestrator implementation following Single Responsibility\
    \ Principle.\n\"\"\"\n\nimport sys\nfrom typing import List\nfrom .interfaces\
    \ import (\n    BenchmarkOrchestrator, BenchmarkRegistry, BenchmarkResult, \n\
    \    TimerInterface, OutputManager\n)\n\n\nclass BenchmarkOrchestratorImpl(BenchmarkOrchestrator):\n\
    \    \"\"\"Implementation of benchmark execution orchestration\"\"\"\n    \n \
    \   def __init__(self, \n                 registry: BenchmarkRegistry,\n     \
    \            timer: TimerInterface,\n                 output_manager: OutputManager\
    \ = None):\n        self.registry = registry\n        self.timer = timer\n   \
    \     self.output_manager = output_manager\n        self.results: List[BenchmarkResult]\
    \ = []\n    \n    def run_benchmarks(self, operations: List[str], sizes: List[int])\
    \ -> List[BenchmarkResult]:\n        \"\"\"Execute benchmarks and return results\"\
    \"\"\n        self.results = []\n        \n        for operation in operations:\n\
    \            for size in sizes:\n                self._run_single(operation, size)\n\
    \        \n        if self.output_manager:\n            self.output_manager.save_results(self.results,\
    \ None)\n        \n        return self.results\n    \n    def _run_single(self,\
    \ operation: str, size: int) -> None:\n        \"\"\"Run a single operation/size\
    \ combination\"\"\"\n        print(f\"\\nOperation: {operation}, Size: {size}\"\
    )\n        print(\"-\" * 50)\n        sys.stdout.flush()\n        \n        #\
    \ Generate test data\n        generator = self.registry.get_data_generator(operation)\n\
    \        if not generator:\n            raise ValueError(f\"No data generator\
    \ for operation: {operation}\")\n        \n        test_data = generator.generate(size,\
    \ operation)\n        \n        # Get implementations for this operation\n   \
    \     impls = self.registry.get_implementations(operation)\n        if not impls:\n\
    \            print(f\"No implementations for operation: {operation}\")\n     \
    \       return\n        \n        # Run reference implementation first (find first\
    \ non-skipped implementation)\n        expected_result = None\n        ref_name\
    \ = None\n        for impl_name, impl_func in impls.items():\n            setup_func\
    \ = self.registry.get_setup(operation, impl_name)\n            result, _ = self.timer.measure_time(impl_func,\
    \ test_data, setup_func)\n            if result is not None:\n               \
    \ expected_result = result\n                ref_name = impl_name\n           \
    \     break\n        \n        # If all implementations return None, skip this\
    \ operation/size combination\n        if expected_result is None:\n          \
    \  print(\"  All implementations skipped\")\n            return\n        \n  \
    \      # Get validator for this operation\n        validator = self.registry.get_validator(operation)\n\
    \        \n        # Run all implementations\n        for impl_name, impl_func\
    \ in impls.items():\n            try:\n                setup_func = self.registry.get_setup(operation,\
    \ impl_name)\n                result, time_ms = self.timer.measure_time(impl_func,\
    \ test_data, setup_func)\n                \n                # Check if implementation\
    \ returned None to skip\n                if result is None:\n                \
    \    print(f\"  {impl_name:<20} SKIPPED\")\n                    sys.stdout.flush()\n\
    \                    continue\n                \n                correct = validator.validate(expected_result,\
    \ result)\n                \n                # Store result\n                benchmark_result\
    \ = BenchmarkResult(\n                    operation=operation,\n             \
    \       size=size,\n                    implementation=impl_name,\n          \
    \          time_ms=time_ms,\n                    correct=correct\n           \
    \     )\n                self.results.append(benchmark_result)\n             \
    \   \n                status = \"OK\" if correct else \"FAIL\"\n             \
    \   print(f\"  {impl_name:<20} {time_ms:>8.3f} ms  {status}\")\n             \
    \   sys.stdout.flush()\n                \n            except Exception as e:\n\
    \                # Get a meaningful error message\n                error_msg =\
    \ str(e) if str(e) else f\"{type(e).__name__}: {repr(e)}\"\n                \n\
    \                benchmark_result = BenchmarkResult(\n                    operation=operation,\n\
    \                    size=size,\n                    implementation=impl_name,\n\
    \                    time_ms=float('inf'),\n                    correct=False,\n\
    \                    error=error_msg\n                )\n                self.results.append(benchmark_result)\n\
    \                print(f\"  {impl_name:<20} ERROR: {error_msg[:40]}\")\n     \
    \           sys.stdout.flush()"
  dependsOn:
  - cp_library/perf/interfaces.py
  isVerificationFile: false
  path: cp_library/perf/orchestrator.py
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
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/orchestrator.py
layout: document
redirect_from:
- /library/cp_library/perf/orchestrator.py
- /library/cp_library/perf/orchestrator.py.html
title: cp_library/perf/orchestrator.py
---
