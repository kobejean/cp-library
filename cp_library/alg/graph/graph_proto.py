import cp_library.alg.graph.__header__
from typing import Iterable
from cp_library.io.parser_cls import Parsable, Parser, TokenStream

class GraphProtocol(list, Parsable):

    def neighbors(G, v: int) -> Iterable[int]:
        return G[v]

    @classmethod
    def compile(cls, N: int, M: int, E):
        edge = Parser.compile(E)
        def parse(ts: TokenStream):
            return cls(N, (edge(ts) for _ in range(M)))
        return parse