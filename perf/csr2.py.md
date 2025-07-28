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
    path: cp_library/ds/view/csr2_cls.py
    title: cp_library/ds/view/csr2_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view2_cls.py
    title: cp_library/ds/view/view2_cls.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing CSR2 vs direct arrays\
    \ for dual-array sparse data.\nCSR2 provides view2 objects for efficient row access\
    \ patterns.\n\"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0,\
    \ os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig\nfrom cp_library.ds.view.csr2_cls import CSR2\n\
    from cp_library.ds.view.view2_cls import view2\n\n# Configure benchmark\nconfig\
    \ = BenchmarkConfig(\n    name=\"csr2\",\n    sizes=[1000000, 100000, 10000, 1000,\
    \ 100],  # Reverse order to warm up JIT\n    operations=['copy_construction',\
    \ 'direct_access', 'random_access', 'indexed_iter', 'foreach_iter', 'modification',\
    \ 'bucketize', 'col1_indexed_iter', 'col1_foreach_iter'],\n    iterations=10,\n\
    \    warmup=3,\n    output_dir=\"./output/benchmark_results/csr2\"\n)\n\n# Create\
    \ benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\n@benchmark.data_generator(\"\
    default\")\ndef generate_csr2_data(size: int, operation: str):\n    \"\"\"Generate\
    \ test data for CSR2 operations\"\"\"\n    # Create rows with variable sizes\n\
    \    num_rows = max(1, size // 100)  # Average 100 elements per row\n    row_sizes\
    \ = []\n    total = 0\n    \n    while total < size:\n        row_size = random.randint(50,\
    \ 150)\n        if total + row_size > size:\n            row_size = size - total\n\
    \        row_sizes.append(row_size)\n        total += row_size\n    \n    # Generate\
    \ offset array\n    offsets = [0]\n    for row_size in row_sizes:\n        offsets.append(offsets[-1]\
    \ + row_size)\n    \n    # Generate data arrays\n    array_a = [random.randint(0,\
    \ 1000000) for _ in range(size)]\n    array_b = [random.randint(0, 1000000) for\
    \ _ in range(size)]\n    \n    # Create list of lists structure\n    list_structure\
    \ = []\n    for i in range(len(row_sizes)):\n        start = offsets[i]\n    \
    \    end = offsets[i + 1]\n        row = [(array_a[j], array_b[j]) for j in range(start,\
    \ end)]\n        list_structure.append(row)\n    \n    # For bucketize operation\n\
    \    actual_num_rows = len(row_sizes)\n    keys = [random.randint(0, max(0, actual_num_rows\
    \ - 1)) for _ in range(size)]\n    values_v = [random.randint(0, 1000000) for\
    \ _ in range(size)]\n    values_w = [random.randint(0, 1000000) for _ in range(size)]\n\
    \    \n    return {\n        'array_a': array_a,\n        'array_b': array_b,\n\
    \        'offsets': offsets,\n        'num_rows': len(row_sizes),\n        'list_structure':\
    \ list_structure,\n        'keys': keys,\n        'values_v': values_v,\n    \
    \    'values_w': values_w,\n        'size': size\n    }\n\n# Specialized data\
    \ generator for single-element rows\n@benchmark.data_generator(\"col1_indexed_iter\"\
    )\ndef generate_col1_indexed_data(size: int, operation: str):\n    \"\"\"Generate\
    \ test data where every row has exactly 1 column - tests indexed iteration\"\"\
    \"\n    return _generate_col1_data(size, operation)\n\n@benchmark.data_generator(\"\
    col1_foreach_iter\")\ndef generate_col1_foreach_data(size: int, operation: str):\n\
    \    \"\"\"Generate test data where every row has exactly 1 column - tests foreach\
    \ iteration\"\"\"\n    return _generate_col1_data(size, operation)\n\ndef _generate_col1_data(size:\
    \ int, operation: str):\n    \"\"\"Helper to generate single-element row data\"\
    \"\"\n    # Each row has exactly 1 element\n    num_rows = size\n    \n    # Generate\
    \ offset array for single-element rows\n    offsets = list(range(size + 1))  #\
    \ [0, 1, 2, 3, ..., size]\n    \n    # Generate data arrays\n    array_a = [random.randint(0,\
    \ 1000000) for _ in range(size)]\n    array_b = [random.randint(0, 1000000) for\
    \ _ in range(size)]\n    \n    # Create list of lists structure (each row has\
    \ 1 element)\n    list_structure = [[(array_a[i], array_b[i])] for i in range(size)]\n\
    \    \n    # For bucketize operation - distribute across fewer buckets to avoid\
    \ empty ones\n    bucket_count = max(1, size // 10)  # 10 elements per bucket\
    \ on average\n    keys = [random.randint(0, bucket_count - 1) for _ in range(size)]\n\
    \    values_v = [random.randint(0, 1000000) for _ in range(size)]\n    values_w\
    \ = [random.randint(0, 1000000) for _ in range(size)]\n    \n    return {\n  \
    \      'array_a': array_a,\n        'array_b': array_b,\n        'offsets': offsets,\n\
    \        'num_rows': num_rows,\n        'list_structure': list_structure,\n  \
    \      'keys': keys,\n        'values_v': values_v,\n        'values_w': values_w,\n\
    \        'size': size,\n        'bucket_count': bucket_count\n    }\n\n# Copy\
    \ construction operation\n@benchmark.implementation(\"csr2\", \"copy_construction\"\
    )\ndef copy_construction_csr2(data):\n    \"\"\"Construct CSR2 from copied arrays\
    \ for fair comparison\"\"\"\n    array_a_copy = data['array_a'].copy()\n    array_b_copy\
    \ = data['array_b'].copy()\n    offsets_copy = data['offsets'].copy()\n    csr\
    \ = CSR2(array_a_copy, array_b_copy, offsets_copy)\n    return len(csr)\n\n@benchmark.implementation(\"\
    direct_arrays\", \"copy_construction\")\ndef copy_construction_direct(data):\n\
    \    \"\"\"Copy arrays for fair comparison with CSR2\"\"\"\n    array_a_copy =\
    \ data['array_a'].copy()\n    array_b_copy = data['array_b'].copy()\n    offsets_copy\
    \ = data['offsets'].copy()\n    return len(offsets_copy) - 1  # Return number\
    \ of rows\n\n@benchmark.implementation(\"list_of_lists\", \"copy_construction\"\
    )\ndef copy_construction_list_of_lists(data):\n    \"\"\"Copy pre-initialized\
    \ list of lists\"\"\"\n    list_structure = [row.copy() for row in data['list_structure']]\n\
    \    return len(list_structure)\n\n# Direct access operation\n@benchmark.implementation(\"\
    csr2\", \"direct_access\")\ndef direct_access_csr2(data):\n    \"\"\"Direct access\
    \ through CSR2 views\"\"\"\n    csr = CSR2(data['array_a'], data['array_b'], data['offsets'])\n\
    \    checksum = 0\n    for i in range(len(csr)):\n        view = csr[i]\n    \
    \    for j in range(len(view)):\n            a_val = view.A[view.l + j]\n    \
    \        b_val = view.B[view.l + j]\n            checksum ^= (a_val + b_val)\n\
    \    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"direct_arrays\"\
    , \"direct_access\")\ndef direct_access_direct(data):\n    \"\"\"Direct access\
    \ using direct arrays\"\"\"\n    array_a = data['array_a']\n    array_b = data['array_b']\n\
    \    offsets = data['offsets']\n    checksum = 0\n    for i in range(data['num_rows']):\n\
    \        for j in range(offsets[i], offsets[i + 1]):\n            checksum ^=\
    \ (array_a[j] + array_b[j])\n    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"\
    list_of_lists\", \"direct_access\")\ndef direct_access_list_of_lists(data):\n\
    \    \"\"\"Direct access through list of lists\"\"\"\n    list_structure = data['list_structure']\n\
    \    checksum = 0\n    for row in list_structure:\n        for a_val, b_val in\
    \ row:\n            checksum ^= (a_val + b_val)\n    return checksum & 0xFFFFFFFF\n\
    \n# Random access operation\n@benchmark.implementation(\"csr2\", \"random_access\"\
    )\ndef random_access_csr2(data):\n    \"\"\"Random access using csr(i,j)\"\"\"\
    \n    csr = CSR2(data['array_a'], data['array_b'], data['offsets'])\n    checksum\
    \ = 0\n    num_accesses = min(1000, data['size'] // 10)\n    \n    rng = random.Random(42)\n\
    \    for _ in range(num_accesses):\n        i = rng.randint(0, data['num_rows']\
    \ - 1)\n        row_size = data['offsets'][i + 1] - data['offsets'][i]\n     \
    \   if row_size > 0:\n            j = rng.randint(0, row_size - 1)\n         \
    \   a_val, b_val = csr(i, j)\n            checksum ^= (a_val + b_val)\n    return\
    \ checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"direct_arrays\", \"random_access\"\
    )\ndef random_access_direct(data):\n    \"\"\"Random access using direct indexing\"\
    \"\"\n    array_a = data['array_a']\n    array_b = data['array_b']\n    offsets\
    \ = data['offsets']\n    checksum = 0\n    num_accesses = min(1000, data['size']\
    \ // 10)\n    \n    rng = random.Random(42)\n    for _ in range(num_accesses):\n\
    \        i = rng.randint(0, data['num_rows'] - 1)\n        start = offsets[i]\n\
    \        end = offsets[i + 1]\n        if end > start:\n            j = rng.randint(0,\
    \ end - start - 1)\n            checksum ^= (array_a[start + j] + array_b[start\
    \ + j])\n    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"random_access\")\ndef random_access_list_of_lists(data):\n    \"\"\"Random\
    \ access through list of lists\"\"\"\n    list_structure = data['list_structure']\n\
    \    checksum = 0\n    num_accesses = min(1000, data['size'] // 10)\n    \n  \
    \  rng = random.Random(42)\n    for _ in range(num_accesses):\n        i = rng.randint(0,\
    \ data['num_rows'] - 1)\n        if len(list_structure[i]) > 0:\n            j\
    \ = rng.randint(0, len(list_structure[i]) - 1)\n            a_val, b_val = list_structure[i][j]\n\
    \            checksum ^= (a_val + b_val)\n    return checksum & 0xFFFFFFFF\n\n\
    # Setup for modify operations\n@benchmark.setup(\"csr2\", [\"modification\"])\n\
    def setup_csr2_modify(data):\n    \"\"\"Copy data before modification\"\"\"\n\
    \    new_data = data.copy()\n    new_data['array_a'] = data['array_a'].copy()\n\
    \    new_data['array_b'] = data['array_b'].copy()\n    return new_data\n\n@benchmark.setup(\"\
    direct_arrays\", [\"modification\"])\ndef setup_direct_modify(data):\n    \"\"\
    \"Copy data before modification\"\"\"\n    new_data = data.copy()\n    new_data['array_a']\
    \ = data['array_a'].copy()\n    new_data['array_b'] = data['array_b'].copy()\n\
    \    return new_data\n\n@benchmark.setup(\"list_of_lists\", [\"modification\"\
    ])\ndef setup_list_of_lists_modify(data):\n    \"\"\"Copy list structure before\
    \ modification\"\"\"\n    new_data = data.copy()\n    new_data['list_structure']\
    \ = [row.copy() for row in data['list_structure']]\n    return new_data\n\n# Modification\
    \ operation\n@benchmark.implementation(\"csr2\", \"modification\")\ndef modification_csr2(data):\n\
    \    \"\"\"Modify elements using csr.set(i,j,val)\"\"\"\n    csr = CSR2(data['array_a'],\
    \ data['array_b'], data['offsets'])\n    checksum = 0\n    num_modifications =\
    \ min(1000, data['size'] // 10)\n    \n    rng = random.Random(42)\n    for _\
    \ in range(num_modifications):\n        i = rng.randint(0, data['num_rows'] -\
    \ 1)\n        row_size = data['offsets'][i + 1] - data['offsets'][i]\n       \
    \ if row_size > 0:\n            j = rng.randint(0, row_size - 1)\n           \
    \ new_val = (rng.randint(0, 1000000), rng.randint(0, 1000000))\n            csr.set(i,\
    \ j, new_val)\n            checksum ^= (new_val[0] + new_val[1])\n    return checksum\
    \ & 0xFFFFFFFF\n\n@benchmark.implementation(\"direct_arrays\", \"modification\"\
    )\ndef modification_direct(data):\n    \"\"\"Modify elements using direct array\
    \ access\"\"\"\n    array_a = data['array_a']\n    array_b = data['array_b']\n\
    \    offsets = data['offsets']\n    checksum = 0\n    num_modifications = min(1000,\
    \ data['size'] // 10)\n    \n    rng = random.Random(42)\n    for _ in range(num_modifications):\n\
    \        i = rng.randint(0, data['num_rows'] - 1)\n        start = offsets[i]\n\
    \        end = offsets[i + 1]\n        if end > start:\n            j = rng.randint(0,\
    \ end - start - 1)\n            new_val_a = rng.randint(0, 1000000)\n        \
    \    new_val_b = rng.randint(0, 1000000)\n            array_a[start + j] = new_val_a\n\
    \            array_b[start + j] = new_val_b\n            checksum ^= (new_val_a\
    \ + new_val_b)\n    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"\
    list_of_lists\", \"modification\")\ndef modification_list_of_lists(data):\n  \
    \  \"\"\"Modify elements in list of lists\"\"\"\n    list_structure = data['list_structure']\n\
    \    checksum = 0\n    num_modifications = min(1000, data['size'] // 10)\n   \
    \ \n    rng = random.Random(42)\n    for _ in range(num_modifications):\n    \
    \    i = rng.randint(0, data['num_rows'] - 1)\n        if len(list_structure[i])\
    \ > 0:\n            j = rng.randint(0, len(list_structure[i]) - 1)\n         \
    \   new_val = (rng.randint(0, 1000000), rng.randint(0, 1000000))\n           \
    \ list_structure[i][j] = new_val\n            checksum ^= (new_val[0] + new_val[1])\n\
    \    return checksum & 0xFFFFFFFF\n\n# Indexed iteration using [i] access\n@benchmark.implementation(\"\
    csr2\", \"indexed_iter\")\ndef indexed_iter_csr2(data):\n    \"\"\"Iterate using\
    \ csr[i] access\"\"\"\n    csr = CSR2(data['array_a'], data['array_b'], data['offsets'])\n\
    \    checksum = 0\n    for i in range(len(csr)):\n        row_view = csr[i]\n\
    \        for j in range(len(row_view)):\n            a_val, b_val = row_view[j]\n\
    \            checksum ^= (a_val + b_val)\n    return checksum & 0xFFFFFFFF\n\n\
    @benchmark.implementation(\"direct_arrays\", \"indexed_iter\")\ndef indexed_iter_direct(data):\n\
    \    \"\"\"Iterate using direct array access\"\"\"\n    array_a = data['array_a']\n\
    \    array_b = data['array_b']\n    offsets = data['offsets']\n    checksum =\
    \ 0\n    for i in range(data['num_rows']):\n        for j in range(offsets[i],\
    \ offsets[i + 1]):\n            checksum ^= (array_a[j] + array_b[j])\n    return\
    \ checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"list_of_lists\", \"indexed_iter\"\
    )\ndef indexed_iter_list_of_lists(data):\n    \"\"\"Iterate using list[i] access\"\
    \"\"\n    list_structure = data['list_structure']\n    checksum = 0\n    for i\
    \ in range(len(list_structure)):\n        row = list_structure[i]\n        for\
    \ j in range(len(row)):\n            a_val, b_val = row[j]\n            checksum\
    \ ^= (a_val + b_val)\n    return checksum & 0xFFFFFFFF\n\n# Foreach iteration\
    \ using for-in pattern\n@benchmark.implementation(\"csr2\", \"foreach_iter\")\n\
    def foreach_iter_csr2(data):\n    \"\"\"Iterate using for row in csr\"\"\"\n \
    \   csr = CSR2(data['array_a'], data['array_b'], data['offsets'])\n    checksum\
    \ = 0\n    for row_view in csr:\n        for a_val, b_val in row_view:\n     \
    \       checksum ^= (a_val + b_val)\n    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"\
    direct_arrays\", \"foreach_iter\")\ndef foreach_iter_direct(data):\n    \"\"\"\
    Iterate using direct arrays with manual chunking\"\"\"\n    array_a = data['array_a']\n\
    \    array_b = data['array_b']\n    offsets = data['offsets']\n    checksum =\
    \ 0\n    for i in range(data['num_rows']):\n        for j in range(offsets[i],\
    \ offsets[i + 1]):\n            checksum ^= (array_a[j] + array_b[j])\n    return\
    \ checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"list_of_lists\", \"foreach_iter\"\
    )\ndef foreach_iter_list_of_lists(data):\n    \"\"\"Iterate using for row in list\"\
    \"\"\n    list_structure = data['list_structure']\n    checksum = 0\n    for row\
    \ in list_structure:\n        for a_val, b_val in row:\n            checksum ^=\
    \ (a_val + b_val)\n    return checksum & 0xFFFFFFFF\n\n\n# Bucketize operation\n\
    @benchmark.implementation(\"csr2\", \"bucketize\")\ndef bucketize_csr2(data):\n\
    \    \"\"\"Use CSR2.bucketize method\"\"\"\n    csr = CSR2.bucketize(data['num_rows'],\
    \ data['keys'], data['values_v'], data['values_w'])\n    checksum = 0\n    for\
    \ i in range(len(csr)):\n        view = csr[i]\n        for j in range(len(view)):\n\
    \            checksum ^= (view.A[view.l + j] + view.B[view.l + j])\n    return\
    \ checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"manual_bucketize\", \"\
    bucketize\")\ndef bucketize_manual(data):\n    \"\"\"Manual bucketization into\
    \ lists\"\"\"\n    keys = data['keys']\n    values_v = data['values_v']\n    values_w\
    \ = data['values_w']\n    num_rows = data['num_rows']\n    \n    buckets_a = [[]\
    \ for _ in range(num_rows)]\n    buckets_b = [[] for _ in range(num_rows)]\n \
    \   \n    for i in range(len(keys)):\n        k = keys[i]\n        if 0 <= k <\
    \ num_rows:\n            buckets_a[k].append(values_v[i])\n            buckets_b[k].append(values_w[i])\n\
    \    \n    checksum = 0\n    for i in range(num_rows):\n        for j in range(len(buckets_a[i])):\n\
    \            checksum ^= (buckets_a[i][j] + buckets_b[i][j])\n    return checksum\
    \ & 0xFFFFFFFF\n\n# Column-1 iteration - indexed access\n@benchmark.implementation(\"\
    csr2\", \"col1_indexed_iter\")\ndef col1_indexed_csr2(data):\n    \"\"\"Iterate\
    \ through CSR2 where every row has exactly 1 element using indexed access\"\"\"\
    \n    array_a = data['array_a']\n    array_b = data['array_b']\n    offsets =\
    \ data['offsets']\n    csr = CSR2(array_a, array_b, offsets)\n    \n    checksum\
    \ = 0\n    # Iterate through many single-element rows using indexing\n    for\
    \ i in range(len(csr)):\n        view = csr[i]  # Each view has exactly 1 element\n\
    \        checksum ^= (view.A[view.l] + view.B[view.l])  # Direct access to single\
    \ element\n    \n    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"\
    list_of_lists\", \"col1_indexed_iter\")\ndef col1_indexed_lists(data):\n    \"\
    \"\"Iterate through list of single-element lists using indexed access\"\"\"\n\
    \    list_structure = data['list_structure']\n    \n    checksum = 0\n    # Iterate\
    \ through many single-element lists using indexing\n    for i in range(len(list_structure)):\n\
    \        a_val, b_val = list_structure[i][0]  # Each row has exactly 1 element\n\
    \        checksum ^= (a_val + b_val)\n    \n    return checksum & 0xFFFFFFFF\n\
    \n@benchmark.implementation(\"direct_arrays\", \"col1_indexed_iter\")\ndef col1_indexed_direct(data):\n\
    \    \"\"\"Direct indexed access through arrays (baseline for single elements)\"\
    \"\"\n    array_a = data['array_a']\n    array_b = data['array_b']\n    \n   \
    \ checksum = 0\n    # Direct indexed iteration - each element is its own \"row\"\
    \n    for i in range(len(array_a)):\n        checksum ^= (array_a[i] + array_b[i])\n\
    \    \n    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"csr2\"\
    , \"col1_foreach_iter\")\ndef col1_foreach_csr2(data):\n    \"\"\"Iterate through\
    \ CSR2 using foreach loop where every row has exactly 1 element\"\"\"\n    array_a\
    \ = data['array_a']\n    array_b = data['array_b']\n    offsets = data['offsets']\n\
    \    csr = CSR2(array_a, array_b, offsets)\n    \n    checksum = 0\n    # Use\
    \ foreach iteration pattern\n    for view in csr:  # Each view has exactly 1 element\n\
    \        a_val, b_val = view[0]  # Access the single element\n        checksum\
    \ ^= (a_val + b_val)\n    \n    return checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"\
    list_of_lists\", \"col1_foreach_iter\")\ndef col1_foreach_lists(data):\n    \"\
    \"\"Iterate through list of single-element lists using foreach\"\"\"\n    list_structure\
    \ = data['list_structure']\n    \n    checksum = 0\n    # Use foreach iteration\
    \ pattern\n    for row in list_structure:\n        a_val, b_val = row[0]  # Each\
    \ row has exactly 1 element\n        checksum ^= (a_val + b_val)\n    \n    return\
    \ checksum & 0xFFFFFFFF\n\n@benchmark.implementation(\"direct_arrays\", \"col1_foreach_iter\"\
    )\ndef col1_foreach_direct(data):\n    \"\"\"Direct foreach iteration through\
    \ arrays (baseline for single elements)\"\"\"\n    array_a = data['array_a']\n\
    \    array_b = data['array_b']\n    \n    checksum = 0\n    # Direct foreach iteration\
    \ - each element is its own \"row\"\n    for i in range(len(array_a)):\n     \
    \   checksum ^= (array_a[i] + array_b[i])\n    \n    return checksum & 0xFFFFFFFF\n\
    \nif __name__ == \"__main__\":\n    # Parse command line args and run appropriate\
    \ mode\n    runner = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/view/csr2_cls.py
  - cp_library/ds/view/view2_cls.py
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
  path: perf/csr2.py
  requiredBy: []
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/csr2.py
layout: document
redirect_from:
- /library/perf/csr2.py
- /library/perf/csr2.py.html
title: perf/csr2.py
---
