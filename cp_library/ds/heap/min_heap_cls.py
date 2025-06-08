import cp_library.__header__
from typing import Iterable
from cp_library.misc.typing import _T
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
from cp_library.ds.heap.fast_heapq import heapify, heappop, heappush, heappushpop, heapreplace
from cp_library.ds.heap.heap_proto import HeapProtocol

class MinHeap(HeapProtocol[_T]):
    def __init__(self, iterable: Iterable = None): self.data = list(iterable) if iterable else []; heapify(self.data)
    def pop(self): return heappop(self.data)
    def push(self, item: _T): heappush(self.data, item)
    def pushpop(self, item: _T): return heappushpop(self.data, item)
    def replace(self, item: _T): return heapreplace(self.data, item)