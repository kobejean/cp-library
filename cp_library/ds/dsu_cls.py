
class DSU:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n

    def merge(self, u, v):
        assert 0 <= u < self.n
        assert 0 <= v < self.n

        x, y = self.leader(u), self.leader(v)
        if x == y: return x

        if -self.par[x] < -self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

        return x

    def same(self, u: int, v: int):
        assert 0 <= u < self.n
        assert 0 <= v < self.n
        return self.leader(u) == self.leader(v)

    def leader(self, i) -> int:
        assert 0 <= i < self.n

        p = self.par[i]
        while p >= 0:
            if self.par[p] < 0:
                return p
            self.par[i], i, p = self.par[p], self.par[p], self.par[self.par[p]]

        return i

    def size(self, i) -> int:
        assert 0 <= i < self.n
        
        return -self.par[self.leader(i)]

    def groups(self) -> list[list[int]]:
        leader_buf = [self.leader(i) for i in range(self.n)]

        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))
