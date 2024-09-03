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
  bundledCode: "import heapq\nfrom math import inf\n\ndef dijkstra(G, N, root) ->\
    \ list[int]:\n    D = [inf for _ in range(N)]\n    D[root] = 0\n    q = [(0, root)]\n\
    \    while q:\n        d, v = heapq.heappop(q)\n        if d > D[v]: continue\n\
    \n        for w, u in G[v]:\n            nd = d + w\n            if nd < D[u]:\n\
    \                D[u] = nd\n                heapq.heappush(q, (nd, u))\n    return\
    \ D\n"
  code: "import heapq\nfrom math import inf\n\ndef dijkstra(G, N, root) -> list[int]:\n\
    \    D = [inf for _ in range(N)]\n    D[root] = 0\n    q = [(0, root)]\n    while\
    \ q:\n        d, v = heapq.heappop(q)\n        if d > D[v]: continue\n\n     \
    \   for w, u in G[v]:\n            nd = d + w\n            if nd < D[u]:\n   \
    \             D[u] = nd\n                heapq.heappush(q, (nd, u))\n    return\
    \ D\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/dijkstra_fn.py
  requiredBy: []
  timestamp: '2024-09-03 23:33:52+09:00'
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
