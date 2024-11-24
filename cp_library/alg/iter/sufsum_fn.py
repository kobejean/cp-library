import cp_library.alg.iter.__header__
from itertools import accumulate
from typing import Callable, Reversible, TypeVar

T = TypeVar('T')
def sufsum(iter: Reversible[T], func: Callable[[T,T],T] = None, initial: T = None) -> list[T]:
    return list(accumulate(reversed(iter), func, initial=initial))[::-1]