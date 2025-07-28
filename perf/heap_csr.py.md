---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/fast_heapq.py
    title: cp_library/ds/heap/fast_heapq.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing heap operations on CSR\
    \ sparse rows vs list of lists/heaps.\nTests heapify, heappop, heapreplace, heappush,\
    \ heappushpop operations.\n\"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0,\
    \ os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig\nfrom cp_library.ds.view.csr_cls import CSR\n\
    from cp_library.ds.heap.fast_heapq import heapify, heappop, heapreplace, heappush,\
    \ heappushpop\n\n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"\
    heap_csr\",\n    sizes=[10000000, 1000000, 100000, 10000, 1000, 100, 10],  # Reverse\
    \ order to warm up JIT\n    operations=['initialization', 'initialization_bucketize',\
    \ 'heapify', 'heappop', 'heapreplace', 'heappush', 'heappushpop'],\n    iterations=10,\n\
    \    warmup=3,\n    output_dir=\"./output/benchmark_results/heap_csr\"\n)\n\n\
    # Create benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\
    \ for initialization\n@benchmark.data_generator(\"initialization\")\ndef generate_initialization_data(size:\
    \ int, operation: str):\n    \"\"\"Generate raw data for initialization benchmark\"\
    \"\"\n    # Generate multiple sparse rows (each row is a heap)\n    num_rows =\
    \ max(10, size // 100)  # 10-100 rows depending on size\n    total_elements =\
    \ size\n    \n    # Generate raw row data\n    raw_rows = []\n    elements_per_row\
    \ = total_elements // num_rows\n    remaining = total_elements % num_rows\n  \
    \  \n    for i in range(num_rows):\n        # Variable row sizes (some rows get\
    \ extra elements)\n        row_size = elements_per_row + (1 if i < remaining else\
    \ 0)\n        row_size = max(1, row_size)  # Ensure at least 1 element per row\n\
    \        \n        # Generate random heap data for this row\n        row_data\
    \ = [random.randint(1, 1000000) for _ in range(row_size)]\n        raw_rows.append(row_data)\n\
    \    \n    return {\n        'raw_rows': raw_rows,\n        'num_rows': num_rows,\n\
    \        'size': size,\n        'operation': operation\n    }\n\n# Data generator\
    \ for bucketize initialization\n@benchmark.data_generator(\"initialization_bucketize\"\
    )\ndef generate_bucketize_data(size: int, operation: str):\n    \"\"\"Generate\
    \ (key, value) pairs for bucketize initialization benchmark\"\"\"\n    # Generate\
    \ multiple sparse rows (each row is a heap)\n    num_rows = max(10, size // 100)\
    \  # 10-100 rows depending on size\n    total_elements = size\n    \n    # Generate\
    \ (key, value) pairs\n    keys = []\n    values = []\n    \n    elements_per_row\
    \ = total_elements // num_rows\n    remaining = total_elements % num_rows\n  \
    \  \n    for i in range(num_rows):\n        # Variable row sizes (some rows get\
    \ extra elements)\n        row_size = elements_per_row + (1 if i < remaining else\
    \ 0)\n        row_size = max(1, row_size)  # Ensure at least 1 element per row\n\
    \        \n        # Generate random heap data for this row\n        for _ in\
    \ range(row_size):\n            keys.append(i)  # Row index as key\n         \
    \   values.append(random.randint(1, 1000000))  # Random value\n    \n    # Shuffle\
    \ to simulate unsorted input\n    combined = list(zip(keys, values))\n    random.shuffle(combined)\n\
    \    keys, values = zip(*combined)\n    keys, values = list(keys), list(values)\n\
    \    \n    # Create equivalent raw rows for list_of_lists comparison\n    raw_rows\
    \ = [[] for _ in range(num_rows)]\n    for key, value in zip(keys, values):\n\
    \        raw_rows[key].append(value)\n    \n    return {\n        'keys': keys,\n\
    \        'values': values,\n        'raw_rows': raw_rows,\n        'num_rows':\
    \ num_rows,\n        'size': size,\n        'operation': operation\n    }\n\n\
    # Data generator for other operations\n@benchmark.data_generator(\"default\")\n\
    def generate_csr_heap_data(size: int, operation: str):\n    \"\"\"Generate test\
    \ data for CSR heap operations\"\"\"\n    # Generate multiple sparse rows (each\
    \ row is a heap)\n    num_rows = max(10, size // 100)  # 10-100 rows depending\
    \ on size\n    total_elements = size\n    \n    # Create sparse row data\n   \
    \ A = []  # All elements concatenated\n    O = [0]  # Offsets for each row\n \
    \   \n    elements_per_row = total_elements // num_rows\n    remaining = total_elements\
    \ % num_rows\n    \n    for i in range(num_rows):\n        # Variable row sizes\
    \ (some rows get extra elements)\n        row_size = elements_per_row + (1 if\
    \ i < remaining else 0)\n        row_size = max(1, row_size)  # Ensure at least\
    \ 1 element per row\n        \n        # Generate random heap data for this row\n\
    \        row_data = [random.randint(1, 1000000) for _ in range(row_size)]\n  \
    \      A.extend(row_data)\n        O.append(len(A))\n    \n    # Create list of\
    \ lists equivalent\n    list_of_lists = []\n    for i in range(num_rows):\n  \
    \      start, end = O[i], O[i + 1]\n        list_of_lists.append(A[start:end].copy())\n\
    \    \n    return {\n        'A': A,\n        'O': O,\n        'list_of_lists':\
    \ list_of_lists,\n        'num_rows': num_rows,\n        'new_value': random.randint(1,\
    \ 1000000),\n        'target_row': random.randint(0, num_rows - 1),\n        'size':\
    \ size,\n        'operation': operation\n    }\n\n# Setup functions for operations\
    \ that modify data\n@benchmark.setup(\"csr\", [\"heappop\", \"heapreplace\", \"\
    heappush\", \"heappushpop\"])\ndef setup_csr_heap(data):\n    \"\"\"Setup function\
    \ that copies data and heapifies CSR rows\"\"\"\n    new_data = data.copy()\n\
    \    new_data['A'] = data['A'].copy()\n    new_data['O'] = data['O'].copy()\n\
    \    \n    # Create CSR and pre-heapify all rows\n    csr = CSR(new_data['A'],\
    \ new_data['O'])\n    for row_view in csr:\n        heapify(row_view)\n    \n\
    \    new_data['csr'] = csr\n    return new_data\n\n@benchmark.setup(\"list_of_lists\"\
    , [\"heappop\", \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef setup_list_of_lists_heap(data):\n\
    \    \"\"\"Setup function that copies data and heapifies list of lists\"\"\"\n\
    \    new_data = data.copy()\n    # Deep copy list of lists\n    new_data['list_of_lists']\
    \ = [row.copy() for row in data['list_of_lists']]\n    \n    # Pre-heapify all\
    \ lists\n    for row in new_data['list_of_lists']:\n        heapify(row)\n   \
    \ \n    return new_data\n\n# For heapify operation, we need setup without pre-heapifying\n\
    @benchmark.setup(\"csr\", [\"heapify\"])\ndef setup_csr_heapify(data):\n    \"\
    \"\"Setup function that only copies data for heapify operation\"\"\"\n    new_data\
    \ = data.copy()\n    new_data['A'] = data['A'].copy()\n    new_data['O'] = data['O'].copy()\n\
    \    new_data['csr'] = CSR(new_data['A'], new_data['O'])\n    return new_data\n\
    \n@benchmark.setup(\"list_of_lists\", [\"heapify\"])\ndef setup_list_of_lists_heapify(data):\n\
    \    \"\"\"Setup function that only copies data for heapify operation\"\"\"\n\
    \    new_data = data.copy()\n    new_data['list_of_lists'] = [row.copy() for row\
    \ in data['list_of_lists']]\n    return new_data\n\n# Initialization operation\n\
    @benchmark.implementation(\"csr\", \"initialization\")\ndef initialization_csr(data):\n\
    \    \"\"\"Initialize CSR from raw row data\"\"\"\n    raw_rows = data['raw_rows']\n\
    \    \n    # Create CSR structure\n    A = []  # All elements concatenated\n \
    \   O = [0]  # Offsets for each row\n    \n    for row_data in raw_rows:\n   \
    \     A.extend(row_data)\n        O.append(len(A))\n    \n    # Create CSR object\n\
    \    csr = CSR(A, O)\n    \n    # Return checksum to ensure it's not optimized\
    \ away\n    checksum = 0\n    for i in range(min(10, len(csr))):  # First 10 rows\n\
    \        row_view = csr[i]\n        for j in range(min(3, len(row_view))):  #\
    \ First 3 elements per row\n            checksum ^= row_view[j]\n    \n    return\
    \ checksum\n\n@benchmark.implementation(\"list_of_lists\", \"initialization\"\
    )\ndef initialization_list_of_lists(data):\n    \"\"\"Initialize list of lists\
    \ from raw row data\"\"\"\n    raw_rows = data['raw_rows']\n    \n    # Create\
    \ list of lists (deep copy)\n    list_of_lists = [row.copy() for row in raw_rows]\n\
    \    \n    # Return checksum to ensure it's not optimized away\n    checksum =\
    \ 0\n    for i in range(min(10, len(list_of_lists))):  # First 10 rows\n     \
    \   row = list_of_lists[i]\n        for j in range(min(3, len(row))):  # First\
    \ 3 elements per row\n            checksum ^= row[j]\n    \n    return checksum\n\
    \n# Bucketize initialization operation\n@benchmark.implementation(\"csr\", \"\
    initialization_bucketize\")\ndef initialization_bucketize_csr(data):\n    \"\"\
    \"Initialize CSR using bucketize from (key, value) pairs\"\"\"\n    keys = data['keys']\n\
    \    values = data['values']\n    num_rows = data['num_rows']\n    \n    # Create\
    \ CSR using bucketize\n    csr = CSR.bucketize(num_rows, keys, values)\n    \n\
    \    # Return checksum to ensure it's not optimized away\n    checksum = 0\n \
    \   for i in range(min(10, len(csr))):  # First 10 rows\n        row_view = csr[i]\n\
    \        for j in range(min(3, len(row_view))):  # First 3 elements per row\n\
    \            checksum ^= row_view[j]\n    \n    return checksum\n\n@benchmark.implementation(\"\
    list_of_lists\", \"initialization_bucketize\")\ndef initialization_bucketize_list_of_lists(data):\n\
    \    \"\"\"Initialize list of lists by grouping (key, value) pairs manually\"\"\
    \"\n    keys = data['keys']\n    values = data['values']\n    num_rows = data['num_rows']\n\
    \    \n    # Group by key manually (simulating what bucketize does)\n    list_of_lists\
    \ = [[] for _ in range(num_rows)]\n    for e, k in enumerate(keys):\n        list_of_lists[k].append(values[e])\n\
    \    \n    # Return checksum to ensure it's not optimized away\n    checksum =\
    \ 0\n    for i in range(min(10, len(list_of_lists))):  # First 10 rows\n     \
    \   row = list_of_lists[i]\n        for j in range(min(3, len(row))):  # First\
    \ 3 elements per row\n            checksum ^= row[j]\n    \n    return checksum\n\
    \n# Heapify operation\n@benchmark.implementation(\"csr\", \"heapify\")\ndef heapify_csr(data):\n\
    \    \"\"\"Heapify all CSR rows\"\"\"\n    csr = data['csr']\n    \n    checksum\
    \ = 0\n    for row_view in csr:\n        heapify(row_view)\n        # Add first\
    \ few elements to checksum\n        for j in range(min(3, len(row_view))):\n \
    \           checksum ^= row_view[j]\n    \n    return checksum\n\n@benchmark.implementation(\"\
    list_of_lists\", \"heapify\")\ndef heapify_list_of_lists(data):\n    \"\"\"Heapify\
    \ all lists in list of lists\"\"\"\n    list_of_lists = data['list_of_lists']\n\
    \    \n    checksum = 0\n    for row in list_of_lists:\n        heapify(row)\n\
    \        # Add first few elements to checksum\n        for j in range(min(3, len(row))):\n\
    \            checksum ^= row[j]\n    \n    return checksum\n\n# Heappop operation\
    \ (heaps are already heapified in setup)\n@benchmark.implementation(\"csr\", \"\
    heappop\")\ndef heappop_csr(data):\n    \"\"\"Pop from CSR heaps\"\"\"\n    csr\
    \ = data['csr']\n    \n    checksum = 0\n    # Pop from multiple rows\n    for\
    \ row_view in csr:\n        pop_count = min(3, len(row_view))  # Pop up to 3 elements\
    \ per row\n        for _ in range(pop_count):\n            if row_view:\n    \
    \            val = heappop(row_view)\n                checksum ^= val\n    \n\
    \    return checksum\n\n@benchmark.implementation(\"list_of_lists\", \"heappop\"\
    )\ndef heappop_list_of_lists(data):\n    \"\"\"Pop from list of lists heaps\"\"\
    \"\n    list_of_lists = data['list_of_lists']\n    \n    checksum = 0\n    # Pop\
    \ from multiple rows\n    for row in list_of_lists:\n        pop_count = min(3,\
    \ len(row))  # Pop up to 3 elements per row\n        for _ in range(pop_count):\n\
    \            if row:\n                val = heappop(row)\n                checksum\
    \ ^= val\n    \n    return checksum\n\n# Heapreplace operation (heaps are already\
    \ heapified in setup)\n@benchmark.implementation(\"csr\", \"heapreplace\")\ndef\
    \ heapreplace_csr(data):\n    \"\"\"Replace in CSR heaps\"\"\"\n    csr = data['csr']\n\
    \    new_value = data['new_value']\n    \n    checksum = 0\n    # Replace in multiple\
    \ rows\n    for row_view in csr:\n        if row_view:\n            replace_count\
    \ = min(2, len(row_view))  # Replace up to 2 elements per row\n            for\
    \ j in range(replace_count):\n                if row_view:\n                 \
    \   val = heapreplace(row_view, new_value + j)\n                    checksum ^=\
    \ val\n    \n    return checksum\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"heapreplace\")\ndef heapreplace_list_of_lists(data):\n    \"\"\"Replace in\
    \ list of lists heaps\"\"\"\n    list_of_lists = data['list_of_lists']\n    new_value\
    \ = data['new_value']\n    \n    checksum = 0\n    # Replace in multiple rows\n\
    \    for row in list_of_lists:\n        if row:\n            replace_count = min(2,\
    \ len(row))  # Replace up to 2 elements per row\n            for j in range(replace_count):\n\
    \                if row:\n                    val = heapreplace(row, new_value\
    \ + j)\n                    checksum ^= val\n    \n    return checksum\n\n# Heappush\
    \ operation (heaps are already heapified in setup)\n@benchmark.implementation(\"\
    csr\", \"heappush\")\ndef heappush_csr(data):\n    \"\"\"Push to CSR heaps\"\"\
    \"\n    csr = data['csr']\n    new_value = data['new_value']\n    \n    checksum\
    \ = 0\n    # Push to multiple rows\n    for i in range(min(5, len(csr))):  # Push\
    \ to first 5 rows\n        row_view = csr[i]\n        # Check if there's space\
    \ to expand (view can grow within A bounds)\n        if row_view.r < len(csr.A):\n\
    \            push_count = min(2, len(csr.A) - row_view.r)  # Push up to 2 elements\
    \ per row\n            for j in range(push_count):\n                val = new_value\
    \ + i * 10 + j\n                heappush(row_view, val)\n                checksum\
    \ ^= val\n    \n    return checksum\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"heappush\")\ndef heappush_list_of_lists(data):\n    \"\"\"Push to list of\
    \ lists heaps\"\"\"\n    list_of_lists = data['list_of_lists']\n    new_value\
    \ = data['new_value']\n    \n    checksum = 0\n    # Push to multiple rows\n \
    \   for i in range(min(5, len(list_of_lists))):  # Push to first 5 rows\n    \
    \    row = list_of_lists[i]\n        push_count = 2  # Push 2 elements per row\n\
    \        for j in range(push_count):\n            val = new_value + i * 10 + j\n\
    \            heappush(row, val)\n            checksum ^= val\n    \n    return\
    \ checksum\n\n# Heappushpop operation (heaps are already heapified in setup)\n\
    @benchmark.implementation(\"csr\", \"heappushpop\")\ndef heappushpop_csr(data):\n\
    \    \"\"\"Push and pop from CSR heaps\"\"\"\n    csr = data['csr']\n    new_value\
    \ = data['new_value']\n    \n    checksum = 0\n    # Pushpop from multiple rows\n\
    \    for i, row_view in enumerate(csr):\n        if row_view:\n            pushpop_count\
    \ = min(2, len(row_view))  # Pushpop up to 2 elements per row\n            for\
    \ j in range(pushpop_count):\n                val = new_value + i * 10 + j\n \
    \               popped = heappushpop(row_view, val)\n                checksum\
    \ ^= popped\n    \n    return checksum\n\n@benchmark.implementation(\"list_of_lists\"\
    , \"heappushpop\")\ndef heappushpop_list_of_lists(data):\n    \"\"\"Push and pop\
    \ from list of lists heaps\"\"\"\n    list_of_lists = data['list_of_lists']\n\
    \    new_value = data['new_value']\n    \n    checksum = 0\n    # Pushpop from\
    \ multiple rows\n    for i, row in enumerate(list_of_lists):\n        if row:\n\
    \            pushpop_count = min(2, len(row))  # Pushpop up to 2 elements per\
    \ row\n            for j in range(pushpop_count):\n                val = new_value\
    \ + i * 10 + j\n                popped = heappushpop(row, val)\n             \
    \   checksum ^= popped\n    \n    return checksum\n\nif __name__ == \"__main__\"\
    :\n    # Parse command line args and run appropriate mode\n    runner = benchmark.parse_args()\n\
    \    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/view/csr_cls.py
  - cp_library/ds/heap/fast_heapq.py
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
  path: perf/heap_csr.py
  requiredBy: []
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/heap_csr.py
layout: document
redirect_from:
- /library/perf/heap_csr.py
- /library/perf/heap_csr.py.html
title: perf/heap_csr.py
---
