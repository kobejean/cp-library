import cp_library.alg.graph.__header__
from typing import Iterator
from cp_library.alg.iter.slice_iterator_reverse_cls import SliceIteratorReverse
from cp_library.alg.dp.chmin_fn import chmin
from cp_library.ds.elist_fn import elist
from cp_library.ds.array.i32f_fn import i32f
from cp_library.ds.array.u8f_fn import u8f
from cp_library.ds.array.u32f_fn import u32f

def strongly_connected_components(G) -> Iterator[list[int]]:
    '''
    Finds strongly connected sccs in directed graph using Tarjan's algorithm.
    Returns sccs in topological order.
    '''
    tin, low, on_stack, time = i32f(N := G.N, -1), u32f(N), u8f(N), 0
    order, sccs, L = elist(N), elist(N), elist(N)
    
    def enter(u):
        nonlocal time
        tin[u] = low[u] = (time := time+1)
        order.append(u)
        on_stack[u] = 1

    def back_or_cross(u,v):
        if on_stack[v]: chmin(low, u, tin[v])

    def leave(u):
        if low[u] == tin[u]:
            L.append(len(sccs))
            while True:
                on_stack[v := order.pop()] = 0
                sccs.append(v)
                if v == u: break

    def up(u,v):
        chmin(low, v, low[u])

    G.dfs(enter_fn=enter, back_fn=back_or_cross, cross_fn=back_or_cross, leave_fn=leave, up_fn=up)
    return SliceIteratorReverse(sccs, L)