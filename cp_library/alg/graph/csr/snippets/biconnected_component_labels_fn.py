import cp_library.__header__
from typing import Iterable, Union
import cp_library.alg.__header__
from cp_library.alg.dp.chmin_fn import chmin
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
from cp_library.alg.graph.csr.graph_base_cls import GraphBase
import cp_library.alg.graph.csr.snippets.__header__

def biconnected_component_labels(G: GraphBase, s: Union[int,list,None] = None) -> Iterable[list[int]]:
    '''
    Returns a list of edge biconnected component classifications.
    '''
    low, st, bccs, id = [N := G.N]*N, elist(G.M), [-1]*len(G.Ea), -1

    def back(u,v,i):
        st.append(i)
        chmin(low, u, G.tin[v])

    def down(u,v,i):
        st.append(i)
        low[v] = G.tin[v]

    def up(u,p,i):
        nonlocal id
        chmin(low, p, low[u])
        if low[u] >= G.tin[p]:
            # add new biconnected component
            j = -1; id += 1
            while j != i:
                bccs[j := st.pop()] = bccs[G.twin[j]] = id
            
    G.dfs(s, down_fn=down, back_fn=back, up_fn=up)
    return bccs
two_vertex_connected_component_labels = biconnected_component_labels

from cp_library.ds.elist_fn import elist