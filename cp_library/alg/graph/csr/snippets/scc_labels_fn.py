import cp_library.__header__
from typing import Iterator
import cp_library.alg.__header__
from cp_library.alg.dp.chmin_fn import chmin
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
import cp_library.alg.graph.csr.snippets.__header__

def scc_labels(G: 'DiGraph') -> Iterator[list[int]]:
    low, on, st, sccs, id = u32f(N := G.N), u8f(N), elist(N), [0]*N, 0
    
    def enter(u):
        low[u] = G.tin[u]
        st.append(u)
        on[u] = 1

    def back_or_cross(u,v,i):
        if on[v]: chmin(low, u, G.tin[v])

    def leave(u):
        nonlocal id
        if low[u] == G.tin[u]:
            v, id = -1, id+1
            while v != u:
                on[v := st.pop()] = 0
                sccs[v] = id

    def up(u,v,i):
        chmin(low, v, low[u])

    G.dfs(enter_fn=enter, back_fn=back_or_cross, cross_fn=back_or_cross, leave_fn=leave, up_fn=up)
    return sccs
from cp_library.alg.graph.csr.digraph_cls import DiGraph
from cp_library.ds.elist_fn import elist
from cp_library.ds.array.u8f_fn import u8f
from cp_library.ds.array.u32f_fn import u32f