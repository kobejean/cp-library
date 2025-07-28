---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heappop_fn.py
    title: cp_library/ds/heap/heappop_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heappush_fn.py
    title: cp_library/ds/heap/heappush_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heapsiftdown_fn.py
    title: cp_library/ds/heap/heapsiftdown_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heapsiftup_fn.py
    title: cp_library/ds/heap/heapsiftup_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\n\n\ndef heapsiftup(heap: list, pos: int):\n    n, item, c = len(heap)-1,\
    \ heap[pos], pos<<1|1\n    while c < n and heap[c := c+(heap[c+1]<heap[c])] <\
    \ item: heap[pos], pos, c = heap[c], c, c<<1|1\n    if c == n and heap[c] < item:\
    \ heap[pos], pos = heap[c], c\n    heap[pos] = item\n\ndef heappop(heap: list):\n\
    \    item = heap.pop()\n    if heap: item, heap[0] = heap[0], item; heapsiftup(heap,\
    \ 0)\n    return item\n\ndef heapsiftdown(heap: list, root: int, pos: int):\n\
    \    item = heap[pos]\n    while root < pos and item < heap[p := (pos-1)>>1]:\
    \ heap[pos], pos = heap[p], p\n    heap[pos] = item\n\ndef heappush(heap: list,\
    \ item):\n    heap.append(item)\n    heapsiftdown(heap, 0, len(heap)-1)\nfrom\
    \ collections import Counter, UserList\nfrom typing import Iterable\nfrom math\
    \ import inf\nfrom typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T');\
    \ _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3');\
    \ _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\nclass MinMultiset(UserList[_T]):\n\
    \    def __init__(self, iterable: Iterable = None, default = inf): self.data =\
    \ list(iterable) if iterable else []; self.default = default; self.counter = Counter(self.data)\n\
    \    def add(self, x: _T): self.counter[x] += 1; heappush(self.data, x)\n    def\
    \ remove(self, x: _T):\n        cnt, data = self.counter, self.data; cnt[x] -=\
    \ 1\n        while data and cnt[data[0]] == 0: heappop(data)\n    @property\n\
    \    def min(self): return self.data[0] if self.data else self.default\n"
  code: "import cp_library.ds.heap.__header__\nfrom cp_library.ds.heap.heappop_fn\
    \ import heappop\nfrom cp_library.ds.heap.heappush_fn import heappush\nfrom collections\
    \ import Counter, UserList\nfrom typing import Iterable\nfrom math import inf\n\
    from cp_library.misc.typing import _T\n\nclass MinMultiset(UserList[_T]):\n  \
    \  def __init__(self, iterable: Iterable = None, default = inf): self.data = list(iterable)\
    \ if iterable else []; self.default = default; self.counter = Counter(self.data)\n\
    \    def add(self, x: _T): self.counter[x] += 1; heappush(self.data, x)\n    def\
    \ remove(self, x: _T):\n        cnt, data = self.counter, self.data; cnt[x] -=\
    \ 1\n        while data and cnt[data[0]] == 0: heappop(data)\n    @property\n\
    \    def min(self): return self.data[0] if self.data else self.default\n"
  dependsOn:
  - cp_library/ds/heap/heappop_fn.py
  - cp_library/ds/heap/heappush_fn.py
  - cp_library/ds/heap/heapsiftup_fn.py
  - cp_library/ds/heap/heapsiftdown_fn.py
  isVerificationFile: false
  path: cp_library/ds/heap/min_multiset_cls.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/heap/min_multiset_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/min_multiset_cls.py
- /library/cp_library/ds/heap/min_multiset_cls.py.html
title: cp_library/ds/heap/min_multiset_cls.py
---
