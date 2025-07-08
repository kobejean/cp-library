import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
from cp_library.alg.graph.csr.graph_weighted_base_cls import GraphWeightedBase

class GraphWeighted(GraphWeightedBase):
    def __init__(G, N: int, U: list[int], V: list[int], W: list[int]):
        Ma, deg = 0, u32f(N)
        for e in range(M := len(U)):
            distinct = (u := U[e]) != (v := V[e])
            deg[u] += 1; deg[v] += distinct; Ma += 1+distinct
        twin, Ea, Ua, Va, Wa = u32f(Ma), u32f(Ma), u32f(Ma), u32f(Ma), [0]*Ma
        
        La, i = u32f(N), 0
        for u,d in enumerate(deg): 
            La[u], i = i, i + d
        Ra = La[:]

        for e in range(M):
            u, v, w = U[e], V[e], W[e]
            i, j = Ra[u], Ra[v]
            Ra[u],Ua[i],Va[i],Wa[i],Ea[i],twin[i] = i+1,u,v,w,e,j
            if i == j: continue # don't add self loops twice
            Ra[v],Ua[j],Va[j],Wa[j],Ea[j],twin[j] = j+1,v,u,w,e,i

        super().__init__(N, M, U, V, W, deg, La, Ra, Ua, Va, Wa, Ea, twin)
from cp_library.ds.array.u32f_fn import u32f
