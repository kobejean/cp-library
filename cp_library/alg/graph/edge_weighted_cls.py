import cp_library.alg.graph.__header__

from typing import TypeAlias
from cp_library.io.parser_cls import Parsable, TokenStream
from cp_library.alg.graph.edge_cls import Edge

class EdgeWeighted(Edge, Parsable):
    H: TypeAlias = tuple[int,int]
    @property
    def u(self): return self[0]
    @property
    def v(self): return self[1]
    @property
    def w(self): return self[2]
    @property
    def forw(self) -> H: return self[1], self[2]
    @property
    def back(self) -> H: return self[0], self[2]

    def __lt__(self, other: tuple) -> bool:
        a = self[2],self[0],self[1]
        b = other[2],other[0],other[1]
        return a < b
    
    @classmethod
    def compile(cls, I=-1):
        def parse(ts: TokenStream):
            u,v,w = ts.line()
            return cls((int(u)+I, int(v)+I, int(w)))
        return parse