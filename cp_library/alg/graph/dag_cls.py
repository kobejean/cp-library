import cp_library.alg.graph.__header__

from typing import Iterable
from cp_library.alg.graph.edge_cls import Edge
from cp_library.alg.graph.digraph_cls import DiGraph

class DAG(DiGraph):
    def __init__(G, N: int, E: list[Edge]=[]):
        super().__init__(N, E)
        deg_in = [0]*N
        for _,v in G.E:
            deg_in[v] += 1
        G.deg_in = deg_in

    def starts(G, v: int|list[int]|None) -> Iterable:
        match v:
            case int(v): return (v,)
            case None: return (v for v in range(G.N) if G.deg_in[v] == 0)
            case V: return V