---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge/edge_list_weighted_cls.py
    title: cp_library/alg/graph/edge/edge_list_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_fn.py
    title: argsort
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/isort_parallel_fn.py
    title: cp_library/alg/iter/sort/isort_parallel_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/sort_parallel_fn.py
    title: cp_library/alg/iter/sort/sort_parallel_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/csr/csr_incremental_cls.py
    title: cp_library/ds/csr/csr_incremental_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/skew_heap_forrest_cls.py
    title: cp_library/ds/heap/skew_heap_forrest_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nSimple edge list benchmark using the new\
    \ declarative framework.\nMuch less boilerplate, easier to understand and extend.\n\
    \"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig\nfrom cp_library.alg.graph.edge.edge_list_weighted_cls\
    \ import EdgeListWeighted\n\n# Configure benchmark\nconfig = BenchmarkConfig(\n\
    \    name=\"edge_list\",\n    sizes=[1000000, 100000, 10000, 1000, 100, 10, 1],\
    \  # Reverse order to warm up JIT\n    operations=['sum_weights', 'filter', 'degree_count',\
    \ 'transform', 'sort', 'construction'],\n    iterations=10,\n    warmup=2,\n \
    \   output_dir=\"./output/benchmark_results/edge_list\"\n)\n\n# Create benchmark\
    \ instance\nbenchmark = Benchmark(config)\n\n# Data generators\n@benchmark.data_generator(\"\
    default\")\ndef generate_edge_data(size: int, operation: str):\n    \"\"\"Generate\
    \ edge list data in all formats\"\"\"\n    max_node = max(1, int(size ** 0.5)\
    \ * 2)\n    \n    # Generate raw edge data\n    U = [random.randint(0, max_node)\
    \ for _ in range(size)]\n    V = [random.randint(0, max_node) for _ in range(size)]\n\
    \    W = [random.randint(1, 1000) for _ in range(size)]\n    \n    # Create different\
    \ representations\n    edges_tuple = [(U[i], V[i], W[i]) for i in range(size)]\n\
    \    edge_list = EdgeListWeighted(max_node + 1, U, V, W)\n    \n    # Pre-initialize\
    \ data for fair timing (exclude initialization)\n    preinitialized = {\n    \
    \    'edges_tuple': list(edges_tuple),\n        'edge_list': EdgeListWeighted(max_node\
    \ + 1, list(U), list(V), list(W)),\n        'U': list(U), 'V': list(V), 'W': list(W),\n\
    \        'threshold': 500,\n        'max_node': max_node,\n        'degree_array':\
    \ [0] * (max_node + 1)\n    }\n    \n    return {\n        'edges_tuple': edges_tuple,\n\
    \        'edge_list': edge_list,\n        'U': U, 'V': V, 'W': W,\n        'size':\
    \ size,\n        'operation': operation,\n        'threshold': 500,\n        'max_node':\
    \ max_node,\n        'preinitialized': preinitialized\n    }\n\n# Construction\
    \ benchmarks - all should do equivalent work\n@benchmark.implementation(\"construct_tuple\"\
    , \"construction\")\ndef construct_tuple_list(data):\n    \"\"\"Construct list\
    \ of tuples from raw data\"\"\"\n    U, V, W = data['U'], data['V'], data['W']\n\
    \    return [(U[i], V[i], W[i]) for i in range(len(U))]\n\n@benchmark.implementation(\"\
    construct_edge_list_ref\", \"construction\")\ndef construct_edge_list_ref(data):\n\
    \    \"\"\"Construct EdgeListWeighted from raw data (reference assignment)\"\"\
    \"\n    U, V, W = data['U'], data['V'], data['W']\n    return EdgeListWeighted(data['max_node']\
    \ + 1, U, V, W)\n\n@benchmark.implementation(\"construct_edge_list_copy\", \"\
    construction\")\ndef construct_edge_list_copy(data):\n    \"\"\"Construct EdgeListWeighted\
    \ from copied data (fair comparison)\"\"\"\n    U, V, W = data['U'], data['V'],\
    \ data['W']\n    return EdgeListWeighted(data['max_node'] + 1, list(U), list(V),\
    \ list(W))\n\n@benchmark.implementation(\"construct_separated\", \"construction\"\
    )\ndef construct_separated_lists(data):\n    \"\"\"Create separated lists (copy\
    \ data)\"\"\"\n    U, V, W = data['U'], data['V'], data['W']\n    return (list(U),\
    \ list(V), list(W))\n\n# Sum weights operation\n@benchmark.implementation(\"tuple_direct\"\
    , \"sum_weights\")\ndef sum_weights_tuple_direct(data):\n    \"\"\"Sum weights\
    \ using direct tuple iteration\"\"\"\n    return sum(w for u, v, w in data['edges_tuple'])\n\
    \n@benchmark.implementation(\"edge_list_iter\", \"sum_weights\")\ndef sum_weights_edge_list_iter(data):\n\
    \    \"\"\"Sum weights using EdgeListWeighted iteration\"\"\"\n    return sum(w\
    \ for u, v, w in data['edge_list'])\n\n@benchmark.implementation(\"edge_list_direct\"\
    , \"sum_weights\")\ndef sum_weights_edge_list_direct(data):\n    \"\"\"Sum weights\
    \ using EdgeListWeighted direct access\"\"\"\n    return sum(data['edge_list'].W)\n\
    \n@benchmark.implementation(\"separated_lists\", \"sum_weights\")\ndef sum_weights_separated(data):\n\
    \    \"\"\"Sum weights using separated lists\"\"\"\n    return sum(data['W'])\n\
    \n# Filter operation\n@benchmark.implementation(\"tuple_direct\", \"filter\")\n\
    def filter_tuple_direct(data):\n    \"\"\"Filter edges using tuple iteration\"\
    \"\"\n    threshold = data['threshold']\n    return [(u, v, w) for u, v, w in\
    \ data['edges_tuple'] if w > threshold]\n\n@benchmark.implementation(\"edge_list_iter\"\
    , \"filter\")\ndef filter_edge_list_iter(data):\n    \"\"\"Filter edges using\
    \ EdgeListWeighted iteration\"\"\"\n    threshold = data['threshold']\n    return\
    \ [(u, v, w) for u, v, w in data['edge_list'] if w > threshold]\n\n@benchmark.implementation(\"\
    edge_list_direct\", \"filter\")\ndef filter_edge_list_direct(data):\n    \"\"\"\
    Filter edges using EdgeListWeighted direct access\"\"\"\n    threshold = data['threshold']\n\
    \    edge_list = data['edge_list']\n    result = []\n    for i in range(len(edge_list)):\n\
    \        if edge_list.W[i] > threshold:\n            result.append((edge_list.U[i],\
    \ edge_list.V[i], edge_list.W[i]))\n    return result\n\n@benchmark.implementation(\"\
    separated_lists\", \"filter\")\ndef filter_separated(data):\n    \"\"\"Filter\
    \ edges using separated lists\"\"\"\n    threshold = data['threshold']\n    U,\
    \ V, W = data['U'], data['V'], data['W']\n    return [(U[i], V[i], W[i]) for i\
    \ in range(len(W)) if W[i] > threshold]\n\n# Degree count operation\n@benchmark.implementation(\"\
    tuple_direct\", \"degree_count\")\ndef degree_count_tuple_direct(data):\n    \"\
    \"\"Count degrees using tuple iteration\"\"\"\n    degree = [0] * (data['max_node']\
    \ + 1)\n    for u, v, w in data['edges_tuple']:\n        degree[u] += 1\n    return\
    \ degree\n\n@benchmark.implementation(\"edge_list_iter\", \"degree_count\")\n\
    def degree_count_edge_list_iter(data):\n    \"\"\"Count degrees using EdgeListWeighted\
    \ iteration\"\"\"\n    degree = [0] * (data['max_node'] + 1)\n    for u, v, w\
    \ in data['edge_list']:\n        degree[u] += 1\n    return degree\n\n@benchmark.implementation(\"\
    edge_list_direct\", \"degree_count\")\ndef degree_count_edge_list_direct(data):\n\
    \    \"\"\"Count degrees using EdgeListWeighted direct access\"\"\"\n    degree\
    \ = [0] * (data['max_node'] + 1)\n    for u in data['edge_list'].U:\n        degree[u]\
    \ += 1\n    return degree\n\n@benchmark.implementation(\"separated_lists\", \"\
    degree_count\")\ndef degree_count_separated(data):\n    \"\"\"Count degrees using\
    \ separated lists\"\"\"\n    degree = [0] * (data['max_node'] + 1)\n    for u\
    \ in data['U']:\n        degree[u] += 1\n    return degree\n\n# Transform operation\n\
    @benchmark.implementation(\"tuple_direct\", \"transform\")\ndef transform_tuple_direct(data):\n\
    \    \"\"\"Transform edges using tuple iteration\"\"\"\n    return [(u, v, w *\
    \ 2) for u, v, w in data['edges_tuple']]\n\n@benchmark.implementation(\"edge_list_iter\"\
    , \"transform\")\ndef transform_edge_list_iter(data):\n    \"\"\"Transform edges\
    \ using EdgeListWeighted iteration\"\"\"\n    return [(u, v, w * 2) for u, v,\
    \ w in data['edge_list']]\n\n@benchmark.implementation(\"edge_list_direct\", \"\
    transform\")\ndef transform_edge_list_direct(data):\n    \"\"\"Transform edges\
    \ using EdgeListWeighted direct access\"\"\"\n    edge_list = data['edge_list']\n\
    \    return [(edge_list.U[i], edge_list.V[i], edge_list.W[i] * 2) \n         \
    \   for i in range(len(edge_list))]\n\n@benchmark.implementation(\"separated_lists\"\
    , \"transform\")\ndef transform_separated(data):\n    \"\"\"Transform edges using\
    \ separated lists\"\"\"\n    U, V, W = data['U'], data['V'], data['W']\n    return\
    \ [(U[i], V[i], W[i] * 2) for i in range(len(W))]\n\n# Sort operation\n@benchmark.implementation(\"\
    tuple_direct\", \"sort\")\ndef sort_tuple_direct(data):\n    \"\"\"Sort edges\
    \ using tuple list\"\"\"\n    edges = list(data['edges_tuple'])\n    edges.sort(key=lambda\
    \ x: x[2])\n    return edges\n\n@benchmark.implementation(\"edge_list_sort\",\
    \ \"sort\")\ndef sort_edge_list_builtin(data):\n    \"\"\"Sort edges using EdgeListWeighted\
    \ built-in sort\"\"\"\n    edge_list = EdgeListWeighted(data['edge_list'].N, \n\
    \                                list(data['edge_list'].U), \n               \
    \                 list(data['edge_list'].V), \n                              \
    \  list(data['edge_list'].W))\n    edge_list.sort()\n    return edge_list\n\n\
    @benchmark.implementation(\"separated_lists\", \"sort\")\ndef sort_separated(data):\n\
    \    \"\"\"Sort edges using separated lists\"\"\"\n    U, V, W = list(data['U']),\
    \ list(data['V']), list(data['W'])\n    # Sort by weight using indices\n    indices\
    \ = sorted(range(len(W)), key=lambda i: W[i])\n    return ([U[i] for i in indices],\
    \ [V[i] for i in indices], [W[i] for i in indices])\n\n# Custom validators\n@benchmark.validator(\"\
    sort\")\ndef validate_sort(expected, actual):\n    \"\"\"Validate that sort results\
    \ are equivalent\"\"\"\n    # Convert both to comparable format\n    if hasattr(expected,\
    \ 'W'):  # EdgeListWeighted\n        expected_weights = expected.W\n    elif isinstance(expected,\
    \ tuple):  # separated lists\n        expected_weights = expected[2]\n    else:\
    \  # list of tuples\n        expected_weights = [w for u, v, w in expected]\n\
    \    \n    if hasattr(actual, 'W'):  # EdgeListWeighted\n        actual_weights\
    \ = actual.W\n    elif isinstance(actual, tuple):  # separated lists\n       \
    \ actual_weights = actual[2]\n    else:  # list of tuples\n        actual_weights\
    \ = [w for u, v, w in actual]\n    \n    return expected_weights == actual_weights\n\
    \n@benchmark.validator(\"construction\")\ndef validate_construction(expected,\
    \ actual):\n    \"\"\"Validate construction results\"\"\"\n    # Just check that\
    \ something was created and has the right size\n    if actual is None:\n     \
    \   return False\n    \n    # Check based on type\n    if isinstance(actual, list):\
    \  # tuple list\n        return len(actual) > 0\n    elif hasattr(actual, 'M'):\
    \  # EdgeListWeighted\n        return actual.M > 0\n    elif isinstance(actual,\
    \ tuple):  # separated lists\n        return len(actual[0]) > 0\n    \n    return\
    \ True\n\nif __name__ == \"__main__\":\n    # Parse command line args and run\
    \ appropriate mode\n    runner = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/alg/graph/edge/edge_list_weighted_cls.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/alg/iter/sort/sort_parallel_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/ds/dsu_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/ds/heap/skew_heap_forrest_cls.py
  - cp_library/perf/checksum.py
  - cp_library/ds/csr/csr_incremental_cls.py
  - cp_library/io/io_base_cls.py
  isVerificationFile: false
  path: perf/edge_list.py
  requiredBy: []
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/edge_list.py
layout: document
redirect_from:
- /library/perf/edge_list.py
- /library/perf/edge_list.py.html
title: perf/edge_list.py
---
