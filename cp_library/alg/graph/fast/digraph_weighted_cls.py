import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.fast.__header__
from cp_library.alg.graph.fast.graph_weighted_base_cls import GraphWeightedBase

class DiGraphWeighted(GraphWeightedBase):
    def __init__(G, N: int, U: list[int], V: list[int], W: list[int]):
        deg, Ea, Ua, Va, Wa = u32f(N), u32f(M := len(U)), u32f(M), u32f(M), [0]*M
        for u in U: deg[u] += 1
        La, i = u32f(N), 0
        for u in range(N): La[u], i = i, i+deg[u]
        Ra = La[:]
        for e in range(M):
            i = Ra[u := U[e]]
            Ua[i], Va[i], Wa[i], Ea[i], Ra[u] = U[e], V[e], W[e], e, i+1
        super().__init__(N, M, U, V, W, deg, La, Ra, Ua, Va, Wa, Ea)

from cp_library.ds.array_init_fn import u32f