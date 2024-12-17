---
data:
  _extendedDependsOn:
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
    \nfrom collections import deque\nfrom typing import overload\n\nimport sys\ninft:\
    \ int\n\ninft = sys.maxsize\n\n@overload\ndef bfs(G, s: int = 0) -> list[int]:\
    \ ...\n@overload\ndef bfs(G, s: int, g: int) -> int: ...\n\ndef bfs(G, s: int\
    \ = 0, g: int = None):\n    D = [inft for _ in range(G.N)]\n    D[s] = 0\n   \
    \ q = deque([s])\n    while q:\n        nd = D[u := q.popleft()]+1\n        if\
    \ u == g: return D[u]\n        for v in G[u]:\n            if nd < D[v]:\n   \
    \             D[v] = nd\n                q.append(v)\n    return D if g is None\
    \ else inft\n"
  code: "import cp_library.alg.graph.__header__\n\nfrom collections import deque\n\
    from typing import overload\nfrom cp_library.math.inft_cnst import inft\n\n@overload\n\
    def bfs(G, s: int = 0) -> list[int]: ...\n@overload\ndef bfs(G, s: int, g: int)\
    \ -> int: ...\n\ndef bfs(G, s: int = 0, g: int = None):\n    D = [inft for _ in\
    \ range(G.N)]\n    D[s] = 0\n    q = deque([s])\n    while q:\n        nd = D[u\
    \ := q.popleft()]+1\n        if u == g: return D[u]\n        for v in G[u]:\n\
    \            if nd < D[v]:\n                D[v] = nd\n                q.append(v)\n\
    \    return D if g is None else inft"
  dependsOn:
  - cp_library/math/inft_cnst.py
  isVerificationFile: false
  path: cp_library/alg/graph/bfs_fn.py
  requiredBy: []
  timestamp: '2024-12-17 21:59:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/graph/bfs_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/bfs_fn.py
- /library/cp_library/alg/graph/bfs_fn.py.html
title: cp_library/alg/graph/bfs_fn.py
---
