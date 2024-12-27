import cp_library.alg.iter.__header__
from typing import Iterator, SupportsIndex, TypeVar

T = TypeVar('T')
class SliceIteratorReverse(Iterator[T]):
    def __init__(self, A: list[T], L: list[SupportsIndex]):
        self.A, self.L, self.r = A, L, len(A)
    def __len__(self): return len(self.L)
    def __next__(self):
        L = self.L
        if not L: raise StopIteration
        self.r, r = (l := L.pop()), self.r
        return self.A[l:r]