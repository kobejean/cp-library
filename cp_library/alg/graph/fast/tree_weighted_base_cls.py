import cp_library.alg.graph.__header__
from typing import Callable, TypeVar
from cp_library.alg.graph.fast.graph_weighted_base_cls import GraphWeightedBase

from cp_library.alg.graph.fast.tree_base_cls import TreeBase

_T = TypeVar('_T')
class TreeWeightedBase(GraphWeightedBase, TreeBase):

    @classmethod
    def compile(cls, N: int, shift: int = -1):
        return super().compile(N, N-1, shift)
    