---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heap_proto.py
    title: cp_library/ds/heap/heap_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heapq_max_import.py
    title: cp_library/ds/heap/heapq_max_import.py
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
    \nfrom collections import UserList\nfrom typing import TypeVar\nT = TypeVar('T')\n\
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
    \ 0)\n    return returnitem\n\ndef heappushpop_max(heap: list[T], item: T) ->\
    \ T:\n    \"\"\"Fast version of a heappush_max followed by a heappop_max.\"\"\"\
    \n    if heap and heap[0] > item:\n        item, heap[0] = heap[0], item\n   \
    \     heapsiftup_max(heap, 0)\n    return item\n\nfrom typing import Generic,\
    \ TypeVar\n\nT = TypeVar('T')\nclass HeapProtocol(Generic[T]):\n    def pop(self)\
    \ -> T: ...\n    def push(self, item: T): ...\n    def pushpop(self, item: T)\
    \ -> T: ...\n    def replace(self, item: T) -> T: ...\n\nclass MaxPriorityQueue(HeapProtocol[int],\
    \ UserList[int]):\n    \n    def __init__(self, N: int, ids: list[int] = None,\
    \ priorities: list[int] = None, /):\n        self.shift = N.bit_length()\n   \
    \     self.mask = (1 << self.shift)-1\n        if ids is None:\n            super().__init__()\n\
    \        elif priorities is None:\n            heapify_max(ids)\n            self.data\
    \ = ids\n        else:\n            M = len(ids)\n            data = [0]*M\n \
    \           for i in range(M):\n                data[i] = self.encode(ids[i],\
    \ priorities[i]) \n            heapify_max(data)\n            self.data = data\n\
    \n    def encode(self, id, priority):\n        return priority << self.shift |\
    \ id\n    \n    def decode(self, encoded):\n        return self.mask & encoded,\
    \ encoded >> self.shift\n    \n    def pop(self):\n        return self.decode(heappop_max(self.data))\n\
    \    \n    def push(self, id: int, priority: int):\n        heappush_max(self.data,\
    \ self.encode(id, priority))\n\n    def pushpop(self, id: int, priority: int):\n\
    \        return self.decode(heappushpop_max(self.data, self.encode(id, priority)))\n\
    \    \n    def replace(self, id: int, priority: int):\n        return self.decode(heapreplace_max(self.data,\
    \ self.encode(id, priority)))\n\n    def peek(self):\n        return self.decode(self.data[0])\n"
  code: "import cp_library.ds.heap.__header__\n\nfrom collections import UserList\n\
    from cp_library.ds.heap.heapq_max_import import heapify_max, heappop_max, heappush_max,\
    \ heappushpop_max, heapreplace_max\nfrom cp_library.ds.heap.heap_proto import\
    \ HeapProtocol\n\nclass MaxPriorityQueue(HeapProtocol[int], UserList[int]):\n\
    \    \n    def __init__(self, N: int, ids: list[int] = None, priorities: list[int]\
    \ = None, /):\n        self.shift = N.bit_length()\n        self.mask = (1 <<\
    \ self.shift)-1\n        if ids is None:\n            super().__init__()\n   \
    \     elif priorities is None:\n            heapify_max(ids)\n            self.data\
    \ = ids\n        else:\n            M = len(ids)\n            data = [0]*M\n \
    \           for i in range(M):\n                data[i] = self.encode(ids[i],\
    \ priorities[i]) \n            heapify_max(data)\n            self.data = data\n\
    \n    def encode(self, id, priority):\n        return priority << self.shift |\
    \ id\n    \n    def decode(self, encoded):\n        return self.mask & encoded,\
    \ encoded >> self.shift\n    \n    def pop(self):\n        return self.decode(heappop_max(self.data))\n\
    \    \n    def push(self, id: int, priority: int):\n        heappush_max(self.data,\
    \ self.encode(id, priority))\n\n    def pushpop(self, id: int, priority: int):\n\
    \        return self.decode(heappushpop_max(self.data, self.encode(id, priority)))\n\
    \    \n    def replace(self, id: int, priority: int):\n        return self.decode(heapreplace_max(self.data,\
    \ self.encode(id, priority)))\n\n    def peek(self):\n        return self.decode(self.data[0])"
  dependsOn:
  - cp_library/ds/heap/heapq_max_import.py
  - cp_library/ds/heap/heap_proto.py
  isVerificationFile: false
  path: cp_library/ds/heap/max_priority_queue_cls.py
  requiredBy: []
  timestamp: '2024-12-30 17:25:46+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/heap/max_priority_queue_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/max_priority_queue_cls.py
- /library/cp_library/ds/heap/max_priority_queue_cls.py.html
title: cp_library/ds/heap/max_priority_queue_cls.py
---
