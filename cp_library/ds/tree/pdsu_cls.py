import cp_library.__header__
import operator
from cp_library.io.parser_cls import Parsable, IOBase
import cp_library.ds.__header__
import cp_library.ds.tree.__header__

class PDSU(Parsable):
    '''PDSU[N: int, M: int, op=operator.sub, inv=operator.neg, e=0, shift=-1]'''

    def __init__(self, op, inv, e, v) -> None:
        n = v if isinstance(v, int) else len(v)
        self.n = n
        self.par = [-1] * n
        self.op = op
        self.inv = inv
        self.e = e
        self.pot = [e] * n if isinstance(v, int) else v
        self.valid = [True] * n

    def root(self, x: int) -> int:
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
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return self.op(self.pot[x], self.inv(self.pot[y])) == w
        return True

    def merge(self, x: int, y: int, w) -> tuple[int, int]:
        assert 0 <= x < self.n
        assert 0 <= y < self.n
        rx = self.root(x)
        ry = self.root(y)
        if rx != ry:
            par = self.par
            if par[rx] < par[ry]:
                x,y,w,rx,ry = y,x,self.inv(w),ry,rx
                
            par[ry] += par[rx]
            par[rx] = ry
            self.pot[rx] = self.op(
                self.op(self.inv(self.pot[x]), w), self.pot[y]
            )
        else:
            self.valid[rx] &= self.consistent(x, y, w)
        return ry, rx

    def same(self, x: int, y: int) -> bool:
        assert 0 <= x < self.n
        assert 0 <= y < self.n
        return self.root(x) == self.root(y)
    
    def size(self, x: int) -> int:
        assert 0 <= x < self.n
        return -self.par[self.root(x)]
    
    def groups(self):
        root_buf = [self.root(i) for i in range(self.n)]

        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[root_buf[i]].append(i)

        return list(filter(lambda r: r, result))

    def diff(self, x: int, y: int):
        assert self.same(x, y)
        return self.op(self.pot[x], self.inv(self.pot[y]))

    @classmethod
    def compile(cls, N: int, M: int, op=operator.sub, inv=operator.neg, e=0, shift=-1):
        def parse(io: IOBase):
            pdsu = cls(op, inv, e, N)
            for _ in range(M):
                u, v, w = io.readints()
                pdsu.merge(u+shift, v+shift, w)
            return pdsu
        return parse