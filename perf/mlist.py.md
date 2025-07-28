---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_ntt_cls.py
    title: cp_library/math/mod/mint_ntt_cls.py
  - icon: ':warning:'
    path: cp_library/math/mod/mlist_cls.py
    title: cp_library/math/mod/mlist_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/nt/mod_inv_fn.py
    title: cp_library/math/nt/mod_inv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/nt/ntt_cls.py
    title: cp_library/math/nt/ntt_cls.py
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
  code: "#!/usr/bin/env python3\n\"\"\"\nComprehensive benchmark comparing modular\
    \ arithmetic approaches on lists:\n1. Plain int list with manual modular operations\n\
    2. mlist_cls (optimized modular list)\n3. List of mint_cls (modular integers)\n\
    \nTests various operations to provide fair comparison across different use cases.\n\
    \"\"\"\n\nimport random\nimport sys\nimport os\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\
    \nfrom cp_library.perf.benchmark import Benchmark, BenchmarkConfig\nfrom cp_library.math.mod.mlist_cls\
    \ import mlist\nfrom cp_library.math.mod.mint_ntt_cls import mint\n\n# Setup modular\
    \ arithmetic with a common modulus\nMOD = 998244353\nmint.set_mod(MOD)\n\n# Configure\
    \ benchmark\nconfig = BenchmarkConfig(\n    name=\"mlist\",\n    sizes=[1000000,\
    \ 100000, 10000, 1000, 100, 10, 1],  # Reverse order to warm up JIT\n    operations=['construction',\
    \ 'addition', 'multiplication', 'mixed_ops', 'elementwise_mul', 'sum_all', 'conv'],\n\
    \    iterations=10,\n    warmup=3,\n    output_dir=\"./output/benchmark_results/mlist\"\
    \n)\n\n# Create benchmark instance\nbenchmark = Benchmark(config)\n\n# Data generators\n\
    @benchmark.data_generator(\"default\")\ndef generate_modular_data(size: int, operation:\
    \ str):\n    \"\"\"Generate test data for modular arithmetic operations\"\"\"\n\
    \    # Generate two random lists for operations\n    list1 = [random.randint(1,\
    \ MOD-1) for _ in range(size)]\n    list2 = [random.randint(1, MOD-1) for _ in\
    \ range(size)]\n    \n    # Pre-initialize data for fair timing (exclude initialization\
    \ overhead)\n    preinitialized = {\n        'list1_copy': list(list1),\n    \
    \    'list2_copy': list(list2),\n        'mlist1': mlist(list(list1)),\n     \
    \   'mlist2': mlist(list(list2)),\n        'mint_list1': [mint(x) for x in list1],\n\
    \        'mint_list2': [mint(x) for x in list2],\n        'result_buffer': [0]\
    \ * size,\n        'mlist_result': mlist(size),\n        'constant': 12345,\n\
    \        'mint_constant': mint(12345)\n    }\n    \n    return {\n        'list1':\
    \ list1,\n        'list2': list2,\n        'size': size,\n        'operation':\
    \ operation,\n        'mod': MOD,\n        'preinitialized': preinitialized\n\
    \    }\n\n# Construction operation\n@benchmark.implementation(\"int_list\", \"\
    construction\")\ndef construction_int_list(data):\n    \"\"\"Construct int list\
    \ from raw data\"\"\"\n    list1 = list(data['list1'])\n    list2 = list(data['list2'])\n\
    \    checksum = 0\n    for x in list1:\n        checksum ^= x\n    for x in list2:\n\
    \        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"mlist\"\
    , \"construction\")\ndef construction_mlist(data):\n    \"\"\"Construct mlist\
    \ from raw data\"\"\"\n    mlist1 = mlist(data['list1'])\n    mlist2 = mlist(data['list2'])\n\
    \    checksum = 0\n    for x in mlist1.data:\n        checksum ^= x\n    for x\
    \ in mlist2.data:\n        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"\
    mint_list\", \"construction\")\ndef construction_mint_list(data):\n    \"\"\"\
    Construct mint list from raw data\"\"\"\n    mint_list1 = [mint(x) for x in data['list1']]\n\
    \    mint_list2 = [mint(x) for x in data['list2']]\n    checksum = 0\n    for\
    \ x in mint_list1:\n        checksum ^= x\n    for x in mint_list2:\n        checksum\
    \ ^= x\n    return checksum\n\n# Addition operation\n@benchmark.implementation(\"\
    int_list\", \"addition\")\ndef addition_int_list(data):\n    \"\"\"Element-wise\
    \ addition with manual modulo\"\"\"\n    pre = data['preinitialized']\n    list1,\
    \ list2, mod = pre['list1_copy'], pre['list2_copy'], data['mod']\n    checksum\
    \ = 0\n    for i in range(data['size']):\n        checksum ^= (list1[i] + list2[i])\
    \ % mod\n    return checksum\n\n@benchmark.implementation(\"mlist\", \"addition\"\
    )\ndef addition_mlist(data):\n    \"\"\"Element-wise addition using mlist\"\"\"\
    \n    pre = data['preinitialized']\n    list1, list2 = pre['mlist1'], pre['mlist2']\n\
    \    checksum = 0\n    for i in range(data['size']):\n        checksum ^= list1[i]\
    \ + list2[i]\n    return checksum\n\n@benchmark.implementation(\"mint_list\",\
    \ \"addition\")\ndef addition_mint_list(data):\n    \"\"\"Element-wise addition\
    \ using mint list\"\"\"\n    pre = data['preinitialized']\n    list1, list2 =\
    \ pre['mint_list1'], pre['mint_list2']\n    checksum = 0\n    for i in range(data['size']):\n\
    \        checksum ^= list1[i] + list2[i]\n    return checksum\n\n# Multiplication\
    \ operation\n@benchmark.implementation(\"int_list\", \"multiplication\")\ndef\
    \ multiplication_int_list(data):\n    \"\"\"Element-wise multiplication with manual\
    \ modulo\"\"\"\n    pre = data['preinitialized']\n    list1, list2, mod = pre['list1_copy'],\
    \ pre['list2_copy'], data['mod']\n    checksum = 0\n    for i in range(data['size']):\n\
    \        checksum ^= (list1[i] * list2[i]) % mod\n    return checksum\n\n@benchmark.implementation(\"\
    mlist\", \"multiplication\")\ndef multiplication_mlist(data):\n    \"\"\"Element-wise\
    \ multiplication using mlist\"\"\"\n    pre = data['preinitialized']\n    list1,\
    \ list2 = pre['mlist1'], pre['mlist2']\n    checksum = 0\n    for i in range(data['size']):\n\
    \        checksum ^= list1[i] * list2[i]\n    return checksum\n\n@benchmark.implementation(\"\
    mint_list\", \"multiplication\")\ndef multiplication_mint_list(data):\n    \"\"\
    \"Element-wise multiplication using mint list\"\"\"\n    pre = data['preinitialized']\n\
    \    list1, list2 = pre['mint_list1'], pre['mint_list2']\n    checksum = 0\n \
    \   for i in range(data['size']):\n        checksum ^= list1[i] * list2[i]\n \
    \   return checksum\n\n# Mixed operations\n@benchmark.implementation(\"int_list\"\
    , \"mixed_ops\")\ndef mixed_ops_int_list(data):\n    \"\"\"Mix of addition, multiplication,\
    \ and subtraction\"\"\"\n    pre = data['preinitialized']\n    list1, list2, mod\
    \ = pre['list1_copy'], pre['list2_copy'], data['mod']\n    checksum = 0\n    for\
    \ i in range(data['size']):\n        if i % 3 == 0:\n            checksum ^= (list1[i]\
    \ + list2[i]) % mod\n        elif i % 3 == 1:\n            checksum ^= (list1[i]\
    \ * list2[i]) % mod\n        else:\n            checksum ^= (list1[i] - list2[i])\
    \ % mod\n    return checksum\n\n@benchmark.implementation(\"mlist\", \"mixed_ops\"\
    )\ndef mixed_ops_mlist(data):\n    \"\"\"Mix of operations using mlist\"\"\"\n\
    \    pre = data['preinitialized']\n    list1, list2 = pre['mlist1'], pre['mlist2']\n\
    \    checksum = 0\n    for i in range(data['size']):\n        if i % 3 == 0:\n\
    \            checksum ^= list1[i] + list2[i]\n        elif i % 3 == 1:\n     \
    \       checksum ^= list1[i] * list2[i]\n        else:\n            checksum ^=\
    \ list1[i] - list2[i]\n    return checksum\n\n@benchmark.implementation(\"mint_list\"\
    , \"mixed_ops\")\ndef mixed_ops_mint_list(data):\n    \"\"\"Mix of operations\
    \ using mint list\"\"\"\n    pre = data['preinitialized']\n    list1, list2 =\
    \ pre['mint_list1'], pre['mint_list2']\n    checksum = 0\n    for i in range(data['size']):\n\
    \        if i % 3 == 0:\n            checksum ^= list1[i] + list2[i]\n       \
    \ elif i % 3 == 1:\n            checksum ^= list1[i] * list2[i]\n        else:\n\
    \            checksum ^= list1[i] - list2[i]\n    return checksum\n\n\n@benchmark.implementation(\"\
    int_list_e\", \"mixed_ops\")\ndef mixed_ops_int_list(data):\n    \"\"\"Mix of\
    \ addition, multiplication, and subtraction\"\"\"\n    pre = data['preinitialized']\n\
    \    list1, list2, mod = pre['list1_copy'], pre['list2_copy'], data['mod']\n \
    \   checksum = 0\n    for i, x in enumerate(list1):\n        if i % 3 == 0:\n\
    \            checksum ^= (x + list2[i]) % mod\n        elif i % 3 == 1:\n    \
    \        checksum ^= (x * list2[i]) % mod\n        else:\n            checksum\
    \ ^= (x - list2[i]) % mod\n    return checksum\n\n@benchmark.implementation(\"\
    mlist_e\", \"mixed_ops\")\ndef mixed_ops_mlist(data):\n    \"\"\"Mix of operations\
    \ using mlist\"\"\"\n    pre = data['preinitialized']\n    list1, list2 = pre['mlist1'],\
    \ pre['mlist2']\n    checksum = 0\n    for i, x in enumerate(list1):\n       \
    \ if i % 3 == 0:\n            checksum ^= x + list2[i]\n        elif i % 3 ==\
    \ 1:\n            checksum ^= x * list2[i]\n        else:\n            checksum\
    \ ^= x - list2[i]\n    return checksum\n\n@benchmark.implementation(\"mint_list_e\"\
    , \"mixed_ops\")\ndef mixed_ops_mint_list(data):\n    \"\"\"Mix of operations\
    \ using mint list\"\"\"\n    pre = data['preinitialized']\n    list1, list2 =\
    \ pre['mint_list1'], pre['mint_list2']\n    checksum = 0\n    for i, x in enumerate(list1):\n\
    \        if i % 3 == 0:\n            checksum ^= x + list2[i]\n        elif i\
    \ % 3 == 1:\n            checksum ^= x * list2[i]\n        else:\n           \
    \ checksum ^= x - list2[i]\n    return checksum\n\n# Element-wise multiplication\
    \ by constant\n@benchmark.implementation(\"int_list\", \"elementwise_mul\")\n\
    def elementwise_mul_int_list(data):\n    \"\"\"Multiply each element by a constant\"\
    \"\"\n    pre = data['preinitialized']\n    list1, mod, constant = pre['list1_copy'],\
    \ data['mod'], pre['constant']\n    checksum = 0\n    for x in list1:\n      \
    \  checksum ^= (x * constant) % mod\n    return checksum\n\n@benchmark.implementation(\"\
    mlist\", \"elementwise_mul\")\ndef elementwise_mul_mlist(data):\n    \"\"\"Multiply\
    \ each element by a constant using mlist\"\"\"\n    pre = data['preinitialized']\n\
    \    list1, constant = pre['mlist1'], pre['mint_constant']\n    checksum = 0\n\
    \    for x in list1:\n        checksum ^= x * constant\n    return checksum\n\n\
    @benchmark.implementation(\"mint_list\", \"elementwise_mul\")\ndef elementwise_mul_mint_list(data):\n\
    \    \"\"\"Multiply each element by a constant using mint list\"\"\"\n    pre\
    \ = data['preinitialized']\n    list1, constant = pre['mint_list1'], pre['mint_constant']\n\
    \    checksum = 0\n    for x in list1:\n        result = x * constant\n      \
    \  checksum ^= result\n    return checksum\n\n# Sum all elements\n@benchmark.implementation(\"\
    int_list\", \"sum_all\")\ndef sum_all_int_list(data):\n    \"\"\"Sum all elements\"\
    \"\"\n    pre = data['preinitialized']\n    list1, mod = pre['list1_copy'], data['mod']\n\
    \    result = 0\n    for x in list1:\n        result = (result + x) % mod\n  \
    \  return result\n\n@benchmark.implementation(\"mlist\", \"sum_all\")\ndef sum_all_mlist(data):\n\
    \    \"\"\"Sum all elements using mlist\"\"\"\n    pre = data['preinitialized']\n\
    \    list1 = pre['mlist1']\n    result = mint(0)\n    for x in list1:\n      \
    \  result = result + x\n    return int(result)\n\n@benchmark.implementation(\"\
    mint_list\", \"sum_all\")\ndef sum_all_mint_list(data):\n    \"\"\"Sum all elements\
    \ using mint list\"\"\"\n    pre = data['preinitialized']\n    list1 = pre['mint_list1']\n\
    \    result = mint(0)\n    for x in list1:\n        result = result + x\n    return\
    \ int(result)\n\n# Convolution operation\n@benchmark.implementation(\"int_list\"\
    , \"conv\")\ndef conv_int_list(data):\n    \"\"\"Convolution using mint.ntt.conv\
    \ with int lists\"\"\"\n    pre = data['preinitialized']\n    list1, list2 = pre['list1_copy'],\
    \ pre['list2_copy']\n    # Use mint.ntt.conv for convolution\n    result = mint.ntt.conv(list1,\
    \ list2, len(list1) + len(list2) - 1)\n    checksum = 0\n    for x in result:\n\
    \        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"mlist\"\
    , \"conv\")\ndef conv_mlist(data):\n    \"\"\"Convolution using mlist.conv method\"\
    \"\"\n    pre = data['preinitialized']\n    mlist1, mlist2 = pre['mlist1'], pre['mlist2']\n\
    \    # Use mlist.conv method\n    result = mlist1.conv(mlist2, len(mlist1) + len(mlist2)\
    \ - 1)\n    checksum = 0\n    for x in result.data:\n        checksum ^= x\n \
    \   return checksum\n\n@benchmark.implementation(\"mint_list\", \"conv\")\ndef\
    \ conv_mint_list(data):\n    \"\"\"Convolution using mint.ntt.conv with mint lists\"\
    \"\"\n    pre = data['preinitialized']\n    mint_list1, mint_list2 = pre['mint_list1'],\
    \ pre['mint_list2']\n    # Convert to int lists, convolve, convert back\n    int_list1\
    \ = [int(x) for x in mint_list1]\n    int_list2 = [int(x) for x in mint_list2]\n\
    \    result_ints = mint.ntt.conv(int_list1, int_list2, len(int_list1) + len(int_list2)\
    \ - 1)\n    result = [mint(x) for x in result_ints]\n    checksum = 0\n    for\
    \ x in result:\n        checksum ^= x\n    return checksum\n\n@benchmark.implementation(\"\
    mint_list_direct\", \"conv\")\ndef conv_mint_list_direct(data):\n    \"\"\"Convolution\
    \ using mint.ntt.conv directly with mint lists\"\"\"\n    pre = data['preinitialized']\n\
    \    mint_list1, mint_list2 = pre['mint_list1'], pre['mint_list2']\n    result\
    \ = mint.ntt.conv(mint_list1, mint_list2, len(mint_list1) + len(mint_list2) -\
    \ 1)\n    checksum = 0\n    for x in result:\n        checksum ^= x\n    return\
    \ checksum\n\n# Custom validator for modular arithmetic results (now using XOR\
    \ checksums)\n@benchmark.validator(\"default\")\ndef validate_modular_result(expected,\
    \ actual):\n    \"\"\"Validate modular arithmetic results using XOR checksums\"\
    \"\"\n    try:\n        # Compare XOR checksums directly\n        return int(expected)\
    \ == int(actual)\n    except Exception:\n        return False\n\nif __name__ ==\
    \ \"__main__\":\n    # Parse command line args and run appropriate mode\n    runner\
    \ = benchmark.parse_args()\n    runner.run()"
  dependsOn:
  - cp_library/perf/benchmark.py
  - cp_library/math/mod/mlist_cls.py
  - cp_library/math/mod/mint_ntt_cls.py
  - cp_library/perf/interfaces.py
  - cp_library/perf/registry.py
  - cp_library/perf/orchestrator.py
  - cp_library/perf/timing.py
  - cp_library/perf/output.py
  - cp_library/perf/renderers.py
  - cp_library/perf/cli.py
  - cp_library/perf/checksum.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/nt/ntt_cls.py
  - cp_library/math/nt/mod_inv_fn.py
  isVerificationFile: false
  path: perf/mlist.py
  requiredBy: []
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: perf/mlist.py
layout: document
redirect_from:
- /library/perf/mlist.py
- /library/perf/mlist.py.html
title: perf/mlist.py
---
