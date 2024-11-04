import cp_library.alg.dp.__header__
from typing import TypeVar, Generic
from dataclasses import dataclass
from math import inf

T = TypeVar('T')

@dataclass
class Transition2D(Generic[T]):
    di: int
    dj: int
    
    def __call__(self, i: int, j: int, src_val: T, dest_val: T) -> T:
        """Override this to implement transition logic"""
        return src_val  # Default no-op

class DynamicProgramming2D(Generic[T]):
    def __init__(self, rows: int, cols: int, default: T = inf):
        self.rows = rows
        self.cols = cols
        self.table = [[default] * cols for _ in range(rows)]
    
    def __getitem__(self, pos: tuple[int, int]) -> T:
        i, j = pos
        return self.table[i][j]
    
    def __setitem__(self, pos: tuple[int, int], value: T) -> None:
        i, j = pos
        self.table[i][j] = value
    
    def solve(self, transitions: list[Transition2D[T]]) -> None:
        for i in range(self.rows):
            for j in range(self.cols):
                curr_val = self.table[i][j]
                for trans in transitions:
                    ni, nj = i + trans.di, j + trans.dj
                    if 0 <= ni < self.rows and 0 <= nj < self.cols:
                        self.table[ni][nj] = trans(i, j, curr_val, self.table[ni][nj])
