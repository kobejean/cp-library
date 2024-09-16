
def read_edges(M, i0=1):
    E = []
    for _ in range(M):
        u,v,w = read(-i0)
        w += i0
        E.append((w,u,v))
    return E

from cp_library.io.read_int_fn import read