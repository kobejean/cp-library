---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/nt/mod_inv_fn.py
    title: cp_library/math/nt/mod_inv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/nt/ntt_cls.py
    title: cp_library/math/nt/ntt_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/convolution/convolution_int.test.py
    title: test/library-checker/convolution/convolution_int.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/convolution/convolution_mod_1000000007.test.py
    title: test/library-checker/convolution/convolution_mod_1000000007.test.py
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
    from typing import Union\n\n\n\ndef mod_inv(x, mod):\n    a,b,s,t = x, mod, 1,\
    \ 0\n    while b:\n        a,b,s,t = b,a%b,t,s-a//b*t\n    if a == 1: return s\
    \ % mod\n    raise ValueError(f\"{x} is not invertible in mod {mod}\")\n\nclass\
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
    \        return res\n\ndef conv_int(A: list[int], B: list[int], N: Union[int,\
    \ None] = None) -> list[int]:\n    n,m = len(A),len(B)\n    N = n+m-1 if N is\
    \ None else N\n    m1, m2, m3 = 754974721, 167772161, 469762049\n    m2m3, m1m3,\
    \ m1m2, m1m2m3 = m2*m3, m1*m3, m1*m2, m1*m2*m3\n    i1, i2, i3 = mod_inv(m2m3,\
    \ m1), mod_inv(m1m3, m2), mod_inv(m1m2, m3)\n    ntt1, ntt2, ntt3 = NTT(m1), NTT(m2),\
    \ NTT(m3)\n    C,C1,C2,C3 = [0]*N, ntt1.conv(A, B), ntt2.conv(A, B), ntt3.conv(A,\
    \ B)\n    for i in range(N):\n        C[i] = (C1[i]*i1%m1*m2m3+C2[i]*i2%m2*m1m3+C3[i]*i3%m3*m1m2)%m1m2m3\n\
    \    return C\n"
  code: "import cp_library.math.__header__\nfrom typing import Union\nfrom cp_library.math.nt.ntt_cls\
    \ import NTT\nfrom cp_library.math.nt.mod_inv_fn import mod_inv\n\ndef conv_int(A:\
    \ list[int], B: list[int], N: Union[int, None] = None) -> list[int]:\n    n,m\
    \ = len(A),len(B)\n    N = n+m-1 if N is None else N\n    m1, m2, m3 = 754974721,\
    \ 167772161, 469762049\n    m2m3, m1m3, m1m2, m1m2m3 = m2*m3, m1*m3, m1*m2, m1*m2*m3\n\
    \    i1, i2, i3 = mod_inv(m2m3, m1), mod_inv(m1m3, m2), mod_inv(m1m2, m3)\n  \
    \  ntt1, ntt2, ntt3 = NTT(m1), NTT(m2), NTT(m3)\n    C,C1,C2,C3 = [0]*N, ntt1.conv(A,\
    \ B), ntt2.conv(A, B), ntt3.conv(A, B)\n    for i in range(N):\n        C[i] =\
    \ (C1[i]*i1%m1*m2m3+C2[i]*i2%m2*m1m3+C3[i]*i3%m3*m1m2)%m1m2m3\n    return C"
  dependsOn:
  - cp_library/math/nt/ntt_cls.py
  - cp_library/math/nt/mod_inv_fn.py
  isVerificationFile: false
  path: cp_library/math/conv/conv_int_fn.py
  requiredBy: []
  timestamp: '2024-12-30 17:25:46+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/convolution/convolution_mod_1000000007.test.py
  - test/library-checker/convolution/convolution_int.test.py
documentation_of: cp_library/math/conv/conv_int_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/conv_int_fn.py
- /library/cp_library/math/conv/conv_int_fn.py.html
title: cp_library/math/conv/conv_int_fn.py
---
