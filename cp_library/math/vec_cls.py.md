---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/elm_wise_mixin.py
    title: cp_library/math/elm_wise_mixin.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/vec2d_cls.py
    title: cp_library/math/vec2d_cls.py
  - icon: ':warning:'
    path: cp_library/math/vec3d_cls.py
    title: cp_library/math/vec3d_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc151_f_fbisect_left.test.py
    title: test/abc151_f_fbisect_left.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc189_e_vec2d.test.py
    title: test/abc189_e_vec2d.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc274_e_vec2d.test.py
    title: test/abc274_e_vec2d.test.py
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
    \n\n\nimport sys\nimport typing\nfrom collections import deque\nfrom numbers import\
    \ Number\nfrom types import GenericAlias \nfrom typing import Callable, Collection,\
    \ Iterator, TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n    stream = sys.stdin\n\
    \n    def __init__(self):\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return TokenStream.stream.readline().split()\n\nclass\
    \ CharStream(TokenStream):\n    def line(self):\n        assert not self.queue\n\
    \        return next(TokenStream.stream).rstrip()\n        \nT = TypeVar('T')\n\
    ParseFn: TypeAlias = Callable[[TokenStream],T]\nclass Parser:\n    def __init__(self,\
    \ spec: type[T]|T):\n        self.parse = Parser.compile(spec)\n\n    def __call__(self,\
    \ ts: TokenStream) -> T:\n        return self.parse(ts)\n    \n    @staticmethod\n\
    \    def compile_type(cls: type[T], args = ()) -> T:\n        if issubclass(cls,\
    \ Parsable):\n            return cls.compile(*args)\n        elif issubclass(cls,\
    \ (Number, str)):\n            def parse(ts: TokenStream):\n                return\
    \ cls(next(ts))              \n            return parse\n        elif issubclass(cls,\
    \ tuple):\n            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
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
    \            return cls(next(ts))\n        return parser\nfrom math import hypot\n\
    \nimport operator\nfrom typing import Sequence\n\nclass ElmWiseMixin:\n    def\
    \ elm_wise(self, other, op):\n        if isinstance(other, Number):\n        \
    \    return type(self)(op(x, other) for x in self)\n        if isinstance(other,\
    \ Sequence):\n            return type(self)(op(x, y) for x, y in zip(self, other))\n\
    \        raise ValueError(\"Operand must be a number or a tuple of the same length\"\
    )\n\n    def __add__(self, other): return self.elm_wise(other, operator.add)\n\
    \    def __radd__(self, other): return self.elm_wise(other, operator.add)\n  \
    \  def __sub__(self, other): return self.elm_wise(other, operator.sub)\n    def\
    \ __rsub__(self, other): return self.elm_wise(other, lambda x,y: operator.sub(y,x))\n\
    \    def __mul__(self, other): return self.elm_wise(other, operator.mul)\n   \
    \ def __rmul__(self, other): return self.elm_wise(other, operator.mul)\n    def\
    \ __truediv__(self, other): return self.elm_wise(other, operator.truediv)\n  \
    \  def __rtruediv__(self, other): return self.elm_wise(other, lambda x,y: operator.truediv(y,x))\n\
    \    def __floordiv__(self, other): return self.elm_wise(other, operator.floordiv)\n\
    \    def __rfloordiv__(self, other): return self.elm_wise(other, lambda x,y: operator.floordiv(y,x))\n\
    \    def __mod__(self, other): return self.elm_wise(other, operator.mod)\n\n \
    \   def distance(self: 'ElmWiseMixin', other: 'ElmWiseMixin'):\n        diff =\
    \ other-self\n        return hypot(*diff)\n    \n    def magnitude(vec: 'ElmWiseMixin'):\n\
    \        return hypot(*vec)\n    \n    def norm(vec: 'ElmWiseMixin'):\n      \
    \  return vec / vec.magnitude()\nfrom typing import Iterable \n\nclass Vec(ElmWiseMixin,\
    \ tuple, Parsable):\n    def __new__(cls, *args):\n        if len(args) == 1 and\
    \ isinstance(args[0], Iterable):\n            return super().__new__(cls, args[0])\n\
    \        return super().__new__(cls, args)\n\n    @classmethod\n    def compile(cls,\
    \ T: type = int, N = None):\n        elm = Parser.compile(T)\n        if N is\
    \ None:\n            def parse(ts: TokenStream):\n                return cls(elm(ts)\
    \ for _ in ts.wait())\n        else:\n            def parse(ts: TokenStream):\n\
    \                return cls(elm(ts) for _ in range(N))\n        return parse\n\
    \  \n"
  code: "import cp_library.math.__header__\n\nfrom cp_library.io.parser_cls import\
    \ Parsable, Parser, TokenStream\nfrom cp_library.math.elm_wise_mixin import ElmWiseMixin\n\
    from typing import Iterable \nfrom math import hypot\n\nclass Vec(ElmWiseMixin,\
    \ tuple, Parsable):\n    def __new__(cls, *args):\n        if len(args) == 1 and\
    \ isinstance(args[0], Iterable):\n            return super().__new__(cls, args[0])\n\
    \        return super().__new__(cls, args)\n\n    @classmethod\n    def compile(cls,\
    \ T: type = int, N = None):\n        elm = Parser.compile(T)\n        if N is\
    \ None:\n            def parse(ts: TokenStream):\n                return cls(elm(ts)\
    \ for _ in ts.wait())\n        else:\n            def parse(ts: TokenStream):\n\
    \                return cls(elm(ts) for _ in range(N))\n        return parse\n\
    \  "
  dependsOn:
  - cp_library/io/parser_cls.py
  - cp_library/math/elm_wise_mixin.py
  isVerificationFile: false
  path: cp_library/math/vec_cls.py
  requiredBy:
  - cp_library/math/vec2d_cls.py
  - cp_library/math/vec3d_cls.py
  timestamp: '2024-11-26 21:56:46+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc151_f_fbisect_left.test.py
  - test/abc189_e_vec2d.test.py
  - test/abc274_e_vec2d.test.py
documentation_of: cp_library/math/vec_cls.py
layout: document
redirect_from:
- /library/cp_library/math/vec_cls.py
- /library/cp_library/math/vec_cls.py.html
title: cp_library/math/vec_cls.py
---
