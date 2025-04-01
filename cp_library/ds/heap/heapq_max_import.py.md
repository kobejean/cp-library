---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/max_heap_cls.py
    title: cp_library/ds/heap/max_heap_cls.py
  - icon: ':warning:'
    path: cp_library/ds/heap/max_priority_queue_cls.py
    title: cp_library/ds/heap/max_priority_queue_cls.py
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
    from typing import TypeVar\n_T = TypeVar('T')\ndef heappop_max(heap: list[_T],\
    \ /) -> _T: ...\ndef heapsiftdown_max(heap: list[_T], root: int, pos: int): ...\n\
    def heapsiftup_max(heap: list[_T], pos: int): ...\ndef heapsiftdown(heap: list[_T],\
    \ root: int, pos: int): ...\ndef heapsiftup(heap: list[_T], pos: int): ...\n\n\
    from heapq import (\n    _heapify_max as heapify_max, \n    _heappop_max as heappop_max,\
    \ \n    _siftdown_max as heapsiftdown_max,\n    _siftup_max as heapsiftup_max,\n\
    \    _siftdown as heapsiftdown,\n    _siftup as heapsiftup\n)\n\ndef heappush_max(heap:\
    \ list[_T], item: _T):\n    '''Push item onto heap, maintaining the heap invariant.'''\n\
    \    heap.append(item)\n    heapsiftdown_max(heap, 0, len(heap)-1)\n\ndef heapreplace_max(heap:\
    \ list[_T], item: _T) -> _T:\n    '''Pop and return the current largest value,\
    \ and add the new item.\n\n    This is more efficient than heappop_max() followed\
    \ by heappush_max(), and can be\n    more appropriate when using a fixed-size\
    \ heap.  Note that the value\n    returned may be larger than item!  That constrains\
    \ reasonable uses of\n    this routine unless written as part of a conditional\
    \ replacement:\n\n        if item > heap[0]:\n            item = heapreplace_max(heap,\
    \ item)\n    '''\n    returnitem = heap[0]\n    heap[0] = item\n    heapsiftup_max(heap,\
    \ 0)\n    return returnitem\n\ndef heappushpop_max(heap: list[_T], item: _T) ->\
    \ _T:\n    '''Fast version of a heappush_max followed by a heappop_max.'''\n \
    \   if heap and heap[0] > item:\n        item, heap[0] = heap[0], item\n     \
    \   heapsiftup_max(heap, 0)\n    return item\n\n"
  code: "import cp_library.ds.heap.__header__\nfrom cp_library.misc.typing import\
    \ _T\ndef heappop_max(heap: list[_T], /) -> _T: ...\ndef heapsiftdown_max(heap:\
    \ list[_T], root: int, pos: int): ...\ndef heapsiftup_max(heap: list[_T], pos:\
    \ int): ...\ndef heapsiftdown(heap: list[_T], root: int, pos: int): ...\ndef heapsiftup(heap:\
    \ list[_T], pos: int): ...\n\nfrom heapq import (\n    _heapify_max as heapify_max,\
    \ \n    _heappop_max as heappop_max, \n    _siftdown_max as heapsiftdown_max,\n\
    \    _siftup_max as heapsiftup_max,\n    _siftdown as heapsiftdown,\n    _siftup\
    \ as heapsiftup\n)\n\ndef heappush_max(heap: list[_T], item: _T):\n    '''Push\
    \ item onto heap, maintaining the heap invariant.'''\n    heap.append(item)\n\
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
    \   heapsiftup_max(heap, 0)\n    return item\n\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/heap/heapq_max_import.py
  requiredBy:
  - cp_library/ds/heap/max_priority_queue_cls.py
  - cp_library/ds/heap/max_heap_cls.py
  - cp_library/ds/heap/min_k_heap_cls.py
  timestamp: '2025-04-02 01:29:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc249_f_min_k_heap.test.py
documentation_of: cp_library/ds/heap/heapq_max_import.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/heapq_max_import.py
- /library/cp_library/ds/heap/heapq_max_import.py.html
title: cp_library/ds/heap/heapq_max_import.py
---
