import cp_library.__header__
from typing import Iterable
from cp_library.misc.typing import _T
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
from cp_library.ds.heap.fast_heapq import heapify_max, heappop_max, heappush_max, heapreplace_max, heappushpop_max
from cp_library.ds.heap.heap_proto import HeapProtocol

class MaxHeap(HeapProtocol[_T]):
    def __init__(self, iterable: Iterable[_T] = None): self.data = list(iterable) if iterable else []; heapify_max(self.data)
    def pop(self): return heappop_max(self.data)
    def push(self, item: _T): heappush_max(self.data, item)
    def pushpop(self, item: _T): return heappushpop_max(self.data, item)
    def replace(self, item: _T): return heapreplace_max(self.data, item)
