import cp_library.__header__
from cp_library.io.parsable_cls import Parsable
import cp_library.alg.__header__
import cp_library.alg.graph.__header__

class Edge(tuple, Parsable):
    @classmethod
    def compile(cls, I=-1):
        def parse(io: IOBase): u, v = io.readints(); return cls((u+I,v+I))
        return parse
from cp_library.io.io_base_cls import IOBase