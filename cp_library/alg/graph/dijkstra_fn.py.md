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
    \nfrom heapq import heappop, heappush\nfrom typing import overload\nfrom math\
    \ import inf\n\n@overload\ndef dijkstra(G, s: int = 0) -> list[int]: ...\n@overload\n\
    def dijkstra(G, s: int, g: int) -> int: ...\ndef dijkstra(G, s = 0, g: int|None\
    \ = None):\n    N = len(G)\n    D = [inf for _ in range(N)]\n    D[s] = 0\n  \
    \  q = [(0, s)]\n    while q:\n        d, v = heappop(q)\n        if d > D[v]:\
    \ continue\n        if v == g: return d\n        for u, w, *_ in G[v]:\n     \
    \       if (nd := d + w) < D[u]:\n                D[u] = nd\n                heappush(q,\
    \ (nd, u))\n    return D if g is None else inf\n"
  code: "import cp_library.alg.graph.__header__\n\nfrom heapq import heappop, heappush\n\
    from typing import overload\nfrom math import inf\n\n@overload\ndef dijkstra(G,\
    \ s: int = 0) -> list[int]: ...\n@overload\ndef dijkstra(G, s: int, g: int) ->\
    \ int: ...\ndef dijkstra(G, s = 0, g: int|None = None):\n    N = len(G)\n    D\
    \ = [inf for _ in range(N)]\n    D[s] = 0\n    q = [(0, s)]\n    while q:\n  \
    \      d, v = heappop(q)\n        if d > D[v]: continue\n        if v == g: return\
    \ d\n        for u, w, *_ in G[v]:\n            if (nd := d + w) < D[u]:\n   \
    \             D[u] = nd\n                heappush(q, (nd, u))\n    return D if\
    \ g is None else inf"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/dijkstra_fn.py
  requiredBy: []
  timestamp: '2024-11-05 04:28:32+09:00'
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
