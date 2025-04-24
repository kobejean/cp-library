import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.fast.__header__
from cp_library.io.parser_cls import Parsable, TokenStream

class EdgeList(tuple, Parsable):
    def __new__(cls, M):
        return super().__new__(cls, ([0]*M, [0]*M))

    @classmethod
    def compile(cls, N: int, shift: int = -1):
        def parse(ts: TokenStream):
            U, V = P = cls(N)
            for i in range(N):
                u, v = ts.line()
                U[i], V[i] = int(u)+shift, int(v)+shift
            return P
        return parse
