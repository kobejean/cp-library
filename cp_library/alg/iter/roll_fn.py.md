---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/func_graph_cls.py
    title: cp_library/alg/graph/func_graph_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/mut_perm_graph_cls.py
    title: cp_library/alg/graph/mut_perm_graph_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/partial_func_graph_cls.py
    title: cp_library/alg/graph/partial_func_graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/perm_graph_cls.py
    title: cp_library/alg/graph/perm_graph_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc175_d_permutation.test.py
    title: test/atcoder/abc/abc175_d_permutation.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \ndef roll(A: list, t: int):\n    if t:=t%len(A): A[:t], A[t:] = A[-t:], A[:-t]\n\
    \    return A\n"
  code: "import cp_library.alg.iter.__header__\n\ndef roll(A: list, t: int):\n   \
    \ if t:=t%len(A): A[:t], A[t:] = A[-t:], A[:-t]\n    return A\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/roll_fn.py
  requiredBy:
  - cp_library/alg/graph/func_graph_cls.py
  - cp_library/alg/graph/partial_func_graph_cls.py
  - cp_library/alg/graph/mut_perm_graph_cls.py
  - cp_library/alg/graph/perm_graph_cls.py
  timestamp: '2025-03-02 23:16:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc175_d_permutation.test.py
documentation_of: cp_library/alg/iter/roll_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/roll_fn.py
- /library/cp_library/alg/iter/roll_fn.py.html
title: cp_library/alg/iter/roll_fn.py
---
