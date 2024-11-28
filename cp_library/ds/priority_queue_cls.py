import cp_library.ds.__header__

from typing import Iterable
from collections import UserList
from typing import Iterable
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from cp_library.ds.heap_proto import HeapProtocol

class PriorityQueue(HeapProtocol[int], UserList[int]):
    
    def __init__(self, N: int, ids: Iterable[int] = None, priorities: Iterable[int] = None, /):
        self.shift = N.bit_length()
        self.mask = (1 << self.shift)-1
        if ids is None:
            super().__init__()
        elif priorities is None:
            self.data = ids
            heapify(self.data)
        else:
            self.data = [self.encode(id, priority) for id, priority in zip(ids, priorities)]
            heapify(self.data)

    def encode(self, id, priority):
        return priority << self.shift | id
    
    def decode(self, encoded):
        return self.mask & encoded, encoded >> self.shift
    
    def pop(self):
        return self.decode(heappop(self.data))
    
    def push(self, id: int, priority: int):
        heappush(self.data, self.encode(id, priority))

    def pushpop(self, id: int, priority: int):
        return self.decode(heappushpop(self.data, self.encode(id, priority)))
    
    def replace(self, id: int, priority: int):
        return self.decode(heapreplace(self.data, self.encode(id, priority)))

