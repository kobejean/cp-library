import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.tree.__header__
import cp_library.alg.tree.fast.__header__
from cp_library.alg.tree.fast.hld_base_cls import HLDBase
from cp_library.alg.tree.fast.tree_base_cls import TreeBase

class HLDBIT(HLDBase):
    def __init__(hld, T: TreeBase, A: list[int], r=0):
        super().__init__(T, r)
        if len(A) == T.N:
            hld.bit = BIT([A[u] for u in hld.order])
            hld.edge_queries = False
            hld.ptr = hld.tin
        elif len(A) == T.M:
            hld.bit = BIT([A[T.Ea[i]] if (i := hld.back[u]) >= 0 else 0 for u in hld.order])
            hld.edge_queries = True
            hld.ptr = [0]*T.M
            for i in hld.back:
                if i == -1: continue
                hld.ptr[T.Ea[i]] = hld.tin[T.Ua[i]]
    
    def add(hld, u: int, x: int):
        hld.bit.add(hld.ptr[u], x)
        
    def get(hld, u: int):
        return hld.bit.get(hld.ptr[u])
    __getitem__ = get

    def set(hld, u: int, x: int):
        hld.bit.set(hld.ptr[u], x)
    __setitem__ = set

    def subtree_range(hld, u):
        return hld.tin[u]+hld.edge_queries, hld.tout[u]

    def subtree_query(hld, u):
        l, r = hld.subtree_range(u)
        return hld.bit.range_sum(l, r)

    def path_query(hld, u, v):
        us = uv = 0
        while hld.head[u] != hld.head[v]:
            if hld.depth[hld.head[u]] < hld.depth[hld.head[v]]:
                uv += hld.bit.range_sum(hld.tin[hld.head[v]], hld.tin[v]+1)
                v = hld.up[v]
            else:
                us += hld.bit.range_sum(hld.tin[hld.head[u]], hld.tin[u]+1)
                u = hld.up[u]

        if hld.depth[u] < hld.depth[v]:
            return us+hld.bit.range_sum(hld.tin[u]+hld.edge_queries, hld.tin[v]+1)+uv
        else:
            return us+hld.bit.range_sum(hld.tin[v]+hld.edge_queries, hld.tin[u]+1)+uv

from cp_library.ds.tree.bit.bit_cls import BIT