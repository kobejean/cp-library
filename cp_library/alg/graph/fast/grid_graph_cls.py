
import cp_library.alg.graph.__header__
import sys
from cp_library.ds.elist_fn import elist
from cp_library.alg.graph.fast.grid_graph_walled_base_cls import GridGraphWalledBase

class GridGraph(GridGraphWalledBase):

    def __init__(G, H, W, S=[], dirs = [(-1,0),(0,1),(1,0),(0,-1)], wall = '#'):
        N = H*W
        Mest = N*len(dirs)
        deg, La, Ra, Ua, Va = u32f(N), u32f(N), u32f(N), elist(Mest), elist(Mest)
        super().__init__(
            H, W, 0, S, Ua, Va, deg, La, Ra, Ua, Va, None, dirs, wall
        )

        for i in range(H):
            for j in range(W):
                La[u := i*W+j] = len(Ua)
                if G.is_valid(i, j, u):
                    for di,dj in dirs:
                        if G.is_valid(ni:=i+di, nj:=j+dj, v:=ni*W+nj):
                            deg[u] += 1
                            Ua.append(u)
                            Va.append(v)
                Ra[u] = len(Ua)

        G.M = len(Ua)
        G.Ea = u32a(range(G.M))

from cp_library.ds.array_init_fn import u32f, u32a