import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
import cp_library.math.conv.mod.__header__
from cp_library.math.conv.mod.ixor_conv_fn import ixor_conv

def xor_conv(A: list[int], B: list[int], N: int, mod: int) -> list[int]:
    return ixor_conv(A[:], B[:], N, mod)
