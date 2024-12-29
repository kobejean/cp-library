import cp_library.ds.__header__
from typing import Union
from cp_library.io.parser_cls import Parsable, Parser, TokenStream

class Parallel(tuple, Parsable):
    def __new__(cls, N, K=2):
        return super().__new__(cls, ([0]*N for _ in range(K)))

    @classmethod
    def compile(cls, N: int, K: int = 2, T: Union[type,int] = int):
        if T is int:
            def parse(ts: TokenStream):
                P = cls(N, K)
                for i in range(N):
                    for k,val in enumerate(map(T, ts.line())):
                        P[k][i] = val
                return P
        elif isinstance(shift := T, int):
            def parse(ts: TokenStream):
                P = cls(N, K)
                for i in range(N):
                    for k,val in enumerate(map(int, ts.line())):
                        P[k][i] = val+shift
                return P
        else:
            row = Parser.compile(T)
            def parse(ts: TokenStream):
                P = cls(N, K)
                for i in range(N):
                    for k, val in enumerate(row(ts)):
                        P[k][i] = val
                return P
        return parse
