import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
from cp_library.alg.graph.csr.graph_weighted_base_cls import GraphWeightedBase

class GraphPotential(GraphWeightedBase):
    def __init__(G, N: int, U: list[int], V: list[int], W: list[int]):
        deg, Ea, Ua, Va, Wa, La, i = u32f(N), u32f(M2 := len(U)*2), u32f(M2), u32f(M2), [0]*M2, u32f(N), 0
        for e, u in enumerate(U): deg[u] += 1; deg[V[e]] += 1
        for u, d in enumerate(deg): La[u], i = i, i+d
        Ra = La.__copy__()
        for e, u in enumerate(U): Ua[i], Va[i], Wa[i], Ea[i], Ra[u] = U[e], V[e], W[e], e, (i := Ra[u])+1
        for e, v in enumerate(V): Ua[i], Va[i], Wa[i], Ea[i], Ra[v] = V[e], U[e], -W[e], e, (i := Ra[v])+1
        super().__init__(N, M2>>1, U, V, W, deg, La, Ra, Ua, Va, Wa, Ea)
from cp_library.ds.array.u32f_fn import u32f