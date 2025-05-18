import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.fast.__header__
from cp_library.alg.graph.fast.grid_graph_walled_base_cls import GridGraphWalledBase

class GridGraph(GridGraphWalledBase):

    def __init__(G, H, W, S=[], dirs = [(-1,0),(0,1),(1,0),(0,-1)], wall = '#'):
        N = H*W
        Mest = N*len(dirs)
        deg, La, Ra, Ua, Va = u32f(N), u32f(N), u32f(N), elist(Mest), elist(Mest)
        super().__init__(H, W, 0, S, Ua, Va, deg, La, Ra, Ua, Va, None, dirs, wall)
        for i in range(H):
            for j in range(W):
                La[u := i*W+j] = len(Ua)
                for di,dj in dirs:
                    if G.is_valid(ni:=i+di, nj:=j+dj, v:=ni*W+nj):
                        Ua.append(u); Va.append(v); deg[u] += 1
                Ra[u] = len(Ua)
        G.twin = [*range(len(G.Va))]
        for i,u in enumerate(G.Ua):
            for j in G.range(G.Va[i]):
                if G.Va[j] == u:
                    G.twin[i] = j
        G.M, G.Ea = len(Ua), u32a(range(G.M))
from cp_library.ds.array.u32a_fn import u32a
from cp_library.ds.array.u32f_fn import u32f
from cp_library.ds.elist_fn import elist