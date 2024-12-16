import cp_library.alg.tree.__header__

from typing import overload
from functools import cached_property
from cp_library.math.inft_cnst import inft
from cp_library.ds.elist_fn import elist
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
        D = [inft for _ in range(T.N)]
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
        return D if g is None else inft
    
    def euler_tour(T, s = 0):
        N = len(T)
        T.tin = tin = [-1] * N
        T.tout = tout = [-1] * N
        T.par = par = [-1] * N
        T.order = order = elist(2*N)
        T.delta = delta = elist(2*N)
        T.Wdelta = Wdelta = elist(2*N)
        stack = elist(N)
        Wstack = elist(N)
        stack.append(s)
        Wstack.append(0)

        while stack:
            u = stack.pop()
            wd = Wstack.pop()
            p = par[u]
            
            if tin[u] == -1:
                tin[u] = len(order)
                
                for v,w,*_ in T[u]:
                    if v != p:
                        par[v] = u
                        stack.append(u)
                        stack.append(v)
                        Wstack.append(-w)
                        Wstack.append(w)
                delta.append(1)
            else:
                delta.append(-1)
            
            Wdelta.append(wd)
            order.append(u)
            tout[u] = len(order)
        delta[0] = delta[-1] = 0