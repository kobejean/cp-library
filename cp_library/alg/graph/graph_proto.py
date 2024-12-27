import cp_library.alg.graph.__header__
from cp_library.io.parser_cls import Parsable, Parser, TokenStream
from cp_library.alg.graph.dfs_options_cls import DFSFlags, DFSEvent
from cp_library.ds.elist_fn import elist
from typing import Iterable, Union, overload
from collections import deque
from cp_library.math.inft_cnst import inft

class GraphProtocol(list, Parsable):
    def __init__(G, N: int, E: list = None, adj: Iterable = None):
        G.N = N
        if E is not None:
            G.M, G.E = len(E), E
        if adj is not None:
            super().__init__(adj)

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
        if s == None:
            return G.floyd_warshall()
        else:
            return G.bfs(s, g)

    @overload
    def bfs(G, s: Union[int,list] = 0) -> list[int]: ...
    @overload
    def bfs(G, s: Union[int,list], g: int) -> int: ...
    def bfs(G, s = 0, g = None):
        D = [inft for _ in range(G.N)]
        q = deque([s] if isinstance(s, int) else s)
        for u in q: D[u] = 0
        while q:
            nd = D[u := q.popleft()]+1
            if u == g: return D[u]
            for v in G.neighbors(u):
                if nd < D[v]:
                    D[v] = nd
                    q.append(v)
        return D if g is None else inft 

    @overload
    def shortest_path(G, s: int, g: int) -> Union[list[int],None]: ...
    @overload
    def shortest_path(G, s: int, g: int, distances = True) -> tuple[Union[list[int],None],list[int]]: ...
    def shortest_path(G, s: int, g: int, distances = False) -> list[int]:
        D = [inft] * G.N
        D[s] = 0
        if s == g:
            return ([], D) if distances else []
            
        par = [-1] * G.N
        par_edge = [-1] * G.N
        Eid = G.edge_ids()
        q = deque([s])
        
        while q:
            nd = D[u := q.popleft()] + 1
            if u == g: break
                
            for v, eid in zip(G[u], Eid[u]):
                if nd < D[v]:
                    D[v] = nd
                    par[v] = u
                    par_edge[v] = eid
                    q.append(v)
        
        if D[g] == inft:
            return (None, D) if distances else None
            
        path = []
        current = g
        while current != s:
            path.append(par_edge[current])
            current = par[current]
            
        return (path[::-1], D) if distances else path[::-1]
            
     
            
        
    def floyd_warshall(G) -> list[list[int]]:
        D = [[inft]*G.N for _ in range(G.N)]

        for u in range(G.N):
            D[u][u] = 0
            for v in G.neighbors(u):
                D[u][v] = 1
        
        for k, Dk in enumerate(D):
            for Di in D:
                if Di[k] == inft: continue
                for j in range(G.N):
                    if Dk[j] == inft: continue
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

    def find_minimal_cycle(G, s=0):
        D, par, que = [inft] * (N := G.N), [-1] * N, deque([s])
        D[s] = 0
        while que:
            for v in G[u := que.popleft()]:
                if v == s:  # Found cycle back to start
                    cycle = [u]
                    while u != s: cycle.append(u := par[u])
                    return cycle
                if D[v] < inft: continue
                D[v], par[v] = D[u]+1, u
                que.append(v)
    
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
            p = par[v := stack.pop()]
            if vis[v] == 0:
                vis[v] = 1
                tin[v] = low[v] = time
                time += 1
                stack.append(v)
                for i, child in enumerate(G.neighbors(v)):
                    if child == p: continue
                    if vis[child] == 0: # Tree edge - recurse
                        par[child] = v
                        in_edge[child] = Eid[v][i]
                        stack.append(child)
                    else: # Back edge - update low-link value
                        low[v] = min(low[v], tin[child])
            elif vis[v] == 1:
                vis[v] = 2
                if p != -1:
                    low[p] = min(low[p], low[v])
                    if low[v] > tin[p]: bridges.append(in_edge[v])
        return bridges

    def articulation_points(G):
        """
        Find articulation points in an undirected graph using DFS events.
        Returns a boolean list that is True for indices where the vertex is an articulation point.
        """
        N = G.N
        order = [-1] * N
        low = [-1] * N
        par = [-1] * N
        state = [0] * N
        children = [0] * N
        ap = [False] * N
        time = 0
        stack = list(range(N))

        while stack:
            v = stack.pop()
            p = par[v]
            if state[v] == 0:
                state[v] = 1
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
            elif state[v] == 1:
                state[v] = 2
                ap[v] |= p == -1 and children[v] > 1
                if p != -1:
                    low[p] = min(low[p], low[v])
                    ap[p] |= par[p] != -1 and low[v] >= order[p]

        return ap
    
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
        child = [0] * G.N
        stack = [0] * G.N
        if flags & DFSFlags.RETURN_PARENTS:
            parents = [-1] * G.N
        if flags & DFSFlags.RETURN_DEPTHS:
            depths = [-1] * G.N

        events = []
        for s in G.starts(s):
            stack[depth := 0] = s
            if (DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS) in flags:
                events.append((DFSEvent.DOWN,-1,s))
            while depth != -1:
                u = stack[depth]
                
                if not state[u]:
                    state[u] = 1
                    if flags & DFSFlags.ENTER:
                        events.append((DFSEvent.ENTER, u))
                    if flags & DFSFlags.RETURN_DEPTHS:
                        depths[u] = depth
                
                if (c := child[u]) < len(G[u]):
                    child[u] += 1
                    if (s := state[v := G[u][c]]) == 0: # Unvisited
                        if max_depth is None or depth <= max_depth:
                            if flags & DFSFlags.DOWN:
                                events.append((DFSEvent.DOWN, u, v))
                            stack[depth := depth+1] = v
                            if flags & DFSFlags.RETURN_PARENTS:
                                parents[v] = u
                    elif s == 1:  # In progress
                        if flags & DFSFlags.BACK:
                            events.append((DFSEvent.BACK, u, v))
                    elif s == 2: # Completed
                        if flags & DFSFlags.CROSS:
                            events.append((DFSEvent.CROSS, u, v))
                else:
                    depth -= 1
                    state[u] = 0 if DFSFlags.BACKTRACK in flags else 2
                    if flags & DFSFlags.LEAVE:
                        events.append((DFSEvent.LEAVE, u))
                    if depth != -1 and flags & DFSFlags.UP:
                        events.append((DFSEvent.UP, stack[depth], u))
            if (DFSFlags.UP|DFSFlags.CONNECT_ROOTS) in flags:
                events.append((DFSEvent.UP,-1,s))
        ret = tuple((events,)) if DFSFlags.RETURN_ALL & flags else events
        if DFSFlags.RETURN_PARENTS in flags:
            ret += (parents,)
        if DFSFlags.RETURN_DEPTHS in flags:
            ret += (depths,)
        return ret

    def dfs_backtrack(G, flags: DFSFlags, s: Union[int,list] = None, max_depth: Union[int,None] = None):
        stack_depth = (max_depth+1 if max_depth is not None else G.N)
        stack = [0]*stack_depth
        child = [0]*stack_depth
        state = [0]*G.N
        events: list[tuple[DFSEvent, int]|tuple[DFSEvent, int, int]] = []

        for s in G.starts(s):
            if state[s]: continue
            state[s] = 1
            stack[depth := 0] = s
            if DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS in flags:
                events.append((DFSEvent.DOWN,-1,s))
            while depth != -1:
                u = stack[depth]
                if state[u] == 1:
                    state[u] = 2
                    if DFSFlags.ENTER in flags:
                        events.append((DFSEvent.ENTER,u))
                    if max_depth is not None and depth >= max_depth:
                        child[depth] = len(G[u])
                        if DFSFlags.MAXDEPTH in flags:
                            events.append((DFSEvent.MAXDEPTH,u))

                if (c := child[depth]) < len(G[u]):
                    child[depth] += 1
                    if state[v := G[u][c]]:
                        if DFSFlags.BACK in flags:
                            events.append((DFSEvent.BACK,u,v))
                        continue
                    state[v] = 1
                    if DFSFlags.DOWN in flags:
                        events.append((DFSEvent.DOWN,u,v))
                    stack[depth := depth+1] = v
                else:
                    state[u] = 0
                    if DFSFlags.LEAVE in flags:
                        events.append((DFSEvent.LEAVE,u))
                    child[depth] = 0
                    depth -= 1
                    if depth and DFSFlags.UP in flags:
                        events.append((DFSEvent.UP, stack[depth], u))
            if DFSFlags.UP|DFSFlags.CONNECT_ROOTS in flags:
                events.append((DFSEvent.UP,-1,s))
        return events

    def dfs_enter_leave(G, s: Union[int,list,None] = None):
        state = [True] * G.N
        child: list[int] = elist(G.N)
        stack: list[int] = elist(G.N)

        events = []
        for s in G.starts(s):
            if not state[s]: continue
            stack.append(s)
            child.append(0)
            
            while stack:
                u = stack[-1]
                
                if state[u]:
                    state[u] = False
                    events.append((DFSEvent.ENTER, u))

                
                if (c := child[-1]) < len(G[u]):
                    child[-1] += 1
                    if state[v := G[u][c]]:
                        stack.append(v)
                        child.append(0)
                else:
                    stack.pop()
                    child.pop()
                    events.append((DFSEvent.LEAVE, u))

        return events
    
    def dfs_topdown(G, s: Union[int,list,None] = None, connect_roots = False):
        '''Returns list of (u,v) representing u->v edges in order of top down discovery'''
        stack: list[int] = elist(G.N)
        vis = [False]*G.N
        edges: list[tuple[int,int]] = elist(G.N)

        for s in G.starts(s):
            if vis[s]: continue
            if connect_roots:
                edges.append((-1,s))
            vis[s] = True
            stack.append(s)
            while stack:
                u = stack.pop()
                for v in G[u]:
                    if vis[v]: continue
                    vis[v] = True
                    edges.append((u,v))
                    stack.append(v)
        return edges
    
    def dfs_bottomup(G, s: Union[int,list,None] = None, connect_roots = False):
        '''Returns list of (p,u) representing p->u edges in bottom up order'''
        edges = G.dfs_topdown(s, connect_roots)
        edges.reverse()
        return edges

    def is_bipartite(G):
        N = G.N
        que = deque()
        color = [-1]*N
                
        for s in range(N):
            if color[s] >= 0:
                continue
            color[s] = 1
            que.append(s)
            while que:
                u = que.popleft()
                for v in G[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        que.append(v)
                    elif color[v] == color[u]:
                        return False
        return True
    
    def starts(G, v: Union[int,list,None]) -> Iterable:
        if isinstance(v, int):
            return (v,)
        elif v is None:
            return range(G.N)
        else:
            return v

    @classmethod
    def compile(cls, N: int, M: int, E):
        edge = Parser.compile(E)
        def parse(ts: TokenStream):
            return cls(N, [edge(ts) for _ in range(M)])
        return parse
    