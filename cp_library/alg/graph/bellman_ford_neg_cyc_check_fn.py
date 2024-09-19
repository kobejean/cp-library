import cp_library.alg.graph.__init__
from math import inf

def bellman_ford(G, N, root) -> tuple[bool, list[int]]:
    from cp_library.alg.graph.bellman_ford_fn import bellman_ford
    D = bellman_ford(G, N, root)
    neg_cycle = any(D[u]+w<D[v] for u, edges in enumerate(G) for w,v in edges)
    return neg_cycle, D
