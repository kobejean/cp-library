import cp_library.__header__
from cp_library.ds.view.view_cls import view
import cp_library.math.__header__
import cp_library.math.sps.__header__
import cp_library.math.sps.mod.__header__
from cp_library.math.conv.mod.subset_conv_fn import subset_conv

def sps_pow_proj(A, B, M, mod):
    N = len(B).bit_length() - 1
    assert B[0] == 0, "B[0] must be 0 for sps_pow_proj"
    Aview, Bview, P = view(A := A[::-1]), view(B), []
    for i in range(N + 1):
        P.append(A[(1<<N)-1]); A[(1<<N)-1] = 0
        for m in range(N - i):
            i0 = (1<<N)-(1<<(m+1)); i1 = 1 << m
            Aview.set_range(i0, i0 + (1 << m)); Bview.set_range(i1, i1 + (1 << m))
            R = subset_conv(Aview, Bview, m, mod)
            i2 = (1<<N)-(1<<m)
            for h in range(1 << m):
                A[i2 + h] = (A[i2 + h] + R[h]) % mod
                A[i0 + h] = 0
    return P[:M]