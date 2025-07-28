---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/reserve_fn.py
    title: cp_library/ds/list/reserve_fn.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing bytearray vs memoryview\
    \ decoding performance.\nTests decoding slices from bytearray vs memoryview with\
    \ different methods.\n\"\"\"\n\nimport random\nimport string\nimport sys\nimport\
    \ os\nimport io\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig\nfrom cp_library.ds.list.reserve_fn\
    \ import reserve\n\n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"\
    bytearray_decode\",\n    sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse\
    \ order to warm up JIT\n    operations=['small_slices', 'medium_slices', 'large_slices',\
    \ 'all_slices', 'extend'],\n    iterations=20,\n    warmup=3,\n    output_dir=\"\
    ./output/benchmark_results/bytearray_decode\"\n)\n\n# Create benchmark instance\n\
    benchmark = Benchmark(config)\n\n# Data generator\n@benchmark.data_generator(\"\
    default\")\ndef generate_data(size: int, operation: str):\n    \"\"\"Generate\
    \ test data for bytearray/memoryview decode operations\"\"\"\n    # Generate random\
    \ ASCII text with newlines\n    chars = string.ascii_letters + string.digits +\
    \ ' \\n'\n    text = ''.join(random.choice(chars) for _ in range(size))\n    B\
    \ = bytearray(text.encode('ascii'))\n    V = memoryview(B)\n    \n    # Calculate\
    \ proportional slice sizes based on data size\n    small_max = max(1, size //\
    \ 1000)  # 0.1% of size\n    medium_max = max(small_max + 1, size // 100)  # 1%\
    \ of size\n    large_max = max(medium_max + 1, size // 10)  # 10% of size\n  \
    \  \n    # Generate different slice sets based on operation\n    num_slices =\
    \ 1000\n    small_slices = []\n    medium_slices = []\n    large_slices = []\n\
    \    all_slices = []\n    \n    for _ in range(num_slices):\n        l = random.randint(0,\
    \ max(0, size - 2))\n        remaining = size - l\n        \n        # Small slices\n\
    \        if remaining > 0:\n            max_small_len = min(small_max, remaining)\n\
    \            if max_small_len > 0:\n                slice_len = random.randint(1,\
    \ max_small_len)\n                small_slices.append((l, l + slice_len))\n  \
    \      \n        # Medium slices\n        if remaining > small_max and medium_max\
    \ > small_max:\n            max_medium_len = min(medium_max, remaining)\n    \
    \        if max_medium_len > small_max:\n                slice_len = random.randint(small_max\
    \ + 1, max_medium_len)\n                medium_slices.append((l, l + slice_len))\n\
    \        \n        # Large slices\n        if remaining > medium_max and large_max\
    \ > medium_max:\n            max_large_len = min(large_max, remaining)\n     \
    \       if max_large_len > medium_max:\n                slice_len = random.randint(medium_max\
    \ + 1, max_large_len)\n                large_slices.append((l, l + slice_len))\n\
    \        \n        # All slices - mixed sizes\n        if remaining > 0:\n   \
    \         slice_type = random.random()\n            if slice_type < 0.33:\n  \
    \              # Small slice\n                max_len = min(small_max, remaining)\n\
    \                if max_len > 0:\n                    slice_len = random.randint(1,\
    \ max_len)\n                else:\n                    slice_len = 1\n       \
    \     elif slice_type < 0.66:\n                # Medium slice\n              \
    \  if remaining > small_max and medium_max > small_max:\n                    max_len\
    \ = min(medium_max, remaining)\n                    slice_len = random.randint(small_max\
    \ + 1, max_len)\n                else:\n                    # Fall back to small\
    \ slice\n                    max_len = min(small_max, remaining)\n           \
    \         slice_len = random.randint(1, max(1, max_len))\n            else:\n\
    \                # Large slice\n                if remaining > medium_max and\
    \ large_max > medium_max:\n                    max_len = min(large_max, remaining)\n\
    \                    slice_len = random.randint(medium_max + 1, max_len)\n   \
    \             else:\n                    # Fall back to whatever size is available\n\
    \                    slice_len = random.randint(1, min(large_max, remaining))\n\
    \            all_slices.append((l, l + slice_len))\n    \n    # Create BytesIO\n\
    \    bio = io.BytesIO(B)\n    \n    # Return appropriate slices based on operation\n\
    \    if operation == 'small_slices':\n        slices = small_slices\n    elif\
    \ operation == 'medium_slices':\n        slices = medium_slices\n    elif operation\
    \ == 'large_slices':\n        slices = large_slices\n    elif operation == 'all_slices':\n\
    \        slices = all_slices\n    else:\n        slices = []  # No slices needed\
    \ for extend operations\n    \n    # For extend operations, generate data chunks\n\
    \    if operation == 'extend':\n        # Generate chunks to extend\n        num_chunks\
    \ = 1000\n        chunks = []\n        chunk_sizes = [1, 10, 100, 1000]  # Various\
    \ chunk sizes\n        \n        for _ in range(num_chunks):\n            chunk_size\
    \ = random.choice(chunk_sizes)\n            chunk_text = ''.join(random.choice(chars)\
    \ for _ in range(chunk_size))\n            chunk_bytes = chunk_text.encode('ascii')\n\
    \            chunks.append(chunk_bytes)\n        \n        return {\n        \
    \    'bytearray': B,\n            'memoryview': V,\n            'bytesio': bio,\n\
    \            'slices': slices,\n            'chunks': chunks,\n            'size':\
    \ size,\n            'operation': operation\n        }\n    \n    return {\n \
    \       'bytearray': B,\n        'memoryview': V,\n        'bytesio': bio,\n \
    \       'slices': slices,\n        'size': size,\n        'operation': operation\n\
    \    }\n\n# Memoryview bytes implementations\n@benchmark.implementation(\"memoryview_bytes\"\
    , ['small_slices', 'medium_slices', 'large_slices', 'all_slices'])\ndef memoryview_bytes_decode(data):\n\
    \    \"\"\"Decode slices using memoryview[l:r].tobytes().decode()\"\"\"\n    V\
    \ = data['memoryview']\n    slices = data['slices']\n    checksum = 0\n    \n\
    \    for l, r in slices:\n        s = V[l:r].tobytes().decode('ascii', 'ignore')\n\
    \        checksum += len(s)  # Use length for checksum\n    \n    return checksum\n\
    \n# Bytearray implementations\n@benchmark.implementation(\"bytearray\", ['small_slices',\
    \ 'medium_slices', 'large_slices', 'all_slices'])\ndef bytearray_decode(data):\n\
    \    \"\"\"Decode slices using bytearray[l:r].decode()\"\"\"\n    B = data['bytearray']\n\
    \    slices = data['slices']\n    checksum = 0\n    \n    for l, r in slices:\n\
    \        s = B[l:r].decode('ascii', 'ignore')\n        checksum += len(s)  # Use\
    \ length for checksum\n    \n    return checksum\n\n# Memoryview implementations\n\
    @benchmark.implementation(\"memoryview\", ['small_slices', 'medium_slices', 'large_slices',\
    \ 'all_slices'])\ndef memoryview_decode(data):\n    \"\"\"Decode slices using\
    \ str(memoryview[l:r], encoding)\"\"\"\n    V = data['memoryview']\n    slices\
    \ = data['slices']\n    checksum = 0\n    \n    for l, r in slices:\n        s\
    \ = str(V[l:r], 'ascii', 'ignore')\n        checksum += len(s)  # Use length for\
    \ checksum\n    \n    return checksum\n\n# BytesIO implementations\n@benchmark.implementation(\"\
    bytesio\", ['small_slices', 'medium_slices', 'large_slices', 'all_slices'])\n\
    def bytesio_decode(data):\n    \"\"\"Decode slices using BytesIO seek/read operations\"\
    \"\"\n    bio = data['bytesio']\n    slices = data['slices']\n    checksum = 0\n\
    \    \n    for l, r in slices:\n        bio.seek(l)\n        s = bio.read(r -\
    \ l).decode('ascii', 'ignore')\n        checksum += len(s)  # Use length for checksum\n\
    \    \n    return checksum\n\n# Setup functions for extend operations\n@benchmark.setup(\"\
    bytearray\", [\"extend\"])\ndef setup_bytearray_extend(data):\n    \"\"\"Pre-initialize\
    \ bytearray for extend operations\"\"\"\n    prepared = data.copy()\n    prepared['bytearray']\
    \ = bytearray()\n    return prepared\n\n@benchmark.setup(\"bytesio\", [\"extend\"\
    ]) \ndef setup_bytesio_extend(data):\n    \"\"\"Pre-initialize BytesIO for extend\
    \ operations\"\"\"\n    prepared = data.copy()\n    prepared['bytesio'] = io.BytesIO()\n\
    \    return prepared\n\n# Extend implementations\n@benchmark.implementation(\"\
    bytearray\", \"extend\")\ndef bytearray_extend(data):\n    \"\"\"Extend bytearray\
    \ with chunks\"\"\"\n    B = data['bytearray']\n    chunks = data['chunks']\n\
    \    \n    for chunk in chunks:\n        B.extend(chunk)\n    \n    return len(B)\n\
    \n@benchmark.implementation(\"bytesio\", \"extend\")\ndef bytesio_extend(data):\n\
    \    \"\"\"Write chunks to BytesIO\"\"\"\n    bio = data['bytesio']\n    chunks\
    \ = data['chunks']\n    \n    for chunk in chunks:\n        bio.write(chunk)\n\
    \    \n    return bio.tell()\n\nif __name__ == \"__main__\":\n    # Parse command\
    \ line args and run appropriate mode\n    runner = benchmark.parse_args()\n  \
    \  \n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/list/reserve_fn.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/perf/checksum.py
  isVerificationFile: false
  path: perf/bytearray_decode.py
  requiredBy: []
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/bytearray_decode.py
layout: document
redirect_from:
- /library/perf/bytearray_decode.py
- /library/perf/bytearray_decode.py.html
title: perf/bytearray_decode.py
---
