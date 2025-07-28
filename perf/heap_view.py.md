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
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing heap operations on list\
    \ slices vs view objects vs direct indexing.\nTests heapify, heappop, heapreplace,\
    \ heappush, heappushpop operations.\n\"\"\"\n\nimport random\nimport sys\nimport\
    \ os\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig\nfrom cp_library.ds.view.view_cls\
    \ import view\nfrom cp_library.ds.heap.fast_heapq import heapify, heappop, heapreplace,\
    \ heappush, heappushpop\nimport heapq  # Standard library for comparison\n\n#\
    \ Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"heap_view\",\n  \
    \  sizes=[100000, 10000, 1000, 100, 50],  # Reverse order to warm up JIT\n   \
    \ operations=['heapify', 'heappop', 'heapreplace', 'heappush', 'heappushpop'],\n\
    \    iterations=10,\n    warmup=3,\n    output_dir=\"./output/benchmark_results/heap_view\"\
    \n)\n\n# Create benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\n\
    @benchmark.data_generator(\"default\")\ndef generate_heap_data(size: int, operation:\
    \ str):\n    \"\"\"Generate test data for heap operations\"\"\"\n    # Generate\
    \ random list for heap operations\n    data = [random.randint(1, 1000000) for\
    \ _ in range(size)]\n    \n    # Generate random slice boundaries (30-70% of list\
    \ for reasonable heap size)\n    slice_size = random.randint(size // 3, min(size\
    \ * 2 // 3, size - 1))\n    start = random.randint(0, size - slice_size)\n   \
    \ end = start + slice_size\n    \n    return {\n        'data': data,\n      \
    \  'start': start,\n        'end': end,\n        'slice_size': slice_size,\n \
    \       'new_value': random.randint(1, 1000000),\n        'replace_value': random.randint(1,\
    \ 1000000),\n        'size': size,\n        'operation': operation\n    }\n\n\
    # Setup functions for operations that modify data\n@benchmark.setup(\"slice\"\
    , [\"heappop\", \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef setup_slice_heap(data):\n\
    \    \"\"\"Setup function that copies data and heapifies before heap operations\"\
    \"\"\n    new_data = data.copy()\n    new_data['data'] = data['data'].copy()\n\
    \    \n    # Pre-heapify the slice for operations that need it\n    lst = new_data['data']\n\
    \    start, end = new_data['start'], new_data['end']\n    slice_copy = lst[start:end]\n\
    \    heapify(slice_copy)\n    for i, val in enumerate(slice_copy):\n        lst[start\
    \ + i] = val\n    \n    return new_data\n\n@benchmark.setup(\"view\", [\"heappop\"\
    , \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef setup_view_heap(data):\n\
    \    \"\"\"Setup function that copies data and heapifies before heap operations\"\
    \"\"\n    new_data = data.copy()\n    new_data['data'] = data['data'].copy()\n\
    \    \n    # Pre-heapify the view for operations that need it\n    lst = new_data['data']\n\
    \    start, end = new_data['start'], new_data['end']\n    heap_view = view(lst,\
    \ start, end)\n    heapify(heap_view)\n    \n    return new_data\n\n@benchmark.setup(\"\
    direct\", [\"heappop\", \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef\
    \ setup_direct_heap(data):\n    \"\"\"Setup function that copies data and heapifies\
    \ before heap operations\"\"\"\n    new_data = data.copy()\n    new_data['data']\
    \ = data['data'].copy()\n    \n    # Pre-heapify the range for operations that\
    \ need it\n    lst = new_data['data']\n    start, end = new_data['start'], new_data['end']\n\
    \    temp_list = lst[start:end]\n    heapify(temp_list)\n    for i, val in enumerate(temp_list):\n\
    \        lst[start + i] = val\n    \n    return new_data\n\n@benchmark.setup(\"\
    stdlib\", [\"heappop\", \"heapreplace\", \"heappush\", \"heappushpop\"])\ndef\
    \ setup_stdlib_heap(data):\n    \"\"\"Setup function that copies data and heapifies\
    \ before heap operations\"\"\"\n    new_data = data.copy()\n    new_data['data']\
    \ = data['data'].copy()\n    \n    # Pre-heapify the slice for operations that\
    \ need it\n    lst = new_data['data']\n    start, end = new_data['start'], new_data['end']\n\
    \    slice_copy = lst[start:end]\n    heapq.heapify(slice_copy)\n    for i, val\
    \ in enumerate(slice_copy):\n        lst[start + i] = val\n    \n    return new_data\n\
    \n# For heapify operation, we need setup without pre-heapifying\n@benchmark.setup(\"\
    slice\", [\"heapify\"])\ndef setup_slice_heapify(data):\n    \"\"\"Setup function\
    \ that only copies data for heapify operation\"\"\"\n    new_data = data.copy()\n\
    \    new_data['data'] = data['data'].copy()\n    return new_data\n\n@benchmark.setup(\"\
    view\", [\"heapify\"])\ndef setup_view_heapify(data):\n    \"\"\"Setup function\
    \ that only copies data for heapify operation\"\"\"\n    new_data = data.copy()\n\
    \    new_data['data'] = data['data'].copy()\n    return new_data\n\n@benchmark.setup(\"\
    direct\", [\"heapify\"])\ndef setup_direct_heapify(data):\n    \"\"\"Setup function\
    \ that only copies data for heapify operation\"\"\"\n    new_data = data.copy()\n\
    \    new_data['data'] = data['data'].copy()\n    return new_data\n\n@benchmark.setup(\"\
    stdlib\", [\"heapify\"])\ndef setup_stdlib_heapify(data):\n    \"\"\"Setup function\
    \ that only copies data for heapify operation\"\"\"\n    new_data = data.copy()\n\
    \    new_data['data'] = data['data'].copy()\n    return new_data\n\n# Heapify\
    \ operation\n@benchmark.implementation(\"slice\", \"heapify\")\ndef heapify_slice(data):\n\
    \    \"\"\"Heapify a slice\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    # Create slice and heapify\n    slice_copy = lst[start:end]\n\
    \    heapify(slice_copy)\n    \n    # Copy back manually\n    for i, val in enumerate(slice_copy):\n\
    \        lst[start + i] = val\n    \n    # Return checksum\n    checksum = 0\n\
    \    for i in range(start, min(start + 10, end)):  # First 10 elements\n     \
    \   checksum ^= lst[i]\n    return checksum\n\n@benchmark.implementation(\"view\"\
    , \"heapify\")\ndef heapify_view(data):\n    \"\"\"Heapify through a view\"\"\"\
    \n    lst = data['data']\n    start, end = data['start'], data['end']\n    \n\
    \    # Create view and heapify\n    heap_view = view(lst, start, end)\n    heapify(heap_view)\n\
    \    \n    # Return checksum\n    checksum = 0\n    for i in range(start, min(start\
    \ + 10, end)):  # First 10 elements\n        checksum ^= lst[i]\n    return checksum\n\
    \n@benchmark.implementation(\"direct\", \"heapify\")\ndef heapify_direct(data):\n\
    \    \"\"\"Heapify using direct list access\"\"\"\n    lst = data['data']\n  \
    \  start, end = data['start'], data['end']\n    \n    # Heapify the range directly\
    \ in the list\n    temp_list = lst[start:end]\n    heapify(temp_list)\n    for\
    \ i, val in enumerate(temp_list):\n        lst[start + i] = val\n    \n    # Return\
    \ checksum\n    checksum = 0\n    for i in range(start, min(start + 10, end)):\
    \  # First 10 elements\n        checksum ^= lst[i]\n    return checksum\n\n@benchmark.implementation(\"\
    stdlib\", \"heapify\")\ndef heapify_stdlib(data):\n    \"\"\"Heapify using standard\
    \ library\"\"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n\
    \    \n    # Create slice and heapify with stdlib\n    slice_copy = lst[start:end]\n\
    \    heapq.heapify(slice_copy)\n    \n    # Copy back manually\n    for i, val\
    \ in enumerate(slice_copy):\n        lst[start + i] = val\n    \n    # Return\
    \ checksum\n    checksum = 0\n    for i in range(start, min(start + 10, end)):\
    \  # First 10 elements\n        checksum ^= lst[i]\n    return checksum\n\n# Heappop\
    \ operation (heap is already heapified in setup)\n@benchmark.implementation(\"\
    slice\", \"heappop\")\ndef heappop_slice(data):\n    \"\"\"Pop from heap slice\"\
    \"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n  \
    \  \n    # Create slice and pop (already heapified)\n    slice_copy = lst[start:end]\n\
    \    \n    checksum = 0\n    for _ in range(min(10, len(slice_copy))):  # Pop\
    \ up to 10 elements\n        if slice_copy:\n            val = heappop(slice_copy)\n\
    \            checksum ^= val\n    \n    # Copy back\n    for i, val in enumerate(slice_copy):\n\
    \        lst[start + i] = val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    view\", \"heappop\")\ndef heappop_view(data):\n    \"\"\"Pop from heap view\"\"\
    \"\n    lst = data['data']\n    start, end = data['start'], data['end']\n    \n\
    \    # Create view and pop (already heapified)\n    heap_view = view(lst, start,\
    \ end)\n    \n    checksum = 0\n    for _ in range(min(10, len(heap_view))): \
    \ # Pop up to 10 elements\n        if len(heap_view) > 0:\n            val = heappop(heap_view)\n\
    \            checksum ^= val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    direct\", \"heappop\")\ndef heappop_direct(data):\n    \"\"\"Pop from heap using\
    \ direct access\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    # Pop from range (already heapified)\n    temp_list =\
    \ lst[start:end]\n    \n    checksum = 0\n    for _ in range(min(10, len(temp_list))):\
    \  # Pop up to 10 elements\n        if temp_list:\n            val = heappop(temp_list)\n\
    \            checksum ^= val\n    \n    # Copy back\n    for i, val in enumerate(temp_list):\n\
    \        lst[start + i] = val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    stdlib\", \"heappop\")\ndef heappop_stdlib(data):\n    \"\"\"Pop from heap using\
    \ standard library\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    # Create slice and pop with stdlib (already heapified)\n\
    \    slice_copy = lst[start:end]\n    \n    checksum = 0\n    for _ in range(min(10,\
    \ len(slice_copy))):  # Pop up to 10 elements\n        if slice_copy:\n      \
    \      val = heapq.heappop(slice_copy)\n            checksum ^= val\n    \n  \
    \  # Copy back\n    for i, val in enumerate(slice_copy):\n        lst[start +\
    \ i] = val\n    \n    return checksum\n\n# Heapreplace operation (heap is already\
    \ heapified in setup)\n@benchmark.implementation(\"slice\", \"heapreplace\")\n\
    def heapreplace_slice(data):\n    \"\"\"Replace in heap slice\"\"\"\n    lst =\
    \ data['data']\n    start, end = data['start'], data['end']\n    new_value = data['new_value']\n\
    \    \n    # Create slice and replace (already heapified)\n    slice_copy = lst[start:end]\n\
    \    if slice_copy:\n        checksum = 0\n        for _ in range(min(5, len(slice_copy))):\
    \  # Replace up to 5 elements\n            if slice_copy:\n                val\
    \ = heapreplace(slice_copy, new_value)\n                checksum ^= val\n    \
    \            new_value = (new_value + 1) & 0xFFFFFFFF\n        \n        # Copy\
    \ back\n        for i, val in enumerate(slice_copy):\n            lst[start +\
    \ i] = val\n        \n        return checksum\n    return 0\n\n@benchmark.implementation(\"\
    view\", \"heapreplace\")\ndef heapreplace_view(data):\n    \"\"\"Replace in heap\
    \ view\"\"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n\
    \    new_value = data['new_value']\n    \n    # Create view and replace (already\
    \ heapified)\n    heap_view = view(lst, start, end)\n    if len(heap_view) > 0:\n\
    \        checksum = 0\n        for _ in range(min(5, len(heap_view))):  # Replace\
    \ up to 5 elements\n            if len(heap_view) > 0:\n                val =\
    \ heapreplace(heap_view, new_value)\n                checksum ^= val\n       \
    \         new_value = (new_value + 1) & 0xFFFFFFFF\n        \n        return checksum\n\
    \    return 0\n\n@benchmark.implementation(\"direct\", \"heapreplace\")\ndef heapreplace_direct(data):\n\
    \    \"\"\"Replace in heap using direct access\"\"\"\n    lst = data['data']\n\
    \    start, end = data['start'], data['end']\n    new_value = data['new_value']\n\
    \    \n    # Replace from range (already heapified)\n    temp_list = lst[start:end]\n\
    \    if temp_list:\n        checksum = 0\n        for _ in range(min(5, len(temp_list))):\
    \  # Replace up to 5 elements\n            if temp_list:\n                val\
    \ = heapreplace(temp_list, new_value)\n                checksum ^= val\n     \
    \           new_value = (new_value + 1) & 0xFFFFFFFF\n        \n        # Copy\
    \ back\n        for i, val in enumerate(temp_list):\n            lst[start + i]\
    \ = val\n        \n        return checksum\n    return 0\n\n@benchmark.implementation(\"\
    stdlib\", \"heapreplace\")\ndef heapreplace_stdlib(data):\n    \"\"\"Replace in\
    \ heap using standard library\"\"\"\n    lst = data['data']\n    start, end =\
    \ data['start'], data['end']\n    new_value = data['new_value']\n    \n    # Create\
    \ slice and replace with stdlib (already heapified)\n    slice_copy = lst[start:end]\n\
    \    if slice_copy:\n        checksum = 0\n        for _ in range(min(5, len(slice_copy))):\
    \  # Replace up to 5 elements\n            if slice_copy:\n                val\
    \ = heapq.heapreplace(slice_copy, new_value)\n                checksum ^= val\n\
    \                new_value = (new_value + 1) & 0xFFFFFFFF\n        \n        #\
    \ Copy back\n        for i, val in enumerate(slice_copy):\n            lst[start\
    \ + i] = val\n        \n        return checksum\n    return 0\n\n# Heappush operation\
    \ (heap is already heapified in setup)\n@benchmark.implementation(\"slice\", \"\
    heappush\")\ndef heappush_slice(data):\n    \"\"\"Push to heap slice\"\"\"\n \
    \   lst = data['data']\n    start, end = data['start'], data['end']\n    new_value\
    \ = data['new_value']\n    \n    # Create slice and push (already heapified)\n\
    \    slice_copy = lst[start:end]\n    \n    checksum = 0\n    for i in range(5):\
    \  # Push 5 elements\n        val = (new_value + i) & 0xFFFFFFFF\n        heappush(slice_copy,\
    \ val)\n        checksum ^= val\n    \n    # Note: Can't copy back easily since\
    \ slice grew, just return checksum\n    return checksum\n\n@benchmark.implementation(\"\
    view\", \"heappush\")\ndef heappush_view(data):\n    \"\"\"Push to heap view\"\
    \"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n  \
    \  new_value = data['new_value']\n    \n    # Create view and push (already heapified)\n\
    \    heap_view = view(lst, start, end)\n    \n    checksum = 0\n    max_push =\
    \ min(5, len(lst) - end)  # Limited by available space\n    for i in range(max_push):\n\
    \        val = (new_value + i) & 0xFFFFFFFF\n        heappush(heap_view, val)\n\
    \        checksum ^= val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    direct\", \"heappush\")\ndef heappush_direct(data):\n    \"\"\"Push to heap using\
    \ direct access\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    new_value = data['new_value']\n    \n    # Push to range (already\
    \ heapified)\n    temp_list = lst[start:end]\n    \n    checksum = 0\n    for\
    \ i in range(5):  # Push 5 elements\n        val = (new_value + i) & 0xFFFFFFFF\n\
    \        heappush(temp_list, val)\n        checksum ^= val\n    \n    # Note:\
    \ Can't copy back easily since temp_list grew, just return checksum\n    return\
    \ checksum\n\n@benchmark.implementation(\"stdlib\", \"heappush\")\ndef heappush_stdlib(data):\n\
    \    \"\"\"Push to heap using standard library\"\"\"\n    lst = data['data']\n\
    \    start, end = data['start'], data['end']\n    new_value = data['new_value']\n\
    \    \n    # Create slice and push with stdlib (already heapified)\n    slice_copy\
    \ = lst[start:end]\n    \n    checksum = 0\n    for i in range(5):  # Push 5 elements\n\
    \        val = (new_value + i) & 0xFFFFFFFF\n        heapq.heappush(slice_copy,\
    \ val)\n        checksum ^= val\n    \n    # Note: Can't copy back easily since\
    \ slice grew, just return checksum\n    return checksum\n\n# Heappushpop operation\
    \ (heap is already heapified in setup)\n@benchmark.implementation(\"slice\", \"\
    heappushpop\")\ndef heappushpop_slice(data):\n    \"\"\"Push and pop from heap\
    \ slice\"\"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n\
    \    new_value = data['new_value']\n    \n    # Create slice and pushpop (already\
    \ heapified)\n    slice_copy = lst[start:end]\n    if slice_copy:\n        checksum\
    \ = 0\n        for i in range(min(5, len(slice_copy))):  # Pushpop up to 5 elements\n\
    \            val = (new_value + i) & 0xFFFFFFFF\n            popped = heappushpop(slice_copy,\
    \ val)\n            checksum ^= popped\n        \n        # Copy back\n      \
    \  for i, val in enumerate(slice_copy):\n            lst[start + i] = val\n  \
    \      \n        return checksum\n    return 0\n\n@benchmark.implementation(\"\
    view\", \"heappushpop\")\ndef heappushpop_view(data):\n    \"\"\"Push and pop\
    \ from heap view\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    new_value = data['new_value']\n    \n    # Create view and\
    \ pushpop (already heapified)\n    heap_view = view(lst, start, end)\n    if len(heap_view)\
    \ > 0:\n        checksum = 0\n        for i in range(min(5, len(heap_view))):\
    \  # Pushpop up to 5 elements\n            val = (new_value + i) & 0xFFFFFFFF\n\
    \            popped = heappushpop(heap_view, val)\n            checksum ^= popped\n\
    \        \n        return checksum\n    return 0\n\n@benchmark.implementation(\"\
    direct\", \"heappushpop\")\ndef heappushpop_direct(data):\n    \"\"\"Push and\
    \ pop from heap using direct access\"\"\"\n    lst = data['data']\n    start,\
    \ end = data['start'], data['end']\n    new_value = data['new_value']\n    \n\
    \    # Pushpop from range (already heapified)\n    temp_list = lst[start:end]\n\
    \    if temp_list:\n        checksum = 0\n        for i in range(min(5, len(temp_list))):\
    \  # Pushpop up to 5 elements\n            val = (new_value + i) & 0xFFFFFFFF\n\
    \            popped = heappushpop(temp_list, val)\n            checksum ^= popped\n\
    \        \n        # Copy back\n        for i, val in enumerate(temp_list):\n\
    \            lst[start + i] = val\n        \n        return checksum\n    return\
    \ 0\n\n@benchmark.implementation(\"stdlib\", \"heappushpop\")\ndef heappushpop_stdlib(data):\n\
    \    \"\"\"Push and pop from heap using standard library\"\"\"\n    lst = data['data']\n\
    \    start, end = data['start'], data['end']\n    new_value = data['new_value']\n\
    \    \n    # Create slice and pushpop with stdlib (already heapified)\n    slice_copy\
    \ = lst[start:end]\n    if slice_copy:\n        checksum = 0\n        for i in\
    \ range(min(5, len(slice_copy))):  # Pushpop up to 5 elements\n            val\
    \ = (new_value + i) & 0xFFFFFFFF\n            popped = heapq.heappushpop(slice_copy,\
    \ val)\n            checksum ^= popped\n        \n        # Copy back\n      \
    \  for i, val in enumerate(slice_copy):\n            lst[start + i] = val\n  \
    \      \n        return checksum\n    return 0\n\nif __name__ == \"__main__\"\
    :\n    # Parse command line args and run appropriate mode\n    runner = benchmark.parse_args()\n\
    \    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/view/view_cls.py
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/ds/list/list_find_fn.py
  - cp_library/perf/checksum.py
  isVerificationFile: false
  path: perf/heap_view.py
  requiredBy: []
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/heap_view.py
layout: document
redirect_from:
- /library/perf/heap_view.py
- /library/perf/heap_view.py.html
title: perf/heap_view.py
---
