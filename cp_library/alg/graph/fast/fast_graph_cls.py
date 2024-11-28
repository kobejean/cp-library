import cp_library.alg.graph.fast.__header__

from typing import Sequence
from cp_library.io.parser_cls import Parsable, TokenStream
from cp_library.ds.fill_fn import fill_i32, fill_u32, fill_u64

def argsort(A: list[int]):
    N = len(A)
    mask = (1 << (shift := N.bit_length())) - 1
    indices = [0]*N
    for i in range(N):
        indices[i] = A[i] << shift | i
    indices.sort()
    for i in range(N):
        indices[i] &= mask
    return indices


class StaticDiGraphWeighted(Sequence, Parsable):
    def __init__(G, N: int, U: list, V: list, W: list):
        M = len(U)
        deg, Ei, adj, Wadj = fill_u32(N), fill_u32(M), fill_u32(M), [0]*M

        for u in U:
            deg[u] += 1
            

        L, idx = fill_u32(N), 0
        for u in range(N): 
            L[u], idx = idx, idx + deg[u]
        R = L[:]

        # place edge data using R to track
        for e in range(M):
            i = R[u := U[e]]
            adj[i], Wadj[i], Ei[i] = V[e], W[e], e
            R[u] += 1
        G.N, G.M, G.L, G.R, G.adj, G.Wadj, G.Ei = N, M, L, R, adj, Wadj, Ei
        G.U, G.V, G.W = U, V, W

    def __len__(G) -> int:
        return G.N
    
    def __getitem__(G, v):
        l,r = G.L[v],G.R[v]
        return zip(G.adj[l:r], G.W[l:r])

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
    
from cp_library.ds.elist_fn import elist
from cp_library.ds.priority_queue_cls import PriorityQueue
from cp_library.math.inft_cnst import inft