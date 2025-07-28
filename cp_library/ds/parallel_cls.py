import cp_library.__header__
import typing
from typing import Union
from cp_library.io.parsable_cls import Parsable
import cp_library.ds.__header__

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
        def parse(io: IOBase):
            P = cls(N, K)
            for i in range(N):
                for k, parse in enumerate(row):
                    P[k][i] = parse(io)
            return P
        return parse
from cp_library.io.parser_cls import Parser
from cp_library.io.io_base_cls import IOBase