import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.sps.__header__
import cp_library.math.sps.mod.__header__
from cp_library.math.conv.mod.subset_deconv_fn import subset_deconv

def sps_div(A, B, mod): return subset_deconv(A, B, len(A).bit_length() - 1, mod)