---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://judge.yosupo.jp/submission/268171
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\n\n# from harurun4635: https://judge.yosupo.jp/submission/268171\nclass LazySegTree:\n\
    \    def push(self, k):\n        # self.all_apply(2 * k, self.lazy[k])\n     \
    \   self.data[2 * k] = self.mapping(self.lazy[k], self.data[2 * k])\n        if\
    \ 2 * k < self.size:\n            self.lazy[2 * k] = self.composition(self.lazy[k],\
    \ self.lazy[2 * k])\n\n        # self.all_apply(2 * k + 1, self.lazy[k])\n   \
    \     self.data[2 * k + 1] = self.mapping(self.lazy[k], self.data[2 * k + 1])\n\
    \        if 2 * k < self.size:\n            self.lazy[2 * k + 1] = self.composition(self.lazy[k],\
    \ self.lazy[2 * k + 1])\n\n        self.lazy[k] = self.id\n\n    def __init__(self,\
    \ op, e, mapping, composition, id, lst):\n        self.n = len(lst)\n        self.log\
    \ = (self.n - 1).bit_length()\n        self.size = 1 << self.log\n        self.data\
    \ = [e] * (2 * self.size)\n        self.lazy = [id] * (2 * self.size)\n      \
    \  self.e = e\n        self.op = op\n        self.mapping = mapping\n        self.composition\
    \ = composition\n        self.id = id\n        for i in range(self.n):\n     \
    \       self.data[self.size + i] = lst[i]\n        for i in range(self.size -\
    \ 1, 0, -1):\n            # self.update(i)\n            self.data[i] = self.op(self.data[i\
    \ << 1], self.data[(i << 1) | 1])\n\n    def set(self, p, x):\n        assert\
    \ 0 <= p and p < self.n\n        p += self.size\n        for i in range(self.log,\
    \ 0, -1):\n            self.push(p >> i)\n        self.data[p] = x\n        for\
    \ i in range(1, self.log + 1):\n            # self.update(p >> i)\n          \
    \  k = p >> i\n            self.data[k] = self.op(self.data[k << 1], self.data[(k\
    \ << 1) | 1])\n\n    def get(self, p):\n        assert 0 <= p and p < self.n\n\
    \        p += self.size\n        for i in range(self.log, 0, -1):\n          \
    \  self.push(p >> i)\n        return self.data[p]\n\n    def prod(self, l, r):\n\
    \        assert 0 <= l and l <= r and r <= self.n\n        if l == r:\n      \
    \      return self.e\n        l += self.size\n        r += self.size\n       \
    \ for i in range(self.log, 0, -1):\n            if ((l >> i) << i) != l:\n   \
    \             self.push(l >> i)\n            if ((r >> i) << i) != r:\n      \
    \          self.push(r >> i)\n        sml, smr = self.e, self.e\n        while\
    \ l < r:\n            if l & 1:\n                sml = self.op(sml, self.data[l])\n\
    \                l += 1\n            if r & 1:\n                r -= 1\n     \
    \           smr = self.op(self.data[r], smr)\n            l >>= 1\n          \
    \  r >>= 1\n        return self.op(sml, smr)\n\n    def all_prod(self):\n    \
    \    return self.data[1]\n\n    def apply_point(self, p, f):\n        assert 0\
    \ <= p and p < self.n\n        p += self.size\n        for i in range(self.log,\
    \ 0, -1):\n            self.push(p >> i)\n        self.data[p] = self.mapping(f,\
    \ self.data[p])\n        for i in range(1, self.log + 1):\n            # self.update(p\
    \ >> i)\n            k = p >> i\n            self.data[k] = self.op(self.data[k\
    \ << 1], self.data[(k << 1) | 1])\n\n    def apply(self, l, r, f):\n        assert\
    \ 0 <= l and l <= r and r <= self.n\n        if l == r:\n            return\n\
    \        l += self.size\n        r += self.size\n        for i in range(self.log,\
    \ 0, -1):\n            if ((l >> i) << i) != l:\n                self.push(l >>\
    \ i)\n            if ((r >> i) << i) != r:\n                self.push((r - 1)\
    \ >> i)\n        l2, r2 = l, r\n        while l < r:\n            if l & 1:\n\
    \                # self.all_apply(l, f)\n                self.data[l] = self.mapping(f,\
    \ self.data[l])\n                if l < self.size:\n                    self.lazy[l]\
    \ = self.composition(f, self.lazy[l])\n                l += 1\n            if\
    \ r & 1:\n                r -= 1\n                # self.all_apply(r, f)\n   \
    \             self.data[r] = self.mapping(f, self.data[r])\n                if\
    \ l < self.size:\n                    self.lazy[r] = self.composition(f, self.lazy[r])\n\
    \n            l >>= 1\n            r >>= 1\n        l, r = l2, r2\n        for\
    \ i in range(1, self.log + 1):\n            if ((l >> i) << i) != l:\n       \
    \         # self.update(l >> i)\n                k = l >> i\n                self.data[k]\
    \ = self.op(self.data[k << 1], self.data[(k << 1) | 1])\n            if ((r >>\
    \ i) << i) != r:\n                # self.update((r - 1) >> i)\n              \
    \  k = (r - 1) >> i\n                self.data[k] = self.op(self.data[k << 1],\
    \ self.data[(k << 1) | 1])\n\n    def max_right(self, l, g):\n        assert 0\
    \ <= l and l <= self.n\n        assert g(self.e)\n        if l == self.n:\n  \
    \          return self.n\n        l += self.size\n        for i in range(self.log,\
    \ 0, -1):\n            self.push(l >> i)\n        sm = self.e\n        while 1:\n\
    \            while l % 2 == 0:\n                l >>= 1\n            if not (g(self.op(sm,\
    \ self.data[l]))):\n                while l < self.size:\n                   \
    \ self.push(l)\n                    l = 2*l\n                    if g(self.op(sm,\
    \ self.data[l])):\n                        sm = self.op(sm, self.data[l])\n  \
    \                      l += 1\n                return l - self.size\n        \
    \    sm = self.op(sm, self.data[l])\n            l += 1\n            if (l&-l)\
    \ == l: break\n        return self.n\n\n    def min_left(self, r, g):\n      \
    \  assert 0 <= r and r <= self.n\n        assert g(self.e)\n        if r == 0:\
    \ return 0\n        r += self.size\n        for i in range(self.log, 0, -1):\n\
    \            self.push((r - 1) >> i)\n        sm = self.e\n        while 1:\n\
    \            r -= 1\n            while r > 1 and (r % 2):\n                r >>=\
    \ 1\n            if not (g(self.op(self.data[r], sm))):\n                while\
    \ r < self.size:\n                    self.push(r)\n                    r = 2*r\
    \ + 1\n                    nsm = self.op(self.data[r], sm) \n                \
    \    if g(nsm):\n                        sm = nsm\n                        r -=\
    \ 1\n                return r + 1 - self.size\n            sm = self.op(self.data[r],\
    \ sm)\n            if (r&-r) == r: break\n        return 0\n    \n    def __str__(self):\n\
    \        return str([self.get(i) for i in range(self.n)])\n"
  code: "import cp_library.__header__\nimport cp_library.ds.__header__\nimport cp_library.ds.tree.__header__\n\
    \n# from harurun4635: https://judge.yosupo.jp/submission/268171\nclass LazySegTree:\n\
    \    def push(self, k):\n        # self.all_apply(2 * k, self.lazy[k])\n     \
    \   self.data[2 * k] = self.mapping(self.lazy[k], self.data[2 * k])\n        if\
    \ 2 * k < self.size:\n            self.lazy[2 * k] = self.composition(self.lazy[k],\
    \ self.lazy[2 * k])\n\n        # self.all_apply(2 * k + 1, self.lazy[k])\n   \
    \     self.data[2 * k + 1] = self.mapping(self.lazy[k], self.data[2 * k + 1])\n\
    \        if 2 * k < self.size:\n            self.lazy[2 * k + 1] = self.composition(self.lazy[k],\
    \ self.lazy[2 * k + 1])\n\n        self.lazy[k] = self.id\n\n    def __init__(self,\
    \ op, e, mapping, composition, id, lst):\n        self.n = len(lst)\n        self.log\
    \ = (self.n - 1).bit_length()\n        self.size = 1 << self.log\n        self.data\
    \ = [e] * (2 * self.size)\n        self.lazy = [id] * (2 * self.size)\n      \
    \  self.e = e\n        self.op = op\n        self.mapping = mapping\n        self.composition\
    \ = composition\n        self.id = id\n        for i in range(self.n):\n     \
    \       self.data[self.size + i] = lst[i]\n        for i in range(self.size -\
    \ 1, 0, -1):\n            # self.update(i)\n            self.data[i] = self.op(self.data[i\
    \ << 1], self.data[(i << 1) | 1])\n\n    def set(self, p, x):\n        assert\
    \ 0 <= p and p < self.n\n        p += self.size\n        for i in range(self.log,\
    \ 0, -1):\n            self.push(p >> i)\n        self.data[p] = x\n        for\
    \ i in range(1, self.log + 1):\n            # self.update(p >> i)\n          \
    \  k = p >> i\n            self.data[k] = self.op(self.data[k << 1], self.data[(k\
    \ << 1) | 1])\n\n    def get(self, p):\n        assert 0 <= p and p < self.n\n\
    \        p += self.size\n        for i in range(self.log, 0, -1):\n          \
    \  self.push(p >> i)\n        return self.data[p]\n\n    def prod(self, l, r):\n\
    \        assert 0 <= l and l <= r and r <= self.n\n        if l == r:\n      \
    \      return self.e\n        l += self.size\n        r += self.size\n       \
    \ for i in range(self.log, 0, -1):\n            if ((l >> i) << i) != l:\n   \
    \             self.push(l >> i)\n            if ((r >> i) << i) != r:\n      \
    \          self.push(r >> i)\n        sml, smr = self.e, self.e\n        while\
    \ l < r:\n            if l & 1:\n                sml = self.op(sml, self.data[l])\n\
    \                l += 1\n            if r & 1:\n                r -= 1\n     \
    \           smr = self.op(self.data[r], smr)\n            l >>= 1\n          \
    \  r >>= 1\n        return self.op(sml, smr)\n\n    def all_prod(self):\n    \
    \    return self.data[1]\n\n    def apply_point(self, p, f):\n        assert 0\
    \ <= p and p < self.n\n        p += self.size\n        for i in range(self.log,\
    \ 0, -1):\n            self.push(p >> i)\n        self.data[p] = self.mapping(f,\
    \ self.data[p])\n        for i in range(1, self.log + 1):\n            # self.update(p\
    \ >> i)\n            k = p >> i\n            self.data[k] = self.op(self.data[k\
    \ << 1], self.data[(k << 1) | 1])\n\n    def apply(self, l, r, f):\n        assert\
    \ 0 <= l and l <= r and r <= self.n\n        if l == r:\n            return\n\
    \        l += self.size\n        r += self.size\n        for i in range(self.log,\
    \ 0, -1):\n            if ((l >> i) << i) != l:\n                self.push(l >>\
    \ i)\n            if ((r >> i) << i) != r:\n                self.push((r - 1)\
    \ >> i)\n        l2, r2 = l, r\n        while l < r:\n            if l & 1:\n\
    \                # self.all_apply(l, f)\n                self.data[l] = self.mapping(f,\
    \ self.data[l])\n                if l < self.size:\n                    self.lazy[l]\
    \ = self.composition(f, self.lazy[l])\n                l += 1\n            if\
    \ r & 1:\n                r -= 1\n                # self.all_apply(r, f)\n   \
    \             self.data[r] = self.mapping(f, self.data[r])\n                if\
    \ l < self.size:\n                    self.lazy[r] = self.composition(f, self.lazy[r])\n\
    \n            l >>= 1\n            r >>= 1\n        l, r = l2, r2\n        for\
    \ i in range(1, self.log + 1):\n            if ((l >> i) << i) != l:\n       \
    \         # self.update(l >> i)\n                k = l >> i\n                self.data[k]\
    \ = self.op(self.data[k << 1], self.data[(k << 1) | 1])\n            if ((r >>\
    \ i) << i) != r:\n                # self.update((r - 1) >> i)\n              \
    \  k = (r - 1) >> i\n                self.data[k] = self.op(self.data[k << 1],\
    \ self.data[(k << 1) | 1])\n\n    def max_right(self, l, g):\n        assert 0\
    \ <= l and l <= self.n\n        assert g(self.e)\n        if l == self.n:\n  \
    \          return self.n\n        l += self.size\n        for i in range(self.log,\
    \ 0, -1):\n            self.push(l >> i)\n        sm = self.e\n        while 1:\n\
    \            while l % 2 == 0:\n                l >>= 1\n            if not (g(self.op(sm,\
    \ self.data[l]))):\n                while l < self.size:\n                   \
    \ self.push(l)\n                    l = 2*l\n                    if g(self.op(sm,\
    \ self.data[l])):\n                        sm = self.op(sm, self.data[l])\n  \
    \                      l += 1\n                return l - self.size\n        \
    \    sm = self.op(sm, self.data[l])\n            l += 1\n            if (l&-l)\
    \ == l: break\n        return self.n\n\n    def min_left(self, r, g):\n      \
    \  assert 0 <= r and r <= self.n\n        assert g(self.e)\n        if r == 0:\
    \ return 0\n        r += self.size\n        for i in range(self.log, 0, -1):\n\
    \            self.push((r - 1) >> i)\n        sm = self.e\n        while 1:\n\
    \            r -= 1\n            while r > 1 and (r % 2):\n                r >>=\
    \ 1\n            if not (g(self.op(self.data[r], sm))):\n                while\
    \ r < self.size:\n                    self.push(r)\n                    r = 2*r\
    \ + 1\n                    nsm = self.op(self.data[r], sm) \n                \
    \    if g(nsm):\n                        sm = nsm\n                        r -=\
    \ 1\n                return r + 1 - self.size\n            sm = self.op(self.data[r],\
    \ sm)\n            if (r&-r) == r: break\n        return 0\n    \n    def __str__(self):\n\
    \        return str([self.get(i) for i in range(self.n)])"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/tree/lazy_segtree_cls.py
  requiredBy: []
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/tree/lazy_segtree_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/lazy_segtree_cls.py
- /library/cp_library/ds/tree/lazy_segtree_cls.py.html
title: cp_library/ds/tree/lazy_segtree_cls.py
---
