import cp_library.alg.graph.__header__

from cp_library.alg.graph.edge_weighted_cls import EdgeWeighted
from cp_library.alg.graph.graph_weighted_proto import GraphWeightedProtocol

class GraphWeighted(GraphWeightedProtocol):
    def __init__(G, N: int, E=[]):
        super().__init__(N, E, ([] for _ in range(N)))
        G.E = E
        for u,v,*w in G.E:
            G[u].append((v,*w))
            G[v].append((u,*w))
    
    def edge_ids(G) -> list[list[int]]:
        Eid = [[] for _ in range(G.N)]
        for e,(u,v,*w) in enumerate(G.E):
            Eid[u].append(e)
            Eid[v].append(e)
        return Eid
    
    @classmethod
    def compile(cls, N: int, M: int, E: type|int = EdgeWeighted[-1]):
        if isinstance(E, int): E = EdgeWeighted[E]
        return super().compile(N, M, E)
