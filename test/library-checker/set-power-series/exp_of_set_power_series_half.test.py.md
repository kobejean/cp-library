---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnts_fn.py
    title: cp_library/bit/popcnts_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view_cls.py
    title: cp_library/ds/view/view_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast/fast_io_fn.py
    title: cp_library/io/fast/fast_io_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_mobius_fn.py
    title: cp_library/math/conv/ior_mobius_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_mobius_ranked_fn.py
    title: cp_library/math/conv/ior_mobius_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_zeta_fn.py
    title: cp_library/math/conv/ior_zeta_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_zeta_pair_ranked_fn.py
    title: cp_library/math/conv/ior_zeta_pair_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/isubset_conv_half_fn.py
    title: cp_library/math/conv/mod/isubset_conv_half_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/isubset_deconv_ranked_fn.py
    title: cp_library/math/conv/mod/isubset_deconv_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/subset_deconv_fn.py
    title: cp_library/math/conv/mod/subset_deconv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/sps/mod/sps_exp_half_fn.py
    title: cp_library/math/sps/mod/sps_exp_half_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/sps/mod/sps_ln_fn.py
    title: cp_library/math/sps/mod/sps_ln_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/exp_of_set_power_series
    links:
    - https://judge.yosupo.jp/problem/exp_of_set_power_series
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/exp_of_set_power_series\n\
    \ndef main():\n    N = rd()\n    B = rdl(1<<N)\n    C = sps_exp_half(B, 998244353)\n\
    \    wtnl(C)\n    # assert sps_ln(C, 998244353) == B\n\n# from cp_library.math.sps.mod.sps_exp_fn\
    \ import sps_exp\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\n\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import\
    \ newlist_hint\nexcept:\n    def newlist_hint(hint):\n        return []\nelist\
    \ = newlist_hint\n    \n\nfrom typing import Generic\nfrom typing import TypeVar\n\
    _S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1');\
    \ _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5');\
    \ _T6 = TypeVar('T6')\n\nimport sys\n\ndef list_find(lst: list, value, start =\
    \ 0, stop = sys.maxsize):\n    try:\n        return lst.index(value, start, stop)\n\
    \    except:\n        return -1\n\n\nclass view(Generic[_T]):\n    __slots__ =\
    \ 'A', 'l', 'r'\n    def __init__(V, A: list[_T], l: int = 0, r: int = 0): V.A,\
    \ V.l, V.r = A, l, r\n    def __len__(V): return V.r - V.l\n    def __getitem__(V,\
    \ i: int): \n        if 0 <= i < V.r - V.l: return V.A[V.l+i]\n        else: raise\
    \ IndexError\n    def __setitem__(V, i: int, v: _T): V.A[V.l+i] = v\n    def __contains__(V,\
    \ v: _T): return list_find(V.A, v, V.l, V.r) != -1\n    def set_range(V, l: int,\
    \ r: int): V.l, V.r = l, r\n    def index(V, v: _T): return V.A.index(v, V.l,\
    \ V.r) - V.l\n    def reverse(V):\n        l, r = V.l, V.r-1\n        while l\
    \ < r: V.A[l], V.A[r] = V.A[r], V.A[l]; l += 1; r -= 1\n    def sort(V, /, *args,\
    \ **kwargs):\n        A = V.A[V.l:V.r]; A.sort(*args, **kwargs)\n        for i,a\
    \ in enumerate(A,V.l): V.A[i] = a\n    def pop(V): V.r -= 1; return V.A[V.r]\n\
    \    def append(V, v: _T): V.A[V.r] = v; V.r += 1\n    def popleft(V): V.l +=\
    \ 1; return V.A[V.l-1]\n    def appendleft(V, v: _T): V.l -= 1; V.A[V.l] = v;\
    \ \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\n\n\ndef popcnts(N):\n\
    \    P = [0]*(1 << N)\n    for i in range(N):\n        for m in range(b := 1<<i):\n\
    \            P[m^b] = P[m] + 1\n    return P\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n    x\u2080 \u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2080\n                \u2573   \
    \       \u2572 \u2571          \u2572     \u2571          \n    x\u2084 \u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2572\u2500\u2500\u2500\u2571\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2081\n       \
    \                    \u2573 \u2573          \u2572 \u2572 \u2571 \u2571      \
    \    \n    x\u2082 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2572\u2500\
    \u2573\u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25BA X\u2082\n                \u2573          \u2571 \u2572          \u2572\
    \ \u2573 \u2573 \u2571          \n    x\u2086 \u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2573\u2500\u2573\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25BA X\u2083\n                                     \
    \   \u2573 \u2573 \u2573 \u2573         \n    x\u2081 \u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2573\u2500\u2573\u2500\u2573\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2084\n                \u2573   \
    \       \u2572 \u2571          \u2571 \u2573 \u2573 \u2572          \n    x\u2085\
    \ \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2571\u2500\u2573\u2500\u2572\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2085\n \
    \                          \u2573 \u2573          \u2571 \u2571 \u2572 \u2572\
    \          \n    x\u2083 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2571\
    \u2500\u2500\u2500\u2572\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25BA X\u2086\n                \u2573          \u2571 \u2572          \u2571\
    \     \u2572          \n    x\u2087 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X\u2087\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n                      Math - Convolution           \
    \          \n'''\n\n\ndef ior_zeta_pair_ranked(A, B, N, M, Z):\n    for i in range(0,\
    \ Z, M):\n        l, r = i+(1<<(i>>N))-1, i+M\n        for j in range(N):\n  \
    \          m = l|(b := 1<<j)\n            while m < r: A[m] += A[m^b]; B[m] +=\
    \ B[m^b]; m = m+1|b\n    return A, B\n\ndef ior_mobius_ranked(A: list[int], N:\
    \ int, M: int, Z: int):\n    for i in range(0, Z, M):\n        l, r = i, i+M-(1<<(N-(i>>N)))+1\n\
    \        for j in range(N):\n            m = l|(b := 1<<j)\n            while\
    \ m < r: A[m] -= A[m^b]; m = m+1|b\n    return A\n\ndef isubset_deconv_ranked(Ar,\
    \ Br, N, Z, M, mod):\n    inv = pow(Br[0], -1, mod); ior_zeta_pair_ranked(Ar,\
    \ Br, N, M, Z)\n    for i in range(Z): Br[i], Ar[i] = Br[i]%mod, Ar[i]%mod\n \
    \   for i in range(0, Z, M):\n        for k in range(M): Ar[i|k] = Ar[i|k] * inv\
    \ % mod\n        for j in range(M, Z-i, M):\n            ij = i + j; l = (1 <<\
    \ (j>>N))-1\n            for k in range(l,M): Ar[ij|k] -= Ar[i|k] * Br[j|k] %\
    \ mod\n    return ior_mobius_ranked(Ar, N, M, Z)\n\ndef subset_deconv(A: list[int],\
    \ B: list[int], N: int, mod: int) -> list[int]:\n    Z = (N+1)*(M:=1<<N)\n   \
    \ Ar, Br, C, P = [0]*Z, [0]*Z, [0]*M, popcnts(N)\n    for i, p in enumerate(P):\
    \ Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]\n    isubset_deconv_ranked(Ar, Br, N, Z,\
    \ M, mod)\n    for i, p in enumerate(P): C[i] = Ar[p<<N|i] % mod\n    return C\n\
    \n\ndef sps_ln(P, mod):\n    assert P[0] == 1\n    N = len(P).bit_length()-1;\
    \ P0, P1 = view(P), view(P); m = 1; ln = elist(1 << N); ln.append(0)\n    for\
    \ n in range(N): P0.set_range(0, m); P1.set_range(m, m := m<<1); ln.extend(subset_deconv(P1,\
    \ P0, n, mod))\n    return ln\n\ndef ior_zeta(A: list[int], N: int, Z: int = None):\n\
    \    Z = Z if Z else len(A)\n    for i in range(N):\n        m = b = 1<<i\n  \
    \      while m < Z: A[m] += A[m^b]; m = m+1|b\n    return A\n\ndef isubset_conv_half(Ar:\
    \ list[int], B: list[int], n: int, N: int, mod: int, pcnt) -> list[int]:\n   \
    \ Br = [0]*(z := (n+1)*(m := 1<<n))\n    for i in range(m): Br[pcnt[i]<<n|i] =\
    \ B[i]\n    ior_zeta(Br, n)\n    for i in range(z): Br[i] = Br[i]%mod\n    for\
    \ ij in range(n,-1,-1):\n        ij_, i_ = (ij+1)<<N|m, ij<<n\n        for k in\
    \ range(m): Ar[ij_|k] = (Br[i_|k] * Ar[k]) % mod\n        for i in range(ij):\n\
    \            j = ij-i; i_, j_ = i<<n, j<<N\n            for k in range(m): Ar[ij_|k]\
    \ = (Ar[ij_|k] + Br[i_|k] * Ar[j_|k]) % mod\n    for i in range(n+1):\n      \
    \  i = i << N\n        for k in range(m): Ar[i|k|m] += Ar[i|k]\n\ndef ior_mobius(A:\
    \ list[int], N: int, Z: int = None):\n    Z = Z if Z else len(A)\n    for i in\
    \ range(N):\n        m = b = 1<<i\n        while m < Z: A[m] -= A[m^b]; m = m+1|b\n\
    \    return A\n\ndef sps_exp_half(P, mod):\n    assert P[0] == 0\n    N = len(P).bit_length()\
    \ - 1\n    Z = (N+1)*(M := 1<<N)\n    exp = [0]*Z; exp[0] = 1\n    pcnt = popcnts(N)\n\
    \    P = view(P); m = 1\n    for n in range(N):\n        P.set_range(m, m := m<<1)\n\
    \        isubset_conv_half(exp, P, n, N, mod, pcnt)\n    ior_mobius(exp, N)\n\
    \    return [exp[p<<N|i] % mod for i,p in enumerate(pcnt)]\n\n\nfrom __pypy__.builders\
    \ import StringBuilder\nfrom os import read as os_read, write as os_write\nfrom\
    \ atexit import register as atexist_register\n\nclass Fastio:\n    ibuf = bytes()\n\
    \    pil = pir = 0\n    sb = StringBuilder()\n    def load(self):\n        self.ibuf\
    \ = self.ibuf[self.pil:]\n        self.ibuf += os_read(0, 131072)\n        self.pil\
    \ = 0; self.pir = len(self.ibuf)\n    def flush_atexit(self): os_write(1, self.sb.build().encode())\n\
    \    def flush(self):\n        os_write(1, self.sb.build().encode())\n       \
    \ self.sb = StringBuilder()\n    def fastin(self):\n        if self.pir - self.pil\
    \ < 64: self.load()\n        minus = x = 0\n        while self.ibuf[self.pil]\
    \ < 45: self.pil += 1\n        if self.ibuf[self.pil] == 45: minus = 1; self.pil\
    \ += 1\n        while self.ibuf[self.pil] >= 48:\n            x = x * 10 + (self.ibuf[self.pil]\
    \ & 15)\n            self.pil += 1\n        if minus: return -x\n        return\
    \ x\n    def fastin_string(self):\n        if self.pir - self.pil < 64: self.load()\n\
    \        while self.ibuf[self.pil] <= 32: self.pil += 1\n        res = bytearray()\n\
    \        while self.ibuf[self.pil] > 32:\n            if self.pir - self.pil <\
    \ 64: self.load()\n            res.append(self.ibuf[self.pil])\n            self.pil\
    \ += 1\n        return res\n    def fastout(self, x): self.sb.append(str(x))\n\
    \    def fastoutln(self, x): self.sb.append(str(x)); self.sb.append('\\n')\nfastio\
    \ = Fastio()\nrd = fastio.fastin; rds = fastio.fastin_string; wt = fastio.fastout;\
    \ wtn = fastio.fastoutln; flush = fastio.flush\natexist_register(fastio.flush_atexit)\n\
    sys.stdin = None; sys.stdout = None\ndef rdl(n):\n    lst = [0]*n\n    for i in\
    \ range(n): lst[i] = rd()\n    return lst\ndef wtnl(l): wtn(' '.join(map(str,\
    \ l)))\n# from cp_library.io.write_fn import write\n# from cp_library.io.read_fn\
    \ import read\n\nmain()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/exp_of_set_power_series\n\
    \ndef main():\n    N = rd()\n    B = rdl(1<<N)\n    C = sps_exp_half(B, 998244353)\n\
    \    wtnl(C)\n    # assert sps_ln(C, 998244353) == B\n\n# from cp_library.math.sps.mod.sps_exp_fn\
    \ import sps_exp\nfrom cp_library.math.sps.mod.sps_ln_fn import sps_ln\nfrom cp_library.math.sps.mod.sps_exp_half_fn\
    \ import sps_exp_half\nfrom cp_library.io.fast.fast_io_fn import rd, rdl, wtnl\n\
    # from cp_library.io.write_fn import write\n# from cp_library.io.read_fn import\
    \ read\n\nmain()"
  dependsOn:
  - cp_library/math/sps/mod/sps_ln_fn.py
  - cp_library/math/sps/mod/sps_exp_half_fn.py
  - cp_library/io/fast/fast_io_fn.py
  - cp_library/ds/elist_fn.py
  - cp_library/ds/view/view_cls.py
  - cp_library/math/conv/mod/subset_deconv_fn.py
  - cp_library/bit/popcnts_fn.py
  - cp_library/math/conv/mod/isubset_conv_half_fn.py
  - cp_library/math/conv/ior_mobius_fn.py
  - cp_library/math/conv/mod/isubset_deconv_ranked_fn.py
  - cp_library/math/conv/ior_zeta_fn.py
  - cp_library/math/conv/ior_zeta_pair_ranked_fn.py
  - cp_library/math/conv/ior_mobius_ranked_fn.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: true
  path: test/library-checker/set-power-series/exp_of_set_power_series_half.test.py
  requiredBy: []
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/set-power-series/exp_of_set_power_series_half.test.py
layout: document
redirect_from:
- /verify/test/library-checker/set-power-series/exp_of_set_power_series_half.test.py
- /verify/test/library-checker/set-power-series/exp_of_set_power_series_half.test.py.html
title: test/library-checker/set-power-series/exp_of_set_power_series_half.test.py
---
