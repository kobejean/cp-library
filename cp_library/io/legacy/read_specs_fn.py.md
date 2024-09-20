---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_1_c_floyd_warshall.test.py
    title: test/grl_1_c_floyd_warshall.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_a_kruskal_heap.test.py
    title: test/grl_2_a_kruskal_heap.test.py
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
    \nimport sys\nfrom typing import Type, TypeVar\n\nT = TypeVar('T')\ndef read(spec:\
    \ Type[T]|T=[int]) -> T:\n    stream = TokenStream(sys.stdin)\n    parser = Parser.compile(spec)\n\
    \    return parser(stream)\n\n\nimport typing\nfrom collections import deque\n\
    from numbers import Number\nfrom typing import Callable, Collection, Iterator,\
    \ TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self, stream = sys.stdin):\n\
    \        self.stream = stream\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
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
    \    def compile(cls):\n        return lambda ts: cls(next(ts))\n"
  code: "import cp_library.io.__init__\n\nimport sys\nfrom typing import Type, TypeVar\n\
    \nT = TypeVar('T')\ndef read(spec: Type[T]|T=[int]) -> T:\n    stream = TokenStream(sys.stdin)\n\
    \    parser = Parser.compile(spec)\n    return parser(stream)\n\nfrom cp_library.io.parser_cls\
    \ import Parser, TokenStream"
  dependsOn:
  - cp_library/io/parser_cls.py
  isVerificationFile: false
  path: cp_library/io/legacy/read_specs_fn.py
  requiredBy: []
  timestamp: '2024-09-21 04:14:27+09:00'
  verificationStatus: LIBRARY_ALL_AC
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
