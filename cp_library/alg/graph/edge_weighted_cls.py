import cp_library.alg.graph.__header__

from cp_library.io.parser_cls import TokenStream
from cp_library.alg.graph.edge_cls import Edge

from functools import total_ordering 

@total_ordering
class EdgeWeighted(Edge):
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