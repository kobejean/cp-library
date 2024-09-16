def read_tree(N, i0=1):
    T = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v = read(-i0)
        T[u].append(v)
        T[v].append(u)
    return T

from cp_library.io.read_int_fn import read