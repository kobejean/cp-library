---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnt32_fn.py
    title: cp_library/bit/popcnt32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u32f_fn.py
    title: cp_library/ds/array/u32f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/bit_array_cls.py
    title: cp_library/ds/wavelet/bit_array_cls.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nSimple boolean list benchmark using the new\
    \ declarative framework.\nCompares different boolean data structures and operations.\n\
    \"\"\"\n\nimport random\nimport array\nimport sys\nimport os\nsys.path.insert(0,\
    \ os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig\n\n# Import optional dependencies\ntry:\n\
    \    import bitarray\n    HAS_BITARRAY = True\nexcept ImportError:\n    HAS_BITARRAY\
    \ = False\n\ntry:\n    from cp_library.ds.wavelet.bit_array_cls import BitArray\n\
    \    HAS_CUSTOM_BITARRAY = True\nexcept ImportError:\n    HAS_CUSTOM_BITARRAY\
    \ = False\n\n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"bool_list\"\
    ,\n    sizes=[1000000, 100000, 10000, 1000, 100, 10, 1],  # Reverse order to warm\
    \ up JIT\n    operations=['construction', 'access', 'count', 'sum', 'flip', 'and',\
    \ 'or'],\n    iterations=10,\n    warmup=2,\n    output_dir=\"./output/benchmark_results/bool_list\"\
    \n)\n\n# Create benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\n\
    @benchmark.data_generator(\"default\")\ndef generate_bool_data(size: int, operation:\
    \ str):\n    \"\"\"Generate boolean data in various formats\"\"\"\n    # Generate\
    \ random boolean data\n    bool_list = [random.random() < 0.5 for _ in range(size)]\n\
    \    int_list = [int(b) for b in bool_list]\n    \n    # Create different representations\n\
    \    array_b = array.array('b', int_list)\n    array_B = array.array('B', int_list)\n\
    \    \n    # Pack into bytes (8 bits per byte)\n    bytes_data = bytearray((size\
    \ + 7) // 8)\n    for i, bit in enumerate(bool_list):\n        if bit:\n     \
    \       bytes_data[i // 8] |= 1 << (7 - (i % 8))\n    bytes_data = bytes(bytes_data)\n\
    \    \n    # Create bitarray if available\n    bit_array = None\n    if HAS_BITARRAY:\n\
    \        bit_array = bitarray.bitarray(bool_list)\n    \n    # Create custom BitArray\
    \ if available\n    custom_bitarray = None\n    if HAS_CUSTOM_BITARRAY:\n    \
    \    custom_bitarray = BitArray(int_list)\n        custom_bitarray.build()\n \
    \   \n    # Pre-generate auxiliary data for binary operations\n    other_bool\
    \ = [random.random() < 0.5 for _ in range(size)]\n    other_int = [int(b) for\
    \ b in other_bool]\n    \n    return {\n        'bool_list': bool_list,\n    \
    \    'int_list': int_list,\n        'array_b': array_b,\n        'array_B': array_B,\n\
    \        'bytes_data': bytes_data,\n        'bit_array': bit_array,\n        'custom_bitarray':\
    \ custom_bitarray,\n        'other_bool': other_bool,\n        'other_int': other_int,\n\
    \        'size': size,\n        'operation': operation\n    }\n\n# Construction\
    \ operations\n@benchmark.implementation(\"list_bool\", \"construction\")\ndef\
    \ construction_list_bool(data):\n    \"\"\"Construct list[bool] from raw data\"\
    \"\"\n    # Use the same source data for all implementations\n    raw_data = data['bool_list']\n\
    \    result = list(raw_data)  # Create a copy\n    # Return consistent checksum\
    \ based on source data\n    checksum = 0\n    for i, b in enumerate(raw_data):\n\
    \        if b:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    list_int\", \"construction\")\ndef construction_list_int(data):\n    \"\"\"Construct\
    \ list[int] from raw data\"\"\"\n    # Use the same source data for all implementations\n\
    \    raw_data = data['bool_list']\n    int_list = [int(b) for b in raw_data]\n\
    \    # Return consistent checksum based on source data\n    checksum = 0\n   \
    \ for i, b in enumerate(raw_data):\n        if b:\n            checksum ^= i\n\
    \    return checksum\n\n@benchmark.implementation(\"array_b\", \"construction\"\
    )\ndef construction_array_b(data):\n    \"\"\"Construct array.array('b') from\
    \ raw data\"\"\"\n    # Use the same source data for all implementations\n   \
    \ raw_data = data['bool_list']\n    int_list = [int(b) for b in raw_data]\n  \
    \  array_b = array.array('b', int_list)\n    # Return consistent checksum based\
    \ on source data\n    checksum = 0\n    for i, b in enumerate(raw_data):\n   \
    \     if b:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_B\", \"construction\")\ndef construction_array_B(data):\n    \"\"\"Construct\
    \ array.array('B') from raw data\"\"\"\n    # Use the same source data for all\
    \ implementations\n    raw_data = data['bool_list']\n    int_list = [int(b) for\
    \ b in raw_data]\n    array_B = array.array('B', int_list)\n    # Return consistent\
    \ checksum based on source data\n    checksum = 0\n    for i, b in enumerate(raw_data):\n\
    \        if b:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytes\", \"construction\")\ndef construction_bytes(data):\n    \"\"\"Construct\
    \ bytes from raw data\"\"\"\n    # Use the same source data for all implementations\n\
    \    raw_data = data['bool_list']\n    size = data['size']\n    bytes_data = bytearray((size\
    \ + 7) // 8)\n    for i, bit in enumerate(raw_data):\n        if bit:\n      \
    \      bytes_data[i // 8] |= 1 << (7 - (i % 8))\n    bytes_data = bytes(bytes_data)\n\
    \    # Return consistent checksum based on source data\n    checksum = 0\n   \
    \ for i, b in enumerate(raw_data):\n        if b:\n            checksum ^= i\n\
    \    return checksum\n\nif HAS_BITARRAY:\n    @benchmark.implementation(\"bitarray\"\
    , \"construction\")\n    def construction_bitarray(data):\n        \"\"\"Construct\
    \ bitarray from raw data\"\"\"\n        # Use the same source data for all implementations\n\
    \        raw_data = data['bool_list']\n        bit_array = bitarray.bitarray(raw_data)\n\
    \        # Return consistent checksum based on source data\n        checksum =\
    \ 0\n        for i, b in enumerate(raw_data):\n            if b:\n           \
    \     checksum ^= i\n        return checksum\n\nif HAS_CUSTOM_BITARRAY:\n    @benchmark.implementation(\"\
    custom_bitarray\", \"construction\")\n    def construction_custom_bitarray(data):\n\
    \        \"\"\"Construct custom BitArray from raw data\"\"\"\n        # Use the\
    \ same source data for all implementations\n        raw_data = data['bool_list']\n\
    \        int_list = [int(b) for b in raw_data]\n        custom_bitarray = BitArray(int_list)\n\
    \        custom_bitarray.build()\n        # Return consistent checksum based on\
    \ source data\n        checksum = 0\n        for i, b in enumerate(raw_data):\n\
    \            if b:\n                checksum ^= i\n        return checksum\n\n\
    # Access operations\n@benchmark.implementation(\"list_bool\", \"access\")\ndef\
    \ access_list_bool(data):\n    \"\"\"Access operation on list[bool]\"\"\"\n  \
    \  lst = data['bool_list']\n    total = 0\n    access_count = min(1000, len(lst))\n\
    \    step = max(1, len(lst) // access_count)\n    for i in range(0, len(lst),\
    \ step):\n        if i < len(lst) and lst[i]:\n            total += 1\n    return\
    \ total\n\n@benchmark.implementation(\"list_int\", \"access\")\ndef access_list_int(data):\n\
    \    \"\"\"Access operation on list[int]\"\"\"\n    lst = data['int_list']\n \
    \   total = 0\n    access_count = min(1000, len(lst))\n    step = max(1, len(lst)\
    \ // access_count)\n    for i in range(0, len(lst), step):\n        if i < len(lst)\
    \ and lst[i]:\n            total += 1\n    return total\n\n@benchmark.implementation(\"\
    array_b\", \"access\")\ndef access_array_b(data):\n    \"\"\"Access operation\
    \ on array.array('b')\"\"\"\n    arr = data['array_b']\n    total = 0\n    access_count\
    \ = min(1000, len(arr))\n    step = max(1, len(arr) // access_count)\n    for\
    \ i in range(0, len(arr), step):\n        if i < len(arr) and arr[i]:\n      \
    \      total += 1\n    return total\n\n# Count operations\n@benchmark.implementation(\"\
    list_bool\", \"count\")\ndef count_list_bool(data):\n    \"\"\"Count True values\
    \ in list[bool]\"\"\"\n    return data['bool_list'].count(True)\n\n@benchmark.implementation(\"\
    list_int\", \"count\")\ndef count_list_int(data):\n    \"\"\"Count True values\
    \ in list[int]\"\"\"\n    return sum(data['int_list'])\n\n@benchmark.implementation(\"\
    array_b\", \"count\")\ndef count_array_b(data):\n    \"\"\"Count True values in\
    \ array.array('b')\"\"\"\n    return sum(data['array_b'])\n\n# Sum operations\
    \ (same as count for boolean data)\n@benchmark.implementation(\"list_bool\", \"\
    sum\")\ndef sum_list_bool(data):\n    \"\"\"Sum boolean values in list[bool]\"\
    \"\"\n    return sum(data['bool_list'])\n\n@benchmark.implementation(\"list_int\"\
    , \"sum\")\ndef sum_list_int(data):\n    \"\"\"Sum boolean values in list[int]\"\
    \"\"\n    return sum(data['int_list'])\n\n@benchmark.implementation(\"array_b\"\
    , \"sum\")\ndef sum_array_b(data):\n    \"\"\"Sum boolean values in array.array('b')\"\
    \"\"\n    return sum(data['array_b'])\n\n# Flip operations\n@benchmark.implementation(\"\
    list_bool\", \"flip\")\ndef flip_list_bool(data):\n    \"\"\"Flip all boolean\
    \ values in list[bool]\"\"\"\n    lst = list(data['bool_list'])  # Create copy\n\
    \    checksum = 0\n    for i in range(len(lst)):\n        lst[i] = not lst[i]\n\
    \        if lst[i]:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    list_int\", \"flip\")\ndef flip_list_int(data):\n    \"\"\"Flip all boolean values\
    \ in list[int]\"\"\"\n    lst = list(data['int_list'])  # Create copy\n    checksum\
    \ = 0\n    for i in range(len(lst)):\n        lst[i] = 1 - lst[i]\n        if\
    \ lst[i]:\n            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_b\", \"flip\")\ndef flip_array_b(data):\n    \"\"\"Flip all boolean values\
    \ in array.array('b')\"\"\"\n    arr = array.array('b', data['array_b'])  # Create\
    \ copy\n    checksum = 0\n    for i in range(len(arr)):\n        arr[i] = 1 -\
    \ arr[i]\n        if arr[i]:\n            checksum ^= i\n    return checksum\n\
    \n@benchmark.implementation(\"array_B\", \"flip\")\ndef flip_array_B(data):\n\
    \    \"\"\"Flip all boolean values in array.array('B')\"\"\"\n    arr = array.array('B',\
    \ data['array_B'])  # Create copy\n    checksum = 0\n    for i in range(len(arr)):\n\
    \        arr[i] = 1 - arr[i]\n        if arr[i]:\n            checksum ^= i\n\
    \    return checksum\n\n@benchmark.implementation(\"bytearray\", \"flip\")\ndef\
    \ flip_bytearray(data):\n    \"\"\"Flip all boolean values in bytearray (non-bit-packed)\"\
    \"\"\n    # Use int_list as source for non-bit-packed\n    int_list = data['int_list']\n\
    \    result = bytearray(int_list)  # Create copy\n    checksum = 0\n    for i\
    \ in range(len(result)):\n        result[i] = 1 - result[i]\n        if result[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytes\", \"flip\")\ndef flip_bytes(data):\n    \"\"\"Flip all boolean values in\
    \ bytes (non-bit-packed)\"\"\"\n    # Use int_list as source for non-bit-packed\n\
    \    int_list = data['int_list']\n    result = bytearray(int_list)  # Convert\
    \ to mutable\n    checksum = 0\n    for i in range(len(result)):\n        result[i]\
    \ = 1 - result[i]\n        if result[i]:\n            checksum ^= i\n    result\
    \ = bytes(result)  # Convert back to immutable\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray_packed\", \"flip\")\ndef flip_bytearray_packed(data):\n    \"\"\"Flip\
    \ all boolean values in bytearray (bit-packed)\"\"\"\n    # Use bit-packed bytes_data\n\
    \    size = data['size']\n    bytes_data = data['bytes_data']\n    result = bytearray(bytes_data)\
    \  # Create copy\n    checksum = 0\n    \n    # Flip each bit\n    for i in range(size):\n\
    \        byte_idx = i // 8\n        bit_idx = 7 - (i % 8)\n        \n        #\
    \ Get current bit\n        current_bit = (result[byte_idx] >> bit_idx) & 1\n \
    \       \n        # Flip the bit\n        if current_bit:\n            result[byte_idx]\
    \ &= ~(1 << bit_idx)  # Clear bit\n        else:\n            result[byte_idx]\
    \ |= (1 << bit_idx)   # Set bit\n            checksum ^= i\n    \n    return checksum\n\
    \n@benchmark.implementation(\"bytes_packed\", \"flip\")\ndef flip_bytes_packed(data):\n\
    \    \"\"\"Flip all boolean values in bytes (bit-packed)\"\"\"\n    # Use bit-packed\
    \ bytes_data\n    size = data['size']\n    bytes_data = data['bytes_data']\n \
    \   result = bytearray(bytes_data)  # Convert to mutable\n    checksum = 0\n \
    \   \n    # Flip each bit\n    for i in range(size):\n        byte_idx = i //\
    \ 8\n        bit_idx = 7 - (i % 8)\n        \n        # Get current bit\n    \
    \    current_bit = (result[byte_idx] >> bit_idx) & 1\n        \n        # Flip\
    \ the bit\n        if current_bit:\n            result[byte_idx] &= ~(1 << bit_idx)\
    \  # Clear bit\n        else:\n            result[byte_idx] |= (1 << bit_idx)\
    \   # Set bit\n            checksum ^= i\n    \n    result = bytes(result)  #\
    \ Convert back to immutable\n    return checksum\n\n# AND operations\n@benchmark.implementation(\"\
    list_bool\", \"and\")\ndef and_list_bool(data):\n    \"\"\"AND operation on list[bool]\"\
    \"\"\n    lst = data['bool_list']\n    other = data['other_bool']\n    checksum\
    \ = 0\n    for i in range(len(lst)):\n        if lst[i] and other[i]:\n      \
    \      checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"list_int\"\
    , \"and\")\ndef and_list_int(data):\n    \"\"\"AND operation on list[int]\"\"\"\
    \n    lst = data['int_list']\n    other = data['other_int']\n    checksum = 0\n\
    \    for i in range(len(lst)):\n        if lst[i] & other[i]:\n            checksum\
    \ ^= i\n    return checksum\n\n@benchmark.implementation(\"array_b\", \"and\"\
    )\ndef and_array_b(data):\n    \"\"\"AND operation on array.array('b')\"\"\"\n\
    \    arr = data['array_b']\n    other = array.array('b', data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] & other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_B\", \"and\")\ndef and_array_B(data):\n    \"\"\"AND operation on array.array('B')\"\
    \"\"\n    arr = data['array_B']\n    other = array.array('B', data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] & other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray\", \"and\")\ndef and_bytearray(data):\n    \"\"\"AND operation on bytearray\
    \ (non-bit-packed)\"\"\"\n    arr = bytearray(data['int_list'])\n    other = bytearray(data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] & other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytes\", \"and\")\ndef and_bytes(data):\n    \"\"\"AND operation on bytes (non-bit-packed)\"\
    \"\"\n    arr = bytes(data['int_list'])\n    other = bytes(data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] & other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray_packed\", \"and\")\ndef and_bytearray_packed(data):\n    \"\"\"AND operation\
    \ on bytearray (bit-packed)\"\"\"\n    size = data['size']\n    bytes_data = data['bytes_data']\n\
    \    other_bool = data['other_bool']\n    checksum = 0\n    \n    # AND each bit\n\
    \    for i in range(size):\n        byte_idx = i // 8\n        bit_idx = 7 - (i\
    \ % 8)\n        \n        # Get bits from both arrays\n        bit1 = (bytes_data[byte_idx]\
    \ >> bit_idx) & 1\n        bit2 = other_bool[i]\n        \n        # AND operation\n\
    \        if bit1 and bit2:\n            checksum ^= i\n    \n    return checksum\n\
    \n@benchmark.implementation(\"bytes_packed\", \"and\")\ndef and_bytes_packed(data):\n\
    \    \"\"\"AND operation on bytes (bit-packed)\"\"\"\n    size = data['size']\n\
    \    bytes_data = data['bytes_data']\n    other_bool = data['other_bool']\n  \
    \  checksum = 0\n    \n    # AND each bit\n    for i in range(size):\n       \
    \ byte_idx = i // 8\n        bit_idx = 7 - (i % 8)\n        \n        # Get bits\
    \ from both arrays\n        bit1 = (bytes_data[byte_idx] >> bit_idx) & 1\n   \
    \     bit2 = other_bool[i]\n        \n        # AND operation\n        if bit1\
    \ and bit2:\n            checksum ^= i\n    \n    return checksum\n\n# OR operations\n\
    @benchmark.implementation(\"list_bool\", \"or\")\ndef or_list_bool(data):\n  \
    \  \"\"\"OR operation on list[bool]\"\"\"\n    lst = data['bool_list']\n    other\
    \ = data['other_bool']\n    checksum = 0\n    for i in range(len(lst)):\n    \
    \    if lst[i] or other[i]:\n            checksum ^= i\n    return checksum\n\n\
    @benchmark.implementation(\"list_int\", \"or\")\ndef or_list_int(data):\n    \"\
    \"\"OR operation on list[int]\"\"\"\n    lst = data['int_list']\n    other = data['other_int']\n\
    \    checksum = 0\n    for i in range(len(lst)):\n        if lst[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_b\", \"or\")\ndef or_array_b(data):\n    \"\"\"OR operation on array.array('b')\"\
    \"\"\n    arr = data['array_b']\n    other = array.array('b', data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    array_B\", \"or\")\ndef or_array_B(data):\n    \"\"\"OR operation on array.array('B')\"\
    \"\"\n    arr = data['array_B']\n    other = array.array('B', data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray\", \"or\")\ndef or_bytearray(data):\n    \"\"\"OR operation on bytearray\
    \ (non-bit-packed)\"\"\"\n    arr = bytearray(data['int_list'])\n    other = bytearray(data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytes\", \"or\")\ndef or_bytes(data):\n    \"\"\"OR operation on bytes (non-bit-packed)\"\
    \"\"\n    arr = bytes(data['int_list'])\n    other = bytes(data['other_int'])\n\
    \    checksum = 0\n    for i in range(len(arr)):\n        if arr[i] | other[i]:\n\
    \            checksum ^= i\n    return checksum\n\n@benchmark.implementation(\"\
    bytearray_packed\", \"or\")\ndef or_bytearray_packed(data):\n    \"\"\"OR operation\
    \ on bytearray (bit-packed)\"\"\"\n    size = data['size']\n    bytes_data = data['bytes_data']\n\
    \    other_bool = data['other_bool']\n    checksum = 0\n    \n    # OR each bit\n\
    \    for i in range(size):\n        byte_idx = i // 8\n        bit_idx = 7 - (i\
    \ % 8)\n        \n        # Get bits from both arrays\n        bit1 = (bytes_data[byte_idx]\
    \ >> bit_idx) & 1\n        bit2 = other_bool[i]\n        \n        # OR operation\n\
    \        if bit1 or bit2:\n            checksum ^= i\n    \n    return checksum\n\
    \n@benchmark.implementation(\"bytes_packed\", \"or\")\ndef or_bytes_packed(data):\n\
    \    \"\"\"OR operation on bytes (bit-packed)\"\"\"\n    size = data['size']\n\
    \    bytes_data = data['bytes_data']\n    other_bool = data['other_bool']\n  \
    \  checksum = 0\n    \n    # OR each bit\n    for i in range(size):\n        byte_idx\
    \ = i // 8\n        bit_idx = 7 - (i % 8)\n        \n        # Get bits from both\
    \ arrays\n        bit1 = (bytes_data[byte_idx] >> bit_idx) & 1\n        bit2 =\
    \ other_bool[i]\n        \n        # OR operation\n        if bit1 or bit2:\n\
    \            checksum ^= i\n    \n    return checksum\n\n# Add bitarray implementations\
    \ if available\nif HAS_BITARRAY:\n    @benchmark.implementation(\"bitarray\",\
    \ [\"access\", \"count\", \"sum\", \"flip\", \"and\", \"or\"])\n    def bitarray_operations(data):\n\
    \        \"\"\"Operations on bitarray\"\"\"\n        operation = data['operation']\n\
    \        bit_arr = data['bit_array']\n        \n        if operation == 'access':\n\
    \            total = 0\n            access_count = min(1000, len(bit_arr))\n \
    \           step = max(1, len(bit_arr) // access_count)\n            for i in\
    \ range(0, len(bit_arr), step):\n                if i < len(bit_arr) and bit_arr[i]:\n\
    \                    total += 1\n            return total\n        elif operation\
    \ == 'count':\n            return bit_arr.count(True)\n        elif operation\
    \ == 'sum':\n            return bit_arr.count(True)\n        elif operation ==\
    \ 'flip':\n            result = bitarray.bitarray(bit_arr)\n            result.invert()\n\
    \            checksum = 0\n            for i, bit in enumerate(result):\n    \
    \            if bit:\n                    checksum ^= i\n            return checksum\n\
    \        elif operation == 'and':\n            other = bitarray.bitarray(data['other_bool'])\n\
    \            result = bit_arr & other\n            checksum = 0\n            for\
    \ i, bit in enumerate(result):\n                if bit:\n                    checksum\
    \ ^= i\n            return checksum\n        elif operation == 'or':\n       \
    \     other = bitarray.bitarray(data['other_bool'])\n            result = bit_arr\
    \ | other\n            checksum = 0\n            for i, bit in enumerate(result):\n\
    \                if bit:\n                    checksum ^= i\n            return\
    \ checksum\n\n# Add custom BitArray implementations if available\nif HAS_CUSTOM_BITARRAY:\n\
    \    @benchmark.implementation(\"custom_bitarray\", [\"access\", \"count\", \"\
    sum\"])\n    def custom_bitarray_operations(data):\n        \"\"\"Operations on\
    \ custom BitArray\"\"\"\n        operation = data['operation']\n        bit_arr\
    \ = data['custom_bitarray']\n        \n        if operation == 'access':\n   \
    \         total = 0\n            access_count = min(1000, len(bit_arr))\n    \
    \        step = max(1, len(bit_arr) // access_count)\n            for i in range(0,\
    \ len(bit_arr), step):\n                if i < len(bit_arr) and bit_arr[i]:\n\
    \                    total += 1\n            return total\n        elif operation\
    \ in ['count', 'sum']:\n            return sum(bit_arr[i] for i in range(len(bit_arr)))\n\
    \n# Custom validator for boolean operations\n@benchmark.validator(\"default\"\
    )\ndef validate_bool_result(expected, actual):\n    \"\"\"Validate boolean operation\
    \ results\"\"\"\n    # Convert results to comparable format\n    if hasattr(expected,\
    \ 'tolist'):  # array.array\n        expected = expected.tolist()\n    if hasattr(actual,\
    \ 'tolist'):  # array.array\n        actual = actual.tolist()\n    \n    # Handle\
    \ bitarray\n    if hasattr(expected, 'to01'):  # bitarray\n        expected =\
    \ [int(b) for b in expected.to01()]\n    if hasattr(actual, 'to01'):  # bitarray\n\
    \        actual = [int(b) for b in actual.to01()]\n    \n    # Convert booleans\
    \ to ints for comparison\n    if isinstance(expected, list) and len(expected)\
    \ > 0:\n        if isinstance(expected[0], bool):\n            expected = [int(b)\
    \ for b in expected]\n    if isinstance(actual, list) and len(actual) > 0:\n \
    \       if isinstance(actual[0], bool):\n            actual = [int(b) for b in\
    \ actual]\n    \n    return expected == actual\n\nif __name__ == \"__main__\"\
    :\n    # Parse command line args and run appropriate mode\n    runner = benchmark.parse_args()\n\
    \    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/wavelet/bit_array_cls.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/bit/popcnt32_fn.py
  - cp_library/ds/array/u32f_fn.py
  - cp_library/perf/checksum.py
  isVerificationFile: false
  path: perf/bool_list.py
  requiredBy: []
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/bool_list.py
layout: document
redirect_from:
- /library/perf/bool_list.py
- /library/perf/bool_list.py.html
title: perf/bool_list.py
---
