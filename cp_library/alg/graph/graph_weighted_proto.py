from cp_library.ds.elist_fn import elist
from cp_library.alg.graph.dfs_options_cls import DFSEvent, DFSFlags
import cp_library.alg.graph.__header__

from typing import overload
from heapq import heapify, heappop, heappush
import operator
from math import inf

from cp_library.alg.graph.graph_proto import GraphProtocol

class GraphWeightedProtocol(GraphProtocol):

    def neighbors(G, v: int):
        return map(operator.itemgetter(0), G[v])
    
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
                return G.dijkstra(s)
            case s, g:
                return G.dijkstra(s, g)
    
    def dijkstra(G, s = 0, g = None):
        D = [inf for _ in range(G.N)]
        D[s] = 0
        q = [(0, s)]
        while q:
            d, v = heappop(q)
            if d > D[v]: continue
            if v == g: return d
            for u, w, *_ in G[v]:
                if (nd := d + w) < D[u]:
                    D[u] = nd
                    heappush(q, (nd, u))
        return D if g is None else inf
    
    def shortest_path(G, s: int, g: int) -> list[int]:
        if s == g:
            return []
            
        D = [inf] * G.N
        D[s] = 0
        par = [-1] * G.N
        par_edge = [-1] * G.N
        Eid = G.edge_ids()
        q = [(0, s)]
        
        while q:
            d, v = heappop(q)
            if d > D[v]: continue
            if v == g: break
                
            for (u, w, *_), eid in zip(G[v], Eid[v]):
                if (nd := d + w) < D[u]:
                    D[u] = nd
                    par[u] = v
                    par_edge[u] = eid
                    heappush(q, (nd, u))
        
        if D[g] == inf:
            return None
            
        path = []
        current = g
        while current != s:
            path.append(par_edge[current])
            current = par[current]
            
        return path[::-1]
    
    def kruskal(G):
        E, N = G.E, G.N
        heapify(E)
        dsu = DSU(N)
        MST = []
        need = N-1
        while E and need:
            edge = heappop(E)
            u,v,*_ = edge
            u,v = dsu.merge(u,v)
            if u != v:
                MST.append(edge)
                need -= 1
        cls = type(G)
        return cls(N, MST)
    
    def bellman_ford(G, s = 0) -> list[int]:
        D = [inf]*G.N
        D[s] = 0
        for _ in range(G.N-1):
            for u, edges in enumerate(G):
                for v,w,*_ in edges:
                    D[v] = min(D[v], D[u] + w)
        return D
    
    def floyd_warshall(G) -> list[list[int]]:
        D = [[inf]*G.N for _ in range(G.N)]

        for u, edges in enumerate(G):
            D[u][u] = 0
            for v,w in edges:
                D[u][v] = min(D[u][v], w)
        
        for k, Dk in enumerate(D):
            for Di in D:
                for j in range(G.N):
                    Di[j] = min(Di[j], Di[k]+Dk[j])
        return D
    
    def dfs_events(G, flags: DFSFlags, s: int|list|None = None, max_depth: int|None = None):
        match flags:
            case DFSFlags.INTERVAL:
                if max_depth is None:
                    return G.dfs_enter_leave(s)
            case DFSFlags.DOWN|DFSFlags.TOPDOWN:
                if max_depth is None:
                    edges = G.dfs_topdown(s, DFSFlags.CONNECT_ROOTS in flags)
                    return [(DFSEvent.DOWN, p, u) for p,u in edges]
            case DFSFlags.UP|DFSFlags.BOTTOMUP:
                if max_depth is None:
                    edges = G.dfs_bottomup(s, DFSFlags.CONNECT_ROOTS in flags)
                    return [(DFSEvent.UP, p, u) for p,u in edges]
            case flags if flags & DFSFlags.BACKTRACK:
                return G.dfs_backtrack(flags, s, max_depth)
        state = [0] * G.N
        child = elist(G.N)
        weights = elist(G.N)
        stack = elist(G.N)
        if flags & DFSFlags.RETURN_PARENTS:
            parents = [-1] * G.N
        if flags & DFSFlags.RETURN_DEPTHS:
            depths = [-1] * G.N

        events = []
        for s in G.starts(s):
            stack.append(s)
            child.append(0)
            if (DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS) in flags:
                events.append((DFSEvent.DOWN,-1,s,-1))
            while stack:
                u = stack[-1]
                
                if not state[u]:
                    state[u] = 1
                    if flags & DFSFlags.ENTER:
                        events.append((DFSEvent.ENTER, u))
                    if flags & DFSFlags.RETURN_DEPTHS:
                        depths[u] = len(stack)-1
                
                if (c := child[-1]) < len(G[u]):
                    child[-1] += 1
                    v, w = G[u][c]
                    match state[v]:
                        case 0:  # Unvisited
                            if max_depth is None or len(stack)-1 <= max_depth:
                                if flags & DFSFlags.DOWN:
                                    events.append((DFSEvent.DOWN, u, v, w))
                                stack.append(v)
                                weights.append(w)
                                child.append(0)
                                if flags & DFSFlags.RETURN_PARENTS:
                                    parents[v] = u
                        case 1:  # In progress
                            if flags & DFSFlags.BACK:
                                events.append((DFSEvent.BACK, u, v, w))
                        case 2:  # Completed
                            if flags & DFSFlags.CROSS:
                                events.append((DFSEvent.CROSS, u, v, w))
                else:
                    stack.pop()
                    child.pop()
                    state[u] = 0 if DFSFlags.BACKTRACK in flags else 2
                    if flags & DFSFlags.LEAVE:
                        events.append((DFSEvent.LEAVE, u))
                    if stack and flags & DFSFlags.UP:
                        pw = weights.pop()
                        events.append((DFSEvent.UP, stack[-1], u, pw))
            if (DFSFlags.UP|DFSFlags.CONNECT_ROOTS) in flags:
                events.append((DFSEvent.UP,-1,s,-1))
        ret = tuple((events,)) if DFSFlags.RETURN_ALL & flags else events
        if DFSFlags.RETURN_PARENTS in flags:
            ret += (parents,)
        if DFSFlags.RETURN_DEPTHS in flags:
            ret += (depths,)
        return ret

    def dfs_backtrack(G, flags: DFSFlags, s: int|list = None, max_depth: int|None = None):
        stack_depth = (max_depth+1 if max_depth is not None else G.N)
        stack = elist(stack_depth)
        child = elist(stack_depth)
        weights = elist(stack_depth)
        state = [0]*G.N
        events: list[tuple[DFSEvent, int]|tuple[DFSEvent, int, int]] = []

        for s in G.starts(s):
            if state[s]: continue
            state[s] = 1
            stack.append(s)
            child.append(0)
            if DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS in flags:
                events.append((DFSEvent.DOWN,-1,s,-1))
            while stack:
                u = stack[-1]
                if state[u] == 1:
                    state[u] = 2
                    if DFSFlags.ENTER in flags:
                        events.append((DFSEvent.ENTER,u))
                    if max_depth is not None and len(stack) > max_depth:
                        child[-1] = len(G[u])
                        if DFSFlags.MAXDEPTH in flags:
                            events.append((DFSEvent.MAXDEPTH,u))

                if (c := child[-1]) < len(G[u]):
                    child[-1] += 1
                    v, w = G[u][c]
                    if state[v]:
                        if DFSFlags.BACK in flags:
                            events.append((DFSEvent.BACK,u,v,w))
                        continue
                    state[v] = 1
                    if DFSFlags.DOWN in flags:
                        events.append((DFSEvent.DOWN,u,v,w))
                    stack.append(v)
                    child.append(0)
                    weights.append(w)
                else:
                    state[u] = 0
                    if DFSFlags.LEAVE in flags:
                        events.append((DFSEvent.LEAVE,u))
                    stack.pop()
                    child.pop()
                    if stack and DFSFlags.UP in flags:
                        pw = weights.pop()
                        events.append((DFSEvent.UP, stack[-1], u, pw))
                    
            if DFSFlags.UP|DFSFlags.CONNECT_ROOTS in flags:
                events.append((DFSEvent.UP,-1,s,-1))
        return events
    
    def dfs_topdown(G, s: int|list[int]|None = None, connect_roots = False):
        '''Returns list of (u,v) representing u->v edges in order of top down discovery'''
        stack: list[int] = elist(G.N)
        vis = [False]*G.N
        edges: list[tuple[int,int]] = elist(G.N)

        for s in G.starts(s):
            if vis[s]: continue
            if connect_roots:
                edges.append((-1,s,-1))
            vis[s] = True
            stack.append(s)
            while stack:
                u = stack.pop()
                for v,w in G[u]:
                    if vis[v]: continue
                    vis[v] = True
                    edges.append((u,v,w))
                    stack.append(v)
        return edges

from cp_library.ds.dsu_cls import DSU