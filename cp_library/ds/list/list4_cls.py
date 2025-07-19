from cp_library.alg.iter.sort.isort_parallel_fn import isort_parallel
import cp_library.__header__
from typing import Generic
from cp_library.misc.typing import _T1, _T2, _T3, _T4
import cp_library.ds.__header__
import cp_library.ds.view.__header__

class list4(Generic[_T1, _T2, _T3, _T4]):
    __slots__ = 'A1', 'A2', 'A3', 'A4'
    def __init__(lst, A1: list[_T1], A2: list[_T2], A3: list[_T3], A4: list[_T4]):
        lst.A1, lst.A2, lst.A3, lst.A4 = A1, A2, A3, A4
    def __len__(lst): return len(lst.A1)
    def __getitem__(lst, i: int): return lst.A1[i], lst.A2[i], lst.A3[i], lst.A4[i]
    def __setitem__(lst, i: int, v: tuple[_T1, _T2, _T3, _T4]): lst.A1[i], lst.A2[i], lst.A3[i], lst.A4[i] = v
    def __contains__(lst, v: tuple[_T1, _T2, _T3, _T4]): raise NotImplementedError
    def index(lst, v: tuple[_T1, _T2, _T3, _T4]): raise NotImplementedError
    def reverse(lst): lst.A1.reverse(); lst.A2.reverse(); lst.A3.reverse(); lst.A4.reverse()
    def sort(lst, reverse=False): isort_parallel(lst.A1, lst.A2, lst.A3, lst.A4, reverse=reverse)
    def pop(lst): return lst.A1.pop(), lst.A2.pop(), lst.A3.pop(), lst.A4.pop()
    def append(lst, v: tuple[_T1, _T2, _T3, _T4]):
        v1, v2, v3, v4 = v
        lst.A1.append(v1); lst.A2.append(v2); lst.A3.append(v3); lst.A4.append(v4)
    def add(lst, i: int, v: tuple[_T1, _T2, _T3, _T4]): lst.A1[i] += v[0]; lst.A2[i] += v[1]; lst.A3[i] += v[2]; lst.A4[i] += v[3]