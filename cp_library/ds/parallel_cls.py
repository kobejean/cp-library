import cp_library.ds.__header__
import typing
from typing import Union
from cp_library.io.parser_cls import Parsable, Parser, TokenStream

class Parallel(tuple, Parsable):
    def __new__(cls, N, K=2):
        return super().__new__(cls, ([0]*N for _ in range(K)))

    @classmethod
    def compile(cls, N: int, T: Union[type,list[type]] = tuple[int, int], K = -1):
        if K==-1:
            T = typing.get_args(T) or T
            K = len(row := [Parser.compile(t) for t in T])
        else:
            row = [Parser.compile(T)]*K
        def parse(ts: TokenStream):
            P = cls(N, K)
            for i in range(N):
                for k, parse in enumerate(row):
                    P[k][i] = parse(ts)
            return P
        return parse