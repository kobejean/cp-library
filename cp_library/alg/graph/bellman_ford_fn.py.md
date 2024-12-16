---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/math/inft_cnst.py
    title: cp_library/math/inft_cnst.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
    title: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/digraph_weighted_cls.py
    title: cp_library/alg/graph/fast/digraph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/graph_weighted_base_cls.py
    title: cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/graph_weighted_cls.py
    title: cp_library/alg/graph/fast/graph_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/tree_weighted_base_cls.py
    title: cp_library/alg/graph/fast/tree_weighted_base_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_1_a_fast_dijkstra.test.py
    title: test/grl_1_a_fast_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_b_bellman_ford.test.py
    title: test/grl_1_b_bellman_ford.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_b_fast_bellman_ford.test.py
    title: test/grl_1_b_fast_bellman_ford.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_c_fast_floyd_warshall.test.py
    title: test/grl_1_c_fast_floyd_warshall.test.py
  - icon: ':heavy_check_mark:'
    path: test/minimum_spanning_tree_kruskal.test.py
    title: test/minimum_spanning_tree_kruskal.test.py
  - icon: ':heavy_check_mark:'
    path: test/minimum_spanning_tree_kruskal_heap.test.py
    title: test/minimum_spanning_tree_kruskal_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/shortest_path_fast_graph.test.py
    title: test/shortest_path_fast_graph.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nimport sys\ninft: int\n\ninft = sys.maxsize\n\ndef bellman_ford(G, N, root)\
    \ -> list[int]:\n    D = [inft]*N\n    D[root] = 0\n    for _ in range(N-1):\n\
    \        for u, edges in enumerate(G):\n            if D[u] == inft: continue\n\
    \            for v,w in edges:\n                D[v] = min(D[v], D[u] + w)\n \
    \   return D\n"
  code: "import cp_library.alg.graph.__header__\nfrom cp_library.math.inft_cnst import\
    \ inft\n\ndef bellman_ford(G, N, root) -> list[int]:\n    D = [inft]*N\n    D[root]\
    \ = 0\n    for _ in range(N-1):\n        for u, edges in enumerate(G):\n     \
    \       if D[u] == inft: continue\n            for v,w in edges:\n           \
    \     D[v] = min(D[v], D[u] + w)\n    return D\n"
  dependsOn:
  - cp_library/math/inft_cnst.py
  isVerificationFile: false
  path: cp_library/alg/graph/bellman_ford_fn.py
  requiredBy:
  - cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
  - cp_library/alg/graph/fast/graph_weighted_cls.py
  - cp_library/alg/graph/fast/tree_weighted_base_cls.py
  - cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - cp_library/alg/graph/fast/digraph_weighted_cls.py
  timestamp: '2024-12-17 03:19:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_1_a_fast_dijkstra.test.py
  - test/minimum_spanning_tree_kruskal.test.py
  - test/grl_1_c_fast_floyd_warshall.test.py
  - test/grl_1_b_bellman_ford.test.py
  - test/shortest_path_fast_graph.test.py
  - test/grl_1_b_fast_bellman_ford.test.py
  - test/minimum_spanning_tree_kruskal_heap.test.py
documentation_of: cp_library/alg/graph/bellman_ford_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/bellman_ford_fn.py
- /library/cp_library/alg/graph/bellman_ford_fn.py.html
title: cp_library/alg/graph/bellman_ford_fn.py
---
