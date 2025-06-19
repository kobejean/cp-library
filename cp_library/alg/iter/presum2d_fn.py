import cp_library.__header__
from cp_library.misc.typing import _T
import operator
import cp_library.alg.__header__
import cp_library.alg.iter.__header__

def presum2d(A: list[list[_T]], op = operator.add, initial: _T = None, step = 1) -> list[list[_T]]:
    if initial is None:
        N, M, B = len(A), len(A[0]), [Ai[:] for Ai in A]
    else:
        N, M = len(A)+1, len(A[0])+1
        B = [[initial]*M for _ in range(N)]
        for i in range(N-1):
            for j in range(M-1):
                B[i+1][j+1] = A[i][j]
    for i in range(N-step):
        for j in range(M):
            B[i+step][j] = op(B[i+step][j], B[i][j])
    for i in range(N):
        for j in range(M-step):
            B[i][j+step] = op(B[i][j+step], B[i][j])
    return B