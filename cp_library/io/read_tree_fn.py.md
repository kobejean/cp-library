---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/arc183_d_keep_perfectly_matched_centroid_iterative.test.py
    title: test/arc183_d_keep_perfectly_matched_centroid_iterative.test.py
  - icon: ':x:'
    path: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
    title: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_iterative.test.py
    title: test/dp_v_subtree_rerooting_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_recursive.test.py
    title: test/dp_v_subtree_rerooting_recursive.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "def read_tree(N, i0=1):\n    T = [[] for _ in range(N)]\n    for _\
    \ in range(N-1):\n        u,v = read(-i0)\n        T[u].append(v)\n        T[v].append(u)\n\
    \    return T\n\n\ndef read(shift=0, base=10):\n    return [int(s, base) + shift\
    \ for s in  input().split()]\n"
  code: "def read_tree(N, i0=1):\n    T = [[] for _ in range(N)]\n    for _ in range(N-1):\n\
    \        u,v = read(-i0)\n        T[u].append(v)\n        T[v].append(u)\n   \
    \ return T\n\nfrom cp_library.io.read_int_fn import read"
  dependsOn:
  - cp_library/io/read_int_fn.py
  isVerificationFile: false
  path: cp_library/io/read_tree_fn.py
  requiredBy: []
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/dp_v_subtree_rerooting_iterative.test.py
  - test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
  - test/arc183_d_keep_perfectly_matched_centroid_iterative.test.py
  - test/dp_v_subtree_rerooting_recursive.test.py
documentation_of: cp_library/io/read_tree_fn.py
layout: document
redirect_from:
- /library/cp_library/io/read_tree_fn.py
- /library/cp_library/io/read_tree_fn.py.html
title: cp_library/io/read_tree_fn.py
---
