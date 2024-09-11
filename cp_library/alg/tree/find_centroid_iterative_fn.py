
def find_centroid(T):
    N = len(T)
    size = [1] * N
    stack = [(0, None, True)]

    while stack:
        u, p, forw = stack.pop()
        if forw:
            stack.append((u, p, False))
            for v in T[u]:
                if v != p:
                    stack.append((v, u, True))
        else:
            is_cent = True
            for v in T[u]:
                if v == p: continue
                if size[v] > N//2:
                    is_cent = False
                size[u] += size[v]
            
            if is_cent and N - size[u] <=  N//2:
                return u
    N = len(T)
    size = [0] * N
    stack = [(0, None, True)]
    cent = None

    while stack:
        u, p, forw = stack.pop()

        if forw:
            size[u] = 1
            stack.append((u, p, False))
            for v in T[u]:
                if v != p:
                    stack.append((v, u, True))
        else:
            is_cent = True
            for v in T[u]:
                if v == p:
                    continue
                if size[v] > N // 2:
                    is_cent = False
                size[u] += size[v]
            
            if N - size[u] > N // 2:
                is_cent = False
            
            if is_cent:
                cent = u
                break

    return cent