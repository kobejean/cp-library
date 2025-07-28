import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.sps.__header__
import cp_library.math.sps.mod.__header__
from cp_library.math.sps.mod.sps_ln_small_fn import sps_ln_small
from cp_library.math.sps.mod.sps_ln_fn import sps_ln

def sps_ln_adaptive(P, mod): return sps_ln(P, mod) if len(P).bit_length()-1 > 17 else sps_ln_small(P, mod)
