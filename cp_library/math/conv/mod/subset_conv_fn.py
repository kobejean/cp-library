import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
import cp_library.math.conv.mod.__header__
from cp_library.math.conv.mod.isubset_conv_fn import isubset_conv

def subset_conv(A: list[int], B: list[int], N: int, mod: int) -> list[int]:
    return isubset_conv(A[:], B, N, mod)