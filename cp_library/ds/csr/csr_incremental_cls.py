import cp_library.__header__
from typing import Sequence
from cp_library.misc.typing import _T
import cp_library.ds.__header__
import cp_library.ds.csr.__header__

class CSRIncremental(Sequence[list[_T]]):
    def __init__(csr, sizes: list[int]):
        csr.L, N = [0]*len(sizes), 0
        for i,sz in enumerate(sizes):
            csr.L[i] = N; N += sz
        csr.R, csr.A = csr.L[:], [0]*N

    def append(csr, i: int, x: _T):
        csr.A[csr.R[i]] = x; csr.R[i] += 1
    
    def __iter__(csr):
        for i,l in enumerate(csr.L):
            yield csr.A[l:csr.R[i]]
    
    def __getitem__(csr, i: int) -> _T:
        return csr.A[i]
    
    def __len__(dsu):
        return len(dsu.L)

    def range(csr, i: int) -> _T:
        return range(csr.L[i], csr.R[i])