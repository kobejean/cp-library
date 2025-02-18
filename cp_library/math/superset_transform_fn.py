import cp_library.math.__header__
from cp_library.misc.typing import _T
import operator

def superset_transform(A: list[_T], N: int, Z: int = None, /, op = operator.add) -> list[_T]:
    Z = 1<<N
    for i in range(N):
        m = b = 1<<i
        while m < Z: A[m^b], m = op(A[m^b], A[m]), m+1|b
    return A