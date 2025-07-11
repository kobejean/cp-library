
import cp_library.__header__
from typing import Generic
from cp_library.misc.typing import _T
import cp_library.ds.__header__
import cp_library.ds.view.__header__
from cp_library.ds.view.view_cls import view

class CSR(Generic[_T]):
    __slots__ = 'A', 'O'
    def __init__(csr, A: list[_T], O: list[int]): csr.A, csr.O = A, O
    def __len__(csr): return len(csr.O)-1
    def __getitem__(csr, i: int): return view(csr.A, csr.O[i], csr.O[i+1])
    def __call__(csr, i: int, j: int): return csr.A[csr.O[i]+j]
    def set(csr, i: int, j: int, v: _T): csr.A[csr.O[i]+j] = v
    @classmethod
    def bucketize(cls, N: int, K: list[int], V: list[_T]):
        A: list[_T] = [0]*len(K); O = [0]*(N+1)
        for k in K: O[k] += 1
        for i in range(N): O[i+1] += O[i]
        for e in range(len(K)): k = K[~e]; O[k] -= 1; A[O[k]] = V[~e]
        return cls(A, O)