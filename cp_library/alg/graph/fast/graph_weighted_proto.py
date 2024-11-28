from math import inf
import cp_library.alg.graph.__header__

from typing import overload
from heapq import heapify, heappop, heappush
import operator
from typing import Sequence
from cp_library.io.parser_cls import Parsable, TokenStream
from cp_library.alg.iter.argsort_fn import argsort
from cp_library.alg.graph.dfs_options_cls import DFSEvent, DFSFlags
from cp_library.alg.graph.fast.graph_proto import GraphProtocol

class GraphWeightedProtocol(GraphProtocol):
    
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

    def __len__(G) -> int:
        return G.N
    
    def __getitem__(G, v):
        l,r = G.La[v],G.Ra[v]
        return zip(G.Va[l:r], G.Wa[l:r])

    def dijkstra(G, s: int, t: int = None):
        N, La, Ra, Va, Wa, Ea = G.N, G.La, G.Ra, G.Va, G.Wa, G.Ea
        G.down = down = fill_i32(N, -1)
        G.par = par = fill_i32(N, -1)
        G.D = D = fill_u64(N, inft)
        D[s] = 0
            
        que = PriorityQueue(N)
        que.push(s, 0)
        
        while que:
            u, d = que.pop()
            if u == t: break
            if d > D[u]: continue
            for i in range(La[u], Ra[u]):
                v, w = Va[i], Wa[i], 
                if (nd := d + w) < D[v]:
                    D[v], par[v], down[v] = nd, u, Ea[i]
                    que.push(v, nd)
        return D

    def shortest_path(G, s: int, t: int):
        D = G.dijkstra(s, t)
        if D[t] == inft: return None
        par = G.par
            
        path = fill_u32(0)
        path.append(t)
        v = t
        while v != s:
            path.append(v := par[v])
        return path[::-1]
    
    def shortest_path_edge_ids(G, s: int, t: int):
        D = G.dijkstra(s, t)
        if D[t] == inft: return None
        par, down = G.par, G.down
            
        path = elist(G.N)
        v = t
        while v != s:
            path.append(down[v])
            v = par[v] 
        return path[::-1]

    def kruskal(G):
        N, U, V, W = G.N, G.U, G.V, G.W 
        dsu = DSU(N)
        MST = [0]*(N-1)
        need = N-1
        for e in argsort(W):
            u, v = dsu.merge(U[e],V[e],True)
            if u != v:
                need -= 1
                MST[need] = e
                if not need: break
        return None if need else MST
    
    def kruskal_heap(G):
        N, M, U, V, W = G.N, G.M, G.U, G.V, G.W 
        que = PriorityQueue(M, list(range(M)), W)
        dsu = DSU(N)
        MST = [0]*(N-1)
        need = N-1
        while que and need:
            e, _ = que.pop()
            u, v = dsu.merge(U[e],V[e],True)
            if u != v:
                MST[need := need-1] = e
        return None if need else MST
   
    def bellman_ford(G, s: int = 0) -> list[int]:
        N, M = G.N, G.M
        Ua, Va, Wa = G.Ua, G.Va, G.Wa
        D = [inft]*N
        D[s] = 0
        for _ in range(N-1):
            for i in range(M):
                u,v,w = Ua[i], Va[i], Wa[i]
                if D[u] == inft: continue
                D[v] = min(D[v], D[u] + w)
        return D
    
    def bellman_ford_neg_cyc_check(G, s: int = 0) -> tuple[bool, list[int]]:
        from cp_library.alg.graph.bellman_ford_fn import bellman_ford
        D = G.bellman_ford(s)
        M, U, V, W = G.M, G.U, G.V, G.W
        neg_cycle = any(D[U[i]]+W[i]<D[V[i]] for i in range(M) if D[U[i]] < inft)
        return neg_cycle, D
    
    def floyd_warshall(G) -> list[list[int]]:
        N, M = G.N, G.M
        Ua, Va, Wa = G.Ua, G.Va, G.Wa
        D = [[inft]*N for _ in range(N)]

        for u in range(N):
            D[u][u] = 0

        for i in range(M):
            u,v,w = Ua[i], Va[i], Wa[i]
            D[u][v] = min(D[u][v], w)
        
        for k, Dk in enumerate(D):
            for Di in D:
                if Di[k] == inft: continue
                for j in range(N):
                    if Dk[j] == inft: continue
                    Di[j] = min(Di[j], Di[k]+Dk[j])
        return D
        
    def floyd_warshall_neg_cyc_check(G):
        D = G.floyd_warshall()
        return any(D[i][i] < 0 for i in range(G.N)), D
    
from cp_library.ds.dsu_cls import DSU
from cp_library.ds.elist_fn import elist
from cp_library.ds.fill_fn import fill_i32, fill_u32, fill_u64
from cp_library.ds.priority_queue_cls import PriorityQueue
from cp_library.math.inft_cnst import inft