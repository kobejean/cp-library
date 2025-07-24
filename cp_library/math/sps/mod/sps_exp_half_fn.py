from cp_library.bit.popcnts_fn import popcnts
import cp_library.__header__
from cp_library.ds.view.view_cls import view
import cp_library.math.__header__
from cp_library.math.conv.ior_zeta_fn import ior_zeta
from cp_library.math.conv.ior_mobius_fn import ior_mobius
import cp_library.math.sps.__header__

def subset_conv_half(Ar: list[int], B: list[int], n: int, N: int, mod: int, pcnt) -> list[int]:
    Br = [0]*(z := (n+1)*(m := 1<<n))
    for i in range(m): Br[pcnt[i]<<n|i] = B[i]
    ior_zeta(Br, n)
    for i in range(z): Br[i] = Br[i]%mod
    for ij in range(n,-1,-1):
        ij_ = (ij+1)<<N|m
        for i in range(ij+1):
            j = ij-i; j_ = j<<N; i_ = i<<n
            for k in range(m): Ar[ij_|k] = (Ar[ij_|k] + Br[i_|k] * Ar[j_|k]) % mod
    for i in range(n+1):
        i = i << N
        for k in range(m): Ar[i|k|m] += Ar[i|k]

def sps_exp_half(P, mod):
    assert P[0] == 0
    N = len(P).bit_length() - 1
    Z = (N+1)*(M := 1<<N)
    exp = [0]*Z; exp[0] = 1
    pcnt = popcnts(N)
    P = view(P); m = 1
    for n in range(N):
        P.set_range(m, m := m<<1)
        subset_conv_half(exp, P, n, N, mod, pcnt)
    ior_mobius(exp, N)
    return [exp[p<<N|i] % mod for i,p in enumerate(pcnt)]