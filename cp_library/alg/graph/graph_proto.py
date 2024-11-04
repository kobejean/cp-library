import cp_library.alg.graph.__header__
from cp_library.io.parser_cls import Parsable, Parser, TokenStream

from typing import Iterable, overload
from collections import deque
from math import inf

class GraphProtocol(list, Parsable):

    def neighbors(G, v: int) -> Iterable[int]:
        return G[v]
    
    def edge_ids(G) -> list[list[int]]: ...

    @overload
    def distance(G) -> list[list[int]]: ...
    @overload
    def distance(G, s: int = 0) -> list[int]: ...
    @overload
    def distance(G, s: int, g: int) -> int: ...
    def distance(G, s = None, g = None):
        match s, g:
            case None, None:
                return G.floyd_warshall()
            case s, None:
                return G.bfs(s)
            case s, g:
                return G.bfs(s, g)

    @overload
    def bfs(G, s: int = 0) -> list[int]: ...
    @overload
    def bfs(G, s: int, g: int) -> int: ...
    def bfs(G, s = 0, g = None):
        D = [inf for _ in range(G.N)]
        D[s] = 0
        q = deque([s])
        while q:
            nd = D[u := q.popleft()]+1
            if u == g: return D[u]
            for v in G.neighbors(u):
                if nd < D[v]:
                    D[v] = nd
                    q.append(v)
        return D if g is None else inf    
    
    
    def floyd_warshall(G) -> list[list[int]]:
        D = [[inf]*G.N for _ in range(G.N)]

        for u in G:
            D[u][u] = 0
            for v in G.neighbors(u):
                D[u][v] = 1
        
        for k, Dk in enumerate(D):
            for Di in D:
                for j in range(G.N):
                    Di[j] = min(Di[j], Di[k]+Dk[j])
        return D
    
    
    def find_cycle(G, s = 0, vis = None, par = None):
        N = G.N
        vis = vis or [0] * N
        par = par or [-1] * N
        if vis[s]: return None
        vis[s] = 1
        stack = [(True, s)]
        while stack:
            forw, v = stack.pop()
            if forw:
                stack.append((False, v))
                vis[v] = 1
                for u in G.neighbors(v):
                    if vis[u] == 1 and u != par[v]:
                        # Cycle detected
                        cyc = [u]
                        vis[u] = 2
                        while v != u:
                            cyc.append(v)
                            vis[v] = 2
                            v = par[v]
                        return cyc
                    elif vis[u] == 0:
                        par[u] = v
                        stack.append((True, u))
            else:
                vis[v] = 2
        return None
    
    def bridges(G):
        tin = [-1] * G.N
        low = [-1] * G.N
        par = [-1] * G.N
        vis = [0] * G.N
        in_edge = [-1] * G.N

        Eid = G.edge_ids()
        time = 0
        bridges = []
        stack = list(range(G.N))
        while stack:
            v = stack.pop()
            p = par[v]
            match vis[v]:
                case 0:
                    vis[v] = 1
                    tin[v] = low[v] = time
                    time += 1
                    stack.append(v)
                    for i, child in enumerate(G.neighbors(v)):
                        if child == p:
                            continue
                        match vis[child]:
                            case 0:
                                # Tree edge - recurse
                                par[child] = v
                                in_edge[child] = Eid[v][i]
                                stack.append(child)
                            case 1:
                                # Back edge - update low-link value
                                low[v] = min(low[v], tin[child])
                case 1:
                    vis[v] = 2
                    if p != -1:
                        low[p] = min(low[p], low[v])
                        if low[v] > tin[p]:
                            bridges.append(in_edge[v])
                
        return bridges

    def articulation_points(G):
        N = G.N
        order = [-1] * N
        low = [-1] * N
        par = [-1] * N
        vis = [0] * G.N
        children = [0] * G.N
        ap = [False] * N
        time = 0
        stack = list(range(N))

        while stack:
            v = stack.pop()
            p = par[v]
            if vis[v] == 0:
                vis[v] = 1
                order[v] = low[v] = time
                time += 1
            
                stack.append(v)
                for child in G[v]:
                    if order[child] == -1:
                        par[child] = v
                        stack.append(child)
                    elif child != p:
                        low[v] = min(low[v], order[child])
                if p != -1:
                    children[p] += 1
            elif vis[v] == 1:
                vis[v] = 2
                ap[v] |= p == -1 and children[v] > 1
                if p != -1:
                    low[p] = min(low[p], low[v])
                    ap[p] |= par[p] != -1 and low[v] >= order[p]

        return ap

    @classmethod
    def compile(cls, N: int, M: int, E):
        edge = Parser.compile(E)
        def parse(ts: TokenStream):
            return cls(N, (edge(ts) for _ in range(M)))
        return parse
    