import cp_library.__header__
import cp_library.alg.__header__
from cp_library.alg.graph.fast.graph_weighted_meta_cls import GraphWeightedMeta

import cp_library.alg.tree.__header__
import cp_library.alg.tree.fast.__header__
from cp_library.alg.tree.fast.tree_weighted_base_cls import TreeWeightedBase

class TreeWeightedMeta(TreeWeightedBase, GraphWeightedMeta):
    @classmethod
    def compile(cls, N: int, D = 2, T: list[type] = [-1,-1,int,int]):
        return GraphWeightedMeta.compile.__func__(cls, N, N-1, D, T)

