---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/que/deque_cls.py
    title: cp_library/ds/que/deque_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/que/que_cls.py
    title: cp_library/ds/que/que_cls.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing Que vs FIFO queue alternatives.\n\
    Tests FIFO queue operations: push/append, pop/popleft, construction.\n\"\"\"\n\
    \nimport random\nimport sys\nimport os\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig\nfrom cp_library.ds.que.que_cls\
    \ import Que\nfrom cp_library.ds.que.deque_cls import Deque\nfrom collections\
    \ import deque as builtin_deque\nimport queue\n\n# Configure benchmark\nconfig\
    \ = BenchmarkConfig(\n    name=\"que\",\n    sizes=[1000000, 100000, 10000, 1000,\
    \ 100],  # Reverse order to warm up JIT\n    operations=['construction', 'access',\
    \ 'iteration', 'modification', 'fifo_push_pop', 'bulk_operations', 'mixed_fifo'],\n\
    \    iterations=10,\n    warmup=3,\n    output_dir=\"./output/benchmark_results/que\"\
    \n)\n\n# Create benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\n\
    @benchmark.data_generator(\"default\")\ndef generate_que_data(size: int, operation:\
    \ str):\n    \"\"\"Generate test data for FIFO queue operations\"\"\"\n    # Generate\
    \ initial data\n    initial_data = [random.randint(1, 1000) for _ in range(size)]\n\
    \    \n    # Generate operation data\n    num_ops = size\n    push_values = [random.randint(1,\
    \ 1000) for _ in range(num_ops)]\n    \n    return {\n        'initial_data':\
    \ initial_data,\n        'push_values': push_values,\n        'size': size,\n\
    \        'num_ops': num_ops\n    }\n\n# Setup functions\n@benchmark.setup(\"default\"\
    )\ndef setup(data):\n    prepared = data.copy()\n    return prepared\n\n# Construction\
    \ operation\n@benchmark.implementation(\"que\", \"construction\")\ndef construction_que(data):\n\
    \    \"\"\"Construct Que\"\"\"\n    que = Que(data['initial_data'])\n    return\
    \ len(que)\n\n@benchmark.implementation(\"deque_fifo\", \"construction\")\ndef\
    \ construction_deque_fifo(data):\n    \"\"\"Construct Deque for FIFO usage\"\"\
    \"\n    deque = Deque(data['initial_data'], maxlen=len(data['initial_data']) *\
    \ 2)\n    return len(deque)\n\n@benchmark.implementation(\"builtin_deque_fifo\"\
    , \"construction\")\ndef construction_builtin_deque_fifo(data):\n    \"\"\"Construct\
    \ builtin deque for FIFO usage\"\"\"\n    deque = builtin_deque(data['initial_data'],\
    \ maxlen=len(data['initial_data']) * 2)\n    return len(deque)\n\n# Access operations\n\
    @benchmark.implementation(\"que\", \"access\")\ndef access_que(data):\n    \"\"\
    \"Random access on Que using __getitem__\"\"\"\n    que = Que(data['initial_data'])\n\
    \    checksum = 0\n    for i in range(len(que)):\n        val = que[i]\n     \
    \   checksum ^= val\n    return checksum\n\n@benchmark.implementation(\"deque_fifo\"\
    , \"access\")\ndef access_deque_fifo(data):\n    \"\"\"Random access on Deque\
    \ using __getitem__\"\"\"\n    deque = Deque(data['initial_data'], maxlen=len(data['initial_data'])\
    \ * 2)\n    checksum = 0\n    for i in range(len(deque)):\n        val = deque[i]\n\
    \        checksum ^= val\n    return checksum\n\n@benchmark.implementation(\"\
    builtin_deque_fifo\", \"access\")\ndef access_builtin_deque_fifo(data):\n    \"\
    \"\"Random access on builtin deque using __getitem__ (O(n) operation)\"\"\"\n\
    \    # Skip for large sizes due to O(n) complexity\n    if data['size'] > 10000:\n\
    \        return None\n    \n    deque = builtin_deque(data['initial_data'])\n\
    \    checksum = 0\n    for i in range(len(deque)):\n        val = deque[i]\n \
    \       checksum ^= val\n    return checksum\n\n# Iteration operations\n@benchmark.implementation(\"\
    que\", \"iteration\")\ndef iteration_que(data):\n    \"\"\"Iterate through Que\
    \ using for-in\"\"\"\n    que = Que(data['initial_data'])\n    checksum = 0\n\
    \    for val in que:\n        checksum ^= val\n    return checksum\n\n@benchmark.implementation(\"\
    deque_fifo\", \"iteration\")\ndef iteration_deque_fifo(data):\n    \"\"\"Iterate\
    \ through Deque using for-in\"\"\"\n    deque = Deque(data['initial_data'], maxlen=len(data['initial_data'])\
    \ * 2)\n    checksum = 0\n    for val in deque:\n        checksum ^= val\n   \
    \ return checksum\n\n@benchmark.implementation(\"builtin_deque_fifo\", \"iteration\"\
    )\ndef iteration_builtin_deque_fifo(data):\n    \"\"\"Iterate through builtin\
    \ deque using for-in\"\"\"\n    deque = builtin_deque(data['initial_data'])\n\
    \    checksum = 0\n    for val in deque:\n        checksum ^= val\n    return\
    \ checksum\n\n# Modification operations\n@benchmark.implementation(\"que\", \"\
    modification\")\ndef modification_que(data):\n    \"\"\"Modify Que elements using\
    \ __setitem__\"\"\"\n    que = Que(data['initial_data'])\n    checksum = 0\n \
    \   for i in range(len(que)):\n        old_val = que[i]\n        new_val = (old_val\
    \ * 2) & 0xFFFFFFFF\n        que[i] = new_val\n        checksum ^= new_val\n \
    \   return checksum\n\n@benchmark.implementation(\"deque_fifo\", \"modification\"\
    )\ndef modification_deque_fifo(data):\n    \"\"\"Modify Deque elements using __setitem__\"\
    \"\"\n    deque = Deque(data['initial_data'], maxlen=len(data['initial_data'])\
    \ * 2)\n    checksum = 0\n    for i in range(len(deque)):\n        old_val = deque[i]\n\
    \        new_val = (old_val * 2) & 0xFFFFFFFF\n        deque[i] = new_val\n  \
    \      checksum ^= new_val\n    return checksum\n\n@benchmark.implementation(\"\
    builtin_deque_fifo\", \"modification\")\ndef modification_builtin_deque_fifo(data):\n\
    \    \"\"\"Modify builtin deque elements using __setitem__ (O(n) operation)\"\"\
    \"\n    # Skip for large sizes due to O(n) complexity\n    if data['size'] > 10000:\n\
    \        return None\n    \n    deque = builtin_deque(data['initial_data'])\n\
    \    checksum = 0\n    for i in range(len(deque)):\n        old_val = deque[i]\n\
    \        new_val = (old_val * 2) & 0xFFFFFFFF\n        deque[i] = new_val\n  \
    \      checksum ^= new_val\n    return checksum\n\n# FIFO push/pop operations\n\
    @benchmark.implementation(\"que\", \"fifo_push_pop\")\ndef fifo_push_pop_que(data):\n\
    \    \"\"\"FIFO push/pop on Que\"\"\"\n    que = Que()\n    checksum = 0\n   \
    \ \n    # Push all values\n    for val in data['push_values']:\n        que.push(val)\n\
    \        checksum ^= len(que)\n    \n    # Pop all values (FIFO order)\n    while\
    \ len(que) > 0:\n        val = que.pop()\n        checksum ^= val\n    \n    return\
    \ checksum\n\n@benchmark.implementation(\"deque_fifo\", \"fifo_push_pop\")\ndef\
    \ fifo_push_pop_deque_fifo(data):\n    \"\"\"FIFO push/pop on Deque\"\"\"\n  \
    \  deque = Deque(maxlen=len(data['push_values']) * 2)\n    checksum = 0\n    \n\
    \    # Push all values (append right)\n    for val in data['push_values']:\n \
    \       deque.append(val)\n        checksum ^= len(deque)\n    \n    # Pop all\
    \ values (pop left for FIFO)\n    while len(deque) > 0:\n        val = deque.popleft()\n\
    \        checksum ^= val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    builtin_deque_fifo\", \"fifo_push_pop\")\ndef fifo_push_pop_builtin_deque_fifo(data):\n\
    \    \"\"\"FIFO push/pop on builtin deque\"\"\"\n    deque = builtin_deque()\n\
    \    checksum = 0\n    \n    # Push all values (append right)\n    for val in\
    \ data['push_values']:\n        deque.append(val)\n        checksum ^= len(deque)\n\
    \    \n    # Pop all values (pop left for FIFO)\n    while len(deque) > 0:\n \
    \       val = deque.popleft()\n        checksum ^= val\n    \n    return checksum\n\
    \n\n# Bulk operations (construct with data, then pop all)\n@benchmark.implementation(\"\
    que\", \"bulk_operations\")\ndef bulk_operations_que(data):\n    \"\"\"Bulk construct\
    \ and pop all on Que\"\"\"\n    que = Que(data['initial_data'])\n    checksum\
    \ = 0\n    \n    # Pop all values\n    while len(que) > 0:\n        val = que.pop()\n\
    \        checksum ^= val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    deque_fifo\", \"bulk_operations\")\ndef bulk_operations_deque_fifo(data):\n  \
    \  \"\"\"Bulk construct and pop all on Deque\"\"\"\n    deque = Deque(data['initial_data'],\
    \ maxlen=len(data['initial_data']) * 2)\n    checksum = 0\n    \n    # Pop all\
    \ values (FIFO)\n    while len(deque) > 0:\n        val = deque.popleft()\n  \
    \      checksum ^= val\n    \n    return checksum\n\n@benchmark.implementation(\"\
    builtin_deque_fifo\", \"bulk_operations\")\ndef bulk_operations_builtin_deque_fifo(data):\n\
    \    \"\"\"Bulk construct and pop all on builtin deque\"\"\"\n    deque = builtin_deque(data['initial_data'])\n\
    \    checksum = 0\n    \n    # Pop all values (FIFO)\n    while len(deque) > 0:\n\
    \        val = deque.popleft()\n        checksum ^= val\n    \n    return checksum\n\
    \n\n# Mixed FIFO operations\n@benchmark.implementation(\"que\", \"mixed_fifo\"\
    )\ndef mixed_fifo_que(data):\n    \"\"\"Mixed FIFO operations on Que\"\"\"\n \
    \   que = Que()\n    checksum = 0\n    \n    for i, val in enumerate(data['push_values']):\n\
    \        if i % 3 == 0:\n            # Push\n            que.push(val)\n     \
    \       checksum ^= len(que)\n        elif i % 3 == 1 and len(que) > 0:\n    \
    \        # Pop (FIFO)\n            popped = que.pop()\n            checksum ^=\
    \ popped\n        else:\n            # Push again\n            que.push(val)\n\
    \            checksum ^= len(que)\n    \n    return checksum\n\n@benchmark.implementation(\"\
    deque_fifo\", \"mixed_fifo\")\ndef mixed_fifo_deque_fifo(data):\n    \"\"\"Mixed\
    \ FIFO operations on Deque\"\"\"\n    deque = Deque(maxlen=len(data['push_values'])\
    \ * 2)\n    checksum = 0\n    \n    for i, val in enumerate(data['push_values']):\n\
    \        if i % 3 == 0:\n            # Push (append right)\n            deque.append(val)\n\
    \            checksum ^= len(deque)\n        elif i % 3 == 1 and len(deque) >\
    \ 0:\n            # Pop (pop left for FIFO)\n            popped = deque.popleft()\n\
    \            checksum ^= popped\n        else:\n            # Push again\n   \
    \         deque.append(val)\n            checksum ^= len(deque)\n    \n    return\
    \ checksum\n\n@benchmark.implementation(\"builtin_deque_fifo\", \"mixed_fifo\"\
    )\ndef mixed_fifo_builtin_deque_fifo(data):\n    \"\"\"Mixed FIFO operations on\
    \ builtin deque\"\"\"\n    deque = builtin_deque()\n    checksum = 0\n    \n \
    \   for i, val in enumerate(data['push_values']):\n        if i % 3 == 0:\n  \
    \          # Push (append right)\n            deque.append(val)\n            checksum\
    \ ^= len(deque)\n        elif i % 3 == 1 and len(deque) > 0:\n            # Pop\
    \ (pop left for FIFO)\n            popped = deque.popleft()\n            checksum\
    \ ^= popped\n        else:\n            # Push again\n            deque.append(val)\n\
    \            checksum ^= len(deque)\n    \n    return checksum\n\nif __name__\
    \ == \"__main__\":\n    # Parse command line args and run appropriate mode\n \
    \   runner = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/que/que_cls.py
  - cp_library/ds/que/deque_cls.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/ds/elist_fn.py
  - cp_library/ds/list/list_find_fn.py
  - cp_library/perf/checksum.py
  isVerificationFile: false
  path: perf/que.py
  requiredBy: []
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/que.py
layout: document
redirect_from:
- /library/perf/que.py
- /library/perf/que.py.html
title: perf/que.py
---
