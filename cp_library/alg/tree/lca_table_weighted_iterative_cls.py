import cp_library.alg.tree.__header__
from cp_library.alg.iter.presum_fn import presum
from cp_library.alg.tree.lca_table_iterative_cls import LCATable

class LCATableWeighted(LCATable):
    def __init__(self, T, root = 0):
        super().__init__(T, root)
        self.weights = T.Wdelta
        self.weighted_depth = None

    def distance(self, u, v) -> int:
        if self.weighted_depth is None:
            self.weighted_depth = presum(self.weights)
        l, r, a, _ = self._query(u, v)
        m = self.start[a]
        return self.weighted_depth[l] + self.weighted_depth[r] - 2*self.weighted_depth[m]