
import cp_library.__header__
from typing import Generic
from cp_library.misc.typing import _T1, _T2
import cp_library.ds.__header__
import cp_library.ds.view.__header__
from cp_library.ds.view.view2_cls import view2

class CSR2(Generic[_T1, _T2]):
    __slots__ = 'A1', 'A2', 'O'
    def __init__(csr, A1: list[_T1], A2: list[_T2], O: list[int]): csr.A1, csr.A2, csr.O = A1, A2, O
    def __len__(csr): return len(csr.O)-1
    def __getitem__(csr, i: int): return view2(csr.A1, csr.A2, csr.O[i], csr.O[i+1])
    def __call__(csr, i: int, j: int): ij = csr.O[i]+j; return csr.A1[ij], csr.A2[ij]
    def set(csr, i: int, j: int, v: tuple[_T1, _T2]): ij = csr.O[i]+j; csr.A1[ij], csr.A2[ij] = v
    @classmethod
    def bucketize(cls, N: int, K: list[int], V1: list[_T1], V2: list[_T2]):
        A1: list[_T1] = [0]*len(K); A2: list[_T2] = [0]*len(K); O = [0]*(N+1)
        for k in K: O[k] += 1
        for i in range(N): O[i+1] += O[i]
        for e in range(len(K)): k = K[~e]; O[k] -= 1; A1[O[k]] = V1[~e]; A2[O[k]] = V2[~e]
        return cls(A1, A2, O)