import cp_library.__header__
from typing import Iterable, Union
import cp_library.alg.__header__
from cp_library.alg.dp.chmin_fn import chmin
from cp_library.alg.iter.slice_iterator_reverse_cls import SliceIteratorReverse
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
from cp_library.alg.graph.csr.graph_base_cls import GraphBase
import cp_library.alg.graph.csr.snippets.__header__

def two_edge_connected_components(G: GraphBase, s: Union[int,list,None] = None) -> Iterable[list[int]]:
    '''
    Returns an iterator of vertex lists, each representing a two-edge-connected component.
    '''
    low, st, e2ccs, L = [N := G.N]*N, elist(G.M), elist(G.M), elist(G.M)

    def enter(u):
        st.append(u)
        low[u] = G.tin[u]

    def back(u,v,i):
        chmin(low, u, G.tin[v])

    def up(u,p,i):
        chmin(low, p, low[u])
        if low[u] > G.tin[p]:
            # add new two-edge-connected component
            L.append(len(e2ccs))
            v = -1
            while v != u:
                e2ccs.append(v := st.pop())

    def leave(u):
        if G.back[u] < 0:
            # add new two-edge-connected component
            L.append(len(e2ccs))
            e2ccs.extend(st)
            st.clear()

    G.dfs(s, enter_fn=enter, back_fn=back, up_fn=up, leave_fn=leave)
    return SliceIteratorReverse(e2ccs, L)

from cp_library.ds.elist_fn import elist