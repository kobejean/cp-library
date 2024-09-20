
from typing import TypeAlias
from cp_library.io.parser_cls import Parsable, TokenStream
from cp_library.alg.graph.edge_cls import Edge

class EdgeWeighted(Edge, Parsable):
    H: TypeAlias = tuple[int,int]
    @property
    def w(self): return self[0]
    @property
    def u(self): return self[1]
    @property
    def v(self): return self[2]
    @property
    def forw(self) -> H: return self[0], self[2]
    @property
    def back(self) -> H: return self[0], self[1]
    @classmethod
    def compile(cls, I=1):
        def parse(ts: TokenStream):
            u,v,w = map(int,ts.line())
            return cls((w,u-I,v-I))
        return parse