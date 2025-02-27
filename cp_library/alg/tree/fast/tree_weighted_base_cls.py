import cp_library.alg.tree.fast.__header__
from typing import TypeVar, Union
from cp_library.alg.graph.fast.graph_weighted_base_cls import GraphWeightedBase
from cp_library.alg.tree.fast.tree_base_cls import TreeBase

_T = TypeVar('T')
class TreeWeightedBase(TreeBase, GraphWeightedBase):

    def dfs_distance(T, s: int, g: Union[int,None] = None):
        stack, Wa, Va = elist(N := T.N), T.Wa, T.Va
        T.D, T.back = D, back = [inf]*N, i32f(N, -1)
        stack.append(s)
        D[s] = 0
        while stack:
            d = D[u := stack.pop()]
            if u == g: return d
            for i in T.range(u):
                if (nd := d+Wa[i]) < D[v := Va[i]]:
                    D[v], back[v] = nd, i
                    stack.append(v)
        return D if g is None else inf 
    
    def euler_tour(T, s = 0):
        N, Va, Wa = len(T), T.Va, T.Wa
        tin, tout, par = [-1]*N,[-1]*N,[-1]*N
        order, delta, Wdelta = elist(2*N), elist(2*N), elist(2*N)
        
        stack, Wstack = elist(N), elist(N)
        stack.append(s)
        Wstack.append(0)
        while stack:
            p, wd = par[u := stack.pop()], Wstack.pop()
            if tin[u] == -1:
                tin[u] = len(order)
                for i in T.range(u):
                    if (v := Va[i]) != p:
                        w, par[v] = Wa[i], u
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
        T.tin, T.tout, T.par = tin, tout, par
        T.order, T.delta, T.Wdelta = order, delta, Wdelta

    def hld_precomp(T, r = 0):
        N, time, Va, Wa = T.N, 0, T.Va, T.Wa
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
                for i in T.range(v):
                    if (c := Va[i]) != p:
                        depth[c], par[c], Wpar[c] = depth[v]+1, v, Wa[i]
                        stack.append(c)

            elif s == 1: # dfs up
                p, l = par[v], -1
                for i in T.range(v):
                    if (c := Va[i]) != p:
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
                
                for i in T.range(v):
                    if (c := Va[i]) != p and c != l:
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

    @classmethod
    def compile(cls, N: int, shift: int = -1):
        return GraphWeightedBase.compile.__func__(cls, N, N-1, shift)
    
from cp_library.ds.elist_fn import elist
from cp_library.ds.array_init_fn import i64f, i32f
from math import inf