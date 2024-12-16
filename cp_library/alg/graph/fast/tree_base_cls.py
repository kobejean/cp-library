import cp_library.alg.graph.__header__
from typing import Callable, Sequence, TypeVar, Union, overload
from collections import deque
from cp_library.io.parser_cls import Parsable, Parser, TokenStream
from cp_library.alg.graph.dfs_options_cls import DFSFlags, DFSEvent
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
        N = len(T)
        T.tin = tin = [-1] * N
        T.tout = tout = [-1] * N
        T.par = par = [-1] * N
        T.order = order = elist(2*N)
        T.delta = delta = elist(2*N)
        Va = T.Va
        
        stack = elist(N)
        stack.append(s)

        while stack:
            u = stack.pop()
            p = par[u]
            
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

    @classmethod
    def compile(cls, N: int, shift: int = -1):
        return super().compile(N, N-1, shift)
    
from cp_library.ds.elist_fn import elist
from cp_library.ds.fill_fn import fill_u32
from cp_library.math.inft_cnst import inft