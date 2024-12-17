import cp_library.ds.__header__
from math import prod
from typing import Container, Iterable
from cp_library.io.parser_cls import Parsable, Parser, TokenStream

class grid2d(Parsable, Container):

    def __init__(self, shape: tuple[int, int], data = 0):
        self.shape = shape
        self.size = prod(shape)
        if isinstance(data, Iterable) and not isinstance(data, str):
            self.data = list(elm for row in data for elm in row)
        else:
            self.data = [data] * (self.size)
    
    @classmethod
    def compile(cls, shape: tuple[int, int], T: type = int):
        elm = Parser.compile(T)
        def parse(ts: TokenStream):
            obj = cls.__new__(cls)
            obj.shape = shape
            obj.size = prod(shape)
            obj.data = list(elm(ts) for _ in range(obj.size))
            return obj
        return parse
    
    def __contains__(self, x: object) -> bool:
        return x in self.data
    
    def __getitem__(self, key: tuple[int, int]):
        i, j = key
        return self.data[i * self.shape[1] + j]
    
    def __setitem__(self, key: tuple[int, int], value):
        i, j = key
        self.data[i * self.shape[1] + j] = value
    
    def __repr__(self) -> str:
        (N, M), data = self.shape, self.data
        return '\n'.join(' '.join(str(data[j]) for j in range(i,i+M)) for i in range(0,N*M,M))
