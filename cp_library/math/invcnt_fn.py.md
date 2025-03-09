---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack_sm_fn.py
    title: cp_library/bit/pack_sm_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit_cls.py
    title: cp_library/ds/tree/bit_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
    title: test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nfrom typing import Sequence\n\nclass BIT(Sequence[int]):\n    def __init__(bit,\
    \ v):\n        if isinstance(v, int): bit.d, bit.n = [0]*v, v\n        else: bit.build(v)\n\
    \        bit.lb = 1<<(bit.n.bit_length()-1)\n\n    def build(bit, data):\n   \
    \     bit.d, bit.n = data, len(data)\n        for i in range(bit.n):\n       \
    \     if (r := i|i+1) < bit.n: bit.d[r] += bit.d[i]\n\n    def add(bit, i, x):\n\
    \        assert 0 <= i <= bit.n\n        while i < bit.n:\n            bit.d[i]\
    \ += x\n            i |= i+1\n\n    def sum(bit, r: int) -> int:\n        assert\
    \ 0 <= r <= bit.n\n        s = 0\n        while r: s, r = s+bit.d[r-1], r&r-1\n\
    \        return s\n\n    def range_sum(bit, l, r):\n        assert 0 <= l <= r\
    \ <= bit.n\n        s = 0\n        while r: s, r = s+bit.d[r-1], r&r-1\n     \
    \   while l: s, l = s-bit.d[l-1], l&l-1\n        return s\n\n    def __len__(bit)\
    \ -> int:\n        return bit.n\n    \n    def __getitem__(bit, i: int) -> int:\n\
    \        s, l = bit.d[i], i&(i+1)\n        while l != i: s, i = s-bit.d[i-1],\
    \ i-(i&-i)\n        return s\n    get = __getitem__\n    \n    def __setitem__(bit,\
    \ i: int, x: int) -> None:\n        bit.add(i, x-bit[i])\n    set = __setitem__\n\
    \n    def prelist(bit) -> list[int]:\n        pre = [0]+bit.d\n        for i in\
    \ range(bit.n+1): pre[i] += pre[i&i-1]\n        return pre\n\n    def bisect_left(bit,\
    \ v) -> int:\n        return bit.bisect_right(v-1) if v>0 else 0\n    \n    def\
    \ bisect_right(bit, v) -> int:\n        i, ni = s, m = 0, bit.lb\n        while\
    \ m:\n            if ni <= bit.n and (ns:=s+bit.d[ni-1]) <= v: s, i = ns, ni\n\
    \            ni = (m:=m>>1)|i\n        return i\n\n\ndef pack_sm(N: int):\n  \
    \  s = N.bit_length()\n    return s, (1<<s)-1\n\ndef pack_enc(a: int, b: int,\
    \ s: int):\n    return a << s | b\n    \ndef pack_dec(ab: int, s: int, m: int):\n\
    \    return ab >> s, ab & m\n\ndef invcnt(A: list[int]):\n    s, m = pack_sm(N\
    \ := len(A))\n    bit, cnt, I = BIT(N), 0, [pack_enc(a,i,s) for i,a in enumerate(A)]\n\
    \    I.sort(reverse=True)\n    for i in I:\n        cnt += bit.sum(i&m)\n    \
    \    bit.add(i&m, 1)\n    return cnt\n"
  code: "import cp_library.math.__header__\nfrom cp_library.ds.tree.bit_cls import\
    \ BIT\nfrom cp_library.bit.pack_sm_fn import pack_sm, pack_enc\n\ndef invcnt(A:\
    \ list[int]):\n    s, m = pack_sm(N := len(A))\n    bit, cnt, I = BIT(N), 0, [pack_enc(a,i,s)\
    \ for i,a in enumerate(A)]\n    I.sort(reverse=True)\n    for i in I:\n      \
    \  cnt += bit.sum(i&m)\n        bit.add(i&m, 1)\n    return cnt"
  dependsOn:
  - cp_library/ds/tree/bit_cls.py
  - cp_library/bit/pack_sm_fn.py
  isVerificationFile: false
  path: cp_library/math/invcnt_fn.py
  requiredBy: []
  timestamp: '2025-03-09 20:40:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
documentation_of: cp_library/math/invcnt_fn.py
layout: document
redirect_from:
- /library/cp_library/math/invcnt_fn.py
- /library/cp_library/math/invcnt_fn.py.html
title: cp_library/math/invcnt_fn.py
---
