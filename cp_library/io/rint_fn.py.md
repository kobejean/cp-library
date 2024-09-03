---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: cp_library/io/read_edges_weighted_fn.py
    title: cp_library/io/read_edges_weighted_fn.py
  - icon: ':x:'
    path: cp_library/io/read_graph_weighted_directed_fn.py
    title: cp_library/io/read_graph_weighted_directed_fn.py
  - icon: ':warning:'
    path: cp_library/io/read_graph_weighted_fn.py
    title: cp_library/io/read_graph_weighted_fn.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/grl_1_a_dijkstra.test.py
    title: test/grl_1_a_dijkstra.test.py
  - icon: ':x:'
    path: test/grl_1_b_bellman_ford.test.py
    title: test/grl_1_b_bellman_ford.test.py
  - icon: ':x:'
    path: test/grl_1_c_floyd_warshall.test.py
    title: test/grl_1_c_floyd_warshall.test.py
  - icon: ':x:'
    path: test/grl_2_a_kruskal_heap.test.py
    title: test/grl_2_a_kruskal_heap.test.py
  - icon: ':x:'
    path: test/grl_2_a_kruskal_sort.test.py
    title: test/grl_2_a_kruskal_sort.test.py
  - icon: ':x:'
    path: test/grl_2_b_edmonds_branching.test.py
    title: test/grl_2_b_edmonds_branching.test.py
  - icon: ':heavy_check_mark:'
    path: test/unionfind.test.py
    title: test/unionfind.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "def rint(shift=0, base=10):\n    return [int(x, base) + shift for\
    \ x in input().split()]\n"
  code: "def rint(shift=0, base=10):\n    return [int(x, base) + shift for x in input().split()]"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/io/rint_fn.py
  requiredBy:
  - cp_library/io/read_graph_weighted_fn.py
  - cp_library/io/read_graph_weighted_directed_fn.py
  - cp_library/io/read_edges_weighted_fn.py
  timestamp: '2024-09-03 19:30:15+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/grl_1_a_dijkstra.test.py
  - test/unionfind.test.py
  - test/grl_1_c_floyd_warshall.test.py
  - test/grl_1_b_bellman_ford.test.py
  - test/grl_2_a_kruskal_sort.test.py
  - test/grl_2_b_edmonds_branching.test.py
  - test/grl_2_a_kruskal_heap.test.py
documentation_of: cp_library/io/rint_fn.py
layout: document
redirect_from:
- /library/cp_library/io/rint_fn.py
- /library/cp_library/io/rint_fn.py.html
title: cp_library/io/rint_fn.py
---
