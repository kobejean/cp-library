---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_2_a_kruskal_heap.test.py
    title: test/grl_2_a_kruskal_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_a_kruskal_sort.test.py
    title: test/grl_2_a_kruskal_sort.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_b_edmonds_branching.test.py
    title: test/grl_2_b_edmonds_branching.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\ndef read_edges(M, i0=1):\n    E = []\n    for _ in range(M):\n \
    \       u,v,w = read(-i0)\n        w += i0\n        E.append((w,u,v))\n    return\
    \ E\n\n\ndef read(shift=0, base=10):\n    return [int(s, base) + shift for s in\
    \  input().split()]\n"
  code: "\ndef read_edges(M, i0=1):\n    E = []\n    for _ in range(M):\n        u,v,w\
    \ = read(-i0)\n        w += i0\n        E.append((w,u,v))\n    return E\n\nfrom\
    \ cp_library.io.read_int_fn import read"
  dependsOn:
  - cp_library/io/read_int_fn.py
  isVerificationFile: false
  path: cp_library/io/read_edges_weighted_fn.py
  requiredBy: []
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_2_a_kruskal_sort.test.py
  - test/grl_2_b_edmonds_branching.test.py
  - test/grl_2_a_kruskal_heap.test.py
documentation_of: cp_library/io/read_edges_weighted_fn.py
layout: document
redirect_from:
- /library/cp_library/io/read_edges_weighted_fn.py
- /library/cp_library/io/read_edges_weighted_fn.py.html
title: cp_library/io/read_edges_weighted_fn.py
---
