---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':question:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/subset_sum_fn.py
    title: cp_library/math/subset_sum_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc184/tasks/abc184_f
    links:
    - https://atcoder.jp/contests/abc184/tasks/abc184_f
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc184/tasks/abc184_f\n\
    \n\nfrom bisect import bisect_left\n\ndef solve(N, T, A):\n    if N <= 5:\n  \
    \      A = sorted(subset_sum(A))\n        return max_lim(A, T)\n    else:\n  \
    \      mid = N//2\n        B = sorted(subset_sum(A[mid:]))\n        C = sorted(subset_sum(A[:mid]))\n\
    \        ans = 0\n        for b in B:\n            if b > T: break\n         \
    \   ans = max(ans, max_lim(C, T-b)+b)\n        return ans\n    \ndef max_lim(X,\
    \ lim):\n    pi = bisect_left(X, lim+1)-1\n    if 0 <= pi < len(X):\n        return\
    \ X[pi]\n    return 0\n\ndef main():\n    N, T = read(tuple[int, ...])\n    A\
    \ = sorted(read(list[int, N]))\n    ans = solve(N, T, A)\n    print(ans)\n   \
    \ \n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\nimport\
    \ sys\nfrom typing import Type, TypeVar, overload\n\nimport typing\nfrom collections\
    \ import deque\nfrom numbers import Number\nfrom typing import Callable, Collection,\
    \ Iterator, TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self,\
    \ stream = sys.stdin):\n        self.stream = stream\n        self.queue = deque()\n\
    \n    def __next__(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self.line())\n        while self.queue: yield\n\
    \        \n    def line(self):\n        assert not self.queue\n        return\
    \ next(self.stream).rstrip().split()\n\nclass CharStream(TokenStream):\n    def\
    \ line(self):\n        assert not self.queue\n        return next(self.stream).rstrip()\n\
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
    \ parser\n\nT = TypeVar('T')\n@overload\ndef read(spec: int|None) -> list[int]:\
    \ ...\n@overload\ndef read(spec: Type[T]|T, char=False) -> T: ...\ndef read(spec:\
    \ Type[T]|T=None, char=False):\n    match spec, char:\n        case None, False:\n\
    \            return list(map(int, input().split()))\n        case int(offset),\
    \ False:\n            return [int(s)+offset for s in input().split()]\n      \
    \  case _, _:\n            if char:\n                stream = CharStream(sys.stdin)\n\
    \            else:\n                stream = TokenStream(sys.stdin)\n        \
    \    parser: T = Parser.compile(spec)\n            return parser(stream)\n\n\n\
    def subset_sum(A):\n    dp = [0]*(1 << len(A))\n    for i,a in enumerate(A):\n\
    \        for mask in range(bit := 1 << i):\n            dp[mask^bit] = dp[mask]\
    \ + a\n    return dp\n\nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc184/tasks/abc184_f\n\
    \n\nfrom bisect import bisect_left\n\ndef solve(N, T, A):\n    if N <= 5:\n  \
    \      A = sorted(subset_sum(A))\n        return max_lim(A, T)\n    else:\n  \
    \      mid = N//2\n        B = sorted(subset_sum(A[mid:]))\n        C = sorted(subset_sum(A[:mid]))\n\
    \        ans = 0\n        for b in B:\n            if b > T: break\n         \
    \   ans = max(ans, max_lim(C, T-b)+b)\n        return ans\n    \ndef max_lim(X,\
    \ lim):\n    pi = bisect_left(X, lim+1)-1\n    if 0 <= pi < len(X):\n        return\
    \ X[pi]\n    return 0\n\ndef main():\n    N, T = read(tuple[int, ...])\n    A\
    \ = sorted(read(list[int, N]))\n    ans = solve(N, T, A)\n    print(ans)\n   \
    \ \n\nfrom cp_library.io.read_specs_fn import read\nfrom cp_library.math.subset_sum_fn\
    \ import subset_sum\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/io/read_specs_fn.py
  - cp_library/math/subset_sum_fn.py
  - cp_library/io/parser_cls.py
  isVerificationFile: true
  path: test/abc184_f_subset_sum_fn.test.py
  requiredBy: []
  timestamp: '2024-11-04 21:00:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc184_f_subset_sum_fn.test.py
layout: document
redirect_from:
- /verify/test/abc184_f_subset_sum_fn.test.py
- /verify/test/abc184_f_subset_sum_fn.test.py.html
title: test/abc184_f_subset_sum_fn.test.py
---