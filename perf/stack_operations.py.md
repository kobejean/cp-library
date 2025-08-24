---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/elist_fn.py
    title: cp_library/ds/list/elist_fn.py
  - icon: ':warning:'
    path: cp_library/ds/stack/stack_fn.py
    title: cp_library/ds/stack/stack_fn.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing stack operations: stack_fn\
    \ vs elist_fn vs normal list.\nTests push-only, mixed push/pop, and peek-heavy\
    \ workloads.\n\"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0,\
    \ os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig\nfrom cp_library.ds.stack.stack_fn import\
    \ stack\nfrom cp_library.ds.list.elist_fn import elist\n\n# Configure benchmark\n\
    config = BenchmarkConfig(\n    name=\"stack_operations\",\n    sizes=[1000000,\
    \ 100000, 10000, 1000],  # Reverse order to warm up JIT\n    operations=['construction',\
    \ 'push_only', 'pop_only', 'push_pop_mixed', 'peek_heavy', 'construction_with_data'],\n\
    \    iterations=10,\n    warmup=3,\n    output_dir=\"./output/benchmark_results/stack\"\
    \n)\n\n# Create benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generator\n\
    @benchmark.data_generator(\"default\")\ndef generate_stack_data(size: int, operation:\
    \ str):\n    \"\"\"Generate test data for stack operations\"\"\"\n    # Generate\
    \ values to push\n    push_values = [random.randint(0, 1000000) for _ in range(size)]\n\
    \    \n    # For mixed operations, generate operation sequence\n    num_ops =\
    \ min(size, 100000)  # Limit operations for large sizes\n    \n    return {\n\
    \        'size': size,\n        'push_values': push_values,\n        'num_ops':\
    \ num_ops,\n        'operation': operation\n    }\n\n# Setup functions for operations\
    \ that need preinitialized stacks\n@benchmark.setup(\"stack\", [\"pop_only\"])\n\
    def setup_stack_pop(data):\n    \"\"\"Setup stack with data for pop operations\"\
    \"\"\n    new_data = data.copy()\n    size = data['size']\n    values = data['push_values']\n\
    \    \n    st = stack(size)\n    for val in values:\n        st.push(val)\n  \
    \  \n    new_data['stack'] = st\n    return new_data\n\n@benchmark.setup(\"elist\"\
    , [\"pop_only\"])\ndef setup_elist_pop(data):\n    \"\"\"Setup elist with data\
    \ for pop operations\"\"\"\n    new_data = data.copy()\n    size = data['size']\n\
    \    values = data['push_values']\n    \n    lst = elist(size)\n    for val in\
    \ values:\n        lst.append(val)\n    \n    new_data['elist'] = lst\n    return\
    \ new_data\n\n@benchmark.setup(\"list\", [\"pop_only\"])\ndef setup_list_pop(data):\n\
    \    \"\"\"Setup list with data for pop operations\"\"\"\n    new_data = data.copy()\n\
    \    values = data['push_values']\n    \n    new_data['list'] = values.copy()\n\
    \    return new_data\n\n# Push-only operation\n@benchmark.implementation(\"stack\"\
    , \"push_only\")\ndef push_only_stack(data):\n    \"\"\"Push n elements using\
    \ stack class\"\"\"\n    size = data['size']\n    values = data['push_values']\n\
    \    \n    st = stack(size)\n    for val in values:\n        st.push(val)\n  \
    \  \n    # Return something to verify correctness\n    return len(st)\n\n@benchmark.implementation(\"\
    elist\", \"push_only\")\ndef push_only_elist(data):\n    \"\"\"Push n elements\
    \ using elist with hint\"\"\"\n    size = data['size']\n    values = data['push_values']\n\
    \    \n    lst = elist(size)\n    for val in values:\n        lst.append(val)\n\
    \    \n    return len(lst)\n\n@benchmark.implementation(\"list\", \"push_only\"\
    )\ndef push_only_list(data):\n    \"\"\"Push n elements using normal list\"\"\"\
    \n    values = data['push_values']\n    \n    lst = []\n    for val in values:\n\
    \        lst.append(val)\n    \n    return len(lst)\n\n# Mixed push/pop operations\n\
    @benchmark.implementation(\"stack\", \"push_pop_mixed\")\ndef push_pop_mixed_stack(data):\n\
    \    \"\"\"Mixed push and pop operations using stack class\"\"\"\n    size = data['size']\n\
    \    num_ops = data['num_ops']\n    \n    st = stack(size)\n    \n    # Initial\
    \ push\n    for i in range(size // 2):\n        st.push(i)\n    \n    # Mixed\
    \ operations\n    checksum = 0\n    for i in range(num_ops):\n        if i % 3\
    \ == 0 and len(st) > 0:\n            checksum ^= st.pop()\n        else:\n   \
    \         st.push(i)\n            if len(st) > size * 0.9:  # Prevent overflow\n\
    \                st.pop()\n    \n    return checksum\n\n@benchmark.implementation(\"\
    elist\", \"push_pop_mixed\")\ndef push_pop_mixed_elist(data):\n    \"\"\"Mixed\
    \ push and pop operations using elist\"\"\"\n    size = data['size']\n    num_ops\
    \ = data['num_ops']\n    \n    lst = elist(size)\n    \n    # Initial push\n \
    \   for i in range(size // 2):\n        lst.append(i)\n    \n    # Mixed operations\n\
    \    checksum = 0\n    for i in range(num_ops):\n        if i % 3 == 0 and len(lst)\
    \ > 0:\n            checksum ^= lst.pop()\n        else:\n            lst.append(i)\n\
    \            if len(lst) > size * 0.9:\n                lst.pop()\n    \n    return\
    \ checksum\n\n@benchmark.implementation(\"list\", \"push_pop_mixed\")\ndef push_pop_mixed_list(data):\n\
    \    \"\"\"Mixed push and pop operations using normal list\"\"\"\n    size = data['size']\n\
    \    num_ops = data['num_ops']\n    \n    lst = []\n    \n    # Initial push\n\
    \    for i in range(size // 2):\n        lst.append(i)\n    \n    # Mixed operations\n\
    \    checksum = 0\n    for i in range(num_ops):\n        if i % 3 == 0 and len(lst)\
    \ > 0:\n            checksum ^= lst.pop()\n        else:\n            lst.append(i)\n\
    \            if len(lst) > size * 0.9:\n                lst.pop()\n    \n    return\
    \ checksum\n\n# Peek-heavy operations\n@benchmark.implementation(\"stack\", \"\
    peek_heavy\")\ndef peek_heavy_stack(data):\n    \"\"\"Peek-heavy operations using\
    \ stack class\"\"\"\n    size = min(data['size'], 10000)  # Limit for peek operations\n\
    \    \n    st = stack(size)\n    for i in range(size):\n        st.push(i)\n \
    \   \n    checksum = 0\n    # Many peek operations\n    for _ in range(size *\
    \ 10):\n        if len(st) > 0:\n            checksum ^= st.peek()\n    \n   \
    \ return checksum\n\n@benchmark.implementation(\"elist\", \"peek_heavy\")\ndef\
    \ peek_heavy_elist(data):\n    \"\"\"Peek-heavy operations using elist\"\"\"\n\
    \    size = min(data['size'], 10000)\n    \n    lst = elist(size)\n    for i in\
    \ range(size):\n        lst.append(i)\n    \n    checksum = 0\n    for _ in range(size\
    \ * 10):\n        if len(lst) > 0:\n            checksum ^= lst[-1]\n    \n  \
    \  return checksum\n\n@benchmark.implementation(\"list\", \"peek_heavy\")\ndef\
    \ peek_heavy_list(data):\n    \"\"\"Peek-heavy operations using normal list\"\"\
    \"\n    size = min(data['size'], 10000)\n    \n    lst = []\n    for i in range(size):\n\
    \        lst.append(i)\n    \n    checksum = 0\n    for _ in range(size * 10):\n\
    \        if len(lst) > 0:\n            checksum ^= lst[-1]\n    \n    return checksum\n\
    \n# Construction benchmarks\n@benchmark.implementation(\"stack\", \"construction\"\
    )\ndef construction_stack(data):\n    \"\"\"Construct empty stack with capacity\"\
    \"\"\n    size = data['size']\n    st = stack(size)\n    return len(st)  # Should\
    \ be 0\n\n@benchmark.implementation(\"elist\", \"construction\")\ndef construction_elist(data):\n\
    \    \"\"\"Construct empty elist with hint\"\"\"\n    size = data['size']\n  \
    \  lst = elist(size)\n    return len(lst)  # Should be 0\n\n@benchmark.implementation(\"\
    list\", \"construction\")\ndef construction_list(data):\n    \"\"\"Construct empty\
    \ list\"\"\"\n    lst = []\n    return len(lst)  # Should be 0\n\n# Construction\
    \ with initial data\n@benchmark.implementation(\"stack\", \"construction_with_data\"\
    )\ndef construction_with_data_stack(data):\n    \"\"\"Construct and fill stack\"\
    \"\"\n    size = data['size']\n    values = data['push_values']\n    \n    st\
    \ = stack(size)\n    for val in values:\n        st.push(val)\n    return len(st)\n\
    \n@benchmark.implementation(\"elist\", \"construction_with_data\")\ndef construction_with_data_elist(data):\n\
    \    \"\"\"Construct and fill elist\"\"\"\n    size = data['size']\n    values\
    \ = data['push_values']\n    \n    lst = elist(size)\n    for val in values:\n\
    \        lst.append(val)\n    return len(lst)\n\n@benchmark.implementation(\"\
    list\", \"construction_with_data\")\ndef construction_with_data_list(data):\n\
    \    \"\"\"Construct and fill list using comprehension\"\"\"\n    values = data['push_values']\n\
    \    lst = [val for val in values]\n    return len(lst)\n\n# Pop-only operations\
    \ (with preinitialized data)\n@benchmark.implementation(\"stack\", \"pop_only\"\
    )\ndef pop_only_stack(data):\n    \"\"\"Pop all elements from preinitialized stack\"\
    \"\"\n    st = data['stack']\n    checksum = 0\n    \n    while len(st) > 0:\n\
    \        checksum ^= st.pop()\n    \n    return checksum\n\n@benchmark.implementation(\"\
    elist\", \"pop_only\")\ndef pop_only_elist(data):\n    \"\"\"Pop all elements\
    \ from preinitialized elist\"\"\"\n    lst = data['elist']\n    checksum = 0\n\
    \    \n    while len(lst) > 0:\n        checksum ^= lst.pop()\n    \n    return\
    \ checksum\n\n@benchmark.implementation(\"list\", \"pop_only\")\ndef pop_only_list(data):\n\
    \    \"\"\"Pop all elements from preinitialized list\"\"\"\n    lst = data['list']\n\
    \    checksum = 0\n    \n    while len(lst) > 0:\n        checksum ^= lst.pop()\n\
    \    \n    return checksum\n\nif __name__ == \"__main__\":\n    # Parse command\
    \ line args and run appropriate mode\n    runner = benchmark.parse_args()\n  \
    \  runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/stack/stack_fn.py
  - cp_library/ds/list/elist_fn.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/perf/checksum.py
  isVerificationFile: false
  path: perf/stack_operations.py
  requiredBy: []
  timestamp: '2025-08-24 20:27:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/stack_operations.py
layout: document
redirect_from:
- /library/perf/stack_operations.py
- /library/perf/stack_operations.py.html
title: perf/stack_operations.py
---
