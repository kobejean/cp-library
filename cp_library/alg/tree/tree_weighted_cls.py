import cp_library.alg.tree.__header__
from typing import Union
from cp_library.alg.graph.edge_weighted_cls import EdgeWeighted
from cp_library.alg.graph.graph_weighted_cls import GraphWeighted
from cp_library.alg.tree.tree_weighted_proto import TreeWeightedProtocol

class TreeWeighted(TreeWeightedProtocol, GraphWeighted):
    @classmethod
    def compile(cls, N: int, E: Union[type,int] = EdgeWeighted[-1]):
        return GraphWeighted.compile.__func__(cls, N, N-1, E)