import cp_library.alg.graph.fast.__header__
from cp_library.alg.graph.fast.graph_base_cls import GraphBase

class Graph(GraphBase):
    def __init__(G, N: int, U: list[int], V: list[int]):
        M2 = (M := len(U)) << 1
        deg, Ea, Ua, Va = u32a(N), u32a(M2), u32a(M2), u32a(M2)
        for u in U: deg[u] += 1
        for v in V: deg[v] += 1
        La, i = u32a(N), 0
        for u in range(N): La[u], i = i, i + deg[u]
        Ra = La[:]
        for e in range(M):
            i, j = Ra[u := U[e]], Ra[v := V[e]]
            Ua[i], Va[i], Ea[i], Ra[u] = u, v, e, i+1
            Ua[j], Va[j], Ea[j], Ra[v] = v, u, M+e, j+1
        super().__init__(N, M, U, V, deg, La, Ra, Ua, Va, Ea)

from cp_library.ds.fill_fn import u32a
