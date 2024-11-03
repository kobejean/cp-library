import cp_library.alg.graph.__header__

def floyd_warshall(G, N, directed=True):
    if directed:
        from cp_library.alg.graph.floyd_warshall_directed_fn import floyd_warshall
    else:
        from cp_library.alg.graph.floyd_warshall_fn import floyd_warshall
    D = floyd_warshall(G, N)
    return any(D[i][i] < 0 for i in range(N)), D
