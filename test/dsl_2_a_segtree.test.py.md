---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/segtree_cls.py
    title: cp_library/ds/segtree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A\n\
    \ndef main():\n    N, Q = read()\n\n    seg = SegTree(min, 2147483647, N)\n\n\
    \    for _ in range(Q):\n        com, x, y = read()\n        if com:\n       \
    \     print(seg.prod(x,y+1))\n        else:\n            seg.set(x,y)\n\n'''\n\
    \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\n\nimport\
    \ typing\n\nclass SegTree:\n    def __init__(self,\n                 op: typing.Callable[[typing.Any,\
    \ typing.Any], typing.Any],\n                 e: typing.Any,\n               \
    \  v: typing.Union[int, typing.List[typing.Any]]) -> None:\n        self.op =\
    \ op\n        self.e = e\n\n        if isinstance(v, int):\n            v = [e]\
    \ * v\n\n        self.n = len(v)\n        self.log = (self.n-1).bit_length()+1\n\
    \        self.size = 1 << self.log\n        self.d = [e] * (2 * self.size)\n\n\
    \        for i in range(self.n):\n            self.d[self.size + i] = v[i]\n \
    \       for i in range(self.size - 1, 0, -1):\n            self._update(i)\n\n\
    \    def set(self, p: int, x: typing.Any) -> None:\n        assert 0 <= p < self.n\n\
    \n        p += self.size\n        self.d[p] = x\n        for i in range(1, self.log\
    \ + 1):\n            self._update(p >> i)\n\n    def get(self, p: int) -> typing.Any:\n\
    \        assert 0 <= p < self.n\n\n        return self.d[p + self.size]\n\n  \
    \  def prod(self, left: int, right: int) -> typing.Any:\n        assert 0 <= left\
    \ <= right <= self.n\n        sml = self.e\n        smr = self.e\n        left\
    \ += self.size\n        right += self.size\n\n        while left < right:\n  \
    \          if left & 1:\n                sml = self.op(sml, self.d[left])\n  \
    \              left += 1\n            if right & 1:\n                right -=\
    \ 1\n                smr = self.op(self.d[right], smr)\n            left >>= 1\n\
    \            right >>= 1\n\n        return self.op(sml, smr)\n\n    def all_prod(self)\
    \ -> typing.Any:\n        return self.d[1]\n\n    def max_right(self, left: int,\n\
    \                  f: typing.Callable[[typing.Any], bool]) -> int:\n        assert\
    \ 0 <= left <= self.n\n        assert f(self.e)\n\n        if left == self.n:\n\
    \            return self.n\n\n        left += self.size\n        sm = self.e\n\
    \n        first = True\n        while first or (left & -left) != left:\n     \
    \       first = False\n            while left % 2 == 0:\n                left\
    \ >>= 1\n            if not f(self.op(sm, self.d[left])):\n                while\
    \ left < self.size:\n                    left *= 2\n                    if f(self.op(sm,\
    \ self.d[left])):\n                        sm = self.op(sm, self.d[left])\n  \
    \                      left += 1\n                return left - self.size\n  \
    \          sm = self.op(sm, self.d[left])\n            left += 1\n\n        return\
    \ self.n\n\n    def min_left(self, right: int,\n                 f: typing.Callable[[typing.Any],\
    \ bool]) -> int:\n        assert 0 <= right <= self.n\n        assert f(self.e)\n\
    \n        if right == 0:\n            return 0\n\n        right += self.size\n\
    \        sm = self.e\n\n        first = True\n        while first or (right &\
    \ -right) != right:\n            first = False\n            right -= 1\n     \
    \       while right > 1 and right % 2:\n                right >>= 1\n        \
    \    if not f(self.op(self.d[right], sm)):\n                while right < self.size:\n\
    \                    right = 2 * right + 1\n                    if f(self.op(self.d[right],\
    \ sm)):\n                        sm = self.op(self.d[right], sm)\n           \
    \             right -= 1\n                return right + 1 - self.size\n     \
    \       sm = self.op(self.d[right], sm)\n\n        return 0\n\n    def _update(self,\
    \ k: int) -> None:\n        self.d[k] = self.op(self.d[2 * k], self.d[2 * k +\
    \ 1])\n\n\ndef read(shift=0, base=10):\n    return [int(s, base) + shift for s\
    \ in input().split()]\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A\n\
    \ndef main():\n    N, Q = read()\n\n    seg = SegTree(min, 2147483647, N)\n\n\
    \    for _ in range(Q):\n        com, x, y = read()\n        if com:\n       \
    \     print(seg.prod(x,y+1))\n        else:\n            seg.set(x,y)\n\nfrom\
    \ cp_library.ds.segtree_cls import SegTree\nfrom cp_library.io.read_int_fn import\
    \ read\n\nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/ds/segtree_cls.py
  - cp_library/io/read_int_fn.py
  isVerificationFile: true
  path: test/dsl_2_a_segtree.test.py
  requiredBy: []
  timestamp: '2024-11-04 21:00:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/dsl_2_a_segtree.test.py
layout: document
redirect_from:
- /verify/test/dsl_2_a_segtree.test.py
- /verify/test/dsl_2_a_segtree.test.py.html
title: test/dsl_2_a_segtree.test.py
---