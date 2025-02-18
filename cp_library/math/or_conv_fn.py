import operator
from typing import Callable
import cp_library.math.__header__
from cp_library.math.subset_zeta_fn import subset_zeta
from cp_library.math.subset_mobius_fn import subset_mobius

def or_conv(A: list[int], B: list[int], N: int,
            add: Callable[[int,int],int] = operator.add,
            sub: Callable[[int,int],int] = operator.sub,
            mul: Callable[[int,int],int] = operator.mul) -> list[int]:
    subset_zeta(A, N), subset_zeta(B, N)
    for i, b in enumerate(B): A[i] *= b
    return subset_mobius(A, N)
