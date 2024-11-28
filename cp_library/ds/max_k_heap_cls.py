import cp_library.ds.__header__
from typing import Iterable, TypeVar

from cp_library.ds.min_heap_cls import MinHeap
from cp_library.ds.k_heap_mixin import KHeapMixin

T = TypeVar('T')
class MaxKHeap(KHeapMixin[T], MinHeap[T]):
    """MaxKHeap[K: int, T: type, N: int|None]"""

    def __init__(self, K: int, iterable: Iterable[T] = None):
        MinHeap.__init__(self, iterable)
        KHeapMixin.__init__(self, K)
