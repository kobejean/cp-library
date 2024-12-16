import cp_library.alg.graph.__header__
from typing import Callable, TypeVar
from cp_library.ds.elist_fn import elist
from cp_library.alg.graph.fast.graph_weighted_base_cls import GraphWeightedBase

from cp_library.alg.graph.fast.tree_base_cls import TreeBase

_T = TypeVar('_T')
class TreeWeightedBase(GraphWeightedBase, TreeBase):
     
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
        Va, Wa = T.Va, T.Wa

        while stack:
            u = stack.pop()
            wd = Wstack.pop()
            p = par[u]
            
            if tin[u] == -1:
                tin[u] = len(order)
                
                for i in T.range(u):
                    if (v := Va[i]) != p:
                        w = Wa[i]
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

    @classmethod
    def compile(cls, N: int, shift: int = -1):
        return super().compile(N, N-1, shift)
    