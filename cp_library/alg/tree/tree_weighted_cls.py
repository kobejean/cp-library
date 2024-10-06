import cp_library.alg.tree.__header__

from cp_library.alg.graph.edge_weighted_cls import EdgeWeighted
from cp_library.alg.graph.graph_weighted_cls import GraphWeighted

class TreeWeighted(GraphWeighted):
    @classmethod
    def compile(cls, N: int, E: type|int = EdgeWeighted[-1]):
        return super().compile(N, N-1, E)