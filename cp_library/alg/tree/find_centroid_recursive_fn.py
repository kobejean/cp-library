import cp_library.alg.tree.__header__
import cp_library.misc.setrecursionlimit

def find_centroid(T):
    N = len(T)
    size = [1] * N
    half = N // 2

    def dfs(u=0, p=None):
        is_cent = True
        for v in T[u]:
            if v == p: continue
            cent = dfs(v, u)
            if cent != -1: return cent
            if size[v] > half: is_cent = False
            size[u] += size[v]
        if N - size[u] > half:
            is_cent = False
        return u if is_cent else -1

    return dfs()