import cp_library.alg.iter.__header__
import operator
from itertools import accumulate
from typing import Callable, Iterable, TypeVar

T = TypeVar('T')
def presum(iter: Iterable[T], func: Callable[[T,T],T] = None, initial: T = None, step = 1) -> list[T]:
    if step == 1:
        return list(accumulate(iter, func, initial=initial))
    else:
        assert step >= 2
        if func is None:
            func = operator.add
        A = list(iter)
        if initial is not None:
            A = [initial] + A
        for i in range(step,len(A)):
            A[i] = func(A[i], A[i-step])
        return A