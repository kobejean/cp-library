import cp_library.alg.graph.fast.__header__
from typing import Iterator
from cp_library.alg.graph.fast.graph_base_cls import GraphBase

class DiGraph(GraphBase):
    def __init__(G, N: int, U: list[int], V: list[int]):
        deg, Ea, Ua, Va, La, i = u32a(N), u32a(M := len(U)), u32a(M), u32a(M), u32a(N), 0
        for u in U: deg[u] += 1
        for u in range(N): La[u], i = i, i+deg[u]
        Ra = La[:]
        for e in range(M):
            i = Ra[u := U[e]]
            Ua[i], Va[i], Ea[i], Ra[u] = u, V[e], e, i+1
        super().__init__(N, M, U, V, deg, La, Ra, Ua, Va, Ea)

    def scc(G) -> Iterator[list[int]]:
        """
        Finds strongly connected sccs in directed graph using Tarjan's algorithm.
        Returns sccs in topological order.
        """
        Ra, tin, low, on_stack, I, time = G.Ra, i32a(N := G.N, -1), u32a(N), u8a(N), G.La[:], 0
        order, stack, sccs, L = elist(N), elist(N), elist(N), elist(N)
        for u in range(N):
            if tin[u] >= 0: continue
            stack.append(u)
            while stack:
                if tin[u := stack[-1]] < 0:
                    tin[u] = low[u] = (time := time+1)
                    order.append(u)
                    on_stack[u] = 1
                if (i := I[u]) < Ra[u]:
                    I[u] += 1
                    if tin[v := G.Va[i]] < 0: stack.append(v)
                    elif on_stack[v]: chmin(low, u, tin[v])
                else:
                    stack.pop()
                    if low[u] == tin[u]:
                        L.append(len(sccs))
                        while True:
                            on_stack[v := order.pop()] = 0
                            sccs.append(v)
                            if v == u: break
                    if stack: chmin(low, stack[-1], low[u])
        return SliceIteratorReverse(sccs, L)
    
from cp_library.alg.iter.slice_iterator_reverse_cls import SliceIteratorReverse
from cp_library.ds.fill_fn import u32a, i32a, u8a
from cp_library.ds.elist_fn import elist
from cp_library.alg.dp.chmin_fn import chmin