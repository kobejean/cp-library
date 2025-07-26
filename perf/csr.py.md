---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/csr_cls.py
    title: cp_library/ds/view/csr_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view_cls.py
    title: cp_library/ds/view/view_cls.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing CSR vs list of lists\
    \ for sparse row operations.\nTests direct access, view creation, iteration patterns,\
    \ and modification.\n\"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0,\
    \ os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig\nfrom cp_library.ds.view.csr_cls import CSR\n\
    \n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"csr\",\n    sizes=[1000000,\
    \ 100000, 10000, 1000, 100],  # Reverse order to warm up JIT\n    operations=['copy_construction',\
    \ 'direct_access', 'random_access', 'indexed_iter', 'foreach_iter', 'modification',\
    \ 'bucketize', 'col1_indexed_iter', 'col1_foreach_iter'],\n    iterations=10,\n\
    \    warmup=3,\n    output_dir=\"./output/benchmark_results/csr\"\n)\n\n# Create\
    \ benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\n@benchmark.data_generator(\"\
    default\")\ndef generate_csr_data(size: int, operation: str):\n    \"\"\"Generate\
    \ test data for CSR operations\"\"\"\n    # Create rows with variable sizes (using\
    \ CSR2's better approach)\n    row_sizes = []\n    total = 0\n    \n    while\
    \ total < size:\n        row_size = random.randint(50, 150)\n        if total\
    \ + row_size > size:\n            row_size = size - total\n        row_sizes.append(row_size)\n\
    \        total += row_size\n    \n    # Generate offset array\n    O = [0]\n \
    \   for row_size in row_sizes:\n        O.append(O[-1] + row_size)\n    \n   \
    \ # Generate data array\n    A = [random.randint(1, 1000000) for _ in range(size)]\n\
    \    \n    # Create list of lists equivalent\n    list_of_lists = []\n    for\
    \ i in range(len(row_sizes)):\n        start, end = O[i], O[i + 1]\n        list_of_lists.append(A[start:end].copy())\n\
    \    \n    # Create CSR\n    csr = CSR(A.copy(), O.copy())\n    \n    # For bucketize\
    \ operation\n    actual_num_rows = len(row_sizes)\n    keys = [random.randint(0,\
    \ max(0, actual_num_rows - 1)) for _ in range(size)]\n    values = [random.randint(0,\
    \ 1000000) for _ in range(size)]\n    \n    return {\n        'csr': csr,\n  \
    \      'list_of_lists': list_of_lists,\n        'A': A,\n        'O': O,\n   \
    \     'num_rows': len(row_sizes),\n        'keys': keys,\n        'values': values,\n\
    \        'size': size,\n        'operation': operation\n    }\n\n# Specialized\
    \ data generator for single-element rows\n@benchmark.data_generator(\"col1_indexed_iter\"\
    )\ndef generate_col1_indexed_data(size: int, operation: str):\n    \"\"\"Generate\
    \ test data where every row has exactly 1 column - tests indexed iteration\"\"\
    \"\n    return _generate_col1_data(size, operation)\n\n@benchmark.data_generator(\"\
    col1_foreach_iter\")\ndef generate_col1_foreach_data(size: int, operation: str):\n\
    \    \"\"\"Generate test data where every row has exactly 1 column - tests foreach\
    \ iteration\"\"\"\n    return _generate_col1_data(size, operation)\n\ndef _generate_col1_data(size:\
    \ int, operation: str):\n    \"\"\"Helper to generate single-element row data\"\
    \"\"\n    # Each row has exactly 1 element\n    num_rows = size\n    \n    # Generate\
    \ offset array for single-element rows\n    O = list(range(size + 1))  # [0, 1,\
    \ 2, 3, ..., size]\n    \n    # Generate data array\n    A = [random.randint(1,\
    \ 1000000) for _ in range(size)]\n    \n    # Create list of lists equivalent\
    \ (each row has 1 element)\n    list_of_lists = [[A[i]] for i in range(size)]\n\
    \    \n    # Create CSR\n    csr = CSR(A.copy(), O.copy())\n    \n    # For bucketize\
    \ operation - distribute across fewer buckets to avoid empty ones\n    bucket_count\
    \ = max(1, size // 10)  # 10 elements per bucket on average\n    keys = [random.randint(0,\
    \ bucket_count - 1) for _ in range(size)]\n    values = [random.randint(0, 1000000)\
    \ for _ in range(size)]\n    \n    return {\n        'csr': csr,\n        'list_of_lists':\
    \ list_of_lists,\n        'A': A,\n        'O': O,\n        'num_rows': num_rows,\n\
    \        'keys': keys,\n        'values': values,\n        'size': size,\n   \
    \     'operation': operation,\n        'bucket_count': bucket_count\n    }\n\n\
    # Setup functions for operations that modify data\n@benchmark.setup(\"csr\", [\"\
    modification\"])\ndef setup_csr_modify(data):\n    \"\"\"Setup function that copies\
    \ CSR data before modification\"\"\"\n    new_data = data.copy()\n    A_copy =\
    \ data['A'].copy()\n    O_copy = data['O'].copy()\n    new_data['csr'] = CSR(A_copy,\
    \ O_copy)\n    return new_data\n\n@benchmark.setup(\"list_of_lists\", [\"modification\"\
    ])\ndef setup_list_modify(data):\n    \"\"\"Setup function that copies list data\
    \ before modification\"\"\"\n    new_data = data.copy()\n    new_data['list_of_lists']\
    \ = [row.copy() for row in data['list_of_lists']]\n    return new_data\n\n# Direct\
    \ element access operation\n@benchmark.implementation(\"csr\", \"direct_access\"\
    )\ndef direct_access_csr(data):\n    \"\"\"Access elements using csr(i,j)\"\"\"\
    \n    csr = data['csr']\n    checksum = 0\n    for i in range(len(csr)):\n   \
    \     for j in range(len(csr[i])):\n            checksum ^= csr(i, j)\n    return\
    \ checksum\n\n@benchmark.implementation(\"list_of_lists\", \"direct_access\")\n\
    def direct_access_list_of_lists(data):\n    \"\"\"Access elements using list[i][j]\"\
    \"\"\n    list_of_lists = data['list_of_lists']\n    checksum = 0\n    for i in\
    \ range(len(list_of_lists)):\n        for j in range(len(list_of_lists[i])):\n\
    \            checksum ^= list_of_lists[i][j]\n    return checksum\n\n\n# Indexed\
    \ iteration using [i] access\n@benchmark.implementation(\"csr\", \"indexed_iter\"\
    )\ndef indexed_iter_csr(data):\n    \"\"\"Iterate using csr[i] access\"\"\"\n\
    \    csr = data['csr']\n    checksum = 0\n    for i in range(len(csr)):\n    \
    \    row_view = csr[i]\n        for j in range(len(row_view)):\n            checksum\
    \ ^= row_view[j]\n    return checksum\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"indexed_iter\")\ndef indexed_iter_list_of_lists(data):\n    \"\"\"Iterate\
    \ using list[i] access\"\"\"\n    list_of_lists = data['list_of_lists']\n    checksum\
    \ = 0\n    for i in range(len(list_of_lists)):\n        row = list_of_lists[i]\n\
    \        for j in range(len(row)):\n            checksum ^= row[j]\n    return\
    \ checksum\n\n# Foreach iteration using for-in pattern\n@benchmark.implementation(\"\
    csr\", \"foreach_iter\")\ndef foreach_iter_csr(data):\n    \"\"\"Iterate using\
    \ for row in csr\"\"\"\n    csr = data['csr']\n    checksum = 0\n    for row_view\
    \ in csr:\n        for element in row_view:\n            checksum ^= element\n\
    \    return checksum\n\n@benchmark.implementation(\"list_of_lists\", \"foreach_iter\"\
    )\ndef foreach_iter_list_of_lists(data):\n    \"\"\"Iterate using for row in list\"\
    \"\"\n    list_of_lists = data['list_of_lists']\n    checksum = 0\n    for row\
    \ in list_of_lists:\n        for element in row:\n            checksum ^= element\n\
    \    return checksum\n\n# In-place modification operation\n@benchmark.implementation(\"\
    csr\", \"modification\")\ndef modification_csr(data):\n    \"\"\"Modify elements\
    \ through CSR view\"\"\"\n    csr = data['csr']\n    checksum = 0\n    for i in\
    \ range(len(csr)):\n        row_view = csr[i]\n        for j in range(len(row_view)):\n\
    \            row_view[j] = (row_view[j] * 2) & 0xFFFFFFFF\n            checksum\
    \ ^= row_view[j]\n    return checksum\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"modification\")\ndef modification_list_of_lists(data):\n    \"\"\"Modify elements\
    \ in list directly\"\"\"\n    list_of_lists = data['list_of_lists']\n    checksum\
    \ = 0\n    for i in range(len(list_of_lists)):\n        row = list_of_lists[i]\n\
    \        for j in range(len(row)):\n            row[j] = (row[j] * 2) & 0xFFFFFFFF\n\
    \            checksum ^= row[j]\n    return checksum\n\n# Copy construction operation\n\
    @benchmark.implementation(\"csr\", \"copy_construction\")\ndef copy_construction_csr(data):\n\
    \    \"\"\"Construct CSR from copied arrays for fair comparison\"\"\"\n    A_copy\
    \ = data['A'].copy()\n    O_copy = data['O'].copy()\n    csr = CSR(A_copy, O_copy)\n\
    \    return len(csr)\n\n@benchmark.implementation(\"list_of_lists\", \"copy_construction\"\
    )\ndef copy_construction_list_of_lists(data):\n    \"\"\"Copy pre-initialized\
    \ list of lists\"\"\"\n    list_structure = [row.copy() for row in data['list_of_lists']]\n\
    \    return len(list_structure)\n\n# Random access operation\n@benchmark.implementation(\"\
    csr\", \"random_access\")\ndef random_access_csr(data):\n    \"\"\"Random access\
    \ using csr(i,j)\"\"\"\n    csr = data['csr']\n    checksum = 0\n    num_accesses\
    \ = min(1000, data['size'] // 10)\n    \n    rng = random.Random(42)\n    for\
    \ _ in range(num_accesses):\n        i = rng.randint(0, data['num_rows'] - 1)\n\
    \        row_size = len(csr[i])\n        if row_size > 0:\n            j = rng.randint(0,\
    \ row_size - 1)\n            checksum ^= csr(i, j)\n    return checksum & 0xFFFFFFFF\n\
    \n@benchmark.implementation(\"list_of_lists\", \"random_access\")\ndef random_access_list_of_lists(data):\n\
    \    \"\"\"Random access through list of lists\"\"\"\n    list_of_lists = data['list_of_lists']\n\
    \    checksum = 0\n    num_accesses = min(1000, data['size'] // 10)\n    \n  \
    \  rng = random.Random(42)\n    for _ in range(num_accesses):\n        i = rng.randint(0,\
    \ data['num_rows'] - 1)\n        if len(list_of_lists[i]) > 0:\n            j\
    \ = rng.randint(0, len(list_of_lists[i]) - 1)\n            checksum ^= list_of_lists[i][j]\n\
    \    return checksum & 0xFFFFFFFF\n\n# Bucketize operation\n@benchmark.implementation(\"\
    csr\", \"bucketize\")\ndef bucketize_csr(data):\n    \"\"\"Use CSR.bucketize method\"\
    \"\"\n    csr = CSR.bucketize(data['num_rows'], data['keys'], data['values'])\n\
    \    checksum = 0\n    for i in range(len(csr)):\n        row_view = csr[i]\n\
    \        for j in range(len(row_view)):\n            checksum ^= row_view[j]\n\
    \    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"bucketize\")\ndef bucketize_list_of_lists(data):\n    \"\"\"Manual bucketization\
    \ into lists\"\"\"\n    keys = data['keys']\n    values = data['values']\n   \
    \ num_rows = data['num_rows']\n    \n    buckets = [[] for _ in range(num_rows)]\n\
    \    \n    for i in range(len(keys)):\n        k = keys[i]\n        if 0 <= k\
    \ < num_rows:\n            buckets[k].append(values[i])\n    \n    checksum =\
    \ 0\n    for i in range(num_rows):\n        for j in range(len(buckets[i])):\n\
    \            checksum ^= buckets[i][j]\n    return checksum & 0xFFFFFFFF\n\n#\
    \ Column-1 iteration - indexed access\n@benchmark.implementation(\"csr\", \"col1_indexed_iter\"\
    )\ndef col1_indexed_csr(data):\n    \"\"\"Iterate through CSR where every row\
    \ has exactly 1 element using indexed access\"\"\"\n    csr = data['csr']\n  \
    \  \n    checksum = 0\n    # Iterate through many single-element rows using indexing\n\
    \    for i in range(len(csr)):\n        view = csr[i]  # Each view has exactly\
    \ 1 element\n        checksum ^= view[0]  # Access the single element\n    \n\
    \    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"col1_indexed_iter\")\ndef col1_indexed_lists(data):\n    \"\"\"Iterate through\
    \ list of single-element lists using indexed access\"\"\"\n    list_of_lists =\
    \ data['list_of_lists']\n    \n    checksum = 0\n    # Iterate through many single-element\
    \ lists using indexing\n    for i in range(len(list_of_lists)):\n        checksum\
    \ ^= list_of_lists[i][0]  # Each row has exactly 1 element\n    \n    return checksum\
    \ & 0xFFFFFFFF\n\n@benchmark.implementation(\"direct_array\", \"col1_indexed_iter\"\
    )\ndef col1_indexed_direct(data):\n    \"\"\"Direct indexed access through array\
    \ (baseline for single elements)\"\"\"\n    A = data['A']\n    \n    checksum\
    \ = 0\n    # Direct indexed iteration - each element is its own \"row\"\n    for\
    \ i in range(len(A)):\n        checksum ^= A[i]\n    \n    return checksum & 0xFFFFFFFF\n\
    \n@benchmark.implementation(\"csr\", \"col1_foreach_iter\")\ndef col1_foreach_csr(data):\n\
    \    \"\"\"Iterate through CSR using foreach loop where every row has exactly\
    \ 1 element\"\"\"\n    csr = data['csr']\n    \n    checksum = 0\n    # Use foreach\
    \ iteration pattern (Python will use __getitem__)\n    for view in csr:  # Each\
    \ view has exactly 1 element\n        checksum ^= view[0]  # Access the single\
    \ element\n    \n    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"\
    list_of_lists\", \"col1_foreach_iter\")\ndef col1_foreach_lists(data):\n    \"\
    \"\"Iterate through list of single-element lists using foreach\"\"\"\n    list_of_lists\
    \ = data['list_of_lists']\n    \n    checksum = 0\n    # Use foreach iteration\
    \ pattern\n    for row in list_of_lists:\n        checksum ^= row[0]  # Each row\
    \ has exactly 1 element\n    \n    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"\
    direct_array\", \"col1_foreach_iter\")\ndef col1_foreach_direct(data):\n    \"\
    \"\"Direct foreach iteration through array (baseline for single elements)\"\"\"\
    \n    A = data['A']\n    \n    checksum = 0\n    # Direct foreach iteration -\
    \ each element is its own \"row\"\n    for val in A:\n        checksum ^= val\n\
    \    \n    return checksum & 0xFFFFFFFF\n\nif __name__ == \"__main__\":\n    #\
    \ Parse command line args and run appropriate mode\n    runner = benchmark.parse_args()\n\
    \    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/view/csr_cls.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/ds/view/view_cls.py
  - cp_library/perf/checksum.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: false
  path: perf/csr.py
  requiredBy: []
  timestamp: '2025-07-26 11:14:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/csr.py
layout: document
redirect_from:
- /library/perf/csr.py
- /library/perf/csr.py.html
title: perf/csr.py
---
