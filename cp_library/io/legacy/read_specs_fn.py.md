---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/grl_1_c_floyd_warshall.test.py
    title: test/grl_1_c_floyd_warshall.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_a_kruskal_heap.test.py
    title: test/grl_2_a_kruskal_heap.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nimport sys\nfrom typing import Type, TypeVar\n\nT = TypeVar('T')\ndef read(spec:\
    \ Type[T]|T=[int]) -> T:\n    stream = TokenStream(sys.stdin)\n    parser = Parser.compile(spec)\n\
    \    return parser(stream)\n\n\nimport typing\nfrom collections import deque\n\
    from numbers import Number\nfrom typing import Callable, Collection, Iterator,\
    \ TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self, stream\
    \ = sys.stdin):\n        self.stream = stream\n        self.queue = deque()\n\n\
    \    def __next__(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self.line())\n        while self.queue: yield\n\
    \        \n    def line(self):\n        assert not self.queue\n        return\
    \ next(self.stream).rstrip().split()\n        \nT = TypeVar('T')\nParseFn: TypeAlias\
    \ = Callable[[TokenStream],T]\nclass Parser:\n    def __init__(self, spec: type[T]|T):\n\
    \        self.parse = Parser.compile(spec)\n\n    def __call__(self, ts: TokenStream)\
    \ -> T:\n        return self.parse(ts)\n    \n    @staticmethod\n    def compile_type(cls:\
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
    \        # @parse_stride(stride=inf)\n        def parse(ts: TokenStream):\n  \
    \          return cls(fn(ts) for _ in ts.wait())\n        return parse\n\n   \
    \ @staticmethod\n    def compile_repeat(cls: T, spec, N) -> ParseFn[T]:\n    \
    \    fn = Parser.compile(spec)\n        # @parse_stride(stride=fn.stride*N)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in range(N))\n\
    \        return parse\n\n    @staticmethod\n    def compile_children(cls: T, specs)\
    \ -> ParseFn[T]:\n        fns = tuple(Parser.compile(spec) for spec in specs)\
    \ \n        # @parse_stride(stride=sum(fn.stride for fn in fns))\n        def\
    \ parse(ts: TokenStream):\n            return cls(fn(ts) for fn in fns)  \n  \
    \      return parse\n\n    @staticmethod\n    def compile_tuple(cls: type[T],\
    \ specs) -> ParseFn[T]:\n        match specs:\n            case [spec, end] if\
    \ end is ...:\n                return Parser.compile_line(cls, spec)\n       \
    \     case specs:   \n                return Parser.compile_children(cls, specs)\n\
    \    \n    @staticmethod\n    def compile_collection(cls, specs):\n        match\
    \ specs:\n            case [ ] | [_] | set():\n                return Parser.compile_line(cls,\
    \ *specs)\n            case [spec, int() as n]:\n                return Parser.compile_repeat(cls,\
    \ spec, n)\n            case _:\n                raise NotImplementedError()\n\
    \n        \nclass Parsable:\n    @classmethod\n    def compile(cls):\n       \
    \ # @parse_stride(stride=1)\n        def parser(ts: TokenStream):\n          \
    \  return cls(next(ts))\n        return parser\n"
  code: "import cp_library.io.__header__\n\nimport sys\nfrom typing import Type, TypeVar\n\
    \nT = TypeVar('T')\ndef read(spec: Type[T]|T=[int]) -> T:\n    stream = TokenStream(sys.stdin)\n\
    \    parser = Parser.compile(spec)\n    return parser(stream)\n\nfrom cp_library.io.parser_cls\
    \ import Parser, TokenStream"
  dependsOn:
  - cp_library/io/parser_cls.py
  isVerificationFile: false
  path: cp_library/io/legacy/read_specs_fn.py
  requiredBy: []
  timestamp: '2024-09-21 16:44:49+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/grl_1_c_floyd_warshall.test.py
  - test/grl_2_a_kruskal_heap.test.py
documentation_of: cp_library/io/legacy/read_specs_fn.py
layout: document
redirect_from:
- /library/cp_library/io/legacy/read_specs_fn.py
- /library/cp_library/io/legacy/read_specs_fn.py.html
title: cp_library/io/legacy/read_specs_fn.py
---