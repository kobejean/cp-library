---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_fn.py
    title: argsort
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/isort_parallel_fn.py
    title: cp_library/alg/iter/sort/isort_parallel_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list2_cls.py
    title: cp_library/ds/list/list2_cls.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing list2 (dual-array list)\
    \ vs regular tuple list.\nTests construction, access, modification, sorting, append/pop\
    \ operations.\n\"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0,\
    \ os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig\nfrom cp_library.ds.list.list2_cls import\
    \ list2\n\n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"list2\"\
    ,\n    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up\
    \ JIT\n    operations=['construction', 'tuple_access', 'iteration', 'modification',\
    \ 'sorting', 'append_pop', 'add_operation'],\n    iterations=10,\n    warmup=3,\n\
    \    output_dir=\"./output/benchmark_results/list2\"\n)\n\n# Create benchmark\
    \ instance\nbenchmark = Benchmark(config)\n\n# Data generator\n@benchmark.data_generator(\"\
    default\")\ndef generate_list2_data(size: int, operation: str):\n    \"\"\"Generate\
    \ test data for list2 operations\"\"\"\n    # Generate parallel arrays\n    A1\
    \ = [random.randint(1, 1000000) for _ in range(size)]\n    A2 = [random.randint(1,\
    \ 1000000) for _ in range(size)]\n    \n    # Create list2 instance\n    l2 =\
    \ list2(A1.copy(), A2.copy())\n    \n    # Create equivalent data structures\n\
    \    tuple_list = [(A1[i], A2[i]) for i in range(size)]\n    list_of_lists = [[A1[i],\
    \ A2[i]] for i in range(size)]\n    \n    return {\n        'list2': l2,\n   \
    \     'tuple_list': tuple_list,\n        'list_of_lists': list_of_lists,\n   \
    \     'A1': A1.copy(),\n        'A2': A2.copy(),\n        'size': size\n    }\n\
    \n# Setup functions for operations that modify data\n@benchmark.setup(\"list2\"\
    , [\"modification\", \"sorting\", \"append_pop\", \"add_operation\"])\ndef setup_list2_modify(data):\n\
    \    \"\"\"Setup function that copies list2 data before modification\"\"\"\n \
    \   new_data = data.copy()\n    A1_copy = data['A1'].copy()\n    A2_copy = data['A2'].copy()\n\
    \    new_data['list2'] = list2(A1_copy, A2_copy)\n    return new_data\n\n@benchmark.setup(\"\
    tuple_list\", [\"modification\", \"sorting\", \"append_pop\"])\ndef setup_tuple_list_modify(data):\n\
    \    \"\"\"Setup function that copies tuple list before modification\"\"\"\n \
    \   new_data = data.copy()\n    new_data['tuple_list'] = data['tuple_list'].copy()\n\
    \    return new_data\n\n@benchmark.setup(\"list_of_lists\", [\"modification\"\
    , \"sorting\", \"append_pop\"])\ndef setup_list_of_lists_modify(data):\n    \"\
    \"\"Setup function that copies list of lists before modification\"\"\"\n    new_data\
    \ = data.copy()\n    new_data['list_of_lists'] = [row.copy() for row in data['list_of_lists']]\n\
    \    return new_data\n\n# Construction operation\n@benchmark.implementation(\"\
    list2\", \"construction\")\ndef construction_list2(data):\n    \"\"\"Construct\
    \ list2 from arrays\"\"\"\n    A1_copy = data['A1'].copy()\n    A2_copy = data['A2'].copy()\n\
    \    l2 = list2(A1_copy, A2_copy)\n    return len(l2)\n\n@benchmark.implementation(\"\
    tuple_list\", \"construction\")\ndef construction_tuple_list(data):\n    \"\"\"\
    Construct tuple list from arrays\"\"\"\n    A1, A2 = data['A1'], data['A2']\n\
    \    tuple_list = [(A1[i], A2[i]) for i in range(len(A1))]\n    return len(tuple_list)\n\
    \n@benchmark.implementation(\"list_of_lists\", \"construction\")\ndef construction_list_of_lists(data):\n\
    \    \"\"\"Construct list of lists from arrays\"\"\"\n    A1, A2 = data['A1'],\
    \ data['A2']\n    list_of_lists = [[A1[i], A2[i]] for i in range(len(A1))]\n \
    \   return len(list_of_lists)\n\n# Tuple access operation\n@benchmark.implementation(\"\
    list2\", \"tuple_access\")\ndef tuple_access_list2(data):\n    \"\"\"Access tuples\
    \ using list2[i]\"\"\"\n    l2 = data['list2']\n    checksum = 0\n    for i in\
    \ range(len(l2)):\n        a1, a2 = l2[i]\n        checksum ^= a1 ^ a2\n    return\
    \ checksum\n\n@benchmark.implementation(\"tuple_list\", \"tuple_access\")\ndef\
    \ tuple_access_tuple_list(data):\n    \"\"\"Access tuples using list[i]\"\"\"\n\
    \    tuple_list = data['tuple_list']\n    checksum = 0\n    for i in range(len(tuple_list)):\n\
    \        a1, a2 = tuple_list[i]\n        checksum ^= a1 ^ a2\n    return checksum\n\
    \n@benchmark.implementation(\"list_of_lists\", \"tuple_access\")\ndef tuple_access_list_of_lists(data):\n\
    \    \"\"\"Access elements using list[i]\"\"\"\n    list_of_lists = data['list_of_lists']\n\
    \    checksum = 0\n    for i in range(len(list_of_lists)):\n        a1, a2 = list_of_lists[i],\
    \ list_of_lists[i]\n        checksum ^= a1 ^ a2\n    return checksum\n\n# Iteration\
    \ operation\n@benchmark.implementation(\"list2\", \"iteration\")\ndef iteration_list2(data):\n\
    \    \"\"\"Iterate through list2 using for-in\"\"\"\n    l2 = data['list2']\n\
    \    checksum = 0\n    for a1, a2 in l2:\n        checksum ^= a1 ^ a2\n    return\
    \ checksum\n\n@benchmark.implementation(\"tuple_list\", \"iteration\")\ndef iteration_tuple_list(data):\n\
    \    \"\"\"Iterate through tuple list using for-in\"\"\"\n    tuple_list = data['tuple_list']\n\
    \    checksum = 0\n    for a1, a2 in tuple_list:\n        checksum ^= a1 ^ a2\n\
    \    return checksum\n\n@benchmark.implementation(\"list_of_lists\", \"iteration\"\
    )\ndef iteration_list_of_lists(data):\n    \"\"\"Iterate through list of lists\"\
    \"\"\n    list_of_lists = data['list_of_lists']\n    checksum = 0\n    for row\
    \ in list_of_lists:\n        a1, a2 = row[0], row[1]\n        checksum ^= a1 ^\
    \ a2\n    return checksum\n\n# Modification operation\n@benchmark.implementation(\"\
    list2\", \"modification\")\ndef modification_list2(data):\n    \"\"\"Modify list2\
    \ elements using __setitem__\"\"\"\n    l2 = data['list2']\n    checksum = 0\n\
    \    for i in range(len(l2)):\n        a1, a2 = l2[i]\n        new_a1 = (a1 *\
    \ 2) & 0xFFFFFFFF\n        new_a2 = (a2 * 3) & 0xFFFFFFFF\n        l2[i] = (new_a1,\
    \ new_a2)\n        checksum ^= new_a1 ^ new_a2\n    return checksum\n\n@benchmark.implementation(\"\
    tuple_list\", \"modification\")\ndef modification_tuple_list(data):\n    \"\"\"\
    Modify tuple list elements\"\"\"\n    tuple_list = data['tuple_list']\n    checksum\
    \ = 0\n    for i in range(len(tuple_list)):\n        a1, a2 = tuple_list[i]\n\
    \        new_a1 = (a1 * 2) & 0xFFFFFFFF\n        new_a2 = (a2 * 3) & 0xFFFFFFFF\n\
    \        tuple_list[i] = (new_a1, new_a2)\n        checksum ^= new_a1 ^ new_a2\n\
    \    return checksum\n\n@benchmark.implementation(\"list_of_lists\", \"modification\"\
    )\ndef modification_list_of_lists(data):\n    \"\"\"Modify list of lists elements\"\
    \"\"\n    list_of_lists = data['list_of_lists']\n    checksum = 0\n    for i in\
    \ range(len(list_of_lists)):\n        a1, a2 = list_of_lists[i][0], list_of_lists[i][1]\n\
    \        new_a1 = (a1 * 2) & 0xFFFFFFFF\n        new_a2 = (a2 * 3) & 0xFFFFFFFF\n\
    \        list_of_lists[i][0] = new_a1\n        list_of_lists[i][1] = new_a2\n\
    \        checksum ^= new_a1 ^ new_a2\n    return checksum\n\n# Sorting operation\n\
    @benchmark.implementation(\"list2\", \"sorting\")\ndef sorting_list2(data):\n\
    \    \"\"\"Sort list2 using isort_parallel\"\"\"\n    l2 = data['list2']\n   \
    \ l2.sort()  # Uses isort_parallel on both arrays\n    \n    checksum = 0\n  \
    \  for i in range(min(100, len(l2))):\n        a1, a2 = l2[i]\n        checksum\
    \ ^= a1 ^ a2\n    return checksum\n\n@benchmark.implementation(\"tuple_list\"\
    , \"sorting\")\ndef sorting_tuple_list(data):\n    \"\"\"Sort tuple list by first\
    \ element\"\"\"\n    tuple_list = data['tuple_list']\n    tuple_list.sort(key=lambda\
    \ x: x[0])\n    \n    checksum = 0\n    for i in range(min(100, len(tuple_list))):\n\
    \        a1, a2 = tuple_list[i]\n        checksum ^= a1 ^ a2\n    return checksum\n\
    \n@benchmark.implementation(\"list_of_lists\", \"sorting\")\ndef sorting_list_of_lists(data):\n\
    \    \"\"\"Sort list of lists by first element\"\"\"\n    list_of_lists = data['list_of_lists']\n\
    \    list_of_lists.sort(key=lambda x: x[0])\n    \n    checksum = 0\n    for i\
    \ in range(min(100, len(list_of_lists))):\n        a1, a2 = list_of_lists[i][0],\
    \ list_of_lists[i][1]\n        checksum ^= a1 ^ a2\n    return checksum\n\n# Append/pop\
    \ operation\n@benchmark.implementation(\"list2\", \"append_pop\")\ndef append_pop_list2(data):\n\
    \    \"\"\"Test list2 append/pop operations\"\"\"\n    l2 = data['list2']\n  \
    \  checksum = 0\n    operations = min(1000, len(l2) // 10)\n    \n    # Pop from\
    \ end and append back\n    for _ in range(operations):\n        a1, a2 = l2.pop()\n\
    \        checksum ^= a1 ^ a2\n    for i in range(operations):\n        l2.append((i\
    \ + 1000, i + 2000))\n        checksum ^= (i + 1000) ^ (i + 2000)\n    return\
    \ checksum\n\n@benchmark.implementation(\"tuple_list\", \"append_pop\")\ndef append_pop_tuple_list(data):\n\
    \    \"\"\"Test tuple list append/pop operations\"\"\"\n    tuple_list = data['tuple_list']\n\
    \    checksum = 0\n    operations = min(1000, len(tuple_list) // 10)\n    \n \
    \   # Pop from end and append back\n    for _ in range(operations):\n        a1,\
    \ a2 = tuple_list.pop()\n        checksum ^= a1 ^ a2\n    for i in range(operations):\n\
    \        tuple_list.append((i + 1000, i + 2000))\n        checksum ^= (i + 1000)\
    \ ^ (i + 2000)\n    return checksum\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"append_pop\")\ndef append_pop_list_of_lists(data):\n    \"\"\"Test list of\
    \ lists append/pop operations\"\"\"\n    list_of_lists = data['list_of_lists']\n\
    \    checksum = 0\n    operations = min(1000, len(list_of_lists) // 10)\n    \n\
    \    # Pop from end and append back\n    for _ in range(operations):\n       \
    \ row = list_of_lists.pop()\n        a1, a2 = row[0], row[1]\n        checksum\
    \ ^= a1 ^ a2\n    for i in range(operations):\n        list_of_lists.append([i\
    \ + 1000, i + 2000])\n        checksum ^= (i + 1000) ^ (i + 2000)\n    return\
    \ checksum\n\n# Add operation (specific to list2)\n@benchmark.implementation(\"\
    list2\", \"add_operation\")\ndef add_operation_list2(data):\n    \"\"\"Test list2\
    \ add operation\"\"\"\n    l2 = data['list2']\n    checksum = 0\n    for i in\
    \ range(len(l2)):\n        add_val = (i % 100, (i % 100) * 2)\n        l2.add(i,\
    \ add_val)\n        a1, a2 = l2[i]\n        checksum ^= a1 ^ a2\n    return checksum\n\
    \nif __name__ == \"__main__\":\n    # Parse command line args and run appropriate\
    \ mode\n    runner = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/list/list2_cls.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/perf/checksum.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: false
  path: perf/list2.py
  requiredBy: []
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/list2.py
layout: document
redirect_from:
- /library/perf/list2.py
- /library/perf/list2.py.html
title: perf/list2.py
---
