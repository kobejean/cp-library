---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "\nimport sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\npypyjit.set_param(\"\
    max_unroll_recursion=-1\")\n\ndef find_centroids(T):\n    N = len(T)\n    size\
    \ = [1] * N\n    centroids = []\n\n    def dfs1(u, p):\n        for v in T[u]:\n\
    \            if v != p:\n                dfs1(v, u)\n                size[u] +=\
    \ size[v]\n\n    def dfs2(u, p):\n        is_centroid = True\n        for v in\
    \ T[u]:\n            if v != p:\n                if size[v] > N // 2:\n      \
    \              is_centroid = False\n                    break\n        \n    \
    \    if is_centroid and (N - size[u]) <= N // 2:\n            centroids.append(u)\n\
    \        \n        for v in T[u]:\n            if v != p:\n                dfs2(v,\
    \ u)\n\n    dfs1(0, -1)\n    dfs2(0, -1)\n\n    return centroids\n"
  code: "\nimport cp_library.misc.setrecursionlimit\n\ndef find_centroids(T):\n  \
    \  N = len(T)\n    size = [1] * N\n    centroids = []\n\n    def dfs1(u, p):\n\
    \        for v in T[u]:\n            if v != p:\n                dfs1(v, u)\n\
    \                size[u] += size[v]\n\n    def dfs2(u, p):\n        is_centroid\
    \ = True\n        for v in T[u]:\n            if v != p:\n                if size[v]\
    \ > N // 2:\n                    is_centroid = False\n                    break\n\
    \        \n        if is_centroid and (N - size[u]) <= N // 2:\n            centroids.append(u)\n\
    \        \n        for v in T[u]:\n            if v != p:\n                dfs2(v,\
    \ u)\n\n    dfs1(0, -1)\n    dfs2(0, -1)\n\n    return centroids"
  dependsOn:
  - cp_library/misc/setrecursionlimit.py
  isVerificationFile: false
  path: cp_library/alg/tree/centroid.py
  requiredBy: []
  timestamp: '2024-08-27 19:11:09+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/tree/centroid.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/centroid.py
- /library/cp_library/alg/tree/centroid.py.html
title: cp_library/alg/tree/centroid.py
---
