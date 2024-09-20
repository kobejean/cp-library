import cp_library.alg.__init__

from typing import TypeVar
from cp_library.alg.graph.edge_list_cls import EdgeCollection
from cp_library.alg.graph.edge_weighted_cls import EdgeWeighted

M = TypeVar('M', bound=int)
E = TypeVar('E', bound=EdgeWeighted)
class EdgeCollectionWeighted(EdgeCollection):
    @classmethod
    def compile(cls, M: M, E: E = EdgeWeighted[-1]):
        if isinstance(I := E, int):
            E = EdgeWeighted[I]
        return super().compile(M, E)

class EdgeListWeighted(EdgeCollectionWeighted, list[E]):
    pass

class EdgeSetWeighted(EdgeCollectionWeighted, set[E]):
    pass