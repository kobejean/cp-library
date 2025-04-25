---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/fast_heapq.py
    title: cp_library/ds/heap/fast_heapq.py
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
    \ndef heappush(heap: list, item):\n    heap.append(item)\n    heapsiftdown(heap,\
    \ 0, len(heap)-1)\n\ndef heappop(heap: list):\n    item = heap.pop()\n    if heap:\
    \ item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapreplace(heap:\
    \ list, item):\n    item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return\
    \ item\n\ndef heappushpop(heap: list, item):\n    if heap and heap[0] < item:\
    \ item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapify(x:\
    \ list):\n    for i in reversed(range(len(x)//2)): heapsiftup(x, i)\n\ndef heapsiftdown(heap:\
    \ list, root: int, pos: int):\n    item = heap[pos]\n    while root < pos and\
    \ item < heap[p := (pos-1)>>1]: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\
    \ndef heapsiftup(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and heap[c] < item: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\ndef heappop_max(heap: list):\n    item\
    \ = heap.pop()\n    if heap: item, heap[0] = heap[0], item; heapsiftup_max(heap,\
    \ 0)\n    return item\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heapify_max(x:\
    \ list):\n    for i in reversed(range(len(x)//2)): heapsiftup_max(x, i)\n\ndef\
    \ heappush_max(heap: list, item):\n    heap.append(item); heapsiftdown_max(heap,\
    \ 0, len(heap)-1)\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heappushpop_max(heap:\
    \ list, item):\n    if heap and heap[0] > item: item, heap[0] = heap[0], item;\
    \ heapsiftup_max(heap, 0)\n    return item\n\ndef heapsiftdown_max(heap: list,\
    \ root: int, pos: int):\n    item = heap[pos]\n    while root < pos and heap[p\
    \ := (pos-1)>>1] < item: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\n\
    def heapsiftup_max(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and item < heap[c := c+(heap[c]<heap[c+1])]: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and item < heap[c]: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\n# def heapsiftdown(heap: list, root: int,\
    \ pos: int):\n#     item = heap[pos]\n#     while root < pos and item < heap[p\
    \ := (pos-1)>>1]: heap[pos], pos = heap[p], p\n#     heap[pos] = item\n\n# def\
    \ heapsiftup(heap: list, pos: int):\n#     n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n#     while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n#     if c == n and heap[c] < item: heap[pos],\
    \ pos = heap[c], c\n#     heap[pos] = item\nfrom typing import Generic\nfrom typing\
    \ import TypeVar\n_T = TypeVar('T')\n\nclass HeapProtocol(Generic[_T]):\n    def\
    \ pop(self) -> _T: ...\n    def push(self, item: _T): ...\n    def pushpop(self,\
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
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/ds/heap/heap_proto.py
  isVerificationFile: false
  path: cp_library/alg/graph/shortest_path_fn.py
  requiredBy: []
  timestamp: '2025-04-25 16:40:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/graph/shortest_path_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/shortest_path_fn.py
- /library/cp_library/alg/graph/shortest_path_fn.py.html
title: cp_library/alg/graph/shortest_path_fn.py
---
