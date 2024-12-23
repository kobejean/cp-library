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
    path: cp_library/math/nt/ntt_cls.py
    title: cp_library/math/nt/ntt_cls.py
  _extendedRequiredBy: []
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
    from typing import MutableSequence, SupportsIndex\nfrom cp_library.math.table.comb_table_cls\
    \ import CombTable\n\n    \nclass mint(int):\n    mod: int\n    zero: 'mint'\n\
    \    one: 'mint'\n    two: 'mint'\n    cache: list['mint']\n\n    def __new__(cls,\
    \ *args, **kwargs):\n        if (x := int(*args, **kwargs)) <= 2:\n          \
    \  return cls.cache[x]\n        else:\n            return cls.fix(x)\n\n    @classmethod\n\
    \    def set_mod(cls, mod: int):\n        mint.mod = cls.mod = mod\n        mint.zero\
    \ = cls.zero = cls.cast(0)\n        mint.one = cls.one = cls.fix(1)\n        mint.two\
    \ = cls.two = cls.fix(2)\n        mint.cache = cls.cache = [cls.zero, cls.one,\
    \ cls.two]\n\n    @classmethod\n    def fix(cls, x): return cls.cast(x%cls.mod)\n\
    \n    @classmethod\n    def cast(cls, x): return super().__new__(cls,x)\n\n  \
    \  @classmethod\n    def mod_inv(cls, x):\n        a,b,s,t = int(x), cls.mod,\
    \ 1, 0\n        while b: a,b,s,t = b,a%b,t,s-a//b*t\n        if a == 1: return\
    \ cls.fix(s)\n        raise ValueError(f\"{x} is not invertible in mod {cls.mod}\"\
    )\n    \n    @property\n    def inv(self): return mint.mod_inv(self)\n\n    def\
    \ __add__(self, x): return mint.fix(super().__add__(x))\n    def __radd__(self,\
    \ x): return mint.fix(super().__radd__(x))\n    def __sub__(self, x): return mint.fix(super().__sub__(x))\n\
    \    def __rsub__(self, x): return mint.fix(super().__rsub__(x))\n    def __mul__(self,\
    \ x): return mint.fix(super().__mul__(x))\n    def __rmul__(self, x): return mint.fix(super().__rmul__(x))\n\
    \    def __floordiv__(self, x): return self * mint.mod_inv(x)\n    def __rfloordiv__(self,\
    \ x): return self.inv * x\n    def __truediv__(self, x): return self * mint.mod_inv(x)\n\
    \    def __rtruediv__(self, x): return self.inv * x\n    def __pow__(self, x):\
    \ \n        return self.cast(super().__pow__(x, self.mod))\n    def __neg__(self):\
    \ return mint.mod-self\n    def __pos__(self): return self\n    def __abs__(self):\
    \ return self\n\nclass NTT:\n    def __init__(self, mod = 998244353) -> None:\n\
    \        self.mod = m = mod\n        self.g = g = self.primitive_root(m)\n   \
    \     self.rank2 = rank2 = ((m-1)&(1-m)).bit_length() - 1\n        self.root =\
    \ root = [0] * (rank2 + 1)\n        root[rank2] = pow(g, (m - 1) >> rank2, m)\n\
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
    \ g\n    \n    def fntt(self, A):\n        im, r8, m, h = self.root[2],self.rate3,self.mod,(len(A)-1).bit_length()\n\
    \        for L in range(0,h-1,2):\n            p, r = 1<<(h-L-2),1\n         \
    \   for s in range(1 << L):\n                r3,of=(r2:=r*r%m)*r%m,s<<(h-L)\n\
    \                for i in range(p):\n                    i3=(i2:=(i1:=(i0:=i+of)+p)+p)+p\n\
    \                    a0,a1,a2,a3 = A[i0],A[i1]*r,A[i2]*r2,A[i3]*r3\n         \
    \           a0,a1,a2,a3 = a0+a2,a1+a3,a0-a2,(a1-a3)%m*im\n                   \
    \ A[i0],A[i1],A[i2],A[i3] = (a0+a1)%m,(a0-a1)%m,(a2+a3)%m,(a2-a3)%m\n        \
    \        r=r*r8[(~s&-~s).bit_length()-1]%m\n        if h&1:\n            r, r8\
    \ = 1, self.rate2\n            for s in range(1<<(h-1)):\n                i1=(i0:=s<<1)+1\n\
    \                al,ar = A[i0],A[i1]*r%m\n                A[i0],A[i1] = (al+ar)%m,(al-ar)%m\n\
    \                r=r*r8[(~s&-~s).bit_length()-1]%m\n    \n    def ifntt(self,\
    \ A):\n        im, r8, m, h = self.iroot[2],self.irate3,self.mod,(len(A)-1).bit_length()\n\
    \        for L in range(h,1,-2):\n            p,r = 1<<(h-L),1\n            for\
    \ s in range(1<<(L-2)):\n                r3,of=(r2:=r*r%m)*r%m,s<<(h-L+2)\n  \
    \              for i in range(p):\n                    i3=(i2:=(i1:=(i0:=i+of)+p)+p)+p\n\
    \                    a0,a1,a2,a3 = A[i0],A[i1],A[i2],A[i3]\n                 \
    \   a0,a1,a2,a3 = a0+a1,a2+a3,a0-a1,(a2-a3)*im%m\n                    A[i0],A[i1],A[i2],A[i3]\
    \ = (a0+a1)%m,(a2+a3)*r%m,(a0-a1)*r2%m,(a2-a3)*r3%m\n                r=r*r8[(~s&-~s).bit_length()-1]%m\n\
    \        if h&1:\n            for i0 in range(p:=1<<(h-1)):\n                al,ar\
    \ = A[i0],A[i1:=i0+p]\n                A[i0],A[i1] = (al+ar)%m,(al-ar)%m\n   \
    \ \n    def conv_naive(self, A, B, N):\n        n, m, mod = len(A),len(B),self.mod\n\
    \        C = [0]*N\n        if n < m: A,B,n,m = B,A,m,n\n        for i,a in enumerate(A):\n\
    \            for j in range(min(m,N-i)):\n                C[ij]=(C[ij:=i+j]+a*B[j])%mod\n\
    \        return C\n    \n    def conv_fntt(self, A, B, N):\n        n,m,mod=len(A),len(B),self.mod\n\
    \        z=1<<(n+m-2).bit_length()\n        self.fntt(A:=A+[0]*(z-n)), self.fntt(B:=B+[0]*(z-m))\n\
    \        for i in range(z):A[i]=A[i]*B[i]%mod\n        self.ifntt(A)\n       \
    \ A,iz=A[:N],pow(z,mod-2,mod)\n        for i in range(N):A[i]=A[i]*iz%mod\n  \
    \      return A\n    \n    def conv(self, A, B, N = None):\n        n,m = len(A),\
    \ len(B)\n        N = n+m-1 if N is None else N\n        if min(n,m) <= 60: return\
    \ self.conv_naive(A, B, N)\n        return self.conv_fntt(A, B, N)\n\n    def\
    \ cycle_conv(self, A, B):\n        n,m,mod=len(A),len(B),self.mod\n        assert\
    \ n == m\n        if n==0:return[]\n        con,res=self.conv(A,B),[0]*n\n   \
    \     for i in range(n-1):res[i]=(con[i]+con[i+n])%mod\n        res[n-1]=con[n-1]\n\
    \        return res\n\nclass mint(mint):\n    ntt: NTT\n\n    @classmethod\n \
    \   def set_mod(cls, mod: int):\n        super().set_mod(mod)\n        cls.ntt\
    \ = NTT(mod)\n\nclass FPS(MutableSequence[int]):\n    def __init__(fps, coef:\
    \ list[int]):\n        fps.coef = coef\n\n    def __getitem__(fps, i: SupportsIndex,\
    \ /):\n        return fps.coef[i]\n        # return list.__getitem__(fps.coef,\
    \ i)\n    \n    def __setitem__(fps, i: SupportsIndex, a: int):\n        fps.coef[i]\
    \ = a\n        # list.__setitem__(fps, i, a)\n    \n    def __len__(fps):\n  \
    \      return len(fps.coef)\n    \n    def __contains__(self, value):\n      \
    \  return super().__contains__(value)\n    \n    def tayler_shift(fps, c: int)\
    \ -> list[int]:\n        inv, N, coef = (fact := CombTable.table).inv, len(fps),\
    \ fps.coef\n        res = [int(coef[i]*fact[i]) for i in range(N-1,-1,-1)]\n \
    \       B = [0]*N\n        B[0] = 1\n        for i in range(1, N):\n         \
    \   B[i] = int(B[i - 1] * inv[i] * c * fact[i-1])\n        res = mint.ntt.conv(res,\
    \ B, N)\n        return FPS([int(x * inv[i]) for i, x in enumerate(reversed(res))])\n\
    \    \n    def conv(fps, other):\n        return FPS(mint.ntt.conv(fps.coef[:],\
    \ other.coef))\n    def iconv(fps, other):\n        fps.coef = mint.ntt.conv(fps.coef,\
    \ other.coef)\n\n    def scalar_mul(fps, other):\n        return FPS([a*other\
    \ for a in fps.coef])\n    def iscalar_mul(fps, other):\n        coef = fps.coef\n\
    \        for i in range(len(coef)): coef[i] *= other\n    \n    def __mul__(lhs,\
    \ rhs):\n        if rhs.__class__ is FPS: return lhs.conv(rhs)\n        elif rhs.__class__\
    \ is list: return lhs.conv(FPS(rhs))\n        else: lhs.scalar_mul(rhs)\n\n  \
    \  __rmul__ = __mul__\n    \n    def __imul__(lhs, rhs):\n        if rhs.__class__\
    \ is FPS: lhs.iconv(rhs)\n        elif rhs.__class__ is list: lhs.iconv(FPS(rhs))\n\
    \        else: lhs.iscalar_mul(rhs)\n"
  code: "import cp_library.math.fps.__header__\nfrom typing import MutableSequence,\
    \ SupportsIndex\nfrom cp_library.math.table.comb_table_cls import CombTable\n\
    from cp_library.math.mod.mint_ntt_cls import mint\n\nclass FPS(MutableSequence[int]):\n\
    \    def __init__(fps, coef: list[int]):\n        fps.coef = coef\n\n    def __getitem__(fps,\
    \ i: SupportsIndex, /):\n        return fps.coef[i]\n        # return list.__getitem__(fps.coef,\
    \ i)\n    \n    def __setitem__(fps, i: SupportsIndex, a: int):\n        fps.coef[i]\
    \ = a\n        # list.__setitem__(fps, i, a)\n    \n    def __len__(fps):\n  \
    \      return len(fps.coef)\n    \n    def __contains__(self, value):\n      \
    \  return super().__contains__(value)\n    \n    def tayler_shift(fps, c: int)\
    \ -> list[int]:\n        inv, N, coef = (fact := CombTable.table).inv, len(fps),\
    \ fps.coef\n        res = [int(coef[i]*fact[i]) for i in range(N-1,-1,-1)]\n \
    \       B = [0]*N\n        B[0] = 1\n        for i in range(1, N):\n         \
    \   B[i] = int(B[i - 1] * inv[i] * c * fact[i-1])\n        res = mint.ntt.conv(res,\
    \ B, N)\n        return FPS([int(x * inv[i]) for i, x in enumerate(reversed(res))])\n\
    \    \n    def conv(fps, other):\n        return FPS(mint.ntt.conv(fps.coef[:],\
    \ other.coef))\n    def iconv(fps, other):\n        fps.coef = mint.ntt.conv(fps.coef,\
    \ other.coef)\n\n    def scalar_mul(fps, other):\n        return FPS([a*other\
    \ for a in fps.coef])\n    def iscalar_mul(fps, other):\n        coef = fps.coef\n\
    \        for i in range(len(coef)): coef[i] *= other\n    \n    def __mul__(lhs,\
    \ rhs):\n        if rhs.__class__ is FPS: return lhs.conv(rhs)\n        elif rhs.__class__\
    \ is list: return lhs.conv(FPS(rhs))\n        else: lhs.scalar_mul(rhs)\n\n  \
    \  __rmul__ = __mul__\n    \n    def __imul__(lhs, rhs):\n        if rhs.__class__\
    \ is FPS: lhs.iconv(rhs)\n        elif rhs.__class__ is list: lhs.iconv(FPS(rhs))\n\
    \        else: lhs.iscalar_mul(rhs)\n"
  dependsOn:
  - cp_library/math/mod/mint_ntt_cls.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/nt/ntt_cls.py
  isVerificationFile: false
  path: cp_library/math/fps/fps_cls.py
  requiredBy: []
  timestamp: '2024-12-23 15:11:03+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/fps/fps_cls.py
layout: document
redirect_from:
- /library/cp_library/math/fps/fps_cls.py
- /library/cp_library/math/fps/fps_cls.py.html
title: cp_library/math/fps/fps_cls.py
---
