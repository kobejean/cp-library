import cp_library.__header__
from math import inf
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
import cp_library.alg.graph.csr.snippets.__header__
from cp_library.alg.graph.csr.snippets.recover_path_edge_ids_fn import recover_path_edge_ids

def shortest_path_edge_ids(G: 'GraphBase', s: int, t: int):
    if G.distance(s, t) >= inf: return None
    P = recover_path_edge_ids(G, s, t); P.reverse()
    return P
from cp_library.alg.graph.csr.graph_base_cls import GraphBase
GraphBase.shortest_path_edge_ids = shortest_path_edge_ids