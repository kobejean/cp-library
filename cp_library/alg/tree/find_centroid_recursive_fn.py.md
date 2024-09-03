---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
    title: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "\nimport sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\npypyjit.set_param(\"\
    max_unroll_recursion=-1\")\n\ndef find_centroid(T):\n    N = len(T)\n    size\
    \ = [1] * N\n    half = N // 2\n\n    def dfs(u=0, p=None):\n        is_cent =\
    \ True\n        for v in T[u]:\n            if v == p: continue\n            cent\
    \ = dfs(v, u)\n            if cent != -1: return cent\n            if size[v]\
    \ > half: is_cent = False\n            size[u] += size[v]\n        if N - size[u]\
    \ > half:\n            is_cent = False\n        return u if is_cent else -1\n\n\
    \    return dfs()\n"
  code: "\nimport cp_library.misc.setrecursionlimit\n\ndef find_centroid(T):\n   \
    \ N = len(T)\n    size = [1] * N\n    half = N // 2\n\n    def dfs(u=0, p=None):\n\
    \        is_cent = True\n        for v in T[u]:\n            if v == p: continue\n\
    \            cent = dfs(v, u)\n            if cent != -1: return cent\n      \
    \      if size[v] > half: is_cent = False\n            size[u] += size[v]\n  \
    \      if N - size[u] > half:\n            is_cent = False\n        return u if\
    \ is_cent else -1\n\n    return dfs()"
  dependsOn:
  - cp_library/misc/setrecursionlimit.py
  isVerificationFile: false
  path: cp_library/alg/tree/find_centroid_recursive_fn.py
  requiredBy: []
  timestamp: '2024-09-03 23:33:52+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
documentation_of: cp_library/alg/tree/find_centroid_recursive_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/find_centroid_recursive_fn.py
- /library/cp_library/alg/tree/find_centroid_recursive_fn.py.html
title: cp_library/alg/tree/find_centroid_recursive_fn.py
---
