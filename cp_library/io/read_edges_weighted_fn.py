from cp_library.io.rint_fn import rint

def read_edges(M, i0=1):
    E = []
    for _ in range(M):
        u,v,w = rint(-i0)
        w += i0
        E.append((w,u,v))
    return E