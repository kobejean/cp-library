import cp_library.__header__
from math import inf
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
import cp_library.alg.graph.csr.snippets.__header__
from cp_library.alg.graph.csr.snippets.recover_path_vertices_fn import recover_path_vertices

def shortest_path_vertices(G: 'GraphBase', s: int, t: int):
    if G.distance(s, t) >= inf: return None
    P = recover_path_vertices(G, s, t); P.reverse()
    return P
from cp_library.alg.graph.csr.graph_base_cls import GraphBase
GraphBase.shortest_path_vertices = shortest_path_vertices