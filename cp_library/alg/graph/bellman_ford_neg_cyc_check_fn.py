import cp_library.alg.graph.__header__
from cp_library.math.inft_cnst import inft

def bellman_ford(G, N, root) -> tuple[bool, list[int]]:
    from cp_library.alg.graph.bellman_ford_fn import bellman_ford
    D = bellman_ford(G, N, root)
    neg_cycle = any(D[u]+w<D[v] for u, edges in enumerate(G) for v,w in edges if D[u] != inft)
    return neg_cycle, D
