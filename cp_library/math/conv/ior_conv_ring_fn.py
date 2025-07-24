import cp_library.__header__
import operator
from typing import Callable
from cp_library.misc.typing import _T
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.ior_transform_fn import ior_transform

def ior_conv_ring(A: list[_T], B: list[_T], N: int,
            mul: Callable[[_T,_T],_T] = operator.mul,
            sub: Callable[[_T,_T],_T] = operator.sub,
            add: Callable[[_T,_T],_T] = operator.add) -> list[_T]:
    assert len(A) == len(B)
    ior_transform(A, N, op=add), ior_transform(B, N, op=add)
    for i, b in enumerate(B): A[i] = mul(A[i], b)
    return ior_transform(A, N, op=sub)
