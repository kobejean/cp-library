---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_func_fn.py
    title: cp_library/io/read_func_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mat_id_fn.py
    title: cp_library/math/mat_id_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mat_mul_fn.py
    title: cp_library/math/mat_mul_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mat_pow_fn.py
    title: cp_library/math/mat_pow_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mat_mul_fn.py
    title: cp_library/math/mod/mat_mul_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mat_pow_fn.py
    title: cp_library/math/mod/mat_pow_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/pow_of_matrix
    links:
    - https://judge.yosupo.jp/problem/pow_of_matrix
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \n\ndef main():\n    mod = 998244353\n    N, K = read()\n    if N < 10:\n    \
    \    '''\n        \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n                     https://kobejean.github.io/cp-library     \
    \          \n        '''\n        \n        def mat_pow(A,K):\n            N =\
    \ len(A)\n            ret = A if K & 1 else mat_id(N)\n            for i in range(1,K.bit_length()):\n\
    \                A = mat_mul(A,A) \n                if K >> i & 1:\n         \
    \           ret = mat_mul(ret,A) \n            return ret \n        \n       \
    \ '''\n        \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n                     https://kobejean.github.io/cp-library           \
    \    \n        '''\n        \n        def mat_mul(A,B):\n            assert len(A[0])\
    \ == len(B)\n            R = [[0]*len(B[0]) for _ in range(len(A))] \n       \
    \     for i,Ri in enumerate(R):\n                for k,Aik in enumerate(A[i]):\n\
    \                    for j,Bkj in enumerate(B[k]):\n                        Ri[j]\
    \ = Bkj*Aik + Ri[j]  \n            return R \n        '''\n        \u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n               \
    \      https://kobejean.github.io/cp-library               \n        '''\n   \
    \     \n        def mat_id(N):\n            return [[int(i==j) for j in range(N)]\
    \ for i in range(N)]\n        '''\n        \u257A\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2578\n                     https://kobejean.github.io/cp-library\
    \               \n        '''\n        \n        class mint(int):\n          \
    \  mod: int\n            zero: 'mint'\n            one: 'mint'\n            two:\
    \ 'mint'\n            cache: list['mint']\n        \n            def __new__(cls,\
    \ *args, **kwargs):\n                if (x := int(*args, **kwargs)) <= 2:\n  \
    \                  return cls.cache[x]\n                else:\n              \
    \      return cls.fix(x)\n        \n            @classmethod\n            def\
    \ set_mod(cls, mod):\n                cls.mod = mod\n                cls.zero\
    \ = cls.cast(0)\n                cls.one = cls.fix(1)\n                cls.two\
    \ = cls.fix(2)\n                cls.cache = [cls.zero, cls.one, cls.two]\n   \
    \     \n            @classmethod\n            def fix(cls, x): return cls.cast(x%cls.mod)\n\
    \        \n            @classmethod\n            def cast(cls, x): return super().__new__(cls,x)\n\
    \        \n            @classmethod\n            def mod_inv(cls, x):\n      \
    \          a,b,s,t = int(x), cls.mod, 1, 0\n                while b: a,b,s,t =\
    \ b,a%b,t,s-a//b*t\n                if a == 1: return cls.fix(s)\n           \
    \     raise ValueError(f\"{x} is not invertible in mod {cls.mod}\")\n        \
    \    \n            @property\n            def inv(self): return mint.mod_inv(self)\n\
    \        \n            def __add__(self, x): return mint.fix(super().__add__(x))\n\
    \            def __radd__(self, x): return mint.fix(super().__radd__(x))\n   \
    \         def __sub__(self, x): return mint.fix(super().__sub__(x))\n        \
    \    def __rsub__(self, x): return mint.fix(super().__rsub__(x))\n           \
    \ def __mul__(self, x): return mint.fix(super().__mul__(x))\n            def __rmul__(self,\
    \ x): return mint.fix(super().__rmul__(x))\n            def __floordiv__(self,\
    \ x): return self * mint.mod_inv(x)\n            def __rfloordiv__(self, x): return\
    \ self.inv * x\n            def __truediv__(self, x): return self * mint.mod_inv(x)\n\
    \            def __rtruediv__(self, x): return self.inv * x\n            def __pow__(self,\
    \ x): \n                return self.cast(super().__pow__(x, self.mod))\n     \
    \       def __neg__(self): return mint.mod-self\n            def __pos__(self):\
    \ return self\n            def __abs__(self): return self\n        \n        mint.set_mod(998244353)\n\
    \n        A = [read(mint) for _ in range(N)]\n        B = mat_pow(A, K)\n    else:\n\
    \        '''\n        \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n                     https://kobejean.github.io/cp-library     \
    \          \n        '''\n        \n        def mat_pow(A,K,mod):\n          \
    \  N = len(A)\n            ret = A if K & 1 else mat_id(N)\n            for i\
    \ in range(1,K.bit_length()):\n                A = mat_mul(A,A,mod) \n       \
    \         if K >> i & 1:\n                    ret = mat_mul(ret,A,mod) \n    \
    \        return ret \n        \n        '''\n        \u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n                     https://kobejean.github.io/cp-library\
    \               \n        '''\n        \n        def mat_mul(A,B,mod):\n     \
    \       assert len(A[0]) == len(B)\n            R = [[0]*len(B[0]) for _ in range(len(A))]\
    \ \n            for i,Ri in enumerate(R):\n                for k,Aik in enumerate(A[i]):\n\
    \                    for j,Bkj in enumerate(B[k]):\n                        Ri[j]\
    \ = (Ri[j] + Aik*Bkj) % mod\n            return R\n        '''\n        \u257A\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n         \
    \            https://kobejean.github.io/cp-library               \n        '''\n\
    \        \n        def mat_id(N):\n            return [[int(i==j) for j in range(N)]\
    \ for i in range(N)]\n\n        A = [read() for _ in range(N)]\n        B = mat_pow(A,\
    \ K, mod)\n\n    for row in B:\n        write(*row)\n\n'''\n\u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\ndef read(func=0, /):\n    if callable(func): return [func(s)\
    \ for s in input().split()]\n    return [int(s)+func for s in input().split()]\n\
    import os\nimport sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n\
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
    \ = IOWrapper(sys.stdout)\n\ndef write(*args, **kwargs):\n    \"\"\"Prints the\
    \ values to a stream, or to stdout_fast by default.\"\"\"\n    sep, file = kwargs.pop(\"\
    sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n    at_start = True\n \
    \   for x in args:\n        if not at_start:\n            file.write(sep)\n  \
    \      file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    \nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \n\ndef main():\n    mod = 998244353\n    N, K = read()\n    if N < 10:\n    \
    \    from cp_library.math.mat_pow_fn import mat_pow\n        from cp_library.math.mod.mint_cls\
    \ import mint\n        mint.set_mod(998244353)\n\n        A = [read(mint) for\
    \ _ in range(N)]\n        B = mat_pow(A, K)\n    else:\n        from cp_library.math.mod.mat_pow_fn\
    \ import mat_pow\n\n        A = [read() for _ in range(N)]\n        B = mat_pow(A,\
    \ K, mod)\n\n    for row in B:\n        write(*row)\n\nfrom cp_library.io.read_func_fn\
    \ import read\nfrom cp_library.io.write_fn import write\n\nif __name__ == '__main__':\n\
    \    main()"
  dependsOn:
  - cp_library/math/mat_pow_fn.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/mod/mat_pow_fn.py
  - cp_library/io/read_func_fn.py
  - cp_library/io/write_fn.py
  - cp_library/math/mat_mul_fn.py
  - cp_library/math/mat_id_fn.py
  - cp_library/math/mod/mat_mul_fn.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/pow_of_matrix_matpow.test.py
  requiredBy: []
  timestamp: '2024-12-17 23:55:08+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/pow_of_matrix_matpow.test.py
layout: document
redirect_from:
- /verify/test/pow_of_matrix_matpow.test.py
- /verify/test/pow_of_matrix_matpow.test.py.html
title: test/pow_of_matrix_matpow.test.py
---
