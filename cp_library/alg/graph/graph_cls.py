import cp_library.alg.__init__

from cp_library.alg.graph.edge_list_type import EdgeList
from cp_library.io.parsable_cls import Parsable

class Graph(list, Parsable):
    def __init__(self, N, edges: EdgeList=[]):
        super().__init__(([] for _ in range(N)))
        for u,v in edges:
            self[u].append(v)
            self[v].append(u)

    @classmethod
    def parse(cls, parse_spec, N, M, I=-1):
        return cls(N, parse_spec(EdgeList[I,M]))
