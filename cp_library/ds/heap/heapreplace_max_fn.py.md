---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heapsiftup_max_fn.py
    title: cp_library/ds/heap/heapsiftup_max_fn.py
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
    \n\n\ndef heapsiftup_max(heap: list, pos: int):\n    n, item, c = len(heap)-1,\
    \ heap[pos], pos<<1|1\n    while c < n and item < heap[c := c+(heap[c]<heap[c+1])]:\
    \ heap[pos], pos, c = heap[c], c, c<<1|1\n    if c == n and item < heap[c]: heap[pos],\
    \ pos = heap[c], c\n    heap[pos] = item\n\ndef heapreplace_max(heap: list, item):\n\
    \    item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n"
  code: "import cp_library.__header__\nimport cp_library.ds.__header__\nimport cp_library.ds.heap.__header__\n\
    from cp_library.ds.heap.heapsiftup_max_fn import heapsiftup_max\n\ndef heapreplace_max(heap:\
    \ list, item):\n    item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n \
    \   return item\n"
  dependsOn:
  - cp_library/ds/heap/heapsiftup_max_fn.py
  isVerificationFile: false
  path: cp_library/ds/heap/heapreplace_max_fn.py
  requiredBy:
  - cp_library/ds/heap/max_heap_cls.py
  - cp_library/ds/heap/min_k_heap_cls.py
  - cp_library/ds/heap/max_priority_queue_cls.py
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc249_f_min_k_heap.test.py
documentation_of: cp_library/ds/heap/heapreplace_max_fn.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/heapreplace_max_fn.py
- /library/cp_library/ds/heap/heapreplace_max_fn.py.html
title: cp_library/ds/heap/heapreplace_max_fn.py
---
