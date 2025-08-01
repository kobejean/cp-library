import cp_library.__header__
from cp_library.ds.list.elist_fn import elist
from cp_library.ds.view.view_cls import view
import cp_library.math.__header__
from cp_library.math.conv.mod.subset_conv_fn import subset_conv
import cp_library.math.sps.__header__

def sps_exp(P, mod):
    assert P[0] == 0
    exp = elist(1 << (N := len(P).bit_length()-1)); exp.append(1); P = view(P); m = 1
    for n in range(N): P.set_range(m, m := m<<1); exp.extend(subset_conv(P, exp, n, mod))
    return exp