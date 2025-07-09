import cp_library.__header__
import operator
from typing import Generic
from cp_library.misc.typing import _T
import cp_library.ds.__header__
from cp_library.ds.elist_fn import elist
import cp_library.ds.heap.__header__

class SkewHeapForrest(Generic[_T]):
    def __init__(shf, N, M, e: _T = 0, op = operator.add):
        shf.V, shf.A, shf.L, shf.R, shf.roots = [e]*M, [e]*M, [-1]*M, [-1]*M, [-1]*N
        shf.id, shf.st, shf.e, shf.op = 0, elist(M), e, op
    
    def propagate(shf, u: int):
        if (a := shf.A[u]) != shf.e:
            if ~(l := shf.L[u]): shf.A[l] = shf.op(shf.A[l], a)
            if ~(r := shf.R[u]): shf.A[r] = shf.op(shf.A[r], a)
            shf.V[u] = shf.op(shf.V[u], a); shf.A[u] = shf.e

    def merge(shf, u: int, v: int):
        while ~u and ~v:
            shf.propagate(u); shf.propagate(v)
            if shf.V[v] < shf.V[u]: u, v = v, u
            shf.st.append(u); shf.R[u], u = shf.L[u], shf.R[u]
        u = u if ~u else v
        while shf.st: shf.L[u := shf.st.pop()] = u
        return u
    
    def min(shf, i: int):
        assert ~(root := shf.roots[i])
        shf.propagate(root)
        return shf.V[root]

    def push(shf, i: int, x: _T):
        shf.V[shf.id] = x
        shf.roots[i] = shf.merge(shf.roots[i], shf.id)
        shf.id += 1

    def pop(shf, i: int) -> _T:
        assert ~(root := shf.roots[i])
        shf.propagate(root)
        val, shf.roots[i] = shf.V[root], shf.merge(shf.L[root], shf.R[root])
        return val
    
    def add(shf, i: int, val: _T): shf.A[shf.roots[i]] = shf.op(shf.A[shf.roots[i]], val)
    def empty(shf, i: int): return shf.roots[i] == -1
    