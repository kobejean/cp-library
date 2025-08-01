import cp_library.__header__
from cp_library.io.parsable_cls import Parsable
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__

class EdgeList(tuple, Parsable):
    def __new__(cls, M): return super().__new__(cls, ([0]*M, [0]*M))
    @classmethod
    def compile(cls, N: int, shift: int = -1):
        def parse(io: IOBase):
            U, V = P = cls(N)
            for i in range(N): u, v = io.readints(); U[i], V[i] = u+shift, v+shift
            return P
        return parse
from cp_library.io.io_base_cls import IOBase