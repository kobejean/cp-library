---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_1_a_dijkstra.test.py
    title: test/grl_1_a_dijkstra.test.py
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
    import heapq\nfrom math import inf\n\ndef dijkstra(G, N, root) -> list[int]:\n\
    \    D = [inf for _ in range(N)]\n    D[root] = 0\n    q = [(0, root)]\n    while\
    \ q:\n        d, u = heapq.heappop(q)\n        if d > D[u]: continue\n\n     \
    \   for v,w in G[u]:\n            if (nd := d + w) < D[v]:\n                D[v]\
    \ = nd\n                heapq.heappush(q, (nd, v))\n    return D\n"
  code: "import cp_library.alg.graph.__header__\nimport heapq\nfrom math import inf\n\
    \ndef dijkstra(G, N, root) -> list[int]:\n    D = [inf for _ in range(N)]\n  \
    \  D[root] = 0\n    q = [(0, root)]\n    while q:\n        d, u = heapq.heappop(q)\n\
    \        if d > D[u]: continue\n\n        for v,w in G[u]:\n            if (nd\
    \ := d + w) < D[v]:\n                D[v] = nd\n                heapq.heappush(q,\
    \ (nd, v))\n    return D\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/dijkstra_fn.py
  requiredBy: []
  timestamp: '2024-09-28 04:04:21+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_1_a_dijkstra.test.py
documentation_of: cp_library/alg/graph/dijkstra_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/dijkstra_fn.py
- /library/cp_library/alg/graph/dijkstra_fn.py.html
title: cp_library/alg/graph/dijkstra_fn.py
---
