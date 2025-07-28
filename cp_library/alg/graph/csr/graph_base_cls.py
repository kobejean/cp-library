from cp_library.ds.view.view_cls import view
import cp_library.__header__
from math import inf
from typing import Callable, Sequence, Union, overload
from cp_library.io.parsable_cls import Parsable
import cp_library.alg.__header__
from cp_library.alg.dp.chmin_fn import chmin
import cp_library.alg.graph.__header__
from cp_library.alg.graph.dfs_options_cls import DFSEvent

class GraphBase(Parsable):
    def __init__(G, N: int, M: int, U: list[int], V: list[int], 
                 deg: list[int], La: list[int], Ra: list[int],
                 Ua: list[int], Va: list[int], Ea: list[int], twin: list[int] = None):
        G.N = N
        '''The number of vertices.'''
        G.M = M
        '''The number of edges.'''
        G.U = U
        '''A list of source vertices in the original edge list.'''
        G.V = V
        '''A list of destination vertices in the original edge list.'''
        G.deg = deg
        '''deg[u] is the out degree of vertex u.'''
        G.La = La
        '''La[u] stores the start index of the list of adjacent vertices from u.'''
        G.Ra = Ra
        '''Ra[u] stores the stop index of the list of adjacent vertices from u.'''
        G.Ua = Ua
        '''Ua[i] = u for La[u] <= i < Ra[u], useful for backtracking.'''
        G.Va = Va
        '''Va[i] lists adjacent vertices to u for La[u] <= i < Ra[u].'''
        G.Ea = Ea
        '''Ea[i] lists the edge ids that start from u for La[u] <= i < Ra[u].
        For undirected graphs, edge ids in range M<= e <2*M are edges from V[e-M] -> U[e-M].
        '''
        G.twin = twin if twin is not None else range(len(Ua))
        '''twin[i] in undirected graphs stores index j of the same edge but with u and v swapped.'''
        G.st: list[int] = None
        G.order: list[int] = None
        G.vis: list[int] = None
        G.back: list[int] = None
        G.tin: list[int] = None
    
    def clear(G):
        G.vis = G.back = G.tin = None

    def prep_vis(G):
        if G.vis is None: G.vis = u8f(G.N)
        return G.vis
    
    def prep_st(G):
        if G.st is None: G.st = elist(G.N)
        else: G.st.clear()
        return G.st
    
    def prep_order(G):
        if G.order is None: G.order = elist(G.N)
        else: G.order.clear()
        return G.order
    
    def prep_back(G):
        if G.back is None: G.back = i32f(G.N, -2)
        return G.back
    
    def prep_tin(G):
        if G.tin is None: G.tin = i32f(G.N, -1)
        return G.tin
    
    def _remove(G, a: int):
        G.deg[u := G.Ua[a]] -= 1
        G.Ra[u] = (r := G.Ra[u]-1)
        G.Ua[a], G.Va[a], G.Ea[a] = G.Ua[r], G.Va[r], G.Ea[r]
        G.twin[a], G.twin[r] = G.twin[r], G.twin[a]
        G.twin[G.twin[a]] = a
        G.twin[G.twin[r]] = r

    def remove(G, a: int):
        b = G.twin[a]; G._remove(a)
        if a != b: G._remove(b)

    def __len__(G) -> int: return G.N
    def __getitem__(G, u): return view(G.Va, G.La[u], G.Ra[u])
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

    def recover_path(G, s, t):
        Ua, back, vertices = G.Ua, G.back, u32f(1, v := t)
        while v != s: vertices.append(v := Ua[back[v]])
        return vertices
    
    def recover_path_edge_ids(G, s, t):
        Ea, Ua, back, edges, v = G.Ea, G.Ua, G.back, u32f(0), t
        while v != s: edges.append(Ea[i := back[v]]), (v := Ua[i])
        return edges

    def shortest_path(G, s: int, t: int):
        if G.distance(s, t) >= inf: return None
        vertices = G.recover_path(s, t)
        vertices.reverse()
        return vertices
    
    def shortest_path_edge_ids(G, s: int, t: int):
        if G.distance(s, t) >= inf: return None
        edges = G.recover_path_edge_ids(s, t)
        edges.reverse()
        return edges
    
    @overload
    def bfs(G, s: Union[int,list] = 0) -> list[int]: ...
    @overload
    def bfs(G, s: Union[int,list], g: int) -> int: ...
    def bfs(G, s: int = 0, g: int = None):
        S, Va, back, D = G.starts(s), G.Va, i32f(N := G.N, -1), [inf]*N
        G.back, G.D = back, D
        for u in S: D[u] = 0
        que = Que(S)
        while que:
            nd = D[u := que.pop()]+1
            if u == g: return nd-1
            for i in G.range(u):
                if chmin(D, v := Va[i], nd): back[v] = i; que.push(v)
        return D if g is None else inf 

    def floyd_warshall(G) -> list[list[int]]:
        G.D = D = [[inf]*G.N for _ in range(G.N)]
        for u in range(G.N): D[u][u] = 0
        for i in range(len(G.Ua)): D[G.Ua[i]][G.Va[i]] = 1
        for k, Dk in enumerate(D):
            for Di in D:
                if (Dik := Di[k]) == inf: continue
                for j in range(G.N):
                    chmin(Di, j, Dik+Dk[j])
        return D

    def find_cycle_indices(G, s: Union[int, None] = None):
        Ea, Ua, Va, vis, back = G.Ea, G. Ua, G.Va, u8f(N := G.N), u32f(N, i32_max)
        G.vis, G.back, st = vis, back, elist(N)
        for s in G.starts(s):
            if vis[s]: continue
            st.append(s)
            while st:
                if not vis[u := st.pop()]:
                    st.append(u)
                    vis[u], pe = 1, Ea[j] if (j := back[u]) != i32_max else i32_max
                    for i in G.range(u):
                        if not vis[v := Va[i]]:
                            back[v] = i
                            st.append(v)
                        elif vis[v] == 1 and pe != Ea[i]:
                            I = u32f(1,i)
                            while v != u: I.append(i := back[u]), (u := Ua[i])
                            I.reverse()
                            return I
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
        D, par, que, Va = u32f(N := G.N, u32_max), i32f(N, -1), Que([s]), G.Va
        D[s] = 0
        while que:
            for i in G.range(u := que.pop()):
                if (v := Va[i]) == s:  # Found cycle back to start
                    cycle = [u]
                    while u != s: cycle.append(u := par[u])
                    return cycle
                if D[v] < u32_max: continue
                D[v], par[v] = D[u]+1, u; que.push(v)

    def dfs_topo(G, s: Union[int,list] = None) -> list[int]:
        '''Returns lists of indices i where Ua[i] -> Va[i] are edges in order of top down discovery'''
        vis, st, order = G.prep_vis(), G.prep_st(), G.prep_order()
        for s in G.starts(s):
            if vis[s]: continue
            vis[s] = 1; st.append(s) 
            while st:
                for i in G.range(st.pop()):
                    if vis[v := G.Va[i]]: continue
                    vis[v] = 1; order.append(i); st.append(v)
        return order

    def dfs(G, s: Union[int,list] = None, /, 
            backtrack = False,
            max_depth = None,
            enter_fn: Callable[[int],None] = None,
            leave_fn: Callable[[int],None] = None,
            max_depth_fn: Callable[[int],None] = None,
            down_fn: Callable[[int,int,int],None] = None,
            back_fn: Callable[[int,int,int],None] = None,
            forward_fn: Callable[[int,int,int],None] = None,
            cross_fn: Callable[[int,int,int],None] = None,
            up_fn: Callable[[int,int,int],None] = None):
        I, time, vis, st, back, tin = G.La[:], -1, G.prep_vis(), G.prep_st(), G.prep_back(), G.prep_tin()
        for s in G.starts(s):
            if vis[s]: continue
            back[s], tin[s] = -1, (time := time+1); st.append(s)
            while st:
                if vis[u := st[-1]] == 0:
                    vis[u] = 1
                    if enter_fn: enter_fn(u)
                    if max_depth is not None and len(st) > max_depth:
                        I[u] = G.Ra[u]
                        if max_depth_fn: max_depth_fn(u)
                if (i := I[u]) < G.Ra[u]:
                    I[u] += 1
                    if (s := vis[v := G.Va[i]]) == 0:
                        back[v], tin[v] = i, (time := time+1); st.append(v)
                        if down_fn: down_fn(u,v,i)
                    elif back_fn and s == 1 and back[u] != G.twin[i]: back_fn(u,v,i)
                    elif (cross_fn or forward_fn) and s == 2:
                        if forward_fn and tin[u] < tin[v]: forward_fn(u,v,i)
                        elif cross_fn: cross_fn(u,v,i)
                else:
                    vis[u] = 2; st.pop()
                    if backtrack: vis[u], I[u] = 0, G.La[u]
                    if leave_fn: leave_fn(u)
                    if up_fn and st: up_fn(u, st[-1], back[u])
    
    def dfs_enter_leave(G, s: Union[int,list[int],None] = None) -> Sequence[tuple[DFSEvent,int]]:
        N, I = G.N, G.La[:]
        st, back, plst = elist(N), i32f(N,-2), PacketList(order := elist(2*N), N-1)
        G.back, ENTER, LEAVE = back, int(DFSEvent.ENTER) << plst.shift, int(DFSEvent.LEAVE) << plst.shift
        for s in G.starts(s):
            if back[s] >= -1: continue
            back[s] = -1
            order.append(ENTER | s), st.append(s)
            while st:
                if (i := I[u := st[-1]]) < G.Ra[u]:
                    I[u] += 1
                    if back[v := G.Va[i]] >= -1: continue
                    back[v] = i; order.append(ENTER | v); st.append(v)
                else:
                    order.append(LEAVE | u); st.pop()
        return plst
    
    def starts(G, s: Union[int,list[int],None] = None) -> list[int]:
        if isinstance(s, int): return [s]
        elif s is None: return range(G.N)
        elif isinstance(s, list): return s
        else: return list(s)

    @classmethod
    def compile(cls, N: int, M: int, shift: int = -1):
        def parse(io: IOBase):
            U, V = u32f(M), u32f(M)
            for i in range(M): u, v = io.readints(); U[i], V[i] = u+shift, v+shift
            return cls(N, U, V)
        return parse
from cp_library.bit.masks.u32_max_cnst import u32_max
from cp_library.bit.masks.i32_max_cnst import i32_max
from cp_library.ds.array.u8f_fn import u8f
from cp_library.ds.array.u32f_fn import u32f
from cp_library.ds.array.i32f_fn import i32f
from cp_library.ds.list.elist_fn import elist
from cp_library.ds.packet_list_cls import PacketList
from cp_library.ds.que.que_cls import Que
from cp_library.io.io_base_cls import IOBase