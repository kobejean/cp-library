---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/min2_fn.py
    title: cp_library/alg/dp/min2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array_init_fn.py
    title: cp_library/ds/array_init_fn.py
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
    from array import array\n\ndef i8f(N: int, elm: int = 0):      return array('b',\
    \ (elm,))*N  # signed char\ndef u8f(N: int, elm: int = 0):      return array('B',\
    \ (elm,))*N  # unsigned char\ndef i16f(N: int, elm: int = 0):     return array('h',\
    \ (elm,))*N  # signed short\ndef u16f(N: int, elm: int = 0):     return array('H',\
    \ (elm,))*N  # unsigned short\ndef i32f(N: int, elm: int = 0):     return array('i',\
    \ (elm,))*N  # signed int\ndef u32f(N: int, elm: int = 0):     return array('I',\
    \ (elm,))*N  # unsigned int\ndef i64f(N: int, elm: int = 0):     return array('q',\
    \ (elm,))*N  # signed long long\ndef u64f(N: int, elm: int = 0):     return array('Q',\
    \ (elm,))*N  # unsigned long long\ndef f32f(N: int, elm: float = 0.0): return\
    \ array('f', (elm,))*N  # float\ndef f64f(N: int, elm: float = 0.0): return array('d',\
    \ (elm,))*N  # double\n\ndef i8a(init = None):  return array('b') if init is None\
    \ else array('b', init)  # signed char\ndef u8a(init = None):  return array('B')\
    \ if init is None else array('B', init)  # unsigned char\ndef i16a(init = None):\
    \ return array('h') if init is None else array('h', init)  # signed short\ndef\
    \ u16a(init = None): return array('H') if init is None else array('H', init) \
    \ # unsigned short\ndef i32a(init = None): return array('i') if init is None else\
    \ array('i', init)  # signed int\ndef u32a(init = None): return array('I') if\
    \ init is None else array('I', init)  # unsigned int\ndef i64a(init = None): return\
    \ array('q') if init is None else array('q', init)  # signed long long\ndef u64a(init\
    \ = None): return array('Q') if init is None else array('Q', init)  # unsigned\
    \ long long\ndef f32a(init = None): return array('f') if init is None else array('f',\
    \ init)  # float\ndef f64a(init = None): return array('d') if init is None else\
    \ array('d', init)  # double\n\ni8_max = (1 << 7)-1\nu8_max = (1 << 8)-1\ni16_max\
    \ = (1 << 15)-1\nu16_max = (1 << 16)-1\ni32_max = (1 << 31)-1\nu32_max = (1 <<\
    \ 32)-1\ni64_max = (1 << 63)-1\nu64_max = (1 << 64)-1\n\n\ndef min2(a, b):\n \
    \   return a if a < b else b\n\n\nclass BitsetTree:\n    def __init__(B, S: str):\n\
    \        B.N = N = len(S)\n        L = u32f((N+31)>>5)\n        for k,c in enumerate(S):\n\
    \            k,r = k>>5,k&31\n            if c=='1': L[k]|=1<<r\n        B.levels\
    \ = [L]\n        while (N := len(L := B.levels[-1])) > 1:\n            A = u32f((N+31)>>5)\n\
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
  code: "from cp_library.ds.array_init_fn import u32f\nimport cp_library.__header__\n\
    from cp_library.alg.dp.min2_fn import min2\nimport cp_library.ds.__header__\n\
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
  - cp_library/ds/array_init_fn.py
  - cp_library/alg/dp/min2_fn.py
  isVerificationFile: false
  path: cp_library/ds/tree/bitset_tree_cls.py
  requiredBy: []
  timestamp: '2025-05-06 22:58:43+09:00'
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
