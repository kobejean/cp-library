---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
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
    \n\nimport sys\nfrom typing import Iterator, Type, TypeVar, overload\n\nimport\
    \ typing\nfrom collections import deque\nfrom numbers import Number\nfrom typing\
    \ import Callable, Collection, Iterator, TypeVar\n\nclass TokenStream(Iterator):\n\
    \    def __init__(self, stream = sys.stdin):\n        self.stream = stream\n \
    \       self.queue = deque()\n\n    def __next__(self):\n        if not self.queue:\
    \ self.queue.extend(self.line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return next(self.stream).rstrip().split()\n    \n  \
    \      \nT = TypeVar('T')\nclass Parser:\n    def __init__(self, spec: type[T]|T):\n\
    \        self.parse = Parser.compile(spec)\n\n    def __call__(self, ts: TokenStream)\
    \ -> T:\n        return self.parse(ts)\n\n    @staticmethod\n    def compile(spec:\
    \ type[T]|T=int) -> Callable[[TokenStream],T]:\n            \n        def compile_tuple(cls,\
    \ specs):\n            match specs:\n                case [spec, end] if end is\
    \ ...: \n                    fn = Parser.compile(spec) \n                    return\
    \ lambda ts: cls(fn(ts) for _ in ts.wait())\n                case specs:\n   \
    \                 fns = tuple(Parser.compile(spec) for spec in specs)        \
    \       \n                    return lambda ts: cls(fn(ts) for fn in fns)\n\n\
    \        def compile_collection(cls, specs) -> list:\n            match specs:\n\
    \                case [ ] | [_] | set():   \n                    fn = Parser.compile(*specs)\
    \       \n                    return lambda ts: cls(fn(ts) for _ in ts.wait())\n\
    \                case [spec, int() as n]: \n                    fn = Parser.compile(spec)\n\
    \                    return lambda ts: cls(fn(ts) for _ in range(n))\n       \
    \         case _:\n                    raise NotImplementedError()\n        \n\
    \        def match_spec(spec, types):\n            if issubclass(cls := type(specs\
    \ := spec), types):\n                return cls, specs\n            elif (isinstance(spec,\
    \ type) and \n                issubclass(cls := typing.get_origin(spec) or spec,\
    \ types)):\n                return cls, (typing.get_args(spec) or tuple())\n \
    \           \n        if args := match_spec(spec, Parsable):\n            cls,\
    \ args = args\n            return cls.compile(*args)\n        elif issubclass(cls\
    \ := type(offset := spec), Number):         \n            return lambda ts: cls(next(ts))\
    \ + offset\n        elif args := match_spec(spec, tuple):      \n            return\
    \ compile_tuple(*args)\n        elif args := match_spec(spec, Collection): \n\
    \            return compile_collection(*args)\n        elif callable(cls := spec):\
    \                  \n            return lambda ts: cls(next(ts))\n        else:\n\
    \            raise NotImplementedError()\n        \nclass Parsable:\n    @classmethod\n\
    \    def compile(cls):\n        return lambda ts: cls(next(ts))\n\nT = TypeVar('T')\n\
    @overload\ndef read(spec: int|None) -> Iterator[int]: ...\n@overload\ndef read(spec:\
    \ Type[T]|T) -> T: ...\ndef read(spec: Type[T]|T=None):\n    match spec:\n   \
    \     case None:\n            return map(int, input().split())\n        case int(i0):\n\
    \            return (int(s)-i0 for s in input().split())\n        case _:\n  \
    \          stream = TokenStream(sys.stdin)\n            parser = Parser(spec)\n\
    \            return parser(stream)\n\ndef read_edges(M, i0=1):\n    return read(list[tuple[-i0,-i0],\
    \ M])\n"
  code: "import cp_library.io.__init__\n\nfrom cp_library.io.read_specs_fn import\
    \ read\n\ndef read_edges(M, i0=1):\n    return read(list[tuple[-i0,-i0], M])\n"
  dependsOn:
  - cp_library/io/read_specs_fn.py
  - cp_library/io/parser_cls.py
  isVerificationFile: false
  path: cp_library/io/read_edges_fn.py
  requiredBy: []
  timestamp: '2024-09-21 04:14:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/io/read_edges_fn.py
layout: document
redirect_from:
- /library/cp_library/io/read_edges_fn.py
- /library/cp_library/io/read_edges_fn.py.html
title: cp_library/io/read_edges_fn.py
---
