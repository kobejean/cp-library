import cp_library.__header__
from typing import Iterable
from cp_library.misc.typing import _T
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
from cp_library.ds.heap.heapify_max_fn import heapify_max
from cp_library.ds.heap.heappop_max_fn import heappop_max
from cp_library.ds.heap.heappush_max_fn import heappush_max
from cp_library.ds.heap.heappushpop_max_fn import heappushpop_max
from cp_library.ds.heap.heapreplace_max_fn import heapreplace_max
from cp_library.ds.heap.heap_base_cls import HeapBase

class MaxHeap(HeapBase[_T]):
    def __init__(self, iterable: Iterable[_T] = None): self.data = list(iterable) if iterable else []; heapify_max(self.data)
    def pop(self): return heappop_max(self.data)
    def push(self, item: _T): heappush_max(self.data, item)
    def pushpop(self, item: _T): return heappushpop_max(self.data, item)
    def replace(self, item: _T): return heapreplace_max(self.data, item)
