import cp_library.__header__
from cp_library.bit.popcnts_fn import popcnts
from cp_library.ds.list.elist_fn import elist
from cp_library.ds.view.view_cls import view
import cp_library.math.__header__
from cp_library.math.conv.ior_zeta_fn import ior_zeta
from cp_library.math.conv.ior_mobius_ranked_fn import ior_mobius_ranked
import cp_library.math.sps.__header__
import cp_library.math.sps.mod.__header__

def isubset_conv_zeta_ranked(Ar: list[int], Br: list[int], n: int, N: int, mod: int) -> list[int]:
    m = 1<<n
    for ij in range(n,-1,-1):
        ij_, i_ = (ij+1)<<N|m, ij<<n
        for k in range(m): Ar[ij_|k] = Br[i_|k] * Ar[k] % mod
        for i in range(ij):
            j = ij-i; i_, j_ = i<<n, j<<N
            for k in range(m): Ar[ij_|k] = (Ar[ij_|k] + Br[i_|k] * Ar[j_|k]) % mod

def sps_composite(A: list[int], B: list[int], mod: int) -> list[int]:
    C = [0]*(M := 1 << (N := len(B).bit_length() - 1))
    if not A: return C
    dA, B0, B1, Br, Cr, pcnt = A[:], elist(N+1), view(B), elist(N), [0]*(Z := (N+1)*M), popcnts(N)
    for n in range(N+1):
        if n < N:
            # zeta transform of ranked 
            B1.set_range(1<<n, 2<<n)
            br = [0]*(z := (n+1)*(m := 1<<n))
            for i in range(m): br[pcnt[i]<<n|i] = B1[i]
            ior_zeta(br, n)
            for i in range(z): br[i] %= mod
            Br.append(br)
        # evaluate current polynomial at B[0] using Horner's method
        t = 0
        for j in range(len(dA)-1, -1, -1): t = (t * B[0] + dA[j]) % mod
        B0.append(t)
        # update dA to be the derivative
        for j in range(1, len(dA)): dA[j-1] = (j * dA[j]) % mod
        if dA: dA[-1] = 0
    for n in range(N+1):
        for m in range(n-1, -1, -1):
            # effectively computes `C[1<<m:2<<m] = subset_conv(C[:1<<m], B[1<<m:2<<m])`
            # but basically maintains `Cr`, the ranked zeta transformed `C`
            # partial zeta updates need to be made after loop ends to propagate contributions
            isubset_conv_zeta_ranked(Cr, Br[m], m, N, mod)
        # partial zeta updates
        for m in range(n):
            b = 1 << m
            for j in range(m+1):
                j <<= N
                for k in range(j, j|b): Cr[k|b] += Cr[k]
        for k in range(1<<n): Cr[k] = B0[~n]
    ior_mobius_ranked(Cr, N, M, Z)
    for i, p in enumerate(pcnt): C[i] = Cr[p<<N|i] % mod
    return C