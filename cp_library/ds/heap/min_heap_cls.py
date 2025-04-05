import cp_library.ds.heap.__header__
from collections import UserList
from typing import Iterable
from cp_library.ds.heap.fast_heapq import heapify, heappop, heappush, heappushpop, heapreplace
from cp_library.ds.heap.heap_proto import HeapProtocol
from cp_library.misc.typing import _T

class MinHeap(HeapProtocol[_T], UserList[_T]):
    def __init__(self, iterable: Iterable = None):
        super().__init__(iterable)
        heapify(self.data)
    
    def pop(self): return heappop(self.data)
    def push(self, item: _T): heappush(self.data, item)
    def pushpop(self, item: _T): return heappushpop(self.data, item)
    def replace(self, item: _T): return heapreplace(self.data, item)
