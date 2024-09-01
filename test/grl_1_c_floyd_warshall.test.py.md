---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
    title: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyd_warshall_directed_fn.py
    title: cp_library/alg/graph/floyd_warshall_directed_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyd_warshall_fn.py
    title: cp_library/alg/graph/floyd_warshall_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_graph_weighted_directed_fn.py
    title: cp_library/io/read_graph_weighted_directed_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/rint_fn.py
    title: cp_library/io/rint_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/misc/inf_cnst.py
    title: cp_library/misc/inf_cnst.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C\n\
    inf = float('inf')\ndef rint(shift=0, base=10):\n    return [int(x, base) + shift\
    \ for x in input().split()]\n\ndef read_graph(N, M, i0=1):\n    G = [[] for _\
    \ in range(N)]\n    for _ in range(M):\n        u,v,w = rint(-i0)\n        w +=\
    \ i0\n        G[u].append((w,v))\n    return G\n\ndef floyd_warshall(G, N, directed=True)\
    \ -> tuple[bool, list[int]]:\n    if directed:\n        from math import inf\n\
    \        \n        def floyd_warshall(G, N) -> list[int]:\n            D = [[inf]*N\
    \ for _ in range(N)]\n        \n            for u, edges in enumerate(G):\n  \
    \              D[u][u] = 0\n                for w,v in edges:\n              \
    \      D[u][v] = min(D[u][v], w)\n            \n            for k, Dk in enumerate(D):\n\
    \                for Di in D:\n                    for j in range(N):\n      \
    \                  Di[j] = min(Di[j], Di[k]+Dk[j])\n            return D\n   \
    \ else:\n        \n        def floyd_warshall(G, N) -> list[int]:\n          \
    \  D = [[inf]*N for _ in range(N)]\n        \n            for u, edges in enumerate(G):\n\
    \                D[u][u] = 0\n                for w,v in edges:\n            \
    \        D[u][v] = min(D[u][v], w)\n            \n            for k, Dk in enumerate(D):\n\
    \                for i, Di in enumerate(D):\n                    for j in range(i):\n\
    \                        Di[j] = D[j][i] = min(Di[j], Di[k]+Dk[j])\n         \
    \   return D\n    D = floyd_warshall(G, N)\n    return any(D[i][i] < 0 for i in\
    \ range(N)), D\n\nN, M = rint()\nG = read_graph(N, M, 0)\nneg_cycle, D = floyd_warshall(G,\
    \ N)\n\nif neg_cycle:\n    print(\"NEGATIVE CYCLE\")\nelse:\n    for row in D:\n\
    \        print(*('INF' if d == inf else d for d in row))\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C\n\
    from cp_library.misc.inf_cnst import inf\nfrom cp_library.io.rint_fn import rint\n\
    from cp_library.io.read_graph_weighted_directed_fn import read_graph\nfrom cp_library.alg.graph.floyd_warshall_check_neg_cycle_fn\
    \ import floyd_warshall\n\nN, M = rint()\nG = read_graph(N, M, 0)\nneg_cycle,\
    \ D = floyd_warshall(G, N)\n\nif neg_cycle:\n    print(\"NEGATIVE CYCLE\")\nelse:\n\
    \    for row in D:\n        print(*('INF' if d == inf else d for d in row))"
  dependsOn:
  - cp_library/misc/inf_cnst.py
  - cp_library/io/rint_fn.py
  - cp_library/io/read_graph_weighted_directed_fn.py
  - cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  - cp_library/alg/graph/floyd_warshall_directed_fn.py
  - cp_library/alg/graph/floyd_warshall_fn.py
  isVerificationFile: true
  path: test/grl_1_c_floyd_warshall.test.py
  requiredBy: []
  timestamp: '2024-09-02 01:58:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_1_c_floyd_warshall.test.py
layout: document
redirect_from:
- /verify/test/grl_1_c_floyd_warshall.test.py
- /verify/test/grl_1_c_floyd_warshall.test.py.html
title: test/grl_1_c_floyd_warshall.test.py
---
