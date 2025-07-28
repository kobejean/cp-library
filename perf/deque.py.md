---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/que/deque_cls.py
    title: cp_library/ds/que/deque_cls.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing Que vs Deque vs collections.deque.\n\
    Tests append/appendleft, pop/popleft, and construction operations.\n\"\"\"\n\n\
    import random\nimport sys\nimport os\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig\nfrom cp_library.ds.que.deque_cls\
    \ import Deque\nfrom collections import deque as builtin_deque\n\n# Configure\
    \ benchmark\nconfig = BenchmarkConfig(\n    name=\"deque\",\n    sizes=[10000000,\
    \ 1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT\n    operations=['construction',\
    \ 'access', 'iteration', 'modification', 'append_ops', 'append_left_ops', 'pop_ops',\
    \ 'pop_left_ops', 'mixed_ops'],\n    iterations=10,\n    warmup=3,\n    output_dir=\"\
    ./output/benchmark_results/deque\"\n)\n\n# Create benchmark instance\nbenchmark\
    \ = Benchmark(config)\n\n# Data generator\n@benchmark.data_generator(\"default\"\
    )\ndef generate_deque_data(size: int, operation: str):\n    \"\"\"Generate test\
    \ data for deque operations\"\"\"\n    # Generate initial data\n    initial_data\
    \ = [random.randint(1, 1_000_000_000) for _ in range(size)]\n    \n    # Generate\
    \ operation data\n    num_ops = size\n    append_values = [random.randint(1, 1_000_000_000)\
    \ for _ in range(num_ops)]\n    \n    return {\n        'initial_data': initial_data,\n\
    \        'append_values': append_values,\n        'size': size,\n        'num_ops':\
    \ num_ops\n    }\n\n# Setup functions\n@benchmark.setup(\"default\")\ndef setup(data):\n\
    \    prepared = data.copy()\n    return prepared\n\n# Construction operation\n\
    @benchmark.implementation(\"deque\", \"construction\")\ndef construction_deque(data):\n\
    \    \"\"\"Construct Deque\"\"\"\n    # Use maxlen to avoid capacity issues with\
    \ unlimited deque\n    deque = Deque(data['initial_data'], maxlen=len(data['initial_data'])\
    \ * 2)\n    return len(deque)\n\n@benchmark.implementation(\"builtin_deque\",\
    \ \"construction\")\ndef construction_builtin_deque(data):\n    \"\"\"Construct\
    \ builtin deque\"\"\"\n    deque = builtin_deque(data['initial_data'])\n    return\
    \ len(deque)\n\n# Access operations\n@benchmark.implementation(\"deque\", \"access\"\
    )\ndef access_deque(data):\n    \"\"\"Random access on Deque using __getitem__\"\
    \"\"\n    deque = Deque(data['initial_data'], maxlen=len(data['initial_data'])\
    \ * 2)\n    checksum = 0\n    for i in range(len(deque)):\n        val = deque[i]\n\
    \        checksum ^= val\n    return checksum\n\n@benchmark.implementation(\"\
    builtin_deque\", \"access\")\ndef access_builtin_deque(data):\n    \"\"\"Random\
    \ access on builtin deque using __getitem__ (O(n) operation)\"\"\"\n    # Skip\
    \ for large sizes due to O(n) complexity\n    if data['size'] > 10000:\n     \
    \   return None\n    \n    deque = builtin_deque(data['initial_data'])\n    checksum\
    \ = 0\n    for i in range(len(deque)):\n        val = deque[i]\n        checksum\
    \ ^= val\n    return checksum\n\n# Iteration operations\n@benchmark.implementation(\"\
    deque\", \"iteration\")\ndef iteration_deque(data):\n    \"\"\"Iterate through\
    \ Deque using for-in\"\"\"\n    deque = Deque(data['initial_data'], maxlen=len(data['initial_data'])\
    \ * 2)\n    checksum = 0\n    for val in deque:\n        checksum ^= val\n   \
    \ return checksum\n\n@benchmark.implementation(\"builtin_deque\", \"iteration\"\
    )\ndef iteration_builtin_deque(data):\n    \"\"\"Iterate through builtin deque\
    \ using for-in\"\"\"\n    deque = builtin_deque(data['initial_data'])\n    checksum\
    \ = 0\n    for val in deque:\n        checksum ^= val\n    return checksum\n\n\
    # Modification operations\n@benchmark.implementation(\"deque\", \"modification\"\
    )\ndef modification_deque(data):\n    \"\"\"Modify Deque elements using __setitem__\"\
    \"\"\n    deque = Deque(data['initial_data'], maxlen=len(data['initial_data'])\
    \ * 2)\n    checksum = 0\n    for i in range(len(deque)):\n        old_val = deque[i]\n\
    \        new_val = (old_val * 2) & 0xFFFFFFFF\n        deque[i] = new_val\n  \
    \      checksum ^= new_val\n    return checksum\n\n@benchmark.implementation(\"\
    builtin_deque\", \"modification\")\ndef modification_builtin_deque(data):\n  \
    \  \"\"\"Modify builtin deque elements using __setitem__ (O(n) operation)\"\"\"\
    \n    # Skip for large sizes due to O(n) complexity\n    if data['size'] > 10000:\n\
    \        return None\n    \n    deque = builtin_deque(data['initial_data'])\n\
    \    checksum = 0\n    for i in range(len(deque)):\n        old_val = deque[i]\n\
    \        new_val = (old_val * 2) & 0xFFFFFFFF\n        deque[i] = new_val\n  \
    \      checksum ^= new_val\n    return checksum\n\n# Append operations (right\
    \ side)\n@benchmark.implementation(\"deque\", \"append_ops\")\ndef append_ops_deque(data):\n\
    \    \"\"\"Append operations on Deque\"\"\"\n    deque = Deque()\n    checksum\
    \ = 0\n    for val in data['append_values']:\n        deque.append(val)\n    \
    \    checksum ^= len(deque)\n    return checksum\n\n@benchmark.implementation(\"\
    builtin_deque\", \"append_ops\")\ndef append_ops_builtin_deque(data):\n    \"\"\
    \"Append operations on builtin deque\"\"\"\n    deque = builtin_deque()\n    checksum\
    \ = 0\n    for val in data['append_values']:\n        deque.append(val)\n    \
    \    checksum ^= len(deque)\n    return checksum\n\n# Append left operations (only\
    \ Deque and builtin_deque support this)\n@benchmark.implementation(\"deque\",\
    \ \"append_left_ops\")\ndef append_left_ops_deque(data):\n    \"\"\"Append left\
    \ operations on Deque\"\"\"\n    deque = Deque()\n    checksum = 0\n    for val\
    \ in data['append_values']:\n        deque.appendleft(val)\n        checksum ^=\
    \ len(deque)\n    return checksum\n\n@benchmark.implementation(\"builtin_deque\"\
    , \"append_left_ops\")\ndef append_left_ops_builtin_deque(data):\n    \"\"\"Append\
    \ left operations on builtin deque\"\"\"\n    deque = builtin_deque()\n    checksum\
    \ = 0\n    for val in data['append_values']:\n        deque.appendleft(val)\n\
    \        checksum ^= len(deque)\n    return checksum\n\n# Pop operations (right\
    \ side)\n\n@benchmark.implementation(\"deque\", \"pop_ops\")\ndef pop_ops_deque(data):\n\
    \    \"\"\"Pop operations on Deque (right side)\"\"\"\n    deque = Deque(data['initial_data'],\
    \ maxlen=len(data['initial_data']) * 2)\n    checksum = 0\n    for _ in range(min(len(deque),\
    \ len(data['append_values']))):\n        if len(deque) > 0:\n            val =\
    \ deque.pop()\n            checksum ^= val\n    return checksum\n\n@benchmark.implementation(\"\
    builtin_deque\", \"pop_ops\")\ndef pop_ops_builtin_deque(data):\n    \"\"\"Pop\
    \ operations on builtin deque (right side)\"\"\"\n    deque = builtin_deque(data['initial_data'])\n\
    \    checksum = 0\n    for _ in range(min(len(deque), len(data['append_values']))):\n\
    \        if len(deque) > 0:\n            val = deque.pop()\n            checksum\
    \ ^= val\n    return checksum\n\n# Pop left operations (only Deque and builtin_deque\
    \ support this)\n@benchmark.implementation(\"deque\", \"pop_left_ops\")\ndef pop_left_ops_deque(data):\n\
    \    \"\"\"Pop left operations on Deque\"\"\"\n    deque = Deque(data['initial_data'],\
    \ maxlen=len(data['initial_data']) * 2)\n    checksum = 0\n    for _ in range(min(len(deque),\
    \ len(data['append_values']))):\n        if len(deque) > 0:\n            val =\
    \ deque.popleft()\n            checksum ^= val\n    return checksum\n\n@benchmark.implementation(\"\
    builtin_deque\", \"pop_left_ops\")\ndef pop_left_ops_builtin_deque(data):\n  \
    \  \"\"\"Pop left operations on builtin deque\"\"\"\n    deque = builtin_deque(data['initial_data'])\n\
    \    checksum = 0\n    for _ in range(min(len(deque), len(data['append_values']))):\n\
    \        if len(deque) > 0:\n            val = deque.popleft()\n            checksum\
    \ ^= val\n    return checksum\n\n# Mixed operations\n@benchmark.implementation(\"\
    deque\", \"mixed_ops\")\ndef mixed_ops_deque(data):\n    \"\"\"Mixed operations\
    \ on Deque\"\"\"\n    deque = Deque()\n    checksum = 0\n    \n    for i, val\
    \ in enumerate(data['append_values']):\n        if i % 4 == 0:\n            #\
    \ Append right\n            deque.append(val)\n            checksum ^= len(deque)\n\
    \        elif i % 4 == 1:\n            # Append left\n            deque.appendleft(val)\n\
    \            checksum ^= len(deque)\n        elif i % 4 == 2 and len(deque) >\
    \ 0:\n            # Pop right\n            popped = deque.pop()\n            checksum\
    \ ^= popped\n        elif i % 4 == 3 and len(deque) > 0:\n            # Pop left\n\
    \            popped = deque.popleft()\n            checksum ^= popped\n    \n\
    \    return checksum\n\n@benchmark.implementation(\"builtin_deque\", \"mixed_ops\"\
    )\ndef mixed_ops_builtin_deque(data):\n    \"\"\"Mixed operations on builtin deque\"\
    \"\"\n    deque = builtin_deque()\n    checksum = 0\n    \n    for i, val in enumerate(data['append_values']):\n\
    \        if i % 4 == 0:\n            # Append right\n            deque.append(val)\n\
    \            checksum ^= len(deque)\n        elif i % 4 == 1:\n            # Append\
    \ left\n            deque.appendleft(val)\n            checksum ^= len(deque)\n\
    \        elif i % 4 == 2 and len(deque) > 0:\n            # Pop right\n      \
    \      popped = deque.pop()\n            checksum ^= popped\n        elif i %\
    \ 4 == 3 and len(deque) > 0:\n            # Pop left\n            popped = deque.popleft()\n\
    \            checksum ^= popped\n    \n    return checksum\n\nif __name__ == \"\
    __main__\":\n    # Parse command line args and run appropriate mode\n    runner\
    \ = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/que/deque_cls.py
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
  path: perf/deque.py
  requiredBy: []
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/deque.py
layout: document
redirect_from:
- /library/perf/deque.py
- /library/perf/deque.py.html
title: perf/deque.py
---
