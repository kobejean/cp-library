import cp_library.alg.graph.__header__

from typing import Union, overload
from cp_library.ds.heap.fast_heapq  import heapify, heappop, heappush
import operator

from cp_library.alg.graph.dfs_options_cls import DFSEvent, DFSFlags
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
        if s == None:
            return G.floyd_warshall()
        else:
            return G.dijkstra(s, g)
    
    def dijkstra(G, s = 0, g = None):
        D = [inf for _ in range(G.N)]
        D[s] = 0
        que = PriorityQueue(G.N)
        que.push(s, 0)
        while que:
            v, d = que.pop()
            if v == g: return d
            if d > D[v]: continue
            for c, w, *_ in G[v]:
                if (nd := d + w) < D[c]:
                    D[c] = nd
                    que.push(c, nd)
        return D if g is None else inf
    
    @overload
    def shortest_path(G, s: int, t: int) -> list[int]|None: ...
    @overload
    def shortest_path(G, s: int, t: int, distances = True) -> tuple[list[int]|None,list[int]]: ...
    def shortest_path(G, s: int, t: int, distances = False):
        D = [inf] * G.N
        D[s] = 0
        if s == t:
            return ([], D) if distances else []
            
        par = [-1] * G.N
        down = [-1] * G.N
        Eid = G.edge_ids()
        que = PriorityQueue(G.N)
        que.push(s, 0)
        
        while que:
            v, d = que.pop()
            if v == t: break
            if d > D[v]: continue
                
            for i in range(len(G[v])):
                c, w, *_ = G[v][i]
                if (nd := d + w) < D[c]:
                    D[c] = nd
                    par[c] = v
                    down[c] = Eid[v][i]
                    que.push(c, nd)
        
        if D[t] == inf:
            return (None, D) if distances else None
            
        path = []
        v = t
        while v != s:
            path.append(down[v])
            v = par[v]
            
        return (path[::-1], D) if distances else path[::-1]
    
    def kruskal(G):
        E, N = G.E, G.N
        heapify(E)
        dsu = DSU(N)
        MST = []
        need = N-1
        while E and need:
            edge = heappop(E)
            u,v,*_ = edge
            u,v = dsu.merge(u,v,True)
            if u != v:
                MST.append(edge)
                need -= 1
        return MST
    
    def bellman_ford(G, s = 0) -> list[int]:
        D = [inf]*G.N
        D[s] = 0
        for _ in range(G.N-1):
            for u, edges in enumerate(G):
                if D[u] == inf: continue
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
                if Di[k] == inf: continue
                for j in range(G.N):
                    if Dk[j] == inf: continue
                    Di[j] = min(Di[j], Di[k]+Dk[j])
        return D
    
    def dfs_events(G, flags: DFSFlags, s: Union[int,list,None] = None, max_depth: Union[int,None] = None):
        if flags == DFSFlags.INTERVAL:
            if max_depth is None:
                return G.dfs_enter_leave(s)
        elif flags == DFSFlags.DOWN or flags == DFSFlags.TOPDOWN:
            if max_depth is None:
                edges = G.dfs_topdown(s, DFSFlags.CONNECT_ROOTS in flags)
                return [(DFSEvent.DOWN, p, u) for p,u in edges]
        elif flags == DFSFlags.UP or flags == DFSFlags.BOTTOMUP:
            if max_depth is None:
                edges = G.dfs_bottomup(s, DFSFlags.CONNECT_ROOTS in flags)
                return [(DFSEvent.UP, p, u) for p,u in edges]
        elif flags & DFSFlags.BACKTRACK:
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
                    if (s := state[v]) == 0:  # Unvisited
                        if max_depth is None or len(stack)-1 <= max_depth:
                            if flags & DFSFlags.DOWN:
                                events.append((DFSEvent.DOWN, u, v, w))
                            stack.append(v)
                            weights.append(w)
                            child.append(0)
                            if flags & DFSFlags.RETURN_PARENTS:
                                parents[v] = u
                    elif s == 1:  # In progress
                        if flags & DFSFlags.BACK:
                            events.append((DFSEvent.BACK, u, v, w))
                    elif s == 2:  # Completed
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

    def dfs_backtrack(G, flags: DFSFlags, s: Union[int,list] = None, max_depth: Union[int,None] = None):
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
    
    def dfs_topdown(G, s: Union[int,list[int],None] = None, connect_roots = False):
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
from cp_library.ds.heap.priority_queue_cls import PriorityQueue
from cp_library.ds.elist_fn import elist
from math import inf