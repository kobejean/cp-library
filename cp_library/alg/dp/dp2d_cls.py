import cp_library.__header__
import cp_library.alg.__header__
from typing import Generic, Container
from cp_library.io.parsable_cls import Parsable
from dataclasses import dataclass
from math import inf
import cp_library.alg.dp.__header__
from cp_library.misc.typing import _T

@dataclass
class Transition2D(Generic[_T]):
    di: int; dj: int
    
    def __call__(self, i: int, j: int, src: _T, dest: _T) -> _T:
        '''Override this to implement transition logic'''
        return src  # Default no-op
    
    @classmethod
    def make(cls, func):
        class Transition(cls):
            def __call__(self, i: int, j: int, src: _T, dest: _T) -> _T:
                return func(i,j,src,dest)
        return Transition

class DynamicProgramming2D(Generic[_T], Parsable, Container):
    def __init__(self, rows: int, cols: int, default: _T = inf):
        self.rows = rows
        self.cols = cols
        self.table = default if isinstance(default, list) else [[default] * cols for _ in range(rows)]
    
    def __getitem__(self, pos: tuple[int, int]) -> _T:
        i, j = pos
        return self.table[i][j]
    
    def __setitem__(self, pos: tuple[int, int], value: _T) -> None:
        i, j = pos
        self.table[i][j] = value

    def __contains__(self, x: object) -> bool:
        return any(x in row for row in self.table)
    
    def solve(self, transitions: list[Transition2D[_T]]) -> None:
        for i in range(self.rows):
            for j in range(self.cols):
                curr_val = self.table[i][j]
                for trans in transitions:
                    ni, nj = i + trans.di, j + trans.dj
                    if 0 <= ni < self.rows and 0 <= nj < self.cols:
                        self.table[ni][nj] = trans(i, j, curr_val, self.table[ni][nj])
    
    @classmethod
    def compile(cls, N, M, T = int):
        table = Parser.compile(list[list[T,M],N])
        def parse(io: IOBase): return cls(N, M, table(io))
        return parse
from cp_library.io.parser_cls import Parser
from cp_library.io.io_base_cls import IOBase