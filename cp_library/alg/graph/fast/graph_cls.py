import cp_library.alg.graph.fast.__header__
from cp_library.alg.graph.fast.graph_base_cls import GraphBase

class Graph(GraphBase):
    def __init__(G, N: int, U: list[int], V: list[int]):
        deg, Ea, Ua, Va, La, Ra, i = u32f(N), i32f(M2 := (M := len(U)) << 1), u32f(M2), u32f(M2), u32f(N), u32f(N), 0
        for u in U: deg[u] += 1
        for v in V: deg[v] += 1
        for u in range(N): La[u], Ra[u], i = i, i, i+deg[u]
        for e in range(M):
            Ra[u], Ra[v] = (i := Ra[u := U[e]])+1, (j := Ra[v := V[e]])+1
            Ua[i], Va[i], Ea[i], Ua[j], Va[j], Ea[j] = u, v, e, v, u, e
        super().__init__(N, M, U, V, deg, La, Ra, Ua, Va, Ea)

from cp_library.ds.array_init_fn import u32f, i32f
