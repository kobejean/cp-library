import cp_library.ds.heap.__header__
from typing import Iterable
from cp_library.ds.heap.max_heap_cls import MaxHeap
from cp_library.ds.heap.k_heap_mixin import KHeapMixin
from cp_library.misc.typing import _T

class MinKHeap(KHeapMixin[_T], MaxHeap[_T]):
    '''MinKHeap[K: int, T: type, N: Union[int,None]]'''
    def __init__(self, K: int, iterable: Iterable[_T] = None):
        MaxHeap.__init__(self, iterable)
        KHeapMixin.__init__(self, K)
