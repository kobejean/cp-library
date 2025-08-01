import cp_library.__header__
from typing import Callable, Generic
from cp_library.misc.typing import _T

import cp_library.alg.__header__
import cp_library.alg.tree.__header__
import cp_library.alg.tree.csr.__header__
from cp_library.alg.tree.csr.hld_base_cls import HLDBase
from cp_library.alg.tree.csr.tree_base_cls import TreeBase

class HLDMonoid(HLDBase, Generic[_T]):
    def __init__(hld, T: TreeBase, op: Callable[[_T,_T],_T], e: _T, A: list[_T], r=0):
        super().__init__(T, r)
        hld.op, hld.e = op, e
        B = [A[u] for u in hld.order]
        hld.pre = SegTree(op, e, B)
        B.reverse()
        hld.suf = SegTree(op, e, B)
    
    def get(hld, u) -> _T:
        return hld.pre.get(hld.tin[u])
    __getitem__ = get
    
    def set(hld, u, x: _T):
        hld.pre.set(hld.tin[u], x)
        hld.suf.set(hld.N-1-hld.tin[u], x)
    __setitem__ = set

    def path_query(hld, u, v, edge=False):
        us = vs = hld.e
        while hld.head[u] != hld.head[v]:
            if hld.depth[hld.head[u]] < hld.depth[hld.head[v]]:
                vs = hld.op(hld.pre.prod(hld.tin[hld.head[v]], hld.tin[v]+1), vs)
                v = hld.up[v]
            else:
                us = hld.op(us, hld.suf.prod(hld.N-1-hld.tin[u], hld.N-hld.tin[hld.head[u]]))
                u = hld.up[u]

        if hld.depth[u] < hld.depth[v]:
            vs = hld.op(hld.pre.prod(hld.tin[u]+edge, hld.tin[v]+1), vs)
        else:
            us = hld.op(us, hld.suf.prod(hld.N-1-hld.tin[u], hld.N-hld.tin[v]-edge))
        return hld.op(us, vs)

from cp_library.ds.tree.seg.segtree_cls import SegTree