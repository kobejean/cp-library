---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/graph/digraph_weighted_cls.py
    title: cp_library/alg/graph/digraph_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/digraph_weighted_cls.py
    title: cp_library/alg/graph/fast/digraph_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/graph_weighted_base_cls.py
    title: cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/graph_weighted_cls.py
    title: cp_library/alg/graph/fast/graph_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/graph_weighted_cls.py
    title: cp_library/alg/graph/graph_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/graph_weighted_proto.py
    title: cp_library/alg/graph/graph_weighted_proto.py
  - icon: ':warning:'
    path: cp_library/alg/graph/shortest_path_fn.py
    title: cp_library/alg/graph/shortest_path_fn.py
  - icon: ':warning:'
    path: cp_library/alg/tree/fast/tree_weighted_base_cls.py
    title: cp_library/alg/tree/fast/tree_weighted_base_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/fast/tree_weighted_cls.py
    title: cp_library/alg/tree/fast/tree_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/tree_weighted_proto.py
    title: cp_library/alg/tree/tree_weighted_proto.py
  - icon: ':warning:'
    path: cp_library/ds/heap/k_heap_mixin.py
    title: cp_library/ds/heap/k_heap_mixin.py
  - icon: ':warning:'
    path: cp_library/ds/heap/max_heap_cls.py
    title: cp_library/ds/heap/max_heap_cls.py
  - icon: ':warning:'
    path: cp_library/ds/heap/max_k_heap_cls.py
    title: cp_library/ds/heap/max_k_heap_cls.py
  - icon: ':warning:'
    path: cp_library/ds/heap/max_priority_queue_cls.py
    title: cp_library/ds/heap/max_priority_queue_cls.py
  - icon: ':warning:'
    path: cp_library/ds/heap/min_heap_cls.py
    title: cp_library/ds/heap/min_heap_cls.py
  - icon: ':warning:'
    path: cp_library/ds/heap/min_k_heap_cls.py
    title: cp_library/ds/heap/min_k_heap_cls.py
  - icon: ':warning:'
    path: cp_library/ds/heap/priority_queue_cls.py
    title: cp_library/ds/heap/priority_queue_cls.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from typing import Generic, TypeVar\n\nT = TypeVar('T')\nclass HeapProtocol(Generic[T]):\n\
    \    def pop(self) -> T: ...\n    def push(self, item: T): ...\n    def pushpop(self,\
    \ item: T) -> T: ...\n    def replace(self, item: T) -> T: ...\n"
  code: "import cp_library.ds.__header__\nfrom typing import Generic, TypeVar\n\n\
    T = TypeVar('T')\nclass HeapProtocol(Generic[T]):\n    def pop(self) -> T: ...\n\
    \    def push(self, item: T): ...\n    def pushpop(self, item: T) -> T: ...\n\
    \    def replace(self, item: T) -> T: ..."
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/heap/heap_proto.py
  requiredBy:
  - cp_library/alg/tree/tree_weighted_cls.py
  - cp_library/alg/tree/fast/tree_weighted_cls.py
  - cp_library/alg/tree/fast/tree_weighted_base_cls.py
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/graph/graph_weighted_cls.py
  - cp_library/alg/graph/fast/graph_weighted_cls.py
  - cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - cp_library/alg/graph/fast/digraph_weighted_cls.py
  - cp_library/alg/graph/graph_weighted_proto.py
  - cp_library/alg/graph/digraph_weighted_cls.py
  - cp_library/alg/graph/shortest_path_fn.py
  - cp_library/ds/heap/priority_queue_cls.py
  - cp_library/ds/heap/min_heap_cls.py
  - cp_library/ds/heap/k_heap_mixin.py
  - cp_library/ds/heap/min_k_heap_cls.py
  - cp_library/ds/heap/max_priority_queue_cls.py
  - cp_library/ds/heap/max_k_heap_cls.py
  - cp_library/ds/heap/max_heap_cls.py
  timestamp: '2024-12-17 23:23:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/heap/heap_proto.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/heap_proto.py
- /library/cp_library/ds/heap/heap_proto.py.html
title: cp_library/ds/heap/heap_proto.py
---
