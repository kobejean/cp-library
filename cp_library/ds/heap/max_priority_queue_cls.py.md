---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/fast_heapq.py
    title: cp_library/ds/heap/fast_heapq.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heap_proto.py
    title: cp_library/ds/heap/heap_proto.py
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
    \nfrom collections import UserList\n\ndef heappush(heap: list, item):\n    heap.append(item)\n\
    \    heapsiftdown(heap, 0, len(heap)-1)\n\ndef heappop(heap: list):\n    item\
    \ = heap.pop()\n    if heap: item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n\
    \    return item\n\ndef heapreplace(heap: list, item):\n    item, heap[0] = heap[0],\
    \ item; heapsiftup(heap, 0)\n    return item\n\ndef heappushpop(heap: list, item):\n\
    \    if heap and heap[0] < item: item, heap[0] = heap[0], item; heapsiftup(heap,\
    \ 0)\n    return item\n\ndef heapify(x: list):\n    for i in reversed(range(len(x)//2)):\
    \ heapsiftup(x, i)\n\ndef heapsiftdown(heap: list, root: int, pos: int):\n   \
    \ item = heap[pos]\n    while root < pos and item < heap[p := (pos-1)>>1]: heap[pos],\
    \ pos = heap[p], p\n    heap[pos] = item\n\ndef heapsiftup(heap: list, pos: int):\n\
    \    n, item, c = len(heap)-1, heap[pos], pos<<1|1\n    while c < n and heap[c\
    \ := c+(heap[c+1]<heap[c])] < item: heap[pos], pos, c = heap[c], c, c<<1|1\n \
    \   if c == n and heap[c] < item: heap[pos], pos = heap[c], c\n    heap[pos] =\
    \ item\n\ndef heappop_max(heap: list):\n    item = heap.pop()\n    if heap: item,\
    \ heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heapreplace_max(heap:\
    \ list, item):\n    item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n \
    \   return item\n\ndef heapify_max(x: list):\n    for i in reversed(range(len(x)//2)):\
    \ heapsiftup_max(x, i)\n\ndef heappush_max(heap: list, item):\n    heap.append(item);\
    \ heapsiftdown_max(heap, 0, len(heap)-1)\n\ndef heapreplace_max(heap: list, item):\n\
    \    item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\
    \ndef heappushpop_max(heap: list, item):\n    if heap and heap[0] > item: item,\
    \ heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heapsiftdown_max(heap:\
    \ list, root: int, pos: int):\n    item = heap[pos]\n    while root < pos and\
    \ heap[p := (pos-1)>>1] < item: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\
    \ndef heapsiftup_max(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and item < heap[c := c+(heap[c]<heap[c+1])]: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and item < heap[c]: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\n# def heapsiftdown(heap: list, root: int,\
    \ pos: int):\n#     item = heap[pos]\n#     while root < pos and item < heap[p\
    \ := (pos-1)>>1]: heap[pos], pos = heap[p], p\n#     heap[pos] = item\n\n# def\
    \ heapsiftup(heap: list, pos: int):\n#     n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n#     while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n#     if c == n and heap[c] < item: heap[pos],\
    \ pos = heap[c], c\n#     heap[pos] = item\nfrom typing import Generic\nfrom typing\
    \ import TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\n\nclass HeapProtocol(Generic[_T]):\n\
    \    def pop(self) -> _T: ...\n    def push(self, item: _T): ...\n    def pushpop(self,\
    \ item: _T) -> _T: ...\n    def replace(self, item: _T) -> _T: ...\n\nclass MaxPriorityQueue(HeapProtocol[int],\
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
    from cp_library.ds.heap.fast_heapq import heapify_max, heappop_max, heappush_max,\
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
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/ds/heap/heap_proto.py
  isVerificationFile: false
  path: cp_library/ds/heap/max_priority_queue_cls.py
  requiredBy: []
  timestamp: '2025-05-23 09:29:26+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/heap/max_priority_queue_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/max_priority_queue_cls.py
- /library/cp_library/ds/heap/max_priority_queue_cls.py.html
title: cp_library/ds/heap/max_priority_queue_cls.py
---
