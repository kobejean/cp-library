import cp_library.ds.__init__

import typing

class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self.op = op
        self.e = e

        if isinstance(v, int):
            v = [e] * v

        self.n = len(v)
        self.log = (self.n-1).bit_length()+1
        self.size = 1 << self.log
        self.d = [e] * (2 * self.size)

        for i in range(self.n):
            self.d[self.size + i] = v[i]
        for i in range(self.size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self.n

        p += self.size
        self.d[p] = x
        for i in range(1, self.log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self.n

        return self.d[p + self.size]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self.n
        sml = self.e
        smr = self.e
        left += self.size
        right += self.size

        while left < right:
            if left & 1:
                sml = self.op(sml, self.d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self.op(self.d[right], smr)
            left >>= 1
            right >>= 1

        return self.op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self.d[1]

    def max_right(self, left: int,
                  f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self.n
        assert f(self.e)

        if left == self.n:
            return self.n

        left += self.size
        sm = self.e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self.op(sm, self.d[left])):
                while left < self.size:
                    left *= 2
                    if f(self.op(sm, self.d[left])):
                        sm = self.op(sm, self.d[left])
                        left += 1
                return left - self.size
            sm = self.op(sm, self.d[left])
            left += 1

        return self.n

    def min_left(self, right: int,
                 f: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= right <= self.n
        assert f(self.e)

        if right == 0:
            return 0

        right += self.size
        sm = self.e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self.op(self.d[right], sm)):
                while right < self.size:
                    right = 2 * right + 1
                    if f(self.op(self.d[right], sm)):
                        sm = self.op(self.d[right], sm)
                        right -= 1
                return right + 1 - self.size
            sm = self.op(self.d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])