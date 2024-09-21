---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/grl_3_a_tarjan_articulation_points.test.py
    title: test/grl_3_a_tarjan_articulation_points.test.py
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
    \nimport sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\npypyjit.set_param(\"\
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
    \            dfs(i)\n\n    return ap\n"
  code: "import cp_library.misc.setrecursionlimit\n\ndef tarjan_articulation_points(G,\
    \ N):\n    order = [None] * N\n    low = [None] * N\n    parent = [-1] * N\n \
    \   ap = set()\n    time = 0\n\n    def dfs(u):\n        nonlocal time\n     \
    \   children = 0\n        order[u] = low[u] = time\n        time += 1\n\n    \
    \    for v in G[u]:\n            if order[v] is None:\n                children\
    \ += 1\n                parent[v] = u\n                dfs(v)\n              \
    \  low[u] = min(low[u], low[v])\n                if parent[u] != -1 and low[v]\
    \ >= order[u]:\n                    ap.add(u)\n            elif v != parent[u]:\n\
    \                low[u] = min(low[u], order[v])\n\n        if parent[u] == -1\
    \ and children > 1:\n            ap.add(u)\n\n    for i in range(N):\n       \
    \ if order[i] is None:\n            dfs(i)\n\n    return ap"
  dependsOn:
  - cp_library/misc/setrecursionlimit.py
  isVerificationFile: false
  path: cp_library/alg/graph/tarjan_articulation_points_fn.py
  requiredBy: []
  timestamp: '2024-09-21 16:44:49+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/grl_3_a_tarjan_articulation_points.test.py
documentation_of: cp_library/alg/graph/tarjan_articulation_points_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/tarjan_articulation_points_fn.py
- /library/cp_library/alg/graph/tarjan_articulation_points_fn.py.html
title: cp_library/alg/graph/tarjan_articulation_points_fn.py
---
