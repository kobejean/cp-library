import cp_library.alg.graph.__header__
from cp_library.alg.graph.dfs_options_cls import DFSFlags, DFSEvent

def dfs_events(G, flags: DFSFlags, s: int|list|None = None, max_depth: int|None = None):
    match flags:
        case DFSFlags.INTERVAL:
            if max_depth is None:
                return G.dfs_enter_leave(s)
        case DFSFlags.TOPDOWN:
            edges = G.dfs_topdown(s, DFSFlags.CONNECT_ROOTS in flags)
            return [(DFSEvent.DOWN, p, u) for p,u in edges]
        case DFSFlags.BOTTOMUP:
            edges = G.dfs_bottomup(s, DFSFlags.CONNECT_ROOTS in flags)
            return [(DFSEvent.UP, p, u) for p,u in edges]
        case flags if DFSFlags.BACKTRACK in flags:
            return G.dfs_backtrack(s)
    state = [0] * G.N
    child = [0] * G.N
    stack = [0] * G.N
    if DFSFlags.RETURN_PARENTS in flags:
        parents = [-1] * G.N
    if DFSFlags.RETURN_DEPTHS in flags:
        depths = [-1] * G.N

    events = []
    for s in G.starts(s):
        stack[depth := 0] = s
        if DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS in flags:
            events.append((DFSEvent.DOWN,-1,s))
        while depth != -1:
            u = stack[depth]
            
            if not state[u]:
                state[u] = 1
                if DFSFlags.ENTER in flags:
                    events.append((DFSEvent.ENTER, u))
                if DFSFlags.RETURN_DEPTHS in flags:
                    depths[u] = depth
            
            if (c := child[u]) < len(G[u]):
                child[u] += 1
                match state[v := G[u][c]]:
                    case 0:  # Unvisited
                        if max_depth is None or depth <= max_depth:
                            if DFSFlags.DOWN in flags:
                                events.append((DFSEvent.DOWN, u, v))
                            stack[depth := depth+1] = v
                            if DFSFlags.RETURN_PARENTS in flags:
                                parents[v] = u
                    case 1:  # In progress
                        if DFSFlags.BACK in flags:
                            events.append((DFSEvent.BACK, u, v))
                    case 2:  # Completed
                        if DFSFlags.CROSS in flags:
                            events.append((DFSEvent.CROSS, u, v))
            else:
                depth -= 1
                state[u] = 0 if DFSFlags.BACKTRACK in flags else 2
                if DFSFlags.LEAVE in flags:
                    events.append((DFSEvent.LEAVE, u))
                if depth != -1 and DFSFlags.UP in flags:
                    events.append((DFSEvent.UP, stack[depth], u))
        if DFSFlags.UP|DFSFlags.CONNECT_ROOTS in flags:
            events.append((DFSEvent.UP,-1,s))
    ret = tuple((events,)) if DFSFlags.RETURN_ALL & flags else events
    if DFSFlags.RETURN_PARENTS in flags:
        ret += (parents,)
    if DFSFlags.RETURN_DEPTHS in flags:
        ret += (depths,)
    return ret
