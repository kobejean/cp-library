import cp_library.alg.tree.fast.__header__
from typing import Callable, Literal, TypeVar, Union, overload
from cp_library.alg.graph.fast.graph_base_cls import GraphBase

_T = TypeVar('_T')

class TreeBase(GraphBase):
    @overload
    def distance(T) -> list[list[int]]: ...
    @overload
    def distance(T, s: int = 0) -> list[int]: ...
    @overload
    def distance(T, s: int, g: int) -> int: ...
    def distance(T, s = None, g = None):
        if s == None:
            return [T.dfs_distance(u) for u in range(T.N)]
        else:
            return T.dfs_distance(s, g)

    @overload
    def diameter(T) -> int: ...
    @overload
    def diameter(T, endpoints: Literal[True]) -> tuple[int,int,int]: ...
    def diameter(T, endpoints = False):
        mask = (1 << (shift := T.N.bit_length())) - 1
        s = max(d << shift | v for v,d in enumerate(T.distance(0))) & mask
        dg = max(d << shift | v for v,d in enumerate(T.distance(s))) 
        diam, g = dg >> shift, dg & mask
        return (diam, s, g) if endpoints else diam
    
    def dfs_distance(T, s: int, g: Union[int,None] = None):
        stack, Va = elist(N := T.N), T.Va
        T.D, T.back = D, back = fill_u64(N, inft), fill_i32(N, -1)
        D[s] = 0
        stack.append(s)
        while stack:
            nd = D[u := stack.pop()]+1
            if u == g: return nd-1
            for i in T.range(u):
                if nd < D[v := Va[i]]:
                    D[v], back[v] = nd, i
                    stack.append(v)
        return D if g is None else inft

    def rerooting_dp(T, e: _T, 
                     merge: Callable[[_T,_T],_T], 
                     add_child: Callable[[int,int,int,_T],_T] = lambda p,c,i,s:s,
                     s: int = 0):
        N, La, Ra, Ua, Va = T.N, T.La, T.Ra, T.Ua, T.Va
        order = T.dfs_discovery(s)
        dp = [e]*N
        suf = [e]*len(Ua)
        I = Ra[:] # tracks current indices for suffix array accumulation

        # up
        for i in order[::-1]:
            u,v = Ua[i], Va[i]
            # subtree v finished up pass, store value to accumulate for u
            dp[v] = new = add_child(u, v, i, dp[v])
            dp[u] = merge(dp[u], new)
            # suffix accumulation
            I[u] -= 1
            if I[u] > La[u]:
                suf[I[u]-1] = merge(suf[I[u]], new)

        # down
        dp[s] = e
        for i in order:
            u,v = Ua[i], Va[i]
            # prefix accumulation
            dp[u] = merge(pre := dp[u], dp[v])
            # push value to child
            dp[v] = add_child(v, u, i, merge(suf[I[u]], pre))
            I[u] += 1
        
        return dp
    
    def euler_tour(T, s = 0):
        N, Va = len(T), T.Va
        tin, tout, par, back = [-1]*N,[-1]*N,[-1]*N,[0]*N
        order, delta = elist(2*N), elist(2*N)
        
        stack = elist(N)
        stack.append(s)
        while stack:
            p = par[u := stack.pop()]
            if tin[u] == -1:
                tin[u] = len(order)
                for i in T.range(u):
                    if (v := Va[i]) != p:
                        par[v], back[v] = u, i
                        stack.append(u)
                        stack.append(v)
                delta.append(1)
            else:
                delta.append(-1)
            
            order.append(u)
            tout[u] = len(order)
        delta[0] = delta[-1] = 0
        T.tin, T.tout, T.par, T.back = tin, tout, par, back
        T.order, T.delta = order, delta

    def hld_precomp(T, r = 0):
        N, time, Va = T.N, 0, T.Va
        tin, tout, size = [0]*N, [0]*N, [1]*N+[0]
        par, heavy, head = [-1]*N, [-1]*N, [r]*N
        depth, order, state = [0]*N, [0]*N, [0]*N
        stack = elist(N)
        stack.append(r)
        while stack:
            if (s := state[v := stack.pop()]) == 0: # dfs down
                p, state[v] = par[v], 1
                stack.append(v)
                for i in T.range(v):
                    if (c := Va[i]) != p:
                        depth[c], par[c] = depth[v]+1, v
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

    @classmethod
    def compile(cls, N: int, shift: int = -1):
        return GraphBase.compile.__func__(cls, N, N-1, shift)
    
from cp_library.ds.elist_fn import elist
from cp_library.ds.fill_fn import fill_u64, fill_i32
from cp_library.math.inft_cnst import inft