import cp_library.alg.iter.__header__
import operator
from itertools import accumulate
from typing import Callable, Reversible
from cp_library.misc.typing import _T

def sufsum(iter: Reversible[_T], func: Callable[[_T,_T],_T] = None, initial: _T = None, step = 1) -> list[_T]:
    if step == 1:
        A = list(accumulate(reversed(iter), func, initial=initial))
        A.reverse()
        return A   
    else:
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