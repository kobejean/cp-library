import cp_library.__header__
from typing import Union
import cp_library.alg.__header__
from cp_library.alg.dp.chmin_fn import chmin
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
from cp_library.alg.graph.csr.graph_base_cls import GraphBase
import cp_library.alg.graph.csr.snippets.__header__

def cut_edges(G: GraphBase, s: Union[int,list,None] = None):
    '''
    Find cut edges in an undirected graph using DFS edge types.
    Returns a list of adjacency indices where the edge is a cut edge.
    '''
    low, I = [N := G.N]*N, elist(G.M)

    def enter(v):
        low[v] = G.tin[v]

    def back(u,v,i):
        chmin(low, u, G.tin[v])

    def up(u,p,i):
        chmin(low, p, low[u])
        if low[u] > G.tin[p]:
            I.append(i)

    G.dfs(s, enter_fn=enter, back_fn=back, up_fn=up)
    return I

from cp_library.ds.elist_fn import elist