---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "from math import prod\nfrom typing import Container, Iterable\n\n\
    '''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\n\nimport\
    \ sys\nimport typing\nfrom collections import deque\nfrom numbers import Number\n\
    from typing import Callable, Collection, Iterator, TypeAlias, TypeVar\n\nclass\
    \ TokenStream(Iterator):\n    def __init__(self, stream = sys.stdin):\n      \
    \  self.stream = stream\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return next(self.stream).rstrip().split()\n\nclass CharStream(Iterator):\n\
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
    \ parser\n\nclass grid2d(Parsable, Container):\n\n    def __init__(self, shape:\
    \ tuple[int, int], data = 0):\n        self.shape = shape\n        self.size =\
    \ prod(shape)\n        if isinstance(data, Iterable) and not isinstance(data,\
    \ str):\n            self.data = list(elm for row in data for elm in row)\n  \
    \      else:\n            self.data = [data] * (self.size)\n    \n    @classmethod\n\
    \    def compile(cls, shape: tuple[int, int], T: type = int):\n        elm = Parser.compile(T)\n\
    \        def parse(ts: TokenStream):\n            obj = cls.__new__(cls)\n   \
    \         obj.shape = shape\n            obj.size = prod(shape)\n            obj.data\
    \ = list(elm(ts) for _ in range(obj.size))\n            return obj\n        return\
    \ parse\n    \n    def __contains__(self, x: object) -> bool:\n        return\
    \ x in self.data\n    \n    def __getitem__(self, key: tuple[int, int]):\n   \
    \     i, j = key\n        return self.data[i * self.shape[1] + j]\n    \n    def\
    \ __setitem__(self, key: tuple[int, int], value):\n        i, j = key\n      \
    \  self.data[i * self.shape[1] + j] = value\n    \n    def __repr__(self) -> str:\n\
    \        (N, M), data = self.shape, self.data\n        return '\\n'.join(' '.join(str(data[j])\
    \ for j in range(i,i+M)) for i in range(0,N*M,M))\n"
  code: "from math import prod\nfrom typing import Container, Iterable\n\nfrom cp_library.io.parser_cls\
    \ import Parsable, Parser, TokenStream\n\nclass grid2d(Parsable, Container):\n\
    \n    def __init__(self, shape: tuple[int, int], data = 0):\n        self.shape\
    \ = shape\n        self.size = prod(shape)\n        if isinstance(data, Iterable)\
    \ and not isinstance(data, str):\n            self.data = list(elm for row in\
    \ data for elm in row)\n        else:\n            self.data = [data] * (self.size)\n\
    \    \n    @classmethod\n    def compile(cls, shape: tuple[int, int], T: type\
    \ = int):\n        elm = Parser.compile(T)\n        def parse(ts: TokenStream):\n\
    \            obj = cls.__new__(cls)\n            obj.shape = shape\n         \
    \   obj.size = prod(shape)\n            obj.data = list(elm(ts) for _ in range(obj.size))\n\
    \            return obj\n        return parse\n    \n    def __contains__(self,\
    \ x: object) -> bool:\n        return x in self.data\n    \n    def __getitem__(self,\
    \ key: tuple[int, int]):\n        i, j = key\n        return self.data[i * self.shape[1]\
    \ + j]\n    \n    def __setitem__(self, key: tuple[int, int], value):\n      \
    \  i, j = key\n        self.data[i * self.shape[1] + j] = value\n    \n    def\
    \ __repr__(self) -> str:\n        (N, M), data = self.shape, self.data\n     \
    \   return '\\n'.join(' '.join(str(data[j]) for j in range(i,i+M)) for i in range(0,N*M,M))\n"
  dependsOn:
  - cp_library/io/parser_cls.py
  isVerificationFile: false
  path: cp_library/ds/grid.py
  requiredBy: []
  timestamp: '2024-10-04 19:59:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/grid.py
layout: document
redirect_from:
- /library/cp_library/ds/grid.py
- /library/cp_library/ds/grid.py.html
title: cp_library/ds/grid.py
---
