---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/cht_monotone_add_min_cls.py
    title: cp_library/ds/cht_monotone_add_min_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':question:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/dp/tasks/dp_z
    links:
    - https://atcoder.jp/contests/dp/tasks/dp_z
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_z\n\
    \ndef main():\n    N, C = read()\n    H = read([])\n    dp = 0\n    cht = CHTMonotoneAddMin()\n\
    \n    for i in range(N-1):\n        m = -2*H[i]\n        b = H[i]**2 + dp\n  \
    \      cht.insert(m,b)\n        i+=1\n        dp = cht.min(H[i]) + H[i]**2 + C\n\
    \n    print(dp)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n             https://kobejean.github.io/cp-library       \
    \        \n'''\n\nfrom bisect import bisect_left\n\nclass CHTMonotoneAddMin:\n\
    \    def __init__(self):\n        self.hull = []\n\n    def insert(self, m: int,\
    \ b: int) -> None:\n        # Remove lines with greater or equal slopes (maintaining\
    \ monotonicity)\n        while self.hull and self.hull[-1][0] <= m:\n        \
    \    self.hull.pop()\n\n        def is_obsolete():\n            (m1, b1), (m2,\
    \ b2) = self.hull[-2], self.hull[-1]\n            return (b - b1) * (m1 - m2)\
    \ <= (b2 - b1) * (m1 - m)\n        \n        # Remove lines that are no longer\
    \ part of the lower envelope\n        while len(self.hull) >= 2 and is_obsolete():\n\
    \            self.hull.pop()\n        \n        self.hull.append((m, b))\n\n \
    \   def min(self, x: int) -> int:\n        def eval(i):\n            m, b = self.hull[i]\n\
    \            return m * x + b\n        def key(i):\n            m1, b1 = self.hull[i]\n\
    \            m2, b2 = self.hull[i+1]\n            return (m2-m1)*x + (b2-b1)\n\
    \        return eval(bisect_left(range(len(self.hull) - 1), 0, key=key))\n\n\n\
    import sys\nfrom typing import Iterator, Type, TypeVar, overload\n\nimport typing\n\
    from collections import deque\nfrom numbers import Number\nfrom typing import\
    \ Callable, Collection, Iterator, TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n\
    \    def __init__(self, stream = sys.stdin):\n        self.stream = stream\n \
    \       self.queue = deque()\n\n    def __next__(self):\n        if not self.queue:\
    \ self.queue.extend(self.line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return next(self.stream).rstrip().split()\n        \n\
    T = TypeVar('T')\nParseFn: TypeAlias = Callable[[TokenStream],T]\nclass Parser:\n\
    \    def __init__(self, spec: type[T]|T):\n        self.parse = Parser.compile(spec)\n\
    \n    def __call__(self, ts: TokenStream) -> T:\n        return self.parse(ts)\n\
    \    \n    @staticmethod\n    def compile_type(cls: type[T], args = ()) -> T:\n\
    \        if issubclass(cls, Parsable):\n            return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(ts: TokenStream):\n\
    \                return cls(next(ts))              \n            return parse\n\
    \        elif issubclass(cls, tuple):\n            return Parser.compile_tuple(cls,\
    \ args)\n        elif issubclass(cls, Collection):\n            return Parser.compile_collection(cls,\
    \ args)\n        elif callable(cls):\n            def parse(ts: TokenStream):\n\
    \                return cls(next(ts))              \n            return parse\n\
    \        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile(spec: type[T]|T=int) -> ParseFn[T]:\n        if isinstance(spec,\
    \ type):\n            cls = typing.get_origin(spec) or spec\n            args\
    \ = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream):\n                return\
    \ cls(next(ts)) + offset\n            return parse\n        elif isinstance(args\
    \ := spec, tuple):      \n            return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection):  \n            return\
    \ Parser.compile_collection(type(spec), args)\n        else:\n            raise\
    \ NotImplementedError()\n    \n    @staticmethod\n    def compile_line(cls: T,\
    \ spec=int) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        # @parse_stride(stride=inf)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in ts.wait())\n\
    \        return parse\n\n    @staticmethod\n    def compile_repeat(cls: T, spec,\
    \ N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        # @parse_stride(stride=fn.stride*N)\n\
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
    \  return cls(next(ts))\n        return parser\n\nT = TypeVar('T')\n@overload\n\
    def read(spec: int|None) -> Iterator[int]: ...\n@overload\ndef read(spec: Type[T]|T)\
    \ -> T: ...\ndef read(spec: Type[T]|T=None):\n    match spec:\n        case None:\n\
    \            return map(int, input().split())\n        case int(i0):\n       \
    \     return (int(s)-i0 for s in input().split())\n        case _:\n         \
    \   stream = TokenStream(sys.stdin)\n            parser: T = Parser.compile(spec)\n\
    \            return parser(stream)\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_z\n\
    \ndef main():\n    N, C = read()\n    H = read([])\n    dp = 0\n    cht = CHTMonotoneAddMin()\n\
    \n    for i in range(N-1):\n        m = -2*H[i]\n        b = H[i]**2 + dp\n  \
    \      cht.insert(m,b)\n        i+=1\n        dp = cht.min(H[i]) + H[i]**2 + C\n\
    \n    print(dp)\n\nfrom cp_library.ds.cht_monotone_add_min_cls import CHTMonotoneAddMin\n\
    from cp_library.io.read_specs_fn import read\n\nif __name__ == '__main__':\n \
    \   main()"
  dependsOn:
  - cp_library/ds/cht_monotone_add_min_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/io/parser_cls.py
  isVerificationFile: true
  path: test/dp_z_cht_monotone_add_min.test.py
  requiredBy: []
  timestamp: '2024-09-21 16:44:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/dp_z_cht_monotone_add_min.test.py
layout: document
redirect_from:
- /verify/test/dp_z_cht_monotone_add_min.test.py
- /verify/test/dp_z_cht_monotone_add_min.test.py.html
title: test/dp_z_cht_monotone_add_min.test.py
---
