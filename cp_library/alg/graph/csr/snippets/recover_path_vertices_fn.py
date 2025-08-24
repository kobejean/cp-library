import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
import cp_library.alg.graph.csr.snippets.__header__

def recover_path_vertices(G: 'GraphBase', s: int, t: int):
    P = u32f(1, t)
    while s != t: P.append(t := G.Ua[G.back[t]])
    return P
from cp_library.alg.graph.csr.graph_base_cls import GraphBase
GraphBase.recover_path_vertices = recover_path_vertices
from cp_library.ds.array.u32f_fn import u32f