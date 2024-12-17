---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/digraph_cls.py
    title: cp_library/alg/graph/fast/digraph_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/digraph_weighted_cls.py
    title: cp_library/alg/graph/fast/digraph_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/graph_base_cls.py
    title: cp_library/alg/graph/fast/graph_base_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/graph_cls.py
    title: cp_library/alg/graph/fast/graph_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/graph_weighted_base_cls.py
    title: cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/graph_weighted_cls.py
    title: cp_library/alg/graph/fast/graph_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/grid_graph_base_cls.py
    title: cp_library/alg/graph/fast/grid_graph_base_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/grid_graph_cls.py
    title: cp_library/alg/graph/fast/grid_graph_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/grid_graph_walled_base_cls.py
    title: cp_library/alg/graph/fast/grid_graph_walled_base_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/fast/tree_base_cls.py
    title: cp_library/alg/tree/fast/tree_base_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/fast/tree_cls.py
    title: cp_library/alg/tree/fast/tree_cls.py
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
  bundledCode: "from array import array\n\ndef fill_i32(N: int, elm: int = 0):\n \
    \   return array('i', (elm,)) * N\n\ndef fill_u32(N: int, elm: int = 0):\n   \
    \ return array('I', (elm,)) * N\n\ndef fill_i64(N: int, elm: int = 0):\n    return\
    \ array('q', (elm,)) * N\n\ndef fill_u64(N: int, elm: int = 0):\n    return array('Q',\
    \ (elm,)) * N\n"
  code: "from array import array\n\ndef fill_i32(N: int, elm: int = 0):\n    return\
    \ array('i', (elm,)) * N\n\ndef fill_u32(N: int, elm: int = 0):\n    return array('I',\
    \ (elm,)) * N\n\ndef fill_i64(N: int, elm: int = 0):\n    return array('q', (elm,))\
    \ * N\n\ndef fill_u64(N: int, elm: int = 0):\n    return array('Q', (elm,)) *\
    \ N"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/fill_fn.py
  requiredBy:
  - cp_library/alg/tree/fast/tree_weighted_cls.py
  - cp_library/alg/tree/fast/tree_base_cls.py
  - cp_library/alg/tree/fast/tree_weighted_base_cls.py
  - cp_library/alg/tree/fast/tree_cls.py
  - cp_library/alg/graph/fast/graph_cls.py
  - cp_library/alg/graph/fast/graph_weighted_cls.py
  - cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - cp_library/alg/graph/fast/digraph_weighted_cls.py
  - cp_library/alg/graph/fast/grid_graph_base_cls.py
  - cp_library/alg/graph/fast/grid_graph_walled_base_cls.py
  - cp_library/alg/graph/fast/graph_base_cls.py
  - cp_library/alg/graph/fast/digraph_cls.py
  - cp_library/alg/graph/fast/grid_graph_cls.py
  timestamp: '2024-12-17 23:23:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/fill_fn.py
layout: document
redirect_from:
- /library/cp_library/ds/fill_fn.py
- /library/cp_library/ds/fill_fn.py.html
title: cp_library/ds/fill_fn.py
---
