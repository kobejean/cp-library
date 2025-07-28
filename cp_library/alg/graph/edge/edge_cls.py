import cp_library.alg.graph.__header__
from cp_library.io.parser_cls import Parsable, IOBase

class Edge(tuple, Parsable):
    @classmethod
    def compile(cls, I=-1):
        def parse(io: IOBase):
            u, v = io.readints()
            return cls((u+I,v+I))
        return parse