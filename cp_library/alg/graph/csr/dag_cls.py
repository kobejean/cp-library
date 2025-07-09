import cp_library.__header__
from typing import Union
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
from cp_library.alg.graph.csr.digraph_cls import DiGraph

class DAG(DiGraph):
    def __init__(G, N: int, U: list[int], V: list[int]):
        super().__init__(N, U, V)
        G.deg_in, G.deg_out = [0]*N, G.deg
        for v in G.V: G.deg_in[v] += 1

    def starts(G, s: Union[int,list[int],None] = None) -> list[int]:
        if isinstance(s, int): return [s]
        elif s is None: return [s for s in range(G.N) if G.deg_in[s] == 0]
        elif isinstance(s, list): return s
        else: return list(s)