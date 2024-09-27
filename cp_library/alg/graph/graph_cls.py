import cp_library.alg.graph.__header__

from cp_library.io.parser_cls import Parsable, Parser, TokenStream
from cp_library.alg.graph.edge_cls import Edge, H

class Graph(list[H], Parsable):
    def __init__(G, N: int, edges=[]):
        super().__init__([] for _ in range(N))
        G.E = list(edges)
        for edge in G.E:
            G[edge.u].append(edge.forw)
            G[edge.v].append(edge.back)

    @classmethod
    def compile(cls, N: int, M: int, E = Edge[-1]):
        if isinstance(E, int): E = Edge[E]
        edge = Parser.compile(E)
        def parse(ts: TokenStream):
            return cls(N, (edge(ts) for _ in range(M)))
        return parse