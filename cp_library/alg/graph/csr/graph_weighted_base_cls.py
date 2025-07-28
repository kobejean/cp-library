import cp_library.__header__
from math import inf
from typing import overload
import cp_library.alg.__header__
from cp_library.alg.dp.chmin_fn import chmin
from cp_library.alg.iter.arg.argsort_fn import argsort
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
from cp_library.alg.graph.csr.graph_base_cls import GraphBase

class GraphWeightedBase(GraphBase):
    def __init__(self, N: int, M: int, U: list[int], V: list[int], W: list[int], 
                 deg: list[int], La: list[int], Ra: list[int],
                 Ua: list[int], Va: list[int], Wa: list[int], Ea: list[int], twin: list[int] = None):
        super().__init__(N, M, U, V, deg, La, Ra, Ua, Va, Ea, twin)
        self.W = W
        self.Wa = Wa
        '''Wa[i] lists weights to edges from u for La[u] <= i < Ra[u].'''
        
    def _remove(G, a: int):
        G.deg[u := G.Ua[a]] -= 1
        G.Ra[u] = (r := G.Ra[u]-1)
        G.Ua[a], G.Va[a], G.Wa[a], G.Ea[a] = G.Ua[r], G.Va[r], G.Wa[r], G.Ea[r]
        G.twin[a], G.twin[r] = G.twin[r], G.twin[a]
        G.twin[G.twin[a]] = a
        G.twin[G.twin[r]] = r

    def __getitem__(G, u): return view2(G.Va, G.Wa, G.La[u],G.Ra[u])
    
    @overload
    def distance(G) -> list[list[int]]: ...
    @overload
    def distance(G, s: int = 0) -> list[int]: ...
    @overload
    def distance(G, s: int, g: int) -> int: ...
    def distance(G, s = None, g = None):
        if s == None: return G.floyd_warshall()
        else: return G.dijkstra(s, g)

    def dijkstra(G, s: int, t: int = None):
        G.back, G.D, S = i32f(G.N, -1), [inf]*G.N, G.starts(s)
        for s in S: G.D[s] = 0
        que = PriorityQueue(G.N, S)
        while que:
            d, u = que.pop()
            if d > G.D[u]: continue
            if u == t: return d
            i, r = G.La[u]-1, G.Ra[u]
            while (i:=i+1)<r: 
                if chmin(G.D, v := G.Va[i], nd := d + G.Wa[i]):
                    G.back[v] = i; que.push(nd, v)
        return G.D if t is None else inf 

    def kruskal(G):
        U, V, W, dsu, MST, need = G.U, G.V, G.W, DSU(N := G.N), [0]*(N-1), N-1
        for e in argsort(W):
            u, v = dsu.merge(U[e],V[e])
            if u != v:
                MST[need := need-1] = e
                if not need: break
        return None if need else MST
    
    def kruskal_heap(G):
        N, M, U, V, W = G.N, G.M, G.U, G.V, G.W 
        que, dsu, MST = PriorityQueue(M, list(range(M)), W), DSU(N), [0]*(need := N-1)
        while que and need:
            _, e = que.pop()
            u, v = dsu.merge(U[e],V[e])
            if u != v:
                MST[need := need-1] = e
        return None if need else MST
   
    def bellman_ford(G, s: int = 0) -> list[int]:
        Ua, Va, Wa, D = G.Ua, G.Va, G.Wa, [inf]*(N := G.N)
        D[s] = 0
        for _ in range(N-1):
            for i, u in enumerate(Ua):
                if D[u] < inf: chmin(D, Va[i], D[u] + Wa[i])
        return D
    
    def bellman_ford_neg_cyc_check(G, s: int = 0) -> tuple[bool, list[int]]:
        M, U, V, W, D = G.M, G.U, G.V, G.W, G.bellman_ford(s)
        neg_cycle = any(D[U[i]]+W[i]<D[V[i]] for i in range(M) if D[U[i]] < inf)
        return neg_cycle, D
    
    def floyd_warshall(G) -> list[list[int]]:
        N, Ua, Va, Wa = G.N, G.Ua, G.Va, G.Wa
        D = [[inf]*N for _ in range(N)]
        for u in range(N): D[u][u] = 0
        for i in range(len(Ua)): chmin(D[Ua[i]], Va[i], Wa[i])
        for k, Dk in enumerate(D):
            for Di in D:
                if Di[k] >= inf: continue
                for j in range(N):
                    if Dk[j] >= inf: continue
                    chmin(Di, j, Di[k]+Dk[j])
        return D
        
    def floyd_warshall_neg_cyc_check(G):
        D = G.floyd_warshall()
        return any(D[i][i] < 0 for i in range(G.N)), D
    
    @classmethod
    def compile(cls, N: int, M: int, shift: int = -1):
        def parse(io: IOBase):
            U, V, W = u32f(M), u32f(M), [0]*M
            for i in range(M):
                u, v, w = io.readints()
                U[i], V[i], W[i] = u+shift, v+shift, w
            return cls(N, U, V, W)
        return parse
from cp_library.ds.array.i32f_fn import i32f
from cp_library.ds.array.u32f_fn import u32f
from cp_library.ds.dsu_cls import DSU
from cp_library.ds.heap.priority_queue_cls import PriorityQueue
from cp_library.ds.view.view2_cls import view2
from cp_library.io.parser_cls import IOBase