import cp_library.alg.graph.__header__
import cp_library.misc.setrecursionlimit

def tarjan_articulation_points(G, N):
    order = [None] * N
    low = [None] * N
    parent = [-1] * N
    ap = set()
    time = 0

    def dfs(u):
        nonlocal time
        children = 0
        order[u] = low[u] = time
        time += 1

        for v in G[u]:
            if order[v] is None:
                children += 1
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                if parent[u] != -1 and low[v] >= order[u]:
                    ap.add(u)
            elif v != parent[u]:
                low[u] = min(low[u], order[v])

        if parent[u] == -1 and children > 1:
            ap.add(u)

    for i in range(N):
        if order[i] is None:
            dfs(i)

    return ap