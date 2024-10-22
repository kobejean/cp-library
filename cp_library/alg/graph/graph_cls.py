import cp_library.alg.graph.__header__

from cp_library.alg.graph.edge_cls import Edge
from cp_library.alg.graph.graph_proto import GraphProtocol

class Graph(GraphProtocol):
    def __init__(G, N: int, edges=[]):
        super().__init__([] for _ in range(N))
        G.E = list(edges)
        G.N, G.M = N, len(G.E)
        for u,v in G.E:
            G[u].append(v)
            G[v].append(u)

    def edge_ids(G) -> list[list[int]]:
        Eid = [[] for _ in range(G.N)]
        for e,(u,v) in enumerate(G.E):
            Eid[u].append(e)
            Eid[v].append(e)
        return Eid

    @classmethod
    def compile(cls, N: int, M: int, E: type|int = Edge[-1]):
        if isinstance(E, int): E = Edge[E]
        return super().compile(N, M, E)