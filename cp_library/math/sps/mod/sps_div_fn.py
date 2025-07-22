from cp_library.math.conv.mod.subset_deconv_fn import subset_deconv
import cp_library.math.sps.__header__

def sps_div(A, B, mod):
    N = len(A).bit_length() - 1
    return subset_deconv(A, B, N, mod)