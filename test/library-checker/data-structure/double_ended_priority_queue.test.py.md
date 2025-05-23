---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/interval_heap_cls.py
    title: cp_library/ds/heap/interval_heap_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/reserve_fn.py
    title: cp_library/ds/reserve_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast/fast_io_fn.py
    title: cp_library/io/fast/fast_io_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/double_ended_priority_queue
    links:
    - https://judge.yosupo.jp/problem/double_ended_priority_queue
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue\n\
    \ndef main():\n    N, Q = rd(), rd()\n    S = rdl(N)\n    reserve(S, N+Q)\n  \
    \  heap = IntervalHeap(S)\n\n    for _ in range(Q):\n        t = rd()\n      \
    \  if t == 0: heap.push(rd())\n        elif t == 1: wtn(heap.pop_min())\n    \
    \    else: wtn(heap.pop_max())\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\n\nclass IntervalHeap:\n    def __init__(heap, arr:\
    \ list):\n        heap._d = arr\n        for k in range(len(arr)): heap._up(k)\n\
    \n    def push(heap, item):\n        heap._d.append(item)\n        heap._up(len(heap._d)-1)\n\
    \n    def pop_min(heap):\n        item = heap._d.pop()\n        if heap._d: item,\
    \ heap._d[0] = heap._d[0], item; heap._down(0)\n        return item\n\n    def\
    \ pop_max(heap):\n        item = heap._d.pop()\n        if len(heap._d) >= 2:\
    \ item, heap._d[1] = heap._d[1], item; heap._down(1)\n        return item\n\n\
    \    def _up(heap, k):\n        v = heap._d[k]\n        if k&1 and heap._d[k]\
    \ < heap._d[k-1]: heap._d[k] = heap._d[k-1]; k ^= 1\n        while 0 <= (p :=\
    \ (k>>1)-1&~1) and v < heap._d[p]: heap._d[k], k = heap._d[p], p\n        while\
    \ 0 <= (p := (k>>1)-1|1) and heap._d[p] < v: heap._d[k], k = heap._d[p], p\n \
    \       heap._d[k] = v\n\n    def _down(heap, k):\n        n, v, rt = len(d :=\
    \ heap._d)-2, d[k], k\n        if k & 1: # max heap\n            c = 2*k+1\n \
    \           while c < n and v < d[c := c+2 if d[c] < d[c+2] else c]: d[k], k,\
    \ c = d[c], c, c<<1|1\n            if c < n+2 and v < d[c]: d[k], k = d[c], c\n\
    \            d[k] = v\n            if v < d[k-1]:\n                d[k] = d[k-1];\
    \ k ^= 1\n                while rt <= (p := (k>>1)-1&~1) and v < d[p]: d[k], k\
    \ = d[p], p\n                d[k] = v\n        else: # min heap\n            c\
    \ = (k+1)<<1\n            while c < n and d[c := c+2 if d[c+2] < d[c] else c]\
    \ < v: d[k], k, c = d[c], c, (c+1)<<1\n            if c < n+2 and d[c] < v: d[k],\
    \ k = d[c], c\n            d[k] = v\n            if k+1 < n+2 and d[k+1] < d[k]:\n\
    \                d[k] = d[k+1]; k ^= 1\n                while rt <= (p := (k>>1)-1|1)\
    \ and d[p] < v: d[k], k = d[p], p\n                d[k] = v\n\ndef reserve(A:\
    \ list, est_len: int) -> None: ...\ntry:\n    from __pypy__ import resizelist_hint\n\
    except:\n    def resizelist_hint(A: list, est_len: int):\n        pass\nreserve\
    \ = resizelist_hint\n\n\nfrom __pypy__.builders import StringBuilder\nimport sys\n\
    from os import read as os_read, write as os_write\nfrom atexit import register\
    \ as atexist_register\n\nclass Fastio:\n    ibuf = bytes()\n    pil = pir = 0\n\
    \    sb = StringBuilder()\n    def load(self):\n        self.ibuf = self.ibuf[self.pil:]\n\
    \        self.ibuf += os_read(0, 131072)\n        self.pil = 0; self.pir = len(self.ibuf)\n\
    \    def flush_atexit(self): os_write(1, self.sb.build().encode())\n    def flush(self):\n\
    \        os_write(1, self.sb.build().encode())\n        self.sb = StringBuilder()\n\
    \    def fastin(self):\n        if self.pir - self.pil < 64: self.load()\n   \
    \     minus = x = 0\n        while self.ibuf[self.pil] < 45: self.pil += 1\n \
    \       if self.ibuf[self.pil] == 45: minus = 1; self.pil += 1\n        while\
    \ self.ibuf[self.pil] >= 48:\n            x = x * 10 + (self.ibuf[self.pil] &\
    \ 15)\n            self.pil += 1\n        if minus: return -x\n        return\
    \ x\n    def fastin_string(self):\n        if self.pir - self.pil < 64: self.load()\n\
    \        while self.ibuf[self.pil] <= 32: self.pil += 1\n        res = bytearray()\n\
    \        while self.ibuf[self.pil] > 32:\n            if self.pir - self.pil <\
    \ 64: self.load()\n            res.append(self.ibuf[self.pil])\n            self.pil\
    \ += 1\n        return res\n    def fastout(self, x): self.sb.append(str(x))\n\
    \    def fastoutln(self, x): self.sb.append(str(x)); self.sb.append('\\n')\nfastio\
    \ = Fastio()\nrd = fastio.fastin; rds = fastio.fastin_string; wt = fastio.fastout;\
    \ wtn = fastio.fastoutln; flush = fastio.flush\natexist_register(fastio.flush_atexit)\n\
    sys.stdin = None; sys.stdout = None\ndef rdl(n):\n    lst = [0]*n\n    for i in\
    \ range(n): lst[i] = rd()\n    return lst\ndef wtnl(l): wtn(' '.join(map(str,\
    \ l)))\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue\n\
    \ndef main():\n    N, Q = rd(), rd()\n    S = rdl(N)\n    reserve(S, N+Q)\n  \
    \  heap = IntervalHeap(S)\n\n    for _ in range(Q):\n        t = rd()\n      \
    \  if t == 0: heap.push(rd())\n        elif t == 1: wtn(heap.pop_min())\n    \
    \    else: wtn(heap.pop_max())\n\nfrom cp_library.ds.heap.interval_heap_cls import\
    \ IntervalHeap\nfrom cp_library.ds.reserve_fn import reserve\nfrom cp_library.io.fast.fast_io_fn\
    \ import rd, rdl, wtn\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/ds/heap/interval_heap_cls.py
  - cp_library/ds/reserve_fn.py
  - cp_library/io/fast/fast_io_fn.py
  isVerificationFile: true
  path: test/library-checker/data-structure/double_ended_priority_queue.test.py
  requiredBy: []
  timestamp: '2025-05-23 18:57:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/double_ended_priority_queue.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/double_ended_priority_queue.test.py
- /verify/test/library-checker/data-structure/double_ended_priority_queue.test.py.html
title: test/library-checker/data-structure/double_ended_priority_queue.test.py
---
