---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/icoord_compress_fn.py
    title: cp_library/alg/iter/icoord_compress_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack_sm_fn.py
    title: cp_library/bit/pack_sm_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnt32_fn.py
    title: cp_library/bit/popcnt32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array_init_fn.py
    title: cp_library/ds/array_init_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/range_kth_smallest.test.py
    title: test/library-checker/data-structure/range_kth_smallest.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/static_range_frequency_wavelet_matrix.test.py
    title: test/library-checker/data-structure/static_range_frequency_wavelet_matrix.test.py
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
    \nclass BitArray:\n    def __init__(B, N: int, H: int):\n        B.N, B.Z, B.H\
    \ = N, (N+31)>>5, H\n        B.bits, B.pre = u32f(B.Z), u32f(B.Z+1)\n    def build(B):\n\
    \        for i,b in enumerate(B.bits): B.pre[i+1] = B.pre[i]+popcnt32(b)\n   \
    \     B.bits.append(0)\n        B.T0, B.T1 = B.N-B.pre[-1], B.pre[-1]\n    def\
    \ __len__(B): return B.N\n    def __getitem__(B, i: int): return B.bits[i>>5]>>(31-(i&31))&1\n\
    \    def set0(B, i: int): B.bits[i>>5]&=~(1<<31-(i&31))\n    def set1(B, i: int):\
    \ B.bits[i>>5]|=1<<31-(i&31)\n    def rank0(B, r: int): return r-B.rank1(r)\n\
    \    def rank1(B, r: int): return B.pre[r>>5]+popcnt32(B.bits[r>>5]>>32-(r&31))\n\
    \    def select0(B, k: int):\n        if not 0<=k<B.N-B.pre[-1]: return -1\n \
    \       l,r,k=0,B.Z,k+1\n        while 1<r-l:\n            if B.rank0(m:=(l+r)>>1)<k:l=m\n\
    \            else:r=m\n        return l\n    def select1(B, k: int):\n       \
    \ if not 0<=k<B.pre[-1]: return -1\n        l,r,k=0,B.Z,k+1\n        while 1<r-l:\n\
    \            if B.rank1(m:=(l+r)>>1)<k:l=m\n            else:r=m\n        return\
    \ l\n\n    def next_range(B, bit: int, l: int, r: int):\n        if bit: return\
    \ B.T0+B.rank1(l), B.T0+B.rank1(r)\n        else: return B.rank0(l), B.rank0(r)\n\
    \nclass WaveletMatrix:\n    def __init__(W,A):\n        A,W.V = icoord_compress(A)\n\
    \        W.N=N=len(A); W.H=(len(W.V)-1).bit_length()\n        W.L,B=[BitArray(N,\
    \ H) for H in range(W.H-1,-1,-1)],[0]*N\n        for L in W.L:\n            x,y,j=-1,N-1,N\n\
    \            while j:y-=A[j:=j-1]>>L.H&1\n            for j,k in enumerate(A):\n\
    \                if k>>L.H&1:B[y:=y+1]=k;L.set1(j)\n                else:B[x:=x+1]=k\n\
    \            A,B=B,A;L.build()\n\n    def _fval(W, x: int, upper: bool = False):\n\
    \        l,r=-1,len(W.V)\n        while 1<r-l:\n            if W.V[m:=(l+r)>>1]<=x:l=m\n\
    \            else:r=m\n        return l + (upper and W.V[l] != x)\n\n    def __contains__(W,\
    \ x: int):\n        return W.V and W.V[W._fval(x)] == x\n\n    def kth(W, l: int,\
    \ r: int, k: int):\n        if k < 0: k = r-l+k\n        s=0\n        for L in\
    \ W.L:\n            l, r = l-(l1:=L.rank1(l)), r-(r1:=L.rank1(r))\n          \
    \  if k>=r-l:s|=1<<L.H;k-=r-l;l,r=L.T0+l1,L.T0+r1\n        return W.V[s]\n\n \
    \   def rank(W, x: int, r: int): return W.range_rank(0, r, x)\n    def range_rank(W,\
    \ l: int, r: int, x: int):\n        if l >= r or not W.V or x != W.V[x := W._fval(x)]:\
    \ return -1\n        for L in W.L: l, r = L.next_range(L[x], l, r)\n        return\
    \ r-l\n    \n    def range_freq(W, l: int, r: int, x: int):\n        \"\"\"\n\
    \        l, r: Range in the original array (0-indexed, half-open)\n\n        x:\
    \ Value\n\n        Returns: Number of elements in the range equal to x\n     \
    \   \"\"\"\n        if l >= r or not W.V or x != W.V[x := W._fval(x)]: return\
    \ 0\n        return W._rect_freq(l, r, x+1)-W._rect_freq(l, r, x)\n    \n    def\
    \ rect_freq(W, l: int, r: int, a: int, b: int):\n        \"\"\"\n        l, r:\
    \ Range in the original array (0-indexed, half-open)\n\n        a, b: Value range\
    \ (half-open)\n\n        Returns: Number of elements in the range satisfying the\
    \ condition\n        \"\"\"\n        if l >= r or not W.V or (a := W._fval(a,\
    \ True)) >= (b := W._fval(b, True)): return 0\n        return W._rect_freq(l,\
    \ r, b)-W._rect_freq(l, r, a)\n\n    def _rect_freq(W, l: int, r: int, u: int):\n\
    \        if u.bit_length() > W.H: return r-l\n        cnt = 0\n        for L in\
    \ W.L:\n            l, r = l-(l1:=L.rank1(l)), r-(r1:=L.rank1(r))\n          \
    \  if u>>L.H&1:cnt+=r-l;l,r=L.T0+l1,L.T0+r1\n        return cnt\n\n\n\n\ndef icoord_compress(A:\
    \ list[int]):\n    s, m = pack_sm((N := len(A))-1)\n    R, V = [0]*N, [0]*N\n\
    \    for i,a in enumerate(A): A[i] = a<<s|i\n    A.sort()\n    r = p = -1\n  \
    \  for ai in A:\n        a, i = pack_dec(ai, s, m)\n        if a != p: V[r:=r+1]\
    \ = p = a\n        R[i] = r\n    del V[r+1:]\n    return R, V\n\n\n\ndef pack_sm(N:\
    \ int):\n    s = N.bit_length()\n    return s, (1<<s)-1\n\ndef pack_enc(a: int,\
    \ b: int, s: int):\n    return a << s | b\n    \ndef pack_dec(ab: int, s: int,\
    \ m: int):\n    return ab >> s, ab & m\n\ndef pack_indices(A, s):\n    return\
    \ [a << s | i for i,a in enumerate(A)]\n\ndef popcnt32(x):\n    x = ((x >> 1)\
    \  & 0x55555555) + (x & 0x55555555)\n    x = ((x >> 2)  & 0x33333333) + (x & 0x33333333)\n\
    \    x = ((x >> 4)  & 0x0f0f0f0f) + (x & 0x0f0f0f0f)\n    x = ((x >> 8)  & 0x00ff00ff)\
    \ + (x & 0x00ff00ff)\n    x = ((x >> 16) & 0x0000ffff) + (x & 0x0000ffff)\n  \
    \  return x\nfrom array import array\n\ndef i8f(N: int, elm: int = 0):      return\
    \ array('b', (elm,))*N  # signed char\ndef u8f(N: int, elm: int = 0):      return\
    \ array('B', (elm,))*N  # unsigned char\ndef i16f(N: int, elm: int = 0):     return\
    \ array('h', (elm,))*N  # signed short\ndef u16f(N: int, elm: int = 0):     return\
    \ array('H', (elm,))*N  # unsigned short\ndef i32f(N: int, elm: int = 0):    \
    \ return array('i', (elm,))*N  # signed int\ndef u32f(N: int, elm: int = 0): \
    \    return array('I', (elm,))*N  # unsigned int\ndef i64f(N: int, elm: int =\
    \ 0):     return array('q', (elm,))*N  # signed long long\ndef u64f(N: int, elm:\
    \ int = 0):     return array('Q', (elm,))*N  # unsigned long long\ndef f32f(N:\
    \ int, elm: float = 0.0): return array('f', (elm,))*N  # float\ndef f64f(N: int,\
    \ elm: float = 0.0): return array('d', (elm,))*N  # double\n\ndef i8a(init = None):\
    \  return array('b') if init is None else array('b', init)  # signed char\ndef\
    \ u8a(init = None):  return array('B') if init is None else array('B', init) \
    \ # unsigned char\ndef i16a(init = None): return array('h') if init is None else\
    \ array('h', init)  # signed short\ndef u16a(init = None): return array('H') if\
    \ init is None else array('H', init)  # unsigned short\ndef i32a(init = None):\
    \ return array('i') if init is None else array('i', init)  # signed int\ndef u32a(init\
    \ = None): return array('I') if init is None else array('I', init)  # unsigned\
    \ int\ndef i64a(init = None): return array('q') if init is None else array('q',\
    \ init)  # signed long long\ndef u64a(init = None): return array('Q') if init\
    \ is None else array('Q', init)  # unsigned long long\ndef f32a(init = None):\
    \ return array('f') if init is None else array('f', init)  # float\ndef f64a(init\
    \ = None): return array('d') if init is None else array('d', init)  # double\n\
    \ni8_max = (1 << 7)-1\nu8_max = (1 << 8)-1\ni16_max = (1 << 15)-1\nu16_max = (1\
    \ << 16)-1\ni32_max = (1 << 31)-1\nu32_max = (1 << 32)-1\ni64_max = (1 << 63)-1\n\
    u64_max = (1 << 64)-1\n"
  code: "import cp_library.ds.__header__\n\nclass BitArray:\n    def __init__(B, N:\
    \ int, H: int):\n        B.N, B.Z, B.H = N, (N+31)>>5, H\n        B.bits, B.pre\
    \ = u32f(B.Z), u32f(B.Z+1)\n    def build(B):\n        for i,b in enumerate(B.bits):\
    \ B.pre[i+1] = B.pre[i]+popcnt32(b)\n        B.bits.append(0)\n        B.T0, B.T1\
    \ = B.N-B.pre[-1], B.pre[-1]\n    def __len__(B): return B.N\n    def __getitem__(B,\
    \ i: int): return B.bits[i>>5]>>(31-(i&31))&1\n    def set0(B, i: int): B.bits[i>>5]&=~(1<<31-(i&31))\n\
    \    def set1(B, i: int): B.bits[i>>5]|=1<<31-(i&31)\n    def rank0(B, r: int):\
    \ return r-B.rank1(r)\n    def rank1(B, r: int): return B.pre[r>>5]+popcnt32(B.bits[r>>5]>>32-(r&31))\n\
    \    def select0(B, k: int):\n        if not 0<=k<B.N-B.pre[-1]: return -1\n \
    \       l,r,k=0,B.Z,k+1\n        while 1<r-l:\n            if B.rank0(m:=(l+r)>>1)<k:l=m\n\
    \            else:r=m\n        return l\n    def select1(B, k: int):\n       \
    \ if not 0<=k<B.pre[-1]: return -1\n        l,r,k=0,B.Z,k+1\n        while 1<r-l:\n\
    \            if B.rank1(m:=(l+r)>>1)<k:l=m\n            else:r=m\n        return\
    \ l\n\n    def next_range(B, bit: int, l: int, r: int):\n        if bit: return\
    \ B.T0+B.rank1(l), B.T0+B.rank1(r)\n        else: return B.rank0(l), B.rank0(r)\n\
    \nclass WaveletMatrix:\n    def __init__(W,A):\n        A,W.V = icoord_compress(A)\n\
    \        W.N=N=len(A); W.H=(len(W.V)-1).bit_length()\n        W.L,B=[BitArray(N,\
    \ H) for H in range(W.H-1,-1,-1)],[0]*N\n        for L in W.L:\n            x,y,j=-1,N-1,N\n\
    \            while j:y-=A[j:=j-1]>>L.H&1\n            for j,k in enumerate(A):\n\
    \                if k>>L.H&1:B[y:=y+1]=k;L.set1(j)\n                else:B[x:=x+1]=k\n\
    \            A,B=B,A;L.build()\n\n    def _fval(W, x: int, upper: bool = False):\n\
    \        l,r=-1,len(W.V)\n        while 1<r-l:\n            if W.V[m:=(l+r)>>1]<=x:l=m\n\
    \            else:r=m\n        return l + (upper and W.V[l] != x)\n\n    def __contains__(W,\
    \ x: int):\n        return W.V and W.V[W._fval(x)] == x\n\n    def kth(W, l: int,\
    \ r: int, k: int):\n        if k < 0: k = r-l+k\n        s=0\n        for L in\
    \ W.L:\n            l, r = l-(l1:=L.rank1(l)), r-(r1:=L.rank1(r))\n          \
    \  if k>=r-l:s|=1<<L.H;k-=r-l;l,r=L.T0+l1,L.T0+r1\n        return W.V[s]\n\n \
    \   def rank(W, x: int, r: int): return W.range_rank(0, r, x)\n    def range_rank(W,\
    \ l: int, r: int, x: int):\n        if l >= r or not W.V or x != W.V[x := W._fval(x)]:\
    \ return -1\n        for L in W.L: l, r = L.next_range(L[x], l, r)\n        return\
    \ r-l\n    \n    def range_freq(W, l: int, r: int, x: int):\n        \"\"\"\n\
    \        l, r: Range in the original array (0-indexed, half-open)\n\n        x:\
    \ Value\n\n        Returns: Number of elements in the range equal to x\n     \
    \   \"\"\"\n        if l >= r or not W.V or x != W.V[x := W._fval(x)]: return\
    \ 0\n        return W._rect_freq(l, r, x+1)-W._rect_freq(l, r, x)\n    \n    def\
    \ rect_freq(W, l: int, r: int, a: int, b: int):\n        \"\"\"\n        l, r:\
    \ Range in the original array (0-indexed, half-open)\n\n        a, b: Value range\
    \ (half-open)\n\n        Returns: Number of elements in the range satisfying the\
    \ condition\n        \"\"\"\n        if l >= r or not W.V or (a := W._fval(a,\
    \ True)) >= (b := W._fval(b, True)): return 0\n        return W._rect_freq(l,\
    \ r, b)-W._rect_freq(l, r, a)\n\n    def _rect_freq(W, l: int, r: int, u: int):\n\
    \        if u.bit_length() > W.H: return r-l\n        cnt = 0\n        for L in\
    \ W.L:\n            l, r = l-(l1:=L.rank1(l)), r-(r1:=L.rank1(r))\n          \
    \  if u>>L.H&1:cnt+=r-l;l,r=L.T0+l1,L.T0+r1\n        return cnt\n\nfrom cp_library.alg.iter.icoord_compress_fn\
    \ import icoord_compress\nfrom cp_library.bit.popcnt32_fn import popcnt32\nfrom\
    \ cp_library.ds.array_init_fn import u32f\n"
  dependsOn:
  - cp_library/alg/iter/icoord_compress_fn.py
  - cp_library/bit/popcnt32_fn.py
  - cp_library/ds/array_init_fn.py
  - cp_library/bit/pack_sm_fn.py
  isVerificationFile: false
  path: cp_library/ds/wavelet_matrix_cls.py
  requiredBy: []
  timestamp: '2025-05-06 22:58:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/static_range_frequency_wavelet_matrix.test.py
  - test/library-checker/data-structure/range_kth_smallest.test.py
documentation_of: cp_library/ds/wavelet_matrix_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/wavelet_matrix_cls.py
- /library/cp_library/ds/wavelet_matrix_cls.py.html
title: cp_library/ds/wavelet_matrix_cls.py
---
