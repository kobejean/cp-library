import cp_library.__header__
import operator
from typing import Generic, TypeVar
from cp_library.misc.typing import _T
import cp_library.ds.__header__
import cp_library.ds.heap.__header__
_TSkewHeap = TypeVar("SkewHeap", bound="SkewHeap")
class SkewHeap(Generic[_T]):
    __slots__ = 'root', 'op', 'e'
    V, A, L, R, st = [-1], [-1], [-1], [-1], []
    def __init__(H, op = operator.add, e: _T = 0):
        H.root, H.op, H.e = -1, op, e
    
    def merge(H: _TSkewHeap, O: _TSkewHeap):
        H.root = H.merge_nodes(H.root, O.root)
        O.root = -1

    def min(H):
        assert ~H.root
        H.propagate(H.root)
        return H.V[H.root]

    def push(H, x: _T):
        id = len(H.V)
        H.V.append(x); H.A.append(H.e); H.L.append(-1); H.R.append(-1)
        H.root = H.merge_nodes(H.root, id)

    def pop(H) -> _T:
        assert ~H.root
        H.propagate(H.root)
        val, H.root = H.V[H.root], H.merge_nodes(H.L[H.root], H.R[H.root])
        return val
    
    def add(H, val: _T): H.A[H.root] = H.op(H.A[H.root], val)
    def empty(H): return H.root == -1
    def __bool__(H): return H.root != -1
    
    def propagate(H, u: int):
        if (a := H.A[u]) != H.e:
            if ~(l := H.L[u]): H.A[l] = H.op(H.A[l], a)
            if ~(r := H.R[u]): H.A[r] = H.op(H.A[r], a)
            H.V[u] = H.op(H.V[u], a); H.A[u] = H.e

    def merge_nodes(H, u: int, v:int):
        while ~u and ~v:
            H.propagate(u); H.propagate(v)
            if H.V[v] < H.V[u]: u, v = v, u
            H.st.append(u); H.R[u], u = H.L[u], H.R[u]
        u = u if ~u else v
        while H.st: H.L[u := H.st.pop()] = u
        return u