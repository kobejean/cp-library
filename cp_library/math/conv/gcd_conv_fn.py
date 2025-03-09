import cp_library.__header__
import operator
from typing import Callable
from cp_library.misc.typing import _T
import cp_library.math.__header__
import cp_library.math.conv.__header__

def gcd_conv(A: list[_T], B: list[_T], N: int,
            mul: Callable[[_T,_T],_T] = operator.mul,
            sub: Callable[[_T,_T],_T] = operator.sub,
            add: Callable[[_T,_T],_T] = operator.add) -> list[_T]:
    return Primes(N).gcd_conv(A, B, add, sub, mul)

from cp_library.math.table.primes_cls import Primes