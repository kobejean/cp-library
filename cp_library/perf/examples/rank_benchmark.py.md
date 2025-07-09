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
  code: "from cp_library.perf.benchmark import Benchmark, BenchmarkConfig, TestCase\n\
    from cp_library.perf.generators import create_generator\nfrom cp_library.alg.iter.rank.irank_fn\
    \ import irank\nfrom cp_library.alg.iter.rank.irank_multi_fn import irank as irank_multi\n\
    from itertools import product\nfrom typing import Dict, List, Any, Callable, Tuple\n\
    \nclass RankingBenchmark(Benchmark):\n    \"\"\"Benchmark for comparing ranking\
    \ algorithm implementations\"\"\"\n    \n    def generate_test_cases(self, param_grid:\
    \ Dict[str, List[Any]]) -> List[TestCase]:\n        \"\"\"Generate test cases\
    \ from parameter grid\"\"\"\n        test_cases = []\n        \n        # Extract\
    \ parameters\n        param_names = list(param_grid.keys())\n        param_values\
    \ = [param_grid[name] for name in param_names]\n        \n        for values in\
    \ product(*param_values):\n            params = dict(zip(param_names, values))\n\
    \            \n            # Generate data based on distribution parameter\n \
    \           size = params['size']\n            distribution = params['distribution']\n\
    \            \n            # Use the generator factory\n            generator\
    \ = create_generator(distribution)\n            data = generator.generate(size=size)\n\
    \            \n            # Create descriptive name\n            name = f\"size={size},\
    \ dist={distribution}, distinct={params.get('distinct', False)}\"\n          \
    \  \n            test_cases.append(TestCase(\n                name=name,\n   \
    \             params=params,\n                data={'data': data, 'distinct':\
    \ params.get('distinct', False)}\n            ))\n        \n        return test_cases\n\
    \    \n    def get_implementations(self) -> Dict[str, Callable]:\n        \"\"\
    \"Return implementations to benchmark\"\"\"\n        return {\n            'irank':\
    \ lambda data, distinct=False: irank(data.copy(), distinct=distinct),\n      \
    \      'irank_multi': lambda data, distinct=False: irank_multi(data.copy(), distinct=distinct)\n\
    \        }\n    \n    def measure_time(self, func: Callable, test_data: Dict)\
    \ -> Tuple[Any, float]:\n        \"\"\"Override to handle dict test data\"\"\"\
    \n        import time\n        \n        # Warmup\n        for _ in range(self.config.warmup):\n\
    \            func(**test_data)\n        \n        # Actual measurement\n     \
    \   start = time.perf_counter()\n        for _ in range(self.config.iterations):\n\
    \            result = func(**test_data)\n        elapsed_ms = (time.perf_counter()\
    \ - start) * 1000 / self.config.iterations\n        \n        return result, elapsed_ms\n\
    \ndef run_ranking_benchmark():\n    \"\"\"Run a comprehensive ranking algorithm\
    \ benchmark\"\"\"\n    \n    # Configure benchmark\n    config = BenchmarkConfig(\n\
    \        name=\"ranking_algorithms\",\n        iterations=10,\n        warmup=2,\n\
    \        save_results=True,\n        plot_results=False,  # Set to True if matplotlib\
    \ is installed\n        output_dir=\"./benchmark_results/ranking\"\n    )\n  \
    \  \n    # Create benchmark instance\n    benchmark = RankingBenchmark(config)\n\
    \    \n    # Define parameter grid\n    param_grid = {\n        'size': [100,\
    \ 1000, 10000, 50000],\n        'distribution': ['random', 'sorted', 'reverse',\
    \ 'duplicates', 'almost_sorted', 'plateau'],\n        'distinct': [True, False]\n\
    \    }\n    \n    # Run benchmark\n    benchmark.run(param_grid)\n    \n    #\
    \ Print summary statistics\n    print_summary(benchmark.results)\n\ndef print_summary(results):\n\
    \    \"\"\"Print summary statistics from benchmark results\"\"\"\n    from collections\
    \ import defaultdict\n    import statistics\n    \n    # Group results by implementation\n\
    \    impl_times = defaultdict(list)\n    \n    for result in results:\n      \
    \  if result.time_ms != float('inf'):\n            impl_times[result.implementation].append(result.time_ms)\n\
    \    \n    print(\"\\n\" + \"=\"*60)\n    print(\"SUMMARY STATISTICS\")\n    print(\"\
    =\"*60)\n    \n    print(f\"\\n{'Implementation':<20} {'Mean (ms)':<12} {'Std\
    \ Dev':<12} {'Min':<12} {'Max':<12} {'Samples':<10}\")\n    print(\"-\"*80)\n\
    \    \n    for impl, times in impl_times.items():\n        if times:\n       \
    \     mean_time = statistics.mean(times)\n            std_time = statistics.stdev(times)\
    \ if len(times) > 1 else 0\n            min_time = min(times)\n            max_time\
    \ = max(times)\n            \n            print(f\"{impl:<20} {mean_time:<12.3f}\
    \ {std_time:<12.3f} {min_time:<12.3f} {max_time:<12.3f} {len(times):<10}\")\n\
    \    \n    # Calculate speedup ratios\n    if len(impl_times) == 2:\n        impls\
    \ = list(impl_times.keys())\n        impl1_mean = statistics.mean(impl_times[impls[0]])\n\
    \        impl2_mean = statistics.mean(impl_times[impls[1]])\n        speedup =\
    \ impl1_mean / impl2_mean\n        \n        faster = impls[1] if speedup > 1\
    \ else impls[0]\n        ratio = max(speedup, 1/speedup)\n        \n        print(f\"\
    \\n{faster} is {ratio:.2f}x faster on average\")\n\nif __name__ == \"__main__\"\
    :\n    run_ranking_benchmark()"
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
  path: cp_library/perf/examples/rank_benchmark.py
  requiredBy: []
  timestamp: '2025-07-09 08:31:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/examples/rank_benchmark.py
layout: document
redirect_from:
- /library/cp_library/perf/examples/rank_benchmark.py
- /library/cp_library/perf/examples/rank_benchmark.py.html
title: cp_library/perf/examples/rank_benchmark.py
---
