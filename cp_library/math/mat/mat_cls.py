import cp_library.math.__header__

from typing import Iterable, Container, Sequence
from numbers import Number
from cp_library.io.parser_cls import Parsable, Parser, TokenStream
from cp_library.math.elm_wise_in_place_mixin import ElmWiseInPlaceMixin


class Mat(Parsable, Container, ElmWiseInPlaceMixin):

    def __init__(self, data = 0):
        self.data, self.N, self.M = data, len(data), len(data[0])

    def elm_wise(self, other, op):
        N, M = self.N, self.M
        cls = type(self)
        if isinstance(other, Number):
            return cls([[op(elm, other) for elm in row] for row in self.data])
        if isinstance(other, Sequence):
            # return cls(N, M, (op(x, y) for x, y in zip(self, other)))
            return cls([[op(elm, oelm) for elm, oelm in zip(row,orow)] for row, orow in zip(self.data, other.data)])
        raise ValueError("Operand must be a number or a tuple of the same length")
    
    def ielm_wise(self, other, op):
        data = self.data
        if isinstance(other, Number):
            for i in range(len(self)):
                data[i] = op(data[i], other)
        elif isinstance(other, Sequence) and len(data) == len(other):
            for i in range(len(data)):
                data[i] = op(data[i], other[i])
        else:
            raise ValueError("Operand must be a number or a list of the same length")
        return self

    def __len__(self):
        return self.R
    
    def __contains__(self, x: object) -> bool:
        return x in self.data

    def __matmul__(A,B):
        assert A.M == len(B), f"Dimension mismatch {A.M = } {len(B) = }"
        N,M = A.N, B.M
        cls = type(A)
        R = cls([[0]*M for _ in range(N)])
        
        for irow in range(0,N*M,M):
            for k in range(A.M):
                krow, a = k*M, A.data[irow+k]
                for j in range(M):
                    R.data[irow+j] = (B.data[krow+j]*a + R.data[irow+j]) % mint.mod

        return R
    
    def __pow__(A,K):
        R = A.copy() if K & 1 else type(A).identity(A.N)
        for i in range(1,K.bit_length()):
            A = A @ A
            if K >> i & 1:
                R = R @ A
        return R 

    @classmethod
    def identity(cls, N):
        R = cls([[int(i==j) for j in range(N)] for i in range(N)])
        return R
    
    def copy(self):
        cls = type(self)
        obj = cls.__new__(cls)
        obj.N, obj.M = self.N, self.M
        obj.size = self.size
        obj.data = self.data
        return obj
    
    @classmethod
    def compile(cls, N: int, M: int, T: type = int):
        elm = Parser.compile(T)
        size = N*M
        def parse(ts: TokenStream):
            obj = cls.__new__(cls)
            obj.N, obj.M = N, M
            obj.size = size
            obj.data = list(elm(ts) for _ in range(obj.size))
            return obj
        return parse
    
    def __repr__(self) -> str:
        return '\n'.join(' '.join(str(elm) for elm in row) for row in self)


from cp_library.math.mod.mint_cls import mint

class ModMat(Mat):

    # def __init__(self, N: int, M: int, data = None):
    #     super().__init__(N, M, data or mint.zero)

    # def __matmul__(A,B):
    #     assert A.M == len(B), f"Dimension mismatch {A.M = } {len(B) = }"
    #     cls = type(A)
    #     R = cls(A.N,A.M)
    #     Br = super(cls.__bases__[0], B).__getitem__
    #     for Ri,Ai in zip(R,A):
    #         for k,Aik in enumerate(Ai):
    #             for j,Bkj in enumerate(Br(k)):
    #                 Ri[j] = Bkj*Aik + Ri[j] 

    #     return R
    
    # def __pow__(A,K):
    #     A = Mat(A.N, A.M, ((int(elm) for elm in row) for row in A))
    #     R = A if K & 1 else Mat.identity(A.N)
    #     for i in range(1,K.bit_length()):
    #         A = A @ A
    #         A %= mint.mod
    #         if K >> i & 1:
    #             R = R @ A
    #             R %= mint.mod
    #     R = Mat(R.N, R.M, ((mint(elm) for elm in row) for row in R))
    #     return R 
    
    # @classmethod
    # def identity(cls, N):
    #     R = cls(N, N, mint.zero)
    #     for i in range(N):
    #         R[i,i] = mint.one
    #     return R
    
    @classmethod
    def compile(cls, N: int, M: int, T: type = int):
        return super().compile(N, M, T)
    

from cp_library.math.mutvec_cls import MutVec