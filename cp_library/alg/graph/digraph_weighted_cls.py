import cp_library.alg.__header__

from cp_library.alg.graph.edge_weighted_cls import EdgeWeighted
from cp_library.alg.graph.graph_proto import GraphProtocol

from typing import Iterable
from operator import itemgetter

class DiGraphWeighted(GraphProtocol):
    def __init__(G, N, E: list = []):
        super().__init__([] for _ in range(N))
        G.E = list(E)
        for u,v,*w in G.E:
            G[u].append((v,*w))
    
    def neighbors(G, v: int) -> Iterable[int]:
        return map(itemgetter(0), G[v])
    
    @classmethod
    def compile(cls, N: int, M: int, E: type|int = EdgeWeighted[-1]):
        if isinstance(E, int): E = EdgeWeighted[E]
        return super().compile(N, M, E)