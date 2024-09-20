import cp_library.alg.__init__

from typing import TypeVar
from cp_library.io.parser_cls import Parsable, Parser, TokenStream
from cp_library.alg.graph.edge_cls import Edge

E = TypeVar('E', bound=Edge)
M = TypeVar('M', bound=int)

class EdgeCollection(Parsable):
    @classmethod
    def compile(cls, M: M, E: E = Edge[-1]):
        if isinstance(I := E, int):
            E = Edge[I]
        edge = Parser.compile(E)
        def parse(ts: TokenStream):
            return cls(edge(ts) for _ in range(M))
        return parse

class EdgeList(EdgeCollection, list[E]):
    pass

class EdgeSet(EdgeCollection, set[E]):
    pass
