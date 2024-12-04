from heapq import heappop, heappush
import cp_library.ds.heap.__header__
from collections import Counter, UserList
from typing import Iterable, TypeVar

from cp_library.math.inft_cnst import inft

T = TypeVar('T')
class MinMultiset(UserList[T]):
    
    def __init__(self, iterable: Iterable = None, default = -inft):
        super().__init__(iterable)
        self.default = default
        self.counter = Counter(self.data)

    def add(self, x: T):
        self.counter[x] += 1
        heappush(self.data, x)
    
    def remove(self, x: T):
        cnt, data = self.counter, self.data
        cnt[x] -= 1
        while data and cnt[data[0]] == 0:
            heappop(data)

    @property
    def min(self):
        return self.data[0] if self.data else self.default
