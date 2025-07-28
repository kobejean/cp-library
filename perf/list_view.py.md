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
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing operations on list slices\
    \ vs view objects.\nTests various operations to measure the overhead of slice\
    \ copying vs view indirection.\n\"\"\"\n\nimport random\nimport sys\nimport os\n\
    \nfrom cp_library.ds.heap.fast_heapq import heapify, heappop, heapreplace, heappush,\
    \ heappushpop\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig\nfrom cp_library.ds.view.view_cls\
    \ import view\n\n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"\
    list_view\",\n    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order\
    \ to warm up JIT\n    operations=['construction', 'sum', 'modify', 'index', 'reverse',\
    \ 'sort', 'nested_sum', 'pop', 'append'],\n    iterations=10,\n    warmup=3,\n\
    \    output_dir=\"./output/benchmark_results/list_view\"\n)\n\n# Create benchmark\
    \ instance\nbenchmark = Benchmark(config)\n\n# Data generator\n@benchmark.data_generator(\"\
    default\")\ndef generate_view_data(size: int, operation: str):\n    \"\"\"Generate\
    \ test data for slice/view operations\"\"\"\n    # Generate random list\n    data\
    \ = [random.randint(0, 1000000) for _ in range(size)]\n    \n    # Generate random\
    \ slice boundaries (10-50% of list)\n    slice_size = random.randint(size // 10,\
    \ size // 2)\n    start = random.randint(0, size - slice_size)\n    end = start\
    \ + slice_size\n    \n    return {\n        'data': data,\n        'start': start,\n\
    \        'end': end,\n        'slice_size': slice_size,\n        'search_value':\
    \ random.randint(0, 1000000),\n        'size': size,\n        'operation': operation\n\
    \    }\n\n# Construction operation\n@benchmark.implementation(\"slice\", \"construction\"\
    )\ndef construction_slice(data):\n    \"\"\"Create a slice copy of the list\"\"\
    \"\n    lst = data['data']\n    start, end = data['start'], data['end']\n    \n\
    \    # Create slice (copies data)\n    slice_copy = lst[start:end]\n    \n   \
    \ # Return checksum to ensure it's not optimized away\n    checksum = 0\n    for\
    \ x in slice_copy:\n        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"\
    view\", \"construction\")\ndef construction_view(data):\n    \"\"\"Create a view\
    \ of the list\"\"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n\
    \    \n    # Create view (no copy)\n    list_view = view(lst, start, end)\n  \
    \  \n    # Return checksum to ensure it's not optimized away\n    checksum = 0\n\
    \    for i in range(len(list_view)):\n        checksum ^= list_view[i]\n    return\
    \ checksum\n\n# Sum operation\n@benchmark.implementation(\"slice\", \"sum\")\n\
    def sum_slice(data):\n    \"\"\"Sum elements in a slice\"\"\"\n    lst = data['data']\n\
    \    start, end = data['start'], data['end']\n    \n    # Create slice and sum\n\
    \    slice_copy = lst[start:end]\n    return sum(slice_copy) & 0xFFFFFFFF  # Keep\
    \ as 32-bit for checksum\n\n@benchmark.implementation(\"view\", \"sum\")\ndef\
    \ sum_view(data):\n    \"\"\"Sum elements in a view\"\"\"\n    lst = data['data']\n\
    \    start, end = data['start'], data['end']\n    \n    # Create view and sum\
    \ through it\n    list_view = view(lst, start, end)\n    total = 0\n    for i\
    \ in range(len(list_view)):\n        total += list_view[i]\n    return total &\
    \ 0xFFFFFFFF  # Keep as 32-bit for checksum\n\n@benchmark.implementation(\"view_direct\"\
    , \"sum\")\ndef sum_view_direct(data):\n    \"\"\"Sum elements using direct indexing\"\
    \"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n  \
    \  \n    # Sum directly without creating slice or view\n    total = 0\n    for\
    \ i in range(start, end):\n        total += lst[i]\n    return total & 0xFFFFFFFF\
    \  # Keep as 32-bit for checksum\n\n# Setup functions for operations that need\
    \ copying\n@benchmark.setup(\"slice\", [\"modify\", \"reverse\", \"sort\", \"\
    pop\", \"append\"])\ndef setup_slice_modify(data):\n    \"\"\"Setup function that\
    \ copies data before modification\"\"\"\n    new_data = data.copy()\n    new_data['data']\
    \ = data['data'].copy()\n    return new_data\n\n@benchmark.setup(\"view\", [\"\
    modify\", \"reverse\", \"sort\", \"pop\", \"append\"])\ndef setup_view_modify(data):\n\
    \    \"\"\"Setup function that copies data before modification\"\"\"\n    new_data\
    \ = data.copy()\n    new_data['data'] = data['data'].copy()\n    return new_data\n\
    \n@benchmark.setup(\"view_direct\", [\"modify\", \"reverse\", \"sort\", \"pop\"\
    , \"append\"])\ndef setup_view_direct_modify(data):\n    \"\"\"Setup function\
    \ that copies data before modification\"\"\"\n    new_data = data.copy()\n   \
    \ new_data['data'] = data['data'].copy()\n    return new_data\n\n# Modify operation\n\
    @benchmark.implementation(\"slice\", \"modify\")\ndef modify_slice(data):\n  \
    \  \"\"\"Modify elements in a slice\"\"\"\n    lst = data['data']\n    start,\
    \ end = data['start'], data['end']\n    \n    # Create slice and modify\n    slice_copy\
    \ = lst[start:end]\n    for i in range(len(slice_copy)):\n        slice_copy[i]\
    \ = (slice_copy[i] * 2) & 0xFFFFFFFF\n    \n    # Copy back to original positions\
    \ manually\n    for i, val in enumerate(slice_copy):\n        lst[start + i] =\
    \ val\n    \n    # Return checksum\n    checksum = 0\n    for i in range(start,\
    \ end):\n        checksum ^= lst[i]\n    return checksum\n\n@benchmark.implementation(\"\
    view\", \"modify\")\ndef modify_view(data):\n    \"\"\"Modify elements through\
    \ a view\"\"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n\
    \    \n    # Create view and modify through it\n    list_view = view(lst, start,\
    \ end)\n    for i in range(len(list_view)):\n        list_view[i] = (list_view[i]\
    \ * 2) & 0xFFFFFFFF\n    \n    # Return checksum\n    checksum = 0\n    for i\
    \ in range(start, end):\n        checksum ^= lst[i]\n    return checksum\n\n@benchmark.implementation(\"\
    view_direct\", \"modify\")\ndef modify_view_direct(data):\n    \"\"\"Modify elements\
    \ using direct indexing\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    # Modify directly\n    for i in range(start, end):\n\
    \        lst[i] = (lst[i] * 2) & 0xFFFFFFFF\n    \n    # Return checksum\n   \
    \ checksum = 0\n    for i in range(start, end):\n        checksum ^= lst[i]\n\
    \    return checksum\n\n# Index operation\n@benchmark.implementation(\"slice\"\
    , \"index\")\ndef index_slice(data):\n    \"\"\"Find index of element in a slice\"\
    \"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n  \
    \  search_value = data['search_value']\n    \n    # Create slice and search\n\
    \    slice_copy = lst[start:end]\n    try:\n        idx = slice_copy.index(search_value)\n\
    \        return start + idx  # Return global index\n    except ValueError:\n \
    \       return -1\n\n@benchmark.implementation(\"view\", \"index\")\ndef index_view(data):\n\
    \    \"\"\"Find index of element in a view\"\"\"\n    lst = data['data']\n   \
    \ start, end = data['start'], data['end']\n    search_value = data['search_value']\n\
    \    \n    # Create view and search in it\n    list_view = view(lst, start, end)\n\
    \    try:\n        idx = list_view.index(search_value)\n        return start +\
    \ idx  # Return global index\n    except ValueError:\n        return -1\n\n@benchmark.implementation(\"\
    view_direct\", \"index\")\ndef index_view_direct(data):\n    \"\"\"Find index\
    \ of element using direct search\"\"\"\n    lst = data['data']\n    start, end\
    \ = data['start'], data['end']\n    search_value = data['search_value']\n    \n\
    \    # Search directly\n    for i in range(start, end):\n        if lst[i] ==\
    \ search_value:\n            return i\n    return -1\n\n# Reverse operation\n\
    @benchmark.implementation(\"slice\", \"reverse\")\ndef reverse_slice(data):\n\
    \    \"\"\"Reverse a slice\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    # Create slice, reverse, and copy back manually\n   \
    \ slice_copy = lst[start:end]\n    slice_copy.reverse()\n    for i, val in enumerate(slice_copy):\n\
    \        lst[start + i] = val\n    \n    # Return checksum\n    checksum = 0\n\
    \    for i in range(start, min(start + 100, end)):  # First 100 elements\n   \
    \     checksum ^= lst[i]\n    return checksum\n\n@benchmark.implementation(\"\
    view\", \"reverse\")\ndef reverse_view(data):\n    \"\"\"Reverse through a view\"\
    \"\"\n    lst = data['data']\n    start, end = data['start'], data['end']\n  \
    \  \n    # Create view and reverse through it\n    list_view = view(lst, start,\
    \ end)\n    list_view.reverse()\n    \n    # Return checksum\n    checksum = 0\n\
    \    for i in range(start, min(start + 100, end)):  # First 100 elements\n   \
    \     checksum ^= lst[i]\n    return checksum\n\n@benchmark.implementation(\"\
    view_direct\", \"reverse\")\ndef reverse_view_direct(data):\n    \"\"\"Reverse\
    \ using direct manipulation\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    # Reverse directly\n    left, right = start, end - 1\n\
    \    while left < right:\n        lst[left], lst[right] = lst[right], lst[left]\n\
    \        left += 1\n        right -= 1\n    \n    # Return checksum\n    checksum\
    \ = 0\n    for i in range(start, min(start + 100, end)):  # First 100 elements\n\
    \        checksum ^= lst[i]\n    return checksum\n\n# Sort operation\n@benchmark.implementation(\"\
    slice\", \"sort\")\ndef sort_slice(data):\n    \"\"\"Sort a slice\"\"\"\n    lst\
    \ = data['data']\n    start, end = data['start'], data['end']\n    \n    # Create\
    \ slice, sort, and copy back manually\n    slice_copy = lst[start:end]\n    slice_copy.sort()\n\
    \    for i, val in enumerate(slice_copy):\n        lst[start + i] = val\n    \n\
    \    # Return checksum of first elements\n    checksum = 0\n    for i in range(start,\
    \ min(start + 100, end)):\n        checksum ^= lst[i]\n    return checksum\n\n\
    @benchmark.implementation(\"view\", \"sort\")\ndef sort_view(data):\n    \"\"\"\
    Sort through a view\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    # Create view and sort through it\n    list_view = view(lst,\
    \ start, end)\n    list_view.sort()\n    \n    # Return checksum of first elements\n\
    \    checksum = 0\n    for i in range(start, min(start + 100, end)):\n       \
    \ checksum ^= lst[i]\n    return checksum\n\n# Nested sum operation (multiple\
    \ slices)\n@benchmark.implementation(\"slice\", \"nested_sum\")\ndef nested_sum_slice(data):\n\
    \    \"\"\"Sum multiple overlapping slices\"\"\"\n    lst = data['data']\n   \
    \ start, end = data['start'], data['end']\n    slice_size = (end - start) // 4\n\
    \    \n    total = 0\n    # Create 4 overlapping slices\n    for offset in range(4):\n\
    \        s = start + offset * slice_size // 2\n        e = min(s + slice_size,\
    \ end)\n        slice_copy = lst[s:e]\n        total += sum(slice_copy)\n    \n\
    \    return total & 0xFFFFFFFF\n\n@benchmark.implementation(\"view\", \"nested_sum\"\
    )\ndef nested_sum_view(data):\n    \"\"\"Sum multiple overlapping views\"\"\"\n\
    \    lst = data['data']\n    start, end = data['start'], data['end']\n    slice_size\
    \ = (end - start) // 4\n    \n    total = 0\n    # Create 4 overlapping views\n\
    \    for offset in range(4):\n        s = start + offset * slice_size // 2\n \
    \       e = min(s + slice_size, end)\n        list_view = view(lst, s, e)\n  \
    \      for i in range(len(list_view)):\n            total += list_view[i]\n  \
    \  \n    return total & 0xFFFFFFFF\n\n@benchmark.implementation(\"view_direct\"\
    , \"nested_sum\")\ndef nested_sum_view_direct(data):\n    \"\"\"Sum multiple overlapping\
    \ ranges directly\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    slice_size = (end - start) // 4\n    \n    total = 0\n    #\
    \ Sum 4 overlapping ranges\n    for offset in range(4):\n        s = start + offset\
    \ * slice_size // 2\n        e = min(s + slice_size, end)\n        for i in range(s,\
    \ e):\n            total += lst[i]\n    \n    return total & 0xFFFFFFFF\n\n# Pop\
    \ operation\n@benchmark.implementation(\"slice\", \"pop\")\ndef pop_slice(data):\n\
    \    \"\"\"Pop from end of slice\"\"\"\n    lst = data['data']\n    start, end\
    \ = data['start'], data['end']\n    \n    # Create slice and pop from it\n   \
    \ slice_copy = lst[start:end]\n    checksum = 0\n    for _ in range(min(100, len(slice_copy))):\
    \  # Pop up to 100 elements\n        if slice_copy:\n            val = slice_copy.pop()\n\
    \            checksum ^= val\n    \n    # Copy back to original (shortened)\n\
    \    for i, val in enumerate(slice_copy):\n        lst[start + i] = val\n    \n\
    \    return checksum\n\n@benchmark.implementation(\"view\", \"pop\")\ndef pop_view(data):\n\
    \    \"\"\"Pop from end of view\"\"\"\n    lst = data['data']\n    start, end\
    \ = data['start'], data['end']\n    \n    # Create view and pop from it\n    list_view\
    \ = view(lst, start, end)\n    checksum = 0\n    for _ in range(min(100, len(list_view))):\
    \  # Pop up to 100 elements\n        if len(list_view) > 0:\n            val =\
    \ list_view.pop()\n            checksum ^= val\n    \n    return checksum\n\n\
    @benchmark.implementation(\"view_direct\", \"pop\")\ndef pop_view_direct(data):\n\
    \    \"\"\"Pop using direct list manipulation\"\"\"\n    lst = data['data']\n\
    \    start, end = data['start'], data['end']\n    \n    checksum = 0\n    current_end\
    \ = end\n    for _ in range(min(100, end - start)):  # Pop up to 100 elements\n\
    \        if current_end > start:\n            current_end -= 1\n            val\
    \ = lst[current_end]\n            checksum ^= val\n    \n    return checksum\n\
    \n# Append operation\n@benchmark.implementation(\"slice\", \"append\")\ndef append_slice(data):\n\
    \    \"\"\"Append to slice\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    # Create slice and append to it\n    slice_copy = lst[start:end]\n\
    \    checksum = 0\n    for i in range(100):  # Append 100 elements\n        val\
    \ = (i * 17) & 0xFFFFFFFF\n        slice_copy.append(val)\n        checksum ^=\
    \ val\n    \n    # Note: Can't copy back easily since slice grew, so just return\
    \ checksum\n    return checksum\n\n@benchmark.implementation(\"view\", \"append\"\
    )\ndef append_view(data):\n    \"\"\"Append to view\"\"\"\n    lst = data['data']\n\
    \    start, end = data['start'], data['end']\n    \n    # Create view and append\
    \ to it\n    list_view = view(lst, start, end)\n    checksum = 0\n    for i in\
    \ range(min(100, len(lst) - end)):  # Append up to 100 elements or space available\n\
    \        val = (i * 17) & 0xFFFFFFFF\n        list_view.append(val)\n        checksum\
    \ ^= val\n    \n    return checksum\n\n@benchmark.implementation(\"view_direct\"\
    , \"append\")\ndef append_view_direct(data):\n    \"\"\"Append using direct list\
    \ manipulation\"\"\"\n    lst = data['data']\n    start, end = data['start'],\
    \ data['end']\n    \n    checksum = 0\n    current_end = end\n    for i in range(min(100,\
    \ len(lst) - end)):  # Append up to 100 elements or space available\n        val\
    \ = (i * 17) & 0xFFFFFFFF\n        if current_end < len(lst):\n            lst[current_end]\
    \ = val\n            current_end += 1\n            checksum ^= val\n    \n   \
    \ return checksum\n\nif __name__ == \"__main__\":\n    # Parse command line args\
    \ and run appropriate mode\n    runner = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/perf/benchmark.py
  - cp_library/ds/view/view_cls.py
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
  path: perf/list_view.py
  requiredBy: []
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/list_view.py
layout: document
redirect_from:
- /library/perf/list_view.py
- /library/perf/list_view.py.html
title: perf/list_view.py
---
