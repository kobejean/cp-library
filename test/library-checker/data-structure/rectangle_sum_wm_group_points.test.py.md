---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/bisect_left_fn.py
    title: cp_library/alg/divcon/bisect_left_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/rank/irank_fn.py
    title: cp_library/alg/iter/rank/irank_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/rank/rank_fn.py
    title: cp_library/alg/iter/rank/rank_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnt32_fn.py
    title: cp_library/bit/popcnt32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u32f_fn.py
    title: cp_library/ds/array/u32f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/presum_cls.py
    title: cp_library/ds/list/presum_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/bit_array_cls.py
    title: cp_library/ds/wavelet/bit_array_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_compressed_cls.py
    title: cp_library/ds/wavelet/wm_compressed_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_group_cls.py
    title: cp_library/ds/wavelet/wm_group_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_group_compressed_cls.py
    title: cp_library/ds/wavelet/wm_group_compressed_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_group_points_cls.py
    title: cp_library/ds/wavelet/wm_group_points_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_monoid_cls.py
    title: cp_library/ds/wavelet/wm_monoid_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_monoid_compressed_cls.py
    title: cp_library/ds/wavelet/wm_monoid_compressed_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_monoid_points_cls.py
    title: cp_library/ds/wavelet/wm_monoid_points_cls.py
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
    PROBLEM: https://judge.yosupo.jp/problem/rectangle_sum
    links:
    - https://judge.yosupo.jp/problem/rectangle_sum
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_sum\n\
    \nfrom operator import add, sub\n\ndef main():\n    N, Q = map(int, input().split())\n\
    \    X, Y, W = [0]*N, [0]*N, [0]*N\n    for i in range(N): X[i], Y[i], W[i] =\
    \ map(int, input().split())\n    wm = WMGroupPoints(add, 0, sub, X, Y, W)\n  \
    \  for i in range(Q): append(str(wm.prod_rect(*map(int, input().split())))); append('\\\
    n')\n    os.write(1, sb.build().encode())\n\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\n\n\ndef irank(A: list[int], distinct = False):\n  \
    \  P = Packer(len(A)-1); V = P.enumerate(A); V.sort()\n    if distinct:\n    \
    \    for r, ai in enumerate(V): a, i = P.dec(ai); A[i], V[r] = r, a\n    elif\
    \ V:\n        r, p = -1, V[-1]+1 # set p to unique value to trigger `if a != p`\
    \ on first elm\n        for ai in V:\n            a, i = P.dec(ai)\n         \
    \   if a!=p: V[r:=r+1] = p = a\n            A[i] = r\n        del V[r+1:]\n  \
    \  return V\n\n\n\nclass Packer:\n    __slots__ = 's', 'm'\n    def __init__(P,\
    \ mx: int): P.s = mx.bit_length(); P.m = (1 << P.s) - 1\n    def enc(P, a: int,\
    \ b: int): return a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return\
    \ x >> P.s, x & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A),\
    \ reverse); return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n\
    \            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n   \
    \         for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\n\ndef rank(A: list[int], distinct = False): return\
    \ (R := list(A)), irank(R, distinct)\n\n\nimport operator\n\nclass Presum:\n \
    \   def __init__(P, A: list, op=operator.add, e = 0, diff=operator.sub):\n   \
    \     P.N = len(A); P.op, P.e, P.diff, P.pre = op, e, diff, [e]*(P.N+1)\n    \
    \    for i,a in enumerate(A):P.pre[i+1]=op(P.pre[i],a)\n    def __getitem__(srs,\
    \ key): return srs.range_sum(key.start, key.stop) if isinstance(key, slice) else\
    \ srs.sum(key)\n    def sum(srs, r: int): return srs.pre[r]\n    def range_sum(srs,\
    \ l: int, r: int): return srs.diff(srs.pre[r], srs.pre[l])\nfrom abc import abstractmethod\n\
    \nclass BitArray:\n    def __init__(B, N):\n        if isinstance(N, list):\n\
    \            # If N is a list, assume it's a list of 1s and 0s\n            B.N\
    \ = len(N)\n            B.Z = (B.N+31)>>5\n            B.bits, B.cnt = u32f(B.Z+1),\
    \ u32f(B.Z+1)\n            # Set bits based on list values\n            for i,\
    \ bit in enumerate(N):\n                if bit: B.set1(i)\n        elif isinstance(N,\
    \ (bytes, bytearray)):\n            # If N is bytes, convert each byte to 8 bits\n\
    \            B.N = len(N) * 8\n            B.Z = (B.N+31)>>5\n            B.bits,\
    \ B.cnt = u32f(B.Z+1), u32f(B.Z+1)\n            # Set bits based on byte values\
    \ (MSB first for each byte)\n            for byte_idx, byte_val in enumerate(N):\n\
    \                for bit_idx in range(8):\n                    if byte_val & (1\
    \ << (7 - bit_idx)):  # MSB first\n                        B.set1(byte_idx * 8\
    \ + bit_idx)\n        else:\n            # Original behavior: N is an integer\n\
    \            B.N = N\n            B.Z = (N+31)>>5\n            B.bits, B.cnt =\
    \ u32f(B.Z+1), u32f(B.Z+1)\n    def build(B):\n        B.bits.pop()\n        for\
    \ i,b in enumerate(B.bits): B.cnt[i+1] = B.cnt[i]+popcnt32(b)\n        B.bits.append(1)\n\
    \    def __len__(B): return B.N\n    def __getitem__(B, i: int): return B.bits[i>>5]>>(31-(i&31))&1\n\
    \    def set0(B, i: int): B.bits[i>>5]&=~(1<<31-(i&31))\n    def set1(B, i: int):\
    \ B.bits[i>>5]|=1<<31-(i&31)\n    def count0(B, r: int): return r-B.count1(r)\n\
    \    def count1(B, r: int): return B.cnt[r>>5]+popcnt32(B.bits[r>>5]>>32-(r&31))\n\
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
    \ else-1\n\nclass WMMonoid(WMStatic):\n    def __init__(wm,op,e,A:list[int],W:list[int],Amax:int=None):wm._build(op,e,A,W,[0]*len(A),[0]*len(A),max(A,default=0)if\
    \ Amax is None else Amax)\n    def _build(wm,op,e,A,W,nA,nW,Amax):wm.N,wm.H,wm.op,wm.e=len(A),Amax.bit_length(),op,e;wm._build_base(W);wm._build_levels(A,W,nA,nW)\n\
    \    @abstractmethod\n    def _build_base(wm,W):...\n    @abstractmethod\n   \
    \ def _build_level(wm,L,W):...\n    def _build_levels(wm,A,W,nA,nW):\n       \
    \ wm.up=[wm.Level(wm.N,H)for H in range(wm.H)];wm.down=wm.up[::-1]\n        for\
    \ L in wm.down:\n            x,y,i=-1,wm.N-1,wm.N\n            while i:y-=A[i:=i-1]>>L.H&1\n\
    \            for i,a in enumerate(A):\n                if a>>L.H&1:nA[y:=y+1],nW[y]=a,W[i];L.set1(i)\n\
    \                else:nA[x:=x+1],nW[x]=a,W[i]\n            A,nA,W,nW=nA,A,nW,W;wm._build_level(L,W)\n\
    \    def prod_range(wm,l:int,r:int):return wm._prod_range(l,r)if l<r else wm.e\n\
    \    def prod_at(wm,y:int,l:int,r:int):return wm._prod_rect(y,y+1,l,r)if l<r else\
    \ wm.e\n    def prod_below(wm,u:int,l:int,r:int):return wm._prod_below(u,l,r)if\
    \ l<r else wm.e\n    def prod_above(wm,d:int,l:int,r:int):return wm._prod_above(d,l,r)if\
    \ l<r else wm.e\n    def prod_between(wm,d:int,u:int,l:int,r:int):return wm._prod_rect(d,u,l,r)if\
    \ l<r and d<u else wm.e\n    def prod_corner(wm,r:int,u:int):return wm._prod_below(u,0,r)if\
    \ 0<r else wm.e\n    def prod_rect(wm,l:int,d:int,r:int,u:int):return wm._prod_rect(d,u,l,r)if\
    \ l<r and d<u else wm.e\n    @abstractmethod\n    def _prod_range(wm,l,r):...\n\
    \    def _prod_below(wm,u,l,r):\n        if u<=0:return wm.e\n        elif wm.H<u.bit_length():return\
    \ wm._prod_range(l,r)\n        prod=wm.e\n        for L in wm.down:\n        \
    \    l,r=l-(l1:=L.count1(l)),r-(r1:=L.count1(r))\n            if u>>L.H&1:prod=wm.op(prod,L.prod(l,r));l,r=L.T0+l1,L.T0+r1\n\
    \        return prod\n    def _prod_above(wm,d,l,r):\n        if d<=0: return\
    \ wm._prod_range(l, r)\n        elif d.bit_length() > wm.H: return wm.e\n    \
    \    prod, d = wm.e, d-1\n        for L in wm.down:\n            l0,r0=l-(l:=L.T0+L.count1(l)),r-(r:=L.T0+L.count1(r))\n\
    \            if d>>L.H&1==0:prod=wm.op(L.prod(l,r),prod);l,r=L.T0+l0,L.T0+r0\n\
    \        return prod\n    def _prod_rect(wm,d,u,l,r):\n        if u<=0 or wm.H<d.bit_length():return\
    \ wm.e\n        elif d<=0:return wm._prod_below(u,l,r)\n        elif wm.H<u.bit_length():return\
    \ wm._prod_above(d,l,r)\n        same,prod,d=1,wm.e,d-1\n        for L in wm.down:\n\
    \            db,ub,l,r=d>>L.H&1,u>>L.H&1,l-(l1:=L.count1(l)),r-(r1:=L.count1(r))\n\
    \            if same:\n                if db!=ub:same,dl,dr,l,r=0,l,r,L.T0+l1,L.T0+r1\n\
    \                elif db:l,r=L.T0+l1,L.T0+r1\n            else:\n            \
    \    if ub:prod=wm.op(prod,L.prod(l,r));l,r=L.T0+l1,L.T0+r1\n                dl0,dr0=dl-(dl:=L.T0+L.count1(dl)),dr-(dr:=L.T0+L.count1(dr))\n\
    \                if not db:prod=wm.op(L.prod(dl,dr),prod);dl,dr=L.T0+dl0,L.T0+dr0\n\
    \        return prod\n\nclass WMGroup(WMMonoid):\n    class Level(WMStatic.Level):\n\
    \        def build(L, op, e, diff, W):super().build();L.W=Presum(W,op,e,diff)\n\
    \        def prod(L,l:int,r:int):return L.W.range_sum(l,r)\n    def __init__(wm,op,e,diff,A,W,Amax=None):wm._build(op,e,diff,A,W,[0]*len(A),[0]*len(A),max(A,default=0)if\
    \ Amax is None else Amax)\n    def _build(wm,op,e,diff,A,W,nA,nW,Amax):wm.diff=diff;super()._build(op,\
    \ e, A, W, nA, nW, Amax)\n    def _build_base(wm,W):wm.W=Presum(W,wm.op,wm.e,wm.diff)\n\
    \    def _build_level(wm,L,W):L.build(wm.op,wm.e,wm.diff,W)\n    def _prod_range(wm,l,r):return\
    \ wm.W.range_sum(l,r)\n\n\ndef bisect_left(A, x, l, r):\n    while l<r:\n    \
    \    if A[m:=(l+r)>>1]<x:l=m+1\n        else:r=m\n    return l\n\nclass WMCompressed(WMStatic):\n\
    \    def __init__(wm,A):A,wm.Y=rank(A);super().__init__(A,len(wm.Y)-1)\n    def\
    \ _didx(wm,y:int):return bisect_left(wm.Y,y,0,len(wm.Y))\n    def _yidx(wm,y:int):return\
    \ i if(i:=wm._didx(y))<len(wm.Y)and wm.Y[i]==y else-1\n    def __contains__(wm,y:int):return(i:=wm._didx(y))<len(wm.Y)and\
    \ wm.Y[i]==y\n    def kth(wm,k,l,r):return wm.Y[super().kth(k,l,r)]\n    def select(wm,y,k,l=0,r=-1):return\
    \ super().select(y,k,l,r)if~(y:=wm._yidx(y))else-1\n    def rank_range(wm,y,l,r):return\
    \ super().rank_range(y,l,r)if~(y:=wm._yidx(y))else 0\n    def count_at(wm,y,l,r):return\
    \ super().count_at(y,l,r)if~(y:=wm._yidx(y))else 0\n    def count_below(wm,u,l,r):return\
    \ super().count_below(wm._didx(u),l,r)\n    def count_between(wm,d,u,l,r):return\
    \ super().count_between(wm._didx(d),wm._didx(u),l,r)\n    def prev_val(wm,u,l,r):return\
    \ super().prev_val(wm._didx(u),l,r)\n    def next_val(wm,d,l,r):return super().next_val(wm._didx(d),l,r)\n\
    \nclass WMMonoidCompressed(WMMonoid, WMCompressed):\n    def __init__(wm,op,e,A:list[int],W:list[int]):A,wm.Y=rank(A);WMMonoid.__init__(wm,op,e,A,W,len(wm.Y)-1)\n\
    \    def prod_at(wm,y,l,r):return super().prod_at(y,l,r)if~(y:=wm._yidx(y))else\
    \ 0\n    def prod_below(wm,u,l,r):return super().prod_below(wm._didx(u),l,r)\n\
    \    def prod_between(wm,d,u,l,r):return super().prod_between(wm._didx(d),wm._didx(u),l,r)\n\
    \    def prod_corner(wm,r,u):return super().prod_corner(r,wm._didx(u))\n    def\
    \ prod_rect(wm,l,d,r,u):return super().prod_rect(l,wm._didx(d),r,wm._didx(u))\n\
    \nclass WMGroupCompressed(WMGroup,WMMonoidCompressed):\n    def __init__(wm,op,e,diff,A:list[int],W:list):A,wm.Y=rank(A);WMGroup.__init__(wm,op,e,diff,A,W,len(wm.Y)-1)\n\
    \nclass WMPoints(WMCompressed):\n    def __init__(wm,X,Y):\n        wm.I,wm.X=rank(X,distinct=True);A,wm.Y=rank(Y);nA=[0]*len(Y)\n\
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
    \nclass WMMonoidPoints(WMMonoidCompressed,WMPoints):\n    def __init__(wm,op,e,X:list[int],Y:list[int],W:list[int]):\n\
    \        wm.I,wm.X=rank(X,distinct=True);A,wm.Y=rank(Y);nA,nW=[0]*(N:=len(A)),[0]*N\n\
    \        for i,j in enumerate(wm.I):nA[j],nW[j]=A[i],W[i]\n        wm._build(op,e,nA,nW,A,W,len(wm.Y)-1)\n\
    \    def prod_range(wm,l,r):return super().prod_range(wm._lidx(l),wm._lidx(r))\n\
    \    def prod_at(wm,y,l,r):return super().prod_at(y,wm._lidx(l),wm._lidx(r))\n\
    \    def prod_below(wm,u,l,r):return super().prod_below(u,wm._lidx(l),wm._lidx(r))\n\
    \    def prod_between(wm,d,u,l,r):return super().prod_between(d,u,wm._lidx(l),wm._lidx(r))\n\
    \    def prod_corner(wm,r,u):return super().prod_corner(wm._lidx(r),u)\n    def\
    \ prod_rect(wm,l,d,r,u):return super().prod_rect(wm._lidx(l),d,wm._lidx(r),u)\n\
    \nclass WMGroupPoints(WMGroupCompressed,WMMonoidPoints):\n    def __init__(wm,op,e,diff,X:list[int],Y:list[int],W:list):\n\
    \        wm.I,wm.X=rank(X,distinct=True);A,wm.Y=rank(Y);nA,nW=[0]*(N:=len(A)),[0]*N\n\
    \        for i,j in enumerate(wm.I):nA[j],nW[j]=A[i],W[i]\n        wm._build(op,e,diff,nA,nW,A,W,len(wm.Y)-1)\n\
    import sys,os\nfrom __pypy__ import builders # type: ignore\nsb = builders.StringBuilder()\n\
    append = sb.append\ndef input(): return sys.stdin.buffer.readline().strip()\n\n\
    if __name__ == \"__main__\":\n    main()\n    \n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_sum\n\
    \nfrom operator import add, sub\n\ndef main():\n    N, Q = map(int, input().split())\n\
    \    X, Y, W = [0]*N, [0]*N, [0]*N\n    for i in range(N): X[i], Y[i], W[i] =\
    \ map(int, input().split())\n    wm = WMGroupPoints(add, 0, sub, X, Y, W)\n  \
    \  for i in range(Q): append(str(wm.prod_rect(*map(int, input().split())))); append('\\\
    n')\n    os.write(1, sb.build().encode())\n\nfrom cp_library.ds.wavelet.wm_group_points_cls\
    \ import WMGroupPoints\nimport sys,os\nfrom __pypy__ import builders # type: ignore\n\
    sb = builders.StringBuilder()\nappend = sb.append\ndef input(): return sys.stdin.buffer.readline().strip()\n\
    \nif __name__ == \"__main__\":\n    main()\n    "
  dependsOn:
  - cp_library/ds/wavelet/wm_group_points_cls.py
  - cp_library/alg/iter/rank/rank_fn.py
  - cp_library/ds/wavelet/wm_group_compressed_cls.py
  - cp_library/ds/wavelet/wm_monoid_points_cls.py
  - cp_library/ds/wavelet/wm_group_cls.py
  - cp_library/ds/wavelet/wm_monoid_compressed_cls.py
  - cp_library/ds/wavelet/wm_points_cls.py
  - cp_library/ds/list/presum_cls.py
  - cp_library/ds/wavelet/wm_monoid_cls.py
  - cp_library/ds/wavelet/wm_compressed_cls.py
  - cp_library/alg/divcon/bisect_left_fn.py
  - cp_library/ds/wavelet/wm_static_cls.py
  - cp_library/alg/iter/rank/irank_fn.py
  - cp_library/ds/wavelet/bit_array_cls.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/bit/popcnt32_fn.py
  - cp_library/ds/array/u32f_fn.py
  isVerificationFile: true
  path: test/library-checker/data-structure/rectangle_sum_wm_group_points.test.py
  requiredBy: []
  timestamp: '2025-07-11 23:11:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/rectangle_sum_wm_group_points.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/rectangle_sum_wm_group_points.test.py
- /verify/test/library-checker/data-structure/rectangle_sum_wm_group_points.test.py.html
title: test/library-checker/data-structure/rectangle_sum_wm_group_points.test.py
---
