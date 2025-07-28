import cp_library.__header__
import cp_library.math.__header__
from cp_library.math.conv.subset_deconv_fn import subset_deconv
import cp_library.math.sps.__header__

def sps_div(A, B): return subset_deconv(A, B, len(A).bit_length()-1)