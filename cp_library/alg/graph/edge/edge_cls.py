import cp_library.alg.graph.__header__
from cp_library.io.parser_cls import Parsable, TokenStream

class Edge(tuple, Parsable):
    @classmethod
    def compile(cls, I=-1):
        def parse(ts: TokenStream):
            u,v = ts.line()
            return cls((int(u)+I,int(v)+I))
        return parse