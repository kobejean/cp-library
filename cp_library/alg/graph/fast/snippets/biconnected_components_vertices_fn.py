from cp_library.alg.iter.slice_iterator_reverse_cls import SliceIteratorReverse
from cp_library.ds.elist_fn import elist
import cp_library.__header__
import cp_library.alg.__header__
from cp_library.alg.dp.chmin_fn import chmin
import cp_library.alg.graph.__header__
import cp_library.alg.graph.fast.__header__
from cp_library.alg.graph.fast.graph_base_cls import GraphBase
from typing import Iterable, Union

def biconnected_components(G: GraphBase, s: Union[int,list,None] = None) -> Iterable[list[int]]:
    """
    Returns an iterator of vertex lists, each representing a biconnected component.
    Isolated vertices are included as single-vertex components.
    """
    low, st, bccs, L = [N := G.N]*N, elist(G.M), elist(G.M), elist(G.M)

    def back(u,v,i):
        chmin(low, u, G.tin[v])

    def down(u,v,i):
        st.append(i)
        low[v] = G.tin[v]

    def up(u,p,i):
        chmin(low, p, low[u])
        if low[u] >= G.tin[p]:
            # add new biconnected component
            L.append(len(bccs))
            j = -1
            while j != i:
                bccs.append(G.Va[j := st.pop()])
            bccs.append(G.Ua[i])
    G.dfs(s, down_fn=down, back_fn=back, up_fn=up)
    # give the lonely vertices their own components
    for u,d in enumerate(G.deg):
        if d == 0:
            L.append(len(bccs))
            bccs.append(u)
    return SliceIteratorReverse(bccs, L)
