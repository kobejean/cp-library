import cp_library.alg.iter.__header__
from typing import Iterator, SupportsIndex, TypeVar

T = TypeVar('T')
class SliceIterator(Iterator[T]):
    def __init__(self, A: list[T], R: list[SupportsIndex]):
        self.A, self.R, self.l, self.i = A, R, 0, 0
    def __len__(self): return len(self.R)-self.i
    def __next__(self):
        R = self.R
        if self.i >= len(R): raise StopIteration
        self.l, l = (r := R[self.i]), self.l
        self.i += 1
        return self.A[l:r]