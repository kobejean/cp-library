---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/bellman_ford_fn.py
    title: cp_library/alg/graph/bellman_ford_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_1_b_bellman_ford.test.py
    title: test/grl_1_b_bellman_ford.test.py
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
    from math import inf\n\ndef bellman_ford(G, N, root) -> tuple[bool, list[int]]:\n\
    \    \n    def bellman_ford(G, N, root) -> list[int]:\n        D = [inf]*N\n \
    \       D[root] = 0\n        for _ in range(N-1):\n            for u, edges in\
    \ enumerate(G):\n                for v,w in edges:\n                    D[v] =\
    \ min(D[v], D[u] + w)\n        return D\n    D = bellman_ford(G, N, root)\n  \
    \  neg_cycle = any(D[u]+w<D[v] for u, edges in enumerate(G) for v,w in edges)\n\
    \    return neg_cycle, D\n"
  code: "import cp_library.alg.graph.__header__\nfrom math import inf\n\ndef bellman_ford(G,\
    \ N, root) -> tuple[bool, list[int]]:\n    from cp_library.alg.graph.bellman_ford_fn\
    \ import bellman_ford\n    D = bellman_ford(G, N, root)\n    neg_cycle = any(D[u]+w<D[v]\
    \ for u, edges in enumerate(G) for v,w in edges)\n    return neg_cycle, D\n"
  dependsOn:
  - cp_library/alg/graph/bellman_ford_fn.py
  isVerificationFile: false
  path: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
  requiredBy: []
  timestamp: '2024-11-16 11:24:00+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_1_b_bellman_ford.test.py
documentation_of: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
- /library/cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py.html
title: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
---
