import cp_library.alg.dp.__header__
from math import isqrt
from cp_library.io.parser_cls import Parsable, Parser, TokenStream
from typing import Iterable

class Mo(list, Parsable):
    """
    Mo[Q: int, N: int, T: type = tuple[int, int]]
    """
    def __init__(self, queries: Iterable[tuple[int, int]], N: int):
        # Initialize with original queries and their indices
        B = isqrt(N)
        queries = [
            (b, -r, i, l, r) if (b := l//B) & 2 else (b, r, i, l, r)
            for i, (l, r) in enumerate(queries)
        ]
        self.Q = len(queries)
        self.queries = queries

    def add(self, i):
        pass

    def remove(self, i):
        pass

    def answer(self, i, l, r):
        pass
    
    def solve(self):
        self.queries.sort()

        curr_l = curr_r = 0
        ans = [0]*self.Q
        
        for _, _, qid, l, r in self.queries:
            if r > curr_r:
                for i in range(curr_r, r):
                    self.add(i)

            if l < curr_l:
                for i in range(curr_l-1, l-1, -1):
                    self.add(i)

            if l > curr_l:
                for i in range(curr_l, l):
                    self.remove(i)

            if r < curr_r:
                for i in range(curr_r-1, r-1, -1):
                    self.remove(i)
            ans[qid] = self.answer(qid, l, r)
            
            curr_l, curr_r = l, r
        return ans


    @classmethod
    def compile(cls, Q: int, N: int, T: type = tuple[-1, int]):
        query = Parser.compile(T)
        def parse(ts: TokenStream):
            return cls((query(ts) for _ in range(Q)), N)
        return parse

