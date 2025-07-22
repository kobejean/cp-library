import cp_library.__header__
from typing import Generic
from cp_library.misc.typing import _T1, _T2
from cp_library.alg.iter.sort.isort_ranged_fn import isort_ranged
import cp_library.ds.__header__
import cp_library.ds.view.__header__

class view2(Generic[_T1, _T2]):
    __slots__ = 'A1', 'A2', 'l', 'r'
    def __init__(V, A1: list[_T1], A2: list[_T2], l: int = 0, r: int = 0): V.A1, V.A2, V.l, V.r = A1, A2, l, r
    def __len__(V): return V.r - V.l
    def __getitem__(V, i: int): 
        if 0 <= i < V.r - V.l: return V.A1[V.l+i], V.A2[V.l+i]
        else: raise IndexError
    def __setitem__(V, i: int, v: tuple[_T1, _T2]): V.A1[V.l+i], V.A2[V.l+i] = v
    def __contains__(V, v: tuple[_T1, _T2]): raise NotImplemented
    def set_range(V, l: int, r: int): V.l, V.r = l, r
    def index(V, v: tuple[_T1, _T2]): raise NotImplemented
    def reverse(V):
        l, r = V.l, V.r-1
        while l < r: V.A1[l], V.A1[r] = V.A1[r], V.A1[l]; V.A2[l], V.A2[r] = V.A2[r], V.A2[l]; l += 1; r -= 1
    def sort(V, reverse=False): isort_ranged(V.A1, V.A2, l=V.l, r=V.r, reverse=reverse)
    def pop(V): V.r -= 1; return V.A1[V.r], V.A2[V.r]
    def append(V, v: tuple[_T1, _T2]): V.A1[V.r], V.A2[V.r] = v; V.r += 1
    def popleft(V): V.l += 1; return V.A1[V.l-1], V.A2[V.l-1]
    def appendleft(V, v: tuple[_T1, _T2]): V.l -= 1; V.A1[V.l], V.A2[V.l]  = v; 
    def validate(V): return 0 <= V.l <= V.r <= len(V.A1)