import cp_library.alg.tree.__header__

class HeavyLightDecomposition:
    def __init__(self, T, r=0):
        N = len(T)
        # build
        size = [1]*N
        pos = [0]*N
        par = [-1]*N
        heavy = [-1]*N
        head = [-1]*N
        depth = [0]*N
        weights = [0]*N
        order = [0]*N
        time = 0

        stack = [(2,r,r), (0,r,-1)]
        while stack:
            match stack.pop():
                case 0, v, p: # dfs down
                    par[v] = p
                    stack.append((1, v, p))
                    for c, w in T[v]:
                        if c != p:
                            depth[c] = depth[v] + 1 
                            weights[c] = w
                            stack.append((0, c, v))

                case 1, v, p: # dfs up
                    l = -1
                    for c, w in T[v]:
                        if c != p:
                            size[v] += size[c]
                            if l == -1 or size[c] > size[l]:
                                l = c
                    heavy[v] = l

                case 2, v, h: # decompose
                    head[v] = h
                    pos[v] = time
                    order[time] = v
                    p = par[v]
                    time += 1
                    l = heavy[v]
                    for c, _ in T[v]:
                        if c != p and c != l:
                            stack.append((2, c, c))

                    if l != -1:
                        stack.append((2, l, h))
        self.N = N
        self.T = T
        self.size = size
        self.pos = pos
        self.par = par
        self.heavy = heavy
        self.head = head
        self.depth = depth
        self.weights = weights
        self.order = order

    def path(self, u, v, exclude_lca=False):
        head, depth, par, pos = self.head, self.depth, self.par, self.pos
        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u,v = v,u
            yield pos[head[u]], pos[u]+1
            u = par[head[u]]

        if depth[u] < depth[v]:
            u,v = v,u
        l,r = pos[v], pos[u]+1
        if exclude_lca:
            l += 1
        yield l, r

