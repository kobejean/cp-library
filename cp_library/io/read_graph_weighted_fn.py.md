---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/io/rint_fn.py
    title: cp_library/io/rint_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "def rint(shift=0, base=10):\n    return [int(x, base) + shift for\
    \ x in input().split()]\n\ndef read_graph(N, M, i0=1):\n    G = [[] for _ in range(N)]\n\
    \    for _ in range(M):\n        u,v,w = rint(-i0)\n        w += i0\n        G[u].append((w,v))\n\
    \        G[v].append((w,u))\n    return G\n"
  code: "from cp_library.io.rint_fn import rint\n\ndef read_graph(N, M, i0=1):\n \
    \   G = [[] for _ in range(N)]\n    for _ in range(M):\n        u,v,w = rint(-i0)\n\
    \        w += i0\n        G[u].append((w,v))\n        G[v].append((w,u))\n   \
    \ return G"
  dependsOn:
  - cp_library/io/rint_fn.py
  isVerificationFile: false
  path: cp_library/io/read_graph_weighted_fn.py
  requiredBy: []
  timestamp: '2024-09-03 19:30:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/io/read_graph_weighted_fn.py
layout: document
redirect_from:
- /library/cp_library/io/read_graph_weighted_fn.py
- /library/cp_library/io/read_graph_weighted_fn.py.html
title: cp_library/io/read_graph_weighted_fn.py
---
