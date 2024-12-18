import cp_library.alg.graph.fast.__header__
from cp_library.alg.graph.fast.graph_weighted_base_cls import GraphWeightedBase

class DiGraphWeighted(GraphWeightedBase):
    def __init__(G, N: int, U: list[int], V: list[int], W: list[int]):
        M = len(U)
        deg, Ea, Ua, Va, Wa = fill_u32(N), fill_u32(M), fill_u32(M), fill_u32(M), [0]*M
        for u in U: deg[u] += 1
        La, i = fill_u32(N), 0
        for u in range(N): La[u], i = i, i+deg[u]
        Ra = La[:]
        for e in range(M):
            i = Ra[u := U[e]]
            Ua[i], Va[i], Wa[i], Ea[i] = U[e], V[e], W[e], e
            Ra[u] += 1
        super().__init__(N, M, U, V, W, deg, La, Ra, Ua, Va, Wa, Ea)

from cp_library.ds.fill_fn import fill_u32