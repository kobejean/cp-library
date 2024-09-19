---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
    title: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_1_c_floyd_warshall.test.py
    title: test/grl_1_c_floyd_warshall.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "from math import inf\n\ndef floyd_warshall(G, N) -> list[int]:\n \
    \   D = [[inf]*N for _ in range(N)]\n\n    for u, edges in enumerate(G):\n   \
    \     D[u][u] = 0\n        for w,v in edges:\n            D[u][v] = min(D[u][v],\
    \ w)\n    \n    for k, Dk in enumerate(D):\n        for i, Di in enumerate(D):\n\
    \            for j in range(i):\n                Di[j] = D[j][i] = min(Di[j],\
    \ Di[k]+Dk[j])\n    return D\n"
  code: "from math import inf\n\ndef floyd_warshall(G, N) -> list[int]:\n    D = [[inf]*N\
    \ for _ in range(N)]\n\n    for u, edges in enumerate(G):\n        D[u][u] = 0\n\
    \        for w,v in edges:\n            D[u][v] = min(D[u][v], w)\n    \n    for\
    \ k, Dk in enumerate(D):\n        for i, Di in enumerate(D):\n            for\
    \ j in range(i):\n                Di[j] = D[j][i] = min(Di[j], Di[k]+Dk[j])\n\
    \    return D"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/floyd_warshall_fn.py
  requiredBy:
  - cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  timestamp: '2024-09-20 03:21:05+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_1_c_floyd_warshall.test.py
documentation_of: cp_library/alg/graph/floyd_warshall_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/floyd_warshall_fn.py
- /library/cp_library/alg/graph/floyd_warshall_fn.py.html
title: cp_library/alg/graph/floyd_warshall_fn.py
---
