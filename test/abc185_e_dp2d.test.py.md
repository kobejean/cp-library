---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/dp2d_cls.py
    title: cp_library/alg/dp/dp2d_cls.py
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
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc185/tasks/abc185_e
    links:
    - https://atcoder.jp/contests/abc185/tasks/abc185_e
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc185/tasks/abc185_e\n\
    \ndef main():\n    N, M = read(tuple[int, ...])\n    A = read(list[int,N])\n \
    \   B = read(list[int,M])\n    \n    dp = DynamicProgramming2D(N+1, M+1)\n   \
    \ dp[0,0] = 0\n    \n    transitions = [\n        Match(1,1,A,B),    # match/mismatch\n\
    \        Edit(0,1),         # insert\n        Edit(1,0),         # delete\n  \
    \  ]\n    \n    dp.solve(transitions)\n    print(dp[N,M])\n    \n\n'''\n\u257A\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n         \
    \    https://kobejean.github.io/cp-library               \n'''\n\nimport sys\n\
    from typing import Type, TypeVar, overload\n\nimport typing\nfrom collections\
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
    \    parser: T = Parser.compile(spec)\n            return parser(stream)\n\nfrom\
    \ typing import TypeVar, Generic\nfrom dataclasses import dataclass\nfrom math\
    \ import inf\n\nT = TypeVar('T')\n\n@dataclass\nclass Transition2D(Generic[T]):\n\
    \    di: int\n    dj: int\n    \n    def __call__(self, i: int, j: int, src_val:\
    \ T, dest_val: T) -> T:\n        \"\"\"Override this to implement transition logic\"\
    \"\"\n        return src_val  # Default no-op\n\nclass DynamicProgramming2D(Generic[T]):\n\
    \    def __init__(self, rows: int, cols: int, default: T = inf):\n        self.rows\
    \ = rows\n        self.cols = cols\n        self.table = [[default] * cols for\
    \ _ in range(rows)]\n    \n    def __getitem__(self, pos: tuple[int, int]) ->\
    \ T:\n        i, j = pos\n        return self.table[i][j]\n    \n    def __setitem__(self,\
    \ pos: tuple[int, int], value: T) -> None:\n        i, j = pos\n        self.table[i][j]\
    \ = value\n    \n    def solve(self, transitions: list[Transition2D[T]]) -> None:\n\
    \        for i in range(self.rows):\n            for j in range(self.cols):\n\
    \                curr_val = self.table[i][j]\n                for trans in transitions:\n\
    \                    ni, nj = i + trans.di, j + trans.dj\n                   \
    \ if 0 <= ni < self.rows and 0 <= nj < self.cols:\n                        self.table[ni][nj]\
    \ = trans(i, j, curr_val, self.table[ni][nj])\n\n\n@dataclass\nclass Match(Transition2D[int]):\n\
    \    A: list[int]\n    B: list[int]\n\n    def __call__(self, i: int, j: int,\
    \ src_val: int, dest_val: int) -> int:\n        return min(dest_val, src_val +\
    \ (self.A[i] != self.B[j]))\n\nclass Edit(Transition2D[int]):\n    def __call__(self,\
    \ i: int, j: int, src_val: int, dest_val: int) -> int:\n        return min(dest_val,\
    \ src_val + 1)\n    \nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc185/tasks/abc185_e\n\
    \ndef main():\n    N, M = read(tuple[int, ...])\n    A = read(list[int,N])\n \
    \   B = read(list[int,M])\n    \n    dp = DynamicProgramming2D(N+1, M+1)\n   \
    \ dp[0,0] = 0\n    \n    transitions = [\n        Match(1,1,A,B),    # match/mismatch\n\
    \        Edit(0,1),         # insert\n        Edit(1,0),         # delete\n  \
    \  ]\n    \n    dp.solve(transitions)\n    print(dp[N,M])\n    \n\nfrom cp_library.io.read_specs_fn\
    \ import read\nfrom cp_library.alg.dp.dp2d_cls import DynamicProgramming2D, Transition2D\n\
    \nfrom dataclasses import dataclass\n\n@dataclass\nclass Match(Transition2D[int]):\n\
    \    A: list[int]\n    B: list[int]\n\n    def __call__(self, i: int, j: int,\
    \ src_val: int, dest_val: int) -> int:\n        return min(dest_val, src_val +\
    \ (self.A[i] != self.B[j]))\n\nclass Edit(Transition2D[int]):\n    def __call__(self,\
    \ i: int, j: int, src_val: int, dest_val: int) -> int:\n        return min(dest_val,\
    \ src_val + 1)\n    \nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/io/read_specs_fn.py
  - cp_library/alg/dp/dp2d_cls.py
  - cp_library/io/parser_cls.py
  isVerificationFile: true
  path: test/abc185_e_dp2d.test.py
  requiredBy: []
  timestamp: '2024-11-05 04:28:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc185_e_dp2d.test.py
layout: document
redirect_from:
- /verify/test/abc185_e_dp2d.test.py
- /verify/test/abc185_e_dp2d.test.py.html
title: test/abc185_e_dp2d.test.py
---
