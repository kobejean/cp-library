---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
    title: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/grl_1_b_bellman_ford.test.py
    title: test/grl_1_b_bellman_ford.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "from math import inf\n\ndef bellman_ford(G, N, root) -> list[int]:\n\
    \    D = [inf]*N\n    D[root] = 0\n    for _ in range(N-1):\n        for u, edges\
    \ in enumerate(G):\n            for w, v in edges:\n                D[v] = min(D[v],\
    \ D[u] + w)\n    return D\n"
  code: "from math import inf\n\ndef bellman_ford(G, N, root) -> list[int]:\n    D\
    \ = [inf]*N\n    D[root] = 0\n    for _ in range(N-1):\n        for u, edges in\
    \ enumerate(G):\n            for w, v in edges:\n                D[v] = min(D[v],\
    \ D[u] + w)\n    return D\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/bellman_ford_fn.py
  requiredBy:
  - cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
  timestamp: '2024-09-03 19:30:15+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/grl_1_b_bellman_ford.test.py
documentation_of: cp_library/alg/graph/bellman_ford_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/bellman_ford_fn.py
- /library/cp_library/alg/graph/bellman_ford_fn.py.html
title: cp_library/alg/graph/bellman_ford_fn.py
---
