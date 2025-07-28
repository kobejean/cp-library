---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_ntt_cls.py
    title: cp_library/math/mod/mint_ntt_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/nt/mod_inv_fn.py
    title: cp_library/math/nt/mod_inv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/nt/ntt_cls.py
    title: cp_library/math/nt/ntt_cls.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: perf/mlist.py
    title: perf/mlist.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\n    \nclass mint(int):\n    mod: int\n    zero: 'mint'\n    one: 'mint'\n\
    \    two: 'mint'\n    cache: list['mint']\n    def __new__(cls, *args, **kwargs):\n\
    \        if 0 <= (x := int(*args, **kwargs)) < 64: return cls.cache[x]\n     \
    \   else: return cls.fix(x)\n    @classmethod\n    def set_mod(cls, mod: int):\n\
    \        mint.mod = cls.mod = mod\n        mint.zero = cls.zero = cls.cast(0)\n\
    \        mint.one = cls.one = cls.fix(1)\n        mint.two = cls.two = cls.fix(2)\n\
    \        mint.cache = cls.cache = [cls.zero, cls.one, cls.two]\n        for x\
    \ in range(3,64): mint.cache.append(cls.fix(x))\n    @classmethod\n    def fix(cls,\
    \ x): return cls.cast(x%cls.mod)\n    @classmethod\n    def cast(cls, x): return\
    \ super().__new__(cls,x)\n    @classmethod\n    def mod_inv(cls, x):\n       \
    \ a,b,s,t = int(x), cls.mod, 1, 0\n        while b: a,b,s,t = b,a%b,t,s-a//b*t\n\
    \        if a == 1: return cls.fix(s)\n        raise ValueError(f\"{x} is not\
    \ invertible in mod {cls.mod}\")\n    @property\n    def inv(self): return mint.mod_inv(self)\n\
    \    def __add__(self, x): return mint.fix(super().__add__(x))\n    def __radd__(self,\
    \ x): return mint.fix(super().__radd__(x))\n    def __sub__(self, x): return mint.fix(super().__sub__(x))\n\
    \    def __rsub__(self, x): return mint.fix(super().__rsub__(x))\n    def __mul__(self,\
    \ x): return mint.fix(super().__mul__(x))\n    def __rmul__(self, x): return mint.fix(super().__rmul__(x))\n\
    \    def __floordiv__(self, x): return self * mint.mod_inv(x)\n    def __rfloordiv__(self,\
    \ x): return self.inv * x\n    def __truediv__(self, x): return self * mint.mod_inv(x)\n\
    \    def __rtruediv__(self, x): return self.inv * x\n    def __pow__(self, x):\
    \ return self.cast(super().__pow__(x, self.mod))\n    def __neg__(self): return\
    \ mint.mod-self\n    def __pos__(self): return self\n    def __abs__(self): return\
    \ self\n    def __class_getitem__(self, x: int): return self.cache[x]\n\n\ndef\
    \ mod_inv(x, mod):\n    a, b, s, t = x, mod, 1, 0\n    while b:\n        a, b,\
    \ s, t = b,a%b,t,s-a//b*t\n    if a == 1: return s % mod\n    raise ValueError(f\"\
    {x} is not invertible in mod {mod}\")\n\nclass NTT:\n    def __init__(self, mod\
    \ = 998244353) -> None:\n        self.mod = m = mod\n        self.g = g = self.primitive_root(m)\n\
    \        self.rank2 = rank2 = ((m-1)&(1-m)).bit_length() - 1\n        self.root\
    \ = root = [0] * (rank2 + 1)\n        root[rank2] = pow(g, (m - 1) >> rank2, m)\n\
    \        self.iroot = iroot = [0] * (rank2 + 1)\n        iroot[rank2] = pow(root[rank2],\
    \ m - 2, m)\n        for i in range(rank2 - 1, -1, -1):\n            root[i] =\
    \ root[i+1] * root[i+1] % m\n            iroot[i] = iroot[i+1] * iroot[i+1] %\
    \ m\n        def rates(s):\n            r8,ir8 = [0]*max(0,rank2-s+1), [0]*max(0,rank2-s+1)\n\
    \            p = ip = 1\n            for i in range(rank2-s+1):\n            \
    \    r, ir = root[i+s], iroot[i+s]\n                p,ip,r8[i],ir8[i]= p*ir%m,ip*r%m,r*p%m,ir*ip%m\n\
    \            return r8, ir8\n        self.rate2, self.irate2 = rates(2)\n    \
    \    self.rate3, self.irate3 = rates(3)\n \n    def primitive_root(self, m):\n\
    \        if m == 2: return 1\n        if m == 167772161: return 3\n        if\
    \ m == 469762049: return 3\n        if m == 754974721: return 11\n        if m\
    \ == 998244353: return 3\n        divs = [0] * 20\n        cnt, divs[0], x = 1,\
    \ 2, (m - 1) // 2\n        while x % 2 == 0: x //= 2\n        i=3\n        while\
    \ i*i <= x:\n            if x%i == 0:\n                divs[cnt],cnt = i,cnt+1\n\
    \                while x%i==0:x//=i\n            i+=2\n        if x > 1: divs[cnt],cnt\
    \ = x,cnt+1\n        for g in range(2,m):\n            for i in range(cnt):\n\
    \                if pow(g,(m-1)//divs[i],m)==1:break\n            else:return\
    \ g\n    \n    def fntt(self, A: list[int]):\n        im, r8, m, h = self.root[2],self.rate3,self.mod,(len(A)-1).bit_length()\n\
    \        for L in range(0,h-1,2):\n            p, r = 1<<(h-L-2),1\n         \
    \   for s in range(1 << L):\n                r3,of=(r2:=r*r%m)*r%m,s<<(h-L)\n\
    \                for i in range(p):\n                    i3=(i2:=(i1:=(i0:=i+of)+p)+p)+p\n\
    \                    a0,a1,a2,a3 = A[i0],A[i1]*r,A[i2]*r2,A[i3]*r3\n         \
    \           a0,a1,a2,a3 = a0+a2,a1+a3,a0-a2,(a1-a3)%m*im\n                   \
    \ A[i0],A[i1],A[i2],A[i3] = (a0+a1)%m,(a0-a1)%m,(a2+a3)%m,(a2-a3)%m\n        \
    \        r=r*r8[(~s&-~s).bit_length()-1]%m\n        if h&1:\n            r, r8\
    \ = 1, self.rate2\n            for s in range(1<<(h-1)):\n                i1=(i0:=s<<1)+1\n\
    \                al,ar = A[i0],A[i1]*r%m\n                A[i0],A[i1] = (al+ar)%m,(al-ar)%m\n\
    \                r=r*r8[(~s&-~s).bit_length()-1]%m\n        return A\n    \n \
    \   def _ifntt(self, A: list[int]):\n        im, r8, m, h = self.iroot[2],self.irate3,self.mod,(len(A)-1).bit_length()\n\
    \        for L in range(h,1,-2):\n            p,r = 1<<(h-L),1\n            for\
    \ s in range(1<<(L-2)):\n                r3,of=(r2:=r*r%m)*r%m,s<<(h-L+2)\n  \
    \              for i in range(p):\n                    i3=(i2:=(i1:=(i0:=i+of)+p)+p)+p\n\
    \                    a0,a1,a2,a3 = A[i0],A[i1],A[i2],A[i3]\n                 \
    \   a0,a1,a2,a3 = a0+a1,a2+a3,a0-a1,(a2-a3)*im%m\n                    A[i0],A[i1],A[i2],A[i3]\
    \ = (a0+a1)%m,(a2+a3)*r%m,(a0-a1)*r2%m,(a2-a3)*r3%m\n                r=r*r8[(~s&-~s).bit_length()-1]%m\n\
    \        if h&1:\n            for i0 in range(p:=1<<(h-1)):\n                al,ar\
    \ = A[i0],A[i1:=i0+p]\n                A[i0],A[i1] = (al+ar)%m,(al-ar)%m\n   \
    \     return A\n\n    def ifntt(self, A: list[int]):\n        self._ifntt(A)\n\
    \        iz = mod_inv(N:=len(A),mod:=self.mod)\n        for i in range(N): A[i]=A[i]*iz%mod\n\
    \        return A\n    \n    def conv_naive(self, A, B, N):\n        n, m, mod\
    \ = len(A),len(B),self.mod\n        C = [0]*N\n        if n < m: A,B,n,m = B,A,m,n\n\
    \        for i,a in enumerate(A):\n            for j in range(min(m,N-i)):\n \
    \               C[ij]=(C[ij:=i+j]+a*B[j])%mod\n        return C\n    \n    def\
    \ conv_fntt(self, A, B, N):\n        n,m,mod=len(A),len(B),self.mod\n        z=1<<(n+m-2).bit_length()\n\
    \        self.fntt(A:=A+[0]*(z-n)), self.fntt(B:=B+[0]*(z-m))\n        for i,\
    \ b in enumerate(B): A[i] = A[i] * b % mod\n        self.ifntt(A)\n        del\
    \ A[N:]\n        return A\n    \n    def deconv(self, C, B, N = None):\n     \
    \   n, m = len(C), len(B)\n        if N is None: N = n - m + 1\n        z = 1\
    \ << (n + m - 2).bit_length()\n        self.fntt(C := C+[0]*(z-n)), self.fntt(B\
    \ := B+[0]*(z - m))\n\n        A = [0] * z\n        for i in range(z):\n     \
    \       if B[i] == 0:\n                raise ValueError(\"Division by zero in\
    \ NTT domain - deconvolution not possible\")\n            b_inv = mod_inv(B[i],\
    \ self.mod)\n            A[i] = (C[i] * b_inv) % self.mod\n        \n        self.ifntt(A)\n\
    \        return A[:N]\n    \n    def conv_half(self, A, Bres):\n        mod =\
    \ self.mod\n        self.fntt(A)\n        for i, b in enumerate(Bres): A[i] =\
    \ A[i] * b % mod\n        self.ifntt(A)\n        return A\n    \n    def conv(self,\
    \ A, B, N = None):\n        n,m = len(A), len(B)\n        N = n+m-1 if N is None\
    \ else N\n        if min(n,m) <= 60: return self.conv_naive(A, B, N)\n       \
    \ return self.conv_fntt(A, B, N)\n\n    def cycle_conv(self, A, B):\n        n,m,mod=len(A),len(B),self.mod\n\
    \        assert n == m\n        if n==0:return[]\n        con,res=self.conv(A,B),[0]*n\n\
    \        for i in range(n-1):res[i]=(con[i]+con[i+n])%mod\n        res[n-1]=con[n-1]\n\
    \        return res\n\nclass mint(mint):\n    ntt: NTT\n\n    @classmethod\n \
    \   def set_mod(cls, mod: int):\n        super().set_mod(mod)\n        cls.ntt\
    \ = NTT(mod)\n\nclass mlist:\n    def __init__(lst, data): lst.data = [0]*data\
    \ if isinstance(data, int) else [int(x) for x in data]\n    @staticmethod\n  \
    \  def from_raw(data: list[int]):\n        (lst := mlist.__new__(mlist)).data\
    \ = data\n        return lst\n    def __getitem__(lst, i) -> mint: return mint(lst.data[i])\n\
    \    def __setitem__(lst, i, x): lst.data[i] = int(x)\n    def __len__(lst): return\
    \ len(lst.data)\n    def conv(A, B, N):\n        A = A.data\n        B = B.data\
    \ if hasattr(B, 'data') else B\n        return mlist.from_raw(mint.ntt.conv(A,\
    \ B, N))\n"
  code: "import cp_library.__header__\nimport cp_library.math.__header__\nimport cp_library.math.mod.__header__\n\
    from cp_library.math.mod.mint_ntt_cls import mint\n\nclass mlist:\n    def __init__(lst,\
    \ data): lst.data = [0]*data if isinstance(data, int) else [int(x) for x in data]\n\
    \    @staticmethod\n    def from_raw(data: list[int]):\n        (lst := mlist.__new__(mlist)).data\
    \ = data\n        return lst\n    def __getitem__(lst, i) -> mint: return mint(lst.data[i])\n\
    \    def __setitem__(lst, i, x): lst.data[i] = int(x)\n    def __len__(lst): return\
    \ len(lst.data)\n    def conv(A, B, N):\n        A = A.data\n        B = B.data\
    \ if hasattr(B, 'data') else B\n        return mlist.from_raw(mint.ntt.conv(A,\
    \ B, N))"
  dependsOn:
  - cp_library/math/mod/mint_ntt_cls.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/nt/ntt_cls.py
  - cp_library/math/nt/mod_inv_fn.py
  isVerificationFile: false
  path: cp_library/math/mod/mlist_cls.py
  requiredBy:
  - perf/mlist.py
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/mod/mlist_cls.py
layout: document
redirect_from:
- /library/cp_library/math/mod/mlist_cls.py
- /library/cp_library/math/mod/mlist_cls.py.html
title: cp_library/math/mod/mlist_cls.py
---
