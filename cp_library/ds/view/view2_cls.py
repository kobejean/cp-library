
from cp_library.alg.iter.sort.isort_ranged_fn import isort_ranged
import cp_library.__header__
from typing import Generic
from cp_library.misc.typing import _S, _T
import cp_library.ds.__header__
import cp_library.ds.view.__header__

class view2(Generic[_S, _T]):
    __slots__ = 'A', 'B', 'l', 'r'
    def __init__(V, A: list[_S], B: list[_T], l: int, r: int): V.A, V.B, V.l, V.r = A, B, l, r
    def __len__(V): return V.r - V.l
    def __getitem__(V, i: int): 
        if 0 <= i < V.r - V.l: return V.A[V.l+i], V.B[V.l+i]
        else: raise IndexError
    def __setitem__(V, i: int, v: tuple[_S, _T]): V.A[V.l+i], V.B[V.l+i] = v
    def __contains__(V, v: tuple[_S, _T]): raise NotImplemented
    def set_range(V, l: int, r: int): V.l, V.r = l, r
    def index(V, v: tuple[_S, _T]): raise NotImplemented
    def reverse(V):
        l, r = V.l, V.r-1
        while l < r: V.A[l], V.A[r] = V.A[r], V.A[l]; V.B[l], V.B[r] = V.B[r], V.B[l]; l += 1; r -= 1
    def sort(V, reverse=False): isort_ranged(V.A, V.B, l=V.l, r=V.r, reverse=reverse)
    def pop(V): V.r -= 1; return V.A[V.r], V.B[V.r]
    def append(V, v: tuple[_S, _T]): V.A[V.r], V.B[V.r] = v; V.r += 1
    def popleft(V): V.l += 1; return V.A[V.l-1], V.B[V.l-1]
    def appendleft(V, v: tuple[_S, _T]): V.l -= 1; V.A[V.l], V.B[V.l]  = v; 
    def validate(V): return 0 <= V.l <= V.r <= len(V.A)