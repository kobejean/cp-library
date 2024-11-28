import cp_library.ds.__header__
from typing import Iterable, TypeVar

from cp_library.io.parser_cls import Parser, Parsable, TokenStream
from cp_library.ds.heap_proto import HeapProtocol

T = TypeVar('T')
class KHeapMixin(HeapProtocol[T], Parsable):
    """KHeapMixin[K: int, T: type, N: int|None]"""
    def __init__(heap, K: int):
        heap.K = K

    def added(heap, item: T): ...

    def removed(heap, item: T): ...
    
    def pop(heap):
        item = super().pop()
        heap.removed(item)
        return item
    
    def push(heap, item: T):
        if len(heap) < heap._K:
            heap.added(item)
            super().push(item)
        elif heap._K:
            assert len(heap) == heap._K, f'{len(heap)=} {heap._K}'
            heap.pushpop(item)
    
    def pushpop(heap, item: T):
        if item != (remove := super().pushpop(item)):
            heap.removed(remove)
            heap.added(item)
            return remove
        else:
            return item
    
    def replace(heap, item: T):
        remove = super().replace(item)
        heap.removed(remove)
        heap.added(item)
        return remove
    
    
    @property
    def K(heap):
        return heap._K

    @K.setter
    def K(heap, K):
        heap._K = K
        if K is not None:
            while len(heap) > K:
                heap.pop()
    
    @classmethod
    def compile(cls, K: int, T: type, N: int|None = None):
        elm = Parser.compile(T)
        if N is None:
            def parse(ts: TokenStream):
                return cls(K, (elm(ts) for _ in ts.wait()))
        else:
            def parse(ts: TokenStream):
                return cls(K, (elm(ts) for _ in range(N)))
        return parse
