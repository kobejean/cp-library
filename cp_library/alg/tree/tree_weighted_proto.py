import cp_library.alg.tree.__header__

from typing import overload
from functools import cached_property
from math import inf
from cp_library.alg.graph.graph_weighted_proto import GraphWeightedProtocol
from cp_library.alg.tree.tree_proto import TreeProtocol
from cp_library.alg.tree.lca_table_weighted_iterative_cls import LCATableWeighted

class TreeWeightedProtocol(GraphWeightedProtocol, TreeProtocol):

    @cached_property
    def lca(T):
        return LCATableWeighted(T)
    
    @overload
    def dfs(T, s: int = 0) -> list[int]: ...
    @overload
    def dfs(T, s: int, g: int) -> int: ...
    def dfs(T, s = 0, g = None):
        D = [inf for _ in range(T.N)]
        D[s] = 0
        state = [True for _ in range(T.N)]
        stack = [s]

        while stack:
            u = stack.pop()
            if u == g: return D[u]
            state[u] = False
            for v, w, *_ in T[u]:
                if state[v]:
                    D[v] = D[u]+w
                    stack.append(v)
        return D if g is None else inf 