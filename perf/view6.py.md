---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_ranged_fn.py
    title: cp_library/alg/iter/arg/argsort_ranged_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/isort_ranged_fn.py
    title: cp_library/alg/iter/sort/isort_ranged_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view6_cls.py
    title: cp_library/ds/view/view6_cls.py
  - icon: ':warning:'
    path: cp_library/perf/benchmark.py
    title: cp_library/perf/benchmark.py
  - icon: ':warning:'
    path: cp_library/perf/checksum.py
    title: cp_library/perf/checksum.py
  - icon: ':warning:'
    path: cp_library/perf/cli.py
    title: cp_library/perf/cli.py
  - icon: ':warning:'
    path: cp_library/perf/interfaces.py
    title: cp_library/perf/interfaces.py
  - icon: ':warning:'
    path: cp_library/perf/orchestrator.py
    title: cp_library/perf/orchestrator.py
  - icon: ':warning:'
    path: cp_library/perf/output.py
    title: cp_library/perf/output.py
  - icon: ':warning:'
    path: cp_library/perf/registry.py
    title: cp_library/perf/registry.py
  - icon: ':warning:'
    path: cp_library/perf/renderers.py
    title: cp_library/perf/renderers.py
  - icon: ':warning:'
    path: cp_library/perf/timing.py
    title: cp_library/perf/timing.py
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
    , line 418, in visit\n    return visitor(node)\n  File \"/opt/hostedtoolcache/PyPy/3.10.16/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python_bundle.py\"\
    , line 64, in visit_ImportFrom\n    raise NotImplementedError(\"Relative imports\
    \ are not supported\")\nNotImplementedError: Relative imports are not supported\n"
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing view6 (6-array view)\
    \ vs tuple list.\nTests tuple access, iteration, sorting, modification, and append/pop\
    \ operations.\n\"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0,\
    \ os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig\nfrom cp_library.ds.view.view6_cls import\
    \ view6\n\n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"view6\"\
    ,\n    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up\
    \ JIT\n    operations=['tuple_access', 'iteration', 'sorting', 'modification',\
    \ 'append_pop'],\n    iterations=10,\n    warmup=3,\n    output_dir=\"./output/benchmark_results/view6\"\
    \n)\n\n# Create benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\n\
    @benchmark.data_generator(\"default\")\ndef generate_view6_data(size: int, operation:\
    \ str):\n    \"\"\"Generate test data for view6 operations\"\"\"\n    # Generate\
    \ parallel arrays\n    A1 = [random.randint(1, 1000000) for _ in range(size)]\n\
    \    A2 = [random.randint(1, 1000000) for _ in range(size)]\n    A3 = [random.randint(1,\
    \ 1000000) for _ in range(size)]\n    A4 = [random.randint(1, 1000000) for _ in\
    \ range(size)]\n    A5 = [random.randint(1, 1000000) for _ in range(size)]\n \
    \   A6 = [random.randint(1, 1000000) for _ in range(size)]\n    \n    # Create\
    \ view6 covering full range\n    v6 = view6(A1.copy(), A2.copy(), A3.copy(), A4.copy(),\
    \ A5.copy(), A6.copy(), 0, size)\n    \n    # Create equivalent data structures\n\
    \    tuple_list = [(A1[i], A2[i], A3[i], A4[i], A5[i], A6[i]) for i in range(size)]\n\
    \    \n    return {\n        'view6': v6,\n        'tuple_list': tuple_list,\n\
    \        'A1': A1.copy(),\n        'A2': A2.copy(),\n        'A3': A3.copy(),\n\
    \        'A4': A4.copy(),\n        'A5': A5.copy(),\n        'A6': A6.copy(),\n\
    \        'size': size\n    }\n\n# Setup functions for operations that modify data\n\
    @benchmark.setup(\"view6\", [\"modification\", \"sorting\", \"append_pop\"])\n\
    def setup_view6_modify(data):\n    \"\"\"Setup function that copies view6 data\
    \ before modification\"\"\"\n    new_data = data.copy()\n    A1_copy = data['A1'].copy()\n\
    \    A2_copy = data['A2'].copy()\n    A3_copy = data['A3'].copy()\n    A4_copy\
    \ = data['A4'].copy()\n    A5_copy = data['A5'].copy()\n    A6_copy = data['A6'].copy()\n\
    \    new_data['view6'] = view6(A1_copy, A2_copy, A3_copy, A4_copy, A5_copy, A6_copy,\
    \ 0, data['size'])\n    return new_data\n\n@benchmark.setup(\"tuple_list\", [\"\
    modification\", \"sorting\", \"append_pop\"])\ndef setup_tuple_list_modify(data):\n\
    \    \"\"\"Setup function that copies tuple list before modification\"\"\"\n \
    \   new_data = data.copy()\n    new_data['tuple_list'] = data['tuple_list'].copy()\n\
    \    return new_data\n\n# Tuple access operation\n@benchmark.implementation(\"\
    view6\", \"tuple_access\")\ndef tuple_access_view6(data):\n    \"\"\"Access tuples\
    \ using view6[i]\"\"\"\n    v6 = data['view6']\n    checksum = 0\n    for i in\
    \ range(len(v6)):\n        a1, a2, a3, a4, a5, a6 = v6[i]\n        checksum ^=\
    \ a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6\n    return checksum\n\n@benchmark.implementation(\"\
    tuple_list\", \"tuple_access\")\ndef tuple_access_tuple_list(data):\n    \"\"\"\
    Access tuples using list[i]\"\"\"\n    tuple_list = data['tuple_list']\n    checksum\
    \ = 0\n    for i in range(len(tuple_list)):\n        a1, a2, a3, a4, a5, a6 =\
    \ tuple_list[i]\n        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6\n    return checksum\n\
    \n# Iteration operation\n@benchmark.implementation(\"view6\", \"iteration\")\n\
    def iteration_view6(data):\n    \"\"\"Iterate through view6 using for-in (no __iter__)\"\
    \"\"\n    v6 = data['view6']\n    checksum = 0\n    for a1, a2, a3, a4, a5, a6\
    \ in v6:  # Uses __getitem__ with IndexError\n        checksum ^= a1 ^ a2 ^ a3\
    \ ^ a4 ^ a5 ^ a6\n    return checksum\n\n@benchmark.implementation(\"tuple_list\"\
    , \"iteration\")\ndef iteration_tuple_list(data):\n    \"\"\"Iterate through tuple\
    \ list using for-in\"\"\"\n    tuple_list = data['tuple_list']\n    checksum =\
    \ 0\n    for a1, a2, a3, a4, a5, a6 in tuple_list:\n        checksum ^= a1 ^ a2\
    \ ^ a3 ^ a4 ^ a5 ^ a6\n    return checksum\n\n# Sorting operation\n@benchmark.implementation(\"\
    view6\", \"sorting\")\ndef sorting_view6(data):\n    \"\"\"Sort view6 using isort_ranged\"\
    \"\"\n    v6 = data['view6']\n    v6.sort()  # Uses isort_ranged on view range\n\
    \    \n    checksum = 0\n    for i in range(min(100, len(v6))):\n        a1, a2,\
    \ a3, a4, a5, a6 = v6[i]\n        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6\n  \
    \  return checksum\n\n@benchmark.implementation(\"tuple_list\", \"sorting\")\n\
    def sorting_tuple_list(data):\n    \"\"\"Sort tuple list by first element\"\"\"\
    \n    tuple_list = data['tuple_list']\n    tuple_list.sort(key=lambda x: x[0])\n\
    \    \n    checksum = 0\n    for i in range(min(100, len(tuple_list))):\n    \
    \    a1, a2, a3, a4, a5, a6 = tuple_list[i]\n        checksum ^= a1 ^ a2 ^ a3\
    \ ^ a4 ^ a5 ^ a6\n    return checksum\n\n# Modification operation\n@benchmark.implementation(\"\
    view6\", \"modification\")\ndef modification_view6(data):\n    \"\"\"Modify view6\
    \ elements using __setitem__\"\"\"\n    v6 = data['view6']\n    checksum = 0\n\
    \    for i in range(len(v6)):\n        a1, a2, a3, a4, a5, a6 = v6[i]\n      \
    \  new_a1 = (a1 * 2) & 0xFFFFFFFF\n        new_a2 = (a2 * 3) & 0xFFFFFFFF\n  \
    \      new_a3 = (a3 * 4) & 0xFFFFFFFF\n        new_a4 = (a4 * 5) & 0xFFFFFFFF\n\
    \        new_a5 = (a5 * 6) & 0xFFFFFFFF\n        new_a6 = (a6 * 7) & 0xFFFFFFFF\n\
    \        v6[i] = (new_a1, new_a2, new_a3, new_a4, new_a5, new_a6)\n        checksum\
    \ ^= new_a1 ^ new_a2 ^ new_a3 ^ new_a4 ^ new_a5 ^ new_a6\n    return checksum\n\
    \n@benchmark.implementation(\"tuple_list\", \"modification\")\ndef modification_tuple_list(data):\n\
    \    \"\"\"Modify tuple list elements\"\"\"\n    tuple_list = data['tuple_list']\n\
    \    checksum = 0\n    for i in range(len(tuple_list)):\n        a1, a2, a3, a4,\
    \ a5, a6 = tuple_list[i]\n        new_a1 = (a1 * 2) & 0xFFFFFFFF\n        new_a2\
    \ = (a2 * 3) & 0xFFFFFFFF\n        new_a3 = (a3 * 4) & 0xFFFFFFFF\n        new_a4\
    \ = (a4 * 5) & 0xFFFFFFFF\n        new_a5 = (a5 * 6) & 0xFFFFFFFF\n        new_a6\
    \ = (a6 * 7) & 0xFFFFFFFF\n        tuple_list[i] = (new_a1, new_a2, new_a3, new_a4,\
    \ new_a5, new_a6)\n        checksum ^= new_a1 ^ new_a2 ^ new_a3 ^ new_a4 ^ new_a5\
    \ ^ new_a6\n    return checksum\n\n# Append/pop operation\n@benchmark.implementation(\"\
    view6\", \"append_pop\")\ndef append_pop_view6(data):\n    \"\"\"Test view6 append/pop\
    \ operations\"\"\"\n    v6 = data['view6']\n    checksum = 0\n    operations =\
    \ min(1000, len(v6) // 10)\n    \n    # Pop from end and append back\n    for\
    \ _ in range(operations):\n        a1, a2, a3, a4, a5, a6 = v6.pop()\n       \
    \ checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6\n    for i in range(operations):\n \
    \       vals = (i + 1000, i + 2000, i + 3000, i + 4000, i + 5000, i + 6000)\n\
    \        v6.append(vals)\n        checksum ^= vals[0] ^ vals[1] ^ vals[2] ^ vals[3]\
    \ ^ vals[4] ^ vals[5]\n    return checksum\n\n@benchmark.implementation(\"tuple_list\"\
    , \"append_pop\")\ndef append_pop_tuple_list(data):\n    \"\"\"Test tuple list\
    \ append/pop operations\"\"\"\n    tuple_list = data['tuple_list']\n    checksum\
    \ = 0\n    operations = min(1000, len(tuple_list) // 10)\n    \n    # Pop from\
    \ end and append back\n    for _ in range(operations):\n        a1, a2, a3, a4,\
    \ a5, a6 = tuple_list.pop()\n        checksum ^= a1 ^ a2 ^ a3 ^ a4 ^ a5 ^ a6\n\
    \    for i in range(operations):\n        vals = (i + 1000, i + 2000, i + 3000,\
    \ i + 4000, i + 5000, i + 6000)\n        tuple_list.append(vals)\n        checksum\
    \ ^= vals[0] ^ vals[1] ^ vals[2] ^ vals[3] ^ vals[4] ^ vals[5]\n    return checksum\n\
    \nif __name__ == \"__main__\":\n    # Parse command line args and run appropriate\
    \ mode\n    runner = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/view/view6_cls.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/alg/iter/sort/isort_ranged_fn.py
  - cp_library/perf/checksum.py
  - cp_library/alg/iter/arg/argsort_ranged_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: false
  path: perf/view6.py
  requiredBy: []
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/view6.py
layout: document
redirect_from:
- /library/perf/view6.py
- /library/perf/view6.py.html
title: perf/view6.py
---
