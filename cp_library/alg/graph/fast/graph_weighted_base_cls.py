import cp_library.alg.graph.__header__
from typing import overload
from cp_library.io.parser_cls import TokenStream
from cp_library.alg.iter.argsort_fn import argsort
from cp_library.alg.graph.fast.graph_base_cls import GraphBase

class GraphWeightedBase(GraphBase):
    def __init__(self, N: int, M: int, U: list[int], V: list[int], W: list[int], 
                 deg: list[int], La: list[int], Ra: list[int],
                 Ua: list[int], Va: list[int], Wa: list[int], Ea: list[int]):
        super().__init__(N, M, U, V, deg, La, Ra, Ua, Va, Ea)
        self.W = W
        self.Wa = Wa
        """Wa[i] lists weights to edges from u for La[u] <= i < Ra[u]."""
        
    def __getitem__(G, u):
        l,r = G.La[u],G.Ra[u]
        return zip(G.Va[l:r], G.Wa[l:r])
    
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

    def dijkstra(G, s: int, t: int = None):
        N, S, Va, Wa = G.N, G.starts(s), G.Va, G.Wa
        G.back = back = fill_i32(N, -1)
        G.D = D = fill_u64(N, inft)
        for s in S: D[s] = 0
        que = PriorityQueue(N, S)
        while que:
            u, d = que.pop()
            if d > D[u]: continue
            if u == t: return d
            for i in G.range(u): 
                if (nd := d + Wa[i]) < D[v := Va[i]]:
                    D[v], back[v] = nd, i
                    que.push(v, nd)
        return D if t is None else inft 

    def kruskal(G):
        N, U, V, W = G.N, G.U, G.V, G.W 
        dsu = DSU(N)
        MST = [0]*(N-1)
        need = N-1
        for e in argsort(W):
            u, v = dsu.merge(U[e],V[e],True)
            if u != v:
                MST[need := need-1] = e
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
        N, Ua, Va, Wa = G.N, G.Ua, G.Va, G.Wa
        D = [inft]*N
        D[s] = 0
        for _ in range(N-1):
            for i in range(len(Ua)):
                u,v,w = Ua[i], Va[i], Wa[i]
                if D[u] == inft: continue
                D[v] = min(D[v], D[u] + w)
        return D
    
    def bellman_ford_neg_cyc_check(G, s: int = 0) -> tuple[bool, list[int]]:
        D = G.bellman_ford(s)
        M, U, V, W = G.M, G.U, G.V, G.W
        neg_cycle = any(D[U[i]]+W[i]<D[V[i]] for i in range(M) if D[U[i]] < inft)
        return neg_cycle, D
    
    def floyd_warshall(G) -> list[list[int]]:
        N, Ua, Va, Wa = G.N, G.Ua, G.Va, G.Wa
        D = [[inft]*N for _ in range(N)]

        for u in range(N):
            D[u][u] = 0

        for i in range(len(Ua)):
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
    
    @classmethod
    def compile(cls, N: int, M: int, shift: int = -1):
        def parse(ts: TokenStream):
            U, V, W = fill_u32(M), fill_u32(M), [0]*M
            stream = ts.stream
            for i in range(M):
                u, v, W[i] = map(int, stream.readline().split())
                U[i], V[i] = u+shift, v+shift
            return cls(N, U, V, W)
        return parse

from cp_library.ds.dsu_cls import DSU
from cp_library.ds.elist_fn import elist
from cp_library.ds.fill_fn import fill_i32, fill_u32, fill_u64
from cp_library.ds.heap.priority_queue_cls import PriorityQueue
from cp_library.math.inft_cnst import inft