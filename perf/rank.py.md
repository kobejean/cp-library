---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/rank/irank_fn.py
    title: cp_library/alg/iter/rank/irank_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/rank/irank_multi_fn.py
    title: cp_library/alg/iter/rank/irank_multi_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer3_cls.py
    title: cp_library/bit/pack/packer3_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nSimple ranking benchmark using the new declarative\
    \ framework.\nCompares irank vs irank_multi performance across different data\
    \ patterns.\n\"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0,\
    \ os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom cp_library.perf.benchmark\
    \ import Benchmark, BenchmarkConfig\nfrom cp_library.alg.iter.rank.irank_fn import\
    \ irank\nfrom cp_library.alg.iter.rank.irank_multi_fn import irank as irank_multi\n\
    \n# Configure benchmark\nconfig = BenchmarkConfig(\n    name=\"rank\",\n    sizes=[1000000,\
    \ 100000, 10000, 1000, 100, 10, 1],  # Reverse order to warm up JIT\n    operations=['construction',\
    \ 'random', 'sorted', 'duplicates', 'reverse'],\n    iterations=5,\n    warmup=3,\n\
    \    output_dir=\"./output/benchmark_results/rank\"\n)\n\n# Create benchmark instance\n\
    benchmark = Benchmark(config)\n\n# Data generator\n@benchmark.data_generator(\"\
    default\")\ndef generate_rank_data(size: int, operation: str):\n    \"\"\"Generate\
    \ ranking data in different patterns\"\"\"\n    if operation == 'random':\n  \
    \      data = [random.randint(1, size) for _ in range(size)]\n    elif operation\
    \ == 'sorted':\n        data = list(range(size))\n    elif operation == 'duplicates':\n\
    \        # Many duplicates (10% unique values)\n        unique_count = max(1,\
    \ size // 10)\n        data = [random.randint(1, unique_count) for _ in range(size)]\n\
    \    elif operation == 'reverse':\n        data = list(range(size, 0, -1))\n \
    \   else:\n        raise ValueError(f\"Unknown operation: {operation}\")\n   \
    \ \n    # Pre-initialize data for fair timing (exclude copy overhead)\n    preinitialized\
    \ = {\n        'data_copy1': list(data),\n        'data_copy2': list(data),\n\
    \        'distinct': False\n    }\n    \n    return {\n        'data': data,\n\
    \        'distinct': False,\n        'size': size,\n        'operation': operation,\n\
    \        'preinitialized': preinitialized\n    }\n\n# Construction operation\n\
    @benchmark.implementation(\"irank\", \"construction\")\ndef construction_irank(data):\n\
    \    \"\"\"Construct data copy for irank\"\"\"\n    data_copy = list(data['data'])\n\
    \    checksum = 0\n    for x in data_copy:\n        checksum ^= x\n    return\
    \ checksum\n\n@benchmark.implementation(\"irank_multi\", \"construction\")\ndef\
    \ construction_irank_multi(data):\n    \"\"\"Construct data copy for irank_multi\"\
    \"\"\n    data_copy = list(data['data'])\n    checksum = 0\n    for x in data_copy:\n\
    \        checksum ^= x\n    return checksum\n\n# Random operation\n@benchmark.implementation(\"\
    irank\", \"random\")\ndef random_irank(data):\n    \"\"\"Standard irank implementation\
    \ for random data\"\"\"\n    pre = data['preinitialized']\n    result = irank(pre['data_copy1'],\
    \ distinct=pre['distinct'])\n    checksum = 0\n    for x in result:\n        checksum\
    \ ^= x\n    return checksum\n\n@benchmark.implementation(\"irank_multi\", \"random\"\
    )\ndef random_irank_multi(data):\n    \"\"\"Multi-pass irank implementation for\
    \ random data\"\"\"\n    pre = data['preinitialized']\n    result = irank_multi(pre['data_copy2'],\
    \ distinct=pre['distinct'])\n    checksum = 0\n    for x in result:\n        checksum\
    \ ^= x\n    return checksum\n\n# Sorted operation\n@benchmark.implementation(\"\
    irank\", \"sorted\")\ndef sorted_irank(data):\n    \"\"\"Standard irank implementation\
    \ for sorted data\"\"\"\n    pre = data['preinitialized']\n    result = irank(pre['data_copy1'],\
    \ distinct=pre['distinct'])\n    checksum = 0\n    for x in result:\n        checksum\
    \ ^= x\n    return checksum\n\n@benchmark.implementation(\"irank_multi\", \"sorted\"\
    )\ndef sorted_irank_multi(data):\n    \"\"\"Multi-pass irank implementation for\
    \ sorted data\"\"\"\n    pre = data['preinitialized']\n    result = irank_multi(pre['data_copy2'],\
    \ distinct=pre['distinct'])\n    checksum = 0\n    for x in result:\n        checksum\
    \ ^= x\n    return checksum\n\n# Duplicates operation\n@benchmark.implementation(\"\
    irank\", \"duplicates\")\ndef duplicates_irank(data):\n    \"\"\"Standard irank\
    \ implementation for data with duplicates\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank(pre['data_copy1'], distinct=pre['distinct'])\n    checksum\
    \ = 0\n    for x in result:\n        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"\
    irank_multi\", \"duplicates\")\ndef duplicates_irank_multi(data):\n    \"\"\"\
    Multi-pass irank implementation for data with duplicates\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank_multi(pre['data_copy2'], distinct=pre['distinct'])\n    checksum\
    \ = 0\n    for x in result:\n        checksum ^= x\n    return checksum\n\n# Reverse\
    \ operation\n@benchmark.implementation(\"irank\", \"reverse\")\ndef reverse_irank(data):\n\
    \    \"\"\"Standard irank implementation for reverse data\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank(pre['data_copy1'], distinct=pre['distinct'])\n    checksum\
    \ = 0\n    for x in result:\n        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"\
    irank_multi\", \"reverse\")\ndef reverse_irank_multi(data):\n    \"\"\"Multi-pass\
    \ irank implementation for reverse data\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank_multi(pre['data_copy2'], distinct=pre['distinct'])\n    checksum\
    \ = 0\n    for x in result:\n        checksum ^= x\n    return checksum\n\n# Additional\
    \ benchmark with distinct=True\n@benchmark.data_generator(\"distinct\")\ndef generate_rank_data_distinct(size:\
    \ int, operation: str):\n    \"\"\"Generate ranking data with distinct=True\"\"\
    \"\n    base_data = generate_rank_data(size, operation)\n    base_data['distinct']\
    \ = True\n    base_data['preinitialized']['distinct'] = True\n    return base_data\n\
    \ndef irank_distinct_implementation(data):\n    \"\"\"irank with distinct=True\"\
    \"\"\n    pre = data['preinitialized']\n    result = irank(pre['data_copy1'],\
    \ distinct=True)\n    checksum = 0\n    for x in result:\n        checksum ^=\
    \ x\n    return checksum\n\ndef irank_multi_distinct_implementation(data):\n \
    \   \"\"\"irank_multi with distinct=True\"\"\"\n    pre = data['preinitialized']\n\
    \    result = irank_multi(pre['data_copy2'], distinct=True)\n    checksum = 0\n\
    \    for x in result:\n        checksum ^= x\n    return checksum\n\n# Custom\
    \ validator for rank results (now using XOR checksums)\n@benchmark.validator(\"\
    default\")\ndef validate_rank_result(expected, actual):\n    \"\"\"Validate ranking\
    \ results using XOR checksums\"\"\"\n    try:\n        # Compare XOR checksums\
    \ directly\n        return int(expected) == int(actual)\n    except Exception:\n\
    \        return False\n\nif __name__ == \"__main__\":\n    # Parse command line\
    \ args and run appropriate mode\n    runner = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/alg/iter/rank/irank_fn.py
  - cp_library/alg/iter/rank/irank_multi_fn.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/bit/pack/packer3_cls.py
  - cp_library/perf/checksum.py
  isVerificationFile: false
  path: perf/rank.py
  requiredBy: []
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/rank.py
layout: document
redirect_from:
- /library/perf/rank.py
- /library/perf/rank.py.html
title: perf/rank.py
---
