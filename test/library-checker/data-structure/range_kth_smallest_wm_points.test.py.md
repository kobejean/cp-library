---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/bisect_left_fn.py
    title: cp_library/alg/divcon/bisect_left_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/cmpr/coord_compress_fn.py
    title: cp_library/alg/iter/cmpr/coord_compress_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_dec_fn.py
    title: cp_library/bit/pack/pack_dec_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_sm_fn.py
    title: cp_library/bit/pack/pack_sm_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnt32_fn.py
    title: cp_library/bit/popcnt32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u32f_fn.py
    title: cp_library/ds/array/u32f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/bit_array_cls.py
    title: cp_library/ds/wavelet/bit_array_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_compressed_cls.py
    title: cp_library/ds/wavelet/wm_compressed_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_points_cls.py
    title: cp_library/ds/wavelet/wm_points_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_static_cls.py
    title: cp_library/ds/wavelet/wm_static_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_kth_smallest
    links:
    - https://judge.yosupo.jp/problem/range_kth_smallest
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_kth_smallest\n\
    \ndef main():\n    N, Q = map(int, sys.stdin.readline().split())\n    X = [*range(N)]\n\
    \    Y = [int(s) for s in sys.stdin.readline().split()]\n    wm = WMPoints(X,\
    \ Y)\n    for _ in range(Q):\n        l, r, k = sys.stdin.readline().split()\n\
    \        append(str(wm.kth(int(k), int(l), int(r)))); append('\\n')\n    os.write(1,\
    \ sb.build().encode())\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library \
    \              \n'''\n\n\n\ndef bisect_left(A, x, l, r):\n    while l<r:\n   \
    \     if A[m:=(l+r)>>1]<x:l=m+1\n        else:r=m\n    return l\n\n\n\ndef coord_compress(A:\
    \ list[int], distinct = False):\n    s, m = pack_sm((N := len(A))-1); R, V = [0]*N,\
    \ [a<<s|i for i,a in enumerate(A)]; V.sort()\n    if distinct:\n        for r,\
    \ ai in enumerate(V): a, i = pack_dec(ai, s, m); R[i], V[r] = r, a\n    else:\n\
    \        r = p = -1\n        for ai in V:\n            a, i = pack_dec(ai, s,\
    \ m)\n            if a != p: r = r+1; V[r] = p = a\n            R[i] = r\n   \
    \     del V[r+1:]\n    return R, V\n\n\n\ndef pack_dec(ab: int, s: int, m: int):\
    \ return ab>>s,ab&m\ndef pack_sm(N: int): s=N.bit_length(); return s,(1<<s)-1\n\
    \n\n\nclass BitArray:\n    def __init__(B, N: int):\n        B.N, B.Z = N, (N+31)>>5\n\
    \        B.bits, B.cnt = u32f(B.Z+1), u32f(B.Z+1)\n    def build(B):\n       \
    \ B.bits.pop()\n        for i,b in enumerate(B.bits): B.cnt[i+1] = B.cnt[i]+popcnt32(b)\n\
    \        B.bits.append(1)\n    def __len__(B): return B.N\n    def __getitem__(B,\
    \ i: int): return B.bits[i>>5]>>(31-(i&31))&1\n    def set0(B, i: int): B.bits[i>>5]&=~(1<<31-(i&31))\n\
    \    def set1(B, i: int): B.bits[i>>5]|=1<<31-(i&31)\n    def count0(B, r: int):\
    \ return r-B.count1(r)\n    def count1(B, r: int): return B.cnt[r>>5]+popcnt32(B.bits[r>>5]>>32-(r&31))\n\
    \    def select0(B, k: int):\n        if not 0<=k<B.N-B.cnt[-1]: return -1\n \
    \       l,r,k=0,B.N,k+1\n        while 1<r-l:\n            if B.count0(m:=(l+r)>>1)<k:l=m\n\
    \            else:r=m\n        return l\n    def select1(B, k: int):\n       \
    \ if not 0<=k<B.cnt[-1]: return -1\n        l,r,k=0,B.N,k+1\n        while 1<r-l:\n\
    \            if B.count1(m:=(l+r)>>1)<k:l=m\n            else:r=m\n        return\
    \ l\n\ndef popcnt32(x):\n    x = ((x >> 1)  & 0x55555555) + (x & 0x55555555)\n\
    \    x = ((x >> 2)  & 0x33333333) + (x & 0x33333333)\n    x = ((x >> 4)  & 0x0f0f0f0f)\
    \ + (x & 0x0f0f0f0f)\n    x = ((x >> 8)  & 0x00ff00ff) + (x & 0x00ff00ff)\n  \
    \  x = ((x >> 16) & 0x0000ffff) + (x & 0x0000ffff)\n    return x\nif hasattr(int,\
    \ 'bit_count'):\n    popcnt32 = int.bit_count\n\nfrom array import array\ndef\
    \ u32f(N: int, elm: int = 0):     return array('I', (elm,))*N  # unsigned int\n\
    \nclass WMStatic:\n    class Level(BitArray):\n        def __init__(L, N: int,\
    \ H: int):\n            super().__init__(N)\n            L.H = H\n        def\
    \ build(L):\n            super().build()\n            L.T0, L.T1 = L.N-L.cnt[-1],\
    \ L.cnt[-1]\n        def pos(L, bit: int, i: int): return L.T0+L.count1(i) if\
    \ bit else L.count0(i)\n        def pos2(L, bit: int, i: int, j: int): return\
    \ (L.T0+L.count1(i), L.T0+L.count1(j)) if bit else (L.count0(i), L.count0(j))\n\
    \    def __init__(wm,A,Amax:int=None):wm._build(A,[0]*len(A),max(A,default=0)if\
    \ Amax is None else Amax)\n    def _build(wm, A, nA, Amax):wm.N,wm.H=len(A),Amax.bit_length();wm._build_levels(A,nA)\n\
    \    def _build_levels(wm, A, nA):\n        wm.up=[wm.Level(wm.N,H) for H in range(wm.H)];wm.down=wm.up[::-1]\n\
    \        for L in wm.down:\n            x,y,i=-1,wm.N-1,wm.N\n            while\
    \ i:y-=A[i:=i-1]>>L.H&1\n            for i,a in enumerate(A):\n              \
    \  if a>>L.H&1:nA[y:=y+1]=a;L.set1(i)\n                else:nA[x:=x+1]=a\n   \
    \         A,nA=nA,A;L.build()\n    def __getitem__(wm,i):\n        y=0\n     \
    \   for L in wm.down:y=y<<1|(bit:=L[i]);i=L.pos(bit,i)\n        return y\n   \
    \ def kth(wm, k: int, l: int, r: int):\n        '''Returns the `k+1`-th value\
    \ in sorted order of values in range `[l, r)`'''\n        s=0\n        for L in\
    \ wm.down:\n            l,r=l-(l1:=L.count1(l)),r-(r1:=L.count1(r))\n        \
    \    if k>=r-l:s|=1<<L.H;k-=r-l;l,r=L.T0+l1,L.T0+r1\n        return s\n    def\
    \ select(wm, y: int, k: int, l: int = 0, r: int = -1):\n        '''Returns the\
    \ index of the `k+1`-th occurance of `y` in range `[l, r)`'''\n        if not(0<=y<1<<wm.H):return-1\n\
    \        if r==-1:r=wm.N-1\n        for L in wm.down:l,r=L.pos2(L[y],l,r)\n  \
    \      if not l<=(i:=l+k)<r:return-1\n        for L in wm.up:\n            if\
    \ y>>L.H&1:i=L.select1(i-L.T0)\n            else:i=L.select0(i)\n        return\
    \ i\n    def rank(wm, y: int, r: int): return wm.rank_range(y, 0, r)\n    def\
    \ rank_range(wm, y: int, l: int, r: int):\n        if l >= r: return 0\n     \
    \   for L in wm.down:l,r=L.pos2(L[y],l,r)\n        return r-l\n    def count_at(wm,\
    \ y: int, l: int, r: int):\n        '''Count how many `y` values are in range\
    \ `[l,r)` '''\n        if l >= r: return 0\n        return wm._cnt(y+1, l, r)-wm._cnt(y,\
    \ l, r)\n    def count_below(wm, u: int, l: int, r: int):\n        '''Count `i`'s\
    \ in `[l,r)` such that `A[i] < u` '''\n        return wm._cnt(u, l, r)\n    def\
    \ count_between(wm, d: int, u: int, l: int, r: int):\n        '''Count `i`'s in\
    \ `[l,r)` such that `d <= A[i] < u` '''\n        if l >= r or d >= u: return 0\n\
    \        return wm._cnt(u, l, r)-wm._cnt(d, l, r)\n    def _cnt(wm, u: int, l:\
    \ int, r: int):\n        if u<=0:return 0\n        if wm.H<u.bit_length():return\
    \ r-l\n        cnt=0\n        for L in wm.down:\n            l,r=l-(l1:=L.count1(l)),r-(r1:=L.count1(r))\n\
    \            if u>>L.H&1:cnt+=r-l;l,r=L.T0+l1,L.T0+r1\n        return cnt\n  \
    \  def prev_val(wm,u:int,l:int,r:int):return wm.kth(cnt-1, l, r)if(cnt:=wm._cnt(u,l,r))else-1\n\
    \    def next_val(wm,d:int,l:int,r:int):return wm.kth(cnt, l, r)if(cnt:=wm._cnt(d,l,r))<r-l\
    \ else-1\n\nclass WMCompressed(WMStatic):\n    def __init__(wm,A):A,wm.Y=coord_compress(A);super().__init__(A,len(wm.Y)-1)\n\
    \    def _didx(wm,y:int):return bisect_left(wm.Y,y,0,len(wm.Y))\n    def _yidx(wm,y:int):return\
    \ i if(i:=wm._didx(y))<len(wm.Y)and wm.Y[i]==y else-1\n    def __contains__(wm,y:int):return(i:=wm._didx(y))<len(wm.Y)and\
    \ wm.Y[i]==y\n    def kth(wm,k,l,r):return wm.Y[super().kth(k,l,r)]\n    def select(wm,y,k,l=0,r=-1):return\
    \ super().select(y,k,l,r)if~(y:=wm._yidx(y))else-1\n    def rank_range(wm,y,l,r):return\
    \ super().rank_range(y,l,r)if~(y:=wm._yidx(y))else 0\n    def count_at(wm,y,l,r):return\
    \ super().count_at(y,l,r)if~(y:=wm._yidx(y))else 0\n    def count_below(wm,u,l,r):return\
    \ super().count_below(wm._didx(u),l,r)\n    def count_between(wm,d,u,l,r):return\
    \ super().count_between(wm._didx(d),wm._didx(u),l,r)\n    def prev_val(wm,u,l,r):return\
    \ super().prev_val(wm._didx(u),l,r)\n    def next_val(wm,d,l,r):return super().next_val(wm._didx(d),l,r)\n\
    \nclass WMPoints(WMCompressed):\n    def __init__(wm,X,Y):\n        wm.I,wm.X=coord_compress(X,distinct=True);A,wm.Y=coord_compress(Y);nA=[0]*len(Y)\n\
    \        for i,j in enumerate(wm.I):nA[j]=A[i]\n        wm._build(nA,A,len(wm.Y)-1)\n\
    \    def _lidx(wm,x):return bisect_left(wm.X,x,0,len(wm.X))\n    def __getitem__(wm,i):return\
    \ super().__getitem__(wm.I[i])\n    def kth(wm,k,l,r):return super().kth(k,wm._lidx(l),wm._lidx(r))\n\
    \    def select(wm,y,k,l=0,r=-1):return super().select(y,k,wm._lidx(l),wm._lidx(r))\n\
    \    def rank_range(wm,y,l,r):return super().rank_range(y,wm._lidx(l),wm._lidx(r))\n\
    \    def count_at(wm,y,l,r):return super().count_at(y,wm._lidx(l),wm._lidx(r))\n\
    \    def count_below(wm,u,l,r):return super().count_below(u,wm._lidx(l),wm._lidx(r))\n\
    \    def count_between(wm,d,u,l,r):return super().count_between(d,u,wm._lidx(l),wm._lidx(r))\n\
    \    def prev_val(wm,u,l,r):return super().prev_val(u,wm._lidx(l),wm._lidx(r))\n\
    \    def next_val(wm,d,l,r):return super().next_val(d,wm._lidx(l),wm._lidx(r))\n\
    import os\nimport sys\nfrom __pypy__ import builders\nsb = builders.StringBuilder()\n\
    append = sb.append\n\nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_kth_smallest\n\
    \ndef main():\n    N, Q = map(int, sys.stdin.readline().split())\n    X = [*range(N)]\n\
    \    Y = [int(s) for s in sys.stdin.readline().split()]\n    wm = WMPoints(X,\
    \ Y)\n    for _ in range(Q):\n        l, r, k = sys.stdin.readline().split()\n\
    \        append(str(wm.kth(int(k), int(l), int(r)))); append('\\n')\n    os.write(1,\
    \ sb.build().encode())\n\nfrom cp_library.ds.wavelet.wm_points_cls import WMPoints\n\
    import os\nimport sys\nfrom __pypy__ import builders\nsb = builders.StringBuilder()\n\
    append = sb.append\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/ds/wavelet/wm_points_cls.py
  - cp_library/alg/divcon/bisect_left_fn.py
  - cp_library/alg/iter/cmpr/coord_compress_fn.py
  - cp_library/ds/wavelet/wm_compressed_cls.py
  - cp_library/ds/wavelet/wm_static_cls.py
  - cp_library/bit/pack/pack_dec_fn.py
  - cp_library/bit/pack/pack_sm_fn.py
  - cp_library/ds/wavelet/bit_array_cls.py
  - cp_library/bit/popcnt32_fn.py
  - cp_library/ds/array/u32f_fn.py
  isVerificationFile: true
  path: test/library-checker/data-structure/range_kth_smallest_wm_points.test.py
  requiredBy: []
  timestamp: '2025-05-20 13:05:58+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/range_kth_smallest_wm_points.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/range_kth_smallest_wm_points.test.py
- /verify/test/library-checker/data-structure/range_kth_smallest_wm_points.test.py.html
title: test/library-checker/data-structure/range_kth_smallest_wm_points.test.py
---
