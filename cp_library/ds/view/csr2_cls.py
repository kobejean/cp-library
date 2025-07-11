
import cp_library.__header__
from typing import Generic
from cp_library.misc.typing import _S, _T
import cp_library.ds.__header__
import cp_library.ds.view.__header__
from cp_library.ds.view.view2_cls import view2

class CSR2(Generic[_T]):
    __slots__ = 'A', 'B', 'O'
    def __init__(csr, A: list[_S], B: list[_T], O: list[int]): csr.A, csr.B, csr.O = A, B, O
    def __len__(csr): return len(csr.O)-1
    def __getitem__(csr, i: int): return view2(csr.A, csr.B, csr.O[i], csr.O[i+1])
    def __call__(csr, i: int, j: int): ij = csr.O[i]+j; return csr.A[ij], csr.B[ij]
    def set(csr, i: int, j: int, v: _T): ij = csr.O[i]+j; csr.A[ij], csr.B[ij] = v
    @classmethod
    def bucketize(cls, N: int, K: list[int], V: list[_T], W: list[_T]):
        A: list[_S] = [0]*len(K); B: list[_T] = [0]*len(K); O = [0]*(N+1)
        for k in K: O[k] += 1
        for i in range(N): O[i+1] += O[i]
        for e in range(len(K)): k = K[~e]; O[k] -= 1; A[O[k]] = V[~e]; B[O[k]] = W[~e]
        return cls(A, B, O)