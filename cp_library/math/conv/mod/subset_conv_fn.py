import cp_library.__header__
from cp_library.bit.popcnts_fn import popcnts
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.mod.isubset_conv_ranked_fn import isubset_conv_ranked
import cp_library.math.conv.mod.__header__

def subset_conv(A: list[int], B: list[int], N: int, mod: int) -> list[int]:
    Z = (N+1)*(M:=1<<N)
    Ar, Br, C, P = [0]*Z, [0]*Z, [0]*M, popcnts(N)
    for i, p in enumerate(P): Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]
    isubset_conv_ranked(Ar, Br, N, Z, M, mod)
    for i, p in enumerate(P): C[i] = Ar[p<<N|i] % mod
    return C