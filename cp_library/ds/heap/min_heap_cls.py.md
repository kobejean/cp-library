---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/fast_heapq.py
    title: cp_library/ds/heap/fast_heapq.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heap_proto.py
    title: cp_library/ds/heap/heap_proto.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/max_k_heap_cls.py
    title: cp_library/ds/heap/max_k_heap_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc249_f_max_k_heap.test.py
    title: test/atcoder/abc/abc249_f_max_k_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/shortest_path_min_heap.test.py
    title: test/library-checker/graph/shortest_path_min_heap.test.py
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
    from typing import Iterable\nfrom typing import TypeVar\n_S = TypeVar('S'); _T\
    \ = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    \n\n\ndef heappush(heap: list, item):\n    heap.append(item)\n    heapsiftdown(heap,\
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
    \ = heap[c], c\n    heap[pos] = item\nfrom typing import Generic\n\nclass HeapProtocol(Generic[_T]):\n\
    \    def peek(heap) -> _T: return heap.data[0]\n    def pop(heap) -> _T: ...\n\
    \    def push(heap, item: _T): ...\n    def pushpop(heap, item: _T) -> _T: ...\n\
    \    def replace(heap, item: _T) -> _T: ...\n    def __contains__(heap, item:\
    \ _T): return item in heap.data\n    def __len__(heap): return len(heap.data)\n\
    \    def clear(heap): heap.data.clear()\n\nclass MinHeap(HeapProtocol[_T]):\n\
    \    def __init__(self, iterable: Iterable = None): self.data = list(iterable)\
    \ if iterable else []; heapify(self.data)\n    def pop(self): return heappop(self.data)\n\
    \    def push(self, item: _T): heappush(self.data, item)\n    def pushpop(self,\
    \ item: _T): return heappushpop(self.data, item)\n    def replace(self, item:\
    \ _T): return heapreplace(self.data, item)\n"
  code: "import cp_library.__header__\nfrom typing import Iterable\nfrom cp_library.misc.typing\
    \ import _T\nimport cp_library.ds.__header__\nimport cp_library.ds.heap.__header__\n\
    from cp_library.ds.heap.fast_heapq import heapify, heappop, heappush, heappushpop,\
    \ heapreplace\nfrom cp_library.ds.heap.heap_proto import HeapProtocol\n\nclass\
    \ MinHeap(HeapProtocol[_T]):\n    def __init__(self, iterable: Iterable = None):\
    \ self.data = list(iterable) if iterable else []; heapify(self.data)\n    def\
    \ pop(self): return heappop(self.data)\n    def push(self, item: _T): heappush(self.data,\
    \ item)\n    def pushpop(self, item: _T): return heappushpop(self.data, item)\n\
    \    def replace(self, item: _T): return heapreplace(self.data, item)"
  dependsOn:
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/ds/heap/heap_proto.py
  isVerificationFile: false
  path: cp_library/ds/heap/min_heap_cls.py
  requiredBy:
  - cp_library/ds/heap/max_k_heap_cls.py
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/graph/shortest_path_min_heap.test.py
  - test/atcoder/abc/abc249_f_max_k_heap.test.py
documentation_of: cp_library/ds/heap/min_heap_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/min_heap_cls.py
- /library/cp_library/ds/heap/min_heap_cls.py.html
title: cp_library/ds/heap/min_heap_cls.py
---
