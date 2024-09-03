---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/bellman_ford_fn.py
    title: cp_library/alg/graph/bellman_ford_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
    title: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_graph_weighted_directed_fn.py
    title: cp_library/io/read_graph_weighted_directed_fn.py
  - icon: ':question:'
    path: cp_library/io/rint_fn.py
    title: cp_library/io/rint_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_B
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_B\n\
    from math import inf\ndef rint(shift=0, base=10):\n    return [int(x, base) +\
    \ shift for x in input().split()]\n\ndef read_graph(N, M, i0=1):\n    G = [[]\
    \ for _ in range(N)]\n    for _ in range(M):\n        u,v,w = rint(-i0)\n    \
    \    w += i0\n        G[u].append((w,v))\n    return G\n\ndef bellman_ford(G,\
    \ N, root) -> tuple[bool, list[int]]:\n    \n    def bellman_ford(G, N, root)\
    \ -> list[int]:\n        D = [inf]*N\n        D[root] = 0\n        for _ in range(N-1):\n\
    \            for u, edges in enumerate(G):\n                for w, v in edges:\n\
    \                    D[v] = min(D[v], D[u] + w)\n        return D\n    D = bellman_ford(G,\
    \ N, root)\n    neg_cycle = any(D[u]+w<D[v] for u, edges in enumerate(G) for w,v\
    \ in edges)\n    return neg_cycle, D\n\nN, M, r = rint()\nG = read_graph(N, M,\
    \ 0)\n\nneg_cycle, D = bellman_ford(G, N, r)\n\nif neg_cycle:\n    print(\"NEGATIVE\
    \ CYCLE\")\nelse:\n    print(*('INF' if d == inf else d for d in D), sep='\\n')\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_B\n\
    from math import inf\nfrom cp_library.io.rint_fn import rint\nfrom cp_library.io.read_graph_weighted_directed_fn\
    \ import read_graph\nfrom cp_library.alg.graph.bellman_ford_neg_cyc_check_fn import\
    \ bellman_ford\n\nN, M, r = rint()\nG = read_graph(N, M, 0)\n\nneg_cycle, D =\
    \ bellman_ford(G, N, r)\n\nif neg_cycle:\n    print(\"NEGATIVE CYCLE\")\nelse:\n\
    \    print(*('INF' if d == inf else d for d in D), sep='\\n')"
  dependsOn:
  - cp_library/io/rint_fn.py
  - cp_library/io/read_graph_weighted_directed_fn.py
  - cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
  - cp_library/alg/graph/bellman_ford_fn.py
  isVerificationFile: true
  path: test/grl_1_b_bellman_ford.test.py
  requiredBy: []
  timestamp: '2024-09-03 23:33:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_1_b_bellman_ford.test.py
layout: document
redirect_from:
- /verify/test/grl_1_b_bellman_ford.test.py
- /verify/test/grl_1_b_bellman_ford.test.py.html
title: test/grl_1_b_bellman_ford.test.py
---
