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
    path: cp_library/ds/heap/min_k_heap_cls.py
    title: cp_library/ds/heap/min_k_heap_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc249_f_min_k_heap.test.py
    title: test/atcoder/abc/abc249_f_min_k_heap.test.py
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
    from collections import UserList\nfrom typing import Iterable\n\ndef heappush(heap:\
    \ list, item):\n    heap.append(item)\n    heapsiftdown(heap, 0, len(heap)-1)\n\
    \ndef heappop(heap: list):\n    item = heap.pop()\n    if heap: item, heap[0]\
    \ = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapreplace(heap:\
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
    \ item: _T) -> _T: ...\n    def replace(self, item: _T) -> _T: ...\n\nclass MaxHeap(HeapProtocol[_T],\
    \ UserList[_T]):\n    def __init__(self, iterable: Iterable[_T] = None):\n   \
    \     super().__init__(iterable)\n        heapify_max(self.data)\n    def pop(self):\
    \ return heappop_max(self.data)\n    def push(self, item: _T): heappush_max(self.data,\
    \ item)\n    def pushpop(self, item: _T): return heappushpop_max(self.data, item)\n\
    \    def replace(self, item: _T): return heapreplace_max(self.data, item)\n"
  code: "import cp_library.ds.heap.__header__\nfrom collections import UserList\n\
    from typing import Iterable\nfrom cp_library.ds.heap.fast_heapq import heapify_max,\
    \ heappop_max, heappush_max, heapreplace_max, heappushpop_max\nfrom cp_library.ds.heap.heap_proto\
    \ import HeapProtocol\nfrom cp_library.misc.typing import _T\n\nclass MaxHeap(HeapProtocol[_T],\
    \ UserList[_T]):\n    def __init__(self, iterable: Iterable[_T] = None):\n   \
    \     super().__init__(iterable)\n        heapify_max(self.data)\n    def pop(self):\
    \ return heappop_max(self.data)\n    def push(self, item: _T): heappush_max(self.data,\
    \ item)\n    def pushpop(self, item: _T): return heappushpop_max(self.data, item)\n\
    \    def replace(self, item: _T): return heapreplace_max(self.data, item)\n"
  dependsOn:
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/ds/heap/heap_proto.py
  isVerificationFile: false
  path: cp_library/ds/heap/max_heap_cls.py
  requiredBy:
  - cp_library/ds/heap/min_k_heap_cls.py
  timestamp: '2025-04-25 16:40:50+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc249_f_min_k_heap.test.py
documentation_of: cp_library/ds/heap/max_heap_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/max_heap_cls.py
- /library/cp_library/ds/heap/max_heap_cls.py.html
title: cp_library/ds/heap/max_heap_cls.py
---
