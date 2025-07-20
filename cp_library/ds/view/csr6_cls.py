import cp_library.__header__
from typing import Generic
from cp_library.misc.typing import _T1, _T2, _T3, _T4, _T5, _T6
import cp_library.ds.__header__
import cp_library.ds.view.__header__
from cp_library.ds.view.view6_cls import view6

class CSR6(Generic[_T1, _T2, _T3, _T4, _T5, _T6]):
    __slots__ = 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'O'
    def __init__(csr, A1: list[_T1], A2: list[_T2], A3: list[_T3], A4: list[_T4], A5: list[_T5], A6: list[_T6], O: list[int]): 
        csr.A1, csr.A2, csr.A3, csr.A4, csr.A5, csr.A6, csr.O = A1, A2, A3, A4, A5, A6, O
    def __len__(csr): return len(csr.O)-1
    def __getitem__(csr, i: int): return view6(csr.A1, csr.A2, csr.A3, csr.A4, csr.A5, csr.A6, csr.O[i], csr.O[i+1])
    def __call__(csr, i: int, j: int): ij = csr.O[i]+j; return csr.A1[ij], csr.A2[ij], csr.A3[ij], csr.A4[ij], csr.A5[ij], csr.A6[ij]
    def set(csr, i: int, j: int, v: tuple[_T1, _T2, _T3, _T4, _T5, _T6]): ij = csr.O[i]+j; csr.A1[ij], csr.A2[ij], csr.A3[ij], csr.A4[ij], csr.A5[ij], csr.A6[ij] = v
    @classmethod
    def bucketize(cls, N: int, K: list[int], V1: list[_T1], V2: list[_T2], V3: list[_T3], V4: list[_T4], V5: list[_T5], V6: list[_T6]):
        A1: list[_T1] = [0]*len(K); A2: list[_T2] = [0]*len(K); A3: list[_T3] = [0]*len(K); A4: list[_T4] = [0]*len(K); A5: list[_T5] = [0]*len(K); A6: list[_T6] = [0]*len(K); O = [0]*(N+1)
        for k in K: O[k] += 1
        for i in range(N): O[i+1] += O[i]
        for e in range(len(K)): k = K[~e]; O[k] -= 1; A1[O[k]] = V1[~e]; A2[O[k]] = V2[~e]; A3[O[k]] = V3[~e]; A4[O[k]] = V4[~e]; A5[O[k]] = V5[~e]; A6[O[k]] = V6[~e]
        return cls(A1, A2, A3, A4, A5, A6, O)