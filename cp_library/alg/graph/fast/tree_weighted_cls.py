import cp_library.alg.graph.fast.__header__
from cp_library.alg.graph.fast.graph_weighted_cls import GraphWeighted
from cp_library.alg.graph.fast.tree_weighted_base_cls import TreeWeightedBase

class TreeWeighted(GraphWeighted, TreeWeightedBase):
    pass

from cp_library.ds.fill_fn import fill_u32
