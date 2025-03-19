import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.tree.__header__
from cp_library.alg.iter.presum_fn import presum
from cp_library.alg.tree.lca_table_iterative_cls import LCATable

class LCATableWeighted(LCATable):
    def __init__(lca, T, root = 0):
        super().__init__(T, root)
        lca.weights = T.Wdelta
        lca.weighted_depth = None

    def distance(lca, u, v) -> int:
        if lca.weighted_depth is None:
            lca.weighted_depth = presum(lca.weights)
        l, r, a, _ = lca._query(u, v)
        m = lca.tin[a]
        return lca.weighted_depth[l] + lca.weighted_depth[r-1] - 2*lca.weighted_depth[m]