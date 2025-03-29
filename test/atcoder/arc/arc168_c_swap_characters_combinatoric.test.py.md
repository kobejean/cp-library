---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/nt/mod_inv_fn.py
    title: cp_library/math/nt/mod_inv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/modcomb_cls.py
    title: cp_library/math/table/modcomb_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/arc168/tasks/arc168_c
    links:
    - https://atcoder.jp/contests/arc168/tasks/arc168_c
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc168/tasks/arc168_c\n\
    def main():\n    N, K = read()\n    mint.set_mod(998244353)\n    modcomb.precomp(N)\n\
    \    multinom = modcomb.multinom\n    S = input()\n    A, B, C = S.count('A'),\
    \ S.count('B'), S.count('C')\n\n    # x A <-> B\n    # y B <-> C\n    # z C <->\
    \ A\n    # w A -> B -> C -> A or A -> C -> B -> A \n\n    ans = mint.zero\n  \
    \  for x in range(K+1):\n        for y in range(K-x+1):\n            for z in\
    \ range(K-x-y+1):\n                for w in range(((K-x-y-z)//2+1)):\n       \
    \             cnt = multinom(A,x,z+w) * \\\n                          multinom(B,y,x+w)\
    \ * \\\n                          multinom(C,z,y+w)\n                    if w\
    \ > 0: cnt*=2\n                    ans += cnt\n    write(ans)\n\n'''\n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n    \nclass mint(int):\n    mod: int\n    zero: 'mint'\n\
    \    one: 'mint'\n    two: 'mint'\n    cache: list['mint']\n\n    def __new__(cls,\
    \ *args, **kwargs):\n        if 0<= (x := int(*args, **kwargs)) <= 2:\n      \
    \      return cls.cache[x]\n        else:\n            return cls.fix(x)\n\n \
    \   @classmethod\n    def set_mod(cls, mod: int):\n        mint.mod = cls.mod\
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
    \ return self\n    def __abs__(self): return self\n\n\n\ndef mod_inv(x, mod):\n\
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
    \    def perm(n: int, k: int, /) -> mint:\n        '''Returns P(n,k) mod p'''\n\
    \        if n < k: return mint.zero\n        return mint(modcomb.fact[n] * modcomb.fact_inv[n-k])\n\
    \    nPk = perm\n    \n    @staticmethod\n    def catalan(n: int, /) -> mint:\n\
    \        return mint(modcomb.nCk(2*n,n) * modcomb.fact_inv[n+1])\n\n\ndef read(shift=0,\
    \ base=10):\n    return [int(s, base) + shift for s in input().split()]\nimport\
    \ os\nimport sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n\
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
    ascii\")\n\nsys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\nsys.stdout = IOWrapper.stdout\
    \ = IOWrapper(sys.stdout)\n\ndef write(*args, **kwargs):\n    '''Prints the values\
    \ to a stream, or to stdout_fast by default.'''\n    sep, file = kwargs.pop(\"\
    sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n    at_start = True\n \
    \   for x in args:\n        if not at_start:\n            file.write(sep)\n  \
    \      file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    \nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc168/tasks/arc168_c\n\
    def main():\n    N, K = read()\n    mint.set_mod(998244353)\n    modcomb.precomp(N)\n\
    \    multinom = modcomb.multinom\n    S = input()\n    A, B, C = S.count('A'),\
    \ S.count('B'), S.count('C')\n\n    # x A <-> B\n    # y B <-> C\n    # z C <->\
    \ A\n    # w A -> B -> C -> A or A -> C -> B -> A \n\n    ans = mint.zero\n  \
    \  for x in range(K+1):\n        for y in range(K-x+1):\n            for z in\
    \ range(K-x-y+1):\n                for w in range(((K-x-y-z)//2+1)):\n       \
    \             cnt = multinom(A,x,z+w) * \\\n                          multinom(B,y,x+w)\
    \ * \\\n                          multinom(C,z,y+w)\n                    if w\
    \ > 0: cnt*=2\n                    ans += cnt\n    write(ans)\n\nfrom cp_library.math.mod.mint_cls\
    \ import mint\nfrom cp_library.math.table.modcomb_cls import modcomb\nfrom cp_library.io.read_int_fn\
    \ import read\nfrom cp_library.io.write_fn import write\n\nif __name__ == '__main__':\n\
    \    main()"
  dependsOn:
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/table/modcomb_cls.py
  - cp_library/io/read_int_fn.py
  - cp_library/io/write_fn.py
  - cp_library/math/nt/mod_inv_fn.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/atcoder/arc/arc168_c_swap_characters_combinatoric.test.py
  requiredBy: []
  timestamp: '2025-03-29 18:58:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/arc/arc168_c_swap_characters_combinatoric.test.py
layout: document
redirect_from:
- /verify/test/atcoder/arc/arc168_c_swap_characters_combinatoric.test.py
- /verify/test/atcoder/arc/arc168_c_swap_characters_combinatoric.test.py.html
title: test/atcoder/arc/arc168_c_swap_characters_combinatoric.test.py
---
