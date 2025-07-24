import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.sps.__header__
from cp_library.math.sps.mod.sps_exp_small_fn import sps_exp_small
from cp_library.math.sps.mod.sps_exp_half_fn import sps_exp_half

def sps_exp(P, mod):
    N = len(P).bit_length() - 1
    return sps_exp_half(P, mod) if N > 17 else sps_exp_small(P, mod)
