import cp_library.__header__
from cp_library.misc.typing import _T
import operator
import cp_library.math.__header__
import cp_library.math.conv.__header__

def superset_transform(A: list[_T], N: int, /, op = operator.add) -> list[_T]:
    Z = len(A)
    for i in range(N):
        m = b = 1<<i
        while m < Z: A[m^b], m = op(A[m^b], A[m]), m+1|b
    return A