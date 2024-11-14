import cp_library.alg.graph.__header__

from collections.abc import Iterator
from typing import Iterable
from cp_library.alg.graph.grid_graph_proto import GridGraphProtocol

class LazyGridGraph(GridGraphProtocol):

    def neighbors(G, u: int) -> Iterable[int]:
        S, wall, dirs, H, W = G.S, G.wall, G.dirs, G.H, G.W
        i,j = divmod(u, W)
        return tuple(v
            for di,dj in dirs
                if (0 <= (ni:=i+di) < H 
                    and 0 <= (nj:=j+dj) < W  
                    and S[v:=ni*W+nj] != wall)
        ) if S[u] != wall else tuple()
    
    def __len__(G) -> int:
        return G.N
    
    def __getitem__(G, v: int):
        return G.neighbors(v)
    
    def __iter__(G) -> Iterator:
        return iter(G[v] for v in range(G.N))
    