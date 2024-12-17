---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/digraph_weighted_cls.py
    title: cp_library/alg/graph/fast/digraph_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/graph_weighted_base_cls.py
    title: cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/graph_weighted_cls.py
    title: cp_library/alg/graph/fast/graph_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/iter/sort_parallel_fn.py
    title: cp_library/alg/iter/sort_parallel_fn.py
  - icon: ':warning:'
    path: cp_library/alg/tree/fast/tree_weighted_base_cls.py
    title: cp_library/alg/tree/fast/tree_weighted_base_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/fast/tree_weighted_cls.py
    title: cp_library/alg/tree/fast/tree_weighted_cls.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \ndef argsort(A: list[int]):\n    N = len(A)\n    mask = (1 << (shift := N.bit_length()))\
    \ - 1\n    indices = [0]*N\n    for i in range(N):\n        indices[i] = A[i]\
    \ << shift | i\n    indices.sort()\n    for i in range(N):\n        indices[i]\
    \ &= mask\n    return indices\n"
  code: "import cp_library.alg.iter.__header__\n\ndef argsort(A: list[int]):\n   \
    \ N = len(A)\n    mask = (1 << (shift := N.bit_length())) - 1\n    indices = [0]*N\n\
    \    for i in range(N):\n        indices[i] = A[i] << shift | i\n    indices.sort()\n\
    \    for i in range(N):\n        indices[i] &= mask\n    return indices\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/argsort_fn.py
  requiredBy:
  - cp_library/alg/iter/sort_parallel_fn.py
  - cp_library/alg/tree/fast/tree_weighted_cls.py
  - cp_library/alg/tree/fast/tree_weighted_base_cls.py
  - cp_library/alg/graph/fast/graph_weighted_cls.py
  - cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - cp_library/alg/graph/fast/digraph_weighted_cls.py
  timestamp: '2024-12-17 23:23:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/iter/argsort_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/argsort_fn.py
- /library/cp_library/alg/iter/argsort_fn.py.html
title: cp_library/alg/iter/argsort_fn.py
---
