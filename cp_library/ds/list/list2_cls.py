from cp_library.alg.iter.sort.isort_parallel_fn import isort_parallel
import cp_library.__header__
from typing import Generic
from cp_library.misc.typing import _T1, _T2
import cp_library.ds.__header__
import cp_library.ds.view.__header__

class list2(Generic[_T1, _T2]):
    __slots__ = 'A1', 'A2'
    def __init__(lst, A1: list[_T1], A2: list[_T2]): lst.A1, lst.A2 = A1, A2
    def __len__(lst): return len(lst.A1)
    def __getitem__(lst, i: int): return lst.A1[i], lst.A2[i]
    def __setitem__(lst, i: int, v: tuple[_T1, _T2]): lst.A1[i], lst.A2[i] = v
    def __contains__(lst, v: tuple[_T1, _T2]): raise NotImplementedError
    def index(lst, v: tuple[_T1, _T2]): raise NotImplementedError
    def reverse(lst): lst.A1.reverse(); lst.A2.reverse()
    def sort(lst, reverse=False): isort_parallel(lst.A1, lst.A2, reverse=reverse)
    def pop(lst): return lst.A1.pop(), lst.A2.pop()
    def append(lst, v: tuple[_T1, _T2]): v1, v2 = v; lst.A1.append(v1); lst.A2.append(v2)
    def add(lst, i: int, v: tuple[_T1, _T2]): lst.A1[i] += v[0]; lst.A2[i] += v[1]