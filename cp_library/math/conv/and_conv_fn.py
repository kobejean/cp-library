import cp_library.math.conv.__header__
import operator
from typing import Callable
from cp_library.misc.typing import _T
from cp_library.math.conv.superset_transform_fn import superset_transform

def and_conv(A: list[_T], B: list[_T], N: int,
             mul: Callable[[_T,_T],_T] = operator.mul,
             sub: Callable[[_T,_T],_T] = operator.sub,
             add: Callable[[_T,_T],_T] = operator.add) -> list[_T]:
    assert len(A) == len(B)
    superset_transform(A, N, op=add), superset_transform(B, N, op=add)
    for i, b in enumerate(B): A[i] = mul(A[i], b)
    return superset_transform(A, N, op=sub)
