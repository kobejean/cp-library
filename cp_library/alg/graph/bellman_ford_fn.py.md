---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
    title: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_1_b_bellman_ford.test.py
    title: test/aoj/grl/grl_1_b_bellman_ford.test.py
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
    from math import inf\n\ndef bellman_ford(G, N, root) -> list[int]:\n    D = [inf]*N\n\
    \    D[root] = 0\n    for _ in range(N-1):\n        for u, edges in enumerate(G):\n\
    \            if D[u] == inf: continue\n            for v,w in edges:\n       \
    \         D[v] = min(D[v], D[u] + w)\n    return D\n"
  code: "import cp_library.alg.graph.__header__\nfrom math import inf\n\ndef bellman_ford(G,\
    \ N, root) -> list[int]:\n    D = [inf]*N\n    D[root] = 0\n    for _ in range(N-1):\n\
    \        for u, edges in enumerate(G):\n            if D[u] == inf: continue\n\
    \            for v,w in edges:\n                D[v] = min(D[v], D[u] + w)\n \
    \   return D\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/bellman_ford_fn.py
  requiredBy:
  - cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
  timestamp: '2025-04-28 05:45:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_1_b_bellman_ford.test.py
documentation_of: cp_library/alg/graph/bellman_ford_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/bellman_ford_fn.py
- /library/cp_library/alg/graph/bellman_ford_fn.py.html
title: cp_library/alg/graph/bellman_ford_fn.py
---
