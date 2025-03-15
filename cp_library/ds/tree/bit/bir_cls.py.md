---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit_cls.py
    title: cp_library/ds/tree/bit/bit_cls.py
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
    from typing import Sequence\n\n\n\"\"\"\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2578\n            \u250F\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513            \n            \u2503\
    \                                    7 \u2503            \n            \u2517\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B     \
    \       \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513                 \u2502\
    \              \n            \u2503                3 \u2503\u25C4\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2524              \n            \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B     \
    \            \u2502              \n            \u250F\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2513       \u2502  \u250F\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2513       \u2502              \n            \u2503      1 \u2503\
    \u25C4\u2500\u2500\u2500\u2500\u2500\u2500\u2524  \u2503      5 \u2503\u25C4\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2524              \n            \u2517\u2501\u2501\
    \u2501\u2501\u2501\u2501\u252F\u2501\u251B       \u2502  \u2517\u2501\u2501\u2501\
    \u2501\u2501\u2501\u252F\u2501\u251B       \u2502              \n            \u250F\
    \u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\
    \u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502     \
    \         \n            \u2503 0 \u2503\u25C4\u2500\u2524  \u2503 2 \u2503\u25C4\
    \u2500\u2524  \u2503 4 \u2503\u25C4\u2500\u2524  \u2503 6 \u2503\u25C4\u2500\u2524\
    \              \n            \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\
    \u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\
    \u252F\u2501\u251B  \u2502              \n              \u2502    \u2502    \u2502\
    \    \u2502    \u2502    \u2502    \u2502    \u2502              \n          \
    \    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC\
    \              \n            \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\
    \u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\
    \u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\
    \u250F\u2501\u2501\u2501\u2513            \n            \u2503 0 \u2503\u2503\
    \ 1 \u2503\u2503 2 \u2503\u2503 3 \u2503\u2503 4 \u2503\u2503 5 \u2503\u2503 6\
    \ \u2503\u2503 7 \u2503            \n            \u2517\u2501\u2501\u2501\u251B\
    \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\
    \u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\
    \u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B            \n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n           Data\
    \ Structure - Tree - Binary Index Tree            \n\"\"\"\n\nclass BIR(Sequence[int]):\n\
    \    def __init__(bir, size: int):\n        bir.size, bir.bit1, bir.bit2  = size,\
    \ BIT(size), BIT(size)\n    \n    def __len__(bir):\n        return bir.size\n\
    \n    def add(bir, l, r, x) -> None:\n        \"\"\"Add x to all elements in range\
    \ [l, r)\"\"\"\n        bir.bit1.add(l, x), bir.bit1.add(r, -x)\n        bir.bit2.add(l,\
    \ x * l), bir.bit2.add(r, -x * r)\n\n    def sum(bir, i):\n        \"\"\"Get sum\
    \ of elements in range [0, i)\"\"\"\n        return i * bir.bit1.sum(i) - bir.bit2.sum(i)\n\
    \n    def range_sum(bir, l, r):\n        \"\"\"Get sum of elements in range [l,\
    \ r)\"\"\"\n        return bir.sum(r) - bir.sum(l)\n\n    def get(bir, i):\n \
    \       \"\"\"Get the value at index i\"\"\"\n        return (i+1) * bir.bit1.sum(i+1)\
    \ - i*bir.bit1.sum(i) - bir.bit2.get(i)\n    __getitem__ = get\n\n    def set(bir,\
    \ i, x):\n        \"\"\"Set the value at index i to x\"\"\"\n        bir.add(i,\
    \ i+1, x - bir.get(i))\n    __setitem__ = set\n        \nfrom typing import Union\n\
    \nclass BIT:\n    def __init__(bit, v: Union[int, list[int]]):\n        if isinstance(v,\
    \ int): bit.d, bit.n = [0]*v, v\n        else: bit.build(v)\n        bit.lb =\
    \ 1<<(bit.n.bit_length()-1)\n\n    def build(bit, data):\n        bit.d, bit.n\
    \ = data, len(data)\n        for i in range(bit.n):\n            if (r := i|i+1)\
    \ < bit.n: bit.d[r] += bit.d[i]\n\n    def add(bit, i, x):\n        while i <\
    \ bit.n:\n            bit.d[i] += x\n            i |= i+1\n\n    def sum(bit,\
    \ n: int) -> int:\n        s = 0\n        while n: s, n = s+bit.d[n-1], n&n-1\n\
    \        return s\n\n    def range_sum(bit, l, r):\n        s = 0\n        while\
    \ r: s, r = s+bit.d[r-1], r&r-1\n        while l: s, l = s-bit.d[l-1], l&l-1\n\
    \        return s\n\n    def __len__(bit) -> int:\n        return bit.n\n    \n\
    \    def __getitem__(bit, i: int) -> int:\n        s, l = bit.d[i], i&(i+1)\n\
    \        while l != i: s, i = s-bit.d[i-1], i-(i&-i)\n        return s\n    get\
    \ = __getitem__\n    \n    def __setitem__(bit, i: int, x: int) -> None:\n   \
    \     bit.add(i, x-bit[i])\n    set = __setitem__\n\n    def prelist(bit) -> list[int]:\n\
    \        pre = [0]+bit.d\n        for i in range(bit.n+1): pre[i] += pre[i&i-1]\n\
    \        return pre\n\n    def bisect_left(bit, v) -> int:\n        return bit.bisect_right(v-1)\
    \ if v>0 else 0\n    \n    def bisect_right(bit, v) -> int:\n        i = s = 0;\
    \ ni = m = bit.lb\n        while m:\n            if ni <= bit.n and (ns:=s+bit.d[ni-1])\
    \ <= v: s, i = ns, ni\n            ni = (m:=m>>1)|i\n        return i\n"
  code: "import cp_library.__header__\nfrom typing import Sequence\nimport cp_library.ds.__header__\n\
    import cp_library.ds.tree.__header__\nimport cp_library.ds.tree.bit.__header__\n\
    \nclass BIR(Sequence[int]):\n    def __init__(bir, size: int):\n        bir.size,\
    \ bir.bit1, bir.bit2  = size, BIT(size), BIT(size)\n    \n    def __len__(bir):\n\
    \        return bir.size\n\n    def add(bir, l, r, x) -> None:\n        \"\"\"\
    Add x to all elements in range [l, r)\"\"\"\n        bir.bit1.add(l, x), bir.bit1.add(r,\
    \ -x)\n        bir.bit2.add(l, x * l), bir.bit2.add(r, -x * r)\n\n    def sum(bir,\
    \ i):\n        \"\"\"Get sum of elements in range [0, i)\"\"\"\n        return\
    \ i * bir.bit1.sum(i) - bir.bit2.sum(i)\n\n    def range_sum(bir, l, r):\n   \
    \     \"\"\"Get sum of elements in range [l, r)\"\"\"\n        return bir.sum(r)\
    \ - bir.sum(l)\n\n    def get(bir, i):\n        \"\"\"Get the value at index i\"\
    \"\"\n        return (i+1) * bir.bit1.sum(i+1) - i*bir.bit1.sum(i) - bir.bit2.get(i)\n\
    \    __getitem__ = get\n\n    def set(bir, i, x):\n        \"\"\"Set the value\
    \ at index i to x\"\"\"\n        bir.add(i, i+1, x - bir.get(i))\n    __setitem__\
    \ = set\n        \nfrom cp_library.ds.tree.bit.bit_cls import BIT\n"
  dependsOn:
  - cp_library/ds/tree/bit/bit_cls.py
  isVerificationFile: false
  path: cp_library/ds/tree/bit/bir_cls.py
  requiredBy: []
  timestamp: '2025-03-15 12:29:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/tree/bit/bir_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/bit/bir_cls.py
- /library/cp_library/ds/tree/bit/bir_cls.py.html
title: cp_library/ds/tree/bit/bir_cls.py
---
