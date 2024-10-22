---
data:
  _extendedDependsOn: []
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
    \nfrom collections import deque\nfrom math import inf\n\ndef bfs(G, s = 0) ->\
    \ list[int]:\n    N = len(G)\n    D = [inf for _ in range(N)]\n    D[s] = 0\n\
    \    q = deque([s])\n    while q:\n        nd = D[u := q.popleft()]+1\n      \
    \  for v in G[u]:\n            if nd < D[v]:\n                D[v] = nd\n    \
    \            q.append(v)\n    return D\n"
  code: "import cp_library.alg.graph.__header__\n\nfrom collections import deque\n\
    from math import inf\n\ndef bfs(G, s = 0) -> list[int]:\n    N = len(G)\n    D\
    \ = [inf for _ in range(N)]\n    D[s] = 0\n    q = deque([s])\n    while q:\n\
    \        nd = D[u := q.popleft()]+1\n        for v in G[u]:\n            if nd\
    \ < D[v]:\n                D[v] = nd\n                q.append(v)\n    return\
    \ D"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/graph/bfs.py
  requiredBy: []
  timestamp: '2024-10-23 00:17:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/graph/bfs.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/bfs.py
- /library/cp_library/alg/graph/bfs.py.html
title: cp_library/alg/graph/bfs.py
---
