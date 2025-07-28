import cp_library.__header__
from cp_library.io.parsable_cls import Parsable
from itertools import groupby
from typing import Iterable
import cp_library.ds.__header__

class Queries(list, Parsable):
    def __init__(self, data: Iterable = []): super().__init__((i,*query) for i,query in enumerate(data))
    def append(self, query) -> None: return super().append((len(self), *query))
    @classmethod
    def compile(cls, N: int, T: type = tuple[int, int]):
        query = Parser.compile(T)
        def parse(io: IOBase): return cls(query(io) for _ in range(N))
        return parse

class QueriesGrouped(Queries):
    '''QueriesGrouped[Q: int, key = 0, T: type = tuple[int, ...]]'''
    def __init__(self, queries, key = 0):
        if isinstance(key, int):
            group_idx = key+1
            def wrap_key(row): return row[group_idx]
        else:
            def wrap_key(row): _, *query = row; return key(query)
        rows = sorted(((i,*query) for i,query in enumerate(queries)), key = wrap_key)
        groups = [(k, list(g)) for k, g in groupby(rows, key = wrap_key)]
        groups.sort()
        self.key = key
        list.__init__(self, groups)
    @classmethod
    def compile(cls, Q: int, key = 0, T: type = tuple[int, ...]):
        query = Parser.compile(T)
        def parse(io: IOBase): return cls((query(io) for _ in range(Q)), key)
        return parse

class QueriesRange(Queries):
    '''QueriesRange[Q: int, N: int, key = 0, T: type = tuple[-1, int]]'''
    def __init__(self, queries, N: int, key = 0):
        if isinstance(key, int):
            group_idx = key+1
            def wrap_key(row): return row[group_idx]
        else:
            def wrap_key(row): _, *query = row; return key(query)
        rows = list((i,*query) for i,query in enumerate(queries))
        groups = [(k,[]) for k in range(N)]
        for k, group in groupby(rows, key = wrap_key): groups[k][1].extend(group)
        self.key = key
        list.__init__(self, groups)
    @classmethod
    def compile(cls, Q: int, N: int, key = 0, T: type = tuple[-1, int]):
        query = Parser.compile(T)
        def parse(io: IOBase):
            return cls((query(io) for _ in range(Q)), N, key)
        return parse
from cp_library.io.io_base_cls import IOBase
from cp_library.io.parser_cls import Parser