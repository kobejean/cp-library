# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue
# modified from abUma: https://judge.yosupo.jp/submission/144329
from cp_library.ds.reserve_fn import reserve
from cp_library.ds.heap.fast_heapq import heapify_max, heappop, heappop_max, heappush, heapify, heappush_max

class DoubleEndedPriorityQueue:
    def __init__(self, n: int, q: int, arr: list[int]=None) -> None:
        self.mnq, self.mxq = arr or [0]*n, [0]*n
        reserve(self.mnq, n+q); reserve(self.mxq, n+q)
        self.used = bytearray(n+q)
        if arr:
            for i, x in enumerate(arr):
                self.mnq[i] = self.mxq[i] = x << 28 | i
        heapify(self.mnq)
        heapify_max(self.mxq)
    
    def pop_min(self):
        while True:
            tmp = heappop(self.mnq)
            x, i = tmp >> 28, tmp & 0xfffffff
            if self.used[i]: continue
            self.used[i] = 1
            return x
        
    def pop_max(self):
        while True:
            tmp = heappop_max(self.mxq)
            x, i = tmp >> 28, tmp & 0xfffffff
            if self.used[i]: continue
            self.used[i] = 1
            return x
        
    def push(self, x: int, i: int) -> None:
        heappush(self.mnq, tmp := x << 28 | i)
        heappush_max(self.mxq, tmp)

from cp_library.io.fast.fast_io_fn import rd, rdl, wtn

N, Q = rd(), rd()
S = rdl(N)
depq = DoubleEndedPriorityQueue(N, Q, S)
for i in range(Q):
    cmd = rd()
    if cmd == 0:
        x = rd()
        depq.push(x, i + N)
    elif cmd == 1:
        wtn(depq.pop_min())
    else:
        wtn(depq.pop_max())