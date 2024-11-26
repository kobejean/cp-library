import cp_library.alg.iter.__header__
import operator
from itertools import accumulate
from typing import Callable, Reversible, TypeVar

T = TypeVar('T')
def sufsum(iter: Reversible[T], func: Callable[[T,T],T] = None, initial: T = None, step = 1) -> list[T]:
    match step:
        case 1:
            A = list(accumulate(reversed(iter), func, initial=initial))
            A.reverse()
            return A   
        case step:
            assert step >= 2
            if func is None:
                func = operator.add
            A = list(reversed(iter))
            if initial is not None:
                A = [initial] + A
            for i in range(step,len(A)):
                A[i] = func(A[i], A[i-step])
            A.reverse()
            return A