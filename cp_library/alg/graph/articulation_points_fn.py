import cp_library.alg.graph.__header__
from cp_library.alg.graph.dfs_events_fn import DFSEvent, DFSFlags, dfs_events
from cp_library.math.inft_cnst import inft

def articulation_points(G, s: int|list|None = None):
    """
    Find articulation points in an undirected graph using DFS events.
    Returns a boolean list that is True for indices where the vertex is an articulation point.
    """
    N = G.N
    if s is None:
        s = range(N)
    low = [inft] * N
    disc = [-1] * N
    children = [0] * N
    ap = [False] * N
    time = 0
    
    flags = DFSFlags.DOWN | DFSFlags.BACK | DFSFlags.UP | DFSFlags.RETURN_PARENTS
    events, parent = dfs_events(G, flags, s)
    for event in events:
        match event:
            case DFSEvent.DOWN, u, v:
                children[u] += 1
                disc[v] = low[v] = time
                time += 1
            case DFSEvent.BACK, u, v:
                if v != parent[u]:
                    low[u] = min(low[u], disc[v])
            case DFSEvent.UP, p, u:
                if parent[p] != -1:
                    low[p] = min(low[p], low[u])
                    ap[p] |= low[u] >= disc[p]
                else:
                    # root case
                    ap[p] |= children[p] > 1
                    
    return ap