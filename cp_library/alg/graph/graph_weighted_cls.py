import cp_library.alg.graph.__header__

from cp_library.alg.graph.edge_weighted_cls import EdgeWeighted
from cp_library.alg.graph.graph_cls import Graph

class GraphWeighted(Graph):
    @classmethod
    def compile(cls, N: int, M: int, E: EdgeWeighted|int = EdgeWeighted[-1]):
        if isinstance(E, int): E = EdgeWeighted[E]
        return super().compile(N, M, E)