---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/tarjan_articulation_points_fn.py
    title: cp_library/alg/graph/tarjan_articulation_points_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_graph_fn.py
    title: cp_library/io/read_graph_fn.py
  - icon: ':question:'
    path: cp_library/io/rint_fn.py
    title: cp_library/io/rint_fn.py
  - icon: ':question:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A\n\
    def rint(shift=0, base=10):\n    return [int(x, base) + shift for x in input().split()]\n\
    \ndef read_graph(N, M, i0=1):\n    G = [[] for _ in range(N)]\n    for _ in range(M):\n\
    \        u,v = rint(-i0)\n        G[u].append(v)\n        G[v].append(u)\n   \
    \ return G\nimport sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\npypyjit.set_param(\"\
    max_unroll_recursion=-1\")\n\ndef tarjan_articulation_points(G, N):\n    order\
    \ = [None] * N\n    low = [None] * N\n    parent = [-1] * N\n    ap = set()\n\
    \    time = 0\n\n    def dfs(u):\n        nonlocal time\n        children = 0\n\
    \        order[u] = low[u] = time\n        time += 1\n\n        for v in G[u]:\n\
    \            if order[v] is None:\n                children += 1\n           \
    \     parent[v] = u\n                dfs(v)\n                low[u] = min(low[u],\
    \ low[v])\n                if parent[u] != -1 and low[v] >= order[u]:\n      \
    \              ap.add(u)\n            elif v != parent[u]:\n                low[u]\
    \ = min(low[u], order[v])\n\n        if parent[u] == -1 and children > 1:\n  \
    \          ap.add(u)\n\n    for i in range(N):\n        if order[i] is None:\n\
    \            dfs(i)\n\n    return ap\n\nN, M = rint()\nG = read_graph(N, M, 0)\n\
    ans = sorted(tarjan_articulation_points(G, N))\nif ans:\n    print(*ans, sep='\\\
    n')\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A\n\
    from cp_library.io.rint_fn import rint\nfrom cp_library.io.read_graph_fn import\
    \ read_graph\nfrom cp_library.alg.graph.tarjan_articulation_points_fn import tarjan_articulation_points\n\
    \nN, M = rint()\nG = read_graph(N, M, 0)\nans = sorted(tarjan_articulation_points(G,\
    \ N))\nif ans:\n    print(*ans, sep='\\n')"
  dependsOn:
  - cp_library/io/rint_fn.py
  - cp_library/io/read_graph_fn.py
  - cp_library/alg/graph/tarjan_articulation_points_fn.py
  - cp_library/misc/setrecursionlimit.py
  isVerificationFile: true
  path: test/grl_3_a_tarjan_articulation_points.test.py
  requiredBy: []
  timestamp: '2024-09-03 23:33:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_3_a_tarjan_articulation_points.test.py
layout: document
redirect_from:
- /verify/test/grl_3_a_tarjan_articulation_points.test.py
- /verify/test/grl_3_a_tarjan_articulation_points.test.py.html
title: test/grl_3_a_tarjan_articulation_points.test.py
---
