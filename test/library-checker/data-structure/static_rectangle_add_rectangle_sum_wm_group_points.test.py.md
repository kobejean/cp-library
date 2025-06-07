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
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_fn.py
    title: cp_library/io/read_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum
    links:
    - https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum\n\
    \ndef main():\n    mod, s, m = 998244353, 31, (1 << 31)-1\n    N, Q = read(tuple[int,\
    \ ...])\n    N4 = N<<2\n    X, Y, W = [0]*N4,[0]*N4,[(0,0)]*N4\n    mod2 = mod<<s|mod\n\
    \    def polynomial(x, y, w):\n        # coefficients\n        return (-x*w%mod)<<s|(-y*w%mod),((w%mod)<<s)|(x*y%mod*w%mod)\n\
    \    for i in range(N):\n        l, d, r, u, w = read()\n        X[i:=i<<2], Y[i],\
    \ W[i] = l, d, polynomial(l, d, w)\n        X[i:=i +1], Y[i], W[i] = l, u, polynomial(l,\
    \ u, -w)\n        X[i:=i +1], Y[i], W[i] = r, d, polynomial(r, d, -w)\n      \
    \  X[i:=i +1], Y[i], W[i] = r, u, polynomial(r, u, w)\n    \n    def op(a, b):\n\
    \        av, aw = a; bv, bw = b; v, w = av+bv,aw+bw\n        return ((v>>s)%mod)<<s|((v&m)%mod),((w>>s)%mod)<<s|((w&m)%mod)\n\
    \    def diff(a, b):\n        av, aw = a; bv, bw = b; v, w = av+mod2-bv,aw+mod2-bw\n\
    \        return ((v>>s)%mod)<<s|((v&m)%mod),((w>>s)%mod)<<s|((w&m)%mod)\n    e\
    \ = 0,0\n    wm = WMGroupPoints(op, e, diff, X, Y, W)\n    \n    def poly_eval(x,y,poly):\n\
    \        v, w = poly; v1, v2 = v>>s, v&m; w1, w2 = w>>s, w&m\n        return (w2+y*v1+x*v2+x*y%mod*w1)%mod\n\
    \    for _ in range(Q):\n        l, d, r, u = read()\n        ld = poly_eval(l,d,wm.prod_corner(l,d))\n\
    \        lu = poly_eval(l,u,wm.prod_corner(l,u))\n        rd = poly_eval(r,d,wm.prod_corner(r,d))\n\
    \        ru = poly_eval(r,u,wm.prod_corner(r,u))\n        ans = (ru+ld-lu-rd)%mod\n\
    \        write(ans)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n             https://kobejean.github.io/cp-library       \
    \        \n'''\n\n\n\n\ndef coord_compress(A: list[int], distinct = False):\n\
    \    s, m = pack_sm((N := len(A))-1); R, V = [0]*N, [a<<s|i for i,a in enumerate(A)];\
    \ V.sort()\n    if distinct:\n        for r, ai in enumerate(V): a, i = pack_dec(ai,\
    \ s, m); R[i], V[r] = r, a\n    else:\n        r = p = -1\n        for ai in V:\n\
    \            a, i = pack_dec(ai, s, m)\n            if a != p: r = r+1; V[r] =\
    \ p = a\n            R[i] = r\n        del V[r+1:]\n    return R, V\n\n\n\ndef\
    \ pack_dec(ab: int, s: int, m: int): return ab>>s,ab&m\ndef pack_sm(N: int): s=N.bit_length();\
    \ return s,(1<<s)-1\n\n\n\nclass Presum:\n    def __init__(P, op, e, diff, A:\
    \ list):\n        P.N = len(A); P.op, P.e, P.diff, P.pre = op, e, diff, [e]*(P.N+1)\n\
    \        for i,a in enumerate(A):P.pre[i+1]=op(P.pre[i],a)\n    def __getitem__(P,i):return\
    \ P.pre[i]\n    def prod(P,l:int,r:int):return P.diff(P.pre[r],P.pre[l])\nfrom\
    \ abc import abstractmethod\n\nclass BitArray:\n    def __init__(B, N: int):\n\
    \        B.N, B.Z = N, (N+31)>>5\n        B.bits, B.cnt = u32f(B.Z+1), u32f(B.Z+1)\n\
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
    \        def build(L, op, e, diff, W):super().build();L.W=Presum(op,e,diff,W)\n\
    \        def prod(L,l:int,r:int):return L.W.prod(l,r)\n    def __init__(wm,op,e,diff,A,W,Amax=None):wm._build(op,e,diff,A,W,[0]*len(A),[0]*len(A),max(A,default=0)if\
    \ Amax is None else Amax)\n    def _build(wm,op,e,diff,A,W,nA,nW,Amax):wm.diff=diff;super()._build(op,\
    \ e, A, W, nA, nW, Amax)\n    def _build_base(wm,W):wm.W=Presum(wm.op,wm.e,wm.diff,W)\n\
    \    def _build_level(wm,L,W):L.build(wm.op,wm.e,wm.diff,W)\n    def _prod_range(wm,l:int,r:int):return\
    \ wm.W.prod(l,r)\n\n\ndef bisect_left(A, x, l, r):\n    while l<r:\n        if\
    \ A[m:=(l+r)>>1]<x:l=m+1\n        else:r=m\n    return l\n\nclass WMCompressed(WMStatic):\n\
    \    def __init__(wm,A):A,wm.Y=coord_compress(A);super().__init__(A,len(wm.Y)-1)\n\
    \    def _didx(wm,y:int):return bisect_left(wm.Y,y,0,len(wm.Y))\n    def _yidx(wm,y:int):return\
    \ i if(i:=wm._didx(y))<len(wm.Y)and wm.Y[i]==y else-1\n    def __contains__(wm,y:int):return(i:=wm._didx(y))<len(wm.Y)and\
    \ wm.Y[i]==y\n    def kth(wm,k,l,r):return wm.Y[super().kth(k,l,r)]\n    def select(wm,y,k,l=0,r=-1):return\
    \ super().select(y,k,l,r)if~(y:=wm._yidx(y))else-1\n    def rank_range(wm,y,l,r):return\
    \ super().rank_range(y,l,r)if~(y:=wm._yidx(y))else 0\n    def count_at(wm,y,l,r):return\
    \ super().count_at(y,l,r)if~(y:=wm._yidx(y))else 0\n    def count_below(wm,u,l,r):return\
    \ super().count_below(wm._didx(u),l,r)\n    def count_between(wm,d,u,l,r):return\
    \ super().count_between(wm._didx(d),wm._didx(u),l,r)\n    def prev_val(wm,u,l,r):return\
    \ super().prev_val(wm._didx(u),l,r)\n    def next_val(wm,d,l,r):return super().next_val(wm._didx(d),l,r)\n\
    \nclass WMMonoidCompressed(WMMonoid, WMCompressed):\n    def __init__(wm,op,e,A:list[int],W:list[int]):A,wm.Y=coord_compress(A);WMMonoid.__init__(wm,op,e,A,W,len(wm.Y)-1)\n\
    \    def prod_at(wm,y,l,r):return super().prod_at(y,l,r)if~(y:=wm._yidx(y))else\
    \ 0\n    def prod_below(wm,u,l,r):return super().prod_below(wm._didx(u),l,r)\n\
    \    def prod_between(wm,d,u,l,r):return super().prod_between(wm._didx(d),wm._didx(u),l,r)\n\
    \    def prod_corner(wm,r,u):return super().prod_corner(r,wm._didx(u))\n    def\
    \ prod_rect(wm,l,d,r,u):return super().prod_rect(l,wm._didx(d),r,wm._didx(u))\n\
    \nclass WMGroupCompressed(WMGroup,WMMonoidCompressed):\n    def __init__(wm,op,e,diff,A:list[int],W:list):A,wm.Y=coord_compress(A);WMGroup.__init__(wm,op,e,diff,A,W,len(wm.Y)-1)\n\
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
    \nclass WMMonoidPoints(WMMonoidCompressed,WMPoints):\n    def __init__(wm,op,e,X:list[int],Y:list[int],W:list[int]):\n\
    \        wm.I,wm.X=coord_compress(X,distinct=True);A,wm.Y=coord_compress(Y);nA,nW=[0]*(N:=len(A)),[0]*N\n\
    \        for i,j in enumerate(wm.I):nA[j],nW[j]=A[i],W[i]\n        wm._build(op,e,nA,nW,A,W,len(wm.Y)-1)\n\
    \    def prod_range(wm,l,r):return super().prod_range(wm._lidx(l),wm._lidx(r))\n\
    \    def prod_at(wm,y,l,r):return super().prod_at(y,wm._lidx(l),wm._lidx(r))\n\
    \    def prod_below(wm,u,l,r):return super().prod_below(u,wm._lidx(l),wm._lidx(r))\n\
    \    def prod_between(wm,d,u,l,r):return super().prod_between(d,u,wm._lidx(l),wm._lidx(r))\n\
    \    def prod_corner(wm,r,u):return super().prod_corner(wm._lidx(r),u)\n    def\
    \ prod_rect(wm,l,d,r,u):return super().prod_rect(wm._lidx(l),d,wm._lidx(r),u)\n\
    \nclass WMGroupPoints(WMGroupCompressed,WMMonoidPoints):\n    def __init__(wm,op,e,diff,X:list[int],Y:list[int],W:list):\n\
    \        wm.I,wm.X=coord_compress(X,distinct=True);A,wm.Y=coord_compress(Y);nA,nW=[0]*(N:=len(A)),[0]*N\n\
    \        for i,j in enumerate(wm.I):nA[j],nW[j]=A[i],W[i]\n        wm._build(op,e,diff,nA,nW,A,W,len(wm.Y)-1)\n\
    \nimport os\nimport sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n\
    \    BUFSIZE = 8192\n    newlines = 0\n\n    def __init__(self, file):\n     \
    \   self._fd = file.fileno()\n        self.buffer = BytesIO()\n        self.writable\
    \ = \"x\" in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
    \ if self.writable else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n\
    \        while True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n            if not b:\n                break\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines = 0\n        return self.buffer.read()\n\n    def readline(self):\n\
    \        BUFSIZE = self.BUFSIZE\n        while self.newlines == 0:\n         \
    \   b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n        \
    \    self.newlines = b.count(b\"\\n\") + (not b)\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines -= 1\n        return self.buffer.readline()\n\n    def\
    \ flush(self):\n        if self.writable:\n            os.write(self._fd, self.buffer.getvalue())\n\
    \            self.buffer.truncate(0), self.buffer.seek(0)\n\n\nclass IOWrapper(IOBase):\n\
    \    stdin: 'IOWrapper' = None\n    stdout: 'IOWrapper' = None\n    \n    def\
    \ __init__(self, file):\n        self.buffer = FastIO(file)\n        self.flush\
    \ = self.buffer.flush\n        self.writable = self.buffer.writable\n\n    def\
    \ write(self, s):\n        return self.buffer.write(s.encode(\"ascii\"))\n   \
    \ \n    def read(self):\n        return self.buffer.read().decode(\"ascii\")\n\
    \    \n    def readline(self):\n        return self.buffer.readline().decode(\"\
    ascii\")\ntry:\n    sys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\n    sys.stdout\
    \ = IOWrapper.stdout = IOWrapper(sys.stdout)\nexcept:\n    pass\n\ndef write(*args,\
    \ **kwargs):\n    '''Prints the values to a stream, or to stdout_fast by default.'''\n\
    \    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n\
    \    at_start = True\n    for x in args:\n        if not at_start:\n         \
    \   file.write(sep)\n        file.write(str(x))\n        at_start = False\n  \
    \  file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\nfrom typing import Iterable, Type, Union, overload\n\
    import typing\nfrom collections import deque\nfrom numbers import Number\nfrom\
    \ types import GenericAlias \nfrom typing import Callable, Collection, Iterator,\
    \ Union\nfrom typing import TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\n\n\
    class TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\n    def __init__(self):\n\
    \        self.queue = deque()\n\n    def __next__(self):\n        if not self.queue:\
    \ self.queue.extend(self._line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self._line())\n\
    \        while self.queue: yield\n \n    def _line(self):\n        return TokenStream.stream.readline().split()\n\
    \n    def line(self):\n        if self.queue:\n            A = list(self.queue)\n\
    \            self.queue.clear()\n            return A\n        return self._line()\n\
    TokenStream.default = TokenStream()\n\nclass CharStream(TokenStream):\n    def\
    \ _line(self):\n        return TokenStream.stream.readline().rstrip()\nCharStream.default\
    \ = CharStream()\n\n\nParseFn = Callable[[TokenStream],_T]\nclass Parser:\n  \
    \  def __init__(self, spec: Union[type[_T],_T]):\n        self.parse = Parser.compile(spec)\n\
    \n    def __call__(self, ts: TokenStream) -> _T:\n        return self.parse(ts)\n\
    \    \n    @staticmethod\n    def compile_type(cls: type[_T], args = ()) -> _T:\n\
    \        if issubclass(cls, Parsable):\n            return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(ts: TokenStream):\
    \ return cls(next(ts))              \n            return parse\n        elif issubclass(cls,\
    \ tuple):\n            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection):\n            return Parser.compile_collection(cls, args)\n    \
    \    elif callable(cls):\n            def parse(ts: TokenStream):\n          \
    \      return cls(next(ts))              \n            return parse\n        else:\n\
    \            raise NotImplementedError()\n    \n    @staticmethod\n    def compile(spec:\
    \ Union[type[_T],_T]=int) -> ParseFn[_T]:\n        if isinstance(spec, (type,\
    \ GenericAlias)):\n            cls = typing.get_origin(spec) or spec\n       \
    \     args = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream): return cls(next(ts)) +\
    \ offset\n            return parse\n        elif isinstance(args := spec, tuple):\
    \      \n            return Parser.compile_tuple(type(spec), args)\n        elif\
    \ isinstance(args := spec, Collection):\n            return Parser.compile_collection(type(spec),\
    \ args)\n        elif isinstance(fn := spec, Callable): \n            def parse(ts:\
    \ TokenStream): return fn(next(ts))\n            return parse\n        else:\n\
    \            raise NotImplementedError()\n\n    @staticmethod\n    def compile_line(cls:\
    \ _T, spec=int) -> ParseFn[_T]:\n        if spec is int:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream): return cls([int(token) for token in ts.line()])\n\
    \            return parse\n        else:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream): return cls([fn(ts) for _ in ts.wait()])\n\
    \            return parse\n\n    @staticmethod\n    def compile_repeat(cls: _T,\
    \ spec, N) -> ParseFn[_T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream): return cls([fn(ts) for _ in range(N)])\n        return parse\n\
    \n    @staticmethod\n    def compile_children(cls: _T, specs) -> ParseFn[_T]:\n\
    \        fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(ts:\
    \ TokenStream): return cls([fn(ts) for fn in fns])  \n        return parse\n \
    \           \n    @staticmethod\n    def compile_tuple(cls: type[_T], specs) ->\
    \ ParseFn[_T]:\n        if isinstance(specs, (tuple,list)) and len(specs) == 2\
    \ and specs[1] is ...:\n            return Parser.compile_line(cls, specs[0])\n\
    \        else:\n            return Parser.compile_children(cls, specs)\n\n   \
    \ @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and\
    \ isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls, specs[0],\
    \ specs[1])\n        else:\n            raise NotImplementedError()\n\nclass Parsable:\n\
    \    @classmethod\n    def compile(cls):\n        def parser(ts: TokenStream):\
    \ return cls(next(ts))\n        return parser\n\n@overload\ndef read() -> list[int]:\
    \ ...\n@overload\ndef read(spec: Type[_T], char=False) -> _T: ...\n@overload\n\
    def read(spec: _U, char=False) -> _U: ...\n@overload\ndef read(*specs: Type[_T],\
    \ char=False) -> tuple[_T, ...]: ...\n@overload\ndef read(*specs: _U, char=False)\
    \ -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_U], char=False):\n\
    \    if not char and not specs: return [int(s) for s in TokenStream.default.line()]\n\
    \    parser: _T = Parser.compile(specs)\n    ret = parser(CharStream.default if\
    \ char else TokenStream.default)\n    return ret[0] if len(specs) == 1 else ret\n\
    \nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum\n\
    \ndef main():\n    mod, s, m = 998244353, 31, (1 << 31)-1\n    N, Q = read(tuple[int,\
    \ ...])\n    N4 = N<<2\n    X, Y, W = [0]*N4,[0]*N4,[(0,0)]*N4\n    mod2 = mod<<s|mod\n\
    \    def polynomial(x, y, w):\n        # coefficients\n        return (-x*w%mod)<<s|(-y*w%mod),((w%mod)<<s)|(x*y%mod*w%mod)\n\
    \    for i in range(N):\n        l, d, r, u, w = read()\n        X[i:=i<<2], Y[i],\
    \ W[i] = l, d, polynomial(l, d, w)\n        X[i:=i +1], Y[i], W[i] = l, u, polynomial(l,\
    \ u, -w)\n        X[i:=i +1], Y[i], W[i] = r, d, polynomial(r, d, -w)\n      \
    \  X[i:=i +1], Y[i], W[i] = r, u, polynomial(r, u, w)\n    \n    def op(a, b):\n\
    \        av, aw = a; bv, bw = b; v, w = av+bv,aw+bw\n        return ((v>>s)%mod)<<s|((v&m)%mod),((w>>s)%mod)<<s|((w&m)%mod)\n\
    \    def diff(a, b):\n        av, aw = a; bv, bw = b; v, w = av+mod2-bv,aw+mod2-bw\n\
    \        return ((v>>s)%mod)<<s|((v&m)%mod),((w>>s)%mod)<<s|((w&m)%mod)\n    e\
    \ = 0,0\n    wm = WMGroupPoints(op, e, diff, X, Y, W)\n    \n    def poly_eval(x,y,poly):\n\
    \        v, w = poly; v1, v2 = v>>s, v&m; w1, w2 = w>>s, w&m\n        return (w2+y*v1+x*v2+x*y%mod*w1)%mod\n\
    \    for _ in range(Q):\n        l, d, r, u = read()\n        ld = poly_eval(l,d,wm.prod_corner(l,d))\n\
    \        lu = poly_eval(l,u,wm.prod_corner(l,u))\n        rd = poly_eval(r,d,wm.prod_corner(r,d))\n\
    \        ru = poly_eval(r,u,wm.prod_corner(r,u))\n        ans = (ru+ld-lu-rd)%mod\n\
    \        write(ans)\n\nfrom cp_library.ds.wavelet.wm_group_points_cls import WMGroupPoints\n\
    from cp_library.io.write_fn import write\nfrom cp_library.io.read_fn import read\n\
    \nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/ds/wavelet/wm_group_points_cls.py
  - cp_library/io/write_fn.py
  - cp_library/io/read_fn.py
  - cp_library/alg/iter/cmpr/coord_compress_fn.py
  - cp_library/ds/wavelet/wm_group_compressed_cls.py
  - cp_library/ds/wavelet/wm_monoid_points_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/ds/wavelet/wm_group_cls.py
  - cp_library/ds/wavelet/wm_monoid_compressed_cls.py
  - cp_library/ds/wavelet/wm_points_cls.py
  - cp_library/ds/list/presum_cls.py
  - cp_library/ds/wavelet/wm_monoid_cls.py
  - cp_library/ds/wavelet/wm_compressed_cls.py
  - cp_library/alg/divcon/bisect_left_fn.py
  - cp_library/ds/wavelet/wm_static_cls.py
  - cp_library/bit/pack/pack_dec_fn.py
  - cp_library/bit/pack/pack_sm_fn.py
  - cp_library/ds/wavelet/bit_array_cls.py
  - cp_library/bit/popcnt32_fn.py
  - cp_library/ds/array/u32f_fn.py
  isVerificationFile: true
  path: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_wm_group_points.test.py
  requiredBy: []
  timestamp: '2025-06-08 03:08:21+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_wm_group_points.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/static_rectangle_add_rectangle_sum_wm_group_points.test.py
- /verify/test/library-checker/data-structure/static_rectangle_add_rectangle_sum_wm_group_points.test.py.html
title: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_wm_group_points.test.py
---
