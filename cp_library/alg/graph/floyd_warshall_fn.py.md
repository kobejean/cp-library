---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/math/inft_cnst.py
    title: cp_library/math/inft_cnst.py
  _extendedRequiredBy:
  - icon: ':x:'
    path: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
    title: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/grl_1_c_floyd_warshall.test.py
    title: test/grl_1_c_floyd_warshall.test.py
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
    \nimport sys\n\ninft = sys.maxsize\n\ndef floyd_warshall(G, N) -> list[list[int]]:\n\
    \    D = [[inft]*N for _ in range(N)]\n\n    for u, edges in enumerate(G):\n \
    \       D[u][u] = 0\n        for v,w in edges:\n            D[u][v] = min(D[u][v],\
    \ w)\n    \n    for k, Dk in enumerate(D):\n        for i, Di in enumerate(D):\n\
    \            for j in range(i):\n                Di[j] = D[j][i] = min(Di[j],\
    \ Di[k]+Dk[j])\n    return D\n"
  code: "import cp_library.alg.graph.__header__\nfrom cp_library.math.inft_cnst import\
    \ inft\n\ndef floyd_warshall(G, N) -> list[list[int]]:\n    D = [[inft]*N for\
    \ _ in range(N)]\n\n    for u, edges in enumerate(G):\n        D[u][u] = 0\n \
    \       for v,w in edges:\n            D[u][v] = min(D[u][v], w)\n    \n    for\
    \ k, Dk in enumerate(D):\n        for i, Di in enumerate(D):\n            for\
    \ j in range(i):\n                Di[j] = D[j][i] = min(Di[j], Di[k]+Dk[j])\n\
    \    return D"
  dependsOn:
  - cp_library/math/inft_cnst.py
  isVerificationFile: false
  path: cp_library/alg/graph/floyd_warshall_fn.py
  requiredBy:
  - cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  timestamp: '2024-11-28 18:07:28+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/grl_1_c_floyd_warshall.test.py
documentation_of: cp_library/alg/graph/floyd_warshall_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/floyd_warshall_fn.py
- /library/cp_library/alg/graph/floyd_warshall_fn.py.html
title: cp_library/alg/graph/floyd_warshall_fn.py
---
