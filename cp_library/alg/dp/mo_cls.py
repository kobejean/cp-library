import cp_library.__header__
from math import isqrt
import cp_library.alg.__header__
import cp_library.alg.dp.__header__
from cp_library.alg.dp.max2_fn import max2
from cp_library.io.parser_cls import Parsable, Parser, TokenStream

class Mo(Parsable):
    '''Mo[Q: int, N: int, T: type = tuple[int, int]]'''
    def __init__(mo, L: list[int], R: list[int], N: int):
        mo.Q = len(L)
        mo.qbits = mo.Q.bit_length()
        mo.nbits = N.bit_length()
        mo.qmask = (1 << mo.qbits) - 1
        mo.nmask = (1 << mo.nbits) - 1
        mo.B = max2(1,N//isqrt(max2(1,mo.Q)))
        mo.order = [mo.packet(i, L[i], R[i]) for i in range(mo.Q)]
        mo.order.sort()
        mo.L = [0]*mo.Q
        mo.R = [0]*mo.Q
        for i,j in enumerate(mo.order):
            j &= mo.qmask
            mo.order[i] = j
            mo.L[i] = L[j]
            mo.R[i] = R[j]

    def packet(mo, i: int, l: int, r: int) -> int:
        b = l//mo.B
        if b & 1: r = mo.nmask - r
        return (b << mo.nbits | r) << mo.qbits | i

    def add(mo, i: int):
        '''Add element at index i to current range.'''
        pass

    def remove(mo, i: int):
        '''Remove element at index i from current range.'''
        pass

    def answer(mo, i: int, l: int, r: int) -> int:
        '''Compute answer for current range.'''
        pass
    
    def solve(mo) -> list[int]:
        ans = [0]*mo.Q; l = r = 0
        for i in range(mo.Q):
            qid, nl, nr = mo.order[i], mo.L[i], mo.R[i]
            while r < nr: mo.add(r); r += 1
            while nl < l: mo.add(l:=l-1)
            while l < nl: mo.remove(l); l += 1
            while nr < r: mo.remove(r:=r-1)
            ans[qid] = mo.answer(qid, l, r)
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