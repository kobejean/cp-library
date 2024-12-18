import sys
import cp_library.alg.graph.__header__

from cp_library.io.parser_cls import TokenStream
from cp_library.alg.graph.fast.graph_base_cls import GraphBase

class GridGraphBase(GraphBase):

    def __init__(G, H, W, M, S, U, V, deg, La, Ra, Ua, Va, Ea,
            dirs: list = [(-1,0),(0,1),(1,0),(0,-1)]):
        super().__init__(H*W, M, U, V, deg, La, Ra, Ua, Va, Ea)
        G.W = W
        G.H = H
        G.S = S
        G.dirs = dirs

    def vertex(G, key: tuple[int,int] | int):
        if isinstance(key, tuple):
            i,j = key
            return i*G.W+j
        else:
            return key

    def is_valid(G, i, j, v):
        return 0 <= i < G.H and 0 <= j < G.W
    
    @classmethod
    def compile(cls, H: int, W: int, *args):
        def parse(ts: TokenStream):
            S = ''.join(ts.stream.readline().rstrip() for _ in range(H))
            return cls(H, W, S, *args)
        return parse
