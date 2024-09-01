---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/dijkstra_fn.py
    title: cp_library/alg/graph/dijkstra_fn.py
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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A\n\
    inf = float('inf')\ndef rint(shift=0, base=10):\n    return [int(x, base) + shift\
    \ for x in input().split()]\n\ndef read_graph(N, M, i0=1):\n    G = [[] for _\
    \ in range(N)]\n    for _ in range(M):\n        u,v,w = rint(-i0)\n        w +=\
    \ i0\n        G[u].append((w,v))\n    return G\nimport heapq\nfrom math import\
    \ inf\n\ndef dijkstra(G, N, root) -> list[int]:\n    D = [inf for _ in range(N)]\n\
    \    D[root] = 0\n    queue = [(0, root)]\n    while queue:\n        d, v = heapq.heappop(queue)\n\
    \        if d > D[v]: continue\n\n        for w, u in G[v]:\n            nd =\
    \ d + w\n            if nd < D[u]:\n                D[u] = nd\n              \
    \  heapq.heappush(queue, (nd, u))\n    return D\n\nN, M, r = rint()\nG = read_graph(N,\
    \ M, 0)\n\nD = dijkstra(G, N, r)\n\nprint(*('INF' if d == inf else d for d in\
    \ D), sep='\\n')\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A

    from cp_library.misc.inf_cnst import inf

    from cp_library.io.rint_fn import rint

    from cp_library.io.read_graph_weighted_directed_fn import read_graph

    from cp_library.alg.graph.dijkstra_fn import dijkstra


    N, M, r = rint()

    G = read_graph(N, M, 0)


    D = dijkstra(G, N, r)


    print(*(''INF'' if d == inf else d for d in D), sep=''\n'')'
  dependsOn:
  - cp_library/misc/inf_cnst.py
  - cp_library/io/rint_fn.py
  - cp_library/io/read_graph_weighted_directed_fn.py
  - cp_library/alg/graph/dijkstra_fn.py
  isVerificationFile: true
  path: test/grl_1_a_dijkstra.test.py
  requiredBy: []
  timestamp: '2024-09-02 01:58:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_1_a_dijkstra.test.py
layout: document
redirect_from:
- /verify/test/grl_1_a_dijkstra.test.py
- /verify/test/grl_1_a_dijkstra.test.py.html
title: test/grl_1_a_dijkstra.test.py
---
