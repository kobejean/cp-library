import cp_library.ds.__header__
from collections import UserList
from typing import Iterable, TypeVar
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from cp_library.ds.heap_proto import HeapProtocol

T = TypeVar('T')
class MinHeap(HeapProtocol[T], UserList[T]):
    
    def __init__(self, iterable: Iterable = None):
        super().__init__(iterable)
        heapify(self.data)
    
    def pop(self):
        return heappop(self.data)
    
    def push(self, item: T):
        heappush(self.data, item)

    def pushpop(self, item: T):
        return heappushpop(self.data, item)
    
    def replace(self, item: T):
        return heapreplace(self.data, item)
