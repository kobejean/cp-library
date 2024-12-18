import cp_library.alg.graph.__header__
from typing import Union
from cp_library.alg.graph.edge_cls import Edge
from cp_library.alg.graph.graph_proto import GraphProtocol

class Graph(GraphProtocol):
    def __init__(G, N: int, edges=[]):
        super().__init__(set() for _ in range(N))
        G.E = list(edges)
        G.N, G.M = N, len(G.E)
        for u,v in G.E:
            G[u].add(v)
            G[v].add(u)

    @classmethod
    def compile(cls, N: int, M: int, E: Union[type,int] = Edge[-1]):
        if isinstance(E, int): E = Edge[E]
        return super().compile(N, M, E)