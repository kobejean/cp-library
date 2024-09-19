---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':question:'
    path: cp_library/io/parse_stream_fn.py
    title: cp_library/io/parse_stream_fn.py
  - icon: ':question:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mobius_transform_fn.py
    title: cp_library/math/mobius_transform_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mobius_transform_fn.py
    title: cp_library/math/mod/mobius_transform_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/subset_convolution_fn.py
    title: cp_library/math/mod/subset_convolution_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/zeta_transform_fn.py
    title: cp_library/math/mod/zeta_transform_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/subset_convolution_fn.py
    title: cp_library/math/subset_convolution_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/zeta_transform_fn.py
    title: cp_library/math/zeta_transform_fn.py
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
    '''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\n\nimport\
    \ sys\nfrom typing import Type, TypeVar\n\nT = TypeVar('T')\ndef read(spec: Type[T]|T=[int])\
    \ -> T:\n    return parse_stream(sys.stdin, spec)\n\n\nimport typing\nfrom collections\
    \ import deque\nfrom numbers import Number\nfrom typing import Collection, Iterator,\
    \ Type, TypeVar\n\n\nclass Parsable:\n    @classmethod\n    def parse(cls, parse_spec):\n\
    \        return parse_spec(lambda s: cls(s))\n\nT = TypeVar('T')\ndef parse_stream(stream:\
    \ Iterator[str], spec: Type[T]|T) -> T:\n\n    def parse_tuple(cls, specs):\n\
    \        match specs:\n            case [spec, end] if end is ...: \n        \
    \        return cls(parse_line(spec))\n            case specs:               \
    \      \n                return cls(parse_spec(spec) for spec in specs)\n\n  \
    \  def parse_collection(cls, specs) -> list:\n        match specs:\n         \
    \   case [ ] | [_] | set():          \n                return cls(parse_line(*specs))\n\
    \            case [spec, int() as n]: \n                return cls(parse_spec(spec)\
    \ for _ in range(n))\n            case _:\n                raise NotImplementedError()\n\
    \n    def parse_spec(spec):\n        if args := match_spec(spec, Parsable):\n\
    \            cls, args = args\n            return cls.parse(parse_spec, *args)\n\
    \        elif args := match_spec(spec, tuple):      \n            return parse_tuple(*args)\n\
    \        elif args := match_spec(spec, Collection): \n            return parse_collection(*args)\n\
    \        elif issubclass(cls := type(offset := spec), Number):         \n    \
    \        return cls(next_token()) + offset\n        elif callable(cls := spec):\
    \                  \n            return cls(next_token())\n        else:\n   \
    \         raise NotImplementedError()\n\n    def next_token():\n        if not\
    \ queue: queue.extend(next_line())\n        return queue.popleft()\n    \n   \
    \ def parse_line(spec=int):\n        if not queue: queue.extend(next_line())\n\
    \        while queue: yield parse_spec(spec)\n        \n    def next_line():\n\
    \        return next(stream).rstrip().split()\n    \n    def match_spec(spec,\
    \ types):\n        if issubclass(cls := type(specs := spec), types):\n       \
    \     return cls, specs\n        elif (isinstance(spec, type) and \n         \
    \    issubclass(cls := typing.get_origin(spec) or spec, types)):\n           \
    \ return cls, (typing.get_args(spec) or tuple())\n        \n    queue = deque()\
    \ \n    return parse_spec(spec)\nmod = 998244353\n\nN, = read()\nif N < 10:\n\
    \    \n    \n    def subset_convolution(A, B, N):\n        Z = 1 << N\n    \n\
    \        # Prepare arrays for rank (popcount) decomposition\n        Arank = [[0]*Z\
    \ for _ in range(N+1)]\n        Brank = [[0]*Z for _ in range(N+1)]\n    \n  \
    \      # Initialize rank arrays\n        for mask in range(Z):\n            rank\
    \ = mask.bit_count()\n            Arank[rank][mask] = A[mask]\n            Brank[rank][mask]\
    \ = B[mask]\n    \n        # Zeta transform for each rank\n        for Ar in Arank:\
    \ zeta_transform(Ar, N)\n        for Br in Brank: zeta_transform(Br, N)\n    \n\
    \        # Convolution\n        Crank = [[0 for _ in range(Z)] for _ in range(N+1)]\n\
    \        for mask in range(Z):\n            L = mask.bit_count()+1\n         \
    \   for i in range(L):\n                for j in range(min(L, N+1-i)):\n     \
    \               k = i+j\n                    Crank[k][mask] = Crank[k][mask] +\
    \ Arank[i][mask] * Brank[j][mask]\n    \n        # M\xF6bius transform (inverse\
    \ of Zeta transform)\n        for Cr in Crank: mobius_transform(Cr, N)\n     \
    \       \n        # Combine results\n        C = [0] * Z\n        for mask in\
    \ range(Z):\n            rank = mask.bit_count()\n            C[mask] = Crank[rank][mask]\n\
    \    \n        return C\n    \n    \n    def zeta_transform(A, N):\n        for\
    \ i in range(N):\n            bit = 1 << i\n            for mask in range(1 <<\
    \ N):\n                if mask & bit:\n                    A[mask] += A[mask ^\
    \ bit]\n        return A\n    \n    def mobius_transform(A, N):\n        for i\
    \ in range(N):\n            bit = 1 << i\n            for mask in range(1 << N):\n\
    \                if mask & bit:\n                    A[mask] -= A[mask ^ bit]\n\
    \        return A\n    \n    \n    class mint(int):\n        mod = zero = one\
    \ = None\n    \n        def __new__(cls, *args, **kwargs):\n            match\
    \ int(*args, **kwargs):\n                case 0: return cls.zero\n           \
    \     case 1: return cls.one\n                case x: return cls.fix(x)\n    \n\
    \        @classmethod\n        def set_mod(cls, mod):\n            cls.mod = mod\n\
    \            cls.zero, cls.one = cls.cast(0), cls.fix(1)\n    \n        @classmethod\n\
    \        def fix(cls, x): return cls.cast(x%cls.mod)\n    \n        @classmethod\n\
    \        def cast(cls, x): return super().__new__(cls,x)\n    \n        @classmethod\n\
    \        def mod_inv(cls, x):\n            a,b,s,t = int(x), cls.mod, 1, 0\n \
    \           while b: a,b,s,t = b,a%b,t,s-a//b*t\n            if a == 1: return\
    \ cls.fix(s)\n            raise ValueError(f\"{x} is not invertible\")\n     \
    \   \n        @property\n        def inv(self): return mint.mod_inv(self)\n  \
    \  \n        def __add__(self, x): return mint.fix(super().__add__(x))\n     \
    \   def __radd__(self, x): return mint.fix(super().__radd__(x))\n        def __sub__(self,\
    \ x): return mint.fix(super().__sub__(x))\n        def __rsub__(self, x): return\
    \ mint.fix(super().__rsub__(x))\n        def __mul__(self, x): return mint.fix(super().__mul__(x))\n\
    \        def __rmul__(self, x): return mint.fix(super().__rmul__(x))\n       \
    \ def __floordiv__(self, x): return self * mint.mod_inv(x)\n        def __rfloordiv__(self,\
    \ x): return self.inv * x\n        def __truediv__(self, x): return self * mint.mod_inv(x)\n\
    \        def __rtruediv__(self, x): return self.inv * x\n        def __pow__(self,\
    \ x): \n            return self.cast(super().__pow__(x, self.mod))\n        def\
    \ __eq__(self, x): return super().__eq__(self-x, 0)\n        def __neg__(self):\
    \ return mint.mod-self\n        def __pos__(self): return self\n        def __abs__(self):\
    \ return self\n    \n    mint.set_mod(mod)\n    F = read(list[mint])\n    G =\
    \ read(list[mint])\n    print(*subset_convolution(F, G, N))\nelse:\n    \n   \
    \ def subset_convolution(A, B, N, mod):\n        Z = 1 << N\n    \n        # Prepare\
    \ arrays for rank (popcount) decomposition\n        Arank = [[0]*Z for _ in range(N+1)]\n\
    \        Brank = [[0]*Z for _ in range(N+1)]\n    \n        # Initialize rank\
    \ arrays\n        for mask in range(Z):\n            rank = mask.bit_count()\n\
    \            Arank[rank][mask] = A[mask]\n            Brank[rank][mask] = B[mask]\n\
    \    \n        # Zeta transform for each rank\n        for Ar in Arank: zeta_transform(Ar,\
    \ N, mod)\n        for Br in Brank: zeta_transform(Br, N, mod)\n    \n       \
    \ # Convolution\n        Crank = [[0]*Z for _ in range(N+1)]\n        for mask\
    \ in range(Z):\n            L = mask.bit_count()+1\n            for i in range(L):\n\
    \                for j in range(min(L, N+1-i)):\n                    k = i+j\n\
    \                    Crank[k][mask] = (Crank[k][mask] + Arank[i][mask] * Brank[j][mask])\
    \ % mod\n    \n        # M\xF6bius transform (inverse of Zeta transform)\n   \
    \     for Cr in Crank: mobius_transform(Cr, N, mod)\n            \n        # Combine\
    \ results\n        C = [0] * Z\n        for mask in range(Z):\n            rank\
    \ = mask.bit_count()\n            C[mask] = Crank[rank][mask]\n    \n        return\
    \ C\n    \n    \n    def zeta_transform(A, N, mod):\n        for i in range(N):\n\
    \            bit = 1 << i\n            for mask in range(1 << N):\n          \
    \      if mask & bit:\n                    A[mask] = (A[mask] + A[mask ^ bit])\
    \ % mod\n        return A\n    \n    def mobius_transform(A, N, mod):\n      \
    \  for i in range(N):\n            bit = 1 << i\n            for mask in range(1\
    \ << N):\n                if mask & bit:\n                    A[mask] = (A[mask]\
    \ - A[mask ^ bit]) % mod\n        return A\n    \n    F = read(list[int])\n  \
    \  G = read(list[int])\n    print(*subset_convolution(F, G, N, mod))\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution\n\
    from cp_library.io.read_specs_fn import read\nmod = 998244353\n\nN, = read()\n\
    if N < 10:\n    from cp_library.math.subset_convolution_fn import subset_convolution\n\
    \    from cp_library.math.mod.mint_cls import mint\n    mint.set_mod(mod)\n  \
    \  F = read(list[mint])\n    G = read(list[mint])\n    print(*subset_convolution(F,\
    \ G, N))\nelse:\n    from cp_library.math.mod.subset_convolution_fn import subset_convolution\n\
    \    \n    F = read(list[int])\n    G = read(list[int])\n    print(*subset_convolution(F,\
    \ G, N, mod))"
  dependsOn:
  - cp_library/io/read_specs_fn.py
  - cp_library/math/subset_convolution_fn.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/mod/subset_convolution_fn.py
  - cp_library/io/parse_stream_fn.py
  - cp_library/math/zeta_transform_fn.py
  - cp_library/math/mobius_transform_fn.py
  - cp_library/math/mod/zeta_transform_fn.py
  - cp_library/math/mod/mobius_transform_fn.py
  - cp_library/io/parsable_cls.py
  isVerificationFile: true
  path: test/subset_convolution.test.py
  requiredBy: []
  timestamp: '2024-09-20 02:31:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/subset_convolution.test.py
layout: document
redirect_from:
- /verify/test/subset_convolution.test.py
- /verify/test/subset_convolution.test.py.html
title: test/subset_convolution.test.py
---
