---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heap_proto.py
    title: cp_library/ds/heap/heap_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heapq_max_import.py
    title: cp_library/ds/heap/heapq_max_import.py
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
    from collections import UserList\nfrom typing import Iterable\nfrom typing import\
    \ TypeVar\n_T = TypeVar('T')\ndef heappop_max(heap: list[_T], /) -> _T: ...\n\
    def heapsiftdown_max(heap: list[_T], root: int, pos: int): ...\ndef heapsiftup_max(heap:\
    \ list[_T], pos: int): ...\ndef heapsiftdown(heap: list[_T], root: int, pos: int):\
    \ ...\ndef heapsiftup(heap: list[_T], pos: int): ...\n\nfrom heapq import (\n\
    \    _heapify_max as heapify_max, \n    _heappop_max as heappop_max, \n    _siftdown_max\
    \ as heapsiftdown_max,\n    _siftup_max as heapsiftup_max,\n    _siftdown as heapsiftdown,\n\
    \    _siftup as heapsiftup\n)\n\ndef heappush_max(heap: list[_T], item: _T):\n\
    \    '''Push item onto heap, maintaining the heap invariant.'''\n    heap.append(item)\n\
    \    heapsiftdown_max(heap, 0, len(heap)-1)\n\ndef heapreplace_max(heap: list[_T],\
    \ item: _T) -> _T:\n    '''Pop and return the current largest value, and add the\
    \ new item.\n\n    This is more efficient than heappop_max() followed by heappush_max(),\
    \ and can be\n    more appropriate when using a fixed-size heap.  Note that the\
    \ value\n    returned may be larger than item!  That constrains reasonable uses\
    \ of\n    this routine unless written as part of a conditional replacement:\n\n\
    \        if item > heap[0]:\n            item = heapreplace_max(heap, item)\n\
    \    '''\n    returnitem = heap[0]\n    heap[0] = item\n    heapsiftup_max(heap,\
    \ 0)\n    return returnitem\n\ndef heappushpop_max(heap: list[_T], item: _T) ->\
    \ _T:\n    '''Fast version of a heappush_max followed by a heappop_max.'''\n \
    \   if heap and heap[0] > item:\n        item, heap[0] = heap[0], item\n     \
    \   heapsiftup_max(heap, 0)\n    return item\n\nfrom typing import Generic\n\n\
    class HeapProtocol(Generic[_T]):\n    def pop(self) -> _T: ...\n    def push(self,\
    \ item: _T): ...\n    def pushpop(self, item: _T) -> _T: ...\n    def replace(self,\
    \ item: _T) -> _T: ...\n\nclass MaxHeap(HeapProtocol[_T], UserList[_T]):\n   \
    \ def __init__(self, iterable: Iterable[_T] = None):\n        super().__init__(iterable)\n\
    \        heapify_max(self.data)\n    def pop(self): return heappop_max(self.data)\n\
    \    def push(self, item: _T): heappush_max(self.data, item)\n    def pushpop(self,\
    \ item: _T): return heappushpop_max(self.data, item)\n    def replace(self, item:\
    \ _T): return heapreplace_max(self.data, item)\n"
  code: "import cp_library.ds.heap.__header__\nfrom collections import UserList\n\
    from typing import Iterable\nfrom cp_library.ds.heap.heapq_max_import import heapify_max,\
    \ heappop_max, heappush_max, heapreplace_max, heappushpop_max\nfrom cp_library.ds.heap.heap_proto\
    \ import HeapProtocol\nfrom cp_library.misc.typing import _T\n\nclass MaxHeap(HeapProtocol[_T],\
    \ UserList[_T]):\n    def __init__(self, iterable: Iterable[_T] = None):\n   \
    \     super().__init__(iterable)\n        heapify_max(self.data)\n    def pop(self):\
    \ return heappop_max(self.data)\n    def push(self, item: _T): heappush_max(self.data,\
    \ item)\n    def pushpop(self, item: _T): return heappushpop_max(self.data, item)\n\
    \    def replace(self, item: _T): return heapreplace_max(self.data, item)\n"
  dependsOn:
  - cp_library/ds/heap/heapq_max_import.py
  - cp_library/ds/heap/heap_proto.py
  isVerificationFile: false
  path: cp_library/ds/heap/max_heap_cls.py
  requiredBy:
  - cp_library/ds/heap/min_k_heap_cls.py
  timestamp: '2025-03-28 21:58:31+09:00'
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
