---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/rank/irank_fn.py
    title: cp_library/alg/iter/rank/irank_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/rank/irank_multi_fn.py
    title: cp_library/alg/iter/rank/irank_multi_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer3_cls.py
    title: cp_library/bit/pack/packer3_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
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
  code: "\"\"\"Updated ranking benchmark using the cp_library.perf framework\"\"\"\
    \n\nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig, TestCase\n\
    from cp_library.perf.generators import (\n    RandomArrayGenerator, SortedArrayGenerator,\
    \ DuplicatesArrayGenerator,\n    DistributionArrayGenerator, PlateauArrayGenerator,\
    \ AlmostSortedArrayGenerator\n)\nfrom cp_library.alg.iter.rank.irank_fn import\
    \ irank\nfrom cp_library.alg.iter.rank.irank_multi_fn import irank as irank_multi\n\
    from typing import Dict, List, Any, Callable, Tuple\nimport time\n\nclass RankingBenchmark(Benchmark):\n\
    \    \"\"\"Extended benchmark for ranking algorithms with all original test cases\"\
    \"\"\n    \n    def generate_test_cases(self, param_grid: Dict[str, List[Any]])\
    \ -> List[TestCase]:\n        test_cases = []\n        \n        # Very large\
    \ random datasets\n        test_cases.extend([\n            TestCase(\n      \
    \          name=\"Very large random\",\n                params={'size': 50000,\
    \ 'distribution': 'random'},\n                data={'data': RandomArrayGenerator(1,\
    \ 100000).generate(50000), 'distinct': False}\n            ),\n            TestCase(\n\
    \                name=\"Huge random\",\n                params={'size': 100000,\
    \ 'distribution': 'random'},\n                data={'data': RandomArrayGenerator(1,\
    \ 1000000).generate(100000), 'distinct': False}\n            ),\n        ])\n\
    \        \n        # Large sorted datasets\n        test_cases.extend([\n    \
    \        TestCase(\n                name=\"Very large sorted\",\n            \
    \    params={'size': 50000, 'distribution': 'sorted'},\n                data={'data':\
    \ SortedArrayGenerator().generate(50000), 'distinct': False}\n            ),\n\
    \            TestCase(\n                name=\"Huge sorted\",\n              \
    \  params={'size': 100000, 'distribution': 'sorted'},\n                data={'data':\
    \ SortedArrayGenerator().generate(100000), 'distinct': False}\n            ),\n\
    \        ])\n        \n        # Pathological cases\n        test_cases.extend([\n\
    \            TestCase(\n                name=\"Large mostly duplicates\",\n  \
    \              params={'size': 50000, 'distribution': 'duplicates'},\n       \
    \         data={'data': DuplicatesArrayGenerator(100).generate(50000), 'distinct':\
    \ False}\n            ),\n            TestCase(\n                name=\"Huge few\
    \ values\",\n                params={'size': 100000, 'distribution': 'duplicates'},\n\
    \                data={'data': DuplicatesArrayGenerator(10).generate(100000),\
    \ 'distinct': False}\n            ),\n        ])\n        \n        # Real-world-like\
    \ distributions\n        test_cases.extend([\n            TestCase(\n        \
    \        name=\"Normal distribution\",\n                params={'size': 50000,\
    \ 'distribution': 'normal'},\n                data={'data': DistributionArrayGenerator('normal').generate(50000,\
    \ mean=5000, std=1000), 'distinct': False}\n            ),\n            TestCase(\n\
    \                name=\"Exponential-like\",\n                params={'size': 50000,\
    \ 'distribution': 'exponential'},\n                data={'data': DistributionArrayGenerator('exponential').generate(50000,\
    \ rate=0.001), 'distinct': False}\n            ),\n        ])\n        \n    \
    \    # Edge cases with larger data\n        test_cases.extend([\n            TestCase(\n\
    \                name=\"Large alternating\",\n                params={'size':\
    \ 50000, 'distribution': 'alternating'},\n                data={'data': [i if\
    \ i % 2 == 0 else 100000 - i for i in range(50000)], 'distinct': False}\n    \
    \        ),\n            TestCase(\n                name=\"Large plateau\",\n\
    \                params={'size': 50000, 'distribution': 'plateau'},\n        \
    \        data={'data': PlateauArrayGenerator(2).generate(50000), 'distinct': False}\n\
    \            ),\n        ])\n        \n        # Add distinct=True versions for\
    \ some cases\n        for test_case in test_cases[:5]:  # First 5 test cases\n\
    \            distinct_case = TestCase(\n                name=test_case.name +\
    \ \" (distinct)\",\n                params={**test_case.params, 'distinct': True},\n\
    \                data={**test_case.data, 'distinct': True}\n            )\n  \
    \          test_cases.append(distinct_case)\n        \n        return test_cases\n\
    \    \n    def get_implementations(self) -> Dict[str, Callable]:\n        return\
    \ {\n            'irank': lambda data, distinct=False: irank(data.copy(), distinct=distinct),\n\
    \            'irank_multi': lambda data, distinct=False: irank_multi(data.copy(),\
    \ distinct=distinct)\n        }\n    \n    def measure_time(self, func: Callable,\
    \ test_data: Dict) -> Tuple[Any, float]:\n        \"\"\"Override to handle dict\
    \ test data and adjust iterations for large data\"\"\"\n        # Adjust iterations\
    \ based on data size\n        data_size = len(test_data['data'])\n        iterations\
    \ = max(1, 50 // (data_size // 1000)) if data_size > 1000 else self.config.iterations\n\
    \        \n        # Warmup\n        for _ in range(min(self.config.warmup, 1)):\n\
    \            func(**test_data)\n        \n        # Actual measurement\n     \
    \   start = time.perf_counter()\n        for _ in range(iterations):\n       \
    \     result = func(**test_data)\n        elapsed_ms = (time.perf_counter() -\
    \ start) * 1000 / iterations\n        \n        return result, elapsed_ms\n\n\
    class ScalingAnalysisBenchmark(Benchmark):\n    \"\"\"Analyze how performance\
    \ scales with input size\"\"\"\n    \n    def generate_test_cases(self, param_grid:\
    \ Dict[str, List[Any]]) -> List[TestCase]:\n        test_cases = []\n        sizes\
    \ = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000]\n        \n        for\
    \ size in sizes:\n            test_cases.append(TestCase(\n                name=f\"\
    scaling_size_{size}\",\n                params={'size': size},\n             \
    \   data={'data': RandomArrayGenerator(1, size).generate(size), 'distinct': False}\n\
    \            ))\n        \n        return test_cases\n    \n    def get_implementations(self)\
    \ -> Dict[str, Callable]:\n        return {\n            'irank': lambda data,\
    \ distinct=False: irank(data.copy(), distinct=distinct),\n            'irank_multi':\
    \ lambda data, distinct=False: irank_multi(data.copy(), distinct=distinct)\n \
    \       }\n    \n    def measure_time(self, func: Callable, test_data: Dict) ->\
    \ Tuple[Any, float]:\n        \"\"\"Single iteration for scaling test\"\"\"\n\
    \        start = time.perf_counter()\n        result = func(**test_data)\n   \
    \     elapsed_ms = (time.perf_counter() - start) * 1000\n        return result,\
    \ elapsed_ms\n    \n    def run(self, param_grid: Dict[str, List[Any]]):\n   \
    \     \"\"\"Override to add scaling analysis output\"\"\"\n        super().run(param_grid)\n\
    \        \n        print(\"\\nScaling Analysis:\")\n        print(f\"{'Size':<10}\
    \ {'irank (ms)':<15} {'multi (ms)':<15} {'irank/n':<15} {'multi/n':<15}\")\n \
    \       print(\"-\" * 70)\n        \n        # Group results by size\n       \
    \ size_results = {}\n        for result in self.results:\n            size = result.test_case.params['size']\n\
    \            if size not in size_results:\n                size_results[size]\
    \ = {}\n            size_results[size][result.implementation] = result.time_ms\n\
    \        \n        for size in sorted(size_results.keys()):\n            times\
    \ = size_results[size]\n            if 'irank' in times and 'irank_multi' in times:\n\
    \                time1 = times['irank']\n                time2 = times['irank_multi']\n\
    \                time_per_n1 = time1 / size\n                time_per_n2 = time2\
    \ / size\n                \n                print(f\"{size:<10} {time1:<15.3f}\
    \ {time2:<15.3f} {time_per_n1:<15.6f} {time_per_n2:<15.6f}\")\n\ndef run_all_benchmarks():\n\
    \    \"\"\"Run all benchmark suites\"\"\"\n    \n    print(\"=\" * 80)\n    print(\"\
    EXTENDED RANKING BENCHMARK\")\n    print(\"=\" * 80)\n    \n    # Extended benchmark\n\
    \    config1 = BenchmarkConfig(\n        name=\"ranking_extended\",\n        iterations=5,\n\
    \        warmup=2,\n        save_results=True,\n        plot_results=True,\n \
    \       output_dir=\"./benchmark_results/ranking\"\n    )\n    \n    benchmark1\
    \ = RankingBenchmark(config1)\n    benchmark1.run({})  # Empty grid since we manually\
    \ create test cases\n    \n    # Memory usage estimate\n    print(\"\\nMemory\
    \ Usage Estimate:\")\n    print(f\"{'Size':<10} {'Input (MB)':<12} {'Est. Peak\
    \ (MB)':<15}\")\n    print(\"-\" * 40)\n    \n    for size in [10000, 50000, 100000,\
    \ 500000]:\n        input_mb = size * 8 / (1024 * 1024)  # 8 bytes per integer\n\
    \        peak_mb = input_mb * 3  # Rough estimate\n        print(f\"{size:<10}\
    \ {input_mb:<12.2f} {peak_mb:<15.2f}\")\n    \n    print(\"\\n\" + \"=\" * 80)\n\
    \    print(\"SCALING ANALYSIS\")\n    print(\"=\" * 80)\n    \n    # Scaling analysis\n\
    \    config2 = BenchmarkConfig(\n        name=\"ranking_scaling\",\n        iterations=1,\n\
    \        warmup=0,\n        save_results=True,\n        plot_results=True,\n \
    \       output_dir=\"./output/benchmark_results/ranking\"\n    )\n    \n    benchmark2\
    \ = ScalingAnalysisBenchmark(config2)\n    benchmark2.run({})\n\nif __name__ ==\
    \ \"__main__\":\n    run_all_benchmarks()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/perf/generators.py
  - cp_library/alg/iter/rank/irank_fn.py
  - cp_library/alg/iter/rank/irank_multi_fn.py
  - cp_library/perf/plotters.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/bit/pack/packer3_cls.py
  isVerificationFile: false
  path: perf/rank_perf.py
  requiredBy: []
  timestamp: '2025-07-09 08:31:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/rank_perf.py
layout: document
redirect_from:
- /library/perf/rank_perf.py
- /library/perf/rank_perf.py.html
title: perf/rank_perf.py
---
