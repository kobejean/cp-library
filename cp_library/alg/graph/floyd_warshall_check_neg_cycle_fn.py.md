---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyd_warshall_directed_fn.py
    title: cp_library/alg/graph/floyd_warshall_directed_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyd_warshall_fn.py
    title: cp_library/alg/graph/floyd_warshall_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/inft_cnst.py
    title: cp_library/math/inft_cnst.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_1_c_floyd_warshall.test.py
    title: test/grl_1_c_floyd_warshall.test.py
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
    \ndef floyd_warshall(G, N, directed=True):\n    if directed:\n        \n     \
    \   import sys\n        inft: int\n        \n        inft = sys.maxsize\n    \
    \    \n        def floyd_warshall(G, N) -> list[list[int]]:\n            D = [[inft]*N\
    \ for _ in range(N)]\n        \n            for u, edges in enumerate(G):\n  \
    \              D[u][u] = 0\n                for v,w in edges:\n              \
    \      D[u][v] = min(D[u][v], w)\n            \n            for k, Dk in enumerate(D):\n\
    \                for Di in D:\n                    if Di[k] == inft: continue\n\
    \                    for j in range(N):\n                        if Dk[j] == inft:\
    \ continue\n                        Di[j] = min(Di[j], Di[k]+Dk[j])\n        \
    \    return D\n    else:\n        \n        import sys\n        inft: int\n  \
    \      \n        inft = sys.maxsize\n        \n        def floyd_warshall(G, N)\
    \ -> list[list[int]]:\n            D = [[inft]*N for _ in range(N)]\n        \n\
    \            for u, edges in enumerate(G):\n                D[u][u] = 0\n    \
    \            for v,w in edges:\n                    D[u][v] = min(D[u][v], w)\n\
    \            \n            for k, Dk in enumerate(D):\n                for i,\
    \ Di in enumerate(D):\n                    if Di[k] == inft: continue\n      \
    \              for j in range(i):\n                        if Dk[j] == inft: continue\n\
    \                        Di[j] = D[j][i] = min(Di[j], Di[k]+Dk[j])\n         \
    \   return D\n    D = floyd_warshall(G, N)\n    return any(D[i][i] < 0 for i in\
    \ range(N)), D\n"
  code: "import cp_library.alg.graph.__header__\n\ndef floyd_warshall(G, N, directed=True):\n\
    \    if directed:\n        from cp_library.alg.graph.floyd_warshall_directed_fn\
    \ import floyd_warshall\n    else:\n        from cp_library.alg.graph.floyd_warshall_fn\
    \ import floyd_warshall\n    D = floyd_warshall(G, N)\n    return any(D[i][i]\
    \ < 0 for i in range(N)), D\n"
  dependsOn:
  - cp_library/alg/graph/floyd_warshall_directed_fn.py
  - cp_library/alg/graph/floyd_warshall_fn.py
  - cp_library/math/inft_cnst.py
  isVerificationFile: false
  path: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  requiredBy: []
  timestamp: '2024-12-05 05:25:23+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_1_c_floyd_warshall.test.py
documentation_of: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
- /library/cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py.html
title: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
---
