import cp_library.alg.graph.__header__

def find_cycle(G, s: int = 0):
    state = [0] * G.N
    depth = [0] * G.N
    adj = [None] * G.N
    stack = [s]
    
    while stack:
        u = stack[-1]
        
        if not state[u]:
            state[u] = 1
            adj[u] = iter(G.neighbors(u))
        
        if (v := next(adj[u], None)) is not None:
            match state[v]:
                case 0:  # Unvisited
                    depth[v] = len(stack)
                    stack.append(v)
                case 1:  # In progress
                    return stack[depth[v]:]
        else:
            stack.pop()
    return None
