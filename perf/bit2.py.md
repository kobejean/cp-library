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
    path: cp_library/ds/tree/bit/bit2_cls.py
    title: cp_library/ds/tree/bit/bit2_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit_base_cls.py
    title: cp_library/ds/tree/bit/bit_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit_monoid_cls.py
    title: cp_library/ds/tree/bit/bit_monoid_cls.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nBenchmark comparing BIT2 (dual-channel BIT)\
    \ vs regular BIT with tuples.\nTests construction, point updates, prefix sums,\
    \ range sums, and mixed operations.\n\"\"\"\n\nimport random\nimport sys\nimport\
    \ os\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig\nfrom cp_library.ds.tree.bit.bit2_cls\
    \ import BIT2\nfrom cp_library.ds.tree.bit.bit_monoid_cls import BITMonoid\n\n\
    # Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"bit2\",\n    sizes=[1000000,\
    \ 100000, 10000, 1000, 100],  # Reverse order to warm up JIT\n    operations=['construction',\
    \ 'point_updates', 'prefix_sums', 'range_sums', 'mixed_ops'],\n    iterations=10,\n\
    \    warmup=3,\n    output_dir=\"./output/benchmark_results/bit2\"\n)\n\n# Create\
    \ benchmark instance\nbenchmark = Benchmark(config)\n\n# Define operations for\
    \ BIT with tuples\ndef tuple_add(a, b):\n    \"\"\"Addition operation for tuples\"\
    \"\"\n    return (a[0] + b[0], a[1] + b[1])\n\ndef tuple_sub(a, b):\n    \"\"\"\
    Subtraction operation for tuples\"\"\"\n    return (a[0] - b[0], a[1] - b[1])\n\
    \n# Data generator\n@benchmark.data_generator(\"default\")\ndef generate_bit2_data(size:\
    \ int, operation: str):\n    \"\"\"Generate test data for BIT2 operations\"\"\"\
    \n    # Generate random initial values\n    values_a = [random.randint(1, 1000)\
    \ for _ in range(size)]\n    values_b = [random.randint(1, 1000) for _ in range(size)]\n\
    \    \n    # Create tuple values for regular BIT\n    tuple_values = [(values_a[i],\
    \ values_b[i]) for i in range(size)]\n    \n    # Generate update operations\n\
    \    num_updates = min(1000, size // 10)\n    update_indices = [random.randint(0,\
    \ size - 1) for _ in range(num_updates)]\n    update_values_a = [random.randint(1,\
    \ 1000) for _ in range(num_updates)]\n    update_values_b = [random.randint(1,\
    \ 1000) for _ in range(num_updates)]\n    update_tuple_values = [(update_values_a[i],\
    \ update_values_b[i]) for i in range(num_updates)]\n    \n    # Generate query\
    \ ranges\n    num_queries = min(1000, size // 10)\n    query_ranges = []\n   \
    \ for _ in range(num_queries):\n        l = random.randint(0, size - 1)\n    \
    \    r = random.randint(l + 1, size)\n        query_ranges.append((l, r))\n  \
    \  \n    # Generate prefix indices\n    prefix_indices = [random.randint(1, size)\
    \ for _ in range(num_queries)]\n    \n    return {\n        'values_a': values_a,\n\
    \        'values_b': values_b,\n        'tuple_values': tuple_values,\n      \
    \  'update_indices': update_indices,\n        'update_values_a': update_values_a,\n\
    \        'update_values_b': update_values_b,\n        'update_tuple_values': update_tuple_values,\n\
    \        'query_ranges': query_ranges,\n        'prefix_indices': prefix_indices,\n\
    \        'size': size\n    }\n\n# Setup functions to prepare data and reduce overhead\
    \ during timing\n@benchmark.setup(\"default\")\ndef setup(data):\n    prepared\
    \ = data.copy()\n    return prepared\n\n# Construction operation\n@benchmark.implementation(\"\
    bit2_sum\", \"construction\")\ndef construction_bit2_sum(data):\n    \"\"\"Construct\
    \ BIT2 with sum operation\"\"\"\n    bit = BIT2(data['tuple_values'])\n    return\
    \ len(bit)\n\n@benchmark.implementation(\"tuple_bit_sum\", \"construction\")\n\
    def construction_tuple_bit_sum(data):\n    \"\"\"Construct BITMonoid with tuple\
    \ sum operation\"\"\"\n    bit = BITMonoid(tuple_add, (0, 0), data['tuple_values'])\n\
    \    return len(bit)\n\n# Point updates operation\n@benchmark.implementation(\"\
    bit2_sum\", \"point_updates\")\ndef point_updates_bit2_sum(data):\n    \"\"\"\
    Point updates on BIT2 with sum\"\"\"\n    bit = BIT2(data['size'])\n    checksum\
    \ = 0\n    indices = data['update_indices']\n    updates = data['update_tuple_values']\n\
    \    for j in range(len(indices)):\n        i = indices[j]\n        val = updates[j]\n\
    \        bit.set(i, val)\n        result = bit.get(i)\n        checksum ^= result[0]\
    \ ^ result[1]\n    return checksum\n\n@benchmark.implementation(\"tuple_bit_sum\"\
    , \"point_updates\")\ndef point_updates_tuple_bit_sum(data):\n    \"\"\"Point\
    \ updates on BITMonoid with tuples\"\"\"\n    bit = BITMonoid(tuple_add, (0, 0),\
    \ data['size'])\n    checksum = 0\n    indices = data['update_indices']\n    updates\
    \ = data['update_tuple_values']\n    for j in range(len(indices)):\n        i\
    \ = indices[j]\n        val = updates[j]\n        # Set element: add difference\
    \ between target and current\n        current = tuple_sub(bit.sum(i + 1), bit.sum(i))\n\
    \        bit.add(i, tuple_sub(val, current))\n        # Get element: reconstruct\
    \ from prefix sums\n        result = tuple_sub(bit.sum(i + 1), bit.sum(i))\n \
    \       checksum ^= result[0] ^ result[1]\n    return checksum\n\n# Prefix sums\
    \ operation\n@benchmark.implementation(\"bit2_sum\", \"prefix_sums\")\ndef prefix_sums_bit2_sum(data):\n\
    \    \"\"\"Prefix sums on BIT2 with sum\"\"\"\n    bit = BIT2(data['tuple_values'])\n\
    \    checksum = 0\n    for n in data['prefix_indices']:\n        result = bit.sum(n)\n\
    \        checksum ^= result[0] ^ result[1]\n    return checksum\n\n@benchmark.implementation(\"\
    tuple_bit_sum\", \"prefix_sums\")\ndef prefix_sums_tuple_bit_sum(data):\n    \"\
    \"\"Prefix sums on BITMonoid with tuples\"\"\"\n    bit = BITMonoid(tuple_add,\
    \ (0, 0), data['tuple_values'])\n    checksum = 0\n    for n in data['prefix_indices']:\n\
    \        result = bit.sum(n)\n        checksum ^= result[0] ^ result[1]\n    return\
    \ checksum\n\n# Range sums operation\n@benchmark.implementation(\"bit2_sum\",\
    \ \"range_sums\")\ndef range_sums_bit2_sum(data):\n    \"\"\"Range sums on BIT2\
    \ with sum\"\"\"\n    bit = BIT2(data['tuple_values'])\n    checksum = 0\n   \
    \ for l, r in data['query_ranges']:\n        result = bit.sum_range(l, r)\n  \
    \      checksum ^= result[0] ^ result[1]\n    return checksum\n\n@benchmark.implementation(\"\
    tuple_bit_sum\", \"range_sums\")\ndef range_sums_tuple_bit_sum(data):\n    \"\"\
    \"Range sums on BITMonoid with tuples\"\"\"\n    bit = BITMonoid(tuple_add, (0,\
    \ 0), data['tuple_values'])\n    checksum = 0\n    for l, r in data['query_ranges']:\n\
    \        # Range sum: sum(r) - sum(l)\n        result = tuple_sub(bit.sum(r),\
    \ bit.sum(l))\n        checksum ^= result[0] ^ result[1]\n    return checksum\n\
    \n# Mixed operations (updates + queries)\n@benchmark.implementation(\"bit2_sum\"\
    , \"mixed_ops\")\ndef mixed_ops_bit2_sum(data):\n    \"\"\"Mixed updates and queries\
    \ on BIT2\"\"\"\n    bit = BIT2(data['tuple_values'])\n    checksum = 0\n    \n\
    \    # Interleave updates and queries\n    query_ranges = data['query_ranges']\n\
    \    update_indices = data['update_indices']\n    update_tuple_values = data['update_tuple_values']\n\
    \    min_len = min(len(query_ranges), len(update_indices))\n    \n    for i in\
    \ range(min_len):\n        if i % 2 == 0:\n            # Range query\n       \
    \     l, r = query_ranges[i]\n            result = bit.sum_range(l, r)\n     \
    \       checksum ^= result[0] ^ result[1]\n        else:\n            # Update\n\
    \            idx = update_indices[i]\n            val = update_tuple_values[i]\n\
    \            bit.add(idx, val)\n            result = bit.get(idx)\n          \
    \  checksum ^= result[0] ^ result[1]\n    return checksum\n\n@benchmark.implementation(\"\
    tuple_bit_sum\", \"mixed_ops\")\ndef mixed_ops_tuple_bit_sum(data):\n    \"\"\"\
    Mixed updates and queries on BITMonoid\"\"\"\n    bit = BITMonoid(tuple_add, (0,\
    \ 0), data['tuple_values'])\n    checksum = 0\n    \n    # Interleave updates\
    \ and queries\n    query_ranges = data['query_ranges']\n    update_indices = data['update_indices']\n\
    \    update_tuple_values = data['update_tuple_values']\n    min_len = min(len(query_ranges),\
    \ len(update_indices))\n    \n    for i in range(min_len):\n        if i % 2 ==\
    \ 0:\n            # Range query\n            l, r = query_ranges[i]\n        \
    \    result = tuple_sub(bit.sum(r), bit.sum(l))\n            checksum ^= result[0]\
    \ ^ result[1]\n        else:\n            # Update\n            idx = update_indices[i]\n\
    \            val = update_tuple_values[i]\n            bit.add(idx, val)\n   \
    \         result = tuple_sub(bit.sum(idx + 1), bit.sum(idx))\n            checksum\
    \ ^= result[0] ^ result[1]\n    return checksum\n\nif __name__ == \"__main__\"\
    :\n    # Parse command line args and run appropriate mode\n    runner = benchmark.parse_args()\n\
    \    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/ds/tree/bit/bit2_cls.py
  - cp_library/ds/tree/bit/bit_monoid_cls.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/ds/list/list2_cls.py
  - cp_library/ds/tree/bit/bit_base_cls.py
  - cp_library/perf/checksum.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: false
  path: perf/bit2.py
  requiredBy: []
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/bit2.py
layout: document
redirect_from:
- /library/perf/bit2.py
- /library/perf/bit2.py.html
title: perf/bit2.py
---
