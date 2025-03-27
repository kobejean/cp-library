---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack_sm_fn.py
    title: cp_library/bit/pack_sm_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \ndef pack_sm(N: int):\n    s = N.bit_length()\n    return s, (1<<s)-1\n\ndef\
    \ pack_enc(a: int, b: int, s: int):\n    return a << s | b\n    \ndef pack_dec(ab:\
    \ int, s: int, m: int):\n    return ab >> s, ab & m\n\ndef pack_indices(A, s):\n\
    \    return [a << s | i for i,a in enumerate(A)]\nfrom typing import Union\n\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
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
    \ Tree - Binary Index Tree            \n'''\nfrom cp_library.ds.tree.bit import\
    \ BIT\n\nclass SumCountBIT(BIT):\n    def __init__(bit, v: Union[int, list[int]]):\n\
    \        if not isinstance(v, int):\n            s, m = pack_sm(len(v))\n    \
    \        for i,d in enumerate(v):\n                v[i] = d << s | 1\n       \
    \ else:\n            s, m = pack_sm(v)\n        super().__init__(v)\n        bit.s,\
    \ bit.m = s, m\n\n    def add(bit, i, x):\n        \n        while i < bit.n:\n\
    \            bit.d[i] += x\n            i |= i+1\n\n    def sum(bit, n: int) ->\
    \ int:\n        s = 0\n        while n: s, n = s+bit.d[n-1], n&n-1\n        return\
    \ s\n\n    def range_sum(bit, l, r):\n        s = 0\n        while r: s, r = s+bit.d[r-1],\
    \ r&r-1\n        while l: s, l = s-bit.d[l-1], l&l-1\n        return s\n\n   \
    \ def __len__(bit) -> int:\n        return bit.n\n    \n    def __getitem__(bit,\
    \ i: int) -> int:\n        s, l = bit.d[i], i&(i+1)\n        while l != i: s,\
    \ i = s-bit.d[i-1], i-(i&-i)\n        return s\n    get = __getitem__\n    \n\
    \    def __setitem__(bit, i: int, x: int) -> None:\n        bit.add(i, x-bit[i])\n\
    \    set = __setitem__\n\n    def prelist(bit) -> list[int]:\n        pre = [0]+bit.d\n\
    \        for i in range(bit.n+1): pre[i] += pre[i&i-1]\n        return pre\n\n\
    \    def bisect_left(bit, v) -> int:\n        return bit.bisect_right(v-1) if\
    \ v>0 else 0\n    \n    def bisect_right(bit, v) -> int:\n        i = s = 0; ni\
    \ = m = bit.lb\n        while m:\n            if ni <= bit.n and (ns:=s+bit.d[ni-1])\
    \ <= v: s, i = ns, ni\n            ni = (m:=m>>1)|i\n        return i\n"
  code: "from cp_library.bit.pack_sm_fn import pack_sm\nimport cp_library.__header__\n\
    from typing import Union\nimport cp_library.ds.__header__\nimport cp_library.ds.tree.__header__\n\
    import cp_library.ds.tree.bit.__header__\nfrom cp_library.ds.tree.bit import BIT\n\
    \nclass SumCountBIT(BIT):\n    def __init__(bit, v: Union[int, list[int]]):\n\
    \        if not isinstance(v, int):\n            s, m = pack_sm(len(v))\n    \
    \        for i,d in enumerate(v):\n                v[i] = d << s | 1\n       \
    \ else:\n            s, m = pack_sm(v)\n        super().__init__(v)\n        bit.s,\
    \ bit.m = s, m\n\n    def add(bit, i, x):\n        \n        while i < bit.n:\n\
    \            bit.d[i] += x\n            i |= i+1\n\n    def sum(bit, n: int) ->\
    \ int:\n        s = 0\n        while n: s, n = s+bit.d[n-1], n&n-1\n        return\
    \ s\n\n    def range_sum(bit, l, r):\n        s = 0\n        while r: s, r = s+bit.d[r-1],\
    \ r&r-1\n        while l: s, l = s-bit.d[l-1], l&l-1\n        return s\n\n   \
    \ def __len__(bit) -> int:\n        return bit.n\n    \n    def __getitem__(bit,\
    \ i: int) -> int:\n        s, l = bit.d[i], i&(i+1)\n        while l != i: s,\
    \ i = s-bit.d[i-1], i-(i&-i)\n        return s\n    get = __getitem__\n    \n\
    \    def __setitem__(bit, i: int, x: int) -> None:\n        bit.add(i, x-bit[i])\n\
    \    set = __setitem__\n\n    def prelist(bit) -> list[int]:\n        pre = [0]+bit.d\n\
    \        for i in range(bit.n+1): pre[i] += pre[i&i-1]\n        return pre\n\n\
    \    def bisect_left(bit, v) -> int:\n        return bit.bisect_right(v-1) if\
    \ v>0 else 0\n    \n    def bisect_right(bit, v) -> int:\n        i = s = 0; ni\
    \ = m = bit.lb\n        while m:\n            if ni <= bit.n and (ns:=s+bit.d[ni-1])\
    \ <= v: s, i = ns, ni\n            ni = (m:=m>>1)|i\n        return i"
  dependsOn:
  - cp_library/bit/pack_sm_fn.py
  isVerificationFile: false
  path: cp_library/ds/tree/bit/sum_cnt_bit_cls.py
  requiredBy: []
  timestamp: '2025-03-27 22:10:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/tree/bit/sum_cnt_bit_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/bit/sum_cnt_bit_cls.py
- /library/cp_library/ds/tree/bit/sum_cnt_bit_cls.py.html
title: cp_library/ds/tree/bit/sum_cnt_bit_cls.py
---
