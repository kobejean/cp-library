---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit_cls.py
    title: cp_library/ds/tree/bit_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_range_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_range_sum
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\n\
    import io,os\nfrom typing import Sequence\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\nclass BIT(Sequence[int]):\n    def __init__(bit, v):\n\
    \        if isinstance(v, int): bit.d, bit.n = [0]*v, v\n        else: bit.build(v)\n\
    \n    def build(bit, data):\n        bit.d, bit.n = data, len(data)\n        for\
    \ i in range(bit.n):\n            if (r := i|i+1) < bit.n: bit.d[r] += bit.d[i]\n\
    \n    def add(bit, i, x):\n        while i < bit.n:\n            bit.d[i] += x\n\
    \            i |= i+1\n\n    def sum(bit, n: int) -> int:\n        assert 0 <=\
    \ n <= bit.n\n        s = 0\n        while n: s, n = s+bit.d[n-1], n&n-1\n   \
    \     return s\n\n    def range_sum(bit, l, r):\n        s = 0\n        while\
    \ r: s, r = s+bit.d[r-1], r&r-1\n        while l: s, l = s-bit.d[l-1], l&l-1\n\
    \        return s\n\n    def __len__(bit) -> int:\n        return bit.n\n    \n\
    \    def __getitem__(bit, i: int) -> int:\n        s, l = bit.d[i], i&(i+1)\n\
    \        while l != i: s, i = s-bit.d[i-1], i-(i&-i)\n        return s\n    get\
    \ = __getitem__\n    \n    def __setitem__(bit, i: int, x: int) -> None:\n   \
    \     bit.add(i, x-bit[i])\n    set = __setitem__\n\n    def presum(bit) -> list[int]:\n\
    \        pre = [0]+bit.d\n        for i in range(bit.n+1): pre[i] += pre[i&i-1]\n\
    \        return pre\n    \n    def bisect_left(bit, v) -> int:\n        return\
    \ bit.bisect_right(v-1)+1\n    \n    def bisect_right(bit, v) -> int:\n      \
    \  d, i, s, m, n = bit.d, 0, 0, 1 << (bit.n.bit_length()-1), bit.n\n        while\
    \ m:\n            if (ni:=i|m) <= n and (ns:=s+d[(i|m)-1]) <= v: s, i = ns, ni\n\
    \            m >>= 1\n        return i\n\ninput = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline\n\
    MI = lambda : map(int, input().split())\n\nn,q = MI()\na = [int(s) for s in input().split()]\n\
    # b = a.copy()\nbit = BIT(a)\n# for i in range(n):\n#     assert b[i] == bit[i],\
    \ f\"{a[i]} != {bit[i]}\"\nans = []\nfor i in range(q):\n    t,p,x = MI()\n  \
    \  if t: ans.append(bit.range_sum(p,x))\n    else: bit.add(p,x)\n\nos.write(1,\"\
    \ \".join(map(str,ans)).encode())\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\n\
    import io,os\nfrom cp_library.ds.tree.bit_cls import BIT\n\ninput = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline\n\
    MI = lambda : map(int, input().split())\n\nn,q = MI()\na = [int(s) for s in input().split()]\n\
    # b = a.copy()\nbit = BIT(a)\n# for i in range(n):\n#     assert b[i] == bit[i],\
    \ f\"{a[i]} != {bit[i]}\"\nans = []\nfor i in range(q):\n    t,p,x = MI()\n  \
    \  if t: ans.append(bit.range_sum(p,x))\n    else: bit.add(p,x)\n\nos.write(1,\"\
    \ \".join(map(str,ans)).encode())"
  dependsOn:
  - cp_library/ds/tree/bit_cls.py
  isVerificationFile: true
  path: test/library-checker/data-structure/point_add_range_sum.test.py
  requiredBy: []
  timestamp: '2025-03-03 00:10:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/point_add_range_sum.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/point_add_range_sum.test.py
- /verify/test/library-checker/data-structure/point_add_range_sum.test.py.html
title: test/library-checker/data-structure/point_add_range_sum.test.py
---
