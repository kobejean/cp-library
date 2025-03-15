import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
from cp_library.alg.graph.func_graph_cls import FuncGraph

class PermGraph(FuncGraph):
    def inv(P):
        Pinv = [0]*P.N
        for i,p in enumerate(P):
            Pinv[p] = i
        return type(P)(Pinv)
