
import cp_library.__header__
from typing import Generic
from cp_library.misc.typing import _T
import cp_library.ds.__header__
from cp_library.ds.list.list_find_fn import list_find
import cp_library.ds.view.__header__

class view(Generic[_T]):
    __slots__ = 'A', 'l', 'r'
    def __init__(V, A: list[_T], l: int = 0, r: int = 0): V.A, V.l, V.r = A, l, r
    def __len__(V): return V.r - V.l
    def __getitem__(V, i: int): 
        if 0 <= i < V.r - V.l: return V.A[V.l+i]
        else: raise IndexError
    def __setitem__(V, i: int, v: _T): V.A[V.l+i] = v
    def __contains__(V, v: _T): return list_find(V.A, v, V.l, V.r) != -1
    def set_range(V, l: int, r: int): V.l, V.r = l, r
    def index(V, v: _T): return V.A.index(v, V.l, V.r) - V.l
    def reverse(V):
        l, r = V.l, V.r-1
        while l < r: V.A[l], V.A[r] = V.A[r], V.A[l]; l += 1; r -= 1
    def sort(V, /, *args, **kwargs):
        A = V.A[V.l:V.r]; A.sort(*args, **kwargs)
        for i,a in enumerate(A,V.l): V.A[i] = a
    def pop(V): V.r -= 1; return V.A[V.r]
    def append(V, v: _T): V.A[V.r] = v; V.r += 1
    def popleft(V): V.l += 1; return V.A[V.l-1]
    def appendleft(V, v: _T): V.l -= 1; V.A[V.l] = v; 
    def validate(V): return 0 <= V.l <= V.r <= len(V.A)