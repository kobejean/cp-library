---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc261_g_mo.test.py
    title: test/abc261_g_mo.test.py
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
    from math import isqrt\n\n\nimport sys\nimport typing\nfrom collections import\
    \ deque\nfrom numbers import Number\nfrom types import GenericAlias \nfrom typing\
    \ import Callable, Collection, Iterator, TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n\
    \    stream = sys.stdin\n\n    def __init__(self):\n        self.queue = deque()\n\
    \n    def __next__(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self.line())\n        while self.queue: yield\n\
    \        \n    def line(self):\n        assert not self.queue\n        return\
    \ TokenStream.stream.readline().split()\n\nclass CharStream(TokenStream):\n  \
    \  def line(self):\n        assert not self.queue\n        return next(TokenStream.stream).rstrip()\n\
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
    \            return cls(next(ts))\n        return parser\nfrom typing import Iterable\n\
    \nclass Mo(list, Parsable):\n    \"\"\"\n    Mo[Q: int, N: int, T: type = tuple[int,\
    \ int]]\n    \"\"\"\n    def __init__(self, queries: Iterable[tuple[int, int]],\
    \ N: int):\n        # Initialize with original queries and their indices\n   \
    \     B = isqrt(N)\n        queries = [\n            (b, -r, i, l, r) if (b :=\
    \ l//B) & 2 else (b, r, i, l, r)\n            for i, (l, r) in enumerate(queries)\n\
    \        ]\n        self.Q = len(queries)\n        self.queries = queries\n\n\
    \    def add(self, i):\n        pass\n\n    def remove(self, i):\n        pass\n\
    \n    def answer(self, i, l, r):\n        pass\n    \n    def solve(self):\n \
    \       self.queries.sort()\n\n        curr_l = curr_r = 0\n        ans = [0]*self.Q\n\
    \        \n        for _, _, qid, l, r in self.queries:\n            if r > curr_r:\n\
    \                for i in range(curr_r, r):\n                    self.add(i)\n\
    \n            if l < curr_l:\n                for i in range(curr_l-1, l-1, -1):\n\
    \                    self.add(i)\n\n            if l > curr_l:\n             \
    \   for i in range(curr_l, l):\n                    self.remove(i)\n\n       \
    \     if r < curr_r:\n                for i in range(curr_r-1, r-1, -1):\n   \
    \                 self.remove(i)\n            ans[qid] = self.answer(qid, l, r)\n\
    \            \n            curr_l, curr_r = l, r\n        return ans\n\n\n   \
    \ @classmethod\n    def compile(cls, Q: int, N: int, T: type = tuple[-1, int]):\n\
    \        query = Parser.compile(T)\n        def parse(ts: TokenStream):\n    \
    \        return cls((query(ts) for _ in range(Q)), N)\n        return parse\n\n"
  code: "import cp_library.alg.dp.__header__\nfrom math import isqrt\nfrom cp_library.io.parser_cls\
    \ import Parsable, Parser, TokenStream\nfrom typing import Iterable\n\nclass Mo(list,\
    \ Parsable):\n    \"\"\"\n    Mo[Q: int, N: int, T: type = tuple[int, int]]\n\
    \    \"\"\"\n    def __init__(self, queries: Iterable[tuple[int, int]], N: int):\n\
    \        # Initialize with original queries and their indices\n        B = isqrt(N)\n\
    \        queries = [\n            (b, -r, i, l, r) if (b := l//B) & 2 else (b,\
    \ r, i, l, r)\n            for i, (l, r) in enumerate(queries)\n        ]\n  \
    \      self.Q = len(queries)\n        self.queries = queries\n\n    def add(self,\
    \ i):\n        pass\n\n    def remove(self, i):\n        pass\n\n    def answer(self,\
    \ i, l, r):\n        pass\n    \n    def solve(self):\n        self.queries.sort()\n\
    \n        curr_l = curr_r = 0\n        ans = [0]*self.Q\n        \n        for\
    \ _, _, qid, l, r in self.queries:\n            if r > curr_r:\n             \
    \   for i in range(curr_r, r):\n                    self.add(i)\n\n          \
    \  if l < curr_l:\n                for i in range(curr_l-1, l-1, -1):\n      \
    \              self.add(i)\n\n            if l > curr_l:\n                for\
    \ i in range(curr_l, l):\n                    self.remove(i)\n\n            if\
    \ r < curr_r:\n                for i in range(curr_r-1, r-1, -1):\n          \
    \          self.remove(i)\n            ans[qid] = self.answer(qid, l, r)\n   \
    \         \n            curr_l, curr_r = l, r\n        return ans\n\n\n    @classmethod\n\
    \    def compile(cls, Q: int, N: int, T: type = tuple[-1, int]):\n        query\
    \ = Parser.compile(T)\n        def parse(ts: TokenStream):\n            return\
    \ cls((query(ts) for _ in range(Q)), N)\n        return parse\n\n"
  dependsOn:
  - cp_library/io/parser_cls.py
  isVerificationFile: false
  path: cp_library/alg/dp/mo_cls.py
  requiredBy: []
  timestamp: '2024-11-26 21:56:46+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc261_g_mo.test.py
documentation_of: cp_library/alg/dp/mo_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/mo_cls.py
- /library/cp_library/alg/dp/mo_cls.py.html
title: cp_library/alg/dp/mo_cls.py
---
