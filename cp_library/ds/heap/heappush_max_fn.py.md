---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heapsiftdown_max_fn.py
    title: cp_library/ds/heap/heapsiftdown_max_fn.py
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
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/double_ended_priority_queue_2heaps_fast_heapq.test.py
    title: test/library-checker/data-structure/double_ended_priority_queue_2heaps_fast_heapq.test.py
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
    \n\n\ndef heapsiftdown_max(heap: list, root: int, pos: int):\n    item = heap[pos]\n\
    \    while root < pos and heap[p := (pos-1)>>1] < item: heap[pos], pos = heap[p],\
    \ p\n    heap[pos] = item\n\ndef heappush_max(heap: list, item):\n    heap.append(item);\
    \ heapsiftdown_max(heap, 0, len(heap)-1)\n"
  code: "import cp_library.__header__\nimport cp_library.ds.__header__\nimport cp_library.ds.heap.__header__\n\
    from cp_library.ds.heap.heapsiftdown_max_fn import heapsiftdown_max\n\ndef heappush_max(heap:\
    \ list, item):\n    heap.append(item); heapsiftdown_max(heap, 0, len(heap)-1)\n"
  dependsOn:
  - cp_library/ds/heap/heapsiftdown_max_fn.py
  isVerificationFile: false
  path: cp_library/ds/heap/heappush_max_fn.py
  requiredBy:
  - cp_library/ds/heap/max_heap_cls.py
  - cp_library/ds/heap/min_k_heap_cls.py
  - cp_library/ds/heap/max_priority_queue_cls.py
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/double_ended_priority_queue_2heaps_fast_heapq.test.py
  - test/atcoder/abc/abc249_f_min_k_heap.test.py
documentation_of: cp_library/ds/heap/heappush_max_fn.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/heappush_max_fn.py
- /library/cp_library/ds/heap/heappush_max_fn.py.html
title: cp_library/ds/heap/heappush_max_fn.py
---
