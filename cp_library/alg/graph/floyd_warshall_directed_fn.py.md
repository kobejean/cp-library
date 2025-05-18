---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
    title: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_1_c_floyd_warshall.test.py
    title: test/aoj/grl/grl_1_c_floyd_warshall.test.py
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
    from math import inf\n\ndef floyd_warshall(G, N) -> list[list[int]]:\n    D =\
    \ [[inf]*N for _ in range(N)]\n\n    for u, edges in enumerate(G):\n        D[u][u]\
    \ = 0\n        for v,w in edges:\n            D[u][v] = min(D[u][v], w)\n    \n\
    \    for k, Dk in enumerate(D):\n        for Di in D:\n            if Di[k] ==\
    \ inf: continue\n            for j in range(N):\n                if Dk[j] == inf:\
    \ continue\n                Di[j] = min(Di[j], Di[k]+Dk[j])\n    return D\n"
  code: "import cp_library.alg.graph.__header__\nfrom math import inf\n\ndef floyd_warshall(G,\
    \ N) -> list[list[int]]:\n    D = [[inf]*N for _ in range(N)]\n\n    for u, edges\
    \ in enumerate(G):\n        D[u][u] = 0\n        for v,w in edges:\n         \
    \   D[u][v] = min(D[u][v], w)\n    \n    for k, Dk in enumerate(D):\n        for\
    \ Di in D:\n            if Di[k] == inf: continue\n            for j in range(N):\n\
    \                if Dk[j] == inf: continue\n                Di[j] = min(Di[j],\
    \ Di[k]+Dk[j])\n    return D"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/floyd_warshall_directed_fn.py
  requiredBy:
  - cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  timestamp: '2025-05-19 01:45:33+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_1_c_floyd_warshall.test.py
documentation_of: cp_library/alg/graph/floyd_warshall_directed_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/floyd_warshall_directed_fn.py
- /library/cp_library/alg/graph/floyd_warshall_directed_fn.py.html
title: cp_library/alg/graph/floyd_warshall_directed_fn.py
---
