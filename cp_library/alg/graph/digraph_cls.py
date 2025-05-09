import cp_library.alg.graph.__header__
from typing import Union
from cp_library.alg.graph.edge_cls import Edge
from cp_library.alg.graph.graph_proto import GraphProtocol

class DiGraph(GraphProtocol):
    def __init__(G, N: int, E: list[Edge]=[]):
        super().__init__(N, E, ([] for _ in range(N)))
        for u,v in G.E:
            G[u].append(v)

    def edge_ids(G) -> list[list[int]]:
        Eid = [[] for _ in range(G.N)]
        for e,(u,v) in enumerate(G.E):
            Eid[u].append(e)
        return Eid
    
    @classmethod
    def compile(cls, N: int, M: int, E: Union[type,int] = Edge[-1]):
        if isinstance(E, int): E = Edge[E]
        return super().compile(N, M, E)