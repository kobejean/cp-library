---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnt32_fn.py
    title: cp_library/bit/popcnt32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u32f_fn.py
    title: cp_library/ds/array/u32f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit_cls.py
    title: cp_library/ds/tree/bit/bit_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/predecessor_problem
    links:
    - https://judge.yosupo.jp/problem/predecessor_problem
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/predecessor_problem\n\
    \ndef main():\n    N, Q = map(int, sys.stdin.readline().split())\n    T = sys.stdin.readline()\n\
    \n    def construct(T):\n        B = u32f((M := (len(T)+31)>>5))\n        for\
    \ i,c in enumerate(T):\n            if c == '1': B[i>>5] |= 1 << (i&31)\n    \
    \    return M, B\n    \n    M, B = construct(T)\n    bit = BIT([popcnt32(b) for\
    \ b in B])\n\n    def count(b, r):\n        return bit.sum(b)+popcnt32(B[b] &\
    \ ((1<<r)-1))\n    \n    def get(b, r):\n        return B[b]>>r&1\n    \n    def\
    \ set(b, r, x):\n        if get(b, r)^x:\n            if x:\n                B[b]\
    \ |= 1 << r\n                bit.add(b, 1)\n            else:\n              \
    \  B[b] &= ~(1 << r)\n                bit.add(b, -1)\n\n    def ge(b, r):\n  \
    \      nb = bit.bisect_right(count(b, r))\n        if nb < M:\n            m =\
    \ B[nb] if b < nb else (B[nb] >> r) << r\n            return nb<<5|(m & -m).bit_length()-1\n\
    \        else:\n            return -1\n        \n    def le(b, r):\n        nb\
    \ = bit.bisect_left(count(b, r+1))\n        if 0 <= nb:\n            m = B[nb]\
    \ if nb < b else (B[nb] & ((1<<(r+1))-1))\n            return nb<<5|m.bit_length()-1\n\
    \        else:\n            return -1\n\n    for _ in range(Q):\n        c, k\
    \ = sys.stdin.readline().split()\n        k = int(k)\n        b, r = k>>5, k&31\n\
    \        if c == '0': set(b, r, 1)\n        elif c == '1': set(b, r, 0)\n    \
    \    elif c == '2':\n            append(str(get(b, r)))\n            append('\\\
    n')\n        elif c == '3':\n            append(str(ge(b, r)))\n            append('\\\
    n')\n        elif c == '4':\n            append(str(le(b, r)))\n            append('\\\
    n')\n    os.write(1, sb.build().encode())\n\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\ndef popcnt32(x):\n    x = ((x >> 1)  & 0x55555555) +\
    \ (x & 0x55555555)\n    x = ((x >> 2)  & 0x33333333) + (x & 0x33333333)\n    x\
    \ = ((x >> 4)  & 0x0f0f0f0f) + (x & 0x0f0f0f0f)\n    x = ((x >> 8)  & 0x00ff00ff)\
    \ + (x & 0x00ff00ff)\n    x = ((x >> 16) & 0x0000ffff) + (x & 0x0000ffff)\n  \
    \  return x\nif hasattr(int, 'bit_count'):\n    popcnt32 = int.bit_count\n\n\n\
    from array import array\ndef u32f(N: int, elm: int = 0):     return array('I',\
    \ (elm,))*N  # unsigned int\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\
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
    \ Structure - Tree - Binary Index Tree            \n'''\n\nclass BIT:\n    def\
    \ __init__(bit, v):\n        if isinstance(v, int): bit._d, bit._n = [0]*v, v\n\
    \        else: bit.build(v)\n        bit._lb = 1<<bit._n.bit_length()\n\n    def\
    \ build(bit, data):\n        bit._d, bit._n = data, len(data)\n        for i in\
    \ range(bit._n):\n            if (r := i|i+1) < bit._n: bit._d[r] += bit._d[i]\n\
    \n    def add(bit, i, x):\n        while i < bit._n: bit._d[i] += x; i |= i+1\n\
    \n    def sum(bit, n: int) -> int:\n        s = 0\n        while n: s, n = s+bit._d[n-1],\
    \ n&n-1\n        return s\n\n    def sum_range(bit, l, r):\n        s = 0\n  \
    \      while r: s, r = s+bit._d[r-1], r&r-1\n        while l: s, l = s-bit._d[l-1],\
    \ l&l-1\n        return s\n\n    def __len__(bit) -> int:\n        return bit._n\n\
    \    \n    def __getitem__(bit, i: int) -> int:\n        s, l = bit._d[i], i&(i+1)\n\
    \        while l != i: s, i = s-bit._d[i-1], i-(i&-i)\n        return s\n    get\
    \ = __getitem__\n    \n    def __setitem__(bit, i: int, x: int) -> None: bit.add(i,\
    \ x-bit[i])\n    set = __setitem__\n\n    def prelist(bit) -> list[int]:\n   \
    \     pre = [0]+bit._d\n        for i in range(bit._n+1): pre[i] += pre[i&i-1]\n\
    \        return pre\n\n    def bisect_left(bit, v) -> int:\n        return bit.bisect_right(v-1)\
    \ if v>0 else -1\n    \n    def bisect_right(bit, v, key=None) -> int:\n     \
    \   i = s = 0; m = bit._lb\n        if key:\n            while m := m>>1:\n  \
    \              if (ni := m|i) <= bit._n and key(ns:=s+bit._d[ni-1]) <= v: s, i\
    \ = ns, ni\n        else:\n            while m := m>>1:\n                if (ni\
    \ := m|i) <= bit._n and (ns:=s+bit._d[ni-1]) <= v: s, i = ns, ni\n        return\
    \ i\n\nimport os\nfrom __pypy__ import builders\nsb = builders.StringBuilder()\n\
    append = sb.append\nimport sys\n\nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/predecessor_problem\n\
    \ndef main():\n    N, Q = map(int, sys.stdin.readline().split())\n    T = sys.stdin.readline()\n\
    \n    def construct(T):\n        B = u32f((M := (len(T)+31)>>5))\n        for\
    \ i,c in enumerate(T):\n            if c == '1': B[i>>5] |= 1 << (i&31)\n    \
    \    return M, B\n    \n    M, B = construct(T)\n    bit = BIT([popcnt32(b) for\
    \ b in B])\n\n    def count(b, r):\n        return bit.sum(b)+popcnt32(B[b] &\
    \ ((1<<r)-1))\n    \n    def get(b, r):\n        return B[b]>>r&1\n    \n    def\
    \ set(b, r, x):\n        if get(b, r)^x:\n            if x:\n                B[b]\
    \ |= 1 << r\n                bit.add(b, 1)\n            else:\n              \
    \  B[b] &= ~(1 << r)\n                bit.add(b, -1)\n\n    def ge(b, r):\n  \
    \      nb = bit.bisect_right(count(b, r))\n        if nb < M:\n            m =\
    \ B[nb] if b < nb else (B[nb] >> r) << r\n            return nb<<5|(m & -m).bit_length()-1\n\
    \        else:\n            return -1\n        \n    def le(b, r):\n        nb\
    \ = bit.bisect_left(count(b, r+1))\n        if 0 <= nb:\n            m = B[nb]\
    \ if nb < b else (B[nb] & ((1<<(r+1))-1))\n            return nb<<5|m.bit_length()-1\n\
    \        else:\n            return -1\n\n    for _ in range(Q):\n        c, k\
    \ = sys.stdin.readline().split()\n        k = int(k)\n        b, r = k>>5, k&31\n\
    \        if c == '0': set(b, r, 1)\n        elif c == '1': set(b, r, 0)\n    \
    \    elif c == '2':\n            append(str(get(b, r)))\n            append('\\\
    n')\n        elif c == '3':\n            append(str(ge(b, r)))\n            append('\\\
    n')\n        elif c == '4':\n            append(str(le(b, r)))\n            append('\\\
    n')\n    os.write(1, sb.build().encode())\n\nfrom cp_library.bit.popcnt32_fn import\
    \ popcnt32\nfrom cp_library.ds.array.u32f_fn import u32f\nfrom cp_library.ds.tree.bit.bit_cls\
    \ import BIT\n\nimport os\nfrom __pypy__ import builders\nsb = builders.StringBuilder()\n\
    append = sb.append\nimport sys\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/bit/popcnt32_fn.py
  - cp_library/ds/array/u32f_fn.py
  - cp_library/ds/tree/bit/bit_cls.py
  isVerificationFile: true
  path: test/library-checker/data-structure/predecessor_problem_bit.test.py
  requiredBy: []
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/predecessor_problem_bit.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/predecessor_problem_bit.test.py
- /verify/test/library-checker/data-structure/predecessor_problem_bit.test.py.html
title: test/library-checker/data-structure/predecessor_problem_bit.test.py
---
