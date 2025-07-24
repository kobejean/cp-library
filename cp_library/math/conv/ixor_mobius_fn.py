import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.ixor_zeta_fn import ixor_zeta

def ixor_mobius(A: list, N: int):
    ixor_zeta(A, N)
    for i, a in enumerate(A): A[i] = a >> N
    return A
