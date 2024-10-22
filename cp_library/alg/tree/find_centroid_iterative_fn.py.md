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
  bundledCode: "\n\ndef find_centroid(T):\n    N = len(T)\n    size = [1] * N\n  \
    \  stack = [(0, None, True)]\n\n    while stack:\n        u, p, forw = stack.pop()\n\
    \        if forw:\n            stack.append((u, p, False))\n            for v\
    \ in T[u]:\n                if v != p:\n                    stack.append((v, u,\
    \ True))\n        else:\n            is_cent = True\n            for v in T[u]:\n\
    \                if v == p: continue\n                if size[v] > N//2:\n   \
    \                 is_cent = False\n                size[u] += size[v]\n      \
    \      \n            if is_cent and N - size[u] <=  N//2:\n                return\
    \ u\n    N = len(T)\n    size = [0] * N\n    stack = [(0, None, True)]\n    cent\
    \ = None\n\n    while stack:\n        u, p, forw = stack.pop()\n\n        if forw:\n\
    \            size[u] = 1\n            stack.append((u, p, False))\n          \
    \  for v in T[u]:\n                if v != p:\n                    stack.append((v,\
    \ u, True))\n        else:\n            is_cent = True\n            for v in T[u]:\n\
    \                if v == p:\n                    continue\n                if\
    \ size[v] > N // 2:\n                    is_cent = False\n                size[u]\
    \ += size[v]\n            \n            if N - size[u] > N // 2:\n           \
    \     is_cent = False\n            \n            if is_cent:\n               \
    \ cent = u\n                break\n\n    return cent\n"
  code: "import cp_library.alg.tree.__header__\n\ndef find_centroid(T):\n    N = len(T)\n\
    \    size = [1] * N\n    stack = [(0, None, True)]\n\n    while stack:\n     \
    \   u, p, forw = stack.pop()\n        if forw:\n            stack.append((u, p,\
    \ False))\n            for v in T[u]:\n                if v != p:\n          \
    \          stack.append((v, u, True))\n        else:\n            is_cent = True\n\
    \            for v in T[u]:\n                if v == p: continue\n           \
    \     if size[v] > N//2:\n                    is_cent = False\n              \
    \  size[u] += size[v]\n            \n            if is_cent and N - size[u] <=\
    \  N//2:\n                return u\n    N = len(T)\n    size = [0] * N\n    stack\
    \ = [(0, None, True)]\n    cent = None\n\n    while stack:\n        u, p, forw\
    \ = stack.pop()\n\n        if forw:\n            size[u] = 1\n            stack.append((u,\
    \ p, False))\n            for v in T[u]:\n                if v != p:\n       \
    \             stack.append((v, u, True))\n        else:\n            is_cent =\
    \ True\n            for v in T[u]:\n                if v == p:\n             \
    \       continue\n                if size[v] > N // 2:\n                    is_cent\
    \ = False\n                size[u] += size[v]\n            \n            if N\
    \ - size[u] > N // 2:\n                is_cent = False\n            \n       \
    \     if is_cent:\n                cent = u\n                break\n\n    return\
    \ cent"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/tree/find_centroid_iterative_fn.py
  requiredBy: []
  timestamp: '2024-10-23 00:17:22+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/tree/find_centroid_iterative_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/find_centroid_iterative_fn.py
- /library/cp_library/alg/tree/find_centroid_iterative_fn.py.html
title: cp_library/alg/tree/find_centroid_iterative_fn.py
---
