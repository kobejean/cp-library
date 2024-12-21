import cp_library.alg.tree.__header__
from itertools import pairwise
from cp_library.alg.tree.lca_table_iterative_cls import LCATable
from cp_library.alg.iter.argsort_fn import argsort

class AuxiliaryTree(LCATable):

    def __init__(self, T, root=0):
        super().__init__(T, root)
        self.par = [-1]*T.N

    def bucketize(self, K, A):
        self.pre_all = pre_all = argsort(self.start)
        self.buckets = buckets = [[] for _ in range(K)]
        for u in pre_all:
            buckets[A[u]].append(u)
        return buckets

    def build_postorder(self, V, sort = False):
        if sort:
            V = sorted(V, key=self.start.__getitem__)
        L = len(V)
        post, stc, start, par = elist(L<<1), elist(L), self.start, self.par
        stc.append(V[0])
        par[V[0]] = -1
        for u, v in pairwise(V):
            lca, _ = self.query(u, v)
            if lca != u:
                last = stc.pop()
                while stc and start[top := stc[-1]] > start[lca]:
                    post.append(last)
                    par[last] = last = stc.pop()
                if not stc or top != lca:
                    stc.append(lca)
                    par[lca] = -1
                    
                post.append(last)
                par[last] = lca
            stc.append(v)
            par[v] = -1
        
        last = stc.pop()
        while stc:
            post.append(last)
            par[last] = last = stc.pop()
        post.append(last)
        return post, par

from cp_library.ds.elist_fn import elist

