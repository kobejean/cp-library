import cp_library.ds.__header__

class DSU:
    def __init__(self, N):
        self.N = N
        self.par = [-1] * N

    def merge(self, u, v, src = False):
        assert 0 <= u < self.N
        assert 0 <= v < self.N

        x, y = self.leader(u), self.leader(v)
        if x == y: return (x,y) if src else x

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

        return (x,y) if src else x

    def same(self, u: int, v: int):
        assert 0 <= u < self.N
        assert 0 <= v < self.N
        return self.leader(u) == self.leader(v)

    def leader(self, i) -> int:
        assert 0 <= i < self.N
        par = self.par
        p = par[i]
        while p >= 0:
            if par[p] < 0:
                return p
            par[i], i, p = par[p], par[p], par[par[p]]

        return i

    def size(self, i) -> int:
        assert 0 <= i < self.N
        
        return -self.par[self.leader(i)]

    def groups(self) -> list[list[int]]:
        leader_buf = [self.leader(i) for i in range(self.N)]

        result = [[] for _ in range(self.N)]
        for i in range(self.N):
            result[leader_buf[i]].append(i)

        return [r for r in result if r]
