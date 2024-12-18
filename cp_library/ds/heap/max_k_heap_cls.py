import cp_library.ds.heap.__header__
from typing import Iterable, TypeVar

from cp_library.ds.heap.min_heap_cls import MinHeap
from cp_library.ds.heap.k_heap_mixin import KHeapMixin

T = TypeVar('T')
class MaxKHeap(KHeapMixin[T], MinHeap[T]):
    """MaxKHeap[K: int, T: type, N: Union[int,None]]"""

    def __init__(self, K: int, iterable: Iterable[T] = None):
        MinHeap.__init__(self, iterable)
        KHeapMixin.__init__(self, K)
