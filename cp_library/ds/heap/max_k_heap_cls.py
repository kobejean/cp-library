import cp_library.__header__
from typing import Iterable
from cp_library.misc.typing import _T
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
from cp_library.ds.heap.min_heap_cls import MinHeap
from cp_library.ds.heap.k_heap_mixin import KHeapMixin

class MaxKHeap(KHeapMixin[_T], MinHeap[_T]):
    '''MaxKHeap[K: int, T: type, N: Union[int,None]]'''
    def __init__(self, K: int, iterable: Iterable[_T] = None):
        MinHeap.__init__(self, iterable)
        KHeapMixin.__init__(self, K)