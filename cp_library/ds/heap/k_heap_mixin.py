import cp_library.__header__
from typing import Union
from cp_library.misc.typing import _T
from cp_library.io.parsable_cls import Parsable
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
from cp_library.ds.heap.heap_base_cls import HeapBase

class KHeapMixin(HeapBase[_T], Parsable):
    '''KHeapMixin[K: int, T: type, N: Union[int,None]]'''
    def __init__(heap, K: int): heap.K = K
    def added(heap, item: _T): ...
    def removed(heap, item: _T): ...
    def pop(heap): item = super().pop(); heap.removed(item); return item
    def push(heap, item: _T):
        if len(heap) < heap._K: heap.added(item); super().push(item)
        elif heap._K: heap.pushpop(item)
    def pushpop(heap, item: _T):
        if item != (remove := super().pushpop(item)): heap.removed(remove); heap.added(item); return remove
        else: return item
    def replace(heap, item: _T): remove = super().replace(item); heap.removed(remove); heap.added(item); return remove
    @property
    def K(heap): return heap._K
    @K.setter
    def K(heap, K):
        heap._K = K
        if K is not None:
            while len(heap) > K: heap.pop()
    @classmethod
    def compile(cls, K: int, T: type, N: Union[int,None] = None):
        elm = Parser.compile(T)
        if N is None:
            def parse(io: IOBase): return cls(K, (elm(io) for _ in io.wait()))
        else:
            def parse(io: IOBase): return cls(K, (elm(io) for _ in range(N)))
        return parse
from cp_library.io.io_base_cls import IOBase
from cp_library.io.parser_cls import Parser