import cp_library.ds.heap.__header__

from collections import UserList
from cp_library.ds.heap.fast_heapq  import heapify, heappop, heappush, heappushpop, heapreplace
from cp_library.ds.heap.heap_proto import HeapProtocol

class PriorityQueue(HeapProtocol[int], UserList[int]):
    
    def __init__(self, N: int, ids: list[int] = None, priorities: list[int] = None, /):
        self.shift = N.bit_length()
        self.mask = (1 << self.shift)-1
        if ids is None:
            self.data = elist(N)
        elif priorities is None:
            heapify(ids)
            self.data = ids
        else:
            M = len(ids)
            data = [0]*M
            for i in range(M):
                data[i] = self.encode(ids[i], priorities[i]) 
            heapify(data)
            self.data = data

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
    
from cp_library.ds.elist_fn import elist