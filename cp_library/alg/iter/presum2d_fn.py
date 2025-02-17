import cp_library.alg.iter.__header__
import operator
from typing import Callable
from cp_library.misc.typing import _T

def presum2d(A: list[list[_T]], op: Callable[[_T,_T],_T] = operator.add, initial: _T = None, step = 1) -> list[_T]:
    if initial is None:
        N, M, B = len(A), len(A[0]), [Ai[:] for Ai in A]
    else:
        N, M, B = len(A)+1, len(A[0])+1, [[initial]*M for _ in range(N)]
        for i in range(1,N):
            for j in range(1,M):
                B[i][j] = A[i-1][j-1]
    for i in range(N-step):
        for j in range(M):
            B[i+step][j] = op(B[i+step][j], B[i][j])
    for i in range(N):
        for j in range(M-step):
            B[i][j+step] = op(B[i][j+step], B[i][j])
    return B