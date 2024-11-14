from enum import IntEnum, auto
from itertools import chain, groupby
import cp_library.alg.graph.__header__
from cp_library.io.parser_cls import Parsable, Parser, TokenStream
from typing import Iterable, Sequence

class Queries(list, Parsable):
    def __init__(self, data: Iterable = []):
        super().__init__((i,*query) for i,query in enumerate(data))

    def append(self, query) -> None:
        return super().append((len(self), *query))

    @classmethod
    def compile(cls, N: int, T: type = tuple[int, int]):
        query = Parser.compile(T)
        def parse(ts: TokenStream):
            return cls(query(ts) for _ in range(N))
        return parse

class QueriesGrouped(Queries):
    '''QueriesGrouped[Q: int, key = 0, T: type = tuple[int, ...]]'''
    def __init__(self, queries, key = 0):
        if isinstance(key, int):
            group_idx = key+1
            def wrap_key(row):
                return row[group_idx]
        else:
            def wrap_key(row):
                _, *query = row
                return key(query)
        rows = list((i,*query) for i,query in enumerate(queries))
        groups = [(k, list(g)) for k, g in groupby(rows, key = wrap_key)]
        groups.sort()
        self.key = key
        
        list.__init__(self, groups)
            

    @classmethod
    def compile(cls, Q: int, key = 0, T: type = tuple[int, ...]):
        query = Parser.compile(T)
        def parse(ts: TokenStream):
            return cls((query(ts) for _ in range(Q)), key)
        return parse

class QueriesRange(Queries):
    '''QueriesRange[Q: int, N: int, key = 0, T: type = tuple[-1, int]]'''
    def __init__(self, queries, N: int, key = 0):
        if isinstance(key, int):
            group_idx = key+1
            def wrap_key(row):
                return row[group_idx]
        else:
            def wrap_key(row):
                _, *query = row
                return key(query)
        rows = list((i,*query) for i,query in enumerate(queries))
        
        groups = [(k,[]) for k in range(N)]
        for k, group in groupby(rows, key = wrap_key):
            groups[k][1].extend(group)
        self.key = key
        
        list.__init__(self, groups)

    @classmethod
    def compile(cls, Q: int, N: int, key = 0, T: type = tuple[-1, int]):
        query = Parser.compile(T)
        def parse(ts: TokenStream):
            return cls((query(ts) for _ in range(Q)), N, key)
        return parse

from enum import IntEnum, auto

class MoOp(IntEnum):
    ADD_LEFT = auto()
    ADD_RIGHT = auto()
    REMOVE_LEFT = auto()
    REMOVE_RIGHT = auto()
    ANSWER = auto()
    
from math import isqrt
from typing import Iterable

from cp_library.ds.elist_fn import elist

class QueriesMoOps(list[tuple],Parsable):
    """
    QueriesMoOps[Q: int, N: int, T: type = tuple[int, int]]
    Orders queries using Mo's algorithm and generates a sequence of operations to process them efficiently.
    Each operation is either moving pointers or answering a query.
    
    Uses half-interval convention: [left, right)
    Block size is automatically set to sqrt(N) for optimal complexity.
    """
    
    def encode(self, i, l, r):
        return (((r << self.nbits) + l) << self.qbits) + i
    
    def decode(self, bits):
        r = bits >> self.qbits >> self.nbits
        l = bits >> self.qbits & self.nmask
        i = bits & self.qmask
        return i, l, r

    def __init__(self, queries: list[tuple[int, int]], N: int):
        Q = len(queries)
        self.qbits = Q.bit_length()
        self.nbits = N.bit_length()
        self.qmask = (1 << self.qbits)-1
        self.nmask = (1 << self.nbits)-1

        # Initialize with original queries and their indices
        B = isqrt(N)
        K = (N+B-1)//B
        buckets = [elist(64) for _ in range(K)]
        for i, (l, r) in enumerate(queries):
            buckets[l//B].append(self.encode(i, l, r))
        for i, bucket in enumerate(buckets):
            bucket.sort(reverse=i&1)
        
        
        # Generate sequence of operations
        ops = elist(3*Q)

        nl = nr = 0
        
        for bucket in buckets:
            for code in bucket:
                i, l, r = self.decode(code)
                if l < nl:
                    ops.append((MoOp.ADD_LEFT, nl-1, l-1, -1))
                elif l > nl:
                    ops.append((MoOp.REMOVE_LEFT, nl, l, 1))

                if r > nr:
                    ops.append((MoOp.ADD_RIGHT, nr, r, 1))
                elif r < nr:
                    ops.append((MoOp.REMOVE_RIGHT, nr-1, r-1, -1))
                
                ops.append((MoOp.ANSWER, i, l, r))
                
                nl, nr = l, r
        super().__init__(ops)
        self.queries = queries


    @classmethod
    def compile(cls, Q: int, N: int, T: type = tuple[-1, int]):
        query = Parser.compile(T)
        def parse(ts: TokenStream):
            return cls([query(ts) for _ in range(Q)], N)
        return parse
