import cp_library.math.conv.__header__
from cp_library.math.conv.subset_zeta_fn import subset_zeta
from cp_library.math.conv.subset_mobius_fn import subset_mobius

def or_conv(A: list[int], B: list[int], N: int) -> list[int]:
    assert len(A) == len(B)
    subset_zeta(A, N), subset_zeta(B, N)
    for i, b in enumerate(B): A[i] *= b
    return subset_mobius(A, N)
