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
    path: cp_library/ds/tree/bit/bit_cls.py
    title: cp_library/ds/tree/bit/bit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/bit_array_cls.py
    title: cp_library/ds/wavelet/bit_array_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_bit_cls.py
    title: cp_library/ds/wavelet/wm_bit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_bit_compressed_cls.py
    title: cp_library/ds/wavelet/wm_bit_compressed_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_compressed_cls.py
    title: cp_library/ds/wavelet/wm_compressed_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_points_cls.py
    title: cp_library/ds/wavelet/wm_points_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_static_cls.py
    title: cp_library/ds/wavelet/wm_static_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_weighted_cls.py
    title: cp_library/ds/wavelet/wm_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_weighted_compressed_cls.py
    title: cp_library/ds/wavelet/wm_weighted_compressed_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_weighted_points_cls.py
    title: cp_library/ds/wavelet/wm_weighted_points_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/point_add_rectangle_sum_wm_bit_points.test.py
    title: test/library-checker/data-structure/point_add_rectangle_sum_wm_bit_points.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/rectangle_sum_wm_bit_points.test.py
    title: test/library-checker/data-structure/rectangle_sum_wm_bit_points.test.py
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
    \n\n\n\ndef irank(A: list[int], distinct = False):\n    P = Packer(len(A)-1);\
    \ V = P.enumerate(A); V.sort()\n    if distinct:\n        for r, ai in enumerate(V):\
    \ a, i = P.dec(ai); A[i], V[r] = r, a\n    elif V:\n        r, p = -1, V[-1]+1\
    \ # set p to unique value to trigger `if a != p` on first elm\n        for ai\
    \ in V:\n            a, i = P.dec(ai)\n            if a!=p: V[r:=r+1] = p = a\n\
    \            A[i] = r\n        del V[r+1:]\n    return V\n\n\n\nclass Packer:\n\
    \    def __init__(P, mx: int):\n        P.s = mx.bit_length()\n        P.m = (1\
    \ << P.s) - 1\n    def enc(P, a: int, b: int): return a << P.s | b\n    def dec(P,\
    \ x: int) -> tuple[int, int]: return x >> P.s, x & P.m\n    def enumerate(P, A,\
    \ reverse=False): P.ienumerate(A:=A.copy(), reverse); return A\n    def ienumerate(P,\
    \ A, reverse=False):\n        if reverse:\n            for i,a in enumerate(A):\
    \ A[i] = P.enc(-a, i)\n        else:\n            for i,a in enumerate(A): A[i]\
    \ = P.enc(a, i)\n    def indices(P, A: list[int]): P.iindices(A:=A.copy()); return\
    \ A\n    def iindices(P, A):\n        for i,a in enumerate(A): A[i] = P.m&a\n\n\
    def rank(A: list[int], distinct = False): return (R := A.copy()), irank(R, distinct)\n\
    \n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2513            \n            \u2503                           \
    \         7 \u2503            \n            \u2517\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B            \n            \u250F\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2513                 \u2502              \n  \
    \          \u2503                3 \u2503\u25C4\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524           \
    \   \n            \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B                 \u2502\
    \              \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2513       \u2502  \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513\
    \       \u2502              \n            \u2503      1 \u2503\u25C4\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2524  \u2503      5 \u2503\u25C4\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2524              \n            \u2517\u2501\u2501\u2501\u2501\u2501\
    \u2501\u252F\u2501\u251B       \u2502  \u2517\u2501\u2501\u2501\u2501\u2501\u2501\
    \u252F\u2501\u251B       \u2502              \n            \u250F\u2501\u2501\u2501\
    \u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\
    \u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502              \n       \
    \     \u2503 0 \u2503\u25C4\u2500\u2524  \u2503 2 \u2503\u25C4\u2500\u2524  \u2503\
    \ 4 \u2503\u25C4\u2500\u2524  \u2503 6 \u2503\u25C4\u2500\u2524              \n\
    \            \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B\
    \  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B\
    \  \u2502              \n              \u2502    \u2502    \u2502    \u2502  \
    \  \u2502    \u2502    \u2502    \u2502              \n              \u25BC  \
    \  \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC        \
    \      \n            \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\
    \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\
    \u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\
    \u2501\u2501\u2501\u2513            \n            \u2503 0 \u2503\u2503 1 \u2503\
    \u2503 2 \u2503\u2503 3 \u2503\u2503 4 \u2503\u2503 5 \u2503\u2503 6 \u2503\u2503\
    \ 7 \u2503            \n            \u2517\u2501\u2501\u2501\u251B\u2517\u2501\
    \u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\
    \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\
    \u2501\u251B\u2517\u2501\u2501\u2501\u251B            \n\u257A\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n           Data Structure -\
    \ Tree - Binary Index Tree            \n'''\n\nclass BIT:\n    def __init__(bit,\
    \ v):\n        if isinstance(v, int): bit._d, bit._n = [0]*v, v\n        else:\
    \ bit.build(v)\n        bit._lb = 1<<bit._n.bit_length()\n\n    def build(bit,\
    \ data):\n        bit._d, bit._n = data, len(data)\n        for i in range(bit._n):\n\
    \            if (r := i|i+1) < bit._n: bit._d[r] += bit._d[i]\n\n    def add(bit,\
    \ i, x):\n        while i < bit._n: bit._d[i] += x; i |= i+1\n\n    def sum(bit,\
    \ n: int) -> int:\n        s = 0\n        while n: s, n = s+bit._d[n-1], n&n-1\n\
    \        return s\n\n    def sum_range(bit, l, r):\n        s = 0\n        while\
    \ r: s, r = s+bit._d[r-1], r&r-1\n        while l: s, l = s-bit._d[l-1], l&l-1\n\
    \        return s\n\n    def __len__(bit) -> int:\n        return bit._n\n   \
    \ \n    def __getitem__(bit, i: int) -> int:\n        s, l = bit._d[i], i&(i+1)\n\
    \        while l != i: s, i = s-bit._d[i-1], i-(i&-i)\n        return s\n    get\
    \ = __getitem__\n    \n    def __setitem__(bit, i: int, x: int) -> None:\n   \
    \     bit.add(i, x-bit[i])\n    set = __setitem__\n\n    def prelist(bit) -> list[int]:\n\
    \        pre = [0]+bit._d\n        for i in range(bit._n+1): pre[i] += pre[i&i-1]\n\
    \        return pre\n\n    def bisect_left(bit, v) -> int:\n        return bit.bisect_right(v-1)\
    \ if v>0 else -1\n    \n    def bisect_right(bit, v, key=None) -> int:\n     \
    \   i = s = 0; m = bit._lb\n        if key:\n            while m := m>>1:\n  \
    \              if (ni := m|i) <= bit._n and key(ns:=s+bit._d[ni-1]) <= v: s, i\
    \ = ns, ni\n        else:\n            while m := m>>1:\n                if (ni\
    \ := m|i) <= bit._n and (ns:=s+bit._d[ni-1]) <= v: s, i = ns, ni\n        return\
    \ i\n\nclass BitArray:\n    def __init__(B, N):\n        if isinstance(N, list):\n\
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
    \ else-1\n\nclass WMWeighted(WMStatic):\n    class Level(WMStatic.Level):\n  \
    \      def __init__(L,N:int,H:int):super().__init__(N,H);L.W=[0]*(N+1)\n     \
    \   def build(L,W:list[int]):\n            super().build()\n            for i,w\
    \ in enumerate(W):L.W[i+1]=L.W[i]+w\n        def sum(L,l:int,r:int):return L.W[r]-L.W[l]\n\
    \    def __init__(wm, A:list[int],W:list[int],Amax:int=None):wm._build(A,W,[0]*len(A),[0]*len(A),max(A,default=0)if\
    \ Amax is None else Amax)\n    def _build(wm,A,W,nA,nW,Amax):wm.N,wm.H=len(A),Amax.bit_length();wm._build_base(W);wm._build_levels(A,W,nA,nW)\n\
    \    def _build_base(wm, W):\n        wm.W = [0]*(wm.N+1)\n        for i,w in\
    \ enumerate(W): wm.W[i+1] = wm.W[i]+w\n    def _build_levels(wm, A, W, nA, nW):\n\
    \        wm.up = [wm.Level(wm.N, H) for H in range(wm.H)]; wm.down = wm.up[::-1]\n\
    \        for L in wm.down:\n            x,y,i=-1,wm.N-1,wm.N\n            while\
    \ i:y-=A[i:=i-1]>>L.H&1\n            for i,a in enumerate(A):\n              \
    \  if a>>L.H&1:nA[y:=y+1],nW[y]=a,W[i];L.set1(i)\n                else:nA[x:=x+1],nW[x]=a,W[i]\n\
    \            A,nA,W,nW=nA,A,nW,W;L.build(W)\n    def sum_range(wm,l:int,r:int):return\
    \ wm._sum_range(l,r) if l<r else 0\n    def sum_at(wm,y:int,l:int,r:int):return\
    \ wm._sum_rect(y,y+1,l,r) if l<r else 0\n    def sum_below(wm,u:int,l:int,r:int):return\
    \ wm._sum_below(u,l,r) if l<r else 0\n    def sum_above(wm,d:int,l:int,r:int):return\
    \ wm._sum_above(d,l,r) if l<r else 0\n    def sum_between(wm,d:int,u:int,l:int,r:int):return\
    \ wm._sum_rect(d,u,l,r)if l<r and d<u else 0\n    def sum_corner(wm,r:int,u:int):return\
    \ wm.sum_below(u,0,r) if 0<r else 0\n    def sum_rect(wm,l:int,d:int,r:int,u:int):return\
    \ wm._sum_rect(d,u,l,r)if l<r and d<u else 0\n    def _sum_range(wm,l,r):return\
    \ wm.W[r]-wm.W[l]\n    def _sum_below(wm,u,l,r):\n        if u<=0:return 0\n \
    \       elif wm.H<u.bit_length():return wm._sum_range(l,r)\n        sum = 0\n\
    \        for L in wm.down:\n            l,r=l-(l1:=L.count1(l)),r-(r1:=L.count1(r))\n\
    \            if u>>L.H&1:sum+=L.sum(l,r);l,r=L.T0+l1,L.T0+r1\n        return sum\n\
    \    def _sum_above(wm,d,l,r):\n        if d<=0:return wm._sum_range(l,r)\n  \
    \      elif wm.H<d.bit_length():return 0\n        sum,d=0,d-1\n        for L in\
    \ wm.down:\n            l0,r0=l-(l:=L.T0+L.count1(l)),r-(r:=L.T0+L.count1(r))\n\
    \            if d>>L.H&1==0:sum+=L.sum(l,r);l,r=L.T0+l0,L.T0+r0\n        return\
    \ sum\n    def _sum_rect(wm,d,u,l,r):\n        if u<=0 or wm.H<d.bit_length():return\
    \ 0\n        elif d<=0:return wm._sum_below(u,l,r)\n        elif wm.H<u.bit_length():return\
    \ wm._sum_above(d,l,r)\n        same,sum,d=1,0,d-1\n        for L in wm.down:\n\
    \            db,ub,l,r=d>>L.H&1,u>>L.H&1,l-(l1:=L.count1(l)),r-(r1:=L.count1(r))\n\
    \            if same:\n                if db!=ub:same,dl,dr,l,r=0,l,r,L.T0+l1,L.T0+r1\n\
    \                elif db:l,r=L.T0+l1,L.T0+r1\n            else:\n            \
    \    if ub:sum+=L.sum(l,r);l,r=L.T0+l1,L.T0+r1\n                dl0,dr0=dl-(dl:=L.T0+L.count1(dl)),dr-(dr:=L.T0+L.count1(dr))\n\
    \                if not db:sum+=L.sum(dl,dr);dl,dr=L.T0+dl0,L.T0+dr0\n       \
    \ return sum\n\nclass WMBIT(WMWeighted):\n    class Level(WMStatic.Level):\n \
    \       def build(L,W:list[int]):super().build();L.W=BIT(W[:])\n        def sum(L,l:int,r:int):return\
    \ L.W.sum_range(l,r)\n    def _build_base(wm,W):wm.W=BIT(W[:])\n    def _sum_range(wm,l,r):return\
    \ wm.W.sum_range(l,r)\n    def add(wm,i:int,w:int):\n        wm.W.add(i,w)\n \
    \       for L in wm.down:L.W.add(i:=L.pos(L[i],i),w)\n\n\ndef bisect_left(A, x,\
    \ l, r):\n    while l<r:\n        if A[m:=(l+r)>>1]<x:l=m+1\n        else:r=m\n\
    \    return l\n\nclass WMCompressed(WMStatic):\n    def __init__(wm,A):A,wm.Y=rank(A);super().__init__(A,len(wm.Y)-1)\n\
    \    def _didx(wm,y:int):return bisect_left(wm.Y,y,0,len(wm.Y))\n    def _yidx(wm,y:int):return\
    \ i if(i:=wm._didx(y))<len(wm.Y)and wm.Y[i]==y else-1\n    def __contains__(wm,y:int):return(i:=wm._didx(y))<len(wm.Y)and\
    \ wm.Y[i]==y\n    def kth(wm,k,l,r):return wm.Y[super().kth(k,l,r)]\n    def select(wm,y,k,l=0,r=-1):return\
    \ super().select(y,k,l,r)if~(y:=wm._yidx(y))else-1\n    def rank_range(wm,y,l,r):return\
    \ super().rank_range(y,l,r)if~(y:=wm._yidx(y))else 0\n    def count_at(wm,y,l,r):return\
    \ super().count_at(y,l,r)if~(y:=wm._yidx(y))else 0\n    def count_below(wm,u,l,r):return\
    \ super().count_below(wm._didx(u),l,r)\n    def count_between(wm,d,u,l,r):return\
    \ super().count_between(wm._didx(d),wm._didx(u),l,r)\n    def prev_val(wm,u,l,r):return\
    \ super().prev_val(wm._didx(u),l,r)\n    def next_val(wm,d,l,r):return super().next_val(wm._didx(d),l,r)\n\
    \nclass WMWeightedCompressed(WMWeighted, WMCompressed):\n    def __init__(wm,A:list[int],W:list[int]):A,wm.Y=rank(A);super().__init__(A,W,len(wm.Y)-1)\n\
    \    def sum_at(wm,y,l,r):return super().sum_at(y,l,r)if~(y:=wm._yidx(y))else\
    \ 0\n    def sum_below(wm,u,l,r):return super().sum_below(wm._didx(u),l,r)\n \
    \   def sum_between(wm,d,u,l,r):return super().sum_between(wm._didx(d),wm._didx(u),l,r)\n\
    \    def sum_corner(wm,r,u):return super().sum_corner(r,wm._didx(u))\n    def\
    \ sum_rect(wm,l,d,r,u):return super().sum_rect(l,wm._didx(d),r,wm._didx(u))\n\n\
    class WMBITCompressed(WMBIT,WMWeightedCompressed):pass\n\nclass WMPoints(WMCompressed):\n\
    \    def __init__(wm,X,Y):\n        wm.I,wm.X=rank(X,distinct=True);A,wm.Y=rank(Y);nA=[0]*len(Y)\n\
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
    \nclass WMWeightedPoints(WMWeightedCompressed,WMPoints):\n    def __init__(wm,X:list[int],Y:list[int],W:list[int]):\n\
    \        wm.I,wm.X=rank(X,distinct=True);A,wm.Y=rank(Y);nA,nW=[0]*(N:=len(A)),[0]*N\n\
    \        for i,j in enumerate(wm.I):nA[j],nW[j]=A[i],W[i]\n        wm._build(nA,nW,A,W,len(wm.Y)-1)\n\
    \    def sum_range(wm,l,r):return super().sum_range(wm._lidx(l),wm._lidx(r))\n\
    \    def sum_at(wm,y,l,r):return super().sum_at(y,wm._lidx(l),wm._lidx(r))\n \
    \   def sum_below(wm,u,l,r):return super().sum_below(u,wm._lidx(l),wm._lidx(r))\n\
    \    def sum_between(wm,d,u,l,r):return super().sum_between(d,u,wm._lidx(l),wm._lidx(r))\n\
    \    def sum_corner(wm,r,u):return super().sum_corner(wm._lidx(r),u)\n    def\
    \ sum_rect(wm,l,d,r,u):return super().sum_rect(wm._lidx(l),d,wm._lidx(r),u)\n\n\
    class WMBITPoints(WMBITCompressed, WMWeightedPoints):\n    def __init__(wm, X:\
    \ list[int], Y: list[int], W: list[int]):\n        wm.I,wm.X=rank(X,distinct=True);A,wm.Y=rank(Y);nA,nW=[0]*(N:=len(A)),[0]*N\n\
    \        for i,j in enumerate(wm.I):nA[j],nW[j]=A[i],W[i]\n        super()._build(nA,nW,A,W,len(wm.Y)-1)\n\
    \    def add(wm,i:int,w:int):super().add(wm.I[i],w)\n"
  code: "import cp_library.__header__\nfrom cp_library.alg.iter.rank.rank_fn import\
    \ rank\nimport cp_library.ds.__header__\nimport cp_library.ds.wavelet.__header__\n\
    from cp_library.ds.wavelet.wm_bit_compressed_cls import WMBITCompressed\nfrom\
    \ cp_library.ds.wavelet.wm_weighted_points_cls import WMWeightedPoints\n\nclass\
    \ WMBITPoints(WMBITCompressed, WMWeightedPoints):\n    def __init__(wm, X: list[int],\
    \ Y: list[int], W: list[int]):\n        wm.I,wm.X=rank(X,distinct=True);A,wm.Y=rank(Y);nA,nW=[0]*(N:=len(A)),[0]*N\n\
    \        for i,j in enumerate(wm.I):nA[j],nW[j]=A[i],W[i]\n        super()._build(nA,nW,A,W,len(wm.Y)-1)\n\
    \    def add(wm,i:int,w:int):super().add(wm.I[i],w)"
  dependsOn:
  - cp_library/alg/iter/rank/rank_fn.py
  - cp_library/ds/wavelet/wm_bit_compressed_cls.py
  - cp_library/ds/wavelet/wm_weighted_points_cls.py
  - cp_library/ds/wavelet/wm_bit_cls.py
  - cp_library/ds/wavelet/wm_weighted_compressed_cls.py
  - cp_library/ds/wavelet/wm_points_cls.py
  - cp_library/ds/tree/bit/bit_cls.py
  - cp_library/ds/wavelet/wm_weighted_cls.py
  - cp_library/ds/wavelet/wm_compressed_cls.py
  - cp_library/alg/divcon/bisect_left_fn.py
  - cp_library/ds/wavelet/wm_static_cls.py
  - cp_library/alg/iter/rank/irank_fn.py
  - cp_library/ds/wavelet/bit_array_cls.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/bit/popcnt32_fn.py
  - cp_library/ds/array/u32f_fn.py
  isVerificationFile: false
  path: cp_library/ds/wavelet/wm_bit_points_cls.py
  requiredBy: []
  timestamp: '2025-07-09 08:31:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/data-structure/point_add_rectangle_sum_wm_bit_points.test.py
  - test/library-checker/data-structure/rectangle_sum_wm_bit_points.test.py
documentation_of: cp_library/ds/wavelet/wm_bit_points_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/wavelet/wm_bit_points_cls.py
- /library/cp_library/ds/wavelet/wm_bit_points_cls.py.html
title: cp_library/ds/wavelet/wm_bit_points_cls.py
---
