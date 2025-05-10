import cp_library.alg.iter.__header__
import operator
from itertools import accumulate
from typing import Callable, Iterable
from cp_library.misc.typing import _T

def presum(iter: Iterable[_T], func: Callable[[_T,_T],_T] = None, initial: _T = None, step = 1) -> list[_T]:
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