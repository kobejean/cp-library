---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/rint_fn.py
    title: cp_library/io/rint_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_3_a_tarjan_articulation_points.test.py
    title: test/grl_3_a_tarjan_articulation_points.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "def rint(shift=0, base=10):\n    return [int(x, base) + shift for\
    \ x in input().split()]\n\ndef read_graph(N, M, i0=1):\n    G = [[] for _ in range(N)]\n\
    \    for _ in range(M):\n        u,v = rint(-i0)\n        G[u].append(v)\n   \
    \     G[v].append(u)\n    return G\n"
  code: "from cp_library.io.rint_fn import rint\n\ndef read_graph(N, M, i0=1):\n \
    \   G = [[] for _ in range(N)]\n    for _ in range(M):\n        u,v = rint(-i0)\n\
    \        G[u].append(v)\n        G[v].append(u)\n    return G"
  dependsOn:
  - cp_library/io/rint_fn.py
  isVerificationFile: false
  path: cp_library/io/read_graph_fn.py
  requiredBy: []
  timestamp: '2024-09-05 11:18:10+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_3_a_tarjan_articulation_points.test.py
documentation_of: cp_library/io/read_graph_fn.py
layout: document
redirect_from:
- /library/cp_library/io/read_graph_fn.py
- /library/cp_library/io/read_graph_fn.py.html
title: cp_library/io/read_graph_fn.py
---
