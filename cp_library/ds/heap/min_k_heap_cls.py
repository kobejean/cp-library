import cp_library.ds.heap.__header__
from typing import Iterable, TypeVar

from cp_library.ds.heap.max_heap_cls import MaxHeap
from cp_library.ds.heap.k_heap_mixin import KHeapMixin

T = TypeVar('T')
class MinKHeap(KHeapMixin[T], MaxHeap[T]):
    """MinKHeap[K: int, T: type, N: Union[int,None]]"""

    def __init__(self, K: int, iterable: Iterable[T] = None):
        MaxHeap.__init__(self, iterable)
        KHeapMixin.__init__(self, K)
