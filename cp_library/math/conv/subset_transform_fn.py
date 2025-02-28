import cp_library.math.conv.__header__
from cp_library.misc.typing import _T
import operator

def subset_transform(A: list[_T], N: int, /, op = operator.add) -> list[_T]:
    Z = len(A)
    for i in range(N):
        m = b = 1<<i
        while m < Z: A[m], m = op(A[m], A[m^b]), m+1|b
    return A