import cp_library.alg.__header__

from typing import TypeVar
from cp_library.alg.graph.edge_list_cls import EdgeCollection
from cp_library.alg.graph.edge_weighted_cls import EdgeWeighted

M = TypeVar('M', bound=int)
Ew = TypeVar('Ew', bound=EdgeWeighted)
class EdgeCollectionWeighted(EdgeCollection):
    @classmethod
    def compile(cls, M: M, Ew: Ew = EdgeWeighted[-1]):
        if isinstance(I := Ew, int):
            Ew = EdgeWeighted[I]
        return super().compile(M, Ew)

class EdgeListWeighted(EdgeCollectionWeighted, list[Ew]):
    pass

class EdgeSetWeighted(EdgeCollectionWeighted, set[Ew]):
    pass