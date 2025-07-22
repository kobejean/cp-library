from cp_library.math.conv.subset_conv_fn import subset_conv
import cp_library.math.sps.__header__

def sps_mul(A, B):
    N = len(A).bit_length() - 1
    return subset_conv(A, B, N)