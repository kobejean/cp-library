---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/graph/partial_functional_graph_cls.py
    title: cp_library/alg/graph/partial_functional_graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/permutation_cls.py
    title: cp_library/alg/graph/permutation_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc175_d_permutation.test.py
    title: test/abc175_d_permutation.test.py
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
    \ Number\nfrom typing import Callable, Collection, Iterator, TypeAlias, TypeVar\n\
    \nclass TokenStream(Iterator):\n    def __init__(self, stream = sys.stdin):\n\
    \        self.stream = stream\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
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
    \ parser\n\nclass FunctionalGraph(list[int], Parsable):\n    def __init__(F, successors):\n\
    \        super().__init__(successors)\n        F.N = F.M = len(F)\n\n    def find_cycle(P,\
    \ root):\n        slow = fast = root\n        while (slow := P[slow]) != (fast\
    \ := P[P[fast]]):\n            pass\n        \n        cyc = [slow]\n        while\
    \ P[slow] != cyc[0]:\n            slow = P[slow]\n            cyc.append(slow)\n\
    \        return cyc\n    \n    def cycles(P):\n        vis = [False]*P.N\n   \
    \     cycs = []\n        for v in range(P.N):\n            slow = fast = v\n \
    \           while (slow := P[slow]) != (fast := P[P[fast]]) and not vis[fast]:\n\
    \                pass\n            if vis[fast]: continue\n            \n    \
    \        cyc = [slow]\n            vis[slow] = True\n            while P[slow]\
    \ != cyc[0]:\n                slow = P[slow]\n                cyc.append(slow)\n\
    \                vis[slow] = True\n            cycs.append(cyc)\n        return\
    \ cycs\n\n    @classmethod\n    def compile(cls, N: int, shift = -1):\n      \
    \  def parse(ts: TokenStream):\n            return cls(int(next(ts))+shift for\
    \ _ in range(N))\n        return parse\n"
  code: "import cp_library.alg.graph.__header__\n\nfrom cp_library.io.parser_cls import\
    \ Parsable, TokenStream\n\nclass FunctionalGraph(list[int], Parsable):\n    def\
    \ __init__(F, successors):\n        super().__init__(successors)\n        F.N\
    \ = F.M = len(F)\n\n    def find_cycle(P, root):\n        slow = fast = root\n\
    \        while (slow := P[slow]) != (fast := P[P[fast]]):\n            pass\n\
    \        \n        cyc = [slow]\n        while P[slow] != cyc[0]:\n          \
    \  slow = P[slow]\n            cyc.append(slow)\n        return cyc\n    \n  \
    \  def cycles(P):\n        vis = [False]*P.N\n        cycs = []\n        for v\
    \ in range(P.N):\n            slow = fast = v\n            while (slow := P[slow])\
    \ != (fast := P[P[fast]]) and not vis[fast]:\n                pass\n         \
    \   if vis[fast]: continue\n            \n            cyc = [slow]\n         \
    \   vis[slow] = True\n            while P[slow] != cyc[0]:\n                slow\
    \ = P[slow]\n                cyc.append(slow)\n                vis[slow] = True\n\
    \            cycs.append(cyc)\n        return cycs\n\n    @classmethod\n    def\
    \ compile(cls, N: int, shift = -1):\n        def parse(ts: TokenStream):\n   \
    \         return cls(int(next(ts))+shift for _ in range(N))\n        return parse"
  dependsOn:
  - cp_library/io/parser_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/functional_graph_cls.py
  requiredBy:
  - cp_library/alg/graph/permutation_cls.py
  - cp_library/alg/graph/partial_functional_graph_cls.py
  timestamp: '2024-11-05 04:28:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc175_d_permutation.test.py
documentation_of: cp_library/alg/graph/functional_graph_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/functional_graph_cls.py
- /library/cp_library/alg/graph/functional_graph_cls.py.html
title: cp_library/alg/graph/functional_graph_cls.py
---
