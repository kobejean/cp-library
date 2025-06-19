---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_indices_fn.py
    title: cp_library/bit/pack/pack_indices_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_sm_fn.py
    title: cp_library/bit/pack/pack_sm_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit_cls.py
    title: cp_library/ds/tree/bit/bit_cls.py
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
    \n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2513            \n            \u2503                           \
    \         7 \u2503            \n            \u2517\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B            \n            \u250F\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2513                 \u2502              \n  \
    \          \u2503                3 \u2503\u25C4\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524           \
    \   \n            \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B                 \u2502\
    \              \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2513       \u2502  \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513\
    \       \u2502              \n            \u2503      1 \u2503\u25C4\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2524  \u2503      5 \u2503\u25C4\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2524              \n            \u2517\u2501\u2501\u2501\u2501\u2501\
    \u2501\u252F\u2501\u251B       \u2502  \u2517\u2501\u2501\u2501\u2501\u2501\u2501\
    \u252F\u2501\u251B       \u2502              \n            \u250F\u2501\u2501\u2501\
    \u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\
    \u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502              \n       \
    \     \u2503 0 \u2503\u25C4\u2500\u2524  \u2503 2 \u2503\u25C4\u2500\u2524  \u2503\
    \ 4 \u2503\u25C4\u2500\u2524  \u2503 6 \u2503\u25C4\u2500\u2524              \n\
    \            \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B\
    \  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B\
    \  \u2502              \n              \u2502    \u2502    \u2502    \u2502  \
    \  \u2502    \u2502    \u2502    \u2502              \n              \u25BC  \
    \  \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC        \
    \      \n            \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\
    \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\
    \u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\
    \u2501\u2501\u2501\u2513            \n            \u2503 0 \u2503\u2503 1 \u2503\
    \u2503 2 \u2503\u2503 3 \u2503\u2503 4 \u2503\u2503 5 \u2503\u2503 6 \u2503\u2503\
    \ 7 \u2503            \n            \u2517\u2501\u2501\u2501\u251B\u2517\u2501\
    \u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\
    \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\
    \u2501\u251B\u2517\u2501\u2501\u2501\u251B            \n\u257A\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n           Data Structure -\
    \ Tree - Binary Index Tree            \n'''\n\nclass BIT:\n    def __init__(bit,\
    \ v):\n        if isinstance(v, int): bit._d, bit._n = [0]*v, v\n        else:\
    \ bit.build(v)\n        bit._lb = 1<<bit._n.bit_length()\n\n    def build(bit,\
    \ data):\n        bit._d, bit._n = data, len(data)\n        for i in range(bit._n):\n\
    \            if (r := i|i+1) < bit._n: bit._d[r] += bit._d[i]\n\n    def add(bit,\
    \ i, x):\n        while i < bit._n: bit._d[i] += x; i |= i+1\n\n    def sum(bit,\
    \ n: int) -> int:\n        s = 0\n        while n: s, n = s+bit._d[n-1], n&n-1\n\
    \        return s\n\n    def sum_range(bit, l, r):\n        s = 0\n        while\
    \ r: s, r = s+bit._d[r-1], r&r-1\n        while l: s, l = s-bit._d[l-1], l&l-1\n\
    \        return s\n\n    def __len__(bit) -> int:\n        return bit._n\n   \
    \ \n    def __getitem__(bit, i: int) -> int:\n        s, l = bit._d[i], i&(i+1)\n\
    \        while l != i: s, i = s-bit._d[i-1], i-(i&-i)\n        return s\n    get\
    \ = __getitem__\n    \n    def __setitem__(bit, i: int, x: int) -> None:\n   \
    \     bit.add(i, x-bit[i])\n    set = __setitem__\n\n    def prelist(bit) -> list[int]:\n\
    \        pre = [0]+bit._d\n        for i in range(bit._n+1): pre[i] += pre[i&i-1]\n\
    \        return pre\n\n    def bisect_left(bit, v) -> int:\n        return bit.bisect_right(v-1)\
    \ if v>0 else -1\n    \n    def bisect_right(bit, v, key=None) -> int:\n     \
    \   i = s = 0; m = bit._lb\n        if key:\n            while m := m>>1:\n  \
    \              if (ni := m|i) <= bit._n and key(ns:=s+bit._d[ni-1]) <= v: s, i\
    \ = ns, ni\n        else:\n            while m := m>>1:\n                if (ni\
    \ := m|i) <= bit._n and (ns:=s+bit._d[ni-1]) <= v: s, i = ns, ni\n        return\
    \ i\n\ndef invcnt(A: list[int]):\n    s, m = pack_sm(N := len(A))\n    bit, cnt,\
    \ I = BIT(N), 0, pack_indices(A, s); I.sort(reverse=True)\n    for i in I: cnt\
    \ += bit.sum(i&m); bit.add(i&m, 1)\n    return cnt\n\n\ndef pack_indices(A, s):\
    \ return [a<<s|i for i,a in enumerate(A)]\ndef pack_sm(N: int): s=N.bit_length();\
    \ return s,(1<<s)-1\n"
  code: "import cp_library.math.__header__\nfrom cp_library.ds.tree.bit.bit_cls import\
    \ BIT\n\ndef invcnt(A: list[int]):\n    s, m = pack_sm(N := len(A))\n    bit,\
    \ cnt, I = BIT(N), 0, pack_indices(A, s); I.sort(reverse=True)\n    for i in I:\
    \ cnt += bit.sum(i&m); bit.add(i&m, 1)\n    return cnt\nfrom cp_library.bit.pack.pack_indices_fn\
    \ import pack_indices\nfrom cp_library.bit.pack.pack_sm_fn import pack_sm"
  dependsOn:
  - cp_library/ds/tree/bit/bit_cls.py
  - cp_library/bit/pack/pack_indices_fn.py
  - cp_library/bit/pack/pack_sm_fn.py
  isVerificationFile: false
  path: cp_library/math/invcnt_fn.py
  requiredBy: []
  timestamp: '2025-06-20 03:24:59+09:00'
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
