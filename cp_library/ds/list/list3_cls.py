from cp_library.alg.iter.sort.isort_parallel_fn import isort_parallel
import cp_library.__header__
from typing import Generic
from cp_library.misc.typing import _T1, _T2, _T3
import cp_library.ds.__header__
import cp_library.ds.view.__header__

class list3(Generic[_T1, _T2, _T3]):
    __slots__ = 'A1', 'A2', 'A3'
    def __init__(lst, A1: list[_T1], A2: list[_T2], A3: list[_T3]):
        lst.A1, lst.A2, lst.A3 = A1, A2, A3
    def __len__(lst): return len(lst.A1)
    def __getitem__(lst, i: int): return lst.A1[i], lst.A2[i], lst.A3[i]
    def __setitem__(lst, i: int, v: tuple[_T1, _T2, _T3]): lst.A1[i], lst.A2[i], lst.A3[i] = v
    def __contains__(lst, v: tuple[_T1, _T2, _T3]): raise NotImplementedError
    def index(lst, v: tuple[_T1, _T2, _T3]): raise NotImplementedError
    def reverse(lst): lst.A1.reverse(); lst.A2.reverse(); lst.A3.reverse()
    def sort(lst, reverse=False): isort_parallel(lst.A1, lst.A2, lst.A3, reverse=reverse)
    def pop(lst): return lst.A1.pop(), lst.A2.pop(), lst.A3.pop()
    def append(lst, v: tuple[_T1, _T2, _T3]):
        v1, v2, v3 = v
        lst.A1.append(v1); lst.A2.append(v2); lst.A3.append(v3)
    def add(lst, i: int, v: tuple[_T1, _T2, _T3]): lst.A1[i] += v[0]; lst.A2[i] += v[1]; lst.A3[i] += v[2]