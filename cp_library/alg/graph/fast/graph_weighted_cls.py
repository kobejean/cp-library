import cp_library.alg.graph.fast.__header__
from cp_library.alg.graph.fast.graph_weighted_base_cls import GraphWeightedBase

class GraphWeighted(GraphWeightedBase):
    def __init__(G, N: int, U: list[int], V: list[int], W: list[int]):
        M2 = (M := len(U)) << 1
        deg, Ea, Ua, Va, Wa = u32a(N), u32a(M2), u32a(M2), u32a(M2), [0]*M2
        
        for u in U:
            deg[u] += 1
        for v in V:
            deg[v] += 1
            
        La, idx = u32a(N), 0
        for u in range(N): 
            La[u], idx = idx, idx + deg[u]
        Ra = La[:]

        # place edge data using R to track
        for e in range(M):
            u, v, w = U[e], V[e], W[e]
            i, j = Ra[u], Ra[v]
            Ua[i], Va[i], Wa[i], Ea[i] = u, v, w, e
            Ra[u] += 1
            Ua[j], Va[j], Wa[j], Ea[j] = v, u, w, M+e
            Ra[v] += 1

        super().__init__(N, M, U, V, W, deg, La, Ra, Ua, Va, Wa, Ea)

from cp_library.ds.fill_fn import u32a
