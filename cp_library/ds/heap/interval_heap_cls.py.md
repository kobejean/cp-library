---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/double_ended_priority_queue.test.py
    title: test/library-checker/data-structure/double_ended_priority_queue.test.py
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
    \n\n\nclass IntervalHeap:\n    def __init__(heap, arr: list):\n        heap._d\
    \ = arr\n        for k in range(len(arr)): heap._up(k)\n\n    def push(heap, item):\n\
    \        heap._d.append(item)\n        heap._up(len(heap._d)-1)\n\n    def pop_min(heap):\n\
    \        item = heap._d.pop()\n        if heap._d: item, heap._d[0] = heap._d[0],\
    \ item; heap._down(0)\n        return item\n\n    def pop_max(heap):\n       \
    \ item = heap._d.pop()\n        if len(heap._d) >= 2: item, heap._d[1] = heap._d[1],\
    \ item; heap._down(1)\n        return item\n\n    def _up(heap, k):\n        v\
    \ = heap._d[k]\n        if k&1 and heap._d[k] < heap._d[k-1]: heap._d[k] = heap._d[k-1];\
    \ k ^= 1\n        while 0 <= (p := (k>>1)-1&~1) and v < heap._d[p]: heap._d[k],\
    \ k = heap._d[p], p\n        while 0 <= (p := (k>>1)-1|1) and heap._d[p] < v:\
    \ heap._d[k], k = heap._d[p], p\n        heap._d[k] = v\n\n    def _down(heap,\
    \ k):\n        n, v, rt = len(d := heap._d)-2, d[k], k\n        if k & 1: # max\
    \ heap\n            c = 2*k+1\n            while c < n and v < d[c := c+2 if d[c]\
    \ < d[c+2] else c]: d[k], k, c = d[c], c, c<<1|1\n            if c < n+2 and v\
    \ < d[c]: d[k], k = d[c], c\n            d[k] = v\n            if v < d[k-1]:\n\
    \                d[k] = d[k-1]; k ^= 1\n                while rt <= (p := (k>>1)-1&~1)\
    \ and v < d[p]: d[k], k = d[p], p\n                d[k] = v\n        else: # min\
    \ heap\n            c = (k+1)<<1\n            while c < n and d[c := c+2 if d[c+2]\
    \ < d[c] else c] < v: d[k], k, c = d[c], c, (c+1)<<1\n            if c < n+2 and\
    \ d[c] < v: d[k], k = d[c], c\n            d[k] = v\n            if k+1 < n+2\
    \ and d[k+1] < d[k]:\n                d[k] = d[k+1]; k ^= 1\n                while\
    \ rt <= (p := (k>>1)-1|1) and d[p] < v: d[k], k = d[p], p\n                d[k]\
    \ = v\n"
  code: "import cp_library.__header__\nimport cp_library.ds.__header__\nimport cp_library.ds.heap.__header__\n\
    \nclass IntervalHeap:\n    def __init__(heap, arr: list):\n        heap._d = arr\n\
    \        for k in range(len(arr)): heap._up(k)\n\n    def push(heap, item):\n\
    \        heap._d.append(item)\n        heap._up(len(heap._d)-1)\n\n    def pop_min(heap):\n\
    \        item = heap._d.pop()\n        if heap._d: item, heap._d[0] = heap._d[0],\
    \ item; heap._down(0)\n        return item\n\n    def pop_max(heap):\n       \
    \ item = heap._d.pop()\n        if len(heap._d) >= 2: item, heap._d[1] = heap._d[1],\
    \ item; heap._down(1)\n        return item\n\n    def _up(heap, k):\n        v\
    \ = heap._d[k]\n        if k&1 and heap._d[k] < heap._d[k-1]: heap._d[k] = heap._d[k-1];\
    \ k ^= 1\n        while 0 <= (p := (k>>1)-1&~1) and v < heap._d[p]: heap._d[k],\
    \ k = heap._d[p], p\n        while 0 <= (p := (k>>1)-1|1) and heap._d[p] < v:\
    \ heap._d[k], k = heap._d[p], p\n        heap._d[k] = v\n\n    def _down(heap,\
    \ k):\n        n, v, rt = len(d := heap._d)-2, d[k], k\n        if k & 1: # max\
    \ heap\n            c = 2*k+1\n            while c < n and v < d[c := c+2 if d[c]\
    \ < d[c+2] else c]: d[k], k, c = d[c], c, c<<1|1\n            if c < n+2 and v\
    \ < d[c]: d[k], k = d[c], c\n            d[k] = v\n            if v < d[k-1]:\n\
    \                d[k] = d[k-1]; k ^= 1\n                while rt <= (p := (k>>1)-1&~1)\
    \ and v < d[p]: d[k], k = d[p], p\n                d[k] = v\n        else: # min\
    \ heap\n            c = (k+1)<<1\n            while c < n and d[c := c+2 if d[c+2]\
    \ < d[c] else c] < v: d[k], k, c = d[c], c, (c+1)<<1\n            if c < n+2 and\
    \ d[c] < v: d[k], k = d[c], c\n            d[k] = v\n            if k+1 < n+2\
    \ and d[k+1] < d[k]:\n                d[k] = d[k+1]; k ^= 1\n                while\
    \ rt <= (p := (k>>1)-1|1) and d[p] < v: d[k], k = d[p], p\n                d[k]\
    \ = v"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/heap/interval_heap_cls.py
  requiredBy: []
  timestamp: '2025-05-20 13:05:58+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/double_ended_priority_queue.test.py
documentation_of: cp_library/ds/heap/interval_heap_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/interval_heap_cls.py
- /library/cp_library/ds/heap/interval_heap_cls.py.html
title: cp_library/ds/heap/interval_heap_cls.py
---
