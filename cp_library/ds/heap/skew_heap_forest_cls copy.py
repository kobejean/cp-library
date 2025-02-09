import cp_library.ds.heap.__header__
from cp_library.ds.elist_fn import elist
from typing import Container, Generic, Optional
from cp_library.misc.typing import _T
i32max = (1 << 31)-1

class SkewHeapForest(Generic[_T]):
    def __init__(shf, N, M, e: _T = 0):
        shf.V, shf.A, shf.C = [e]*M, [e]*M, [i32max<<31|i32max]*M
        shf.roots = [i32max]*N
        shf.id = 0
        shf.st = elist(M)
    
    def propagate(shf, u: int):
        if (add := shf.A[u]):
            l, r = shf.C[u] >> 31, shf.C[u] & i32max
            if l < i32max: shf.A[l] += add
            if r < i32max: shf.A[r] += add
            shf.V[u] += add
            shf.A[u] = 0

    def merge(shf, u: int, v: int):
        st, V, A, C = shf.st, shf.V, shf.A, shf.C
        while u < i32max and v < i32max:
            if V[v]+A[v] < V[u]+A[u]: u, v = v, u
            shf.propagate(u)
            st.append(u)
            C[u], u = C[u] >> 31, C[u] & i32max
        u = v if u == i32max else u
        while st: C[u := st.pop()] |= u << 31
        return u
    
    def min(shf, i: int):
        assert (root := shf.roots[i]) < i32max
        shf.propagate(root)
        return shf.V[root]

    def push(shf, i: int, x: _T):
        shf.id = (id := shf.id)+1
        shf.V[id] = x
        shf.roots[i] = shf.merge(shf.roots[i], id)

    def pop(shf, i: int) -> _T:
        assert (root := shf.roots[i]) < i32max
        shf.propagate(root)
        val = shf.V[root]
        shf.roots[i] = shf.merge(shf.C[root] >> 31, shf.C[root] & i32max)
        return val
    
    def add(shf, i: int, val: _T):
        shf.A[shf.roots[i]] += val

    def empty(shf, i: int):
        return shf.roots[i] == i32max
    