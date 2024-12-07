import cp_library.alg.graph.__header__
from typing import Sequence, Union, overload
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

    def __getitem__(G, v):
        l,r = G.La[v],G.Ra[v]
        return G.Va[l:r]
    
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
    def bfs(G, s: Union[int,list] = 0) -> list[int]: ...
    @overload
    def bfs(G, s: Union[int,list], g: int) -> int: ...
    def bfs(G, s: int = 0, g: int = None):
        N, La, Ra, Va = G.N, G.La, G.Ra, G.Va
        D = [inft]*N
        q = deque(G.starts(s))
        for u in q: D[u] = 0
        while q:
            nd = D[u := q.popleft()]+1
            if u == g: return nd
            for i in range(La[u],Ra[u]):
                if nd < D[v := Va[i]]:
                    D[v] = nd
                    q.append(v)
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
        N, La, Ra, Va = G.N, G.La, G.Ra, G.Va
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
                for i in range(La[u], Ra[u]):
                    v = Va[i]
                    if vis[v]: continue
                    vis[v] = True
                    order.append(i)
                    stack.append(v)
        return order
    
    def dfs_enter_leave(G, s: Union[int,list[int],None] = None):
        '''Returns lists U and V representing U[i] -> V[i] edges in order of top down discovery'''
        N, La, Ra, Va = G.N, G.La, G.Ra, G.Va
        vis = [False]*N
        I = La[:]
        stack: list[int] = elist(N)
        order: list[int] = elist(2*N)
        G.par = par = [-1]*N
        events: list[DFSEvent] = elist(2*N)

        for s in G.starts(s):
            if vis[s]: continue
            vis[s] = True
            stack.append(s)
            order.append(s)
            events.append(DFSEvent.ENTER)
            while stack:
                u = stack[-1]
                if (i := I[u]) < Ra[u]:
                    I[u] += 1
                    v = Va[i]
                    if vis[v]: continue
                    par[v] = u
                    vis[v] = True
                    order.append(v)
                    events.append(DFSEvent.ENTER)
                    stack.append(v)
                else:
                    stack.pop()
                    order.append(u)
                    events.append(DFSEvent.LEAVE)
        return events, order
    
    def is_bipartite(G):
        N, La, Ra, Va = G.N, G.La, G.Ra, G.Va
        que = deque()
        color = [-1]*N
                
        for s in range(N):
            if color[s] >= 0:
                continue
            color[s] = 1
            que.append(s)
            while que:
                u = que.popleft()
                for i in range(La[u], Ra[u]):
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