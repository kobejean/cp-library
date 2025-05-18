import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.tree.__header__

# from harurun4635: https://judge.yosupo.jp/submission/268171
class LazySegTree:
    def push(self, k):
        # self.all_apply(2 * k, self.lazy[k])
        self.data[2 * k] = self.mapping(self.lazy[k], self.data[2 * k])
        if 2 * k < self.size:
            self.lazy[2 * k] = self.composition(self.lazy[k], self.lazy[2 * k])

        # self.all_apply(2 * k + 1, self.lazy[k])
        self.data[2 * k + 1] = self.mapping(self.lazy[k], self.data[2 * k + 1])
        if 2 * k < self.size:
            self.lazy[2 * k + 1] = self.composition(self.lazy[k], self.lazy[2 * k + 1])

        self.lazy[k] = self.id

    def __init__(self, op, e, mapping, composition, id, lst):
        self.n = len(lst)
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.data = [e] * (2 * self.size)
        self.lazy = [id] * (2 * self.size)
        self.e = e
        self.op = op
        self.mapping = mapping
        self.composition = composition
        self.id = id
        for i in range(self.n):
            self.data[self.size + i] = lst[i]
        for i in range(self.size - 1, 0, -1):
            # self.update(i)
            self.data[i] = self.op(self.data[i << 1], self.data[(i << 1) | 1])

    def set(self, p, x):
        assert 0 <= p and p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.data[p] = x
        for i in range(1, self.log + 1):
            # self.update(p >> i)
            k = p >> i
            self.data[k] = self.op(self.data[k << 1], self.data[(k << 1) | 1])

    def get(self, p):
        assert 0 <= p and p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        return self.data[p]

    def prod(self, l, r):
        assert 0 <= l and l <= r and r <= self.n
        if l == r:
            return self.e
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push(r >> i)
        sml, smr = self.e, self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.data[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.data[1]

    def apply_point(self, p, f):
        assert 0 <= p and p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.data[p] = self.mapping(f, self.data[p])
        for i in range(1, self.log + 1):
            # self.update(p >> i)
            k = p >> i
            self.data[k] = self.op(self.data[k << 1], self.data[(k << 1) | 1])

    def apply(self, l, r, f):
        assert 0 <= l and l <= r and r <= self.n
        if l == r:
            return
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self.push(l >> i)
            if ((r >> i) << i) != r:
                self.push((r - 1) >> i)
        l2, r2 = l, r
        while l < r:
            if l & 1:
                # self.all_apply(l, f)
                self.data[l] = self.mapping(f, self.data[l])
                if l < self.size:
                    self.lazy[l] = self.composition(f, self.lazy[l])
                l += 1
            if r & 1:
                r -= 1
                # self.all_apply(r, f)
                self.data[r] = self.mapping(f, self.data[r])
                if l < self.size:
                    self.lazy[r] = self.composition(f, self.lazy[r])

            l >>= 1
            r >>= 1
        l, r = l2, r2
        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l:
                # self.update(l >> i)
                k = l >> i
                self.data[k] = self.op(self.data[k << 1], self.data[(k << 1) | 1])
            if ((r >> i) << i) != r:
                # self.update((r - 1) >> i)
                k = (r - 1) >> i
                self.data[k] = self.op(self.data[k << 1], self.data[(k << 1) | 1])

    def max_right(self, l, g):
        assert 0 <= l and l <= self.n
        assert g(self.e)
        if l == self.n:
            return self.n
        l += self.size
        for i in range(self.log, 0, -1):
            self.push(l >> i)
        sm = self.e
        while 1:
            while l % 2 == 0:
                l >>= 1
            if not (g(self.op(sm, self.data[l]))):
                while l < self.size:
                    self.push(l)
                    l = 2*l
                    if g(self.op(sm, self.data[l])):
                        sm = self.op(sm, self.data[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.data[l])
            l += 1
            if (l&-l) == l: break
        return self.n

    def min_left(self, r, g):
        assert 0 <= r and r <= self.n
        assert g(self.e)
        if r == 0: return 0
        r += self.size
        for i in range(self.log, 0, -1):
            self.push((r - 1) >> i)
        sm = self.e
        while 1:
            r -= 1
            while r > 1 and (r % 2):
                r >>= 1
            if not (g(self.op(self.data[r], sm))):
                while r < self.size:
                    self.push(r)
                    r = 2*r + 1
                    nsm = self.op(self.data[r], sm) 
                    if g(nsm):
                        sm = nsm
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.data[r], sm)
            if (r&-r) == r: break
        return 0
    
    def __str__(self):
        return str([self.get(i) for i in range(self.n)])