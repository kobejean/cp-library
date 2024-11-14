import cp_library.alg.graph.__header__

from cp_library.alg.graph.lazy_grid_graph_cls import LazyGridGraph

class LazyGridDirectionGraph(LazyGridGraph):

    def neighbors(G, u: int) -> tuple[tuple[int,int], ...]:
        S, wall, dirs, H, W = G.S, G.wall, G.dirs, G.H, G.W
        i,j = divmod(u, W)
        return tuple((v,ndir)
            for ndir,(di,dj) in enumerate(dirs)
                if (0 <= (ni:=i+di) < H 
                    and 0 <= (nj:=j+dj) < W  
                    and S[v:=ni*W+nj] != wall)
        ) if S[u] != wall else tuple()
