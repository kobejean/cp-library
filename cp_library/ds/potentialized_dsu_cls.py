
class PotentializedDSU:

    def __init__(self, op, inv, e, v) -> None:
        n = v if isinstance(v, int) else len(v)
        self.n = n
        self.par = [-1] * n
        self.op = op
        self.inv = inv
        self.e = e
        self.pot = [e] * n if isinstance(v, int) else v

    def leader(self, x: int) -> int:
        assert 0 <= x < self.n
        path = []
        while self.par[x] >= 0:
            path.append(x)
            x = self.par[x]
        for y in reversed(path):
            self.pot[y] = self.op(self.pot[y], self.pot[self.par[y]])
            self.par[y] = x
        return x
    
    def consistent(self, x: int, y: int, w) -> bool:
        rx = self.leader(x)
        ry = self.leader(y)
        if rx == ry:
            return self.op(self.pot[x], self.inv(self.pot[y])) == w
        return True

    def merge(self, x: int, y: int, w) -> int:
        assert 0 <= x < self.n
        assert 0 <= y < self.n
        rx = self.leader(x)
        ry = self.leader(y)
        if rx == ry:
            return rx
        
        if self.par[rx] < self.par[ry]:
            x,y,w,rx,ry = y,x,self.inv(w),ry,rx
            
        self.par[ry] += self.par[rx]
        self.par[rx] = ry
        self.pot[rx] = self.op(
            self.op(self.inv(self.pot[x]), w), self.pot[y]
        )
        return ry

    def same(self, x: int, y: int) -> bool:
        assert 0 <= x < self.n
        assert 0 <= y < self.n
        return self.leader(x) == self.leader(y)
    
    def size(self, x: int) -> int:
        assert 0 <= x < self.n
        return -self.par[self.leader(x)]
    
    def groups(self):
        leader_buf = [self.leader(i) for i in range(self.n)]

        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))

    def diff(self, x: int, y: int):
        assert self.same(x, y)
        return self.op(self.pot[x], self.inv(self.pot[y]))
