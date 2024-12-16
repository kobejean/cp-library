import sys
import cp_library.alg.graph.__header__

from cp_library.io.parser_cls import TokenStream
from cp_library.alg.graph.fast.grid_graph_base_cls import GridGraphBase

class GridGraphWalledBase(GridGraphBase):

    def __init__(G, H, W, M, S, U, V, deg, La, Ra, Ua, Va, Ea,
            dirs: list = [(-1,0),(0,1),(1,0),(0,-1)], wall = '#'):
        super().__init__(H, W, M, S, U, V, deg, La, Ra, Ua, Va, Ea, dirs)
        G.wall = wall

    def is_valid(G, i, j, v):
        return super().is_valid(i, j, v) and G.S[v] != G.wall
    
    @classmethod
    def compile(cls, H: int, W: int, *args):
        def parse(ts: TokenStream):
            S = ''.join(ts.stream.readline().rstrip() for _ in range(H))
            return cls(H, W, S, *args)
        return parse
