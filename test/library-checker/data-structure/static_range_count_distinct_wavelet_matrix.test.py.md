---
data:
  _extendedDependsOn:
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
    path: cp_library/ds/wavelet/wm_static_cls.py
    title: cp_library/ds/wavelet/wm_static_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_count_distinct
    links:
    - https://judge.yosupo.jp/problem/static_range_count_distinct
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_count_distinct\n\
    \n\ndef main():\n    N, Q = map(int, input().split())\n    A = [int(s) for s in\
    \ input().split()]\n    J = jumps(A)\n    wm = WMStatic(J[:], N)\n    for _ in\
    \ range(Q):\n        l, r = input().split()\n        l, r = int(l), int(r)\n \
    \       append(str(wm.count_below(l+1, l, r))); append('\\n')\n    os.write(1,\
    \ sb.build().encode())\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library \
    \              \n'''\n\n\n\nclass BitArray:\n    def __init__(B, N: int):\n  \
    \      B.N, B.Z = N, (N+31)>>5\n        B.bits, B.cnt = u32f(B.Z+1), u32f(B.Z+1)\n\
    \    def build(B):\n        B.bits.pop()\n        for i,b in enumerate(B.bits):\
    \ B.cnt[i+1] = B.cnt[i]+popcnt32(b)\n        B.bits.append(1)\n    def __len__(B):\
    \ return B.N\n    def __getitem__(B, i: int): return B.bits[i>>5]>>(31-(i&31))&1\n\
    \    def set0(B, i: int): B.bits[i>>5]&=~(1<<31-(i&31))\n    def set1(B, i: int):\
    \ B.bits[i>>5]|=1<<31-(i&31)\n    def count0(B, r: int): return r-B.count1(r)\n\
    \    def count1(B, r: int): return B.cnt[r>>5]+popcnt32(B.bits[r>>5]>>32-(r&31))\n\
    \    def select0(B, k: int):\n        if not 0<=k<B.N-B.cnt[-1]: return -1\n \
    \       l,r,k=0,B.N,k+1\n        while 1<r-l:\n            if B.count0(m:=(l+r)>>1)<k:l=m\n\
    \            else:r=m\n        return l\n    def select1(B, k: int):\n       \
    \ if not 0<=k<B.cnt[-1]: return -1\n        l,r,k=0,B.N,k+1\n        while 1<r-l:\n\
    \            if B.count1(m:=(l+r)>>1)<k:l=m\n            else:r=m\n        return\
    \ l\n\n\ndef popcnt32(x):\n    x = ((x >> 1)  & 0x55555555) + (x & 0x55555555)\n\
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
    \ else-1\n\ndef pack_sm(N: int): s=N.bit_length(); return s,(1<<s)-1\ndef pack_dec(ab:\
    \ int, s: int, m: int): return ab>>s,ab&m\ndef jumps(A: list[int]):\n    s, m\
    \ = pack_sm((N := len(A))-1)\n    R, V = [0]*N, [0]*N\n    for i,a in enumerate(A):\
    \ A[i] = a<<s|i\n    A.sort()\n    r = p = -1\n    for ai in A:\n        a, i\
    \ = pack_dec(ai, s, m)\n        if a != p: r += 1; p = a\n        R[i], V[r] =\
    \ V[r], i+1\n    return R\n\nimport sys,os\nfrom __pypy__ import builders # type:\
    \ ignore\nsb = builders.StringBuilder()\nappend = sb.append\ndef input(): return\
    \ sys.stdin.buffer.readline().strip()\n\nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_count_distinct\n\
    \n\ndef main():\n    N, Q = map(int, input().split())\n    A = [int(s) for s in\
    \ input().split()]\n    J = jumps(A)\n    wm = WMStatic(J[:], N)\n    for _ in\
    \ range(Q):\n        l, r = input().split()\n        l, r = int(l), int(r)\n \
    \       append(str(wm.count_below(l+1, l, r))); append('\\n')\n    os.write(1,\
    \ sb.build().encode())\n\nfrom cp_library.ds.wavelet.wm_static_cls import WMStatic\n\
    from cp_library.bit.pack.pack_sm_fn import pack_sm\nfrom cp_library.bit.pack.pack_dec_fn\
    \ import pack_dec\ndef jumps(A: list[int]):\n    s, m = pack_sm((N := len(A))-1)\n\
    \    R, V = [0]*N, [0]*N\n    for i,a in enumerate(A): A[i] = a<<s|i\n    A.sort()\n\
    \    r = p = -1\n    for ai in A:\n        a, i = pack_dec(ai, s, m)\n       \
    \ if a != p: r += 1; p = a\n        R[i], V[r] = V[r], i+1\n    return R\n\nimport\
    \ sys,os\nfrom __pypy__ import builders # type: ignore\nsb = builders.StringBuilder()\n\
    append = sb.append\ndef input(): return sys.stdin.buffer.readline().strip()\n\n\
    if __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/ds/wavelet/wm_static_cls.py
  - cp_library/bit/pack/pack_sm_fn.py
  - cp_library/bit/pack/pack_dec_fn.py
  - cp_library/ds/wavelet/bit_array_cls.py
  - cp_library/bit/popcnt32_fn.py
  - cp_library/ds/array/u32f_fn.py
  isVerificationFile: true
  path: test/library-checker/data-structure/static_range_count_distinct_wavelet_matrix.test.py
  requiredBy: []
  timestamp: '2025-05-20 13:05:58+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/static_range_count_distinct_wavelet_matrix.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/static_range_count_distinct_wavelet_matrix.test.py
- /verify/test/library-checker/data-structure/static_range_count_distinct_wavelet_matrix.test.py.html
title: test/library-checker/data-structure/static_range_count_distinct_wavelet_matrix.test.py
---
