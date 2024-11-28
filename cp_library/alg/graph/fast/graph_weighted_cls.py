import cp_library.alg.graph.fast.__header__

from typing import Sequence
from cp_library.io.parser_cls import Parsable, TokenStream
from cp_library.alg.iter.argsort_fn import argsort

class GraphWeighted(Sequence, Parsable):
    def __init__(G, N: int, U: list, V: list, W: list):
        M = len(U)
        M2 = M << 1
        deg, Ei, adj, Wadj = fill_u32(N), fill_u32(M2), fill_u32(M2), [0]*M2
        
        for u in U:
            deg[u] += 1
        for v in V:
            deg[v] += 1
            
        L, idx = fill_u32(N), 0
        for u in range(N): 
            L[u], idx = idx, idx + deg[u]
        R = L[:]

        # place edge data using R to track
        for e in range(M):
            u, v, w = U[e], V[e], W[e]
            i, j = R[u], R[v]
            adj[i], Wadj[i], Ei[i] = v, w, e
            R[u] += 1
            adj[j], Wadj[j], Ei[j] = u, w, M+e
            R[v] += 1
        G.N, G.M, G.L, G.R, G.adj, G.Wadj, G.Ei = N, M, L, R, adj, Wadj, Ei
        G.U, G.V, G.W = U, V, W

    def __len__(G) -> int:
        return G.N
    
    def __getitem__(G, v):
        l,r = G.L[v],G.R[v]
        return zip(G.adj[l:r], G.W[l:r])
    
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

    def dijkstra(G, s: int, t: int = None):
        N, L, R, adj, Wadj, Ei = G.N, G.L, G.R, G.adj, G.Wadj, G.Ei
        G.down = down = fill_i32(N, -1)
        G.par = par = fill_i32(N, -1)
        G.D = D = fill_u64(N, inft)
        D[s] = 0
            
        que = PriorityQueue(N)
        que.push(s, 0)
        
        while que:
            v, d = que.pop()
            if v == t: break
            if d > D[v]: continue
            for i in range(L[v], R[v]):
                c, w = adj[i], Wadj[i], 
                if (nd := d + w) < D[c]:
                    D[c], par[c], down[c] = nd, v, Ei[i]
                    que.push(c, nd)
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

    @classmethod
    def compile(cls, N: int, M: int, shift: int = -1):
        def parse(ts: TokenStream):
            U, V, W = fill_u32(M), fill_u32(M), [0]*M
            stream = ts.stream
            for i in range(M):
                u, v, W[i] = map(int, stream.readline().split())
                U[i], V[i] = u-shift, v-shift
            return cls(N, U, V, W)
        return parse
    
from cp_library.ds.dsu_cls import DSU
from cp_library.ds.elist_fn import elist
from cp_library.ds.priority_queue_cls import PriorityQueue
from cp_library.ds.fill_fn import fill_i32, fill_u32, fill_u64
from cp_library.math.inft_cnst import inft
