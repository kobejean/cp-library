import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.tree.__header__
from cp_library.alg.dp.sort2_fn import sort2
from cp_library.alg.iter.presum_fn import presum
from cp_library.ds.min_sparse_table_cls import MinSparseTable

class LCATable(MinSparseTable):
    def __init__(lca, T, root = 0):
        N = len(T)
        T.euler_tour(root)
        lca.depth = depth = presum(T.delta)
        lca.tin, lca.tout = T.tin[:], T.tout[:]
        lca.mask = (1 << (shift := N.bit_length()))-1
        lca.shift = shift
        order = T.order
        M = len(order)
        packets = [0]*M
        for i in range(M):
            packets[i] = depth[i] << shift | order[i] 
        super().__init__(packets)

    def _query(lca, u, v):
        tin = lca.tin
        l, r = sort2(tin[u], tin[v]); r += 1
        da = super().query(l, r)
        return l, r, da & lca.mask, da >> lca.shift

    def query(lca, u, v) -> tuple[int,int]:
        l, r, a, d = lca._query(u, v)
        return a, d
    
    def distance(lca, u, v) -> int:
        l, r, a, d = lca._query(u, v)
        return lca.depth[l] + lca.depth[r-1] - 2*d
    
    def path(lca, u, v):
        path, par, lca, c = [], lca.T.par, lca.query(u, v)[0], u
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