import cp_library.ds.heap.__header__
from cp_library.ds.heap.fast_heapq  import heappop, heappush
from collections import Counter, UserList
from typing import Iterable
from math import inf
from cp_library.misc.typing import _T

class MinMultiset(UserList[_T]):
    def __init__(self, iterable: Iterable = None, default = -inf):
        super().__init__(iterable)
        self.default = default
        self.counter = Counter(self.data)

    def add(self, x: _T):
        self.counter[x] += 1
        heappush(self.data, x)
    
    def remove(self, x: _T):
        cnt, data = self.counter, self.data
        cnt[x] -= 1
        while data and cnt[data[0]] == 0: heappop(data)

    @property
    def min(self): return self.data[0] if self.data else self.default
