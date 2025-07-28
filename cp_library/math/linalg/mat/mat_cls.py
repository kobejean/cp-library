import cp_library.__header__
from typing import Container, Sequence
from numbers import Number
from cp_library.io.parsable_cls import Parsable
import cp_library.math.__header__
import cp_library.math.linalg.__header__
from cp_library.math.linalg.elm_wise_in_place_mixin import ElmWiseInPlaceMixin
import cp_library.math.linalg.mat.__header__

class Mat(Parsable, Container, ElmWiseInPlaceMixin):
    def __init__(self, flat, N, M): self.data, self.N, self.M = flat, N, M
    def elm_wise(self, other, op):
        cls = type(self)
        if isinstance(other, Number): return cls([op(elm, other) for elm in self.data])
        if isinstance(other, Sequence): return cls([op(self.data[i], elm) for i, elm in enumerate(other)])
        raise ValueError("Operand must be a number or a tuple of the same length")
    def ielm_wise(self, other, op):
        data = self.data
        if isinstance(other, Number):
            for i in range(len(data)): data[i] = op(data[i], other)
        elif isinstance(other, Sequence) and len(data) == len(other):
            for i, elm in enumerate(other): data[i] = op(data[i], elm)
        else: raise ValueError("Operand must be a number or a list of the same length")
        return self
    def __len__(self): return self.N
    def __getitem__(self, ij: tuple[int, int]): i, j = ij; return self.data[i*self.M+j]
    def __setitem__(self, ij: tuple[int, int], val: int): i, j = ij; self.data[i*self.M+j] = val
    def __contains__(self, x: int) -> bool: return x in self.data
    def __matmul__(A,B):
        assert A.M == B.N, f"Dimension mismatch {A.M = } {B.N = }"
        N,M = A.N, B.M
        cls = type(A)
        R = cls([0]*(M*N))
        for irow in range(0,N*M,M):
            for k in range(A.M):
                krow, a = k*M, A.data[irow+k]
                for j in range(M):
                    R.data[irow+j] = B.data[krow+j]*a + R.data[irow+j]
        return R
    def __pow__(A,K):
        R = A[:] if K & 1 else type(A).identity(A.N)
        for i in range(1,K.bit_length()):
            A = A @ A
            if K >> i & 1: R = R @ A
        return R 
    @classmethod
    def identity(cls, N):
        data = [0]*(N*N)
        for i in range(0,N*N,N+1): data[i] = 1
        return cls(data)
    def copy(self):
        cls = type(self)
        obj = cls.__new__(cls)
        obj.N, obj.M, obj.data = self.N, self.M, self.data
        return obj
    @classmethod
    def compile(cls, N: int, M: int, T: type = int):
        elm, size = Parser.compile(T), N*M
        def parse(io: IOBase): return cls([elm(io) for _ in range(size)])
        return parse
    def __repr__(self) -> str: return '\n'.join(' '.join(str(elm) for elm in row) for row in self)
from cp_library.io.parser_cls import Parser
from cp_library.io.io_base_cls import IOBase