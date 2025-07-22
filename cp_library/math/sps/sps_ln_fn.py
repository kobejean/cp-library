import cp_library.__header__
from cp_library.ds.elist_fn import elist
from cp_library.ds.view.view_cls import view
import cp_library.math.__header__
from cp_library.math.conv.subset_deconv_fn import subset_deconv
import cp_library.math.sps.__header__

def sps_ln(P):
    assert P[0] == 1
    N = len(P).bit_length() - 1
    P0, P1 = view(P), view(P); m = 1
    ln = elist(1 << N); ln.append(0)
    for n in range(N):
        P0.set_range(0, m); P1.set_range(m, m := m<<1)
        ln.extend(subset_deconv(P0, P1, n))
    return ln