---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "def read_graph(N, M, i0=1):\n    G = [[] for _ in range(N)]\n    for\
    \ _ in range(M):\n        u,v,w = read(-i0)\n        w += i0\n        G[u].append((w,v))\n\
    \        G[v].append((w,u))\n    return G\n\n\ndef read(shift=0, base=10):\n \
    \   return [int(s, base) + shift for s in  input().split()]\n"
  code: "def read_graph(N, M, i0=1):\n    G = [[] for _ in range(N)]\n    for _ in\
    \ range(M):\n        u,v,w = read(-i0)\n        w += i0\n        G[u].append((w,v))\n\
    \        G[v].append((w,u))\n    return G\n\nfrom cp_library.io.read_int_fn import\
    \ read"
  dependsOn:
  - cp_library/io/read_int_fn.py
  isVerificationFile: false
  path: cp_library/io/read_graph_weighted_fn.py
  requiredBy: []
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/io/read_graph_weighted_fn.py
layout: document
redirect_from:
- /library/cp_library/io/read_graph_weighted_fn.py
- /library/cp_library/io/read_graph_weighted_fn.py.html
title: cp_library/io/read_graph_weighted_fn.py
---
