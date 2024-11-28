---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/fast_graph_cls.py
    title: cp_library/alg/graph/fast/fast_graph_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/shortest_path_static_graph_weighted.test.py
    title: test/shortest_path_static_graph_weighted.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
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
  - cp_library/alg/graph/fast/fast_graph_cls.py
  timestamp: '2024-11-28 19:02:10+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/shortest_path_static_graph_weighted.test.py
documentation_of: cp_library/ds/fill_fn.py
layout: document
redirect_from:
- /library/cp_library/ds/fill_fn.py
- /library/cp_library/ds/fill_fn.py.html
title: cp_library/ds/fill_fn.py
---
