---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc184_e_grid_graph_bfs_fn.test.py
    title: test/atcoder/abc/abc184_e_grid_graph_bfs_fn.test.py
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
    \nfrom collections import deque\nfrom typing import overload\nfrom math import\
    \ inf\n\n@overload\ndef bfs(G, s: int = 0) -> list[int]: ...\n@overload\ndef bfs(G,\
    \ s: int, g: int) -> int: ...\n\ndef bfs(G, s: int = 0, g: int = None):\n    D\
    \ = [inf for _ in range(G.N)]\n    D[s] = 0\n    q = deque([s])\n    while q:\n\
    \        nd = D[u := q.popleft()]+1\n        if u == g: return D[u]\n        for\
    \ v in G[u]:\n            if nd < D[v]:\n                D[v] = nd\n         \
    \       q.append(v)\n    return D if g is None else inf\n"
  code: "import cp_library.alg.graph.__header__\n\nfrom collections import deque\n\
    from typing import overload\nfrom math import inf\n\n@overload\ndef bfs(G, s:\
    \ int = 0) -> list[int]: ...\n@overload\ndef bfs(G, s: int, g: int) -> int: ...\n\
    \ndef bfs(G, s: int = 0, g: int = None):\n    D = [inf for _ in range(G.N)]\n\
    \    D[s] = 0\n    q = deque([s])\n    while q:\n        nd = D[u := q.popleft()]+1\n\
    \        if u == g: return D[u]\n        for v in G[u]:\n            if nd < D[v]:\n\
    \                D[v] = nd\n                q.append(v)\n    return D if g is\
    \ None else inf"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/bfs_fn.py
  requiredBy: []
  timestamp: '2024-12-30 17:25:46+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc184_e_grid_graph_bfs_fn.test.py
documentation_of: cp_library/alg/graph/bfs_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/bfs_fn.py
- /library/cp_library/alg/graph/bfs_fn.py.html
title: cp_library/alg/graph/bfs_fn.py
---
