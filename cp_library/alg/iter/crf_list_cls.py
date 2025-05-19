import cp_library.__header__
from typing import Generic
from cp_library.misc.typing import _T
import cp_library.alg.__header__
import cp_library.alg.iter.__header__

class CRFList(Generic[_T]):
    def __init__(crf, A: list[_T], S: list[int]):
        crf.N, crf.A, crf.S = len(S), A, S
        S.append(len(A))

    def __len__(crf) -> int: return crf.N

    def __getitem__(crf, i: int) -> list[_T]:
        return crf.A[crf.S[i]:crf.S[i+1]]
    
    def get(crf, i: int, j: int) -> _T:
        return crf.A[crf.S[i]+j]
    
    def len(crf, i: int) -> int:
        return crf.S[i+1] - crf.S[i]