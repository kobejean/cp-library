import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
import cp_library.alg.graph.csr.snippets.__header__

def recover_path_edge_ids(G: 'GraphBase', s: int, t: int):
    P = u32f(0)
    while s != t: P.append(G.Ea[a := G.back[t]]), (t := G.Ua[a])
    return P
from cp_library.alg.graph.csr.graph_base_cls import GraphBase
GraphBase.recover_path_edge_ids = recover_path_edge_ids
from cp_library.ds.array.u32f_fn import u32f