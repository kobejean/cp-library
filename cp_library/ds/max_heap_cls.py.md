---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/ds/heap_proto.py
    title: cp_library/ds/heap_proto.py
  - icon: ':x:'
    path: cp_library/ds/heapq_max_import.py
    title: cp_library/ds/heapq_max_import.py
  _extendedRequiredBy:
  - icon: ':x:'
    path: cp_library/ds/min_k_heap_cls.py
    title: cp_library/ds/min_k_heap_cls.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/abc249_f_min_k_heap.test.py
    title: test/abc249_f_min_k_heap.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from collections import UserList\nfrom typing import Iterable, TypeVar\nT = TypeVar('T')\n\
    def heappop_max(heap: list[T], /) -> T: ...\ndef heapsiftdown_max(heap: list[T],\
    \ root: int, pos: int): ...\ndef heapsiftup_max(heap: list[T], pos: int): ...\n\
    def heapsiftdown(heap: list[T], root: int, pos: int): ...\ndef heapsiftup(heap:\
    \ list[T], pos: int): ...\n\nfrom heapq import (\n    _heapify_max as heapify_max,\
    \ \n    _heappop_max as heappop_max, \n    _siftdown_max as heapsiftdown_max,\n\
    \    _siftup_max as heapsiftup_max,\n    _siftdown as heapsiftdown,\n    _siftup\
    \ as heapsiftup\n)\n\ndef heappush_max(heap: list[T], item: T):\n    \"\"\"Push\
    \ item onto heap, maintaining the heap invariant.\"\"\"\n    heap.append(item)\n\
    \    heapsiftdown_max(heap, 0, len(heap)-1)\n\ndef heapreplace_max(heap: list[T],\
    \ item: T) -> T:\n    \"\"\"Pop and return the current largest value, and add\
    \ the new item.\n\n    This is more efficient than heappop_max() followed by heappush_max(),\
    \ and can be\n    more appropriate when using a fixed-size heap.  Note that the\
    \ value\n    returned may be larger than item!  That constrains reasonable uses\
    \ of\n    this routine unless written as part of a conditional replacement:\n\n\
    \        if item > heap[0]:\n            item = heapreplace_max(heap, item)\n\
    \    \"\"\"\n    returnitem = heap[0]\n    heap[0] = item\n    heapsiftup_max(heap,\
    \ 0)\n    return returnitem\n\ndef heapushpop_max(heap: list[T], item: T) -> T:\n\
    \    \"\"\"Fast version of a heappush_max followed by a heappop_max.\"\"\"\n \
    \   if heap and heap[0] > item:\n        item, heap[0] = heap[0], item\n     \
    \   heapsiftup_max(heap, 0)\n    return item\n\nfrom typing import Generic, TypeVar\n\
    \nT = TypeVar('T')\nclass HeapProtocol(Generic[T]):\n    def pop(self) -> T: ...\n\
    \    def push(self, item: T): ...\n    def pushpop(self, item: T) -> T: ...\n\
    \    def replace(self, item: T) -> T: ...\n\nT = TypeVar('T')\nclass MaxHeap(HeapProtocol[T],\
    \ UserList[T]):\n    \n    def __init__(self, iterable: Iterable[T] = None):\n\
    \        super().__init__(iterable)\n        heapify_max(self.data)\n    \n  \
    \  def pop(self):\n        return heappop_max(self.data)\n    \n    def push(self,\
    \ item: T):\n        heappush_max(self.data, item)\n\n    def pushpop(self, item:\
    \ T):\n        return heapushpop_max(self.data, item)\n    \n    def replace(self,\
    \ item: T):\n        return heapreplace_max(self.data, item)\n\n"
  code: "import cp_library.ds.__header__\nfrom collections import UserList\nfrom typing\
    \ import Iterable, TypeVar\nfrom cp_library.ds.heapq_max_import import heapify_max,\
    \ heappop_max, heappush_max, heapreplace_max, heapushpop_max\nfrom cp_library.ds.heap_proto\
    \ import HeapProtocol\n\nT = TypeVar('T')\nclass MaxHeap(HeapProtocol[T], UserList[T]):\n\
    \    \n    def __init__(self, iterable: Iterable[T] = None):\n        super().__init__(iterable)\n\
    \        heapify_max(self.data)\n    \n    def pop(self):\n        return heappop_max(self.data)\n\
    \    \n    def push(self, item: T):\n        heappush_max(self.data, item)\n\n\
    \    def pushpop(self, item: T):\n        return heapushpop_max(self.data, item)\n\
    \    \n    def replace(self, item: T):\n        return heapreplace_max(self.data,\
    \ item)\n\n"
  dependsOn:
  - cp_library/ds/heapq_max_import.py
  - cp_library/ds/heap_proto.py
  isVerificationFile: false
  path: cp_library/ds/max_heap_cls.py
  requiredBy:
  - cp_library/ds/min_k_heap_cls.py
  timestamp: '2024-11-28 18:07:28+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/abc249_f_min_k_heap.test.py
documentation_of: cp_library/ds/max_heap_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/max_heap_cls.py
- /library/cp_library/ds/max_heap_cls.py.html
title: cp_library/ds/max_heap_cls.py
---
