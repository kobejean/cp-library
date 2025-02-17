import cp_library.math.__header__
from cp_library.math.subset_zeta_fn import subset_zeta
from cp_library.math.subset_mobius_fn import subset_mobius

def or_conv(A: list[int], B: list[int], N: int, block: int = 5) -> list[int]:
    A, B = subset_zeta(A, N, block), subset_zeta(B, N, block)
    for i, b in enumerate(B): A[i] *= b
    return subset_mobius(A)
