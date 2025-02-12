---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heap_proto.py
    title: cp_library/ds/heap/heap_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/min_heap_cls.py
    title: cp_library/ds/heap/min_heap_cls.py
  _extendedRequiredBy: []
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
    from math import inf\n\nfrom collections import UserList\nfrom typing import Iterable\n\
    from heapq import heapify, heappop, heappush, heappushpop, heapreplace\nfrom typing\
    \ import Generic\nfrom typing import TypeVar\n_T = TypeVar('T')\n\nclass HeapProtocol(Generic[_T]):\n\
    \    def pop(self) -> _T: ...\n    def push(self, item: _T): ...\n    def pushpop(self,\
    \ item: _T) -> _T: ...\n    def replace(self, item: _T) -> _T: ...\n\nclass MinHeap(HeapProtocol[_T],\
    \ UserList[_T]):\n    def __init__(self, iterable: Iterable = None):\n       \
    \ super().__init__(iterable)\n        heapify(self.data)\n    \n    def pop(self):\
    \ return heappop(self.data)\n    def push(self, item: _T): heappush(self.data,\
    \ item)\n    def pushpop(self, item: _T): return heappushpop(self.data, item)\n\
    \    def replace(self, item: _T): return heapreplace(self.data, item)\n\ndef shortest_path(G,\
    \ s: int, g: int) -> tuple[list[int]|None,list[int]]:\n    D = [inf] * G.N\n \
    \   D[s] = 0\n    if s == g:\n        return [], D\n    par = [-1] * G.N\n   \
    \ par_edge = [-1] * G.N\n    Eid = G.edge_ids()\n    heap = MinHeap()\n    heap.push((0,\
    \ s))\n\n    while heap:\n        d, v = heap.pop()\n        if d > D[v]: continue\n\
    \        if v == g: break\n    \n        for i,(u, w, *_) in enumerate(G[v]):\n\
    \            if (nd := d + w) < D[u]:\n                D[u] = nd\n           \
    \     par[u] = v\n                par_edge[u] = Eid[v][i]\n                heap.push((nd,\
    \ u))\n    \n    if D[g] == inf:\n        return None, D\n        \n    path =\
    \ []\n    current = g\n    while current != s:\n        path.append(par_edge[current])\n\
    \        current = par[current]\n        \n    return path[::-1], D\n\n\n"
  code: "import cp_library.alg.graph.__header__\nfrom math import inf\nfrom cp_library.ds.heap.min_heap_cls\
    \ import MinHeap\n\ndef shortest_path(G, s: int, g: int) -> tuple[list[int]|None,list[int]]:\n\
    \    D = [inf] * G.N\n    D[s] = 0\n    if s == g:\n        return [], D\n   \
    \ par = [-1] * G.N\n    par_edge = [-1] * G.N\n    Eid = G.edge_ids()\n    heap\
    \ = MinHeap()\n    heap.push((0, s))\n\n    while heap:\n        d, v = heap.pop()\n\
    \        if d > D[v]: continue\n        if v == g: break\n    \n        for i,(u,\
    \ w, *_) in enumerate(G[v]):\n            if (nd := d + w) < D[u]:\n         \
    \       D[u] = nd\n                par[u] = v\n                par_edge[u] = Eid[v][i]\n\
    \                heap.push((nd, u))\n    \n    if D[g] == inf:\n        return\
    \ None, D\n        \n    path = []\n    current = g\n    while current != s:\n\
    \        path.append(par_edge[current])\n        current = par[current]\n    \
    \    \n    return path[::-1], D\n\n\n"
  dependsOn:
  - cp_library/ds/heap/min_heap_cls.py
  - cp_library/ds/heap/heap_proto.py
  isVerificationFile: false
  path: cp_library/alg/graph/shortest_path_fn.py
  requiredBy: []
  timestamp: '2025-02-12 22:25:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/graph/shortest_path_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/shortest_path_fn.py
- /library/cp_library/alg/graph/shortest_path_fn.py.html
title: cp_library/alg/graph/shortest_path_fn.py
---
