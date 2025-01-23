---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/reserve_fn.py
    title: cp_library/ds/reserve_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_deriv_fn.py
    title: cp_library/math/fps/fps_deriv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_exp_fn.py
    title: cp_library/math/fps/fps_exp_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_integ_fn.py
    title: cp_library/math/fps/fps_integ_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_inv_fn.py
    title: cp_library/math/fps/fps_inv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_log_fn.py
    title: cp_library/math/fps/fps_log_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_normalize_fn.py
    title: cp_library/math/fps/fps_normalize_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_pow_fn.py
    title: cp_library/math/fps/fps_pow_fn.py
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
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/modcomb_cls.py
    title: cp_library/math/table/modcomb_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
    title: test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
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
    from typing import SupportsIndex\n\n    \nclass mint(int):\n    mod: int\n   \
    \ zero: 'mint'\n    one: 'mint'\n    two: 'mint'\n    cache: list['mint']\n\n\
    \    def __new__(cls, *args, **kwargs):\n        if 0<= (x := int(*args, **kwargs))\
    \ <= 2:\n            return cls.cache[x]\n        else:\n            return cls.fix(x)\n\
    \n    @classmethod\n    def set_mod(cls, mod: int):\n        mint.mod = cls.mod\
    \ = mod\n        mint.zero = cls.zero = cls.cast(0)\n        mint.one = cls.one\
    \ = cls.fix(1)\n        mint.two = cls.two = cls.fix(2)\n        mint.cache =\
    \ cls.cache = [cls.zero, cls.one, cls.two]\n\n    @classmethod\n    def fix(cls,\
    \ x): return cls.cast(x%cls.mod)\n\n    @classmethod\n    def cast(cls, x): return\
    \ super().__new__(cls,x)\n\n    @classmethod\n    def mod_inv(cls, x):\n     \
    \   a,b,s,t = int(x), cls.mod, 1, 0\n        while b: a,b,s,t = b,a%b,t,s-a//b*t\n\
    \        if a == 1: return cls.fix(s)\n        raise ValueError(f\"{x} is not\
    \ invertible in mod {cls.mod}\")\n    \n    @property\n    def inv(self): return\
    \ mint.mod_inv(self)\n\n    def __add__(self, x): return mint.fix(super().__add__(x))\n\
    \    def __radd__(self, x): return mint.fix(super().__radd__(x))\n    def __sub__(self,\
    \ x): return mint.fix(super().__sub__(x))\n    def __rsub__(self, x): return mint.fix(super().__rsub__(x))\n\
    \    def __mul__(self, x): return mint.fix(super().__mul__(x))\n    def __rmul__(self,\
    \ x): return mint.fix(super().__rmul__(x))\n    def __floordiv__(self, x): return\
    \ self * mint.mod_inv(x)\n    def __rfloordiv__(self, x): return self.inv * x\n\
    \    def __truediv__(self, x): return self * mint.mod_inv(x)\n    def __rtruediv__(self,\
    \ x): return self.inv * x\n    def __pow__(self, x): \n        return self.cast(super().__pow__(x,\
    \ self.mod))\n    def __neg__(self): return mint.mod-self\n    def __pos__(self):\
    \ return self\n    def __abs__(self): return self\n\n\ndef mod_inv(x, mod):\n\
    \    a,b,s,t = x, mod, 1, 0\n    while b:\n        a,b,s,t = b,a%b,t,s-a//b*t\n\
    \    if a == 1: return s % mod\n    raise ValueError(f\"{x} is not invertible\
    \ in mod {mod}\")\nfrom itertools import accumulate\n\nclass modcomb():\n    fact:\
    \ list[int]\n    fact_inv: list[int]\n    inv: list[int] = [0,1]\n\n    @staticmethod\n\
    \    def precomp(N):\n        mod = mint.mod\n        def mod_mul(a,b): return\
    \ a*b%mod\n        fact = list(accumulate(range(1,N+1), mod_mul, initial=1))\n\
    \        fact_inv = list(accumulate(range(N,0,-1), mod_mul, initial=mod_inv(fact[N],\
    \ mod)))\n        fact_inv.reverse()\n        modcomb.fact, modcomb.fact_inv =\
    \ fact, fact_inv\n    \n    @staticmethod\n    def extend_inv(N):\n        N,\
    \ inv, mod = N+1, modcomb.inv, mint.mod\n        while len(inv) < N:\n       \
    \     j, k = divmod(mod, len(inv))\n            inv.append(-inv[k] * j % mod)\n\
    \n    @staticmethod\n    def factorial(n: int, /) -> mint:\n        return mint(modcomb.fact[n])\n\
    \n    @staticmethod\n    def comb(n: int, k: int, /) -> mint:\n        inv, mod\
    \ = modcomb.fact_inv, mint.mod\n        if n < k: return mint.zero\n        return\
    \ mint(inv[k] * inv[n-k] % mod * modcomb.fact[n])\n    nCk = binom = comb\n  \
    \  \n    @staticmethod\n    def comb_with_replacement(n: int, k: int, /) -> mint:\n\
    \        if n <= 0: return mint.zero\n        return modcomb.nCk(n + k - 1, k)\n\
    \    nHk = comb_with_replacement\n    \n    @staticmethod\n    def multinom(n:\
    \ int, *K: int) -> mint:\n        nCk, res = modcomb.nCk, mint.one\n        for\
    \ k in K: res, n = res*nCk(n,k), n-k\n        return res\n\n    @staticmethod\n\
    \    def perm(n: int, k: int, /) -> mint:\n        \"\"\"Returns P(n,k) mod p\"\
    \"\"\n        if n < k: return mint.zero\n        return mint(modcomb.fact[n]\
    \ * modcomb.fact_inv[n-k])\n    nPk = perm\n    \n    @staticmethod\n    def catalan(n:\
    \ int, /) -> mint:\n        return mint(modcomb.nCk(2*n,n) * modcomb.fact_inv[n+1])\n\
    \n\ndef fps_deriv(P: list[int]):\n    mod = mint.mod\n    return [P[i]*i%mod for\
    \ i in range(1,len(P))]\n\n\ndef fps_integ(P: list) -> list:\n    N, mod = len(P),\
    \ mint.mod\n    res = [0] * (N+1)\n    if N:\n        res[1] = 1\n    for i in\
    \ range(2, N+1):\n        j, k = divmod(mod, i)\n        res[i] = (-res[k] * j)\
    \ % mod\n    for i, x in enumerate(P, start=1):\n        res[i] = res[i] * x %\
    \ mod\n    return res\n\n\ndef fps_inv(P: list) -> list:\n    ntt, inv, d = mint.ntt,\
    \ [0]*(deg:=len(P)), 1\n    inv[0] = mod_inv(P[0], mod := mint.mod)\n    while\
    \ d < deg:\n        sz, f, g = min(deg,z:=d<<1), [0]*z, [0]*z\n        f[:sz],\
    \ g[:d] = P[:sz], inv[:d]\n        ntt.conv_half(f,gres:=ntt.fntt(g))\n      \
    \  f[:d] = [0]*d\n        ntt.conv_half(f,gres)\n        for j in range(d,sz):\
    \ inv[j] = mod-f[j] if f[j] else 0\n        d = z\n    return inv\n\n\n\nclass\
    \ NTT:\n    def __init__(self, mod = 998244353) -> None:\n        self.mod = m\
    \ = mod\n        self.g = g = self.primitive_root(m)\n        self.rank2 = rank2\
    \ = ((m-1)&(1-m)).bit_length() - 1\n        self.root = root = [0] * (rank2 +\
    \ 1)\n        root[rank2] = pow(g, (m - 1) >> rank2, m)\n        self.iroot =\
    \ iroot = [0] * (rank2 + 1)\n        iroot[rank2] = pow(root[rank2], m - 2, m)\n\
    \        for i in range(rank2 - 1, -1, -1):\n            root[i] = root[i+1] *\
    \ root[i+1] % m\n            iroot[i] = iroot[i+1] * iroot[i+1] % m\n        def\
    \ rates(s):\n            r8,ir8 = [0]*max(0,rank2-s+1), [0]*max(0,rank2-s+1)\n\
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
    \ = NTT(mod)\n\ndef fps_log(P: list) -> list:\n    return fps_integ(mint.ntt.conv(fps_deriv(P),\
    \ fps_inv(P), len(P)-1))\n\n\ndef fps_exp(P: list) -> list:\n    max_sz = 1 <<\
    \ ((deg := len(P))-1).bit_length()\n    modcomb.extend_inv(max_sz)\n    inv, mod,\
    \ ntt = modcomb.inv, mint.mod, mint.ntt\n    fntt, ifntt, conv_half = ntt.fntt,\
    \ ntt.ifntt, ntt.conv_half\n    dP = fps_deriv(P) + [0]*(max_sz-deg+1)\n    R,\
    \ E, Eres = [1, (P[1] if 1 < deg else 0)], [1], [1, 1]\n    reserve(R, max_sz),\
    \ reserve(E, max_sz)\n    p = 2\n    while p < deg:\n        Rres = fntt(R + [0]*p)\n\
    \        x = ifntt([Rres[i]*-e%mod for i, e in enumerate(Eres)])\n        x[:h]\
    \ = [0]*(h:=p>>1)\n        E[h:] = conv_half(x, Eres)[h:]\n        Eres = fntt(E\
    \ + [0]*p)\n        x = conv_half(dP[:p-1]+[0], Rres[:p])\n        for i in range(1,p):\
    \ x[i-1] -= R[i]*i % mod\n        x += [0] * p\n        for i in range(p-1): x[p+i],x[i]\
    \ = x[i],0\n        conv_half(x,Eres)\n        for i in range(min(deg, p<<1)-1,p-1,-1):\
    \ x[i] = P[i]+x[i-1]*inv[i]%mod \n        x[:p] = [0] * p\n        R[p:] = conv_half(x,Rres)[p:]\n\
    \        p <<= 1\n    return R[:deg]\n\n\n\ndef reserve(A: list, est_len: int)\
    \ -> None: ...\ntry:\n    from __pypy__ import resizelist_hint\nexcept:\n    def\
    \ resizelist_hint(A: list, est_len: int):\n        pass\nreserve = resizelist_hint\n\
    \ndef fps_normalize(P: list, deg) -> list:\n    if (N:=len(P)) < deg: P[N:] =\
    \ [0]*(deg-N)\n    del P[deg:]\n    return P\n\ndef fps_pow(P: list, k: int, deg\
    \ = -1) -> list:\n    deg, mod = (len(P) if deg<0 else deg), mint.mod\n    if\
    \ k == 0: return [1]+[0]*(deg-1) if deg else []\n    i = next((i for i, c in enumerate(P)\
    \ if c), default=deg)\n    if i * k >= deg: return [0] * deg\n    inv, alpha =\
    \ mod_inv(P[i],mod), pow(P[i], k, mod)\n    R = fps_log([P[j]*inv%mod for j in\
    \ range(i,deg)])\n    for j,r in enumerate(R): R[j] = r*k%mod\n    R = fps_exp(R)\n\
    \    for j,r in enumerate(R): R[j] = r*alpha%mod\n    R[:0] = [0] * (i * k)\n\
    \    return fps_normalize(R, deg)\n\n\ndef stirling2_k(n: SupportsIndex, k: SupportsIndex):\n\
    \    kinv,fact,mod = modcomb.fact_inv[k],modcomb.fact,mint.mod\n    R = fps_pow(modcomb.fact_inv[1:n+2-k],k,n+1-k)\n\
    \    return [mint(r*kinv%mod*fact[i]) for i,r in enumerate(R,start=k)]\n"
  code: "import cp_library.math.table.__header__\nfrom typing import SupportsIndex\n\
    from cp_library.math.table.modcomb_cls import modcomb\nfrom cp_library.math.mod.mint_cls\
    \ import mint\nfrom cp_library.math.fps.fps_pow_fn import fps_pow\n\ndef stirling2_k(n:\
    \ SupportsIndex, k: SupportsIndex):\n    kinv,fact,mod = modcomb.fact_inv[k],modcomb.fact,mint.mod\n\
    \    R = fps_pow(modcomb.fact_inv[1:n+2-k],k,n+1-k)\n    return [mint(r*kinv%mod*fact[i])\
    \ for i,r in enumerate(R,start=k)]"
  dependsOn:
  - cp_library/math/table/modcomb_cls.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/fps/fps_pow_fn.py
  - cp_library/math/fps/fps_log_fn.py
  - cp_library/math/fps/fps_exp_fn.py
  - cp_library/math/fps/fps_normalize_fn.py
  - cp_library/math/mod/mint_ntt_cls.py
  - cp_library/math/nt/mod_inv_fn.py
  - cp_library/math/fps/fps_deriv_fn.py
  - cp_library/math/fps/fps_integ_fn.py
  - cp_library/math/fps/fps_inv_fn.py
  - cp_library/ds/reserve_fn.py
  - cp_library/math/nt/ntt_cls.py
  isVerificationFile: false
  path: cp_library/math/table/stirling2_k_fn.py
  requiredBy: []
  timestamp: '2025-01-24 05:21:27+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
documentation_of: cp_library/math/table/stirling2_k_fn.py
layout: document
redirect_from:
- /library/cp_library/math/table/stirling2_k_fn.py
- /library/cp_library/math/table/stirling2_k_fn.py.html
title: cp_library/math/table/stirling2_k_fn.py
---
