import cp_library.alg.tree.__header__

from cp_library.alg.graph.edge_cls import Edge
from cp_library.alg.graph.graph_cls import Graph

class Tree(Graph):
    @classmethod
    def compile(cls, N: int, E: type[Edge]|int = Edge[-1]):
        return super().compile(N, N-1, E)