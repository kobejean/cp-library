import cp_library.ds.__header__
from cp_library.io.parser_cls import Parsable, TokenStream

class ParallelRange(tuple, Parsable):
    def __new__(cls, N):
        return super().__new__(cls, ([0]*N, [0]*N))

    @classmethod
    def compile(cls, N: int):
        def parse(ts: TokenStream):
            L, R = P = cls(N)
            for i in range(N):
                l, r = ts.line()
                L[i], R[i] = int(l)-1, int(r)
            return P
        return parse
