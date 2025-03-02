---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/ds/tree/bir_cls.py
    title: cp_library/ds/tree/bir_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/invcnt_fn.py
    title: cp_library/math/invcnt_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_heavy_light_decomposition.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
    title: test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
    title: test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
    title: test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_add_range_sum.test.py
    title: test/library-checker/data-structure/point_add_range_sum.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "from typing import Sequence\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
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
    \            m >>= 1\n        return i\n"
  code: "from typing import Sequence\nimport cp_library.ds.__header__\n\nclass BIT(Sequence[int]):\n\
    \    def __init__(bit, v):\n        if isinstance(v, int): bit.d, bit.n = [0]*v,\
    \ v\n        else: bit.build(v)\n\n    def build(bit, data):\n        bit.d, bit.n\
    \ = data, len(data)\n        for i in range(bit.n):\n            if (r := i|i+1)\
    \ < bit.n: bit.d[r] += bit.d[i]\n\n    def add(bit, i, x):\n        while i <\
    \ bit.n:\n            bit.d[i] += x\n            i |= i+1\n\n    def sum(bit,\
    \ n: int) -> int:\n        assert 0 <= n <= bit.n\n        s = 0\n        while\
    \ n: s, n = s+bit.d[n-1], n&n-1\n        return s\n\n    def range_sum(bit, l,\
    \ r):\n        s = 0\n        while r: s, r = s+bit.d[r-1], r&r-1\n        while\
    \ l: s, l = s-bit.d[l-1], l&l-1\n        return s\n\n    def __len__(bit) -> int:\n\
    \        return bit.n\n    \n    def __getitem__(bit, i: int) -> int:\n      \
    \  s, l = bit.d[i], i&(i+1)\n        while l != i: s, i = s-bit.d[i-1], i-(i&-i)\n\
    \        return s\n    get = __getitem__\n    \n    def __setitem__(bit, i: int,\
    \ x: int) -> None:\n        bit.add(i, x-bit[i])\n    set = __setitem__\n\n  \
    \  def presum(bit) -> list[int]:\n        pre = [0]+bit.d\n        for i in range(bit.n+1):\
    \ pre[i] += pre[i&i-1]\n        return pre\n    \n    def bisect_left(bit, v)\
    \ -> int:\n        return bit.bisect_right(v-1)+1\n    \n    def bisect_right(bit,\
    \ v) -> int:\n        d, i, s, m, n = bit.d, 0, 0, 1 << (bit.n.bit_length()-1),\
    \ bit.n\n        while m:\n            if (ni:=i|m) <= n and (ns:=s+d[(i|m)-1])\
    \ <= v: s, i = ns, ni\n            m >>= 1\n        return i"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/tree/bit_cls.py
  requiredBy:
  - cp_library/math/invcnt_fn.py
  - cp_library/ds/tree/bir_cls.py
  timestamp: '2025-03-03 00:10:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/point_add_range_sum.test.py
  - test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
  - test/atcoder/abc/abc294_g_fast_tree_heavy_light_decomposition.test.py
  - test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
  - test/atcoder/abc/abc294_g_tree_lca_table_weighted_bit.test.py
  - test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
documentation_of: cp_library/ds/tree/bit_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/bit_cls.py
- /library/cp_library/ds/tree/bit_cls.py.html
title: cp_library/ds/tree/bit_cls.py
---
