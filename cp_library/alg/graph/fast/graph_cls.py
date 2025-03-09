import cp_library.alg.graph.fast.__header__
from cp_library.alg.graph.fast.graph_base_cls import GraphBase

class Graph(GraphBase):
    def __init__(G, N: int, U: list[int], V: list[int]):
        M, Ma, deg = len(U), 0, u32f(N)
        for e in range(M := len(U)):
            distinct = (u := U[e]) != (v := V[e])
            deg[u] += 1; deg[v] += distinct; Ma += 1+distinct
        Ea, Ua, Va, La, Ra, i = i32f(Ma), u32f(Ma), u32f(Ma), u32f(N), u32f(N), 0
        for u in range(N): La[u], Ra[u], i = i, i, i+deg[u]
        for e in range(M):
            i, j = Ra[u := U[e]], Ra[v := V[e]]
            Ra[u], Ua[i], Va[i], Ea[i] = i+1, u, v, e
            if i == j: continue
            Ra[v], Ua[j], Va[j], Ea[j] = j+1, v, u, e
        super().__init__(N, M, U, V, deg, La, Ra, Ua, Va, Ea)

from cp_library.ds.array_init_fn import u32f, i32f
