import cp_library.__header__
from typing import Generic
from cp_library.misc.typing import _T
import cp_library.ds.__header__
import cp_library.ds.heap.__header__

class HeapBase(Generic[_T]):
    def peek(heap) -> _T: return heap.data[0]
    def pop(heap) -> _T: ...
    def push(heap, item: _T): ...
    def pushpop(heap, item: _T) -> _T: ...
    def replace(heap, item: _T) -> _T: ...
    def __contains__(heap, item: _T): return item in heap.data
    def __len__(heap): return len(heap.data)
    def clear(heap): heap.data.clear()