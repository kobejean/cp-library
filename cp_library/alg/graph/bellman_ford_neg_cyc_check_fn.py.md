---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/bellman_ford_fn.py
    title: cp_library/alg/graph/bellman_ford_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/inft_cnst.py
    title: cp_library/math/inft_cnst.py
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
    \nimport sys\ninft: int\n\ninft = sys.maxsize\n\ndef bellman_ford(G, N, root)\
    \ -> tuple[bool, list[int]]:\n    \n    def bellman_ford(G, N, root) -> list[int]:\n\
    \        D = [inft]*N\n        D[root] = 0\n        for _ in range(N-1):\n   \
    \         for u, edges in enumerate(G):\n                if D[u] == inft: continue\n\
    \                for v,w in edges:\n                    D[v] = min(D[v], D[u]\
    \ + w)\n        return D\n    D = bellman_ford(G, N, root)\n    neg_cycle = any(D[u]+w<D[v]\
    \ for u, edges in enumerate(G) for v,w in edges if D[u] != inft)\n    return neg_cycle,\
    \ D\n"
  code: "import cp_library.alg.graph.__header__\nfrom cp_library.math.inft_cnst import\
    \ inft\n\ndef bellman_ford(G, N, root) -> tuple[bool, list[int]]:\n    from cp_library.alg.graph.bellman_ford_fn\
    \ import bellman_ford\n    D = bellman_ford(G, N, root)\n    neg_cycle = any(D[u]+w<D[v]\
    \ for u, edges in enumerate(G) for v,w in edges if D[u] != inft)\n    return neg_cycle,\
    \ D\n"
  dependsOn:
  - cp_library/math/inft_cnst.py
  - cp_library/alg/graph/bellman_ford_fn.py
  isVerificationFile: false
  path: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
  requiredBy: []
  timestamp: '2024-12-18 14:55:02+09:00'
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
