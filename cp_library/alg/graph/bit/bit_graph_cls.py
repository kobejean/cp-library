import cp_library.__header__
from typing import Union
from cp_library.io.parser_cls import Parsable, Parser, TokenStream
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.bit.__header__
from cp_library.alg.graph.edge.edge_cls import Edge

class BitGraph(list, Parsable):
    def __init__(G, N: int, E: list['Edge']=[]):
        super().__init__([0]*N)
        G.E, G.N, G.M = E, N, len(E)
        for u,v in E:
            G[u] |= 1 << v
            G[v] |= 1 << u

    def to_complement(G):
        full = (1 << G.N) - 1
        for u in range(G.N):
            G[u] = full ^ G[u]

    def chromatic_number(G):
        Z = 1 << (N := len(G))
        I, coef = [0]*Z, [1]*Z
        I[0] = 1
        for S in range(1, Z):
            T = 1 << (v := ctz32(S)) ^ S
            I[S] = I[T] + I[T & ~G[v]]
            coef[S] = -1 if popcnt32(S) & 1 else 1
        for k in range(1, N):
            Pk = 0
            for S in range(Z):
                coef[S] *= I[S]
                Pk += coef[S]
            if Pk != 0: return k
        return N

    @classmethod
    def compile(cls, N: int, M: int, E: Union[type,int] = Edge[-1]):
        if isinstance(E, int): E = Edge[E]
        edge = Parser.compile(E)
        def parse(ts: TokenStream):
            return cls(N, [edge(ts) for _ in range(M)])
        return parse
from cp_library.bit.popcnt32_fn import popcnt32
from cp_library.bit.ctz32_fn import ctz32