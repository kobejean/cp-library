# verification-helper: PROBLEM https://judge.yosupo.jp/problem/double_ended_priority_queue
# modified from abUma: https://judge.yosupo.jp/submission/144329
from cp_library.ds.reserve_fn import reserve
from cp_library.ds.heap.fast_heapq import heappop, heappush, heapify

class DoubleEndedPriorityQueue:
    def __init__(self, n: int, q: int, arr: list[int]=None) -> None:
        self.hq1 = arr
        self.hq2 = [0]*n
        reserve(self.hq1, n+q)
        reserve(self.hq2, n+q)
        self.used = bytearray(n+q)
        if arr:
            for i, x in enumerate(S):
                self.hq1[i] = tmp = x << 28 | i
                self.hq2[i] = ~tmp
        heapify(self.hq1)
        heapify(self.hq2)
    
    def pop_min(self):
        while 1:
            tmp = heappop(self.hq1)
            x, i = tmp >> 28, tmp & 0xfffffff
            if self.used[i]: continue
            self.used[i] = 1
            return x
        
    def pop_max(self):
        while 1:
            tmp = ~heappop(self.hq2)
            x, i = tmp >> 28, tmp & 0xfffffff
            if self.used[i]: continue
            self.used[i] = 1
            return x
        
    def push(self, x: int, i: int) -> None:
        heappush(self.hq1, tmp := x << 28 | i)
        heappush(self.hq2, ~tmp)

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