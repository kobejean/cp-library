import cp_library.alg.iter.__header__
from itertools import accumulate
from typing import Callable, Iterable, TypeVar

T = TypeVar('T')
def presum(iter: Iterable[T], func: Callable[[T,T],T] = None, initial: T = None) -> list[T]:
    return list(accumulate(iter, func, initial=initial))