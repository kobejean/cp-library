import cp_library.__header__
from typing import Iterator
import cp_library.alg.__header__
from cp_library.alg.dp.chmin_fn import chmin
import cp_library.alg.graph.__header__
import cp_library.alg.graph.fast.__header__
from cp_library.alg.graph.fast.graph_base_cls import GraphBase

class DiGraph(GraphBase):
    def __init__(G, N: int, U: list[int], V: list[int]):
        deg, Ea, Ua, Va, La, Ra, i = u32f(N), u32f(M := len(U)), u32f(M), u32f(M), u32f(N), u32f(N), 0
        for u in U: deg[u] += 1
        for u in range(N): La[u], Ra[u], i = i, i, i+deg[u]
        for e in range(M): Ra[u], Ua[i], Va[i], Ea[i] = (i := Ra[u := U[e]])+1, u, V[e], e
        super().__init__(N, M, U, V, deg, La, Ra, Ua, Va, Ea)

    def scc(G) -> Iterator[list[int]]:
        '''
        Finds strongly connected sccs in directed graph using Tarjan's algorithm.
        Returns sccs in topological order.
        '''
        Ra, tin, low, on_stack, I, time = G.Ra, i32f(N := G.N, -1), u32f(N), u8f(N), G.La[:], -1
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
                        v = -1; L.append(len(sccs))
                        while v != u:
                            on_stack[v := order.pop()] = 0
                            sccs.append(v)
                    if stack: chmin(low, stack[-1], low[u])
        return SliceIteratorReverse(sccs, L)
    
from cp_library.alg.iter.slice_iterator_reverse_cls import SliceIteratorReverse
from cp_library.ds.array_init_fn import u32f, i32f, u8f
from cp_library.ds.elist_fn import elist