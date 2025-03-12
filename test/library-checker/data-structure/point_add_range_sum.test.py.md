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
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_range_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_range_sum
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\n\
    import io,os\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\nfrom typing import Union\n\n\n\"\"\"\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n            \u250F\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513            \n   \
    \         \u2503                                    7 \u2503            \n   \
    \         \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\
    \u2501\u251B            \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513\
    \                 \u2502              \n            \u2503                3 \u2503\
    \u25C4\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2524              \n            \u2517\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u252F\u2501\u251B                 \u2502              \n            \u250F\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513       \u2502  \u250F\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2513       \u2502              \n      \
    \      \u2503      1 \u2503\u25C4\u2500\u2500\u2500\u2500\u2500\u2500\u2524  \u2503\
    \      5 \u2503\u25C4\u2500\u2500\u2500\u2500\u2500\u2500\u2524              \n\
    \            \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B    \
    \   \u2502  \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B     \
    \  \u2502              \n            \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\
    \u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\
    \u2501\u2501\u2501\u2513  \u2502              \n            \u2503 0 \u2503\u25C4\
    \u2500\u2524  \u2503 2 \u2503\u25C4\u2500\u2524  \u2503 4 \u2503\u25C4\u2500\u2524\
    \  \u2503 6 \u2503\u25C4\u2500\u2524              \n            \u2517\u2501\u252F\
    \u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\
    \u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502              \n \
    \             \u2502    \u2502    \u2502    \u2502    \u2502    \u2502    \u2502\
    \    \u2502              \n              \u25BC    \u25BC    \u25BC    \u25BC\
    \    \u25BC    \u25BC    \u25BC    \u25BC              \n            \u250F\u2501\
    \u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\
    \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\
    \u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513     \
    \       \n            \u2503 0 \u2503\u2503 1 \u2503\u2503 2 \u2503\u2503 3 \u2503\
    \u2503 4 \u2503\u2503 5 \u2503\u2503 6 \u2503\u2503 7 \u2503            \n   \
    \         \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\
    \u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\
    \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\
    \u2501\u251B            \n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n           Data Structure - Tree - Binary Index Tree     \
    \       \n\"\"\"\n\nclass BIT:\n    def __init__(bit, v: Union[int, list[int]]):\n\
    \        if isinstance(v, int): bit.d, bit.n = [0]*v, v\n        else: bit.build(v)\n\
    \        bit.lb = 1<<(bit.n.bit_length()-1)\n\n    def build(bit, data):\n   \
    \     bit.d, bit.n = data, len(data)\n        for i in range(bit.n):\n       \
    \     if (r := i|i+1) < bit.n: bit.d[r] += bit.d[i]\n\n    def add(bit, i, x):\n\
    \        while i < bit.n:\n            bit.d[i] += x\n            i |= i+1\n\n\
    \    def sum(bit, n: int) -> int:\n        s = 0\n        while n: s, n = s+bit.d[n-1],\
    \ n&n-1\n        return s\n\n    def range_sum(bit, l, r):\n        s = 0\n  \
    \      while r: s, r = s+bit.d[r-1], r&r-1\n        while l: s, l = s-bit.d[l-1],\
    \ l&l-1\n        return s\n\n    def __len__(bit) -> int:\n        return bit.n\n\
    \    \n    def __getitem__(bit, i: int) -> int:\n        s, l = bit.d[i], i&(i+1)\n\
    \        while l != i: s, i = s-bit.d[i-1], i-(i&-i)\n        return s\n    get\
    \ = __getitem__\n    \n    def __setitem__(bit, i: int, x: int) -> None:\n   \
    \     bit.add(i, x-bit[i])\n    set = __setitem__\n\n    def prelist(bit) -> list[int]:\n\
    \        pre = [0]+bit.d\n        for i in range(bit.n+1): pre[i] += pre[i&i-1]\n\
    \        return pre\n\n    def bisect_left(bit, v) -> int:\n        return bit.bisect_right(v-1)\
    \ if v>0 else 0\n    \n    def bisect_right(bit, v) -> int:\n        i = s = 0;\
    \ ni = m = bit.lb\n        while m:\n            if ni <= bit.n and (ns:=s+bit.d[ni-1])\
    \ <= v: s, i = ns, ni\n            ni = (m:=m>>1)|i\n        return i\n\ninput\
    \ = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline\nMI = lambda : map(int,\
    \ input().split())\n\nn,q = MI()\na = [int(s) for s in input().split()]\n# b =\
    \ a.copy()\nbit = BIT(a)\n# for i in range(n):\n#     assert b[i] == bit[i], f\"\
    {a[i]} != {bit[i]}\"\nans = []\nfor i in range(q):\n    t,p,x = MI()\n    if t:\
    \ ans.append(bit.range_sum(p,x))\n    else: bit.add(p,x)\n\nos.write(1,\" \".join(map(str,ans)).encode())\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\n\
    import io,os\nfrom cp_library.ds.tree.bit.bit_cls import BIT\n\ninput = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline\n\
    MI = lambda : map(int, input().split())\n\nn,q = MI()\na = [int(s) for s in input().split()]\n\
    # b = a.copy()\nbit = BIT(a)\n# for i in range(n):\n#     assert b[i] == bit[i],\
    \ f\"{a[i]} != {bit[i]}\"\nans = []\nfor i in range(q):\n    t,p,x = MI()\n  \
    \  if t: ans.append(bit.range_sum(p,x))\n    else: bit.add(p,x)\n\nos.write(1,\"\
    \ \".join(map(str,ans)).encode())"
  dependsOn:
  - cp_library/ds/tree/bit/bit_cls.py
  isVerificationFile: true
  path: test/library-checker/data-structure/point_add_range_sum.test.py
  requiredBy: []
  timestamp: '2025-03-12 22:12:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/point_add_range_sum.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/point_add_range_sum.test.py
- /verify/test/library-checker/data-structure/point_add_range_sum.test.py.html
title: test/library-checker/data-structure/point_add_range_sum.test.py
---
