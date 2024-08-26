
import cp_library.misc.setrecursionlimit

def find_centroids(T):
    N = len(T)
    size = [1] * N
    centroids = []

    def dfs1(u, p):
        for v in T[u]:
            if v != p:
                dfs1(v, u)
                size[u] += size[v]

    def dfs2(u, p):
        is_centroid = True
        for v in T[u]:
            if v != p:
                if size[v] > N // 2:
                    is_centroid = False
                    break
        
        if is_centroid and (N - size[u]) <= N // 2:
            centroids.append(u)
        
        for v in T[u]:
            if v != p:
                dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)

    return centroids