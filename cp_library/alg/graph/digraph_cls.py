import cp_library.alg.__header__

from cp_library.alg.graph.edge_cls import Edge
from cp_library.alg.graph.graph_proto import GraphProtocol

class DiGraph(GraphProtocol):
    def __init__(G, N: int, E=[]):
        super().__init__([] for _ in range(N))
        G.E = list(E)
        for u,v in G.E:
            G[u].append(v)

    @classmethod
    def compile(cls, N: int, M: int, E: type|int = Edge[-1]):
        if isinstance(E, int): E = Edge[E]
        return super().compile(N, M, E)