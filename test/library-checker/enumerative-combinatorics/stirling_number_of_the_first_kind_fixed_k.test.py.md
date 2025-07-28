---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/reserve_fn.py
    title: cp_library/ds/list/reserve_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_cls.py
    title: cp_library/io/io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_fn.py
    title: cp_library/io/read_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
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
    path: cp_library/math/table/mcomb_cls.py
    title: cp_library/math/table/mcomb_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling1_k_fn.py
    title: cp_library/math/table/stirling1_k_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/stirling_number_of_the_first_kind_fixed_k
    links:
    - https://judge.yosupo.jp/problem/stirling_number_of_the_first_kind_fixed_k
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/stirling_number_of_the_first_kind_fixed_k\n\
    \ndef main():\n    mint.set_mod(998244353)\n    N, K = read()\n    mcomb.precomp(N)\n\
    \    write(*stirling1_k(N, K))\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n    \nclass mint(int):\n    mod: int\n    zero: 'mint'\n\
    \    one: 'mint'\n    two: 'mint'\n    cache: list['mint']\n    def __new__(cls,\
    \ *args, **kwargs):\n        if 0 <= (x := int(*args, **kwargs)) < 64: return\
    \ cls.cache[x]\n        else: return cls.fix(x)\n    @classmethod\n    def set_mod(cls,\
    \ mod: int):\n        mint.mod = cls.mod = mod\n        mint.zero = cls.zero =\
    \ cls.cast(0)\n        mint.one = cls.one = cls.fix(1)\n        mint.two = cls.two\
    \ = cls.fix(2)\n        mint.cache = cls.cache = [cls.zero, cls.one, cls.two]\n\
    \        for x in range(3,64): mint.cache.append(cls.fix(x))\n    @classmethod\n\
    \    def fix(cls, x): return cls.cast(x%cls.mod)\n    @classmethod\n    def cast(cls,\
    \ x): return super().__new__(cls,x)\n    @classmethod\n    def mod_inv(cls, x):\n\
    \        a,b,s,t = int(x), cls.mod, 1, 0\n        while b: a,b,s,t = b,a%b,t,s-a//b*t\n\
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
    {x} is not invertible in mod {mod}\")\nfrom itertools import accumulate\n\nclass\
    \ mcomb():\n    fact: list[int]\n    fact_inv: list[int]\n    inv: list[int] =\
    \ [0,1]\n\n    @staticmethod\n    def precomp(N):\n        mod = mint.mod\n  \
    \      def mod_mul(a,b): return a*b%mod\n        fact = list(accumulate(range(1,N+1),\
    \ mod_mul, initial=1))\n        fact_inv = list(accumulate(range(N,0,-1), mod_mul,\
    \ initial=mod_inv(fact[N], mod)))\n        fact_inv.reverse()\n        mcomb.fact,\
    \ mcomb.fact_inv = fact, fact_inv\n    \n    @staticmethod\n    def extend_inv(N):\n\
    \        N, inv, mod = N+1, mcomb.inv, mint.mod\n        while len(inv) < N:\n\
    \            j, k = divmod(mod, len(inv))\n            inv.append(-inv[k] * j\
    \ % mod)\n\n    @staticmethod\n    def factorial(n: int, /) -> mint:\n       \
    \ return mint(mcomb.fact[n])\n\n    @staticmethod\n    def comb(n: int, k: int,\
    \ /) -> mint:\n        inv, mod = mcomb.fact_inv, mint.mod\n        if n < k or\
    \ k < 0: return mint.zero\n        return mint(inv[k] * inv[n-k] % mod * mcomb.fact[n])\n\
    \    nCk = binom = comb\n    \n    @staticmethod\n    def comb_with_replacement(n:\
    \ int, k: int, /) -> mint:\n        if n <= 0: return mint.zero\n        return\
    \ mcomb.nCk(n + k - 1, k)\n    nHk = comb_with_replacement\n    \n    @staticmethod\n\
    \    def multinom(n: int, *K: int) -> mint:\n        nCk, res = mcomb.nCk, mint.one\n\
    \        for k in K: res, n = res*nCk(n,k), n-k\n        return res\n\n    @staticmethod\n\
    \    def perm(n: int, k: int, /) -> mint:\n        '''Returns P(n,k) mod p'''\n\
    \        if n < k: return mint.zero\n        return mint(mcomb.fact[n] * mcomb.fact_inv[n-k])\n\
    \    nPk = perm\n    \n    @staticmethod\n    def catalan(n: int, /) -> mint:\n\
    \        return mint(mcomb.nCk(2*n,n) * mcomb.fact_inv[n+1])\nfrom typing import\
    \ SupportsIndex\n\nclass NTT:\n    def __init__(self, mod = 998244353) -> None:\n\
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
    \ = NTT(mod)\n\n\ndef fps_deriv(P: list[int]):\n    mod = mint.mod\n    return\
    \ [P[i]*i%mod for i in range(1,len(P))]\n\n\ndef fps_integ(P: list) -> list:\n\
    \    N, mod = len(P), mint.mod; res = [0] * (N+1)\n    if N: res[1] = 1\n    for\
    \ i in range(2, N+1): j, k = divmod(mod, i); res[i] = (-res[k] * j) % mod\n  \
    \  for i, x in enumerate(P, start=1): res[i] = res[i] * x % mod\n    return res\n\
    \n\ndef fps_inv(P: list) -> list:\n    ntt, inv, d = mint.ntt, [0]*(deg:=len(P)),\
    \ 1\n    inv[0] = mod_inv(P[0], mod := mint.mod)\n    while d < deg:\n       \
    \ sz, f, g = min(deg,z:=d<<1), [0]*z, [0]*z\n        f[:sz], g[:d] = P[:sz], inv[:d]\n\
    \        ntt.conv_half(f,gres:=ntt.fntt(g))\n        f[:d] = [0]*d\n        ntt.conv_half(f,gres)\n\
    \        for j in range(d,sz): inv[j] = mod-f[j] if f[j] else 0\n        d = z\n\
    \    return inv\n\n\ndef fps_log(P: list) -> list: return fps_integ(mint.ntt.conv(fps_deriv(P),\
    \ fps_inv(P), len(P)-1))\n\ndef fps_exp(P: list) -> list:\n    max_sz = 1 << ((deg\
    \ := len(P))-1).bit_length()\n    mcomb.extend_inv(max_sz)\n    inv, mod, ntt\
    \ = mcomb.inv, mint.mod, mint.ntt\n    fntt, ifntt, conv_half = ntt.fntt, ntt.ifntt,\
    \ ntt.conv_half\n    dP = fps_deriv(P) + [0]*(max_sz-deg+1)\n    R, E, Eres =\
    \ [1, (P[1] if 1 < deg else 0)], [1], [1, 1]\n    reserve(R, max_sz), reserve(E,\
    \ max_sz)\n    p = 2\n    while p < deg:\n        Rres = fntt(R + [0]*p)\n   \
    \     x = ifntt([Rres[i]*-e%mod for i, e in enumerate(Eres)])\n        for i in\
    \ range(h:=p>>1): x[i] = 0\n        E.extend(conv_half(x, Eres)[h:])\n       \
    \ Eres = fntt(E + [0]*p)\n        x = conv_half(dP[:p-1]+[0], Rres[:p])\n    \
    \    for i in range(1,p): x[i-1] -= R[i]*i % mod\n        x += [0] * p\n     \
    \   for i in range(p-1): x[p+i],x[i] = x[i],0\n        conv_half(x,Eres)\n   \
    \     for i in range(min(deg, p<<1)-1,p-1,-1): x[i] = P[i]+x[i-1]*inv[i]%mod \n\
    \        for i in range(p): x[i] = 0\n        R.extend(conv_half(x,Rres)[p:])\n\
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
    \    return fps_normalize(R, deg)\n\ndef stirling1_k(n: SupportsIndex, k: SupportsIndex,\
    \ signed = True):\n    mcomb.extend_inv(n+k)\n    kinv,fact,mod,deg = mcomb.fact_inv[k],mcomb.fact,mint.mod,n+1-k\n\
    \    R = mcomb.inv[1:deg+1]\n    if signed:\n        for i in range(1,deg,2):\
    \ R[i] = mod - R[i]\n    return [mint(r*kinv%mod*fact[i]) for i,r in enumerate(fps_pow(R,k,deg),start=k)]\n\
    \nfrom typing import Type, Union, overload\nfrom typing import TypeVar\n_S = TypeVar('S');\
    \ _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    \n\n@overload\ndef read() -> list[int]: ...\n@overload\ndef read(spec: Type[_T],\
    \ char=False) -> _T: ...\n@overload\ndef read(spec: _U, char=False) -> _U: ...\n\
    @overload\ndef read(*specs: Type[_T], char=False) -> tuple[_T, ...]: ...\n@overload\n\
    def read(*specs: _U, char=False) -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_T],\
    \ char=False):\n    IO.stdin.char = char\n    if not specs: return IO.stdin.readnumsinto([])\n\
    \    parser: _T = Parser.compile(specs[0] if len(specs) == 1 else specs)\n   \
    \ return parser(IO.stdin)\nfrom os import read as os_read, write as os_write,\
    \ fstat as os_fstat\nimport sys\nfrom __pypy__.builders import StringBuilder\n\
    \n\ndef max2(a, b): return a if a > b else b\n\nclass IOBase:\n    @property\n\
    \    def char(io) -> bool: ...\n    @property\n    def writable(io) -> bool: ...\n\
    \    def __next__(io) -> str: ...\n    def write(io, s: str) -> None: ...\n  \
    \  def readline(io) -> str: ...\n    def readtoken(io) -> str: ...\n    def readtokens(io)\
    \ -> list[str]: ...\n    def readints(io) -> list[int]: ...\n    def readdigits(io)\
    \ -> list[int]: ...\n    def readnums(io) -> list[int]: ...\n    def readchar(io)\
    \ -> str: ...\n    def readchars(io) -> str: ...\n    def readinto(io, lst: list[str])\
    \ -> list[str]: ...\n    def readcharsinto(io, lst: list[str]) -> list[str]: ...\n\
    \    def readtokensinto(io, lst: list[str]) -> list[str]: ...\n    def readintsinto(io,\
    \ lst: list[int]) -> list[int]: ...\n    def readdigitsinto(io, lst: list[int])\
    \ -> list[int]: ...\n    def readnumsinto(io, lst: list[int]) -> list[int]: ...\n\
    \    def wait(io): ...\n    def flush(io) -> None: ...\n    def line(io) -> list[str]:\
    \ ...\n\nclass IO(IOBase):\n    BUFSIZE = 1 << 16; stdin: 'IO'; stdout: 'IO'\n\
    \    __slots__ = 'f', 'file', 'B', 'O', 'V', 'S', 'l', 'p', 'char', 'sz', 'st',\
    \ 'ist', 'writable', 'encoding', 'errors'\n    def __init__(io, file):\n     \
    \   io.file = file\n        try: io.f = file.fileno(); io.sz, io.writable = max2(io.BUFSIZE,\
    \ os_fstat(io.f).st_size), ('x' in file.mode or 'r' not in file.mode)\n      \
    \  except: io.f, io.sz, io.writable = -1, io.BUFSIZE, False\n        io.B, io.O,\
    \ io.S = bytearray(), [], StringBuilder(); io.V = memoryview(io.B); io.l = io.p\
    \ = 0\n        io.char, io.st, io.ist, io.encoding, io.errors = False, [], [],\
    \ 'ascii', 'ignore'\n    def _dec(io, l, r): return io.V[l:r].tobytes().decode(io.encoding,\
    \ io.errors)\n    def readbytes(io, sz): return os_read(io.f, sz)\n    def load(io):\n\
    \        while io.l >= len(io.O):\n            if not (b := io.readbytes(io.sz)):\n\
    \                if io.O[-1] < len(io.B): io.O.append(len(io.B))\n           \
    \     break\n            pos = len(io.B); io.B.extend(b)\n            while ~(pos\
    \ := io.B.find(b'\\n', pos)): io.O.append(pos := pos+1)\n    def __next__(io):\n\
    \        if io.char: return io.readchar()\n        else: return io.readtoken()\n\
    \    def readchar(io):\n        io.load(); r = io.O[io.l]\n        c = chr(io.B[io.p])\n\
    \        if io.p >= r-1: io.p = r; io.l += 1\n        else: io.p += 1\n      \
    \  return c\n    def write(io, s: str): io.S.append(s)\n    def readline(io):\
    \ io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return io._dec(l, io.p)\n\
    \    def readtoken(io):\n        io.load(); r = io.O[io.l]\n        if ~(p :=\
    \ io.B.find(b' ', io.p, r)): s = io._dec(io.p, p); io.p = p+1\n        else: s\
    \ = io._dec(io.p, r-1); io.p = r; io.l += 1\n        return s\n    def readtokens(io):\
    \ io.st.clear(); return io.readtokensinto(io.st)\n    def readints(io): io.ist.clear();\
    \ return io.readintsinto(io.ist)\n    def readdigits(io): io.ist.clear(); return\
    \ io.readdigitsinto(io.ist)\n    def readnums(io): io.ist.clear(); return io.readnumsinto(io.ist)\n\
    \    def readchars(io): io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return\
    \ io._dec(l, io.p-1)\n    def readinto(io, lst):\n        if io.char: return io.readcharsinto(lst)\n\
    \        else: return io.readtokensinto(lst)\n    def readcharsinto(io, lst):\
    \ lst.extend(io.readchars()); return lst\n    def readtokensinto(io, lst): \n\
    \        io.load(); r = io.O[io.l]\n        while ~(p := io.B.find(b' ', io.p,\
    \ r)): lst.append(io._dec(io.p, p)); io.p = p+1\n        lst.append(io._dec(io.p,\
    \ r-1)); io.p = r; io.l += 1; return lst\n    def readintsinto(io, lst):\n   \
    \     io.load(); r = io.O[io.l]\n        while io.p < r:\n            while io.p\
    \ < r and io.B[io.p] <= 32: io.p += 1\n            if io.p >= r: break\n     \
    \       minus = x = 0\n            if io.B[io.p] == 45: minus = 1; io.p += 1\n\
    \            while io.p < r and io.B[io.p] >= 48:\n                x = x * 10\
    \ + (io.B[io.p] & 15); io.p += 1\n            lst.append(-x if minus else x)\n\
    \            if io.p < r and io.B[io.p] == 32: io.p += 1\n        io.l += 1; return\
    \ lst\n    def readdigitsinto(io, lst):\n        io.load(); r = io.O[io.l]\n \
    \       while io.p < r and io.B[io.p] > 32:\n            if io.B[io.p] >= 48 and\
    \ io.B[io.p] <= 57:\n                lst.append(io.B[io.p] & 15)\n           \
    \ io.p += 1\n        if io.p < r and io.B[io.p] == 10: io.p = r; io.l += 1\n \
    \       return lst\n    def readnumsinto(io, lst):\n        if io.char: return\
    \ io.readdigitsinto(lst)\n        else: return io.readintsinto(lst)\n    def line(io):\
    \ io.st.clear(); return io.readinto(io.st)\n    def wait(io):\n        io.load();\
    \ r = io.O[io.l]\n        while io.p < r: yield\n    def flush(io):\n        if\
    \ io.writable: os_write(io.f, io.S.build().encode(io.encoding, io.errors)); io.S\
    \ = StringBuilder()\nsys.stdin = IO.stdin = IO(sys.stdin); sys.stdout = IO.stdout\
    \ = IO(sys.stdout)\nimport typing\nfrom numbers import Number\nfrom types import\
    \ GenericAlias \nfrom typing import Callable, Collection\n\nclass Parsable:\n\
    \    @classmethod\n    def compile(cls):\n        def parser(io: 'IOBase'): return\
    \ cls(next(io))\n        return parser\n    @classmethod\n    def __class_getitem__(cls,\
    \ item): return GenericAlias(cls, item)\n\nclass Parser:\n    def __init__(self,\
    \ spec):  self.parse = Parser.compile(spec)\n    def __call__(self, io: IOBase):\
    \ return self.parse(io)\n    @staticmethod\n    def compile_type(cls, args = ()):\n\
    \        if issubclass(cls, Parsable): return cls.compile(*args)\n        elif\
    \ issubclass(cls, (Number, str)):\n            def parse(io: IOBase): return cls(next(io))\
    \              \n            return parse\n        elif issubclass(cls, tuple):\
    \ return Parser.compile_tuple(cls, args)\n        elif issubclass(cls, Collection):\
    \ return Parser.compile_collection(cls, args)\n        elif callable(cls):\n \
    \           def parse(io: IOBase): return cls(next(io))              \n      \
    \      return parse\n        else: raise NotImplementedError()\n    @staticmethod\n\
    \    def compile(spec=int):\n        if isinstance(spec, (type, GenericAlias)):\n\
    \            cls, args = typing.get_origin(spec) or spec, typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(io: IOBase): return cls(next(io)) + offset\n            return\
    \ parse\n        elif isinstance(args := spec, tuple): return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection): return Parser.compile_collection(type(spec),\
    \ args)\n        elif isinstance(fn := spec, Callable): \n            def parse(io:\
    \ IOBase): return fn(next(io))\n            return parse\n        else: raise\
    \ NotImplementedError()\n    @staticmethod\n    def compile_line(cls, spec=int):\n\
    \        if spec is int:\n            def parse(io: IOBase): return cls(io.readnums())\n\
    \        else:\n            fn = Parser.compile(spec)\n            def parse(io:\
    \ IOBase): return cls([fn(io) for _ in io.wait()])\n        return parse\n   \
    \ @staticmethod\n    def compile_repeat(cls, spec, N):\n        fn = Parser.compile(spec)\n\
    \        def parse(io: IOBase): return cls([fn(io) for _ in range(N)])\n     \
    \   return parse\n    @staticmethod\n    def compile_children(cls, specs):\n \
    \       fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(io:\
    \ IOBase): return cls([fn(io) for fn in fns])  \n        return parse\n    @staticmethod\n\
    \    def compile_tuple(cls, specs):\n        if isinstance(specs, (tuple,list))\
    \ and len(specs) == 2 and specs[1] is ...: return Parser.compile_line(cls, specs[0])\n\
    \        else: return Parser.compile_children(cls, specs)\n    @staticmethod\n\
    \    def compile_collection(cls, specs):\n        if not specs or len(specs) ==\
    \ 1 or isinstance(specs, set):\n            return Parser.compile_line(cls, *specs)\n\
    \        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and isinstance(specs[1],\
    \ int)):\n            return Parser.compile_repeat(cls, specs[0], specs[1])\n\
    \        else:\n            raise NotImplementedError()\n\ndef write(*args, **kwargs):\n\
    \    '''Prints the values to a stream, or to stdout_fast by default.'''\n    sep,\
    \ file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IO.stdout)\n    at_start\
    \ = True\n    for x in args:\n        if not at_start:\n            file.write(sep)\n\
    \        file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    \nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/stirling_number_of_the_first_kind_fixed_k\n\
    \ndef main():\n    mint.set_mod(998244353)\n    N, K = read()\n    mcomb.precomp(N)\n\
    \    write(*stirling1_k(N, K))\n\nfrom cp_library.math.table.mcomb_cls import\
    \ mcomb\nfrom cp_library.math.table.stirling1_k_fn import stirling1_k\nfrom cp_library.math.mod.mint_ntt_cls\
    \ import mint\nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn\
    \ import write\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/math/table/mcomb_cls.py
  - cp_library/math/table/stirling1_k_fn.py
  - cp_library/math/mod/mint_ntt_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/math/fps/fps_pow_fn.py
  - cp_library/io/io_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/math/fps/fps_log_fn.py
  - cp_library/math/fps/fps_exp_fn.py
  - cp_library/math/fps/fps_normalize_fn.py
  - cp_library/math/nt/mod_inv_fn.py
  - cp_library/io/io_base_cls.py
  - cp_library/io/parsable_cls.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/math/fps/fps_deriv_fn.py
  - cp_library/math/fps/fps_integ_fn.py
  - cp_library/math/fps/fps_inv_fn.py
  - cp_library/ds/list/reserve_fn.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/nt/ntt_cls.py
  isVerificationFile: true
  path: test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
  requiredBy: []
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
layout: document
redirect_from:
- /verify/test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
- /verify/test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py.html
title: test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
---
