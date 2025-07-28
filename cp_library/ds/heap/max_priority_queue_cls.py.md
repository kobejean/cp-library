---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
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
    \n\n\nclass Packer:\n    __slots__ = 's', 'm'\n    def __init__(P, mx: int): P.s\
    \ = mx.bit_length(); P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int): return\
    \ a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return x >> P.s, x\
    \ & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A), reverse);\
    \ return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n  \
    \          for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n     \
    \       for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\n\n\n\ndef heappush(heap: list, item):\n    heap.append(item)\n\
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
    \ = heap[c], c\n    heap[pos] = item\nfrom typing import Generic\nfrom typing\
    \ import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U'); _T1\
    \ = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4');\
    \ _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\nclass HeapProtocol(Generic[_T]):\n\
    \    def peek(heap) -> _T: return heap.data[0]\n    def pop(heap) -> _T: ...\n\
    \    def push(heap, item: _T): ...\n    def pushpop(heap, item: _T) -> _T: ...\n\
    \    def replace(heap, item: _T) -> _T: ...\n    def __contains__(heap, item:\
    \ _T): return item in heap.data\n    def __len__(heap): return len(heap.data)\n\
    \    def clear(heap): heap.data.clear()\n\nclass MaxPriorityQueue(HeapProtocol[int]):\n\
    \    def __init__(que, N: int, ids: list[int] = None, priorities: list[int] =\
    \ None, /):\n        que.pkr = Packer(N)\n        if ids is None: que.data = elist(N)\n\
    \        elif priorities is None: heapify_max(ids); que.data = ids\n        else:\n\
    \            que.data = [0]*(M := len(ids))\n            for i in range(M): que.data[i]\
    \ = que.pkr.enc(priorities[i], ids[i])\n            heapify_max(que.data)\n  \
    \  def pop(que): return que.pkr.dec(heappop_max(que.data))\n    def push(que,\
    \ priority: int, id: int): heappush_max(que.data, que.pkr.enc(priority, id))\n\
    \    def pushpop(que, priority: int, id: int): return que.pkr.dec(heappushpop_max(que.data,\
    \ que.pkr.enc(priority, id)))\n    def replace(que, priority: int, id: int): return\
    \ que.pkr.dec(heapreplace_max(que.data, que.pkr.enc(priority, id)))\n    def peek(que):\
    \ return que.pkr.dec(que.data[0])\n\ndef elist(est_len: int) -> list: ...\ntry:\n\
    \    from __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n\
    \        return []\nelist = newlist_hint\n    \n"
  code: "import cp_library.__header__\nfrom cp_library.bit.pack.packer_cls import\
    \ Packer\nimport cp_library.ds.__header__\nimport cp_library.ds.heap.__header__\n\
    from cp_library.ds.heap.fast_heapq import heapify_max, heappop_max, heappush_max,\
    \ heappushpop_max, heapreplace_max\nfrom cp_library.ds.heap.heap_proto import\
    \ HeapProtocol\n\nclass MaxPriorityQueue(HeapProtocol[int]):\n    def __init__(que,\
    \ N: int, ids: list[int] = None, priorities: list[int] = None, /):\n        que.pkr\
    \ = Packer(N)\n        if ids is None: que.data = elist(N)\n        elif priorities\
    \ is None: heapify_max(ids); que.data = ids\n        else:\n            que.data\
    \ = [0]*(M := len(ids))\n            for i in range(M): que.data[i] = que.pkr.enc(priorities[i],\
    \ ids[i])\n            heapify_max(que.data)\n    def pop(que): return que.pkr.dec(heappop_max(que.data))\n\
    \    def push(que, priority: int, id: int): heappush_max(que.data, que.pkr.enc(priority,\
    \ id))\n    def pushpop(que, priority: int, id: int): return que.pkr.dec(heappushpop_max(que.data,\
    \ que.pkr.enc(priority, id)))\n    def replace(que, priority: int, id: int): return\
    \ que.pkr.dec(heapreplace_max(que.data, que.pkr.enc(priority, id)))\n    def peek(que):\
    \ return que.pkr.dec(que.data[0])\nfrom cp_library.ds.elist_fn import elist"
  dependsOn:
  - cp_library/bit/pack/packer_cls.py
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/ds/heap/heap_proto.py
  - cp_library/ds/elist_fn.py
  isVerificationFile: false
  path: cp_library/ds/heap/max_priority_queue_cls.py
  requiredBy: []
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/heap/max_priority_queue_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/max_priority_queue_cls.py
- /library/cp_library/ds/heap/max_priority_queue_cls.py.html
title: cp_library/ds/heap/max_priority_queue_cls.py
---
