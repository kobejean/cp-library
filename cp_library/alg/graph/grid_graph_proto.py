import sys
import cp_library.alg.graph.__header__

from cp_library.io.parser_cls import TokenStream
from cp_library.alg.graph.graph_proto import GraphProtocol

class GridGraphProtocol(GraphProtocol):

    def __init__(G, H, W, S=str, dirs = [(-1,0),(0,1),(1,0),(0,-1)], wall = '#', adj = None):
        super().__init__(W*H, None, adj)
        G.W = W
        G.H = H
        G.S = S
        G.dirs = dirs
        G.wall = wall

    def vertex(G, key: tuple[int,int] | int):
        match key:
            case i, j: return i*G.W+j
            case v: return v

    def is_valid(G, i, j, v):
        return 0 <= i < G.H and 0 <= j < G.W and G.S[v] != G.wall
    
    @classmethod
    def compile(cls, H: int, W: int, *args):
        def parse(ts: TokenStream):
            S = ''.join(ts.stream.readline().rstrip() for _ in range(H))
            return cls(H, W, S, *args)
        return parse