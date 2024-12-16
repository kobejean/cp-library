import cp_library.alg.graph.__header__
from typing import Callable, Sequence, Union, overload
from collections import deque
from cp_library.io.parser_cls import Parsable, Parser, TokenStream
from cp_library.alg.graph.dfs_options_cls import DFSFlags, DFSEvent

class GraphBase(Sequence, Parsable):
    def __init__(self, N: int, M: int, U: list[int], V: list[int], 
                 deg: list[int], La: list[int], Ra: list[int],
                 Ua: list[int], Va: list[int], Ea: list[int]):
        self.N = N
        """The number of vertices."""
        self.M = M
        """The number of edges."""
        self.U = U
        """A list of source vertices in the original edge list."""
        self.V = V
        """A list of destination vertices in the original edge list."""
        self.deg = deg
        """deg[u] is the out degree of vertex u."""
        self.La = La
        """La[u] stores the start index of the list of adjacent vertices from u."""
        self.Ra = Ra
        """Ra[u] stores the stop index of the list of adjacent vertices from u."""
        self.Ua = Ua
        """Ua[i] = u for La[u] <= i < Ra[u], useful for backtracking."""
        self.Va = Va
        """Va[i] lists adjacent vertices to u for La[u] <= i < Ra[u]."""
        self.Ea = Ea
        """Ea[i] lists the edge ids that start from u for La[u] <= i < Ra[u].
        For undirected graphs, edge ids in range M<= e <2*M are edges from V[e-M] -> U[e-M].
        """

    def __len__(G) -> int:
        return G.N

    def __getitem__(G, u):
        l,r = G.La[u],G.Ra[u]
        return G.Va[l:r]
    
    def range(G, u):
        return range(G.La[u],G.Ra[u])
    
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
            case s, g:
                return G.bfs(s, g)

    @overload
    def bfs(G, s: Union[int,list] = 0) -> list[int]: ...
    @overload
    def bfs(G, s: Union[int,list], g: int) -> int: ...
    def bfs(G, s: int = 0, g: int = None):
        N, Va = G.N, G.Va
        D = [inft]*N
        S = G.starts(s)
        que = deque(S)
        for u in S: D[u] = 0
        while que:
            nd = D[u := que.popleft()]+1
            if u == g: return nd-1
            for i in G.range(u):
                if nd < D[v := Va[i]]:
                    D[v] = nd
                    que.append(v)
        return D if g is None else inft 

    def floyd_warshall(G) -> list[list[int]]:
        N, M = G.N, G.M
        Ua, Va = G.Ua, G.Va
        D = [[inft]*N for _ in range(N)]

        for u in range(N):
            D[u][u] = 0

        for i in range(M):
            u,v = Ua[i], Va[i]
            D[u][v] = 1
        
        for k, Dk in enumerate(D):
            for Di in D:
                if Di[k] == inft: continue
                for j in range(N):
                    if Dk[j] == inft: continue
                    Di[j] = min(Di[j], Di[k]+Dk[j])
        return D
    

    def dfs_discovery(G, s: Union[int,list[int],None] = None, include_roots = False):
        '''Returns lists U and V representing U[i] -> V[i] edges in order of top down discovery'''
        N, Va = G.N, G.Va
        vis = [False]*N
        stack: list[int] = elist(N)
        order: list[int] = elist(N)

        for s in G.starts(s):
            if vis[s]: continue
            if include_roots:
                order.append(-s-1)
            vis[s] = True
            stack.append(s)
            while stack:
                u = stack.pop()
                for i in G.range(u):
                    v = Va[i]
                    if vis[v]: continue
                    vis[v] = True
                    order.append(i)
                    stack.append(v)
        return order

    def dfs(G, s: int|list = None, /,
            connect_roots = False, backtrack = False, max_depth = None,
            enter_fn: Callable[[int],None] = None,
            leave_fn: Callable[[int],None] = None,
            max_depth_fn: Callable[[int],None] = None,
            down_fn: Callable[[int,int],None] = None, 
            back_fn: Callable[[int,int],None] = None,
            up_fn: Callable[[int,int],None] = None):
        Va, La, Ra, I = G.Va, G.La, G.Ra, G.La[:]

        state = [0]*G.N
        stack = elist(G.N if max_depth is None else max_depth+1)
        for s in G.starts(s):
            if state[s]: continue
            stack.append(s)
            state[s] = 1
            if connect_roots and down_fn: down_fn(-1,s)
            while stack:
                u = stack[-1]
                if state[u] == 1:
                    state[u] = 2
                    if enter_fn: enter_fn(u)
                    if max_depth is not None and len(stack) > max_depth:
                        I[u] = Ra[u]
                        if max_depth_fn: max_depth_fn(u)

                if (i := I[u]) < Ra[u]:
                    I[u] += 1
                    if state[v := Va[i]]:
                        if back_fn: back_fn(u,v)
                    else:
                        stack.append(v)
                        state[v] = 1
                        if down_fn: down_fn(u,v)
                else:
                    stack.pop()
                    if backtrack:
                        state[u] = 0
                        I[u] = La[u]
                    if leave_fn: leave_fn(u)
                    if up_fn: up_fn(u, stack[-1])
            if connect_roots and up_fn: up_fn(s, -1)

    
    def dfs_enter_leave(G, s: Union[int,list[int],None] = None):
        '''Returns lists U and V representing U[i] -> V[i] edges in order of top down discovery'''
        N, La, Ra, Va = G.N, G.La, G.Ra, G.Va
        I = La[:]
        stack: list[int] = elist(N)
        order: list[int] = elist(2*N)
        events: list[DFSEvent] = elist(2*N)
        G.par = par = [-1]*N
        ENTER, LEAVE = int(DFSEvent.ENTER), int(DFSEvent.LEAVE)

        for s in G.starts(s):
            if par[s] >= 0: continue
            par[s] = s
            order.append(s)
            events.append(ENTER)
            stack.append(s)
            while stack:
                u = stack[-1]
                if (i := I[u]) < Ra[u]:
                    I[u] += 1
                    if par[v := Va[i]] >= 0: continue
                    par[v] = u
                    order.append(v)
                    events.append(ENTER)
                    stack.append(v)
                else:
                    stack.pop()
                    order.append(u)
                    events.append(LEAVE)
            par[s] = s
        return events, order
    
    def is_bipartite(G):
        N, Va = G.N, G.Va
        que = deque()
        color = [-1]*N
                
        for s in range(N):
            if color[s] >= 0:
                continue
            color[s] = 1
            que.append(s)
            while que:
                u = que.popleft()
                for i in G.range(u):
                    if color[v := Va[i]] == -1:
                        color[v] = 1 - color[u]
                        que.append(v)
                    elif color[v] == color[u]:
                        return False
        return True
    
    def starts(G, s: Union[int,list[int],None]) -> list[int]:
        match s:
            case int(s): return [s]
            case None: return [*range(G.N)]
            case V: return V if isinstance(V, list) else list(V)

    @classmethod
    def compile(cls, N: int, M: int, shift: int = -1):
        def parse(ts: TokenStream):
            U, V = fill_u32(M), fill_u32(M)
            stream = ts.stream
            for i in range(M):
                u, v = map(int, stream.readline().split())
                U[i], V[i] = u+shift, v+shift
            return cls(N, U, V)
        return parse
    
from cp_library.ds.elist_fn import elist
from cp_library.ds.fill_fn import fill_u32
from cp_library.math.inft_cnst import inft