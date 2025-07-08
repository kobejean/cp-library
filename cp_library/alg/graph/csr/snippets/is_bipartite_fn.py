import cp_library.__header__
from typing import Union
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
from cp_library.alg.graph.csr.graph_base_cls import GraphBase

def is_bipartite(G: GraphBase, s: Union[int,list,None] = None):
    color, ret = u8f(N := G.N), True

    def visited(u,v,i):
        nonlocal ret
        ret &= color[u] != color[v]
              
    def down(u,v,i):
        color[v] = color[u]^1

    G.dfs(s, down_fn=down, back_fn=visited, cross_fn=visited, forward_fn=visited)
    return ret

from cp_library.ds.array.u8f_fn import u8f