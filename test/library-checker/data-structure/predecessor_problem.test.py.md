---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/min2_fn.py
    title: cp_library/alg/dp/min2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u32f_fn.py
    title: cp_library/ds/array/u32f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bitset_tree_cls.py
    title: cp_library/ds/tree/bitset_tree_cls.py
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
    \    B = BitsetTree(T)\n    for _ in range(Q):\n        c, k = sys.stdin.readline().split()\n\
    \        k = int(k)\n        if c == '0':\n            B[k] = 1\n        elif\
    \ c == '1':\n            B[k] = 0\n        elif c == '2':\n            append(str(B[k]))\n\
    \            append('\\n')\n        elif c == '3':\n            append(str(B.ge(k)))\n\
    \            append('\\n')\n        elif c == '4':\n            append(str(B.le(k)))\n\
    \            append('\\n')\n    os.write(1, sb.build().encode())\n\n'''\n\u257A\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n         \
    \    https://kobejean.github.io/cp-library               \n'''\n\n\ndef min2(a,\
    \ b):\n    return a if a < b else b\n\n\nfrom array import array\ndef u32f(N:\
    \ int, elm: int = 0):     return array('I', (elm,))*N  # unsigned int\n\n\nclass\
    \ BitsetTree:\n    def __init__(B, S: str):\n        B.N = N = len(S)\n      \
    \  L = u32f((N+31)>>5)\n        for k,c in enumerate(S):\n            k,r = k>>5,k&31\n\
    \            if c=='1': L[k]|=1<<r\n        B.levels = [L]\n        while (N :=\
    \ len(L := B.levels[-1])) > 1:\n            A = u32f((N+31)>>5)\n            for\
    \ i in range(0,N,32):\n                a=j=0;r=min2(i+32,N)\n                while\
    \ i+j<r:a|=(0<L[i+j])<<j;j+=1\n                A[i>>5]=a\n            B.levels.append(A)\n\
    \        B.depth = len(B.levels)\n\n    def set0(B, k):\n        if B.levels[0][k>>5]>>(k&31)&1:\
    \ \n            l = -1\n            while (l:=l+1) < B.depth:\n              \
    \  B.levels[l][k>>5]&=~(1<<(k&31));k>>=5\n                if B.levels[l][k]: break\n\
    \n    def set1(B, k):\n        if not B.levels[0][k>>5]>>(k&31)&1: \n        \
    \    l = -1\n            while (l:=l+1) < B.depth: B.levels[l][k>>5]|=1<<(k&31);k>>=5\n\
    \n    def __setitem__(B, k: int, v: int):\n        if v: B.set1(k)\n        else:\
    \ B.set0(k)\n\n    def __getitem__(B, k: int):\n        b,r=k>>5,k&31\n      \
    \  return B.levels[0][b]>>r&1\n    \n    def ge(B, k: int):\n        if not B.levels[-1][0]:\
    \ return -1\n        l = -1\n        while True:\n            k,r=k>>5,k&31\n\
    \            if m:=(B.levels[l:=l+1][k]>>r)<<r: break\n            if (k:=k+1)\
    \ >= len(B.levels[l]): return -1\n        while l:m=B.levels[l:=l-1][k:=k<<5|(m&-m).bit_length()-1]\n\
    \        return k<<5|(m&-m).bit_length()-1\n    \n    def le(B, k: int):\n   \
    \     if not B.levels[-1][0]: return -1\n        l = -1\n        while True:\n\
    \            k,r=k>>5,k&31\n            if m:=B.levels[l:=l+1][k]&((1<<(r+1))-1):\
    \ break\n            if (k:=k-1)<0: return -1\n        while l:m=B.levels[l:=l-1][k:=k<<5|m.bit_length()-1]\n\
    \        return k<<5|m.bit_length()-1\nimport os\nfrom __pypy__ import builders\n\
    sb = builders.StringBuilder()\nappend = sb.append\nimport sys\n\nif __name__ ==\
    \ \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/predecessor_problem\n\
    \ndef main():\n    N, Q = map(int, sys.stdin.readline().split())\n    T = sys.stdin.readline()\n\
    \    B = BitsetTree(T)\n    for _ in range(Q):\n        c, k = sys.stdin.readline().split()\n\
    \        k = int(k)\n        if c == '0':\n            B[k] = 1\n        elif\
    \ c == '1':\n            B[k] = 0\n        elif c == '2':\n            append(str(B[k]))\n\
    \            append('\\n')\n        elif c == '3':\n            append(str(B.ge(k)))\n\
    \            append('\\n')\n        elif c == '4':\n            append(str(B.le(k)))\n\
    \            append('\\n')\n    os.write(1, sb.build().encode())\n\nfrom cp_library.ds.tree.bitset_tree_cls\
    \ import BitsetTree\nimport os\nfrom __pypy__ import builders\nsb = builders.StringBuilder()\n\
    append = sb.append\nimport sys\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/ds/tree/bitset_tree_cls.py
  - cp_library/alg/dp/min2_fn.py
  - cp_library/ds/array/u32f_fn.py
  isVerificationFile: true
  path: test/library-checker/data-structure/predecessor_problem.test.py
  requiredBy: []
  timestamp: '2025-07-09 08:31:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/predecessor_problem.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/predecessor_problem.test.py
- /verify/test/library-checker/data-structure/predecessor_problem.test.py.html
title: test/library-checker/data-structure/predecessor_problem.test.py
---
