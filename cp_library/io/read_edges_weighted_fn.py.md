---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/io/rint_fn.py
    title: cp_library/io/rint_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/grl_2_a_kruskal_heap.test.py
    title: test/grl_2_a_kruskal_heap.test.py
  - icon: ':x:'
    path: test/grl_2_a_kruskal_sort.test.py
    title: test/grl_2_a_kruskal_sort.test.py
  - icon: ':x:'
    path: test/grl_2_b_edmonds_branching.test.py
    title: test/grl_2_b_edmonds_branching.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "def rint(shift=0, base=10):\n    return [int(x, base) + shift for\
    \ x in input().split()]\n\ndef read_edges(M, i0=1):\n    E = []\n    for _ in\
    \ range(M):\n        u,v,w = rint(-i0)\n        w += i0\n        E.append((w,u,v))\n\
    \    return E\n"
  code: "from cp_library.io.rint_fn import rint\n\ndef read_edges(M, i0=1):\n    E\
    \ = []\n    for _ in range(M):\n        u,v,w = rint(-i0)\n        w += i0\n \
    \       E.append((w,u,v))\n    return E"
  dependsOn:
  - cp_library/io/rint_fn.py
  isVerificationFile: false
  path: cp_library/io/read_edges_weighted_fn.py
  requiredBy: []
  timestamp: '2024-09-03 19:30:15+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/grl_2_a_kruskal_sort.test.py
  - test/grl_2_b_edmonds_branching.test.py
  - test/grl_2_a_kruskal_heap.test.py
documentation_of: cp_library/io/read_edges_weighted_fn.py
layout: document
redirect_from:
- /library/cp_library/io/read_edges_weighted_fn.py
- /library/cp_library/io/read_edges_weighted_fn.py.html
title: cp_library/io/read_edges_weighted_fn.py
---
