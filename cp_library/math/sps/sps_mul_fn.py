import cp_library.__header__
import cp_library.math.__header__
from cp_library.math.conv.subset_conv_fn import subset_conv
import cp_library.math.sps.__header__

def sps_mul(A, B): return subset_conv(A, B, len(A).bit_length()-1)