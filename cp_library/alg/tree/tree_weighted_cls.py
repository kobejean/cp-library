import cp_library.alg.tree.__header__

from cp_library.alg.graph.edge_weighted_cls import EdgeWeighted
from cp_library.alg.tree.tree_cls import Tree

class TreeWeighted(Tree):
    @classmethod
    def compile(cls, N: int, E: type[EdgeWeighted]|int = EdgeWeighted[-1]):
        if isinstance(E, int): E = EdgeWeighted[E]
        return super().compile(N, E)