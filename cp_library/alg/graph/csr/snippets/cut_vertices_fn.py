import cp_library.__header__
from typing import Union
import cp_library.alg.__header__
from cp_library.alg.dp.chmin_fn import chmin
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
from cp_library.alg.graph.csr.graph_base_cls import GraphBase

def cut_vertices(G: GraphBase, s: Union[int,list,None] = None):
    '''
    Find cut vertices in an undirected graph using DFS edge types.
    Returns a boolean list that is True for indices of cut vertices.
    '''
    low, children, ap = [N := G.N]*N, [0]*N, [False]*N

    def enter(v):
        low[v] = G.tin[v]

    def back(u,v,i):
        chmin(low, u, G.tin[v])

    def up(u,p,i):
        children[p] += 1
        if G.back[p] < 0:
            # root case
            ap[p] |= children[p] > 1
        else:
            chmin(low, p, low[u])
            ap[p] |= low[u] >= G.tin[p]

    G.dfs(s, enter_fn=enter, back_fn=back, up_fn=up)
    return ap
