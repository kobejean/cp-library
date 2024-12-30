from cp_library.ds.elist_fn import elist
import cp_library.alg.tree.__header__

from typing import overload, Literal, Union
from functools import cached_property
from math import inf
from collections import deque
from cp_library.alg.graph.dfs_options_cls import DFSFlags, DFSEvent
from cp_library.alg.graph.graph_proto import GraphProtocol
from cp_library.alg.tree.lca_table_iterative_cls import LCATable

class TreeProtocol(GraphProtocol):

    @cached_property
    def lca(T):
        return LCATable(T)
    
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
    
    @overload
    def distance(T) -> list[list[int]]: ...
    @overload
    def distance(T, s: int = 0) -> list[int]: ...
    @overload
    def distance(T, s: int, g: int) -> int: ...
    def distance(T, s = None, g = None):
        if s == None:
            return [T.dfs(u) for u in range(T.N)]
        else:
            return T.dfs(s, g)
            
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
            for v in T[u]:
                if state[v]:
                    D[v] = D[u]+1
                    stack.append(v)
        return D if g is None else inf 


    def dfs_events(G, flags: DFSFlags, s: int = 0):         
        events = []
        stack = [(s,-1)]
        adj = [None]*G.N


        while stack:
            u, p = stack[-1]
            
            if adj[u] is None:
                adj[u] = iter(G.neighbors(u))
                if DFSFlags.ENTER in flags:
                    events.append((DFSEvent.ENTER, u))
            
            if (v := next(adj[u], None)) is not None:
                if v == p:
                    if DFSFlags.BACK in flags:
                        events.append((DFSEvent.BACK, u, v))
                else:
                    if DFSFlags.DOWN in flags:
                        events.append((DFSEvent.DOWN, u, v))
                    stack.append((v,u))
            else:
                stack.pop()

                if DFSFlags.LEAVE in flags:
                    events.append((DFSEvent.LEAVE, u))
                if p != -1 and DFSFlags.UP in flags:
                    events.append((DFSEvent.UP, u, p))
        return events
    
    def euler_tour(T, s = 0):
        N = len(T)
        T.tin = tin = [-1] * N
        T.tout = tout = [-1] * N
        T.par = par = [-1] * N
        T.order = order = elist(2*N)
        T.delta = delta = elist(2*N)
        
        stack = elist(N)
        stack.append(s)

        while stack:
            u = stack.pop()
            p = par[u]
            
            if tin[u] == -1:
                tin[u] = len(order)
                
                for v in T[u]:
                    if v != p:
                        par[v] = u
                        stack.append(u)
                        stack.append(v)
                
                delta.append(1)
            else:
                delta.append(-1)
            
            order.append(u)
            tout[u] = len(order)
        delta[0] = delta[-1] = 0

    def hld_precomp(T, r = 0):
        N, time = T.N, 0
        tin, tout, size = [0]*N, [0]*N, [1]*N+[0]
        par, heavy, head = [-1]*N, [-1]*N, [r]*N
        depth, order, state = [0]*N, [0]*N, [0]*N
        stack = elist(N)
        stack.append(r)
        while stack:
            if (s := state[v := stack.pop()]) == 0: # dfs down
                p, state[v] = par[v], 1
                stack.append(v)
                for c in T[v]:
                    if c != p:
                        depth[c], par[c] = depth[v]+1, v
                        stack.append(c)

            elif s == 1: # dfs up
                p, l = par[v], -1
                for c in T[v]:
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
                
                for c in T[v]:
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