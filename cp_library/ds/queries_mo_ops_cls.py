import cp_library.ds.__header__
from cp_library.io.parser_cls import Parsable, Parser, IOBase
from cp_library.ds.elist_fn import elist

from enum import IntFlag, auto
from math import isqrt

class MoOp(IntFlag):
    ADD_LEFT = auto()
    ADD_RIGHT = auto()
    REMOVE_LEFT = auto()
    REMOVE_RIGHT = auto()
    ANSWER = auto()
    
    ADD = ADD_LEFT | ADD_RIGHT
    REMOVE = REMOVE_LEFT | REMOVE_RIGHT

# def hilbert(x: int, y: int, n: int) -> int:
#     '''Convert (x,y) to Hilbert curve distance for given n (power of 2).'''
#     d = 0
#     for s in range(n.bit_length() - 1, -1, -1):
#         rx = (x >> s) & 1
#         ry = (y >> s) & 1
#         d += n * n * ((3 * rx) ^ ry) >> 2
#         if ry == 0:
#             if rx == 1:
#                 x = n-1 - x
#                 y = n-1 - y
#             x, y = y, x
#     return d

class QueriesMoOps(tuple[list[int], ...],Parsable):
    '''
    QueriesMoOps[Q: int, N: int, T: type = tuple[int, int]]
    Orders queries using Mo's algorithm and generates a sequence of operations to process them efficiently.
    Each operation is either moving pointers or answering a query.
    
    Uses half-interval convention: [left, right)
    '''
    
    def __new__(cls, L: list[int], R: list[int], N: int, B: int = None):
        Q = len(L)
        qbits = Q.bit_length()
        nbits = (N+1).bit_length()
        qmask = qmask = (1 << qbits)-1
        nmask = (1 << nbits)-1
        B = max(1,N//isqrt(max(1,Q)) )if B is None else B
        order = [0]*Q
        for i in range(Q):
            l, r = L[i], R[i]
            b = l//B
            r = nmask - r if b & 1 else r
            order[i] = (((b << nbits) + r) << qbits) + i
        # n = 1 << nbits
        # for i in range(Q):
        #     l, r = L[i], R[i]
        #     # Use Hilbert curve mapping for the 2D point (l,r)
        #     h = hilbert(l, r, n)
        #     order[i] = (h << qbits) + i
        order.sort()
        
        ops = elist(3*Q)
        A1 = elist(3*Q)
        A2 = elist(3*Q)
        A3 = elist(3*Q)

        nl = nr = 0
        
        for i in order:
            i &= qmask
            l, r = L[i], R[i]
            if l < nl:
                ops.append(MoOp.ADD_LEFT)
                A1.append(nl-1)
                A2.append(l-1)
                A3.append(-1)
                
            elif l > nl:
                ops.append(MoOp.REMOVE_LEFT)
                A1.append(nl)
                A2.append(l)
                A3.append(1)
                
            if r > nr:
                ops.append(MoOp.ADD_RIGHT)
                A1.append(nr)
                A2.append(r)
                A3.append(1)
                
            elif r < nr:
                ops.append(MoOp.REMOVE_RIGHT)
                A1.append(nr-1)
                A2.append(r-1)
                A3.append(-1)
                
            ops.append(MoOp.ANSWER)
            A1.append(i)
            A2.append(l)
            A3.append(r)
            
            nl, nr = l, r
        return super().__new__(cls, (ops, A1, A2, A3))

    @classmethod
    def compile(cls, Q: int, N: int, T: type = tuple[-1, int], B: int = None):
        if T == tuple[-1, int]:
            query = Parser.compile(T)
            def parse(io: IOBase):
                L, R = [0]*Q, [0]*Q
                for i in range(Q):
                    L[i], R[i] = io.readints()
                    L[i] -= 1
                return cls(L, R, N, B)
            return parse
        else:
            query = Parser.compile(T)
            def parse(io: IOBase):
                L, R = [0]*Q, [0]*Q
                for i in range(Q):
                    L[i], R[i] = query(io)
                return cls(L, R, N, B)
            return parse
