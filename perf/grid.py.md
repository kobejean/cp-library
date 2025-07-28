---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/grid/grid_cls.py
    title: cp_library/ds/grid/grid_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view_cls.py
    title: cp_library/ds/view/view_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nSimple Grid benchmark - minimal overhead,\
    \ focused on core operations.\n\"\"\"\n\nimport random\nimport sys\nimport os\n\
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig\nfrom cp_library.perf.checksum\
    \ import update_checksum\nfrom cp_library.ds.grid.grid_cls import Grid\n\nconfig\
    \ = BenchmarkConfig(\n    name=\"grid\",\n    sizes=[10000000, 1000000, 100000,\
    \ 10000, 1000, 100],\n    operations=['construction', 'random_access', 'row_access',\
    \ 'sequential_access'],\n    iterations=10,\n    warmup=2,\n    output_dir=\"\
    ./output/benchmark_results/grid\"\n)\n\nbenchmark = Benchmark(config)\n\n@benchmark.data_generator(\"\
    default\")\ndef generate_data(size: int, _: str):\n    H = int(size ** 0.5)\n\
    \    W = size // H\n    \n    data = [[random.randint(1, 1000000) for _ in range(W)]\
    \ for _ in range(H)]\n    flat = [val for row in data for val in row]\n    \n\
    \    return {\n        'grid': Grid(H, W, data),\n        'lists': data,\n   \
    \     'flat': flat,\n        'H': H, 'W': W,\n        'coords': [(random.randint(0,\
    \ H-1), random.randint(0, W-1)) for _ in range(min(100, size))]\n    }\n\n# Construction\n\
    @benchmark.implementation(\"grid\", \"construction\")\ndef construction_grid(data):\n\
    \    H, W = data['H'], data['W']\n    grid = Grid(H, W, data['flat'])\n    result\
    \ = 0\n    for i in range(H):\n        for j in range(W):\n            result\
    \ = update_checksum(result, grid(i, j))\n    return result\n\n@benchmark.implementation(\"\
    lists\", \"construction\")\ndef construction_lists(data):\n    H, W = data['H'],\
    \ data['W']\n    lists = [row[:] for row in data['lists']]\n    result = 0\n \
    \   for i in range(H):\n        for j in range(W):\n            result = update_checksum(result,\
    \ lists[i][j])\n    return result\n\n@benchmark.implementation(\"flat\", \"construction\"\
    )\ndef construction_flat(data):\n    H, W = data['H'], data['W']\n    flat = data['flat'][:]\n\
    \    result = 0\n    for i in range(H):\n        for j in range(W):\n        \
    \    result = update_checksum(result, flat[i * W + j])\n    return result\n\n\
    # Random access\n@benchmark.implementation(\"grid\", \"random_access\")\ndef random_access_grid(data):\n\
    \    grid = data['grid']\n    result = 0\n    for i, j in data['coords']:\n  \
    \      result = update_checksum(result, grid(i, j))\n    return result\n\n@benchmark.implementation(\"\
    lists\", \"random_access\")\ndef random_access_lists(data):\n    lists = data['lists']\n\
    \    result = 0\n    for i, j in data['coords']:\n        result = update_checksum(result,\
    \ lists[i][j])\n    return result\n\n@benchmark.implementation(\"flat\", \"random_access\"\
    )\ndef random_access_flat(data):\n    flat, W = data['flat'], data['W']\n    result\
    \ = 0\n    for i, j in data['coords']:\n        result = update_checksum(result,\
    \ flat[i * W + j])\n    return result\n\n# Row access\n@benchmark.implementation(\"\
    grid\", \"row_access\")\ndef row_access_grid(data):\n    H, W = data['H'], data['W']\n\
    \    grid = data['grid']\n    return sum(W for i in range(H) if grid[i])  # Count\
    \ logical width\n\n@benchmark.implementation(\"lists\", \"row_access\")\ndef row_access_lists(data):\n\
    \    H = data['H']\n    lists = data['lists']\n    return sum(len(lists[i]) for\
    \ i in range(H))\n\n@benchmark.implementation(\"flat\", \"row_access\")\ndef row_access_flat(data):\n\
    \    H, W = data['H'], data['W']\n    flat = data['flat']\n    return sum(len(flat[i\
    \ * W:(i + 1) * W]) for i in range(H))\n\n# Sequential access\n@benchmark.implementation(\"\
    grid\", \"sequential_access\")\ndef sequential_access_grid(data):\n    H, W =\
    \ data['H'], data['W']\n    grid = data['grid']\n    result = 0\n    for i in\
    \ range(H):\n        for j in range(W):\n            result = update_checksum(result,\
    \ grid(i, j))\n    return result\n\n@benchmark.implementation(\"lists\", \"sequential_access\"\
    )\ndef sequential_access_lists(data):\n    H, W = data['H'], data['W']\n    lists\
    \ = data['lists']\n    result = 0\n    for i in range(H):\n        for j in range(W):\n\
    \            result = update_checksum(result, lists[i][j])\n    return result\n\
    \n@benchmark.implementation(\"flat\", \"sequential_access\")\ndef sequential_access_flat(data):\n\
    \    H, W = data['H'], data['W']\n    flat = data['flat']\n    result = 0\n  \
    \  for i in range(H):\n        for j in range(W):\n            result = update_checksum(result,\
    \ flat[i * W + j])\n    return result\n\nif __name__ == \"__main__\":\n    # Parse\
    \ command line args and run appropriate mode\n    runner = benchmark.parse_args()\n\
    \    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/perf/checksum.py
  - cp_library/ds/grid/grid_cls.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/io/parsable_cls.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/ds/view/view_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: false
  path: perf/grid.py
  requiredBy: []
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/grid.py
layout: document
redirect_from:
- /library/perf/grid.py
- /library/perf/grid.py.html
title: perf/grid.py
---
