import cp_library.__header__
from typing import Iterator

import cp_library.alg.__header__
from cp_library.alg.dp.chmin_fn import chmin

import cp_library.alg.graph.__header__
import cp_library.alg.graph.fast.__header__
import cp_library.alg.graph.fast.snippets.__header__

def strongly_connected_components(G: 'DiGraph') -> Iterator[list[int]]:
    '''
    Finds strongly connected sccs in directed graph using Tarjan's algorithm.
    Returns sccs in topological order.
    '''
    low, on, st, sccs, L = u32f(N := G.N), u8f(N), elist(N), elist(N), elist(N)
    
    def enter(u):
        low[u] = G.tin[u]
        st.append(u)
        on[u] = 1

    def back_or_cross(u,v,i):
        if on[v]: chmin(low, u, G.tin[v])

    def leave(u):
        if low[u] == G.tin[u]:
            L.append(len(sccs))
            v = -1
            while v != u:
                on[v := st.pop()] = 0
                sccs.append(v)

    def up(u,v,i):
        chmin(low, v, low[u])

    G.dfs(enter_fn=enter, back_fn=back_or_cross, cross_fn=back_or_cross, leave_fn=leave, up_fn=up)
    return SliceIteratorReverse(sccs, L)

from cp_library.alg.graph.fast.digraph_cls import DiGraph
from cp_library.alg.iter.slice_iterator_reverse_cls import SliceIteratorReverse
from cp_library.ds.elist_fn import elist
from cp_library.ds.array_init_fn import u32f, u8f