import cp_library.__header__
from cp_library.bit.popcnts_fn import popcnts
from cp_library.ds.view.view_cls import view
import cp_library.math.__header__
from cp_library.math.conv.mod.isubset_conv_half_fn import isubset_conv_half
from cp_library.math.conv.ior_mobius_fn import ior_mobius
import cp_library.math.sps.__header__

def sps_exp_half(P, mod):
    assert P[0] == 0
    N = len(P).bit_length() - 1
    Z = (N+1)*(M := 1<<N)
    exp = [0]*Z; exp[0] = 1
    pcnt = popcnts(N)
    P = view(P); m = 1
    for n in range(N):
        P.set_range(m, m := m<<1)
        isubset_conv_half(exp, P, n, N, mod, pcnt)
    ior_mobius(exp, N)
    return [exp[p<<N|i] % mod for i,p in enumerate(pcnt)]