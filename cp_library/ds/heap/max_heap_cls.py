import cp_library.ds.heap.__header__
from collections import UserList
from typing import Iterable, TypeVar
from cp_library.ds.heap.heapq_max_import import heapify_max, heappop_max, heappush_max, heapreplace_max, heappushpop_max
from cp_library.ds.heap.heap_proto import HeapProtocol

T = TypeVar('T')
class MaxHeap(HeapProtocol[T], UserList[T]):
    
    def __init__(self, iterable: Iterable[T] = None):
        super().__init__(iterable)
        heapify_max(self.data)
    
    def pop(self):
        return heappop_max(self.data)
    
    def push(self, item: T):
        heappush_max(self.data, item)

    def pushpop(self, item: T):
        return heappushpop_max(self.data, item)
    
    def replace(self, item: T):
        return heapreplace_max(self.data, item)

