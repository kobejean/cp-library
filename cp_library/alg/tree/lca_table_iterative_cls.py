import cp_library.alg.tree.__header__
from cp_library.alg.iter.presum_fn import presum
from cp_library.ds.min_sparse_table_cls import MinSparseTable

class LCATable(MinSparseTable):
    def __init__(self, T, root = 0):
        N = len(T)
        T.euler_tour(root)
        self.depth = depth = presum(T.delta)
        self.start, self.stop = T.tin, T.tout
        self.mask = (1 << (shift := N.bit_length()))-1
        self.shift = shift
        order = T.order
        M = len(order)
        packets = [0]*M
        for i in range(M):
            packets[i] = depth[i] << shift | order[i] 
        super().__init__(packets)

    def _query(self, u, v):
        start = self.start
        l,r = min(start[u], start[v]), max(start[u], start[v])+1
        da = super().query(l, r)
        return l, r, da & self.mask, da >> self.shift

    def query(self, u, v) -> tuple[int,int]:
        l, r, a, d = self._query(u, v)
        return a, d
    
    def distance(self, u, v) -> int:
        l, r, a, d = self._query(u, v)
        return self.depth[l] + self.depth[r] - 2*d
    
    def path(self, u, v):
        path, par, lca, c = [], self.T.par, self.query(u, v)[0], u
        while c != lca:
            path.append(c)
            c = par[c]
        path.append(lca)
        rev_path, c = [], v
        while c != lca:
            rev_path.append(c)
            c = par[c]
        path.extend(reversed(rev_path))
        return path