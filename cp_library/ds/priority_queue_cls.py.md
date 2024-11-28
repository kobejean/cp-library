---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/ds/heap_proto.py
    title: cp_library/ds/heap_proto.py
  _extendedRequiredBy:
  - icon: ':question:'
    path: cp_library/alg/graph/digraph_weighted_cls.py
    title: cp_library/alg/graph/digraph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/fast_graph_cls.py
    title: cp_library/alg/graph/fast/fast_graph_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/static_graph_cls.py
    title: cp_library/alg/graph/fast/static_graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_cls.py
    title: cp_library/alg/graph/graph_weighted_cls.py
  - icon: ':question:'
    path: cp_library/alg/graph/graph_weighted_proto.py
    title: cp_library/alg/graph/graph_weighted_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_proto.py
    title: cp_library/alg/tree/tree_weighted_proto.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc218_f_shortest_path_weighted.test.py
    title: test/abc218_f_shortest_path_weighted.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
    title: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
    title: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc361_e_tree_diameter.test.py
    title: test/abc361_e_tree_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc375_g_find_bridges.test.py
    title: test/abc375_g_find_bridges.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_a_dijkstra.test.py
    title: test/grl_1_a_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_a_graph_distance.test.py
    title: test/grl_1_a_graph_distance.test.py
  - icon: ':x:'
    path: test/grl_1_b_bellman_ford.test.py
    title: test/grl_1_b_bellman_ford.test.py
  - icon: ':x:'
    path: test/grl_1_b_graph_bellman_ford.test.py
    title: test/grl_1_b_graph_bellman_ford.test.py
  - icon: ':x:'
    path: test/grl_1_c_floyd_warshall.test.py
    title: test/grl_1_c_floyd_warshall.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_a_graph_kruskal.test.py
    title: test/grl_2_a_graph_kruskal.test.py
  - icon: ':heavy_check_mark:'
    path: test/shortest_path_graph_weighted.test.py
    title: test/shortest_path_graph_weighted.test.py
  - icon: ':heavy_check_mark:'
    path: test/shortest_path_min_heap.test.py
    title: test/shortest_path_min_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/shortest_path_static_graph_weighted.test.py
    title: test/shortest_path_static_graph_weighted.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nfrom typing import Iterable\nfrom collections import UserList\nfrom heapq import\
    \ heapify, heappop, heappush, heappushpop, heapreplace\nfrom typing import Generic,\
    \ TypeVar\n\nT = TypeVar('T')\nclass HeapProtocol(Generic[T]):\n    def pop(self)\
    \ -> T: ...\n    def push(self, item: T): ...\n    def pushpop(self, item: T)\
    \ -> T: ...\n    def replace(self, item: T) -> T: ...\n\nclass PriorityQueue(HeapProtocol[int],\
    \ UserList[int]):\n    \n    def __init__(self, N: int, ids: Iterable[int] = None,\
    \ priorities: Iterable[int] = None, /):\n        self.shift = N.bit_length()\n\
    \        self.mask = (1 << self.shift)-1\n        if ids is None:\n          \
    \  super().__init__()\n        elif priorities is None:\n            self.data\
    \ = ids\n            heapify(self.data)\n        else:\n            self.data\
    \ = [self.encode(id, priority) for id, priority in zip(ids, priorities)]\n   \
    \         heapify(self.data)\n\n    def encode(self, id, priority):\n        return\
    \ priority << self.shift | id\n    \n    def decode(self, encoded):\n        return\
    \ self.mask & encoded, encoded >> self.shift\n    \n    def pop(self):\n     \
    \   return self.decode(heappop(self.data))\n    \n    def push(self, id: int,\
    \ priority: int):\n        heappush(self.data, self.encode(id, priority))\n\n\
    \    def pushpop(self, id: int, priority: int):\n        return self.decode(heappushpop(self.data,\
    \ self.encode(id, priority)))\n    \n    def replace(self, id: int, priority:\
    \ int):\n        return self.decode(heapreplace(self.data, self.encode(id, priority)))\n\
    \n"
  code: "import cp_library.ds.__header__\n\nfrom typing import Iterable\nfrom collections\
    \ import UserList\nfrom typing import Iterable\nfrom heapq import heapify, heappop,\
    \ heappush, heappushpop, heapreplace\nfrom cp_library.ds.heap_proto import HeapProtocol\n\
    \nclass PriorityQueue(HeapProtocol[int], UserList[int]):\n    \n    def __init__(self,\
    \ N: int, ids: Iterable[int] = None, priorities: Iterable[int] = None, /):\n \
    \       self.shift = N.bit_length()\n        self.mask = (1 << self.shift)-1\n\
    \        if ids is None:\n            super().__init__()\n        elif priorities\
    \ is None:\n            self.data = ids\n            heapify(self.data)\n    \
    \    else:\n            self.data = [self.encode(id, priority) for id, priority\
    \ in zip(ids, priorities)]\n            heapify(self.data)\n\n    def encode(self,\
    \ id, priority):\n        return priority << self.shift | id\n    \n    def decode(self,\
    \ encoded):\n        return self.mask & encoded, encoded >> self.shift\n    \n\
    \    def pop(self):\n        return self.decode(heappop(self.data))\n    \n  \
    \  def push(self, id: int, priority: int):\n        heappush(self.data, self.encode(id,\
    \ priority))\n\n    def pushpop(self, id: int, priority: int):\n        return\
    \ self.decode(heappushpop(self.data, self.encode(id, priority)))\n    \n    def\
    \ replace(self, id: int, priority: int):\n        return self.decode(heapreplace(self.data,\
    \ self.encode(id, priority)))\n\n"
  dependsOn:
  - cp_library/ds/heap_proto.py
  isVerificationFile: false
  path: cp_library/ds/priority_queue_cls.py
  requiredBy:
  - cp_library/alg/graph/fast/fast_graph_cls.py
  - cp_library/alg/graph/fast/static_graph_cls.py
  - cp_library/alg/graph/graph_weighted_proto.py
  - cp_library/alg/graph/graph_weighted_cls.py
  - cp_library/alg/graph/digraph_weighted_cls.py
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/tree_weighted_cls.py
  timestamp: '2024-11-28 18:07:28+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/abc375_g_find_bridges.test.py
  - test/shortest_path_min_heap.test.py
  - test/grl_1_b_bellman_ford.test.py
  - test/grl_1_a_graph_distance.test.py
  - test/grl_1_b_graph_bellman_ford.test.py
  - test/shortest_path_graph_weighted.test.py
  - test/grl_1_c_floyd_warshall.test.py
  - test/abc361_e_tree_diameter.test.py
  - test/abc218_f_shortest_path_weighted.test.py
  - test/shortest_path_static_graph_weighted.test.py
  - test/grl_2_a_graph_kruskal.test.py
  - test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - test/grl_1_a_dijkstra.test.py
documentation_of: cp_library/ds/priority_queue_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/priority_queue_cls.py
- /library/cp_library/ds/priority_queue_cls.py.html
title: cp_library/ds/priority_queue_cls.py
---
