import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.tree.__header__
import cp_library.alg.tree.csr.__header__
from cp_library.alg.tree.csr.hld_cls import HLD
from cp_library.alg.tree.csr.tree_weighted_base_cls import TreeWeightedBase

class HLDWeighted(HLD):
    def __init__(hld, T: TreeWeightedBase, r=0):
        super().__init__(T, r)
        hld.weights = [T.Wa[i] if (i := hld.back[u]) >= 0 else 0 for u in hld.order]