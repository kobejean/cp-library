import cp_library.__header__
from typing import Sequence
import cp_library.alg.__header__
import cp_library.alg.tree.__header__

class HLD(Sequence[int]):
    def __init__(self, T, r=0):
        N = len(T)
        T.hld_precomp(r)
        self.N, self.T, self.size, self.depth = N, T, T.size, T.depth
        self.order, self.start, self.end = T.order, T.tin, T.tout
        self.par, self.heavy, self.head = T.par, T.heavy, T.head

    def __getitem__(self, key):
        return self.start[key]
    
    def __len__(self):
        return len(self.start)
    
    def __contains__(self, value):
        return self.start.__contains__(value)
    
    def subtree_range(self, v):
        return self.start[v], self.end[v]

    def path(self, u, v, query_fn, edge=False):
        head, depth, par, start = self.head, self.depth, self.par, self.start
        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u,v = v,u
            query_fn(start[head[u]], start[u]+1)
            u = par[head[u]]

        if depth[u] < depth[v]:
            u,v = v,u
        query_fn(start[v]+edge, start[u]+1)
