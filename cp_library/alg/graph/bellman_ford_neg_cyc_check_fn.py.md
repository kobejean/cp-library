---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/alg/graph/bellman_ford_fn.py
    title: cp_library/alg/graph/bellman_ford_fn.py
  - icon: ':warning:'
    path: cp_library/math/inft_cnst.py
    title: cp_library/math/inft_cnst.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
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
  timestamp: '2024-12-17 21:59:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
- /library/cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py.html
title: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
---
