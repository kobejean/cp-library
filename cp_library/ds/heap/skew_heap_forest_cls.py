import cp_library.ds.heap.__header__
from cp_library.ds.elist_fn import elist
from typing import Generic
from cp_library.misc.typing import _T

class SkewHeapForest(Generic[_T]):
    def __init__(shf, N, M, e: _T = 0):
        shf.V, shf.A, shf.L, shf.R, shf.roots = [e]*M, [e]*M, [-1]*M, [-1]*M, [-1]*N
        shf.id, shf.st = 0, elist(M)
    
    def propagate(shf, u: int):
        if (add := shf.A[u]):
            if (l := shf.L[u]) != -1: shf.A[l] += add
            if (r := shf.R[u]) != -1: shf.A[r] += add
            shf.V[u] += add
            shf.A[u] = 0

    def merge(shf, u: int, v: int):
        while u >= 0 and v >= 0:
            if shf.V[v]+shf.A[v] < shf.V[u]+shf.A[u]: u, v = v, u
            shf.propagate(u); shf.st.append(u); shf.R[u], u = shf.L[u], shf.R[u]
        u = v if u == -1 else u
        while shf.st: shf.L[u := shf.st.pop()] = u
        return u
    
    def min(shf, i: int):
        assert (root := shf.roots[i]) >= 0
        shf.propagate(root)
        return shf.V[root]

    def push(shf, i: int, x: _T):
        shf.id = (id := shf.id)+1
        shf.V[id] = x
        shf.roots[i] = shf.merge(shf.roots[i], id)

    def pop(shf, i: int) -> _T:
        assert (root := shf.roots[i]) >= 0
        shf.propagate(root := shf.roots[i])
        val = shf.V[root]
        shf.roots[i] = shf.merge(shf.L[root], shf.R[root])
        return val
    
    def add(shf, i: int, val: _T): shf.A[shf.roots[i]] += val
    def empty(shf, i: int): return shf.roots[i] == -1
    