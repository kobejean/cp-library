import cp_library.io.__header__
from cp_library.io.read_specs_fn import read
from cp_library.alg.graph.edge_list_weighted_cls import EdgeListWeighted

def read_edges(M, I=-1):
    return read(EdgeListWeighted[M,I])
