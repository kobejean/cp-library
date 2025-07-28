---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_fn.py
    title: argsort
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/isort_parallel_fn.py
    title: cp_library/alg/iter/sort/isort_parallel_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list2_cls.py
    title: cp_library/ds/list/list2_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/seg/segtree2_cls.py
    title: cp_library/ds/tree/seg/segtree2_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/seg/segtree_cls.py
    title: cp_library/ds/tree/seg/segtree_cls.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing SegTree2 (dual-channel\
    \ segment tree) vs regular segment tree with tuples.\nTests construction, point\
    \ updates, range queries, and search operations.\n\"\"\"\n\nimport random\nimport\
    \ sys\nimport os\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig\nfrom cp_library.ds.tree.seg.segtree2_cls\
    \ import SegTree2\nfrom cp_library.ds.tree.seg.segtree_cls import SegTree\n\n\
    # Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"segtree2\",\n   \
    \ sizes=[1000000, 100000, 10000, 1000, 100],  # Reverse order to warm up JIT\n\
    \    operations=['construction', 'point_updates', 'range_queries', 'mixed_ops',\
    \ 'max_right_search', 'all_prod'],\n    iterations=10,\n    warmup=3,\n    output_dir=\"\
    ./output/benchmark_results/segtree2\"\n)\n\n# Create benchmark instance\nbenchmark\
    \ = Benchmark(config)\n\n# Define operations for segment trees\ndef tuple_add(a,\
    \ b):\n    \"\"\"Addition operation for tuples\"\"\"\n    return (a[0] + b[0],\
    \ a[1] + b[1])\n\ndef sum_threshold_check(x, threshold):\n    \"\"\"Check if sum\
    \ of tuple components is less than or equal to threshold\"\"\"\n    return x[0]\
    \ + x[1] <= threshold\n\n# Data generator\n@benchmark.data_generator(\"default\"\
    )\ndef generate_segtree2_data(size: int, operation: str):\n    \"\"\"Generate\
    \ test data for SegTree2 operations\"\"\"\n    # Generate random initial values\n\
    \    values_a = [random.randint(1, 1000) for _ in range(size)]\n    values_b =\
    \ [random.randint(1, 1000) for _ in range(size)]\n    \n    # Create tuple values\
    \ for regular SegTree\n    tuple_values = [(values_a[i], values_b[i]) for i in\
    \ range(size)]\n    \n    # Generate update operations\n    num_updates = min(1000,\
    \ size // 10)\n    update_indices = [random.randint(0, size - 1) for _ in range(num_updates)]\n\
    \    update_values_a = [random.randint(1, 1000) for _ in range(num_updates)]\n\
    \    update_values_b = [random.randint(1, 1000) for _ in range(num_updates)]\n\
    \    update_tuple_values = [(update_values_a[i], update_values_b[i]) for i in\
    \ range(num_updates)]\n    \n    # Generate query ranges\n    num_queries = min(1000,\
    \ size // 10)\n    query_ranges = []\n    for _ in range(num_queries):\n     \
    \   l = random.randint(0, size - 1)\n        r = random.randint(l + 1, size)\n\
    \        query_ranges.append((l, r))\n    \n    return {\n        'values_a':\
    \ values_a,\n        'values_b': values_b,\n        'tuple_values': tuple_values,\n\
    \        'update_indices': update_indices,\n        'update_values_a': update_values_a,\n\
    \        'update_values_b': update_values_b,\n        'update_tuple_values': update_tuple_values,\n\
    \        'query_ranges': query_ranges,\n        'size': size,\n        'threshold':\
    \ size * 100\n    }\n\n# Setup functions to prepare data and reduce overhead during\
    \ timing\n@benchmark.setup(\"default\")\ndef setup(data):\n    prepared = data.copy()\n\
    \    return prepared\n\n# Construction operation\n@benchmark.implementation(\"\
    segtree2_sum\", \"construction\")\ndef construction_segtree2_sum(data):\n    \"\
    \"\"Construct SegTree2 with sum operation\"\"\"\n    seg = SegTree2(tuple_add,\
    \ (0, 0), data['tuple_values'])\n    return seg.n\n\n@benchmark.implementation(\"\
    segtree_tuple_sum\", \"construction\")\ndef construction_segtree_tuple_sum(data):\n\
    \    \"\"\"Construct regular SegTree with tuple sum operation\"\"\"\n    seg =\
    \ SegTree(tuple_add, (0, 0), data['tuple_values'])\n    return seg.n\n\n# Point\
    \ updates operation\n@benchmark.implementation(\"segtree2_sum\", \"point_updates\"\
    )\ndef point_updates_segtree2_sum(data):\n    \"\"\"Point updates on SegTree2\
    \ with sum\"\"\"\n    seg = SegTree2(tuple_add, (0, 0), data['size'])\n    checksum\
    \ = 0\n    indices = data['update_indices']\n    updates = data['update_tuple_values']\n\
    \    for j in range(len(indices)):\n        i = indices[j]\n        val = updates[j]\n\
    \        seg.set(i, val)\n        result = seg.get(i)\n        checksum ^= result[0]\
    \ ^ result[1]\n    return checksum\n\n@benchmark.implementation(\"segtree_tuple_sum\"\
    , \"point_updates\")\ndef point_updates_segtree_tuple_sum(data):\n    \"\"\"Point\
    \ updates on regular SegTree with tuples\"\"\"\n    seg = SegTree(tuple_add, (0,\
    \ 0), data['size'])\n    checksum = 0\n    indices = data['update_indices']\n\
    \    updates = data['update_tuple_values']\n    for j in range(len(indices)):\n\
    \        i = indices[j]\n        val = updates[j]\n        seg.set(i, val)\n \
    \       result = seg.get(i)\n        checksum ^= result[0] ^ result[1]\n    return\
    \ checksum\n\n# Range queries operation\n@benchmark.implementation(\"segtree2_sum\"\
    , \"range_queries\")\ndef range_queries_segtree2_sum(data):\n    \"\"\"Range queries\
    \ on SegTree2 with sum\"\"\"\n    seg = SegTree2(tuple_add, (0, 0), data['tuple_values'])\n\
    \    checksum = 0\n    for l, r in data['query_ranges']:\n        result = seg.prod(l,\
    \ r)\n        checksum ^= result[0] ^ result[1]\n    return checksum\n\n@benchmark.implementation(\"\
    segtree_tuple_sum\", \"range_queries\")\ndef range_queries_segtree_tuple_sum(data):\n\
    \    \"\"\"Range queries on regular SegTree with tuples\"\"\"\n    seg = SegTree(tuple_add,\
    \ (0, 0), data['tuple_values'])\n    checksum = 0\n    for l, r in data['query_ranges']:\n\
    \        result = seg.prod(l, r)\n        checksum ^= result[0] ^ result[1]\n\
    \    return checksum\n\n# Mixed operations (updates + queries)\n@benchmark.implementation(\"\
    segtree2_sum\", \"mixed_ops\")\ndef mixed_ops_segtree2_sum(data):\n    \"\"\"\
    Mixed updates and queries on SegTree2\"\"\"\n    seg = SegTree2(tuple_add, (0,\
    \ 0), data['tuple_values'])\n    checksum = 0\n    \n    # Interleave updates\
    \ and queries\n    query_ranges = data['query_ranges']\n    update_indices = data['update_indices']\n\
    \    update_tuple_values = data['update_tuple_values']\n    min_len = min(len(query_ranges),\
    \ len(update_indices), len(update_tuple_values))\n    \n    for i in range(min_len):\n\
    \        if i % 2 == 0:\n            # Query\n            l, r = query_ranges[i]\n\
    \            result = seg.prod(l, r)\n            checksum ^= result[0] ^ result[1]\n\
    \        else:\n            # Update\n            idx = update_indices[i]\n  \
    \          val = update_tuple_values[i]\n            seg.set(idx, val)\n     \
    \       result = seg.get(idx)\n            checksum ^= result[0] ^ result[1]\n\
    \    return checksum\n\n@benchmark.implementation(\"segtree_tuple_sum\", \"mixed_ops\"\
    )\ndef mixed_ops_segtree_tuple_sum(data):\n    \"\"\"Mixed updates and queries\
    \ on regular SegTree\"\"\"\n    seg = SegTree(tuple_add, (0, 0), data['tuple_values'])\n\
    \    checksum = 0\n    \n    # Interleave updates and queries\n    query_ranges\
    \ = data['query_ranges']\n    update_indices = data['update_indices']\n    update_tuple_values\
    \ = data['update_tuple_values']\n    min_len = min(len(query_ranges), len(update_indices),\
    \ len(update_tuple_values))\n    \n    for i in range(min_len):\n        if i\
    \ % 2 == 0:\n            # Query\n            l, r = query_ranges[i]\n       \
    \     result = seg.prod(l, r)\n            checksum ^= result[0] ^ result[1]\n\
    \        else:\n            # Update\n            idx = update_indices[i]\n  \
    \          val = update_tuple_values[i]\n            seg.set(idx, val)\n     \
    \       result = seg.get(idx)\n            checksum ^= result[0] ^ result[1]\n\
    \    return checksum\n\n# Max right search operation\n@benchmark.implementation(\"\
    segtree2_sum\", \"max_right_search\")\ndef max_right_search_segtree2_sum(data):\n\
    \    \"\"\"Binary search using max_right on SegTree2\"\"\"\n    seg = SegTree2(tuple_add,\
    \ (0, 0), data['tuple_values'])\n    checksum = 0\n    \n    # Search for positions\
    \ where sum is less than threshold\n    threshold = data['threshold']\n    def\
    \ check_predicate(x):\n        return sum_threshold_check(x, threshold)\n    \n\
    \    for i in range(0, data['size'], max(1, data['size'] // 100)):\n        pos\
    \ = seg.max_right(i, check_predicate)\n        checksum ^= pos\n    return checksum\n\
    \n@benchmark.implementation(\"segtree_tuple_sum\", \"max_right_search\")\ndef\
    \ max_right_search_segtree_tuple_sum(data):\n    \"\"\"Binary search using max_right\
    \ on regular SegTree\"\"\"\n    seg = SegTree(tuple_add, (0, 0), data['tuple_values'])\n\
    \    checksum = 0\n    \n    # Search for positions where sum is less than threshold\n\
    \    threshold = data['threshold']\n    def check_predicate(x):\n        return\
    \ sum_threshold_check(x, threshold)\n    \n    for i in range(0, data['size'],\
    \ max(1, data['size'] // 100)):\n        pos = seg.max_right(i, check_predicate)\n\
    \        checksum ^= pos\n    return checksum\n\n# All product operation\n@benchmark.implementation(\"\
    segtree2_sum\", \"all_prod\")\ndef all_prod_segtree2_sum(data):\n    \"\"\"Get\
    \ total sum using all_prod on SegTree2\"\"\"\n    seg = SegTree2(tuple_add, (0,\
    \ 0), data['tuple_values'])\n    result = seg.all_prod()\n    return result[0]\
    \ ^ result[1]\n\n@benchmark.implementation(\"segtree_tuple_sum\", \"all_prod\"\
    )\ndef all_prod_segtree_tuple_sum(data):\n    \"\"\"Get total sum using all_prod\
    \ on regular SegTree\"\"\"\n    seg = SegTree(tuple_add, (0, 0), data['tuple_values'])\n\
    \    result = seg.all_prod()\n    return result[0] ^ result[1]\n\nif __name__\
    \ == \"__main__\":\n    # Parse command line args and run appropriate mode\n \
    \   runner = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/tree/seg/segtree2_cls.py
  - cp_library/ds/tree/seg/segtree_cls.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/ds/list/list2_cls.py
  - cp_library/perf/checksum.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: false
  path: perf/segtree2.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/segtree2.py
layout: document
redirect_from:
- /library/perf/segtree2.py
- /library/perf/segtree2.py.html
title: perf/segtree2.py
---
