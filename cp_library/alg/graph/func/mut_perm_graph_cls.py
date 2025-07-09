import cp_library.alg.graph.__header__
from cp_library.alg.graph.func.func_graph_cls import FuncGraph
  
class MutPermGraph(FuncGraph):
    def __init__(P, successors: list[int]):
        super().__init__(successors)
        inv = [0]*P.N
        for i,p in enumerate(P):
            inv[p] = i
        P.inv = inv

    def swap(P, i, j):
        P[i], P[j] = P[j], P[i]
        P.inv[P[i]], P.inv[P[j]] = i, j