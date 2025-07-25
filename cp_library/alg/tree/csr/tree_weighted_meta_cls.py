import cp_library.__header__
import cp_library.alg.__header__
from cp_library.alg.graph.csr.graph_weighted_meta_cls import GraphWeightedMeta

import cp_library.alg.tree.__header__
import cp_library.alg.tree.csr.__header__
from cp_library.alg.tree.csr.tree_weighted_base_cls import TreeWeightedBase

class TreeWeightedMeta(TreeWeightedBase, GraphWeightedMeta):
    @classmethod
    def compile(cls, N: int, T: list[type] = [-1,-1,int,int]):
        return GraphWeightedMeta.compile.__func__(cls, N, N-1, T)

