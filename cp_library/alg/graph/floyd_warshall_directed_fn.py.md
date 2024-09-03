---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
    title: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/grl_1_c_floyd_warshall.test.py
    title: test/grl_1_c_floyd_warshall.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "from math import inf\n\ndef floyd_warshall(G, N) -> list[int]:\n \
    \   D = [[inf]*N for _ in range(N)]\n\n    for u, edges in enumerate(G):\n   \
    \     D[u][u] = 0\n        for w,v in edges:\n            D[u][v] = min(D[u][v],\
    \ w)\n    \n    for k, Dk in enumerate(D):\n        for Di in D:\n           \
    \ for j in range(N):\n                Di[j] = min(Di[j], Di[k]+Dk[j])\n    return\
    \ D\n"
  code: "from math import inf\n\ndef floyd_warshall(G, N) -> list[int]:\n    D = [[inf]*N\
    \ for _ in range(N)]\n\n    for u, edges in enumerate(G):\n        D[u][u] = 0\n\
    \        for w,v in edges:\n            D[u][v] = min(D[u][v], w)\n    \n    for\
    \ k, Dk in enumerate(D):\n        for Di in D:\n            for j in range(N):\n\
    \                Di[j] = min(Di[j], Di[k]+Dk[j])\n    return D"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/floyd_warshall_directed_fn.py
  requiredBy:
  - cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  timestamp: '2024-09-03 19:30:15+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/grl_1_c_floyd_warshall.test.py
documentation_of: cp_library/alg/graph/floyd_warshall_directed_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/floyd_warshall_directed_fn.py
- /library/cp_library/alg/graph/floyd_warshall_directed_fn.py.html
title: cp_library/alg/graph/floyd_warshall_directed_fn.py
---
