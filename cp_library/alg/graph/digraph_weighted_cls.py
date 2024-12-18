import cp_library.alg.__header__

from cp_library.alg.graph.edge_weighted_cls import EdgeWeighted
from cp_library.alg.graph.graph_weighted_proto import GraphWeightedProtocol

from typing import Iterable, Union
from operator import itemgetter

class DiGraphWeighted(GraphWeightedProtocol):
    def __init__(G, N, E: list = []):
        super().__init__(N, E, ([] for _ in range(N)))
        for u,v,*w in G.E:
            G[u].append((v,*w))
    
    def edge_ids(G) -> list[list[int]]:
        Eid = [[] for _ in range(G.N)]
        for e,(u,v,*w) in enumerate(G.E):
            Eid[u].append(e)
        return Eid
    
    def neighbors(G, v: int) -> Iterable[int]:
        return map(itemgetter(0), G[v])
    
    @classmethod
    def compile(cls, N: int, M: int, E: Union[type,int] = EdgeWeighted[-1]):
        if isinstance(E, int): E = EdgeWeighted[E]
        return super().compile(N, M, E)
