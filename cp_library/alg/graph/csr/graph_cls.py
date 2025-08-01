import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
from cp_library.alg.graph.csr.graph_base_cls import GraphBase

class Graph(GraphBase):
    def __init__(G, N: int, U: list[int], V: list[int]):
        M, Ma, deg = len(U), 0, u32f(N)
        for e in range(M := len(U)):
            distinct = (u := U[e]) != (v := V[e])
            deg[u] += 1; deg[v] += distinct; Ma += 1+distinct
        twin, Ea, Ua, Va, La, Ra, i = i32f(Ma), i32f(Ma), u32f(Ma), u32f(Ma), u32f(N), u32f(N), 0
        for u in range(N): La[u] = Ra[u] = i; i = i+deg[u]
        for e in range(M):
            i, j = Ra[u := U[e]], Ra[v := V[e]]
            Ra[u], Ua[i], Va[i], Ea[i], twin[i] = i+1, u, v, e, j
            if i == j: continue
            Ra[v], Ua[j], Va[j], Ea[j], twin[j] = j+1, v, u, e, i
        super().__init__(N, M, U, V, deg, La, Ra, Ua, Va, Ea, twin)
from cp_library.ds.array.i32f_fn import i32f
from cp_library.ds.array.u32f_fn import u32f