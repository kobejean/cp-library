---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':x:'
    path: cp_library/math/elm_wise_mixin.py
    title: cp_library/math/elm_wise_mixin.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/slope_cls.py
    title: cp_library/math/slope_cls.py
  - icon: ':x:'
    path: cp_library/math/vec2d_cls.py
    title: cp_library/math/vec2d_cls.py
  - icon: ':warning:'
    path: cp_library/math/vec3d_cls.py
    title: cp_library/math/vec3d_cls.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/atcoder/abc/abc151_f_fbisect_left.test.py
    title: test/atcoder/abc/abc151_f_fbisect_left.test.py
  - icon: ':x:'
    path: test/atcoder/abc/abc189_e_vec2d.test.py
    title: test/atcoder/abc/abc189_e_vec2d.test.py
  - icon: ':x:'
    path: test/atcoder/abc/abc274_e_vec2d.test.py
    title: test/atcoder/abc/abc274_e_vec2d.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\nimport typing\nfrom collections import deque\nfrom numbers import Number\n\
    from types import GenericAlias \nfrom typing import Callable, Collection, Iterator,\
    \ Union\nimport os\nimport sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n\
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
    \ = IOWrapper(sys.stdout)\nfrom typing import TypeVar\n_T = TypeVar('T')\n\nclass\
    \ TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\n    def __init__(self):\n\
    \        self.queue = deque()\n\n    def __next__(self):\n        if not self.queue:\
    \ self.queue.extend(self.line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        return\
    \ TokenStream.stream.readline().split()\n\nclass CharStream(TokenStream):\n  \
    \  def line(self):\n        assert not self.queue\n        return next(TokenStream.stream).rstrip()\n\
    \nParseFn = Callable[[TokenStream],_T]\nclass Parser:\n    def __init__(self,\
    \ spec: Union[type[_T],_T]):\n        self.parse = Parser.compile(spec)\n\n  \
    \  def __call__(self, ts: TokenStream) -> _T:\n        return self.parse(ts)\n\
    \    \n    @staticmethod\n    def compile_type(cls: type[_T], args = ()) -> _T:\n\
    \        if issubclass(cls, Parsable):\n            return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(ts: TokenStream):\n\
    \                return cls(next(ts))              \n            return parse\n\
    \        elif issubclass(cls, tuple):\n            return Parser.compile_tuple(cls,\
    \ args)\n        elif issubclass(cls, Collection):\n            return Parser.compile_collection(cls,\
    \ args)\n        elif callable(cls):\n            def parse(ts: TokenStream):\n\
    \                return cls(next(ts))              \n            return parse\n\
    \        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile(spec: Union[type[_T],_T]=int) -> ParseFn[_T]:\n        if isinstance(spec,\
    \ (type, GenericAlias)):\n            cls = typing.get_origin(spec) or spec\n\
    \            args = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream):\n                return\
    \ cls(next(ts)) + offset\n            return parse\n        elif isinstance(args\
    \ := spec, tuple):      \n            return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection):  \n            return\
    \ Parser.compile_collection(type(spec), args)\n        elif isinstance(fn := spec,\
    \ Callable): \n            def parse(ts: TokenStream):\n                return\
    \ fn(next(ts))\n            return parse\n        else:\n            raise NotImplementedError()\n\
    \n    @staticmethod\n    def compile_line(cls: _T, spec=int) -> ParseFn[_T]:\n\
    \        if spec is int:\n            fn = Parser.compile(spec)\n            def\
    \ parse(ts: TokenStream):\n                return cls((int(token) for token in\
    \ ts.line()))\n            return parse\n        else:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream):\n                return cls((fn(ts) for\
    \ _ in ts.wait()))\n            return parse\n\n    @staticmethod\n    def compile_repeat(cls:\
    \ _T, spec, N) -> ParseFn[_T]:\n        fn = Parser.compile(spec)\n        def\
    \ parse(ts: TokenStream):\n            return cls((fn(ts) for _ in range(N)))\n\
    \        return parse\n\n    @staticmethod\n    def compile_children(cls: _T,\
    \ specs) -> ParseFn[_T]:\n        fns = tuple((Parser.compile(spec) for spec in\
    \ specs))\n        def parse(ts: TokenStream):\n            return cls((fn(ts)\
    \ for fn in fns))  \n        return parse\n            \n    @staticmethod\n \
    \   def compile_tuple(cls: type[_T], specs) -> ParseFn[_T]:\n        if isinstance(specs,\
    \ (tuple,list)) and len(specs) == 2 and specs[1] is ...:\n            return Parser.compile_line(cls,\
    \ specs[0])\n        else:\n            return Parser.compile_children(cls, specs)\n\
    \n    @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 \n\
    \            and isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls,\
    \ specs[0], specs[1])\n        else:\n            raise NotImplementedError()\n\
    \nclass Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(ts:\
    \ TokenStream):\n            return cls(next(ts))\n        return parser\nfrom\
    \ math import hypot\n\nimport operator\nfrom typing import Sequence\n\nclass ElmWiseMixin:\n\
    \    def elm_wise(self, other, op):\n        if isinstance(other, Number):\n \
    \           return type(self)(op(x, other) for x in self)\n        if isinstance(other,\
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
    from typing import Iterable \n\nclass Vec(ElmWiseMixin, tuple, Parsable):\n  \
    \  def __new__(cls, *args):\n        if len(args) == 1 and isinstance(args[0],\
    \ Iterable):\n            return super().__new__(cls, args[0])\n        return\
    \ super().__new__(cls, args)\n\n    @classmethod\n    def compile(cls, T: type\
    \ = int, N = None):\n        elm = Parser.compile(T)\n        if N is None:\n\
    \            def parse(ts: TokenStream):\n                return cls(elm(ts) for\
    \ _ in ts.wait())\n        else:\n            def parse(ts: TokenStream):\n  \
    \              return cls(elm(ts) for _ in range(N))\n        return parse\n  "
  dependsOn:
  - cp_library/io/parser_cls.py
  - cp_library/math/elm_wise_mixin.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/math/vec_cls.py
  requiredBy:
  - cp_library/math/vec3d_cls.py
  - cp_library/math/slope_cls.py
  - cp_library/math/vec2d_cls.py
  timestamp: '2025-01-16 09:57:28+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/atcoder/abc/abc151_f_fbisect_left.test.py
  - test/atcoder/abc/abc189_e_vec2d.test.py
  - test/atcoder/abc/abc274_e_vec2d.test.py
documentation_of: cp_library/math/vec_cls.py
layout: document
redirect_from:
- /library/cp_library/math/vec_cls.py
- /library/cp_library/math/vec_cls.py.html
title: cp_library/math/vec_cls.py
---
