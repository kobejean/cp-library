import cp_library.__header__
from typing import Union
import cp_library.alg.__header__
from cp_library.alg.dp.chmin_fn import chmin
import cp_library.alg.graph.__header__
import cp_library.alg.graph.fast.__header__
from cp_library.alg.graph.fast.graph_base_cls import GraphBase
import cp_library.alg.graph.fast.snippets.__header__

def block_cut_tree(G: GraphBase, s: Union[int,list,None] = None) -> 'Tree':
    '''
    Constructs a block-cut tree from graph G.
    Returns a Tree where vertices [0,N) are original vertices and [N,N+blocks) are biconnected components.
    Inspired by: https://x.com/noshi91/status/1529858538650374144
    '''
    low, st, U, V, bid = [N := G.N]*N, elist(G.M), elist(G.N+G.M), elist(G.N+G.M), N-1

    def back(u,v,i):
        chmin(low, u, G.tin[v])

    def down(u,v,i):
        st.append(v)
        low[v] = G.tin[v]

    def up(u,p,i):
        nonlocal bid
        chmin(low, p, low[u])
        if low[u] >= G.tin[p]:
            v, bid = -1, bid+1
            while u != v: U.append(bid); V.append(v := st.pop())
            U.append(bid); V.append(p)
    G.dfs(s, down_fn=down, back_fn=back, up_fn=up)
    return Tree(bid+1, U, V)

from cp_library.alg.tree.fast.tree_cls import Tree
from cp_library.ds.elist_fn import elist