import cp_library.alg.tree.fast.__header__
from typing import Callable, TypeVar
from cp_library.alg.graph.fast.graph_base_cls import GraphBase

_T = TypeVar('_T')

class TreeBase(GraphBase):

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
        tin, tout, par = [-1]*N,[-1]*N,[-1]*N
        order, delta = elist(2*N), elist(2*N)
        
        stack = elist(N)
        stack.append(s)
        while stack:
            p = par[u := stack.pop()]
            if tin[u] == -1:
                tin[u] = len(order)
                for i in T.range(u):
                    if (v := Va[i]) != p:
                        par[v] = u
                        stack.append(u)
                        stack.append(v)
                delta.append(1)
            else:
                delta.append(-1)
            
            order.append(u)
            tout[u] = len(order)
        delta[0] = delta[-1] = 0
        T.tin, T.tout, T.par = tin, tout, par
        T.order, T.delta = order, delta

    def hld_precomp(T, r = 0):
        N, time, Va = T.N, 0, T.Va
        tin, tout, size = [0]*N, [0]*N, [1]*N+[0]
        par, heavy, head = [-1]*N, [-1]*N, [r]*N
        depth, order, state = [0]*N, [0]*N, [0]*N
        stack = elist(N)
        stack.append(r)
        while stack:
            match state[v := stack.pop()]:
                case 0: # dfs down
                    p, state[v] = par[v], 1
                    stack.append(v)
                    for i in T.range(v):
                        if (c := Va[i]) != p:
                            depth[c], par[c] = depth[v]+1, v
                            stack.append(c)

                case 1: # dfs up
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

                case 2: # decompose down
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
                case 3: # decompose up
                    tout[v] = time
        T.size, T.depth = size, depth
        T.order, T.tin, T.tout = order, tin, tout
        T.par, T.heavy, T.head = par, heavy, head

    @classmethod
    def compile(cls, N: int, shift: int = -1):
        return super().compile(N, N-1, shift)
    
from cp_library.ds.elist_fn import elist