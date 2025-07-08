import cp_library.alg.graph.__header__
from functools import reduce
from cp_library.ds.heap.fast_heapq  import heapify
import cp_library.misc.setrecursionlimit
from cp_library.ds.dsu_cls import DSU
from cp_library.alg.graph.partial_func_graph_cls import PartialFuncGraph

def edmonds_branching(E, N, root) -> list[tuple[int,int,any]]:
    # obtain incoming edges
    Gin = [[] for _ in range(N)]
    for id,(u,v,w) in enumerate(E):
        if v != root:
            Gin[v].append([w,u,id])
    

    # heapify for fast access to optimal edges
    for v in range(N):
        heapify(Gin[v])

    groups = DSU(N)
    active = set(range(N))
    active.discard(root)

    def find_cycle(min_in):
        for v in active:
            cyc = min_in.find_cycle(v)
            if cyc: return cyc
        return None
    
    def contract(cyc):
        kickout = [-1]*len(E)
        active.difference_update(cyc)
        nv = reduce(groups.merge_dest, cyc)
        active.add(nv)
        new_edges = []
        
        # Update Gin to reflect the contracted cycle
        for v in cyc:
            cw, _, cid = Gin[v][0]
            for edge in Gin[v]:
                _, u, id = edge
                if groups.leader(u) != nv:
                    edge[0] -= cw # update weight
                    kickout[id] = cid
                    new_edges.append(edge)
                    if new_edges[-1][0] < new_edges[0][0]:
                        new_edges[0], new_edges[-1] = new_edges[-1], new_edges[0]
            Gin[v].clear()
        Gin[nv] = new_edges
        return kickout


    def rec(Gin):
        min_in = PartialFuncGraph([groups.leader(Gin[v][0][1]) if Gin[v] else -1 for v in range(N)])
        cyc = find_cycle(min_in)
        if cyc:
            C = { Gin[v][0][2] for v in cyc }
            kickout = contract(cyc)
            MCA = rec(Gin)
            for id in MCA:
                C.discard(kickout[id])
            MCA.extend(C)
            return MCA
        else:
            return [edges[0][2] for edges in Gin if edges]

    return [E[id] for id in rec(Gin)]
