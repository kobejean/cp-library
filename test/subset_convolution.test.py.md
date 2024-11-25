---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
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
    \ sys\nfrom typing import Type, TypeVar, overload\nfrom io import TextIOBase\n\
    \nimport typing\nfrom collections import deque\nfrom numbers import Number\nfrom\
    \ types import GenericAlias \nfrom typing import Callable, Collection, Iterator,\
    \ TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self, stream:\
    \ TextIOBase = sys.stdin):\n        self.queue = deque()\n        self.stream\
    \ = stream\n\n    def __next__(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self.line())\n        while self.queue: yield\n\
    \        \n    def line(self):\n        assert not self.queue\n        return\
    \ sys.stdin.readline().split()\n\n    def n_uints(self, n: int, shift = 0, max_digits:\
    \ int = 20):\n        # sync buffers\n        tokens: list[str] = []\n       \
    \ while (lim := sys.stdin.buffer.tell() - sys.stdin.tell()) and len(tokens) <\
    \ n:\n            residual_str: str = sys.stdin.readline(lim)\n            tokens.extend(residual_str.split())\n\
    \        \n        result = [0] * n\n        pos = 0\n        \n        # Process\
    \ residual string and check for partial token\n        partial = None\n      \
    \  if tokens:\n            if not residual_str[-1].isspace():\n              \
    \  partial = tokens.pop()\n            for pos, token in enumerate(tokens):\n\
    \                result[pos] = int(token)+shift\n            pos += 1\n      \
    \  # Process remaining data token by token\n        stdin_buffer = sys.stdin.buffer\n\
    \        num = int(partial) if partial else 0\n        have_digit = partial is\
    \ not None\n\n        original_chunk_size = sys.stdin._CHUNK_SIZE\n        sys.stdin._CHUNK_SIZE\
    \ = max(original_chunk_size, max_digits * (n - pos))\n        \n        while\
    \ pos < n:\n            byte = stdin_buffer.read(1)\n\n            match byte[0]:\n\
    \                case 10 | 32:\n                    if have_digit:\n         \
    \               result[pos] = num+shift\n                        pos += 1\n  \
    \                      num = 0\n                        have_digit = False\n \
    \               case char:  # digit\n                    num = (num * 10) + (char\
    \ - 48)\n                    have_digit = True\n\n        if have_digit:\n   \
    \         result[pos] = num+shift\n            pos += 1\n\n        sys.stdin._CHUNK_SIZE\
    \ = original_chunk_size \n        if pos < n:\n            raise EOFError(f\"\
    Only found {pos} numbers, expected {n}\")\n            \n        return result\n\
    \    \n    def n_ints(self, n: int, shift = 0, max_digits: int = 20):\n      \
    \  # sync buffers\n        tokens: list[str] = []\n        while (lim := sys.stdin.buffer.tell()\
    \ - sys.stdin.tell()) and len(tokens) < n:\n            residual_str: str = sys.stdin.readline(lim)\n\
    \            tokens.extend(residual_str.split())\n        \n        result = [0]\
    \ * n\n        pos = 0\n        \n        # Process residual string and check\
    \ for partial token\n        partial = None\n        if tokens:\n            if\
    \ not residual_str[-1].isspace():\n                partial = tokens.pop()\n  \
    \          for pos, token in enumerate(tokens):\n                result[pos] =\
    \ int(token)+shift\n            pos += 1\n        # Process remaining data token\
    \ by token\n        stdin_buffer = sys.stdin.buffer\n        num = abs(int(partial))\
    \ if partial else 0\n        is_negative = partial and partial.startswith('-')\n\
    \        have_digit = partial is not None\n\n        original_chunk_size = sys.stdin._CHUNK_SIZE\n\
    \        sys.stdin._CHUNK_SIZE = max(original_chunk_size, max_digits * (n - pos))\n\
    \        \n        while pos < n:\n            byte = stdin_buffer.read(1)\n\n\
    \            match byte[0]:\n                case 10 | 32:\n                 \
    \   if have_digit:\n                        result[pos] = -num+shift if is_negative\
    \ else num+shift\n                        pos += 1\n                        num\
    \ = 0\n                        is_negative = False\n                        have_digit\
    \ = False\n                case 45:  # minus sign\n                    is_negative\
    \ = True\n                case char:  # digit\n                    num = (num\
    \ * 10) + (char - 48)\n                    have_digit = True\n\n        if have_digit:\n\
    \            result[pos] = -num+shift if is_negative else num+shift\n        \
    \    pos += 1\n\n        sys.stdin._CHUNK_SIZE = original_chunk_size \n      \
    \  if pos < n:\n            raise EOFError(f\"Only found {pos} numbers, expected\
    \ {n}\")\n            \n        return result\n\nclass CharStream(TokenStream):\n\
    \    def line(self):\n        assert not self.queue\n        return next(self.stream).rstrip()\n\
    \        \nT = TypeVar('T')\nParseFn: TypeAlias = Callable[[TokenStream],T]\n\
    class Parser:\n    def __init__(self, spec: type[T]|T):\n        self.parse =\
    \ Parser.compile(spec)\n\n    def __call__(self, ts: TokenStream) -> T:\n    \
    \    return self.parse(ts)\n    \n    @staticmethod\n    def compile_type(cls:\
    \ type[T], args = ()) -> T:\n        if issubclass(cls, Parsable):\n         \
    \   return cls.compile(*args)\n        elif issubclass(cls, (Number, str)):\n\
    \            def parse(ts: TokenStream):\n                return cls(next(ts))\
    \              \n            return parse\n        elif issubclass(cls, tuple):\n\
    \            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection):\n            return Parser.compile_collection(cls, args)\n    \
    \    elif callable(cls):\n            def parse(ts: TokenStream):\n          \
    \      return cls(next(ts))              \n            return parse\n        else:\n\
    \            raise NotImplementedError()\n    \n    @staticmethod\n    def compile(spec:\
    \ type[T]|T=int) -> ParseFn[T]:\n        if isinstance(spec, (type, GenericAlias)):\n\
    \            cls = typing.get_origin(spec) or spec\n            args = typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(ts: TokenStream):\n                return cls(next(ts)) + offset\n\
    \            return parse\n        elif isinstance(args := spec, tuple):     \
    \ \n            return Parser.compile_tuple(type(spec), args)\n        elif isinstance(args\
    \ := spec, Collection):  \n            return Parser.compile_collection(type(spec),\
    \ args)\n        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile_line(cls: T, spec=int) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in ts.wait())\n\
    \        return parse\n    \n    # @staticmethod\n    # def compile_n_ints(cls:\
    \ T, N, shift = int) -> ParseFn[T]:\n    #     shift = shift if isinstance(shift,\
    \ int) else 0\n    #     def parse(ts: TokenStream):\n    #         return cls(ts.n_ints(N,\
    \ shift))\n    #     return parse\n\n    @staticmethod\n    def compile_repeat(cls:\
    \ T, spec, N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream):\n            return cls(fn(ts) for _ in range(N))\n        return\
    \ parse\n\n    @staticmethod\n    def compile_children(cls: T, specs) -> ParseFn[T]:\n\
    \        fns = tuple(Parser.compile(spec) for spec in specs)\n        def parse(ts:\
    \ TokenStream):\n            return cls(fn(ts) for fn in fns)  \n        return\
    \ parse\n\n    @staticmethod\n    def compile_tuple(cls: type[T], specs) -> ParseFn[T]:\n\
    \        match specs:\n            case [spec, end] if end is ...:\n         \
    \       return Parser.compile_line(cls, spec)\n            case specs:   \n  \
    \              return Parser.compile_children(cls, specs)\n    \n    @staticmethod\n\
    \    def compile_collection(cls, specs):\n        match specs:\n            case\
    \ [ ] | [_] | set():\n                return Parser.compile_line(cls, *specs)\n\
    \            case [spec, int() as N]:\n                # if issubclass(spec, int)\
    \ or isinstance(spec, int):\n                #     return Parser.compile_n_ints(cls,\
    \ N, spec)\n                return Parser.compile_repeat(cls, spec, N)\n     \
    \       case _:\n                raise NotImplementedError()\n\n        \nclass\
    \ Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(ts: TokenStream):\n\
    \            return cls(next(ts))\n        return parser\n\nT = TypeVar('T')\n\
    @overload\ndef read() -> list[int]: ...\n@overload\ndef read(spec: int|None) ->\
    \ list[int]: ...\n@overload\ndef read(spec: Type[T]|T, char=False) -> T: ...\n\
    def read(spec: Type[T]|T=None, char=False):\n    match spec, char:\n        case\
    \ None, False:\n            return list(map(int, input().split()))\n        case\
    \ int(offset), False:\n            return [int(s)+offset for s in input().split()]\n\
    \        case _, _:\n            if char:\n                stream = CharStream()\n\
    \            else:\n                stream = TokenStream()\n            parser:\
    \ T = Parser.compile(spec)\n            return parser(stream)\nmod = 998244353\n\
    \nN, = read()\nif N < 10:\n    \n    \n    def subset_convolution(A, B, N):\n\
    \        Z = 1 << N\n    \n        # Prepare arrays for rank (popcount) decomposition\n\
    \        Arank = [[0]*Z for _ in range(N+1)]\n        Brank = [[0]*Z for _ in\
    \ range(N+1)]\n    \n        # Initialize rank arrays\n        for mask in range(Z):\n\
    \            rank = mask.bit_count()\n            Arank[rank][mask] = A[mask]\n\
    \            Brank[rank][mask] = B[mask]\n    \n        # Zeta transform for each\
    \ rank\n        for Ar in Arank: zeta_transform(Ar, N)\n        for Br in Brank:\
    \ zeta_transform(Br, N)\n    \n        # Convolution\n        Crank = [[0 for\
    \ _ in range(Z)] for _ in range(N+1)]\n        for mask in range(Z):\n       \
    \     L = mask.bit_count()+1\n            for i in range(L):\n               \
    \ for j in range(min(L, N+1-i)):\n                    k = i+j\n              \
    \      Crank[k][mask] = Crank[k][mask] + Arank[i][mask] * Brank[j][mask]\n   \
    \ \n        # M\xF6bius transform (inverse of Zeta transform)\n        for Cr\
    \ in Crank: mobius_transform(Cr, N)\n            \n        # Combine results\n\
    \        C = [0] * Z\n        for mask in range(Z):\n            rank = mask.bit_count()\n\
    \            C[mask] = Crank[rank][mask]\n    \n        return C\n    \n    \n\
    \    \n    def zeta_transform(A, N, block=5):\n        for i in range(min(block,N)):\n\
    \            for mask in range(bit := 1<<i, 1<<N):\n                if mask &\
    \ bit:\n                    A[mask] += A[mask ^ bit]\n        for i in range(block,N):\n\
    \            for base in range(bit := 1<<i, 1<<N, bit << 1):\n               \
    \ for mask in range(base, base+bit):\n                    A[mask] += A[mask ^\
    \ bit]\n        return A\n    \n    \n    def mobius_transform(A, N, block=5):\n\
    \        for i in range(min(block,N)):\n            for mask in range(bit := 1<<i,\
    \ 1<<N):\n                if mask & bit:\n                    A[mask] -= A[mask\
    \ ^ bit]\n        for i in range(block,N):\n            for base in range(bit\
    \ := 1<<i, 1<<N, bit << 1):\n                for mask in range(base, base+bit):\n\
    \                    A[mask] -= A[mask ^ bit]\n        return A\n    \n    \n\
    \    class mint(int):\n        mod = zero = one = two = None\n    \n        def\
    \ __new__(cls, *args, **kwargs):\n            match int(*args, **kwargs):\n  \
    \              case 0: return cls.zero\n                case 1: return cls.one\n\
    \                case 2: return cls.two\n                case x: return cls.fix(x)\n\
    \    \n        @classmethod\n        def set_mod(cls, mod):\n            cls.mod\
    \ = mod\n            cls.zero = cls.cast(0)\n            cls.one = cls.fix(1)\n\
    \            cls.two = cls.fix(2)\n    \n        @classmethod\n        def fix(cls,\
    \ x): return cls.cast(x%cls.mod)\n    \n        @classmethod\n        def cast(cls,\
    \ x): return super().__new__(cls,x)\n    \n        @classmethod\n        def mod_inv(cls,\
    \ x):\n            a,b,s,t = int(x), cls.mod, 1, 0\n            while b: a,b,s,t\
    \ = b,a%b,t,s-a//b*t\n            if a == 1: return cls.fix(s)\n            raise\
    \ ValueError(f\"{x} is not invertible\")\n        \n        @property\n      \
    \  def inv(self): return mint.mod_inv(self)\n    \n        def __add__(self, x):\
    \ return mint.fix(super().__add__(x))\n        def __radd__(self, x): return mint.fix(super().__radd__(x))\n\
    \        def __sub__(self, x): return mint.fix(super().__sub__(x))\n        def\
    \ __rsub__(self, x): return mint.fix(super().__rsub__(x))\n        def __mul__(self,\
    \ x): return mint.fix(super().__mul__(x))\n        def __rmul__(self, x): return\
    \ mint.fix(super().__rmul__(x))\n        def __floordiv__(self, x): return self\
    \ * mint.mod_inv(x)\n        def __rfloordiv__(self, x): return self.inv * x\n\
    \        def __truediv__(self, x): return self * mint.mod_inv(x)\n        def\
    \ __rtruediv__(self, x): return self.inv * x\n        def __pow__(self, x): \n\
    \            return self.cast(super().__pow__(x, self.mod))\n        def __neg__(self):\
    \ return mint.mod-self\n        def __pos__(self): return self\n        def __abs__(self):\
    \ return self\n    \n    mint.set_mod(mod)\n    F = read(list[mint])\n    G =\
    \ read(list[mint])\n    print(*subset_convolution(F, G, N))\nelse:\n    \n   \
    \ \n    def subset_convolution(A, B, N, mod):\n        Z = 1 << N\n    \n    \
    \    # Prepare arrays for rank (popcount) decomposition\n        Arank = [[0]*Z\
    \ for _ in range(N+1)]\n        Brank = [[0]*Z for _ in range(N+1)]\n    \n  \
    \      # Initialize rank arrays\n        for mask in range(Z):\n            rank\
    \ = mask.bit_count()\n            Arank[rank][mask] = A[mask]\n            Brank[rank][mask]\
    \ = B[mask]\n    \n        # Zeta transform for each rank\n        for Ar in Arank:\
    \ zeta_transform(Ar, N, mod)\n        for Br in Brank: zeta_transform(Br, N, mod)\n\
    \    \n        # Convolution\n        Crank = [[0]*Z for _ in range(N+1)]\n  \
    \      for mask in range(Z):\n            L = mask.bit_count()+1\n           \
    \ for i in range(L):\n                for j in range(min(L, N+1-i)):\n       \
    \             k = i+j\n                    Crank[k][mask] = (Crank[k][mask] +\
    \ Arank[i][mask] * Brank[j][mask]) % mod\n    \n        # M\xF6bius transform\
    \ (inverse of Zeta transform)\n        for Cr in Crank: mobius_transform(Cr, N,\
    \ mod)\n            \n        # Combine results\n        C = [0] * Z\n       \
    \ for mask in range(Z):\n            rank = mask.bit_count()\n            C[mask]\
    \ = Crank[rank][mask]\n    \n        return C\n    \n    \n    \n    def zeta_transform(A,\
    \ N, mod, block=5):\n        for i in range(min(block,N)):\n            for mask\
    \ in range(bit := 1<<i, 1<<N):\n                if mask & bit:\n             \
    \       A[mask] = (A[mask] + A[mask ^ bit]) % mod\n        for i in range(block,N):\n\
    \            for base in range(bit := 1<<i, 1<<N, bit << 1):\n               \
    \ for mask in range(base, base+bit):\n                    A[mask] = (A[mask] +\
    \ A[mask ^ bit]) % mod\n        return A\n    \n    \n    def mobius_transform(A,\
    \ N, mod, block=5):\n        for i in range(min(block,N)):\n            for mask\
    \ in range(bit := 1<<i, 1<<N):\n                if mask & bit:\n             \
    \       A[mask] = (A[mask] - A[mask ^ bit]) % mod\n        for i in range(block,N):\n\
    \            for base in range(bit := 1<<i, 1<<N, bit << 1):\n               \
    \ for mask in range(base, base+bit):\n                    A[mask] = (A[mask] -\
    \ A[mask ^ bit]) % mod\n        return A\n    \n    F = read(list[int])\n    G\
    \ = read(list[int])\n    print(*subset_convolution(F, G, N, mod))\n"
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
  - cp_library/io/parser_cls.py
  - cp_library/math/zeta_transform_fn.py
  - cp_library/math/mobius_transform_fn.py
  - cp_library/math/mod/zeta_transform_fn.py
  - cp_library/math/mod/mobius_transform_fn.py
  isVerificationFile: true
  path: test/subset_convolution.test.py
  requiredBy: []
  timestamp: '2024-11-25 18:54:05+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/subset_convolution.test.py
layout: document
redirect_from:
- /verify/test/subset_convolution.test.py
- /verify/test/subset_convolution.test.py.html
title: test/subset_convolution.test.py
---
