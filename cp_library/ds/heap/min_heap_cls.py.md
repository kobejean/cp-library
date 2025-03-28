---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heap_proto.py
    title: cp_library/ds/heap/heap_proto.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/graph/shortest_path_fn.py
    title: cp_library/alg/graph/shortest_path_fn.py
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
    from collections import UserList\nfrom typing import Iterable\nfrom heapq import\
    \ heapify, heappop, heappush, heappushpop, heapreplace\nfrom typing import Generic\n\
    from typing import TypeVar\n_T = TypeVar('T')\n\nclass HeapProtocol(Generic[_T]):\n\
    \    def pop(self) -> _T: ...\n    def push(self, item: _T): ...\n    def pushpop(self,\
    \ item: _T) -> _T: ...\n    def replace(self, item: _T) -> _T: ...\n\nclass MinHeap(HeapProtocol[_T],\
    \ UserList[_T]):\n    def __init__(self, iterable: Iterable = None):\n       \
    \ super().__init__(iterable)\n        heapify(self.data)\n    \n    def pop(self):\
    \ return heappop(self.data)\n    def push(self, item: _T): heappush(self.data,\
    \ item)\n    def pushpop(self, item: _T): return heappushpop(self.data, item)\n\
    \    def replace(self, item: _T): return heapreplace(self.data, item)\n"
  code: "import cp_library.ds.heap.__header__\nfrom collections import UserList\n\
    from typing import Iterable\nfrom heapq import heapify, heappop, heappush, heappushpop,\
    \ heapreplace\nfrom cp_library.ds.heap.heap_proto import HeapProtocol\nfrom cp_library.misc.typing\
    \ import _T\n\nclass MinHeap(HeapProtocol[_T], UserList[_T]):\n    def __init__(self,\
    \ iterable: Iterable = None):\n        super().__init__(iterable)\n        heapify(self.data)\n\
    \    \n    def pop(self): return heappop(self.data)\n    def push(self, item:\
    \ _T): heappush(self.data, item)\n    def pushpop(self, item: _T): return heappushpop(self.data,\
    \ item)\n    def replace(self, item: _T): return heapreplace(self.data, item)\n"
  dependsOn:
  - cp_library/ds/heap/heap_proto.py
  isVerificationFile: false
  path: cp_library/ds/heap/min_heap_cls.py
  requiredBy:
  - cp_library/alg/graph/shortest_path_fn.py
  - cp_library/ds/heap/max_k_heap_cls.py
  timestamp: '2025-03-28 15:11:08+09:00'
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
