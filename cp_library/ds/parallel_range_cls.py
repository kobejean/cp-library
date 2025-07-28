import cp_library.ds.__header__
from cp_library.io.parsable_cls import Parsable

class ParallelRange(tuple, Parsable):
    def __new__(cls, N): return super().__new__(cls, ([0]*N, [0]*N))
    @classmethod
    def compile(cls, N: int):
        def parse(io: IOBase):
            L, R = P = cls(N)
            for i in range(N): l, r = io.readints(); L[i], R[i] = l-1, r
            return P
        return parse
from cp_library.io.io_base_cls import IOBase