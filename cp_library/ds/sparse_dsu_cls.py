import cp_library.ds.__header__
from collections import defaultdict

class SparseDSU:
    def __init__(self, n) -> None:
        self.par = defaultdict(lambda:-1)

    def merge(self, u, v) -> int:
        x, y = self.leader(u), self.leader(v)
        if x == y: return x

        if -self.par[x] < -self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

        return x

    def same(self, u: int, v: int) -> bool:
        return self.leader(u) == self.leader(v)

    def leader(self, i) -> int:
        p = self.par[i]
        while p >= 0:
            if self.par[p] < 0:
                return p
            self.par[i], i, p = self.par[p], self.par[p], self.par[self.par[p]]

        return i

    def size(self, i) -> int:
        return -self.par[self.leader(i)]

    def groups(self) -> list[list[int]]:
        idx = list(self.par.keys())
        leader_buf = [self.leader(i) for i in idx]

        result = [[] for _ in idx]
        for i in idx:
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))
