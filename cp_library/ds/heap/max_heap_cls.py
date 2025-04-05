import cp_library.ds.heap.__header__
from collections import UserList
from typing import Iterable
from cp_library.ds.heap.fast_heapq import heapify_max, heappop_max, heappush_max, heapreplace_max, heappushpop_max
from cp_library.ds.heap.heap_proto import HeapProtocol
from cp_library.misc.typing import _T

class MaxHeap(HeapProtocol[_T], UserList[_T]):
    def __init__(self, iterable: Iterable[_T] = None):
        super().__init__(iterable)
        heapify_max(self.data)
    def pop(self): return heappop_max(self.data)
    def push(self, item: _T): heappush_max(self.data, item)
    def pushpop(self, item: _T): return heappushpop_max(self.data, item)
    def replace(self, item: _T): return heapreplace_max(self.data, item)
