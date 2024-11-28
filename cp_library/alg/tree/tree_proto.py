import cp_library.alg.tree.__header__

from typing import overload, Literal
from functools import cached_property
from cp_library.math.inft_cnst import inft
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
        _, s = max((d,v) for v,d in enumerate(T.dfs(0)))
        diam, g = max((d,v) for v,d in enumerate(T.dfs(s)))
        return (diam, s, g) if endpoints else diam
    
    @overload
    def distance(T) -> list[list[int]]: ...
    @overload
    def distance(T, s: int = 0) -> list[int]: ...
    @overload
    def distance(T, s: int, g: int) -> int: ...
    def distance(T, s = None, g = None):
        match s, g:
            case None, None:
                return [T.dfs(u) for u in range(T.N)]
            case s, g:
                return T.dfs(s, g)
            
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
            for v in T[u]:
                if state[v]:
                    D[v] = D[u]+1
                    stack.append(v)
        return D if g is None else inft 


    def dfs_events(G, opts: DFSFlags, s: int = 0):         
        events = []
        # stack = deque([(s,-1)], maxlen=G.N)
        stack = [(s,-1)]
        adj = [None]*G.N


        while stack:
            u, p = stack[-1]
            
            if adj[u] is None:
                adj[u] = iter(G.neighbors(u))
                if DFSFlags.ENTER in opts:
                    events.append((DFSEvent.ENTER, u))
            
            if (v := next(adj[u], None)) is not None:
                if v == p:
                    if DFSFlags.BACK in opts:
                        events.append((DFSEvent.BACK, u, v))
                else:
                    if DFSFlags.DOWN in opts:
                        events.append((DFSEvent.DOWN, u, v))
                    stack.append((v,u))
            else:
                stack.pop()

                if DFSFlags.LEAVE in opts:
                    events.append((DFSEvent.LEAVE, u))
                if p != -1 and DFSFlags.UP in opts:
                    events.append((DFSEvent.UP, u, p))
        return events