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
    path: cp_library/ds/view/csr6_cls.py
    title: cp_library/ds/view/csr6_cls.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing CSR6 vs direct arrays\
    \ for 6-array sparse data.\nCSR6 provides view6 objects for efficient row access\
    \ patterns.\n\"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0,\
    \ os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig\nfrom cp_library.ds.view.csr6_cls import CSR6\n\
    from cp_library.ds.view.view6_cls import view6\n\n# Configure benchmark\nconfig\
    \ = BenchmarkConfig(\n    name=\"csr6\",\n    sizes=[1000000, 100000, 10000, 1000,\
    \ 100],  # Reverse order to warm up JIT\n    operations=['copy_construction',\
    \ 'direct_access', 'random_access', 'indexed_iter', 'foreach_iter', 'modification',\
    \ 'bucketize', 'col1_indexed_iter', 'col1_foreach_iter'],\n    iterations=10,\n\
    \    warmup=3,\n    output_dir=\"./output/benchmark_results/csr6\"\n)\n\n# Create\
    \ benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\n@benchmark.data_generator(\"\
    default\")\ndef generate_csr6_data(size: int, operation: str):\n    \"\"\"Generate\
    \ test data for CSR6 operations\"\"\"\n    # Create rows with variable sizes\n\
    \    num_rows = max(1, size // 100)  # Average 100 elements per row\n    row_sizes\
    \ = []\n    total = 0\n    \n    while total < size:\n        row_size = random.randint(50,\
    \ 150)\n        if total + row_size > size:\n            row_size = size - total\n\
    \        row_sizes.append(row_size)\n        total += row_size\n    \n    # Generate\
    \ offset array\n    offsets = [0]\n    for row_size in row_sizes:\n        offsets.append(offsets[-1]\
    \ + row_size)\n    \n    # Generate data arrays\n    array_a1 = [random.randint(0,\
    \ 1000000) for _ in range(size)]\n    array_a2 = [random.randint(0, 1000000) for\
    \ _ in range(size)]\n    array_a3 = [random.randint(0, 1000000) for _ in range(size)]\n\
    \    array_a4 = [random.randint(0, 1000000) for _ in range(size)]\n    array_a5\
    \ = [random.randint(0, 1000000) for _ in range(size)]\n    array_a6 = [random.randint(0,\
    \ 1000000) for _ in range(size)]\n    \n    # Create list of lists structure\n\
    \    list_structure = []\n    for i in range(len(row_sizes)):\n        start =\
    \ offsets[i]\n        end = offsets[i + 1]\n        row = [(array_a1[j], array_a2[j],\
    \ array_a3[j], array_a4[j], array_a5[j], array_a6[j]) \n               for j in\
    \ range(start, end)]\n        list_structure.append(row)\n    \n    # For bucketize\
    \ operation\n    actual_num_rows = len(row_sizes)\n    keys = [random.randint(0,\
    \ max(0, actual_num_rows - 1)) for _ in range(size)]\n    values_v1 = [random.randint(0,\
    \ 1000000) for _ in range(size)]\n    values_v2 = [random.randint(0, 1000000)\
    \ for _ in range(size)]\n    values_v3 = [random.randint(0, 1000000) for _ in\
    \ range(size)]\n    values_v4 = [random.randint(0, 1000000) for _ in range(size)]\n\
    \    values_v5 = [random.randint(0, 1000000) for _ in range(size)]\n    values_v6\
    \ = [random.randint(0, 1000000) for _ in range(size)]\n    \n    return {\n  \
    \      'array_a1': array_a1,\n        'array_a2': array_a2,\n        'array_a3':\
    \ array_a3,\n        'array_a4': array_a4,\n        'array_a5': array_a5,\n  \
    \      'array_a6': array_a6,\n        'offsets': offsets,\n        'num_rows':\
    \ len(row_sizes),\n        'list_structure': list_structure,\n        'keys':\
    \ keys,\n        'values_v1': values_v1,\n        'values_v2': values_v2,\n  \
    \      'values_v3': values_v3,\n        'values_v4': values_v4,\n        'values_v5':\
    \ values_v5,\n        'values_v6': values_v6,\n        'size': size\n    }\n\n\
    # Specialized data generator for single-element rows\n@benchmark.data_generator(\"\
    col1_indexed_iter\")\ndef generate_col1_indexed_data(size: int, operation: str):\n\
    \    \"\"\"Generate test data where every row has exactly 1 column - tests indexed\
    \ iteration\"\"\"\n    return _generate_col1_data(size, operation)\n\n@benchmark.data_generator(\"\
    col1_foreach_iter\")\ndef generate_col1_foreach_data(size: int, operation: str):\n\
    \    \"\"\"Generate test data where every row has exactly 1 column - tests foreach\
    \ iteration\"\"\"\n    return _generate_col1_data(size, operation)\n\ndef _generate_col1_data(size:\
    \ int, operation: str):\n    \"\"\"Helper to generate single-element row data\"\
    \"\"\n    # Each row has exactly 1 element\n    num_rows = size\n    \n    # Generate\
    \ offset array for single-element rows\n    offsets = list(range(size + 1))  #\
    \ [0, 1, 2, 3, ..., size]\n    \n    # Generate data arrays\n    array_a1 = [random.randint(0,\
    \ 1000000) for _ in range(size)]\n    array_a2 = [random.randint(0, 1000000) for\
    \ _ in range(size)]\n    array_a3 = [random.randint(0, 1000000) for _ in range(size)]\n\
    \    array_a4 = [random.randint(0, 1000000) for _ in range(size)]\n    array_a5\
    \ = [random.randint(0, 1000000) for _ in range(size)]\n    array_a6 = [random.randint(0,\
    \ 1000000) for _ in range(size)]\n    \n    # Create list of lists structure (each\
    \ row has 1 element)\n    list_structure = [[(array_a1[i], array_a2[i], array_a3[i],\
    \ array_a4[i], array_a5[i], array_a6[i])] \n                      for i in range(size)]\n\
    \    \n    # For bucketize operation - distribute across fewer buckets to avoid\
    \ empty ones\n    bucket_count = max(1, size // 10)  # 10 elements per bucket\
    \ on average\n    keys = [random.randint(0, bucket_count - 1) for _ in range(size)]\n\
    \    values_v1 = [random.randint(0, 1000000) for _ in range(size)]\n    values_v2\
    \ = [random.randint(0, 1000000) for _ in range(size)]\n    values_v3 = [random.randint(0,\
    \ 1000000) for _ in range(size)]\n    values_v4 = [random.randint(0, 1000000)\
    \ for _ in range(size)]\n    values_v5 = [random.randint(0, 1000000) for _ in\
    \ range(size)]\n    values_v6 = [random.randint(0, 1000000) for _ in range(size)]\n\
    \    \n    return {\n        'array_a1': array_a1,\n        'array_a2': array_a2,\n\
    \        'array_a3': array_a3,\n        'array_a4': array_a4,\n        'array_a5':\
    \ array_a5,\n        'array_a6': array_a6,\n        'offsets': offsets,\n    \
    \    'num_rows': num_rows,\n        'list_structure': list_structure,\n      \
    \  'keys': keys,\n        'values_v1': values_v1,\n        'values_v2': values_v2,\n\
    \        'values_v3': values_v3,\n        'values_v4': values_v4,\n        'values_v5':\
    \ values_v5,\n        'values_v6': values_v6,\n        'size': size,\n       \
    \ 'bucket_count': bucket_count\n    }\n\n# Copy construction operation\n@benchmark.implementation(\"\
    csr6\", \"copy_construction\")\ndef copy_construction_csr6(data):\n    \"\"\"\
    Construct CSR6 from copied arrays for fair comparison\"\"\"\n    arrays_copy =\
    \ [\n        data['array_a1'].copy(),\n        data['array_a2'].copy(),\n    \
    \    data['array_a3'].copy(),\n        data['array_a4'].copy(),\n        data['array_a5'].copy(),\n\
    \        data['array_a6'].copy()\n    ]\n    offsets_copy = data['offsets'].copy()\n\
    \    csr = CSR6(*arrays_copy, offsets_copy)\n    return len(csr)\n\n@benchmark.implementation(\"\
    direct_arrays\", \"copy_construction\")\ndef copy_construction_direct(data):\n\
    \    \"\"\"Copy arrays for fair comparison with CSR6\"\"\"\n    arrays_copy =\
    \ [\n        data['array_a1'].copy(),\n        data['array_a2'].copy(),\n    \
    \    data['array_a3'].copy(),\n        data['array_a4'].copy(),\n        data['array_a5'].copy(),\n\
    \        data['array_a6'].copy()\n    ]\n    offsets_copy = data['offsets'].copy()\n\
    \    return len(offsets_copy) - 1  # Return number of rows\n\n@benchmark.implementation(\"\
    list_of_lists\", \"copy_construction\")\ndef copy_construction_list_of_lists(data):\n\
    \    \"\"\"Copy pre-initialized list of lists\"\"\"\n    list_structure = [row.copy()\
    \ for row in data['list_structure']]\n    return len(list_structure)\n\n# Direct\
    \ access operation\n@benchmark.implementation(\"csr6\", \"direct_access\")\ndef\
    \ direct_access_csr6(data):\n    \"\"\"Direct access through CSR6 views\"\"\"\n\
    \    csr = CSR6(data['array_a1'], data['array_a2'], data['array_a3'], \n     \
    \          data['array_a4'], data['array_a5'], data['array_a6'], data['offsets'])\n\
    \    checksum = 0\n    for i in range(len(csr)):\n        view = csr[i]\n    \
    \    for j in range(len(view)):\n            a1 = view.A1[view.l + j]\n      \
    \      a2 = view.A2[view.l + j]\n            a3 = view.A3[view.l + j]\n      \
    \      a4 = view.A4[view.l + j]\n            a5 = view.A5[view.l + j]\n      \
    \      a6 = view.A6[view.l + j]\n            checksum ^= (a1 + a2 + a3 + a4 +\
    \ a5 + a6)\n    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"direct_arrays\"\
    , \"direct_access\")\ndef direct_access_direct(data):\n    \"\"\"Direct access\
    \ using direct arrays\"\"\"\n    arrays = [data['array_a1'], data['array_a2'],\
    \ data['array_a3'], \n              data['array_a4'], data['array_a5'], data['array_a6']]\n\
    \    offsets = data['offsets']\n    checksum = 0\n    for i in range(data['num_rows']):\n\
    \        for j in range(offsets[i], offsets[i + 1]):\n            sum_val = sum(arr[j]\
    \ for arr in arrays)\n            checksum ^= sum_val\n    return checksum & 0xFFFFFFFF\n\
    \n@benchmark.implementation(\"list_of_lists\", \"direct_access\")\ndef direct_access_list_of_lists(data):\n\
    \    \"\"\"Direct access through list of lists\"\"\"\n    list_structure = data['list_structure']\n\
    \    checksum = 0\n    for row in list_structure:\n        for a1, a2, a3, a4,\
    \ a5, a6 in row:\n            checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)\n    return\
    \ checksum & 0xFFFFFFFF\n\n# Random access operation\n@benchmark.implementation(\"\
    csr6\", \"random_access\")\ndef random_access_csr6(data):\n    \"\"\"Random access\
    \ using csr(i,j)\"\"\"\n    csr = CSR6(data['array_a1'], data['array_a2'], data['array_a3'],\
    \ \n               data['array_a4'], data['array_a5'], data['array_a6'], data['offsets'])\n\
    \    checksum = 0\n    num_accesses = min(1000, data['size'] // 10)\n    \n  \
    \  rng = random.Random(42)\n    for _ in range(num_accesses):\n        i = rng.randint(0,\
    \ data['num_rows'] - 1)\n        row_size = data['offsets'][i + 1] - data['offsets'][i]\n\
    \        if row_size > 0:\n            j = rng.randint(0, row_size - 1)\n    \
    \        a1, a2, a3, a4, a5, a6 = csr(i, j)\n            checksum ^= (a1 + a2\
    \ + a3 + a4 + a5 + a6)\n    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"\
    direct_arrays\", \"random_access\")\ndef random_access_direct(data):\n    \"\"\
    \"Random access using direct indexing\"\"\"\n    arrays = [data['array_a1'], data['array_a2'],\
    \ data['array_a3'], \n              data['array_a4'], data['array_a5'], data['array_a6']]\n\
    \    offsets = data['offsets']\n    checksum = 0\n    num_accesses = min(1000,\
    \ data['size'] // 10)\n    \n    rng = random.Random(42)\n    for _ in range(num_accesses):\n\
    \        i = rng.randint(0, data['num_rows'] - 1)\n        start = offsets[i]\n\
    \        end = offsets[i + 1]\n        if end > start:\n            j = rng.randint(0,\
    \ end - start - 1)\n            idx = start + j\n            sum_val = sum(arr[idx]\
    \ for arr in arrays)\n            checksum ^= sum_val\n    return checksum & 0xFFFFFFFF\n\
    \n@benchmark.implementation(\"list_of_lists\", \"random_access\")\ndef random_access_list_of_lists(data):\n\
    \    \"\"\"Random access through list of lists\"\"\"\n    list_structure = data['list_structure']\n\
    \    checksum = 0\n    num_accesses = min(1000, data['size'] // 10)\n    \n  \
    \  rng = random.Random(42)\n    for _ in range(num_accesses):\n        i = rng.randint(0,\
    \ data['num_rows'] - 1)\n        if len(list_structure[i]) > 0:\n            j\
    \ = rng.randint(0, len(list_structure[i]) - 1)\n            a1, a2, a3, a4, a5,\
    \ a6 = list_structure[i][j]\n            checksum ^= (a1 + a2 + a3 + a4 + a5 +\
    \ a6)\n    return checksum & 0xFFFFFFFF\n\n# Setup for modify operations\n@benchmark.setup(\"\
    csr6\", [\"modification\"])\ndef setup_csr6_modify(data):\n    \"\"\"Copy data\
    \ before modification\"\"\"\n    new_data = data.copy()\n    new_data['array_a1']\
    \ = data['array_a1'].copy()\n    new_data['array_a2'] = data['array_a2'].copy()\n\
    \    new_data['array_a3'] = data['array_a3'].copy()\n    new_data['array_a4']\
    \ = data['array_a4'].copy()\n    new_data['array_a5'] = data['array_a5'].copy()\n\
    \    new_data['array_a6'] = data['array_a6'].copy()\n    return new_data\n\n@benchmark.setup(\"\
    direct_arrays\", [\"modification\"])\ndef setup_direct_modify(data):\n    \"\"\
    \"Copy data before modification\"\"\"\n    new_data = data.copy()\n    new_data['array_a1']\
    \ = data['array_a1'].copy()\n    new_data['array_a2'] = data['array_a2'].copy()\n\
    \    new_data['array_a3'] = data['array_a3'].copy()\n    new_data['array_a4']\
    \ = data['array_a4'].copy()\n    new_data['array_a5'] = data['array_a5'].copy()\n\
    \    new_data['array_a6'] = data['array_a6'].copy()\n    return new_data\n\n@benchmark.setup(\"\
    list_of_lists\", [\"modification\"])\ndef setup_list_of_lists_modify(data):\n\
    \    \"\"\"Copy list structure before modification\"\"\"\n    new_data = data.copy()\n\
    \    new_data['list_structure'] = [row.copy() for row in data['list_structure']]\n\
    \    return new_data\n\n# Modification operation\n@benchmark.implementation(\"\
    csr6\", \"modification\")\ndef modification_csr6(data):\n    \"\"\"Modify elements\
    \ using csr.set(i,j,val)\"\"\"\n    csr = CSR6(data['array_a1'], data['array_a2'],\
    \ data['array_a3'], \n               data['array_a4'], data['array_a5'], data['array_a6'],\
    \ data['offsets'])\n    checksum = 0\n    num_modifications = min(1000, data['size']\
    \ // 10)\n    \n    rng = random.Random(42)\n    for _ in range(num_modifications):\n\
    \        i = rng.randint(0, data['num_rows'] - 1)\n        row_size = data['offsets'][i\
    \ + 1] - data['offsets'][i]\n        if row_size > 0:\n            j = rng.randint(0,\
    \ row_size - 1)\n            new_vals = tuple(rng.randint(0, 1000000) for _ in\
    \ range(6))\n            csr.set(i, j, new_vals)\n            checksum ^= sum(new_vals)\n\
    \    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"direct_arrays\"\
    , \"modification\")\ndef modification_direct(data):\n    \"\"\"Modify elements\
    \ using direct array access\"\"\"\n    arrays = [data['array_a1'], data['array_a2'],\
    \ data['array_a3'], \n              data['array_a4'], data['array_a5'], data['array_a6']]\n\
    \    offsets = data['offsets']\n    checksum = 0\n    num_modifications = min(1000,\
    \ data['size'] // 10)\n    \n    rng = random.Random(42)\n    for _ in range(num_modifications):\n\
    \        i = rng.randint(0, data['num_rows'] - 1)\n        start = offsets[i]\n\
    \        end = offsets[i + 1]\n        if end > start:\n            j = rng.randint(0,\
    \ end - start - 1)\n            idx = start + j\n            new_vals = [rng.randint(0,\
    \ 1000000) for _ in range(6)]\n            for k, arr in enumerate(arrays):\n\
    \                arr[idx] = new_vals[k]\n            checksum ^= sum(new_vals)\n\
    \    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"modification\")\ndef modification_list_of_lists(data):\n    \"\"\"Modify elements\
    \ in list of lists\"\"\"\n    list_structure = data['list_structure']\n    checksum\
    \ = 0\n    num_modifications = min(1000, data['size'] // 10)\n    \n    rng =\
    \ random.Random(42)\n    for _ in range(num_modifications):\n        i = rng.randint(0,\
    \ data['num_rows'] - 1)\n        if len(list_structure[i]) > 0:\n            j\
    \ = rng.randint(0, len(list_structure[i]) - 1)\n            new_val = tuple(rng.randint(0,\
    \ 1000000) for _ in range(6))\n            list_structure[i][j] = new_val\n  \
    \          checksum ^= sum(new_val)\n    return checksum & 0xFFFFFFFF\n\n# Indexed\
    \ iteration using [i] access\n@benchmark.implementation(\"csr6\", \"indexed_iter\"\
    )\ndef indexed_iter_csr6(data):\n    \"\"\"Iterate using csr[i] access\"\"\"\n\
    \    csr = CSR6(data['array_a1'], data['array_a2'], data['array_a3'], \n     \
    \          data['array_a4'], data['array_a5'], data['array_a6'], data['offsets'])\n\
    \    checksum = 0\n    for i in range(len(csr)):\n        row_view = csr[i]\n\
    \        for j in range(len(row_view)):\n            a1, a2, a3, a4, a5, a6 =\
    \ row_view[j]\n            checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)\n    return\
    \ checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"direct_arrays\", \"indexed_iter\"\
    )\ndef indexed_iter_direct(data):\n    \"\"\"Iterate using direct array access\"\
    \"\"\n    arrays = [data['array_a1'], data['array_a2'], data['array_a3'], \n \
    \             data['array_a4'], data['array_a5'], data['array_a6']]\n    offsets\
    \ = data['offsets']\n    checksum = 0\n    for i in range(data['num_rows']):\n\
    \        for j in range(offsets[i], offsets[i + 1]):\n            sum_val = sum(arr[j]\
    \ for arr in arrays)\n            checksum ^= sum_val\n    return checksum & 0xFFFFFFFF\n\
    \n@benchmark.implementation(\"list_of_lists\", \"indexed_iter\")\ndef indexed_iter_list_of_lists(data):\n\
    \    \"\"\"Iterate using list[i] access\"\"\"\n    list_structure = data['list_structure']\n\
    \    checksum = 0\n    for i in range(len(list_structure)):\n        row = list_structure[i]\n\
    \        for j in range(len(row)):\n            a1, a2, a3, a4, a5, a6 = row[j]\n\
    \            checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)\n    return checksum &\
    \ 0xFFFFFFFF\n\n# Foreach iteration using for-in pattern\n@benchmark.implementation(\"\
    csr6\", \"foreach_iter\")\ndef foreach_iter_csr6(data):\n    \"\"\"Iterate using\
    \ for row in csr\"\"\"\n    csr = CSR6(data['array_a1'], data['array_a2'], data['array_a3'],\
    \ \n               data['array_a4'], data['array_a5'], data['array_a6'], data['offsets'])\n\
    \    checksum = 0\n    for row_view in csr:\n        for a1, a2, a3, a4, a5, a6\
    \ in row_view:\n            checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)\n    return\
    \ checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"direct_arrays\", \"foreach_iter\"\
    )\ndef foreach_iter_direct(data):\n    \"\"\"Iterate using direct arrays with\
    \ manual chunking\"\"\"\n    arrays = [data['array_a1'], data['array_a2'], data['array_a3'],\
    \ \n              data['array_a4'], data['array_a5'], data['array_a6']]\n    offsets\
    \ = data['offsets']\n    checksum = 0\n    for i in range(data['num_rows']):\n\
    \        for j in range(offsets[i], offsets[i + 1]):\n            sum_val = sum(arr[j]\
    \ for arr in arrays)\n            checksum ^= sum_val\n    return checksum & 0xFFFFFFFF\n\
    \n@benchmark.implementation(\"list_of_lists\", \"foreach_iter\")\ndef foreach_iter_list_of_lists(data):\n\
    \    \"\"\"Iterate using for row in list\"\"\"\n    list_structure = data['list_structure']\n\
    \    checksum = 0\n    for row in list_structure:\n        for a1, a2, a3, a4,\
    \ a5, a6 in row:\n            checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)\n    return\
    \ checksum & 0xFFFFFFFF\n\n# Bucketize operation\n@benchmark.implementation(\"\
    csr6\", \"bucketize\")\ndef bucketize_csr6(data):\n    \"\"\"Use CSR6.bucketize\
    \ method\"\"\"\n    csr = CSR6.bucketize(data['num_rows'], data['keys'], \n  \
    \                       data['values_v1'], data['values_v2'], data['values_v3'],\n\
    \                         data['values_v4'], data['values_v5'], data['values_v6'])\n\
    \    checksum = 0\n    for i in range(len(csr)):\n        view = csr[i]\n    \
    \    for j in range(len(view)):\n            vals = (view.A1[view.l + j], view.A2[view.l\
    \ + j], view.A3[view.l + j],\n                    view.A4[view.l + j], view.A5[view.l\
    \ + j], view.A6[view.l + j])\n            checksum ^= sum(vals)\n    return checksum\
    \ & 0xFFFFFFFF\n\n@benchmark.implementation(\"manual_bucketize\", \"bucketize\"\
    )\ndef bucketize_manual(data):\n    \"\"\"Manual bucketization into lists\"\"\"\
    \n    keys = data['keys']\n    values = [data['values_v1'], data['values_v2'],\
    \ data['values_v3'],\n              data['values_v4'], data['values_v5'], data['values_v6']]\n\
    \    num_rows = data['num_rows']\n    \n    buckets = [[[] for _ in range(6)]\
    \ for _ in range(num_rows)]\n    \n    for i in range(len(keys)):\n        k =\
    \ keys[i]\n        if 0 <= k < num_rows:\n            for j in range(6):\n   \
    \             buckets[k][j].append(values[j][i])\n    \n    checksum = 0\n   \
    \ for i in range(num_rows):\n        for j in range(len(buckets[i][0])):\n   \
    \         sum_val = sum(buckets[i][k][j] for k in range(6))\n            checksum\
    \ ^= sum_val\n    return checksum & 0xFFFFFFFF\n\n# Column-1 iteration - indexed\
    \ access\n@benchmark.implementation(\"csr6\", \"col1_indexed_iter\")\ndef col1_indexed_csr6(data):\n\
    \    \"\"\"Iterate through CSR6 where every row has exactly 1 element using indexed\
    \ access\"\"\"\n    arrays = [data['array_a1'], data['array_a2'], data['array_a3'],\
    \ \n              data['array_a4'], data['array_a5'], data['array_a6']]\n    offsets\
    \ = data['offsets']\n    csr = CSR6(*arrays, offsets)\n    \n    checksum = 0\n\
    \    # Iterate through many single-element rows using indexing\n    for i in range(len(csr)):\n\
    \        view = csr[i]  # Each view has exactly 1 element\n        sum_val = sum(arr[view.l]\
    \ for arr in [view.A1, view.A2, view.A3, view.A4, view.A5, view.A6])\n       \
    \ checksum ^= sum_val\n    \n    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"\
    list_of_lists\", \"col1_indexed_iter\")\ndef col1_indexed_lists(data):\n    \"\
    \"\"Iterate through list of single-element lists using indexed access\"\"\"\n\
    \    list_structure = data['list_structure']\n    \n    checksum = 0\n    # Iterate\
    \ through many single-element lists using indexing\n    for i in range(len(list_structure)):\n\
    \        a1, a2, a3, a4, a5, a6 = list_structure[i][0]  # Each row has exactly\
    \ 1 element\n        checksum ^= (a1 + a2 + a3 + a4 + a5 + a6)\n    \n    return\
    \ checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"direct_arrays\", \"col1_indexed_iter\"\
    )\ndef col1_indexed_direct(data):\n    \"\"\"Direct indexed access through arrays\
    \ (baseline for single elements)\"\"\"\n    arrays = [data['array_a1'], data['array_a2'],\
    \ data['array_a3'], \n              data['array_a4'], data['array_a5'], data['array_a6']]\n\
    \    \n    checksum = 0\n    # Direct indexed iteration - each element is its\
    \ own \"row\"\n    for i in range(len(arrays[0])):\n        sum_val = sum(arr[i]\
    \ for arr in arrays)\n        checksum ^= sum_val\n    \n    return checksum &\
    \ 0xFFFFFFFF\n\n@benchmark.implementation(\"csr6\", \"col1_foreach_iter\")\ndef\
    \ col1_foreach_csr6(data):\n    \"\"\"Iterate through CSR6 using foreach loop\
    \ where every row has exactly 1 element\"\"\"\n    arrays = [data['array_a1'],\
    \ data['array_a2'], data['array_a3'], \n              data['array_a4'], data['array_a5'],\
    \ data['array_a6']]\n    offsets = data['offsets']\n    csr = CSR6(*arrays, offsets)\n\
    \    \n    checksum = 0\n    # Use foreach iteration pattern\n    for view in\
    \ csr:  # Each view has exactly 1 element\n        a1, a2, a3, a4, a5, a6 = view[0]\
    \  # Access the single element\n        checksum ^= (a1 + a2 + a3 + a4 + a5 +\
    \ a6)\n    \n    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"\
    list_of_lists\", \"col1_foreach_iter\")\ndef col1_foreach_lists(data):\n    \"\
    \"\"Iterate through list of single-element lists using foreach\"\"\"\n    list_structure\
    \ = data['list_structure']\n    \n    checksum = 0\n    # Use foreach iteration\
    \ pattern\n    for row in list_structure:\n        a1, a2, a3, a4, a5, a6 = row[0]\
    \  # Each row has exactly 1 element\n        checksum ^= (a1 + a2 + a3 + a4 +\
    \ a5 + a6)\n    \n    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"\
    direct_arrays\", \"col1_foreach_iter\")\ndef col1_foreach_direct(data):\n    \"\
    \"\"Direct foreach iteration through arrays (baseline for single elements)\"\"\
    \"\n    arrays = [data['array_a1'], data['array_a2'], data['array_a3'], \n   \
    \           data['array_a4'], data['array_a5'], data['array_a6']]\n    \n    checksum\
    \ = 0\n    # Direct foreach iteration - each element is its own \"row\"\n    for\
    \ i in range(len(arrays[0])):\n        sum_val = sum(arr[i] for arr in arrays)\n\
    \        checksum ^= sum_val\n    \n    return checksum & 0xFFFFFFFF\n\nif __name__\
    \ == \"__main__\":\n    # Parse command line args and run appropriate mode\n \
    \   runner = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/view/csr6_cls.py
  - cp_library/ds/view/view6_cls.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/perf/checksum.py
  - cp_library/alg/iter/sort/isort_ranged_fn.py
  - cp_library/alg/iter/arg/argsort_ranged_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: false
  path: perf/csr6.py
  requiredBy: []
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/csr6.py
layout: document
redirect_from:
- /library/perf/csr6.py
- /library/perf/csr6.py.html
title: perf/csr6.py
---
