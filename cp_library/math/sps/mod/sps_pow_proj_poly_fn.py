import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.sps.__header__
import cp_library.math.sps.mod.__header__
from cp_library.math.sps.mod.sps_pow_proj_fn import sps_pow_proj

def sps_pow_proj_poly(A, B, M, mod):
    N = len(B).bit_length()-1; b = B[0]; B[0] = 0
    P, F, H = sps_pow_proj(A, B, N + 1, mod), [], [0]*(N+1); H[0] = 1
    for i in range(M):
        v = 0
        for j in range(N + 1):
            if j < len(P): v = (v+H[j]*P[j])%mod
        F.append(v)
        for j in range(N-1, -1, -1): H[j+1]=H[j]*(i+1)%mod
        H[0]=H[0]*b%mod
    return F