import cp_library.alg.graph.__header__

from cp_library.alg.graph.grid_graph_proto import GridGraphProtocol

class GridDirectionGraph(GridGraphProtocol):

    def __init__(G, H, W, S=[], dirs = [(-1,0),(0,1),(1,0),(0,-1)], wall = '#'):
        super().__init__(H, W, S, dirs, wall,
            (tuple((v,ndir) 
                for ndir,(di,dj) in enumerate(dirs)
                    if (0 <= (ni:=i+di) < H 
                        and 0 <= (nj:=j+dj) < W  
                        and S[v:=ni*W+nj] != wall)
            ) if S[i*W+j] != wall else tuple()
            for i in range(H) for j in range(W))
        )
