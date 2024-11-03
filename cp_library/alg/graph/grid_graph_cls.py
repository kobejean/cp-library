from math import inf
from typing import Iterable
from cp_library.io.parser_cls import TokenStream
from cp_library.alg.graph.graph_proto import GraphProtocol

class GridGraph(GraphProtocol):
    def __init__(G, H, W, S=[]):
        G.N = W*H
        G.W = W
        G.H = H
        G.S = S
        G.dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        G.wall = '#'

    def neighbors(G, v: int) -> Iterable[int]:
        H, W = G.H, G.W
        i,j = divmod(v, W)
        adj = []
        for di,dj in G.dirs:
            ni,nj = i+di,j+dj
            u = ni*W+nj
            if 0 <= ni < H and 0 <= nj < W and G.S[u] != G.wall:
                adj.append(u)
        return adj
    
    @classmethod
    def compile(cls, H: int, W: int):
        def parse(ts: TokenStream):
            S = ''.join(next(ts.stream).rstrip() for _ in range(H))
            return cls(H, W, S)
        return parse