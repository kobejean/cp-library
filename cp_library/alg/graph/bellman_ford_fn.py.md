---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/math/inft_cnst.py
    title: cp_library/math/inft_cnst.py
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
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nimport sys\n\ninft = sys.maxsize\n\ndef bellman_ford(G, N, root) -> list[int]:\n\
    \    D = [inft]*N\n    D[root] = 0\n    for _ in range(N-1):\n        for u, edges\
    \ in enumerate(G):\n            for v,w in edges:\n                D[v] = min(D[v],\
    \ D[u] + w)\n    return D\n"
  code: "import cp_library.alg.graph.__header__\nfrom cp_library.math.inft_cnst import\
    \ inft\n\ndef bellman_ford(G, N, root) -> list[int]:\n    D = [inft]*N\n    D[root]\
    \ = 0\n    for _ in range(N-1):\n        for u, edges in enumerate(G):\n     \
    \       for v,w in edges:\n                D[v] = min(D[v], D[u] + w)\n    return\
    \ D\n"
  dependsOn:
  - cp_library/math/inft_cnst.py
  isVerificationFile: false
  path: cp_library/alg/graph/bellman_ford_fn.py
  requiredBy:
  - cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
  timestamp: '2024-11-28 18:07:28+09:00'
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
