import cp_library.ds.__header__

from collections import UserList
from cp_library.ds.heap.heapq_max_import import heapify_max, heappop_max, heappush_max, heappushpop_max, heapreplace_max
from cp_library.ds.heap.heap_proto import HeapProtocol

class MaxPriorityQueue(HeapProtocol[int], UserList[int]):
    
    def __init__(self, N: int, ids: list[int] = None, priorities: list[int] = None, /):
        self.shift = N.bit_length()
        self.mask = (1 << self.shift)-1
        if ids is None:
            super().__init__()
        elif priorities is None:
            heapify_max(ids)
            self.data = ids
        else:
            M = len(ids)
            data = [0]*M
            for i in range(M):
                data[i] = self.encode(ids[i], priorities[i]) 
            heapify_max(data)
            self.data = data

    def encode(self, id, priority):
        return priority << self.shift | id
    
    def decode(self, encoded):
        return self.mask & encoded, encoded >> self.shift
    
    def pop(self):
        return self.decode(heappop_max(self.data))
    
    def push(self, id: int, priority: int):
        heappush_max(self.data, self.encode(id, priority))

    def pushpop(self, id: int, priority: int):
        return self.decode(heappushpop_max(self.data, self.encode(id, priority)))
    
    def replace(self, id: int, priority: int):
        return self.decode(heapreplace_max(self.data, self.encode(id, priority)))

    def peek(self):
        return self.decode(self.data[0])