---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/fast_heapq.py
    title: cp_library/ds/heap/fast_heapq.py
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
    - https://judge.yosupo.jp/submission/144329
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue\n\
    # modified from abUma: https://judge.yosupo.jp/submission/144329\n'''\n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\ndef reserve(A: list, est_len: int) -> None: ...\ntry:\n\
    \    from __pypy__ import resizelist_hint\nexcept:\n    def resizelist_hint(A:\
    \ list, est_len: int):\n        pass\nreserve = resizelist_hint\n\n\ndef heappush(heap:\
    \ list, item):\n    heap.append(item)\n    heapsiftdown(heap, 0, len(heap)-1)\n\
    \ndef heappop(heap: list):\n    item = heap.pop()\n    if heap: item, heap[0]\
    \ = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapreplace(heap:\
    \ list, item):\n    item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return\
    \ item\n\ndef heappushpop(heap: list, item):\n    if heap and heap[0] < item:\
    \ item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapify(x:\
    \ list):\n    for i in reversed(range(len(x)//2)): heapsiftup(x, i)\n\ndef heapsiftdown(heap:\
    \ list, root: int, pos: int):\n    item = heap[pos]\n    while root < pos and\
    \ item < heap[p := (pos-1)>>1]: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\
    \ndef heapsiftup(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and heap[c] < item: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\ndef heappop_max(heap: list):\n    item\
    \ = heap.pop()\n    if heap: item, heap[0] = heap[0], item; heapsiftup_max(heap,\
    \ 0)\n    return item\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heapify_max(x:\
    \ list):\n    for i in reversed(range(len(x)//2)): heapsiftup_max(x, i)\n\ndef\
    \ heappush_max(heap: list, item):\n    heap.append(item); heapsiftdown_max(heap,\
    \ 0, len(heap)-1)\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heappushpop_max(heap:\
    \ list, item):\n    if heap and heap[0] > item: item, heap[0] = heap[0], item;\
    \ heapsiftup_max(heap, 0)\n    return item\n\ndef heapsiftdown_max(heap: list,\
    \ root: int, pos: int):\n    item = heap[pos]\n    while root < pos and heap[p\
    \ := (pos-1)>>1] < item: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\n\
    def heapsiftup_max(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and item < heap[c := c+(heap[c]<heap[c+1])]: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and item < heap[c]: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\nclass DoubleEndedPriorityQueue:\n    def\
    \ __init__(self, n: int, q: int, arr: list[int]=None) -> None:\n        self.mnq,\
    \ self.mxq = arr or [0]*n, [0]*n\n        reserve(self.mnq, n+q); reserve(self.mxq,\
    \ n+q)\n        self.used = bytearray(n+q)\n        if arr:\n            for i,\
    \ x in enumerate(arr):\n                self.mnq[i] = self.mxq[i] = x << 28 |\
    \ i\n        heapify(self.mnq)\n        heapify_max(self.mxq)\n    \n    def pop_min(self):\n\
    \        while True:\n            tmp = heappop(self.mnq)\n            x, i =\
    \ tmp >> 28, tmp & 0xfffffff\n            if self.used[i]: continue\n        \
    \    self.used[i] = 1\n            return x\n        \n    def pop_max(self):\n\
    \        while True:\n            tmp = heappop_max(self.mxq)\n            x,\
    \ i = tmp >> 28, tmp & 0xfffffff\n            if self.used[i]: continue\n    \
    \        self.used[i] = 1\n            return x\n        \n    def push(self,\
    \ x: int, i: int) -> None:\n        heappush(self.mnq, tmp := x << 28 | i)\n \
    \       heappush_max(self.mxq, tmp)\n\n\n\nfrom __pypy__.builders import StringBuilder\n\
    import sys\nfrom os import read as os_read, write as os_write\nfrom atexit import\
    \ register as atexist_register\n\nclass Fastio:\n    ibuf = bytes()\n    pil =\
    \ pir = 0\n    sb = StringBuilder()\n    def load(self):\n        self.ibuf =\
    \ self.ibuf[self.pil:]\n        self.ibuf += os_read(0, 131072)\n        self.pil\
    \ = 0; self.pir = len(self.ibuf)\n    def flush_atexit(self): os_write(1, self.sb.build().encode())\n\
    \    def flush(self):\n        os_write(1, self.sb.build().encode())\n       \
    \ self.sb = StringBuilder()\n    def fastin(self):\n        if self.pir - self.pil\
    \ < 64: self.load()\n        minus = x = 0\n        while self.ibuf[self.pil]\
    \ < 45: self.pil += 1\n        if self.ibuf[self.pil] == 45: minus = 1; self.pil\
    \ += 1\n        while self.ibuf[self.pil] >= 48:\n            x = x * 10 + (self.ibuf[self.pil]\
    \ & 15)\n            self.pil += 1\n        if minus: return -x\n        return\
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
    \ l)))\n\nN, Q = rd(), rd()\nS = rdl(N)\ndepq = DoubleEndedPriorityQueue(N, Q,\
    \ S)\nfor i in range(Q):\n    cmd = rd()\n    if cmd == 0:\n        x = rd()\n\
    \        depq.push(x, i + N)\n    elif cmd == 1:\n        wtn(depq.pop_min())\n\
    \    else:\n        wtn(depq.pop_max())\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue\n\
    # modified from abUma: https://judge.yosupo.jp/submission/144329\nfrom cp_library.ds.reserve_fn\
    \ import reserve\nfrom cp_library.ds.heap.fast_heapq import heapify_max, heappop,\
    \ heappop_max, heappush, heapify, heappush_max\n\nclass DoubleEndedPriorityQueue:\n\
    \    def __init__(self, n: int, q: int, arr: list[int]=None) -> None:\n      \
    \  self.mnq, self.mxq = arr or [0]*n, [0]*n\n        reserve(self.mnq, n+q); reserve(self.mxq,\
    \ n+q)\n        self.used = bytearray(n+q)\n        if arr:\n            for i,\
    \ x in enumerate(arr):\n                self.mnq[i] = self.mxq[i] = x << 28 |\
    \ i\n        heapify(self.mnq)\n        heapify_max(self.mxq)\n    \n    def pop_min(self):\n\
    \        while True:\n            tmp = heappop(self.mnq)\n            x, i =\
    \ tmp >> 28, tmp & 0xfffffff\n            if self.used[i]: continue\n        \
    \    self.used[i] = 1\n            return x\n        \n    def pop_max(self):\n\
    \        while True:\n            tmp = heappop_max(self.mxq)\n            x,\
    \ i = tmp >> 28, tmp & 0xfffffff\n            if self.used[i]: continue\n    \
    \        self.used[i] = 1\n            return x\n        \n    def push(self,\
    \ x: int, i: int) -> None:\n        heappush(self.mnq, tmp := x << 28 | i)\n \
    \       heappush_max(self.mxq, tmp)\n\nfrom cp_library.io.fast.fast_io_fn import\
    \ rd, rdl, wtn\n\nN, Q = rd(), rd()\nS = rdl(N)\ndepq = DoubleEndedPriorityQueue(N,\
    \ Q, S)\nfor i in range(Q):\n    cmd = rd()\n    if cmd == 0:\n        x = rd()\n\
    \        depq.push(x, i + N)\n    elif cmd == 1:\n        wtn(depq.pop_min())\n\
    \    else:\n        wtn(depq.pop_max())"
  dependsOn:
  - cp_library/ds/reserve_fn.py
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/io/fast/fast_io_fn.py
  isVerificationFile: true
  path: test/library-checker/data-structure/double_ended_priority_queue_2heaps_fast_heapq.test.py
  requiredBy: []
  timestamp: '2025-07-26 11:14:31+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/double_ended_priority_queue_2heaps_fast_heapq.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/double_ended_priority_queue_2heaps_fast_heapq.test.py
- /verify/test/library-checker/data-structure/double_ended_priority_queue_2heaps_fast_heapq.test.py.html
title: test/library-checker/data-structure/double_ended_priority_queue_2heaps_fast_heapq.test.py
---
