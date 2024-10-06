import cp_library.alg.graph.__header__

from cp_library.alg.graph.edge_cls import Edge
from cp_library.alg.graph.graph_proto import GraphProtocol

class Graph(GraphProtocol):
    def __init__(G, N: int, edges=[]):
        super().__init__([] for _ in range(N))
        G.E = list(edges)
        for u,v in G.E:
            G[u].append(v)
            G[v].append(u)

    @classmethod
    def compile(cls, N: int, M: int, E: type|int = Edge[-1]):
        if isinstance(E, int): E = Edge[E]
        return super().compile(N, M, E)