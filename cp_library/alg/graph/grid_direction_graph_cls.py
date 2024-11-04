import cp_library.alg.graph.__header__

from cp_library.alg.graph.grid_graph_cls import GridGraph

class GridDirectionGraph(GridGraph):
    
    def __getitem__(G, v: int):
        H, W = G.H, G.W
        i,j = divmod(v, W)
        adj = []
        for ndir,(di,dj) in enumerate(G.dirs):
            ni,nj = i+di,j+dj
            if G.is_valid(ni, nj, u := ni*W+nj):
                adj.append((u,ndir))
        return adj