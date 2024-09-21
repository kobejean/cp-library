import cp_library.alg.__header__

from typing import TypeVar
from cp_library.io.parser_cls import Parsable, Parser, TokenStream
from cp_library.alg.graph.edge_cls import Edge, H


N = TypeVar('N', bound=int)
E = TypeVar('N', bound=Edge)
class DiGraph(list[H], Parsable):
    def __init__(G, N: N, edges: list[E]=[]):
        super().__header__([] for _ in range(N))
        for edge in edges:
            G[edge.u].append(edge.forw)

    @classmethod
    def compile(cls, N: int, M: int, E: E|int = Edge[-1]):
        if isinstance(E, int):
            E = Edge[E]
        edge = Parser.compile(E)
        def parse(ts: TokenStream):
            return cls(N, (edge(ts) for _ in range(M)))
        return parse