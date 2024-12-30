import cp_library.alg.tree.__header__

from typing import overload
from functools import cached_property
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

    def hld_precomp(T, r = 0):
        N, time = T.N, 0
        tin, tout, size = [0]*N, [0]*N, [1]*N+[0]
        par, heavy, head = [-1]*N, [-1]*N, [r]*N
        depth, order, state = [0]*N, [0]*N, [0]*N
        Wpar = [0]*N
        stack = elist(N)
        stack.append(r)
        while stack:
            if (s := state[v := stack.pop()]) == 0: # dfs down
                p, state[v] = par[v], 1
                stack.append(v)
                for c, w, *_ in T[v]:
                    if c != p:
                        depth[c], par[c], Wpar[c] = depth[v]+1, v, w
                        stack.append(c)

            elif s == 1: # dfs up
                p, l = par[v], -1
                for c, w, *_ in T[v]:
                    if c != p:
                        size[v] += size[c]
                        if size[c] > size[l]:
                            l = c
                heavy[v] = l
                if p == -1:
                    state[v] = 2
                    stack.append(v)

            elif s == 2: # decompose down
                p, h, l = par[v], head[v], heavy[v]
                tin[v], order[time], state[v] = time, v, 3
                time += 1
                stack.append(v)
                
                for c, *_ in T[v]:
                    if c != p and c != l:
                        head[c], state[c] = c, 2
                        stack.append(c)

                if l != -1:
                    head[l], state[l] = h, 2
                    stack.append(l)

            elif s == 3: # decompose up
                tout[v] = time
        T.size, T.depth = size, depth
        T.order, T.tin, T.tout = order, tin, tout
        T.par, T.heavy, T.head = par, heavy, head
        T.Wpar = Wpar

from math import inf
from cp_library.ds.elist_fn import elist