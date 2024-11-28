import cp_library.alg.graph.fast.__header__

from typing import Sequence
from cp_library.io.parser_cls import Parsable, TokenStream

class StaticDiGraphWeighted(Sequence, Parsable):
    def __init__(G, N: int, U: list, V: list, W: list):
        M = len(U)
        deg, adj, Wadj = [0]*N, [0]*M, [0]*M

        for u in U:
            deg[u] += 1

        L, idx = [0]*N, 0
        for u in range(N):
            L[u], idx = idx, idx + deg[u]
        R = L[:]

        for eid in range(M):
            u, v, w = U[eid], V[eid], W[eid]
            adj[r], Wadj[r], R[u] = v, w, (r := R[u])+1
        G.N, G.M, G.adj, G.Wadj, G.deg = N, M, adj, Wadj, deg
        G.L, G.R = L, R 

    def __len__(G) -> int:
        return G.N
    
    def __getitem__(G, v):
        l,r = G.L[v],G.R[v]
        return zip(G.adj[l:r], G.Wadj[l:r])

    def dijkstra(G, s: int, t: int):
        N, adj, Wadj = G.N, G.adj, G.Wadj
        L, R = G.L, G.R
        G.par = par = [-1] * N
        G.D = D = [inft] * N
        D[s] = 0
        
        que = PriorityQueue(N)
        que.push(s, 0)

        def expand(i,d):
            for i in range(L[v],R[v]):
                c, w = adj[i], Wadj[i]
                if (nd := d + w) < D[c]:
                    D[c], par[c] = nd, v
                    que.push(c, nd)
        
        while que:
            v, d = que.pop()
            if v == t: break
            if d > D[v]: continue
            expand(v,d)
        return D
        
    def shortest_path(G, s: int, t: int):
        D = G.dijkstra(s, t)
        if D[t] == inft: return None
        par = G.par
            
        path = elist(G.N)
        path.append(t)
        v = t
        while v != s:
            path.append(v := par[v])
        return path[::-1]
    
    def shortest_path_edge_ids(G, s: int, t: int):
        D = G.dijkstra(s, t)
        if D[t] == inft: return None
        par, par_ei = G.par, G.par_ei
            
        path = elist(G.N)
        v = t
        while v != s:
            path.append(par_ei[v])
            v = par[v] 
        return path[::-1]
    
    @classmethod
    def compile(cls, N: int, M: int, shift: int = -1):
        def parse(ts: TokenStream):
            U, V, W = [0]*M, [0]*M, [0]*M
            for i in range(M):
                U[i], V[i], W[i] = map(int, ts.line())
                U[i] += shift
                V[i] += shift
            return cls(N, U, V, W)
        return parse
    
from cp_library.ds.elist_fn import elist
from cp_library.ds.priority_queue_cls import PriorityQueue
from cp_library.math.inft_cnst import inft