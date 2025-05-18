---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/min2_fn.py
    title: cp_library/alg/dp/min2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnt32_fn.py
    title: cp_library/bit/popcnt32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u32f_fn.py
    title: cp_library/ds/array/u32f_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://github.com/tatyam-prime/SortedSet/blob/main/BucketList.py
  bundledCode: "\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\n\n\ndef min2(a, b):\n    return a if a < b else b\nfrom math import\
    \ ceil, sqrt\nfrom typing import TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\n\
    \nclass BitArray:\n    def __init__(B, N: int):\n        B.N, B.Z = N, (N+31)>>5\n\
    \        B.bits, B.cnt = u32f(B.Z+1), u32f(B.Z+1)\n    def build(B):\n       \
    \ B.bits.pop()\n        for i,b in enumerate(B.bits): B.cnt[i+1] = B.cnt[i]+popcnt32(b)\n\
    \        B.bits.append(0)\n    def __len__(B): return B.N\n    def __getitem__(B,\
    \ i: int): return B.bits[i>>5]>>(31-(i&31))&1\n    def set0(B, i: int): B.bits[i>>5]&=~(1<<31-(i&31))\n\
    \    def set1(B, i: int): B.bits[i>>5]|=1<<31-(i&31)\n    def count0(B, r: int):\
    \ return r-B.count1(r)\n    def count1(B, r: int): return B.cnt[r>>5]+popcnt32(B.bits[r>>5]>>32-(r&31))\n\
    \    def select0(B, k: int):\n        if not 0<=k<B.N-B.cnt[-1]: return -1\n \
    \       l,r,k=0,B.N,k+1\n        while 1<r-l:\n            if B.count0(m:=(l+r)>>1)<k:l=m\n\
    \            else:r=m\n        return l\n    def select1(B, k: int):\n       \
    \ if not 0<=k<B.cnt[-1]: return -1\n        l,r,k=0,B.N,k+1\n        while 1<r-l:\n\
    \            if B.count1(m:=(l+r)>>1)<k:l=m\n            else:r=m\n        return\
    \ l\n\n\n\ndef popcnt32(x):\n    x = ((x >> 1)  & 0x55555555) + (x & 0x55555555)\n\
    \    x = ((x >> 2)  & 0x33333333) + (x & 0x33333333)\n    x = ((x >> 4)  & 0x0f0f0f0f)\
    \ + (x & 0x0f0f0f0f)\n    x = ((x >> 8)  & 0x00ff00ff) + (x & 0x00ff00ff)\n  \
    \  x = ((x >> 16) & 0x0000ffff) + (x & 0x0000ffff)\n    return x\nif hasattr(int,\
    \ 'bit_count'):\n    popcnt32 = int.bit_count\n\nfrom array import array\ndef\
    \ u32f(N: int, elm: int = 0):     return array('I', (elm,))*N  # unsigned int\n\
    \n# Inspired by: https://github.com/tatyam-prime/SortedSet/blob/main/BucketList.py\n\
    class BitList:\n    BUCKET_RATIO = 16\n    SPLIT_RATIO = 24\n    \n    def __init__(B,\
    \ N: int) -> None:\n        B.N, B.Z = N, (N+31)>>5\n        B = int(ceil(sqrt(B.Z\
    \ / B.BUCKET_RATIO)))\n        M = (B.Z+B-1)//B\n        B.bits = [[0]*(min2(i+M,B.Z)-i)\
    \ for i in range(B)]\n\n    def _insert(B, a: list[int], b: int, i: int, x: int):\n\
    \        n = len(a)\n        if (0x1041042*i)&0x3fffffff<0x1041042:\n        \
    \    a.append(0)\n            n+=1\n        q = (0x1041042*i)>>30\n        r=62-i+b*63\n\
    \        # b, i = divmod(i, 63)\n        # i = 62-i\n        while b<(n:=n-1):a[n]=a[n]>>1|(a[n-1]&1)<<62\n\
    \        m = (1<<(r+1))-1\n        a[b]=a[b]&~m|1<<i|(a[b]&m)>>1\n\n        B.size\
    \ += 1\n        if len(a) > len(B.bits) * B.SPLIT_RATIO:\n            mid = len(a)\
    \ >> 1\n            B.bits[b:b+1] = [a[:mid], a[mid:]]\n\n    def insert(B, i:\
    \ int, x: int):\n        if B.size == 0:\n            if i != 0 and i != -1: raise\
    \ IndexError\n            B.bits.append([x])\n            B.size = 1\n       \
    \     return\n        for b, a in enumerate(B.bits):\n            if i <= len(a):\
    \ return B._insert(a, b, i, x)\n            i -= len(a)\n    \n    def __getitem__(B,\
    \ i: int):\n        for a in B.bits:\n            if i < len(a): return a[i]\n\
    \            i -= len(a)\n        raise IndexError\n    \n    def __setitem__(B,\
    \ i: int, x: int):\n        for a in B.bits:\n            if i < len(a): a[i]\
    \ = x\n            i -= len(a)\n        raise IndexError\n"
  code: "\nimport cp_library.ds.__header__\nfrom cp_library.alg.dp.min2_fn import\
    \ min2\nfrom math import ceil, sqrt\nfrom cp_library.misc.typing import int\n\n\
    class BitArray:\n    def __init__(B, N: int):\n        B.N, B.Z = N, (N+31)>>5\n\
    \        B.bits, B.cnt = u32f(B.Z+1), u32f(B.Z+1)\n    def build(B):\n       \
    \ B.bits.pop()\n        for i,b in enumerate(B.bits): B.cnt[i+1] = B.cnt[i]+popcnt32(b)\n\
    \        B.bits.append(0)\n    def __len__(B): return B.N\n    def __getitem__(B,\
    \ i: int): return B.bits[i>>5]>>(31-(i&31))&1\n    def set0(B, i: int): B.bits[i>>5]&=~(1<<31-(i&31))\n\
    \    def set1(B, i: int): B.bits[i>>5]|=1<<31-(i&31)\n    def count0(B, r: int):\
    \ return r-B.count1(r)\n    def count1(B, r: int): return B.cnt[r>>5]+popcnt32(B.bits[r>>5]>>32-(r&31))\n\
    \    def select0(B, k: int):\n        if not 0<=k<B.N-B.cnt[-1]: return -1\n \
    \       l,r,k=0,B.N,k+1\n        while 1<r-l:\n            if B.count0(m:=(l+r)>>1)<k:l=m\n\
    \            else:r=m\n        return l\n    def select1(B, k: int):\n       \
    \ if not 0<=k<B.cnt[-1]: return -1\n        l,r,k=0,B.N,k+1\n        while 1<r-l:\n\
    \            if B.count1(m:=(l+r)>>1)<k:l=m\n            else:r=m\n        return\
    \ l\n\nfrom cp_library.bit.popcnt32_fn import popcnt32\nfrom cp_library.ds.array.u32f_fn\
    \ import u32f\n\n# Inspired by: https://github.com/tatyam-prime/SortedSet/blob/main/BucketList.py\n\
    class BitList:\n    BUCKET_RATIO = 16\n    SPLIT_RATIO = 24\n    \n    def __init__(B,\
    \ N: int) -> None:\n        B.N, B.Z = N, (N+31)>>5\n        B = int(ceil(sqrt(B.Z\
    \ / B.BUCKET_RATIO)))\n        M = (B.Z+B-1)//B\n        B.bits = [[0]*(min2(i+M,B.Z)-i)\
    \ for i in range(B)]\n\n    def _insert(B, a: list[int], b: int, i: int, x: int):\n\
    \        n = len(a)\n        if (0x1041042*i)&0x3fffffff<0x1041042:\n        \
    \    a.append(0)\n            n+=1\n        q = (0x1041042*i)>>30\n        r=62-i+b*63\n\
    \        # b, i = divmod(i, 63)\n        # i = 62-i\n        while b<(n:=n-1):a[n]=a[n]>>1|(a[n-1]&1)<<62\n\
    \        m = (1<<(r+1))-1\n        a[b]=a[b]&~m|1<<i|(a[b]&m)>>1\n\n        B.size\
    \ += 1\n        if len(a) > len(B.bits) * B.SPLIT_RATIO:\n            mid = len(a)\
    \ >> 1\n            B.bits[b:b+1] = [a[:mid], a[mid:]]\n\n    def insert(B, i:\
    \ int, x: int):\n        if B.size == 0:\n            if i != 0 and i != -1: raise\
    \ IndexError\n            B.bits.append([x])\n            B.size = 1\n       \
    \     return\n        for b, a in enumerate(B.bits):\n            if i <= len(a):\
    \ return B._insert(a, b, i, x)\n            i -= len(a)\n    \n    def __getitem__(B,\
    \ i: int):\n        for a in B.bits:\n            if i < len(a): return a[i]\n\
    \            i -= len(a)\n        raise IndexError\n    \n    def __setitem__(B,\
    \ i: int, x: int):\n        for a in B.bits:\n            if i < len(a): a[i]\
    \ = x\n            i -= len(a)\n        raise IndexError\n"
  dependsOn:
  - cp_library/alg/dp/min2_fn.py
  - cp_library/bit/popcnt32_fn.py
  - cp_library/ds/array/u32f_fn.py
  isVerificationFile: false
  path: cp_library/ds/wavelet/bit_list_cls.py
  requiredBy: []
  timestamp: '2025-05-19 05:52:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/wavelet/bit_list_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/wavelet/bit_list_cls.py
- /library/cp_library/ds/wavelet/bit_list_cls.py.html
title: cp_library/ds/wavelet/bit_list_cls.py
---
