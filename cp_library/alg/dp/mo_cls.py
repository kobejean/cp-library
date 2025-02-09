import cp_library.alg.dp.__header__
from math import isqrt
from cp_library.io.parser_cls import Parsable, Parser, TokenStream

class Mo(list, Parsable):
    """Mo[Q: int, N: int, T: type = tuple[int, int]]"""
    def __init__(self, L: list[int], R: list[int], N: int):
        self.Q = len(L)
        self.qbits = self.Q.bit_length()
        self.nbits = N.bit_length()
        self.qmask = (1 << self.qbits) - 1
        self.nmask = (1 << self.nbits) - 1
        
        self.B = isqrt(N)
        self.order = [self.packet(i, L[i], R[i]) for i in range(self.Q)]
        self.order.sort()
        self.L = [0]*self.Q
        self.R = [0]*self.Q
        for i,j in enumerate(self.order):
            j &= self.qmask
            self.order[i] = j
            self.L[i] = L[j]
            self.R[i] = R[j]

    def packet(self, i: int, l: int, r: int) -> int:
        """Pack query information into a single integer."""
        b = l//self.B
        if b & 1:
            return (((b << self.nbits) + self.nmask - r) << self.qbits) + i
        else:
            return (((b << self.nbits) + r) << self.qbits) + i

    def add(self, i: int):
        """Add element at index i to current range."""
        pass

    def remove(self, i: int):
        """Remove element at index i from current range."""
        pass

    def answer(self, i: int, l: int, r: int) -> int:
        """Compute answer for current range."""
        pass
    
    def solve(self) -> list[int]:
        curr_l = curr_r = 0
        ans = [0] * self.Q
        order, L, R = self.order, self.L, self.R
        
        for i in range(self.Q):
            qid, l, r = order[i], L[i], R[i]
            
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
            L, R = [0]*Q, [0]*Q
            for i in range(Q):
                L[i], R[i] = query(ts) 
            return cls(L, R, N)
        return parse