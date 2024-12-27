import cp_library.alg.graph.__header__
from typing import Callable, Sequence, Union, overload
from collections import deque
from cp_library.io.parser_cls import Parsable, TokenStream
from cp_library.alg.graph.dfs_options_cls import DFSEvent

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

    def __len__(G) -> int: return G.N
    def __getitem__(G, u): return G.Va[G.La[u]:G.Ra[u]]
    def range(G, u): return range(G.La[u],G.Ra[u])
    
    @overload
    def distance(G) -> list[list[int]]: ...
    @overload
    def distance(G, s: int = 0) -> list[int]: ...
    @overload
    def distance(G, s: int, g: int) -> int: ...
    def distance(G, s = None, g = None):
        if s == None: return G.floyd_warshall()
        else: return G.bfs(s, g)

    def shortest_path(G, s: int, t: int):
        if G.distance(s, t) >= inft: return None
        Ua, back, vertices = G.Ua, G.back, u32a(1, v := t)
        while v != s: vertices.append(v := Ua[back[v]])
        return vertices[::-1]
    
    def shortest_path_edge_ids(G, s: int, t: int):
        if G.distance(s, t) >= inft: return None
        Ea, Ua, back, edges, v = G.Ea, G.Ua, G.back, u32a(0), t
        while v != s:
            edges.append(Ea[i := back[v]])
            v = Ua[i]
        return edges[::-1]
    
    @overload
    def bfs(G, s: Union[int,list] = 0) -> list[int]: ...
    @overload
    def bfs(G, s: Union[int,list], g: int) -> int: ...
    def bfs(G, s: int = 0, g: int = None):
        S, Va, back, D = G.starts(s), G.Va, i32a(N := G.N, -1), u64a(N, inft)
        G.back, G.D = back, D
        for u in S: D[u] = 0
        que = deque(S)
        while que:
            nd = D[u := que.popleft()]+1
            if u == g: return nd-1
            for i in G.range(u):
                if nd < D[v := Va[i]]:
                    D[v], back[v] = nd, i
                    que.append(v)
        return D if g is None else inft 

    def floyd_warshall(G) -> list[list[int]]:
        M, Ua, Va, N = G.M, G.Ua, G.Va, G.N
        G.D = D = [[inft]*N for _ in range(N)]
        for u in range(N): D[u][u] = 0
        for i in range(M): D[Ua[i]][Va[i]] = 1
        for k, Dk in enumerate(D):
            for Di in D:
                if Di[k] == inft: continue
                for j in range(N):
                    if Dk[j] == inft: continue
                    Di[j] = min(Di[j], Di[k]+Dk[j])
        return D

    def find_cycle_indices(G, s: Union[int, None] = None):
        M, Ea, Ua, Va, vis, back = G.M, G.Ea, G. Ua, G.Va, u8a(N := G.N), i32a(N, -1)
        G.vis, G.back, stack = vis, back, elist(N)
        for s in G.starts(s):
            if vis[s]: continue
            stack.append(s)
            while stack:
                if vis[u := stack.pop()] == 0:
                    stack.append(u)
                    vis[u] = 1
                    for i in G.range(u):
                        if vis[v := Va[i]] == 1:
                            if u != v and ((j := back[u]) == -1 or abs(Ea[j]-Ea[i]) == M): continue
                            I = u32a(1,i)
                            while v != u:
                                I.append(i := back[u])
                                u = Ua[i]
                            return I[::-1]
                        elif vis[v] == 0:
                            back[v] = i
                            stack.append(v)
                else:
                    vis[u] = 2
    
    def find_cycle(G, s: Union[int, None] = None):
        if I := G.find_cycle_indices(s): return [G.Ua[i] for i in I]
    
    def find_cycle_edge_ids(G, s: Union[int, None] = None):
        if I := G.find_cycle_indices(s): return [G.Ea[i] for i in I]

    def find_minimal_cycle(G, s=0):
        D, par, que, Va = u64a(N := G.N, inft), i32a(N, -1), deque([s]), G.Va
        D[s] = 0
        while que:
            for i in G.range(u := que.popleft()):
                if (v := Va[i]) == s:  # Found cycle back to start
                    cycle = [u]
                    while u != s: cycle.append(u := par[u])
                    return cycle
                if D[v] < inft: continue
                D[v], par[v] = D[u]+1, u
                que.append(v)

    def dfs_discovery(G, s: Union[int,list[int],None] = None, include_roots = False):
        '''Returns lists U and V representing U[i] -> V[i] edges in order of top down discovery'''
        Va, vis, stack, order = G.Va, [False]*(N := G.N), elist(N), elist(N)
        for s in G.starts(s):
            if vis[s]: continue
            if include_roots: order.append(-s-1)
            vis[s] = True
            stack.append(s)
            while stack:
                for i in G.range(stack.pop()):
                    if vis[v := Va[i]]: continue
                    vis[v] = True
                    order.append(i), stack.append(v)
        return order

    def dfs(G, s: Union[int,list] = None, /, connect_roots = False, backtrack = False, max_depth = None, enter_fn: Callable[[int],None] = None, leave_fn: Callable[[int],None] = None, max_depth_fn: Callable[[int],None] = None, down_fn: Callable[[int,int],None] = None, back_fn: Callable[[int,int],None] = None, cross_fn: Callable[[int,int],None] = None, up_fn: Callable[[int,int],None] = None):
        Va, La, Ra, I = G.Va, G.La, G.Ra, G.La[:]
        state, stack = u8a(G.N), elist(G.N if max_depth is None else max_depth+1)
        for s in G.starts(s):
            if state[s]: continue
            stack.append(s)
            if connect_roots and down_fn: down_fn(-1,s)
            while stack:
                if state[u := stack[-1]] == 0:
                    state[u] = 1
                    if enter_fn: enter_fn(u)
                    if max_depth is not None and len(stack) > max_depth:
                        I[u] = Ra[u]
                        if max_depth_fn: max_depth_fn(u)
                if (i := I[u]) < Ra[u]:
                    I[u] += 1
                    if (s := state[v := Va[i]]) == 0:
                        stack.append(v)
                        if down_fn: down_fn(u,v)
                    elif back_fn and s == 1: back_fn(u,v)
                    elif cross_fn and s == 2: cross_fn(u,v)
                else:
                    stack.pop()
                    state[u] = 2
                    if backtrack: state[u], I[u] = 0, La[u]
                    if leave_fn: leave_fn(u)
                    if up_fn and stack: up_fn(u, stack[-1])
            if connect_roots and up_fn: up_fn(s, -1)
    
    def dfs_enter_leave(G, s: Union[int,list[int],None] = None) -> tuple[list[int],list[int]]:
        '''Returns lists U and V representing U[i] -> V[i] edges in order of top down discovery'''
        N, Ra, Va, I = G.N, G.Ra, G.Va, G.La[:]
        stack, order, events, par = elist(N), elist(2*N), elist(2*N), i32a(N, -1)
        G.par, ENTER, LEAVE = par, int(DFSEvent.ENTER), int(DFSEvent.LEAVE)
        for s in G.starts(s):
            if par[s] >= 0: continue
            par[s] = s
            order.append(s), events.append(ENTER), stack.append(s)
            while stack:
                if (i := I[u := stack[-1]]) < Ra[u]:
                    I[u] += 1
                    if par[v := Va[i]] >= 0: continue
                    par[v] = u
                    order.append(v), events.append(ENTER), stack.append(v)
                else:
                    order.append(u), events.append(LEAVE), stack.pop()
        return events, order
    
    def is_bipartite(G):
        Va, que, color = G.Va, deque(), u8a(N := G.N)                
        for s in range(N):
            if color[s]: continue
            color[s] = 1
            que.append(s)
            while que:
                for i in G.range(u := que.popleft()):
                    if color[v := Va[i]] == 0:
                        color[v] = color[u] ^ 2
                        que.append(v)
                    elif color[v] == color[u]: return False
        return True
    
    def starts(G, s: Union[int,list[int],None]) -> list[int]:
        if isinstance(s, int): return [s]
        elif s is None: return range(G.N)
        elif isinstance(s, list): return s
        else: return list(s)

    @classmethod
    def compile(cls, N: int, M: int, shift: int = -1):
        def parse(ts: TokenStream):
            U, V = u32a(M), u32a(M)
            stream = ts.stream
            for i in range(M):
                u, v = map(int, stream.readline().split())
                U[i], V[i] = u+shift, v+shift
            return cls(N, U, V)
        return parse
    
from cp_library.ds.elist_fn import elist
from cp_library.ds.fill_fn import u8a, u32a, i32a, u64a
from cp_library.math.inft_cnst import inft