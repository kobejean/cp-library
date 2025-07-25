import cp_library.__header__
from cp_library.bit.popcnts_fn import popcnts
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.isubset_deconv_ranked_fn import isubset_deconv_ranked

def subset_deconv(A: list[int], B: list[int], N: int) -> list[int]:
    Z = (N+1)*(M:=1<<N)
    Ar, Br, C, P = [0]*Z, [0]*Z, [0]*M, popcnts(N)
    for i, p in enumerate(P): Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]
    isubset_deconv_ranked(Ar, Br, N, Z, M)
    for i, p in enumerate(P): C[i] = Ar[p<<N|i]
    return C