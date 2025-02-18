import cp_library.math.conv.__header__
from cp_library.math.conv.subset_transform_fn import subset_transform
import operator
from typing import Callable
from cp_library.misc.typing import _T

def or_conv(A: list[_T], B: list[_T], N: int,
            mul: Callable[[_T,_T],_T] = operator.mul,
            sub: Callable[[_T,_T],_T] = operator.sub,
            add: Callable[[_T,_T],_T] = operator.add) -> list[_T]:
    assert len(A) == len(B)
    subset_transform(A, N, op=add), subset_transform(B, N, op=add)
    for i, b in enumerate(B): A[i] = mul(A[i], b)
    return subset_transform(A, N, op=sub)
