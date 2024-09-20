---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "\nfrom math import inf\nfrom numbers import Number\nfrom typing import\
    \ Collection, Iterable, Iterator\nimport typing\n\nfrom cp_library.io.parsable_cls\
    \ import Parsable\n\nclass Parser:\n    def __init__(self, fn, *children):\n \
    \       if isinstance(fn, Parser):\n            raise\n        self.unpack = True\n\
    \        self.fn, self.children = fn, children\n        if len(children) == 1\
    \ and isinstance(children[0], Iterable):\n            self.children = children[0]\n\
    \            self.unpack = False\n        self.stride = sum((c.stride for c in\
    \ self.children if isinstance(c,Parser)))\n        if not children:\n        \
    \    self.stride = 1\n        print(self.fn, self.stride, self.children)\n\n\n\
    \    def __call__(self, s):\n        if not self.children:\n            return\
    \ self.fn(s.token())\n        else:\n            nargs = tuple(c(s) if isinstance(c,Parser)\
    \ else c for c in self.children)\n            return self.fn(*nargs) if self.unpack\
    \ else self.fn(nargs)\n        \n    @staticmethod\n    def compile(spec):\n\n\
    \        def compile_tuple(cls, specs):\n            match specs:\n          \
    \      case [spec, end] if end is ...:\n                    return LineParser(cls,\
    \ Parser.compile(spec))\n                case specs:\n                    children\
    \ = tuple(Parser.compile(spec) for spec in specs)               \n           \
    \         return Parser(cls, children)\n                \n        def compile_collection(cls,\
    \ specs) -> list:\n            match specs:\n                case [ ] | [_] |\
    \ set():\n                    return LineParser(cls, Parser.compile(*specs))\n\
    \                case [spec, int() as n]: \n                    elm = Parser.compile(spec)\n\
    \                    return Parser(cls, tuple(elm for _ in range(n)))\n      \
    \          case _:\n                    raise NotImplementedError()\n        \
    \        \n\n        def match_spec(spec, types):\n            if issubclass(cls\
    \ := type(specs := spec), types):\n                return cls, specs\n       \
    \     elif (isinstance(spec, type) and \n                issubclass(cls := typing.get_origin(spec)\
    \ or spec, types)):\n                return cls, (typing.get_args(spec) or tuple())\n\
    \            \n        if args := match_spec(spec, Parsable):\n            cls,\
    \ args = args\n            return cls.compile(*args)\n        elif args := match_spec(spec,\
    \ tuple):      \n            return compile_tuple(*args)\n        elif args :=\
    \ match_spec(spec, Collection): \n            return compile_collection(*args)\n\
    \        elif issubclass(cls := type(offset := spec), Number):         \n    \
    \        return Parser(lambda s: cls(s) + offset)\n        elif callable(cls :=\
    \ spec):\n            return Parser(cls)\n        else:\n            raise NotImplementedError()\n\
    \        \nclass LineParser(Parser):\n    def __init__(self, fn, child):\n   \
    \     super().__init__(fn,child)\n        self.stride = inf\n\n    def __call__(self,\
    \ s):\n        if not self.children:\n            return self.fn(s.line())\n \
    \       elif isinstance(c := self.children[-1], Parser):\n            batches,\
    \ extra = divmod(s.rem(), c.stride)\n            assert extra == 0\n         \
    \   args = (*self.children[:-1], *(c(s) for _ in range(batches)))\n          \
    \  return self.fn(args)\n        raise NotImplementedError()\n\nclass TokenStream:\n\
    \    def __init__(self, stream: Iterator[str]):\n        self.stream = stream\n\
    \        self.tokens = []\n        self.pos = 0\n\n    def fetch(self):\n    \
    \    if self.pos >= len(self.tokens):\n            self.pos = 0\n            self.tokens\
    \ = next(self.stream).rstrip().split()\n\n    def token(self):\n        self.fetch()\n\
    \        token = self.tokens[self.pos]\n        self.pos += 1\n        return\
    \ token\n    \n    def line(self):\n        self.fetch()\n        line = self.tokens[self.pos:]\n\
    \        self.pos = len(self.tokens)\n        return line\n    \n    def rem(self):\n\
    \        self.fetch()\n        return len(self.tokens) - self.pos\n"
  code: "\nfrom math import inf\nfrom numbers import Number\nfrom typing import Collection,\
    \ Iterable, Iterator\nimport typing\n\nfrom cp_library.io.parsable_cls import\
    \ Parsable\n\nclass Parser:\n    def __init__(self, fn, *children):\n        if\
    \ isinstance(fn, Parser):\n            raise\n        self.unpack = True\n   \
    \     self.fn, self.children = fn, children\n        if len(children) == 1 and\
    \ isinstance(children[0], Iterable):\n            self.children = children[0]\n\
    \            self.unpack = False\n        self.stride = sum((c.stride for c in\
    \ self.children if isinstance(c,Parser)))\n        if not children:\n        \
    \    self.stride = 1\n        print(self.fn, self.stride, self.children)\n\n\n\
    \    def __call__(self, s):\n        if not self.children:\n            return\
    \ self.fn(s.token())\n        else:\n            nargs = tuple(c(s) if isinstance(c,Parser)\
    \ else c for c in self.children)\n            return self.fn(*nargs) if self.unpack\
    \ else self.fn(nargs)\n        \n    @staticmethod\n    def compile(spec):\n\n\
    \        def compile_tuple(cls, specs):\n            match specs:\n          \
    \      case [spec, end] if end is ...:\n                    return LineParser(cls,\
    \ Parser.compile(spec))\n                case specs:\n                    children\
    \ = tuple(Parser.compile(spec) for spec in specs)               \n           \
    \         return Parser(cls, children)\n                \n        def compile_collection(cls,\
    \ specs) -> list:\n            match specs:\n                case [ ] | [_] |\
    \ set():\n                    return LineParser(cls, Parser.compile(*specs))\n\
    \                case [spec, int() as n]: \n                    elm = Parser.compile(spec)\n\
    \                    return Parser(cls, tuple(elm for _ in range(n)))\n      \
    \          case _:\n                    raise NotImplementedError()\n        \
    \        \n\n        def match_spec(spec, types):\n            if issubclass(cls\
    \ := type(specs := spec), types):\n                return cls, specs\n       \
    \     elif (isinstance(spec, type) and \n                issubclass(cls := typing.get_origin(spec)\
    \ or spec, types)):\n                return cls, (typing.get_args(spec) or tuple())\n\
    \            \n        if args := match_spec(spec, Parsable):\n            cls,\
    \ args = args\n            return cls.compile(*args)\n        elif args := match_spec(spec,\
    \ tuple):      \n            return compile_tuple(*args)\n        elif args :=\
    \ match_spec(spec, Collection): \n            return compile_collection(*args)\n\
    \        elif issubclass(cls := type(offset := spec), Number):         \n    \
    \        return Parser(lambda s: cls(s) + offset)\n        elif callable(cls :=\
    \ spec):\n            return Parser(cls)\n        else:\n            raise NotImplementedError()\n\
    \        \nclass LineParser(Parser):\n    def __init__(self, fn, child):\n   \
    \     super().__init__(fn,child)\n        self.stride = inf\n\n    def __call__(self,\
    \ s):\n        if not self.children:\n            return self.fn(s.line())\n \
    \       elif isinstance(c := self.children[-1], Parser):\n            batches,\
    \ extra = divmod(s.rem(), c.stride)\n            assert extra == 0\n         \
    \   args = (*self.children[:-1], *(c(s) for _ in range(batches)))\n          \
    \  return self.fn(args)\n        raise NotImplementedError()\n\nclass TokenStream:\n\
    \    def __init__(self, stream: Iterator[str]):\n        self.stream = stream\n\
    \        self.tokens = []\n        self.pos = 0\n\n    def fetch(self):\n    \
    \    if self.pos >= len(self.tokens):\n            self.pos = 0\n            self.tokens\
    \ = next(self.stream).rstrip().split()\n\n    def token(self):\n        self.fetch()\n\
    \        token = self.tokens[self.pos]\n        self.pos += 1\n        return\
    \ token\n    \n    def line(self):\n        self.fetch()\n        line = self.tokens[self.pos:]\n\
    \        self.pos = len(self.tokens)\n        return line\n    \n    def rem(self):\n\
    \        self.fetch()\n        return len(self.tokens) - self.pos\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/io/_parser_cls.py
  requiredBy: []
  timestamp: '2024-09-21 04:14:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/io/_parser_cls.py
layout: document
redirect_from:
- /library/cp_library/io/_parser_cls.py
- /library/cp_library/io/_parser_cls.py.html
title: cp_library/io/_parser_cls.py
---
