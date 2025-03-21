import cp_library.alg.tree.fast.__header__
from typing import Callable, Literal, TypeVar, Union, overload
from cp_library.alg.graph.fast.graph_base_cls import GraphBase
from cp_library.misc.typing import _T

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
        st, Va = elist(N := T.N), T.Va
        T.D, T.back = D, back = [inf]*N, i32f(N, -1)
        D[s] = 0
        st.append(s)
        while st:
            nd = D[u := st.pop()]+1
            if u == g: return nd-1
            for i in T.range(u):
                if nd < D[v := Va[i]]:
                    D[v], back[v] = nd, i
                    st.append(v)
        return D if g is None else inf

    def rerooting_dp(T, e: _T, 
                     merge: Callable[[_T,_T],_T], 
                     edge_op: Callable[[_T,int,int,int],_T] = lambda s,i,p,u:s,
                     s: int = 0):
        La, Ua, Va = T.La, T.Ua, T.Va
        order, dp, suf, I = T.dfs_topdown(s), [e]*T.N, [e]*len(Ua), T.Ra[:]
        # up
        for i in order[::-1]:
            u,v = Ua[i], Va[i]
            # subtree v finished up pass, store value to accumulate for u
            dp[v] = new = edge_op(dp[v], i, u, v)
            dp[u] = merge(dp[u], new)
            # suffix accumulation
            if (c:=I[u]-1) > La[u]: suf[c-1] = merge(suf[c], new)
            I[u] = c
        # down
        dp[s] = e # at this point dp stores values to be merged in parent
        for i in order:
            u,v = Ua[i], Va[i]
            dp[u] = merge(pre := dp[u], dp[v])
            dp[v] = edge_op(merge(suf[I[u]], pre), i, v, u)
            I[u] += 1
        return dp
    
    def euler_tour(T, s = 0):
        N, Va = len(T), T.Va
        tin, tout, par, back = [-1]*N,[-1]*N,[-1]*N,[0]*N
        order, delta = elist(2*N), elist(2*N)
        
        st = elist(N); st.append(s)
        while st:
            p = par[u := st.pop()]
            if tin[u] == -1:
                tin[u] = len(order)
                for i in T.range(u):
                    if (v := Va[i]) != p:
                        par[v], back[v] = u, i
                        st.append(u); st.append(v)
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
        depth, order, vis = [0]*N, [0]*N, [0]*N
        st = elist(N)
        st.append(r)
        while st:
            if (s := vis[v := st.pop()]) == 0: # dfs down
                p, vis[v] = par[v], 1; st.append(v)
                for i in T.range(v):
                    if (c := Va[i]) != p:
                        depth[c], par[c] = depth[v]+1, v; st.append(c)
            elif s == 1: # dfs up
                p, l = par[v], -1
                for i in T.range(v):
                    if (c := Va[i]) != p:
                        size[v] += size[c]
                        if size[c] > size[l]:
                            l = c
                heavy[v] = l
                if p == -1:
                    vis[v] = 2
                    st.append(v)

            elif s == 2: # decompose down
                p, h, l = par[v], head[v], heavy[v]
                tin[v], order[time], vis[v] = time, v, 3
                time += 1
                st.append(v)
                
                for i in T.range(v):
                    if (c := Va[i]) != p and c != l:
                        head[c], vis[c] = c, 2
                        st.append(c)

                if l != -1:
                    head[l], vis[l] = h, 2
                    st.append(l)

            elif s == 3: # decompose up
                tout[v] = time
        T.size, T.depth = size, depth
        T.order, T.tin, T.tout = order, tin, tout
        T.par, T.heavy, T.head = par, heavy, head

    @classmethod
    def compile(cls, N: int, shift: int = -1):
        return GraphBase.compile.__func__(cls, N, N-1, shift)
    
from cp_library.ds.elist_fn import elist
from cp_library.ds.array_init_fn import u32f, i32f
from math import inf