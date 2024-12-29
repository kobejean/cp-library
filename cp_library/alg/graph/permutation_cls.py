import cp_library.alg.graph.__header__
from cp_library.alg.graph.functional_graph_cls import FunctionalGraph

class Permutation(FunctionalGraph):
    def inv(P):
        Pinv = [0]*P.N
        for i,p in enumerate(P):
            Pinv[p] = i
        return type(P)(Pinv)