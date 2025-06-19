---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/min2_fn.py
    title: cp_library/alg/dp/min2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u32f_fn.py
    title: cp_library/ds/array/u32f_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/predecessor_problem.test.py
    title: test/library-checker/data-structure/predecessor_problem.test.py
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
    \n\ndef min2(a, b):\n    return a if a < b else b\n\n\nfrom array import array\n\
    def u32f(N: int, elm: int = 0):     return array('I', (elm,))*N  # unsigned int\n\
    \n\nclass BitsetTree:\n    def __init__(B, S: str):\n        B.N = N = len(S)\n\
    \        L = u32f((N+31)>>5)\n        for k,c in enumerate(S):\n            k,r\
    \ = k>>5,k&31\n            if c=='1': L[k]|=1<<r\n        B.levels = [L]\n   \
    \     while (N := len(L := B.levels[-1])) > 1:\n            A = u32f((N+31)>>5)\n\
    \            for i in range(0,N,32):\n                a=j=0;r=min2(i+32,N)\n \
    \               while i+j<r:a|=(0<L[i+j])<<j;j+=1\n                A[i>>5]=a\n\
    \            B.levels.append(A)\n        B.depth = len(B.levels)\n\n    def set0(B,\
    \ k):\n        if B.levels[0][k>>5]>>(k&31)&1: \n            l = -1\n        \
    \    while (l:=l+1) < B.depth:\n                B.levels[l][k>>5]&=~(1<<(k&31));k>>=5\n\
    \                if B.levels[l][k]: break\n\n    def set1(B, k):\n        if not\
    \ B.levels[0][k>>5]>>(k&31)&1: \n            l = -1\n            while (l:=l+1)\
    \ < B.depth: B.levels[l][k>>5]|=1<<(k&31);k>>=5\n\n    def __setitem__(B, k: int,\
    \ v: int):\n        if v: B.set1(k)\n        else: B.set0(k)\n\n    def __getitem__(B,\
    \ k: int):\n        b,r=k>>5,k&31\n        return B.levels[0][b]>>r&1\n    \n\
    \    def ge(B, k: int):\n        if not B.levels[-1][0]: return -1\n        l\
    \ = -1\n        while True:\n            k,r=k>>5,k&31\n            if m:=(B.levels[l:=l+1][k]>>r)<<r:\
    \ break\n            if (k:=k+1) >= len(B.levels[l]): return -1\n        while\
    \ l:m=B.levels[l:=l-1][k:=k<<5|(m&-m).bit_length()-1]\n        return k<<5|(m&-m).bit_length()-1\n\
    \    \n    def le(B, k: int):\n        if not B.levels[-1][0]: return -1\n   \
    \     l = -1\n        while True:\n            k,r=k>>5,k&31\n            if m:=B.levels[l:=l+1][k]&((1<<(r+1))-1):\
    \ break\n            if (k:=k-1)<0: return -1\n        while l:m=B.levels[l:=l-1][k:=k<<5|m.bit_length()-1]\n\
    \        return k<<5|m.bit_length()-1\n"
  code: "import cp_library.__header__\nfrom cp_library.alg.dp.min2_fn import min2\n\
    from cp_library.ds.array.u32f_fn import u32f\nimport cp_library.ds.__header__\n\
    import cp_library.ds.tree.__header__\n\nclass BitsetTree:\n    def __init__(B,\
    \ S: str):\n        B.N = N = len(S)\n        L = u32f((N+31)>>5)\n        for\
    \ k,c in enumerate(S):\n            k,r = k>>5,k&31\n            if c=='1': L[k]|=1<<r\n\
    \        B.levels = [L]\n        while (N := len(L := B.levels[-1])) > 1:\n  \
    \          A = u32f((N+31)>>5)\n            for i in range(0,N,32):\n        \
    \        a=j=0;r=min2(i+32,N)\n                while i+j<r:a|=(0<L[i+j])<<j;j+=1\n\
    \                A[i>>5]=a\n            B.levels.append(A)\n        B.depth =\
    \ len(B.levels)\n\n    def set0(B, k):\n        if B.levels[0][k>>5]>>(k&31)&1:\
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
    \        return k<<5|m.bit_length()-1\n"
  dependsOn:
  - cp_library/alg/dp/min2_fn.py
  - cp_library/ds/array/u32f_fn.py
  isVerificationFile: false
  path: cp_library/ds/tree/bitset_tree_cls.py
  requiredBy: []
  timestamp: '2025-06-20 03:24:59+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/predecessor_problem.test.py
documentation_of: cp_library/ds/tree/bitset_tree_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/bitset_tree_cls.py
- /library/cp_library/ds/tree/bitset_tree_cls.py.html
title: cp_library/ds/tree/bitset_tree_cls.py
---
