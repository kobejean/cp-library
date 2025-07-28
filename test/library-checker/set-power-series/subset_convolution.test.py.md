---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnts_fn.py
    title: cp_library/bit/popcnts_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/elist_fn.py
    title: cp_library/ds/list/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_fn.py
    title: cp_library/io/fast_io_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_cls.py
    title: cp_library/io/io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_mobius_ranked_fn.py
    title: cp_library/math/conv/ior_mobius_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_zeta_pair_ranked_fn.py
    title: cp_library/math/conv/ior_zeta_pair_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/isubset_conv_ranked_fn.py
    title: cp_library/math/conv/mod/isubset_conv_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/isubset_deconv_ranked_fn.py
    title: cp_library/math/conv/mod/isubset_deconv_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/subset_conv_fn.py
    title: cp_library/math/conv/mod/subset_conv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/subset_deconv_fn.py
    title: cp_library/math/conv/mod/subset_deconv_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/subset_convolution
    links:
    - https://judge.yosupo.jp/problem/subset_convolution
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution\n\
    \ndef main():\n    mod, n = 998244353, rd()[0]\n    A, B = rdl(1<<n), rdl(1<<n)\n\
    \    C = subset_conv(A, B, n, mod)\n    wtnl(C)\n    assert subset_deconv(C, B,\
    \ n, mod) == A\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\n\n\ndef popcnts(N):\n    P = [0]*(1 << N)\n    for i in range(N):\n\
    \        for m in range(b := 1<<i):\n            P[m^b] = P[m] + 1\n    return\
    \ P\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n    x\u2080 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25BA X\u2080\n                \u2573          \u2572 \u2571          \u2572\
    \     \u2571          \n    x\u2084 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2572\u2500\u2500\u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X\u2081\n                           \u2573 \u2573   \
    \       \u2572 \u2572 \u2571 \u2571          \n    x\u2082 \u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2572\u2500\u2573\u2500\u2571\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2082\n                \u2573   \
    \       \u2571 \u2572          \u2572 \u2573 \u2573 \u2571          \n    x\u2086\
    \ \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u2573\u2500\u2573\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2083\n \
    \                                       \u2573 \u2573 \u2573 \u2573         \n\
    \    x\u2081 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u2573\
    \u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA\
    \ X\u2084\n                \u2573          \u2572 \u2571          \u2571 \u2573\
    \ \u2573 \u2572          \n    x\u2085 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2571\u2500\u2573\u2500\u2572\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X\u2085\n                           \u2573 \u2573   \
    \       \u2571 \u2571 \u2572 \u2572          \n    x\u2083 \u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2571\u2500\u2500\u2500\u2572\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2086\n                \u2573   \
    \       \u2571 \u2572          \u2571     \u2572          \n    x\u2087 \u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2087\n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n               \
    \       Math - Convolution                     \n'''\n\n\ndef max2(a, b): return\
    \ a if a > b else b\n\n\ndef ior_zeta_pair_ranked(A, B, N, M, Z):\n    for i in\
    \ range(0, Z, M):\n        l, r = i+(1<<(i>>N))-1, i+M\n        for j in range(N):\n\
    \            m = l|(b := 1<<j)\n            while m < r: A[m] += A[m^b]; B[m]\
    \ += B[m^b]; m = m+1|b\n    return A, B\n\ndef ior_mobius_ranked(A: list[int],\
    \ N: int, M: int, Z: int):\n    for i in range(0, Z, M):\n        l, r = i, i+M-(1<<(N-(i>>N)))+1\n\
    \        for j in range(N):\n            m = l|(b := 1<<j)\n            while\
    \ m < r: A[m] -= A[m^b]; m = m+1|b\n    return A\n\ndef isubset_conv_ranked(Ar,\
    \ Br, N, M, Z, mod) -> list[int]:\n    ior_zeta_pair_ranked(Ar, Br, N, M, Z)\n\
    \    for i in range(Z): Ar[i], Br[i] = Ar[i]%mod, Br[i]%mod\n    for ij in range(Z-M,-1,-M):\n\
    \        for k in range(M): Ar[ij|k] = (Ar[ij|k] * Br[k]) % mod\n        r = M-(1\
    \ << (N-(ij>>N)))+1\n        for i in range(0,ij,M):\n            j = ij-i; l\
    \ = (1 << (max2(i,j)>>N))-1\n            for k in range(l,r): Ar[ij|k] += Ar[i|k]\
    \ * Br[j|k] % mod\n    return ior_mobius_ranked(Ar, N, M, Z)\n\ndef subset_conv(A:\
    \ list[int], B: list[int], N: int, mod: int) -> list[int]:\n    Z = (N+1)*(M:=1<<N)\n\
    \    Ar, Br, C, P = [0]*Z, [0]*Z, [0]*M, popcnts(N)\n    for i, p in enumerate(P):\
    \ Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]\n    isubset_conv_ranked(Ar, Br, N, M, Z,\
    \ mod)\n    for i, p in enumerate(P): C[i] = Ar[p<<N|i] % mod\n    return C\n\n\
    def isubset_deconv_ranked(Ar, Br, N, Z, M, mod):\n    inv = pow(Br[0], -1, mod);\
    \ ior_zeta_pair_ranked(Ar, Br, N, M, Z)\n    for i in range(Z): Br[i], Ar[i] =\
    \ Br[i]%mod, Ar[i]%mod\n    for i in range(0, Z, M):\n        for k in range(M):\
    \ Ar[i|k] = Ar[i|k] * inv % mod\n        for j in range(M, Z-i, M):\n        \
    \    ij = i + j; l = (1 << (j>>N))-1\n            for k in range(l,M): Ar[ij|k]\
    \ -= Ar[i|k] * Br[j|k] % mod\n    return ior_mobius_ranked(Ar, N, M, Z)\n\ndef\
    \ subset_deconv(A: list[int], B: list[int], N: int, mod: int) -> list[int]:\n\
    \    Z = (N+1)*(M:=1<<N)\n    Ar, Br, C, P = [0]*Z, [0]*Z, [0]*M, popcnts(N)\n\
    \    for i, p in enumerate(P): Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]\n    isubset_deconv_ranked(Ar,\
    \ Br, N, Z, M, mod)\n    for i, p in enumerate(P): C[i] = Ar[p<<N|i] % mod\n \
    \   return C\n\nfrom os import read as os_read, write as os_write, fstat as os_fstat\n\
    import sys\nfrom __pypy__.builders import StringBuilder\n\nclass IOBase:\n   \
    \ @property\n    def char(io) -> bool: ...\n    @property\n    def writable(io)\
    \ -> bool: ...\n    def __next__(io) -> str: ...\n    def write(io, s: str) ->\
    \ None: ...\n    def readline(io) -> str: ...\n    def readtoken(io) -> str: ...\n\
    \    def readtokens(io) -> list[str]: ...\n    def readints(io) -> list[int]:\
    \ ...\n    def readdigits(io) -> list[int]: ...\n    def readnums(io) -> list[int]:\
    \ ...\n    def readchar(io) -> str: ...\n    def readchars(io) -> str: ...\n \
    \   def readinto(io, lst: list[str]) -> list[str]: ...\n    def readcharsinto(io,\
    \ lst: list[str]) -> list[str]: ...\n    def readtokensinto(io, lst: list[str])\
    \ -> list[str]: ...\n    def readintsinto(io, lst: list[int]) -> list[int]: ...\n\
    \    def readdigitsinto(io, lst: list[int]) -> list[int]: ...\n    def readnumsinto(io,\
    \ lst: list[int]) -> list[int]: ...\n    def wait(io): ...\n    def flush(io)\
    \ -> None: ...\n    def line(io) -> list[str]: ...\n\nclass IO(IOBase):\n    BUFSIZE\
    \ = 1 << 16; stdin: 'IO'; stdout: 'IO'\n    __slots__ = 'f', 'file', 'B', 'O',\
    \ 'V', 'S', 'l', 'p', 'char', 'sz', 'st', 'ist', 'writable', 'encoding', 'errors'\n\
    \    def __init__(io, file):\n        io.file = file\n        try: io.f = file.fileno();\
    \ io.sz, io.writable = max2(io.BUFSIZE, os_fstat(io.f).st_size), ('x' in file.mode\
    \ or 'r' not in file.mode)\n        except: io.f, io.sz, io.writable = -1, io.BUFSIZE,\
    \ False\n        io.B, io.O, io.S = bytearray(), [], StringBuilder(); io.V = memoryview(io.B);\
    \ io.l = io.p = 0\n        io.char, io.st, io.ist, io.encoding, io.errors = False,\
    \ [], [], 'ascii', 'ignore'\n    def _dec(io, l, r): return io.V[l:r].tobytes().decode(io.encoding,\
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
    \ r-1)); io.p = r; io.l += 1; return lst\n    def _readint(io, r):\n        while\
    \ io.p < r and io.B[io.p] <= 32: io.p += 1\n        if io.p >= r: return None\n\
    \        minus = x = 0\n        if io.B[io.p] == 45: minus = 1; io.p += 1\n  \
    \      while io.p < r and io.B[io.p] >= 48: x = x * 10 + (io.B[io.p] & 15); io.p\
    \ += 1\n        io.p += 1\n        return -x if minus else x\n    def readintsinto(io,\
    \ lst):\n        io.load(); r = io.O[io.l]\n        while io.p < r and (x := io._readint(r))\
    \ is not None: lst.append(x)\n        io.l += 1; return lst\n    def _readdigit(io):\
    \ d = io.B[io.p] & 15; io.p += 1; return d\n    def readdigitsinto(io, lst):\n\
    \        io.load(); r = io.O[io.l]\n        while io.p < r and io.B[io.p] > 32:\
    \ lst.append(io._readdigit())\n        if io.B[io.p] == 10: io.l += 1\n      \
    \  io.p += 1\n        return lst\n    def readnumsinto(io, lst):\n        if io.char:\
    \ return io.readdigitsinto(lst)\n        else: return io.readintsinto(lst)\n \
    \   def line(io): io.st.clear(); return io.readinto(io.st)\n    def wait(io):\n\
    \        io.load(); r = io.O[io.l]\n        while io.p < r: yield\n    def flush(io):\n\
    \        if io.writable: os_write(io.f, io.S.build().encode(io.encoding, io.errors));\
    \ io.S = StringBuilder()\nsys.stdin = IO.stdin = IO(sys.stdin); sys.stdout = IO.stdout\
    \ = IO(sys.stdout)\ndef rd(): return IO.stdin.readints()\ndef rds(): return IO.stdin.__next__()\n\
    def rdl(n): return IO.stdin.readintsinto(elist(n))\ndef wt(s): IO.stdout.write(s)\n\
    def wtn(s): IO.stdout.write(f'{s}\\n')\ndef wtnl(l): IO.stdout.write(' '.join(map(str,\
    \ l)))\n\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import\
    \ newlist_hint\nexcept:\n    def newlist_hint(hint):\n        return []\nelist\
    \ = newlist_hint\n    \n\nmain()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution\n\
    \ndef main():\n    mod, n = 998244353, rd()[0]\n    A, B = rdl(1<<n), rdl(1<<n)\n\
    \    C = subset_conv(A, B, n, mod)\n    wtnl(C)\n    assert subset_deconv(C, B,\
    \ n, mod) == A\n\nfrom cp_library.math.conv.mod.subset_conv_fn import subset_conv\n\
    from cp_library.math.conv.mod.subset_deconv_fn import subset_deconv\nfrom cp_library.io.fast_io_fn\
    \ import rd, rdl, wtnl\n\nmain()"
  dependsOn:
  - cp_library/math/conv/mod/subset_conv_fn.py
  - cp_library/math/conv/mod/subset_deconv_fn.py
  - cp_library/io/fast_io_fn.py
  - cp_library/bit/popcnts_fn.py
  - cp_library/math/conv/mod/isubset_conv_ranked_fn.py
  - cp_library/math/conv/mod/isubset_deconv_ranked_fn.py
  - cp_library/io/io_cls.py
  - cp_library/ds/list/elist_fn.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/math/conv/ior_zeta_pair_ranked_fn.py
  - cp_library/math/conv/ior_mobius_ranked_fn.py
  - cp_library/io/io_base_cls.py
  isVerificationFile: true
  path: test/library-checker/set-power-series/subset_convolution.test.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/set-power-series/subset_convolution.test.py
layout: document
redirect_from:
- /verify/test/library-checker/set-power-series/subset_convolution.test.py
- /verify/test/library-checker/set-power-series/subset_convolution.test.py.html
title: test/library-checker/set-power-series/subset_convolution.test.py
---
