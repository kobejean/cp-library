import cp_library.ds.__header__
from typing import Callable, Generic, Union
from cp_library.misc.typing import _T

class SegTree(Generic[_T]):
    def __init__(self, op: Callable[[_T, _T], _T], e: _T, v: Union[int, list[_T]]) -> None:
        if isinstance(v, int): v = [e] * v
        self.op, self.e, self.n = op, e, (n := len(v))
        self.log, self.sz, self.d = (log := (n-1).bit_length()+1), (sz := 1 << log), [e] * (sz << 1)
        for i in range(n): self.d[sz + i] = v[i]
        for i in range(sz-1,0,-1): self.d[i] = op(self.d[i<<1], self.d[i<<1|1])

    def set(self, p: int, x: _T) -> None:
        assert 0 <= p < self.n
        (d := self.d)[p := p + self.sz], op = x, self.op
        for _ in range(self.log): d[p:=p>>1] = op(d[p:=p^(p&1)], d[p|1])
    __setitem__ = set

    def get(self, p: int) -> _T:
        assert 0 <= p < self.n
        return self.d[p + self.sz]
    __getitem__ = get

    def prod(self, l: int, r: int) -> _T:
        assert 0 <= l <= r <= self.n
        sml = smr = self.e
        l, r, op, d = l+self.sz, r+self.sz, self.op, self.d
        while l < r:
            if l&1: sml, l = op(sml, d[l]), l+1
            if r&1: smr = op(d[r:=r-1], smr)
            l, r = l >> 1, r >> 1
        return op(sml, smr)

    def all_prod(self) -> _T:
        return self.d[1]

    def max_right(self, l: int, f: Callable[[_T], bool]) -> int:
        assert 0 <= l <= self.n
        assert f(self.e)
        if l == self.n: return self.n
        l, op, d, sm = l+(sz := self.sz), self.op, self.d, self.e
        while True:
            while l&1 == 0: l >>= 1
            if not f(op(sm, d[l])):
                while l < sz:
                    if f(op(sm, d[l:=l<<1])): sm, l = op(sm, d[l]), l+1
                return l - sz
            sm = op(sm, d[l])
            l += 1
            if (l & -l) == l: return self.n

    def min_left(self, r: int, f: Callable[[_T], bool]) -> int:
        assert 0 <= r <= self.n
        assert f(self.e)
        if r == 0: return 0
        r, op, d, sm = r+(sz := self.sz), self.op, self.d, self.e
        while True:
            r -= 1
            while r > 1 and r & 1: r >>= 1
            if not f(op(d[r], sm)):
                while r < sz:
                    if f(op(d[r:=r<<1|1], sm)): sm, r = op(d[r], sm), r-1
                return r + 1 - sz
            sm = op(d[r], sm)
            if (r & -r) == r: return 0