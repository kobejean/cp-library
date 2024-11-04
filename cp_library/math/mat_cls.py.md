---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':warning:'
    path: cp_library/math/elm_wise_in_place_mixin.py
    title: cp_library/math/elm_wise_in_place_mixin.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/elm_wise_mixin.py
    title: cp_library/math/elm_wise_mixin.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  - icon: ':warning:'
    path: cp_library/math/mutvec_cls.py
    title: cp_library/math/mutvec_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nfrom typing import Iterable, Container, Sequence\nfrom numbers import Number\n\
    \n\nimport sys\nimport typing\nfrom collections import deque\nfrom typing import\
    \ Callable, Collection, Iterator, TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n\
    \    def __init__(self, stream = sys.stdin):\n        self.stream = stream\n \
    \       self.queue = deque()\n\n    def __next__(self):\n        if not self.queue:\
    \ self.queue.extend(self.line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return next(self.stream).rstrip().split()\n\nclass CharStream(TokenStream):\n\
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
    \ type[T]|T=int) -> ParseFn[T]:\n        if isinstance(spec, type):\n        \
    \    cls = typing.get_origin(spec) or spec\n            args = typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(ts: TokenStream):\n                return cls(next(ts)) + offset\n\
    \            return parse\n        elif isinstance(args := spec, tuple):     \
    \ \n            return Parser.compile_tuple(type(spec), args)\n        elif isinstance(args\
    \ := spec, Collection):  \n            return Parser.compile_collection(type(spec),\
    \ args)\n        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile_line(cls: T, spec=int) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in ts.wait())\n\
    \        return parse\n\n    @staticmethod\n    def compile_repeat(cls: T, spec,\
    \ N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
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
    \            case [spec, int() as n]:\n                return Parser.compile_repeat(cls,\
    \ spec, n)\n            case _:\n                raise NotImplementedError()\n\
    \n        \nclass Parsable:\n    @classmethod\n    def compile(cls):\n       \
    \ def parser(ts: TokenStream):\n            return cls(next(ts))\n        return\
    \ parser\n\nimport operator\n\n\nclass ElmWiseMixin:\n    def elm_wise(self, other,\
    \ op):\n        if isinstance(other, Number):\n            return type(self)(op(x,\
    \ other) for x in self)\n        if isinstance(other, Sequence):\n           \
    \ return type(self)(op(x, y) for x, y in zip(self, other))\n        raise ValueError(\"\
    Operand must be a number or a tuple of the same length\")\n\n    def __add__(self,\
    \ other): return self.elm_wise(other, operator.add)\n    def __radd__(self, other):\
    \ return self.elm_wise(other, operator.add)\n    def __sub__(self, other): return\
    \ self.elm_wise(other, operator.sub)\n    def __rsub__(self, other): return self.elm_wise(other,\
    \ lambda x,y: operator.sub(y,x))\n    def __mul__(self, other): return self.elm_wise(other,\
    \ operator.mul)\n    def __rmul__(self, other): return self.elm_wise(other, operator.mul)\n\
    \    def __truediv__(self, other): return self.elm_wise(other, operator.truediv)\n\
    \    def __rtruediv__(self, other): return self.elm_wise(other, lambda x,y: operator.truediv(y,x))\n\
    \    def __floordiv__(self, other): return self.elm_wise(other, operator.floordiv)\n\
    \    def __rfloordiv__(self, other): return self.elm_wise(other, lambda x,y: operator.floordiv(y,x))\n\
    \    def __mod__(self, other): return self.elm_wise(other, operator.mod)\n\nclass\
    \ ElmWiseInPlaceMixin(ElmWiseMixin):\n    def ielm_wise(self, other, op):\n  \
    \      if isinstance(other, Number):\n            for i in range(len(self)):\n\
    \                self[i] = op(self[i], other)\n        elif isinstance(other,\
    \ Sequence) and len(self) == len(other):\n            for i in range(len(self)):\n\
    \                self[i] = op(self[i], other[i])\n        else:\n            raise\
    \ ValueError(\"Operand must be a number or a list of the same length\")\n    \
    \    return self\n    \n    def __iadd__(self, other): return self.ielm_wise(other,\
    \ operator.add)\n    def __isub__(self, other): return self.ielm_wise(other, operator.sub)\n\
    \    def __imul__(self, other): return self.ielm_wise(other, operator.mul)\n \
    \   def __itruediv__(self, other): return self.ielm_wise(other, operator.truediv)\n\
    \    def __ifloordiv__(self, other): return self.ielm_wise(other, operator.floordiv)\n\
    \    def __imod__(self, other): return self.ielm_wise(other, operator.mod)\n\n\
    \nclass Mat(Parsable, Container, ElmWiseInPlaceMixin):\n\n    def __init__(self,\
    \ data = 0):\n        self.data, self.N, self.M = data, len(data), len(data[0])\n\
    \n    def elm_wise(self, other, op):\n        N, M = self.N, self.M\n        cls\
    \ = type(self)\n        if isinstance(other, Number):\n            return cls([[op(elm,\
    \ other) for elm in row] for row in self.data])\n        if isinstance(other,\
    \ Sequence):\n            # return cls(N, M, (op(x, y) for x, y in zip(self, other)))\n\
    \            return cls([[op(elm, oelm) for elm, oelm in zip(row,orow)] for row,\
    \ orow in zip(self.data, other.data)])\n        raise ValueError(\"Operand must\
    \ be a number or a tuple of the same length\")\n    \n    def ielm_wise(self,\
    \ other, op):\n        data = self.data\n        if isinstance(other, Number):\n\
    \            for i in range(len(self)):\n                data[i] = op(data[i],\
    \ other)\n        elif isinstance(other, Sequence) and len(data) == len(other):\n\
    \            for i in range(len(data)):\n                data[i] = op(data[i],\
    \ other[i])\n        else:\n            raise ValueError(\"Operand must be a number\
    \ or a list of the same length\")\n        return self\n\n    def __len__(self):\n\
    \        return self.R\n    \n    def __contains__(self, x: object) -> bool:\n\
    \        return x in self.data\n\n    def __matmul__(A,B):\n        assert A.M\
    \ == len(B), f\"Dimension mismatch {A.M = } {len(B) = }\"\n        N,M = A.N,\
    \ B.M\n        cls = type(A)\n        R = cls([[0]*M for _ in range(N)])\n   \
    \     \n        for irow in range(0,N*M,M):\n            for k in range(A.M):\n\
    \                krow, a = k*M, A.data[irow+k]\n                for j in range(M):\n\
    \                    R.data[irow+j] = (B.data[krow+j]*a + R.data[irow+j]) % mint.mod\n\
    \n        return R\n    \n    def __pow__(A,K):\n        R = A.copy() if K & 1\
    \ else type(A).identity(A.N)\n        for i in range(1,K.bit_length()):\n    \
    \        A = A @ A\n            if K >> i & 1:\n                R = R @ A\n  \
    \      return R \n\n    @classmethod\n    def identity(cls, N):\n        R = cls([[int(i==j)\
    \ for j in range(N)] for i in range(N)])\n        return R\n    \n    def copy(self):\n\
    \        cls = type(self)\n        obj = cls.__new__(cls)\n        obj.N, obj.M\
    \ = self.N, self.M\n        obj.size = self.size\n        obj.data = self.data\n\
    \        return obj\n    \n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ T: type = int):\n        elm = Parser.compile(T)\n        size = N*M\n     \
    \   def parse(ts: TokenStream):\n            obj = cls.__new__(cls)\n        \
    \    obj.N, obj.M = N, M\n            obj.size = size\n            obj.data =\
    \ list(elm(ts) for _ in range(obj.size))\n            return obj\n        return\
    \ parse\n    \n    def __repr__(self) -> str:\n        return '\\n'.join(' '.join(str(elm)\
    \ for elm in row) for row in self)\n\n\n\n\nclass mint(int):\n    mod = zero =\
    \ one = None\n\n    def __new__(cls, *args, **kwargs):\n        match int(*args,\
    \ **kwargs):\n            case 0: return cls.zero\n            case 1: return\
    \ cls.one\n            case x: return cls.fix(x)\n\n    @classmethod\n    def\
    \ set_mod(cls, mod):\n        cls.mod = mod\n        cls.zero, cls.one = cls.cast(0),\
    \ cls.fix(1)\n\n    @classmethod\n    def fix(cls, x): return cls.cast(x%cls.mod)\n\
    \n    @classmethod\n    def cast(cls, x): return super().__new__(cls,x)\n\n  \
    \  @classmethod\n    def mod_inv(cls, x):\n        a,b,s,t = int(x), cls.mod,\
    \ 1, 0\n        while b: a,b,s,t = b,a%b,t,s-a//b*t\n        if a == 1: return\
    \ cls.fix(s)\n        raise ValueError(f\"{x} is not invertible\")\n    \n   \
    \ @property\n    def inv(self): return mint.mod_inv(self)\n\n    def __add__(self,\
    \ x): return mint.fix(super().__add__(x))\n    def __radd__(self, x): return mint.fix(super().__radd__(x))\n\
    \    def __sub__(self, x): return mint.fix(super().__sub__(x))\n    def __rsub__(self,\
    \ x): return mint.fix(super().__rsub__(x))\n    def __mul__(self, x): return mint.fix(super().__mul__(x))\n\
    \    def __rmul__(self, x): return mint.fix(super().__rmul__(x))\n    def __floordiv__(self,\
    \ x): return self * mint.mod_inv(x)\n    def __rfloordiv__(self, x): return self.inv\
    \ * x\n    def __truediv__(self, x): return self * mint.mod_inv(x)\n    def __rtruediv__(self,\
    \ x): return self.inv * x\n    def __pow__(self, x): \n        return self.cast(super().__pow__(x,\
    \ self.mod))\n    def __neg__(self): return mint.mod-self\n    def __pos__(self):\
    \ return self\n    def __abs__(self): return self\n\n\nclass ModMat(Mat):\n\n\
    \    # def __init__(self, N: int, M: int, data = None):\n    #     super().__init__(N,\
    \ M, data or mint.zero)\n\n    # def __matmul__(A,B):\n    #     assert A.M ==\
    \ len(B), f\"Dimension mismatch {A.M = } {len(B) = }\"\n    #     cls = type(A)\n\
    \    #     R = cls(A.N,A.M)\n    #     Br = super(cls.__bases__[0], B).__getitem__\n\
    \    #     for Ri,Ai in zip(R,A):\n    #         for k,Aik in enumerate(Ai):\n\
    \    #             for j,Bkj in enumerate(Br(k)):\n    #                 Ri[j]\
    \ = Bkj*Aik + Ri[j] \n\n    #     return R\n    \n    # def __pow__(A,K):\n  \
    \  #     A = Mat(A.N, A.M, ((int(elm) for elm in row) for row in A))\n    #  \
    \   R = A if K & 1 else Mat.identity(A.N)\n    #     for i in range(1,K.bit_length()):\n\
    \    #         A = A @ A\n    #         A %= mint.mod\n    #         if K >> i\
    \ & 1:\n    #             R = R @ A\n    #             R %= mint.mod\n    #  \
    \   R = Mat(R.N, R.M, ((mint(elm) for elm in row) for row in R))\n    #     return\
    \ R \n    \n    # @classmethod\n    # def identity(cls, N):\n    #     R = cls(N,\
    \ N, mint.zero)\n    #     for i in range(N):\n    #         R[i,i] = mint.one\n\
    \    #     return R\n    \n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ T: type = int):\n        return super().compile(N, M, T)\n    \n\n\n\nclass\
    \ MutVec(list, ElmWiseInPlaceMixin, Parsable):\n\n    def __init__(self, *args):\n\
    \        if len(args) == 1 and isinstance(args[0], Iterable):\n            super().__init__(args[0])\n\
    \        else:\n            super().__init__(args)\n    \n\n    @classmethod\n\
    \    def compile(cls, T: type = int, N = None):\n        elm = Parser.compile(T)\n\
    \        if N is None:\n            def parse(ts: TokenStream):\n            \
    \    return cls(elm(ts) for _ in ts.wait())\n        else:\n            def parse(ts:\
    \ TokenStream):\n                return cls(elm(ts) for _ in range(N))\n     \
    \   return parse\n"
  code: "import cp_library.math.__header__\n\nfrom typing import Iterable, Container,\
    \ Sequence\nfrom numbers import Number\nfrom cp_library.io.parser_cls import Parsable,\
    \ Parser, TokenStream\nfrom cp_library.math.elm_wise_in_place_mixin import ElmWiseInPlaceMixin\n\
    \n\nclass Mat(Parsable, Container, ElmWiseInPlaceMixin):\n\n    def __init__(self,\
    \ data = 0):\n        self.data, self.N, self.M = data, len(data), len(data[0])\n\
    \n    def elm_wise(self, other, op):\n        N, M = self.N, self.M\n        cls\
    \ = type(self)\n        if isinstance(other, Number):\n            return cls([[op(elm,\
    \ other) for elm in row] for row in self.data])\n        if isinstance(other,\
    \ Sequence):\n            # return cls(N, M, (op(x, y) for x, y in zip(self, other)))\n\
    \            return cls([[op(elm, oelm) for elm, oelm in zip(row,orow)] for row,\
    \ orow in zip(self.data, other.data)])\n        raise ValueError(\"Operand must\
    \ be a number or a tuple of the same length\")\n    \n    def ielm_wise(self,\
    \ other, op):\n        data = self.data\n        if isinstance(other, Number):\n\
    \            for i in range(len(self)):\n                data[i] = op(data[i],\
    \ other)\n        elif isinstance(other, Sequence) and len(data) == len(other):\n\
    \            for i in range(len(data)):\n                data[i] = op(data[i],\
    \ other[i])\n        else:\n            raise ValueError(\"Operand must be a number\
    \ or a list of the same length\")\n        return self\n\n    def __len__(self):\n\
    \        return self.R\n    \n    def __contains__(self, x: object) -> bool:\n\
    \        return x in self.data\n\n    def __matmul__(A,B):\n        assert A.M\
    \ == len(B), f\"Dimension mismatch {A.M = } {len(B) = }\"\n        N,M = A.N,\
    \ B.M\n        cls = type(A)\n        R = cls([[0]*M for _ in range(N)])\n   \
    \     \n        for irow in range(0,N*M,M):\n            for k in range(A.M):\n\
    \                krow, a = k*M, A.data[irow+k]\n                for j in range(M):\n\
    \                    R.data[irow+j] = (B.data[krow+j]*a + R.data[irow+j]) % mint.mod\n\
    \n        return R\n    \n    def __pow__(A,K):\n        R = A.copy() if K & 1\
    \ else type(A).identity(A.N)\n        for i in range(1,K.bit_length()):\n    \
    \        A = A @ A\n            if K >> i & 1:\n                R = R @ A\n  \
    \      return R \n\n    @classmethod\n    def identity(cls, N):\n        R = cls([[int(i==j)\
    \ for j in range(N)] for i in range(N)])\n        return R\n    \n    def copy(self):\n\
    \        cls = type(self)\n        obj = cls.__new__(cls)\n        obj.N, obj.M\
    \ = self.N, self.M\n        obj.size = self.size\n        obj.data = self.data\n\
    \        return obj\n    \n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ T: type = int):\n        elm = Parser.compile(T)\n        size = N*M\n     \
    \   def parse(ts: TokenStream):\n            obj = cls.__new__(cls)\n        \
    \    obj.N, obj.M = N, M\n            obj.size = size\n            obj.data =\
    \ list(elm(ts) for _ in range(obj.size))\n            return obj\n        return\
    \ parse\n    \n    def __repr__(self) -> str:\n        return '\\n'.join(' '.join(str(elm)\
    \ for elm in row) for row in self)\n\n\nfrom cp_library.math.mod.mint_cls import\
    \ mint\n\nclass ModMat(Mat):\n\n    # def __init__(self, N: int, M: int, data\
    \ = None):\n    #     super().__init__(N, M, data or mint.zero)\n\n    # def __matmul__(A,B):\n\
    \    #     assert A.M == len(B), f\"Dimension mismatch {A.M = } {len(B) = }\"\n\
    \    #     cls = type(A)\n    #     R = cls(A.N,A.M)\n    #     Br = super(cls.__bases__[0],\
    \ B).__getitem__\n    #     for Ri,Ai in zip(R,A):\n    #         for k,Aik in\
    \ enumerate(Ai):\n    #             for j,Bkj in enumerate(Br(k)):\n    #    \
    \             Ri[j] = Bkj*Aik + Ri[j] \n\n    #     return R\n    \n    # def\
    \ __pow__(A,K):\n    #     A = Mat(A.N, A.M, ((int(elm) for elm in row) for row\
    \ in A))\n    #     R = A if K & 1 else Mat.identity(A.N)\n    #     for i in\
    \ range(1,K.bit_length()):\n    #         A = A @ A\n    #         A %= mint.mod\n\
    \    #         if K >> i & 1:\n    #             R = R @ A\n    #            \
    \ R %= mint.mod\n    #     R = Mat(R.N, R.M, ((mint(elm) for elm in row) for row\
    \ in R))\n    #     return R \n    \n    # @classmethod\n    # def identity(cls,\
    \ N):\n    #     R = cls(N, N, mint.zero)\n    #     for i in range(N):\n    #\
    \         R[i,i] = mint.one\n    #     return R\n    \n    @classmethod\n    def\
    \ compile(cls, N: int, M: int, T: type = int):\n        return super().compile(N,\
    \ M, T)\n    \n\nfrom cp_library.math.mutvec_cls import MutVec"
  dependsOn:
  - cp_library/io/parser_cls.py
  - cp_library/math/elm_wise_in_place_mixin.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/mutvec_cls.py
  - cp_library/math/elm_wise_mixin.py
  isVerificationFile: false
  path: cp_library/math/mat_cls.py
  requiredBy: []
  timestamp: '2024-11-04 21:00:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/mat_cls.py
layout: document
redirect_from:
- /library/cp_library/math/mat_cls.py
- /library/cp_library/math/mat_cls.py.html
title: cp_library/math/mat_cls.py
---
