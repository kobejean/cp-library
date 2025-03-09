import cp_library.alg.graph.fast.__header__
from cp_library.alg.graph.fast.graph_weighted_base_cls import GraphWeightedBase

class GraphWeighted(GraphWeightedBase):
    def __init__(G, N: int, U: list[int], V: list[int], W: list[int]):
        Ma, deg = 0, u32f(N)
        for e in range(M := len(U)):
            distinct = (u := U[e]) != (v := V[e])
            deg[u] += 1; deg[v] += distinct; Ma += 1+distinct
        Ea, Ua, Va, Wa = u32f(Ma), u32f(Ma), u32f(Ma), [0]*Ma
        
        La, i = u32f(N), 0
        for u,d in enumerate(deg): 
            La[u], i = i, i + d
        Ra = La[:]

        for e in range(M):
            u, v, w = U[e], V[e], W[e]
            i, j = Ra[u], Ra[v]
            Ra[u],Ua[i],Va[i],Wa[i],Ea[i] = i+1,u,v,w,e
            if i == j: continue # don't add self loops twice
            Ra[v],Ua[j],Va[j],Wa[j],Ea[j] = j+1,v,u,w,e

        super().__init__(N, M, U, V, W, deg, La, Ra, Ua, Va, Wa, Ea)

from cp_library.ds.array_init_fn import u32f, i32f
