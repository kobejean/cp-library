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
    \n\n\nclass IntervalHeap:\n    def __init__(heap, x):\n        super().__init__()\n\
    \        heap._d = x\n        for i in range(len(x)): heap._up(0, i, i+1)\n\n\
    \    def push(heap, v):\n        heap._d.append(v)\n        heap._up(0, len(heap._d)-1,\
    \ len(heap._d))\n\n    def pop_min(heap):\n        v = heap._d.pop()\n       \
    \ if heap._d: v, heap._d[0] = heap._d[0], v; heap._up(0, heap._down(0), len(heap._d))\n\
    \        return v\n\n    def pop_max(heap):\n        v = heap._d.pop()\n     \
    \   if len(heap._d) >= 2: v, heap._d[1] = heap._d[1], v; heap._up(1, heap._down(1),\
    \ len(heap._d))\n        return v\n\n    def _up(heap, rt, k, n):\n        v =\
    \ (d := heap._d)[k]\n        if k|1 < n and d[k|1] < d[k&~1]: d[k] = d[k^1]; k\
    \ ^= 1\n        while rt <= (p := (k>>1)-1&~1) and v < d[p]: d[k], k = d[p], p\n\
    \        while rt <= (p := (k>>1)-1|1) and d[p] < v: d[k], k = d[p], p\n     \
    \   d[k] = v\n\n    def _down(heap, k):\n        n, v = len(d := heap._d), d[k]\n\
    \        if k & 1: # max heap\n            c = 2*k+1\n            while c < n:\n\
    \                if c+2 < n and d[c] < d[c+2]: c += 2\n                if v <\
    \ d[c]: d[k], k, c = d[c], c, 2*c+1\n                else: break\n        else:\
    \ # min heap\n            c = 2*k+2\n            while c < n:\n              \
    \  if c+2 < n and d[c+2] < d[c]: c += 2\n                if d[c] < v: d[k], k,\
    \ c = d[c], c, 2*c+2\n                else: break\n        d[k] = v\n        return\
    \ k\n"
  code: "import cp_library.__header__\nimport cp_library.ds.__header__\nimport cp_library.ds.heap.__header__\n\
    \nclass IntervalHeap:\n    def __init__(heap, x):\n        super().__init__()\n\
    \        heap._d = x\n        for i in range(len(x)): heap._up(0, i, i+1)\n\n\
    \    def push(heap, v):\n        heap._d.append(v)\n        heap._up(0, len(heap._d)-1,\
    \ len(heap._d))\n\n    def pop_min(heap):\n        v = heap._d.pop()\n       \
    \ if heap._d: v, heap._d[0] = heap._d[0], v; heap._up(0, heap._down(0), len(heap._d))\n\
    \        return v\n\n    def pop_max(heap):\n        v = heap._d.pop()\n     \
    \   if len(heap._d) >= 2: v, heap._d[1] = heap._d[1], v; heap._up(1, heap._down(1),\
    \ len(heap._d))\n        return v\n\n    def _up(heap, rt, k, n):\n        v =\
    \ (d := heap._d)[k]\n        if k|1 < n and d[k|1] < d[k&~1]: d[k] = d[k^1]; k\
    \ ^= 1\n        while rt <= (p := (k>>1)-1&~1) and v < d[p]: d[k], k = d[p], p\n\
    \        while rt <= (p := (k>>1)-1|1) and d[p] < v: d[k], k = d[p], p\n     \
    \   d[k] = v\n\n    def _down(heap, k):\n        n, v = len(d := heap._d), d[k]\n\
    \        if k & 1: # max heap\n            c = 2*k+1\n            while c < n:\n\
    \                if c+2 < n and d[c] < d[c+2]: c += 2\n                if v <\
    \ d[c]: d[k], k, c = d[c], c, 2*c+1\n                else: break\n        else:\
    \ # min heap\n            c = 2*k+2\n            while c < n:\n              \
    \  if c+2 < n and d[c+2] < d[c]: c += 2\n                if d[c] < v: d[k], k,\
    \ c = d[c], c, 2*c+2\n                else: break\n        d[k] = v\n        return\
    \ k\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/heap/interval_heap_cls.py
  requiredBy: []
  timestamp: '2025-04-03 08:59:41+09:00'
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
