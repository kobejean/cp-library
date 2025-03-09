import cp_library.__header__
from cp_library.alg.dp.monotone_minima_fn import monotone_minima
import cp_library.math.__header__
import cp_library.math.conv.__header__

def minplus_conv_arb_cnvx(arb: list[int], cnvx: list[int]) -> list[int]:
    N, M = len(cnvx), len(arb)
    def cmp(i, j, k):
        return i >= k and (i-j >= N or (cnvx[i-j] + arb[j] >= cnvx[i-k] + arb[k]))
    cols = monotone_minima(N+M-1, M, cmp)
    return [arb[j] + cnvx[i-j] for i, j in enumerate(cols)]

def minplus_conv_cnvx(A: list[int], B: list[int]) -> list[int]:
    if not (N := len(A)) | (M := len(B)): return []
    C = [0] * (K:=N+M-1)
    C[0], I, J = A[i := 0] + B[j := 0], N-1, M-1
    for k in range(1, K):
        if j == J or (i != I and A[i+1] + B[j] < A[i] + B[j+1]): i += 1
        else: j += 1
        C[k] = A[i] + B[j]
    return C

def minplus_iconv(A: list[int], B: list[int]):
    N, M = len(A), len(B)
    for i in range(N-1,-1,-1):
        A[i] = min(B[j] + A[i-j] for j in range(min(M,i+1)))   
