import cp_library.__header__
from typing import Iterable
from cp_library.misc.typing import _T
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
from cp_library.ds.heap.heapify_fn import heapify
from cp_library.ds.heap.heappop_fn import heappop
from cp_library.ds.heap.heappush_fn import heappush
from cp_library.ds.heap.heappushpop_fn import heappushpop
from cp_library.ds.heap.heapreplace_fn import heapreplace
from cp_library.ds.heap.heap_base_cls import HeapBase

class MinHeap(HeapBase[_T]):
    def __init__(self, iterable: Iterable = None): self.data = list(iterable) if iterable else []; heapify(self.data)
    def pop(self): return heappop(self.data)
    def push(self, item: _T): heappush(self.data, item)
    def pushpop(self, item: _T): return heappushpop(self.data, item)
    def replace(self, item: _T): return heapreplace(self.data, item)