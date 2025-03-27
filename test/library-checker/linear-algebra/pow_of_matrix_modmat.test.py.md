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
    path: cp_library/math/linalg/mat/mod/modmat_cls.py
    title: cp_library/math/linalg/mat/mod/modmat_cls.py
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
    \ndef main():\n    mint.set_mod(998244353)\n    N, K = read()\n    A = ModMat([read()\
    \ for _ in range(N)])\n    B = A**K\n    write(B)\n\n'''\n\u257A\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
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
    \ return self\n    def __abs__(self): return self\nfrom typing import Union, List,\
    \ Tuple\n\nclass ModMat:\n    __slots__ = 'data', 'R', 'C'\n\n    def __init__(self,\
    \ data: List[Union[int,mint]]):\n        self.data, self.R, self.C = data, len(data),\
    \ len(data[0])\n    \n    @classmethod\n    def identity(cls, N) -> 'ModMat':\
    \ return ModMat([[int(i==j) for j in range(N)] for i in range(N)])\n    \n   \
    \ @classmethod\n    def zeros(cls, R, C) -> 'ModMat': return ModMat([[0]*C for\
    \ _ in range(R)])\n\n    def inv(self) -> 'ModMat':\n        assert self.R !=\
    \ self.C\n        \n        N = self.R\n        A = [row[:] for row in self.data]\n\
    \        I = [[int(i==j) for j in range(N)] for i in range(N)]\n        \n   \
    \     for i in range(N):\n            if A[i][i] == 0:\n                for j\
    \ in range(i+1, N):\n                    if A[j][i] != 0:\n                  \
    \      A[i], A[j] = A[j], A[i]\n                        I[i], I[j] = I[j], I[i]\n\
    \                        break\n                else:\n                    raise\
    \ ValueError(\"Matrix is not invertible\")\n            \n            inv = pow(A[i][i],\
    \ -1, mint.mod)\n            for j in range(N):\n                A[i][j] = (A[i][j]\
    \ * inv) % mint.mod\n                I[i][j] = (I[i][j] * inv) % mint.mod\n  \
    \          \n            for j in range(N):\n                if i != j:\n    \
    \                factor = A[j][i]\n                    for k in range(N):\n  \
    \                      A[j][k] = (A[j][k] - factor * A[i][k]) % mint.mod\n   \
    \                     I[j][k] = (I[j][k] - factor * I[i][k]) % mint.mod\n    \
    \    \n        return ModMat(I)\n    \n    def T(self) -> 'ModMat': return ModMat(list(map(list,zip(*self.data))))\n\
    \n    def elem_wise(self, func, other):\n        if isinstance(other, ModMat):\n\
    \            return ModMat([[func(a,b) for a,b in zip(Ai,Bi)] for Ai,Bi in zip(self.data,other.data)])\n\
    \        elif isinstance(other, int):\n            return ModMat([[func(a,other)\
    \ for a in Ai] for Ai in self.data])\n        else:\n            return NotImplemented\n\
    \        \n    def __str__(self): return '\\n'.join(' '.join(map(str,row)) for\
    \ row in self.data)\n    def __iter__(self): return self.data\n    def __copy__(self):\
    \ return ModMat([row[:] for row in self.data])\n    def copy(self): return ModMat([row[:]\
    \ for row in self.data])\n    def __add__(self, other): return self.elem_wise(lambda\
    \ a,b: (a+b) % mint.mod, other)\n    def __radd__(self, other): return self.__add__(other)\n\
    \    def __sub__(self, other): return self.elem_wise(lambda a,b: (a-b) % mint.mod,\
    \ other)\n    def __rsub__(self, other): return self.__sub__(other)\n    def __mul__(self,\
    \ other): return self.elem_wise(lambda a,b: (a*b) % mint.mod, other)\n    def\
    \ __rmul__(self, other): return self.__mul__(other)\n    def __truediv__(self,\
    \ other): return self.elem_wise(lambda a,b: a*pow(b,-1,mint.mod) % mint.mod, other)\n\
    \    def __rtruediv__(self, other): return self.elem_wise(lambda a,b: pow(a,-1,mint.mod)*b\
    \ % mint.mod, other)\n    \n    def __matmul__(self, other: 'ModMat'):\n     \
    \   assert self.C == other.R\n        R = [[0]*other.C for _ in range(self.R)]\n\
    \        for i,Ri in enumerate(R):\n            for k,Aik in enumerate(self.data[i]):\n\
    \                for j,Bkj in enumerate(other.data[k]):\n                    Ri[j]\
    \ = (Ri[j] + Aik*Bkj) % mint.mod\n        return ModMat(R)\n    \n    def __pow__(self,\
    \ K):\n        assert isinstance(K,int)\n        assert self.R == self.C\n   \
    \     A = self.copy()\n        R = A if K & 1 else ModMat.identity(self.R)\n \
    \       for i in range(1,K.bit_length()):\n            A @= A \n            if\
    \ K >> i & 1:\n                R @= A \n        return R\n    \n    def __getitem__(self,\
    \ key: Union[int, Tuple[int, int], slice, Tuple[slice, slice]]):\n        if isinstance(key,\
    \ int):\n            return self.data[key]\n        elif isinstance(key, tuple):\n\
    \            if len(key) == 2:\n                if all(isinstance(k, int) for\
    \ k in key):\n                    return mint(self.data[key[0]][key[1]])\n   \
    \             elif all(isinstance(k, slice) for k in key):\n                 \
    \   return ModMat([[self.data[i][j] for j in range(*key[1].indices(self.C))] \n\
    \                                   for i in range(*key[0].indices(self.R))])\n\
    \            raise IndexError(\"Invalid index\")\n        elif isinstance(key,\
    \ slice):\n            return ModMat([row[:] for row in self.data[key]])\n   \
    \     raise IndexError(\"Invalid index\")\n\n    def __setitem__(self, key: Union[Tuple[int,\
    \ int], slice, Tuple[slice, slice]], value):\n        if isinstance(key, tuple):\n\
    \            if len(key) == 2:\n                if all(isinstance(k, int) for\
    \ k in key):\n                    self.data[key[0]][key[1]] = value % mint.mod\n\
    \                elif all(isinstance(k, slice) for k in key):\n              \
    \      if isinstance(value, ModMat):\n                        for i, row in enumerate(range(*key[0].indices(self.R))):\n\
    \                            for j, col in enumerate(range(*key[1].indices(self.C))):\n\
    \                                self.data[row][col] = value.data[i][j] % mint.mod\n\
    \                    else:\n                        for row in range(*key[0].indices(self.R)):\n\
    \                            for col in range(*key[1].indices(self.C)):\n    \
    \                            self.data[row][col] = value % mint.mod\n        \
    \        else:\n                    raise IndexError(\"Invalid index\")\n    \
    \        else:\n                raise IndexError(\"Invalid index\")\n        elif\
    \ isinstance(key, slice):\n            if isinstance(value, ModMat):\n       \
    \         for i, row in enumerate(range(*key.indices(self.R))):\n            \
    \        self.data[row] = [v % mint.mod for v in value.data[i]]\n            else:\n\
    \                for row in range(*key.indices(self.R)):\n                   \
    \ self.data[row] = [value % mint.mod] * self.C\n        else:\n            raise\
    \ IndexError(\"Invalid index\")\n\n    def __delitem__(self, key: Union[int, slice]):\n\
    \        if isinstance(key, (int, slice)):\n            del self.data[key]\n \
    \           self.R = len(self.data)\n            if self.R == 0:\n           \
    \     self.C = 0\n        else:\n            raise IndexError(\"Invalid index\"\
    )\n\n    \n\n\ndef read(shift=0, base=10):\n    return [int(s, base) + shift for\
    \ s in input().split()]\nimport os\nimport sys\nfrom io import BytesIO, IOBase\n\
    \n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines = 0\n\n    def __init__(self,\
    \ file):\n        self._fd = file.fileno()\n        self.buffer = BytesIO()\n\
    \        self.writable = \"x\" in file.mode or \"r\" not in file.mode\n      \
    \  self.write = self.buffer.write if self.writable else None\n\n    def read(self):\n\
    \        BUFSIZE = self.BUFSIZE\n        while True:\n            b = os.read(self._fd,\
    \ max(os.fstat(self._fd).st_size, BUFSIZE))\n            if not b:\n         \
    \       break\n            ptr = self.buffer.tell()\n            self.buffer.seek(0,\
    \ 2), self.buffer.write(b), self.buffer.seek(ptr)\n        self.newlines = 0\n\
    \        return self.buffer.read()\n\n    def readline(self):\n        BUFSIZE\
    \ = self.BUFSIZE\n        while self.newlines == 0:\n            b = os.read(self._fd,\
    \ max(os.fstat(self._fd).st_size, BUFSIZE))\n            self.newlines = b.count(b\"\
    \\n\") + (not b)\n            ptr = self.buffer.tell()\n            self.buffer.seek(0,\
    \ 2), self.buffer.write(b), self.buffer.seek(ptr)\n        self.newlines -= 1\n\
    \        return self.buffer.readline()\n\n    def flush(self):\n        if self.writable:\n\
    \            os.write(self._fd, self.buffer.getvalue())\n            self.buffer.truncate(0),\
    \ self.buffer.seek(0)\n\n\nclass IOWrapper(IOBase):\n    stdin: 'IOWrapper' =\
    \ None\n    stdout: 'IOWrapper' = None\n    \n    def __init__(self, file):\n\
    \        self.buffer = FastIO(file)\n        self.flush = self.buffer.flush\n\
    \        self.writable = self.buffer.writable\n\n    def write(self, s):\n   \
    \     return self.buffer.write(s.encode(\"ascii\"))\n    \n    def read(self):\n\
    \        return self.buffer.read().decode(\"ascii\")\n    \n    def readline(self):\n\
    \        return self.buffer.readline().decode(\"ascii\")\n\nsys.stdin = IOWrapper.stdin\
    \ = IOWrapper(sys.stdin)\nsys.stdout = IOWrapper.stdout = IOWrapper(sys.stdout)\n\
    \ndef write(*args, **kwargs):\n    '''Prints the values to a stream, or to stdout_fast\
    \ by default.'''\n    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\"\
    , IOWrapper.stdout)\n    at_start = True\n    for x in args:\n        if not at_start:\n\
    \            file.write(sep)\n        file.write(str(x))\n        at_start = False\n\
    \    file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \ndef main():\n    mint.set_mod(998244353)\n    N, K = read()\n    A = ModMat([read()\
    \ for _ in range(N)])\n    B = A**K\n    write(B)\n\nfrom cp_library.math.mod.mint_cls\
    \ import mint\nfrom cp_library.math.linalg.mat.mod.modmat_cls import ModMat\n\
    from cp_library.io.read_int_fn import read\nfrom cp_library.io.write_fn import\
    \ write\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/linalg/mat/mod/modmat_cls.py
  - cp_library/io/read_int_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/library-checker/linear-algebra/pow_of_matrix_modmat.test.py
  requiredBy: []
  timestamp: '2025-03-27 22:10:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/linear-algebra/pow_of_matrix_modmat.test.py
layout: document
redirect_from:
- /verify/test/library-checker/linear-algebra/pow_of_matrix_modmat.test.py
- /verify/test/library-checker/linear-algebra/pow_of_matrix_modmat.test.py.html
title: test/library-checker/linear-algebra/pow_of_matrix_modmat.test.py
---
