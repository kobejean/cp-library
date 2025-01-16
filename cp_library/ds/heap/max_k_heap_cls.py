import cp_library.ds.heap.__header__
from typing import Iterable, TypeVar

from cp_library.ds.heap.min_heap_cls import MinHeap
from cp_library.ds.heap.k_heap_mixin import KHeapMixin
from cp_library.misc.typing import _T

class MaxKHeap(KHeapMixin[_T], MinHeap[_T]):
    """MaxKHeap[K: int, T: type, N: Union[int,None]]"""

    def __init__(self, K: int, iterable: Iterable[_T] = None):
        MinHeap.__init__(self, iterable)
        KHeapMixin.__init__(self, K)
