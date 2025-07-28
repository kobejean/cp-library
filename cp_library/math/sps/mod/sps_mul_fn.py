import cp_library.__header__
import cp_library.math.__header__
from cp_library.math.conv.mod.subset_conv_fn import subset_conv
import cp_library.math.sps.__header__

def sps_mul(A, B, mod):
    N = len(A).bit_length() - 1
    return subset_conv(A, B, N, mod)