---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/grl_1_a_dijkstra.test.py
    title: test/grl_1_a_dijkstra.test.py
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
    import heapq\nfrom math import inf\n\ndef dijkstra(G, N, root) -> list[int]:\n\
    \    D = [inf for _ in range(N)]\n    D[root] = 0\n    q = [(0, root)]\n    while\
    \ q:\n        d, v = heapq.heappop(q)\n        if d > D[v]: continue\n\n     \
    \   for w, u in G[v]:\n            if (nd := d + w) < D[u]:\n                D[u]\
    \ = nd\n                heapq.heappush(q, (nd, u))\n    return D\n"
  code: "import cp_library.alg.graph.__header__\nimport heapq\nfrom math import inf\n\
    \ndef dijkstra(G, N, root) -> list[int]:\n    D = [inf for _ in range(N)]\n  \
    \  D[root] = 0\n    q = [(0, root)]\n    while q:\n        d, v = heapq.heappop(q)\n\
    \        if d > D[v]: continue\n\n        for w, u in G[v]:\n            if (nd\
    \ := d + w) < D[u]:\n                D[u] = nd\n                heapq.heappush(q,\
    \ (nd, u))\n    return D\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/dijkstra_fn.py
  requiredBy: []
  timestamp: '2024-09-21 16:44:49+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/grl_1_a_dijkstra.test.py
documentation_of: cp_library/alg/graph/dijkstra_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/dijkstra_fn.py
- /library/cp_library/alg/graph/dijkstra_fn.py.html
title: cp_library/alg/graph/dijkstra_fn.py
---
