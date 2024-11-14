---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/elm_wise_mixin.py
    title: cp_library/math/elm_wise_mixin.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/vec_cls.py
    title: cp_library/math/vec_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
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
    \nfrom io import TextIOBase\n\n\nimport sys\nimport typing\nfrom collections import\
    \ deque\nfrom numbers import Number\nfrom types import GenericAlias \nfrom typing\
    \ import Callable, Collection, Iterator, TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n\
    \    def __init__(self, stream: TextIOBase = sys.stdin):\n        self.queue =\
    \ deque()\n        self.stream = stream\n\n    def __next__(self):\n        if\
    \ not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return sys.stdin.readline().split()\n\n    def n_uints(self,\
    \ n: int, shift = 0, max_digits: int = 20):\n        # sync buffers\n        tokens:\
    \ list[str] = []\n        while (lim := sys.stdin.buffer.tell() - sys.stdin.tell())\
    \ and len(tokens) < n:\n            residual_str: str = sys.stdin.readline(lim)\n\
    \            tokens.extend(residual_str.split())\n        \n        result = [0]\
    \ * n\n        pos = 0\n        \n        # Process residual string and check\
    \ for partial token\n        partial = None\n        if tokens:\n            if\
    \ not residual_str[-1].isspace():\n                partial = tokens.pop()\n  \
    \          for pos, token in enumerate(tokens):\n                result[pos] =\
    \ int(token)+shift\n            pos += 1\n        # Process remaining data token\
    \ by token\n        stdin_buffer = sys.stdin.buffer\n        num = int(partial)\
    \ if partial else 0\n        have_digit = partial is not None\n\n        original_chunk_size\
    \ = sys.stdin._CHUNK_SIZE\n        sys.stdin._CHUNK_SIZE = max(original_chunk_size,\
    \ max_digits * (n - pos))\n        \n        while pos < n:\n            byte\
    \ = stdin_buffer.read(1)\n\n            match byte[0]:\n                case 10\
    \ | 32:\n                    if have_digit:\n                        result[pos]\
    \ = num+shift\n                        pos += 1\n                        num =\
    \ 0\n                        have_digit = False\n                case char:  #\
    \ digit\n                    num = (num * 10) + (char - 48)\n                \
    \    have_digit = True\n\n        if have_digit:\n            result[pos] = num+shift\n\
    \            pos += 1\n\n        sys.stdin._CHUNK_SIZE = original_chunk_size \n\
    \        if pos < n:\n            raise EOFError(f\"Only found {pos} numbers,\
    \ expected {n}\")\n            \n        return result\n    \n    def n_ints(self,\
    \ n: int, shift = 0, max_digits: int = 20):\n        # sync buffers\n        tokens:\
    \ list[str] = []\n        while (lim := sys.stdin.buffer.tell() - sys.stdin.tell())\
    \ and len(tokens) < n:\n            residual_str: str = sys.stdin.readline(lim)\n\
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
    \        return parse\n    \n    @staticmethod\n    def compile_n_ints(cls: T,\
    \ N, shift = int) -> ParseFn[T]:\n        shift = shift if isinstance(shift, int)\
    \ else 0\n        def parse(ts: TokenStream):\n            return cls(ts.n_ints(N,\
    \ shift))\n        return parse\n\n    @staticmethod\n    def compile_repeat(cls:\
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
    \            case [spec, int() as N]:\n                if issubclass(spec, int)\
    \ or isinstance(spec, int):\n                    return Parser.compile_n_ints(cls,\
    \ N, spec)\n                return Parser.compile_repeat(cls, spec, N)\n     \
    \       case _:\n                raise NotImplementedError()\n\n        \nclass\
    \ Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(ts: TokenStream):\n\
    \            return cls(next(ts))\n        return parser\n\n\nimport operator\n\
    from typing import Sequence\n\nclass ElmWiseMixin:\n    def elm_wise(self, other,\
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
    \    def __mod__(self, other): return self.elm_wise(other, operator.mod)\nfrom\
    \ typing import Iterable \nfrom math import hypot\n\nclass Vec(ElmWiseMixin, tuple,\
    \ Parsable):\n    def __new__(cls, *args):\n        if len(args) == 1 and isinstance(args[0],\
    \ Iterable):\n            return super().__new__(cls, args[0])\n        return\
    \ super().__new__(cls, args)\n\n    def dist(v1: 'Vec', v2: 'Vec'):\n        diff\
    \ = v2-v1\n        return hypot(*diff)\n\n    @classmethod\n    def compile(cls,\
    \ T: type = int, N = None):\n        elm = Parser.compile(T)\n        if N is\
    \ None:\n            def parse(ts: TokenStream):\n                return cls(elm(ts)\
    \ for _ in ts.wait())\n        else:\n            def parse(ts: TokenStream):\n\
    \                return cls(elm(ts) for _ in range(N))\n        return parse\n\
    \  \nfrom math import sqrt\n\nclass Vec2D(Vec):\n\n    def elm_wise(self, other,\
    \ op):\n        if isinstance(other, Number):\n            return Vec2D(op(self[0],\
    \ other), op(self[1], other))\n        if isinstance(other, Sequence):\n     \
    \       return Vec2D(op(self[0], other[0]), op(self[1], other[1]))\n        raise\
    \ ValueError(\"Operand must be a number or a tuple of the same length\")\n\n \
    \   def dist(v1: 'Vec', v2: 'Vec'):\n        dx, dy = v2[0]-v1[0], v2[1]-v1[1]\n\
    \        return sqrt(dx*dx+dy*dy)\n    \n    def rot90(vec):\n        x,y = vec\n\
    \        return Vec2D(-y,x)\n    \n    def rot180(vec):\n        x,y = vec\n \
    \       return Vec2D(-x,-y)\n    \n    def rot270(vec):\n        x,y = vec\n \
    \       return Vec2D(y,-x)\n    \n    def flip_x(vec):\n        x,y = vec\n  \
    \      return Vec2D(-x,y)\n    \n    def flip_y(vec):\n        x,y = vec\n   \
    \     return Vec2D(x,-y)\n    \n    @classmethod\n    def compile(cls, T: type\
    \ = int):\n        elm = Parser.compile(T)\n        def parse(ts: TokenStream):\n\
    \            return cls(elm(ts), elm(ts))\n        return parse\n\n"
  code: "import cp_library.math.__header__\n\nfrom cp_library.io.parser_cls import\
    \ Parser, TokenStream\nfrom cp_library.math.vec_cls import Vec\nfrom numbers import\
    \ Number\nfrom typing import Sequence\nfrom math import sqrt\n\nclass Vec2D(Vec):\n\
    \n    def elm_wise(self, other, op):\n        if isinstance(other, Number):\n\
    \            return Vec2D(op(self[0], other), op(self[1], other))\n        if\
    \ isinstance(other, Sequence):\n            return Vec2D(op(self[0], other[0]),\
    \ op(self[1], other[1]))\n        raise ValueError(\"Operand must be a number\
    \ or a tuple of the same length\")\n\n    def dist(v1: 'Vec', v2: 'Vec'):\n  \
    \      dx, dy = v2[0]-v1[0], v2[1]-v1[1]\n        return sqrt(dx*dx+dy*dy)\n \
    \   \n    def rot90(vec):\n        x,y = vec\n        return Vec2D(-y,x)\n   \
    \ \n    def rot180(vec):\n        x,y = vec\n        return Vec2D(-x,-y)\n   \
    \ \n    def rot270(vec):\n        x,y = vec\n        return Vec2D(y,-x)\n    \n\
    \    def flip_x(vec):\n        x,y = vec\n        return Vec2D(-x,y)\n    \n \
    \   def flip_y(vec):\n        x,y = vec\n        return Vec2D(x,-y)\n    \n  \
    \  @classmethod\n    def compile(cls, T: type = int):\n        elm = Parser.compile(T)\n\
    \        def parse(ts: TokenStream):\n            return cls(elm(ts), elm(ts))\n\
    \        return parse\n\n"
  dependsOn:
  - cp_library/io/parser_cls.py
  - cp_library/math/vec_cls.py
  - cp_library/math/elm_wise_mixin.py
  isVerificationFile: false
  path: cp_library/math/vec2d_cls.py
  requiredBy: []
  timestamp: '2024-11-15 01:34:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc189_e_vec2d.test.py
  - test/abc274_e_vec2d.test.py
documentation_of: cp_library/math/vec2d_cls.py
layout: document
redirect_from:
- /library/cp_library/math/vec2d_cls.py
- /library/cp_library/math/vec2d_cls.py.html
title: cp_library/math/vec2d_cls.py
---
