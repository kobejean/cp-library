import cp_library.alg.graph.__header__
from math import inf
from itertools import islice
from typing import Callable, Sequence, Union, overload
from collections import deque
from cp_library.io.parser_cls import Parsable, TokenStream
from cp_library.alg.graph.dfs_options_cls import DFSEvent

class GraphBase(Sequence, Parsable):
    def __init__(G, N: int, M: int, U: list[int], V: list[int], 
                 deg: list[int], La: list[int], Ra: list[int],
                 Ua: list[int], Va: list[int], Ea: list[int], self_loops = False):
        G.N = N
        """The number of vertices."""
        G.M = M
        """The number of edges."""
        G.U = U
        """A list of source vertices in the original edge list."""
        G.V = V
        """A list of destination vertices in the original edge list."""
        G.deg = deg
        """deg[u] is the out degree of vertex u."""
        G.La = La
        """La[u] stores the start index of the list of adjacent vertices from u."""
        G.Ra = Ra
        """Ra[u] stores the stop index of the list of adjacent vertices from u."""
        G.Ua = Ua
        """Ua[i] = u for La[u] <= i < Ra[u], useful for backtracking."""
        G.Va = Va
        """Va[i] lists adjacent vertices to u for La[u] <= i < Ra[u]."""
        G.Ea = Ea
        """Ea[i] lists the edge ids that start from u for La[u] <= i < Ra[u].
        For undirected graphs, edge ids in range M<= e <2*M are edges from V[e-M] -> U[e-M].
        """
        G.stack: list[int] = None
        G.order: list[int] = None
        G.vis: list[int] = None

    def __len__(G) -> int: return G.N
    def __getitem__(G, u): return islice(G.Va,G.La[u],G.Ra[u])
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
        if G.distance(s, t) >= inf: return None
        Ua, back, vertices = G.Ua, G.back, u32f(1, v := t)
        while v != s: vertices.append(v := Ua[back[v]])
        return vertices[::-1]
    
    def shortest_path_edge_ids(G, s: int, t: int):
        if G.distance(s, t) >= inf: return None
        Ea, Ua, back, edges, v = G.Ea, G.Ua, G.back, u32f(0), t
        while v != s: edges.append(Ea[i := back[v]]), (v := Ua[i])
        return edges[::-1]
    
    @overload
    def bfs(G, s: Union[int,list] = 0) -> list[int]: ...
    @overload
    def bfs(G, s: Union[int,list], g: int) -> int: ...
    def bfs(G, s: int = 0, g: int = None):
        S, Va, back, D = G.starts(s), G.Va, i32f(N := G.N, -1), [inf]*N
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
        return D if g is None else inf 

    def floyd_warshall(G) -> list[list[int]]:
        M, Ua, Va, N = G.M, G.Ua, G.Va, G.N
        G.D = D = [[inf]*N for _ in range(N)]
        for u in range(N): D[u][u] = 0
        for i in range(M): D[Ua[i]][Va[i]] = 1
        for k, Dk in enumerate(D):
            for Di in D:
                if Di[k] == inf: continue
                for j in range(N):
                    Di[j] = min(Di[j], Di[k]+Dk[j])
        return D

    def find_cycle_indices(G, s: Union[int, None] = None):
        M, Ea, Ua, Va, vis, back = G.M, G.Ea, G. Ua, G.Va, u8f(N := G.N), u32f(N, i32_max)
        G.vis, G.back, stack = vis, back, elist(N)
        for s in G.starts(s):
            if vis[s]: continue
            stack.append(s)
            while stack:
                if vis[u := stack.pop()] == 0:
                    stack.append(u)
                    vis[u], pe = 1, ~Ea[j] if (j := back[u]) != i32_max else i32_max
                    for i in G.range(u):
                        if vis[v := Va[i]] == 0:
                            back[v] = i
                            stack.append(v)
                        elif vis[v] == 1 and pe != Ea[i]:
                            I = u32f(1,i)
                            while v != u: I.append(i := back[u]), (u := Ua[i])
                            return I[::-1]
                else:
                    vis[u] = 2
        # check for self loops
        for i in range(len(Ua)):
            if Ua[i] == Va[i]:
                return u32f(1,i)
    
    def find_cycle(G, s: Union[int, None] = None):
        if I := G.find_cycle_indices(s): return [G.Ua[i] for i in I]
    
    def find_cycle_edge_ids(G, s: Union[int, None] = None):
        if I := G.find_cycle_indices(s): return [G.Ea[i] for i in I]

    def find_minimal_cycle(G, s=0):
        D, par, que, Va = u32f(N := G.N, u32_max), i32f(N, -1), deque([s]), G.Va
        D[s] = 0
        while que:
            for i in G.range(u := que.popleft()):
                if (v := Va[i]) == s:  # Found cycle back to start
                    cycle = [u]
                    while u != s: cycle.append(u := par[u])
                    return cycle
                if D[v] < u32_max: continue
                D[v], par[v] = D[u]+1, u
                que.append(v)

    def dfs_topdown(G, s: int) -> list[int]:
        '''Returns lists of indices i where Ua[i] -> Va[i] are edges in order of top down discovery'''
        G.vis, G.stack, G.order = vis, stack, order = u8f(N := G.N), G.stack or elist(N), G.order or elist(N)
        vis[s] = 1
        stack.append(s)
        while stack:
            for i in G.range(stack.pop()):
                if vis[v := G.Va[i]]: continue
                vis[v] = 1
                order.append(i), stack.append(v)
        return order

    def dfs(G, s: Union[int,list] = None, /, connect_roots = False, backtrack = False, max_depth = None, enter_fn: Callable[[int],None] = None, leave_fn: Callable[[int],None] = None, max_depth_fn: Callable[[int],None] = None, down_fn: Callable[[int,int],None] = None, back_fn: Callable[[int,int],None] = None, cross_fn: Callable[[int,int],None] = None, up_fn: Callable[[int,int],None] = None):
        Va, La, Ra, I = G.Va, G.La, G.Ra, G.La[:]
        G.state, G.stack = state, stack = u8f(G.N), elist(G.N if max_depth is None else max_depth+1)
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
    
    def dfs_enter_leave(G, s: Union[int,list[int],None] = None) -> Sequence[tuple[DFSEvent,int]]:
        N, Ra, Va, I = G.N, G.Ra, G.Va, G.La[:]
        stack, par, plist = elist(N), i32f(N,-1), PacketList(order := elist(2*N), N-1)
        G.par, ENTER, LEAVE = par, int(DFSEvent.ENTER) << plist.shift, int(DFSEvent.LEAVE) << plist.shift
        for s in G.starts(s):
            if par[s] >= 0: continue
            par[s] = s
            order.append(ENTER | s), stack.append(s)
            while stack:
                if (i := I[u := stack[-1]]) < Ra[u]:
                    I[u] += 1
                    if par[v := Va[i]] >= 0: continue
                    par[v] = u
                    order.append(ENTER | v), stack.append(v)
                else:
                    order.append(LEAVE | u), stack.pop()
        return PacketList(order, N-1)
    
    def is_bipartite(G):
        Va, que, color = G.Va, deque(), u8f(N := G.N)                
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
            U, V = u32f(M), u32f(M)
            stream = ts.stream
            for i in range(M):
                u, v = map(int, stream.readline().split())
                U[i], V[i] = u+shift, v+shift
            return cls(N, U, V)
        return parse
    
from cp_library.ds.elist_fn import elist
from cp_library.ds.array_init_fn import u8f, u32f, i32f, i64f, u32_max, i32_max
from cp_library.ds.packet_list_cls import PacketList