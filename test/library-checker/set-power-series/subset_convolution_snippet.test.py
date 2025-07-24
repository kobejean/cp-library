# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution

def main():
    mod = 998244353
    n = rd()
    a = rdl(1 << n)
    b = rdl(1 << n)
    wtnl(subset_conv(a, b, n, mod))

from cp_library.alg.dp.butterfly.butterfly_masks_fn import ior_zeta_pair, ior_mobius
from cp_library.bit.popcnts_fn import popcnts

def subset_conv(A,B,N,mod):
    assert len(A) == len(B)
    Z = (N+1)*(M := 1<<N)
    Ar,Br,Cr,P = [0]*Z, [0]*Z, [0]*Z, popcnts(N)
    for i,p in enumerate(P): Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]
    ior_zeta_pair(Ar, Br, N)
    for i in range(Z): Ar[i], Br[i] = Ar[i]%mod, Br[i]%mod
    for i in range(0,Z,M):
        for j in range(0,Z-i,M):
            ij = i+j
            for k in range(M): Cr[ijk] = (Cr[ijk:=ij|k] + Ar[i|k] * Br[j|k]) % mod
    ior_mobius(Cr, N)
    for i,p in enumerate(P): A[i] = Cr[p<<N|i] % mod
    return A

from cp_library.io.fast.fast_io_fn import rd, rdl, wtnl

main()