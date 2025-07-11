import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.ixor_conv_fn import ixor_conv

def xor_conv(A: list, B: list, N: int, mod: int):
    return ixor_conv(list(A), list(B), N, mod)
