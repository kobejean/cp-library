import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.cnt.__header__
from typing import Iterable, Union

def counter(A: Iterable[int] = tuple(), N: Union[int,list[int],None] = None):
    if isinstance(N, int): cnt = [0]*N
    elif N is None: cnt = [0]*(N := max(A := list(A))+1)
    else:  N, cnt = len(N), N
    for a in A: cnt[a] += 1
    return cnt