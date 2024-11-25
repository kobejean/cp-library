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
    from typing import Type, TypeVar, overload\nfrom io import TextIOBase\n\nimport\
    \ typing\nfrom collections import deque\nfrom numbers import Number\nfrom types\
    \ import GenericAlias \nfrom typing import Callable, Collection, Iterator, TypeAlias,\
    \ TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self, stream: TextIOBase\
    \ = sys.stdin):\n        self.queue = deque()\n        self.stream = stream\n\n\
    \    def __next__(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self.line())\n        while self.queue: yield\n\
    \        \n    def line(self):\n        assert not self.queue\n        return\
    \ sys.stdin.readline().split()\n\n    def n_uints(self, n: int, shift = 0, max_digits:\
    \ int = 20):\n        # sync buffers\n        tokens: list[str] = []\n       \
    \ while (lim := sys.stdin.buffer.tell() - sys.stdin.tell()) and len(tokens) <\
    \ n:\n            residual_str: str = sys.stdin.readline(lim)\n            tokens.extend(residual_str.split())\n\
    \        \n        result = [0] * n\n        pos = 0\n        \n        # Process\
    \ residual string and check for partial token\n        partial = None\n      \
    \  if tokens:\n            if not residual_str[-1].isspace():\n              \
    \  partial = tokens.pop()\n            for pos, token in enumerate(tokens):\n\
    \                result[pos] = int(token)+shift\n            pos += 1\n      \
    \  # Process remaining data token by token\n        stdin_buffer = sys.stdin.buffer\n\
    \        num = int(partial) if partial else 0\n        have_digit = partial is\
    \ not None\n\n        original_chunk_size = sys.stdin._CHUNK_SIZE\n        sys.stdin._CHUNK_SIZE\
    \ = max(original_chunk_size, max_digits * (n - pos))\n        \n        while\
    \ pos < n:\n            byte = stdin_buffer.read(1)\n\n            match byte[0]:\n\
    \                case 10 | 32:\n                    if have_digit:\n         \
    \               result[pos] = num+shift\n                        pos += 1\n  \
    \                      num = 0\n                        have_digit = False\n \
    \               case char:  # digit\n                    num = (num * 10) + (char\
    \ - 48)\n                    have_digit = True\n\n        if have_digit:\n   \
    \         result[pos] = num+shift\n            pos += 1\n\n        sys.stdin._CHUNK_SIZE\
    \ = original_chunk_size \n        if pos < n:\n            raise EOFError(f\"\
    Only found {pos} numbers, expected {n}\")\n            \n        return result\n\
    \    \n    def n_ints(self, n: int, shift = 0, max_digits: int = 20):\n      \
    \  # sync buffers\n        tokens: list[str] = []\n        while (lim := sys.stdin.buffer.tell()\
    \ - sys.stdin.tell()) and len(tokens) < n:\n            residual_str: str = sys.stdin.readline(lim)\n\
    \            tokens.extend(residual_str.split())\n        \n        result = [0]\
    \ * n\n        pos = 0\n        \n        # Process residual string and check\
    \ for partial token\n        partial = None\n        if tokens:\n            if\
    \ not residual_str[-1].isspace():\n                partial = tokens.pop()\n  \
    \          for pos, token in enumerate(tokens):\n                result[pos] =\
    \ int(token)+shift\n            pos += 1\n        # Process remaining data token\
    \ by token\n        stdin_buffer = sys.stdin.buffer\n        num = abs(int(partial))\
    \ if partial else 0\n        is_negative = partial and partial.startswith('-')\n\
    \        have_digit = partial is not None\n\n        original_chunk_size = sys.stdin._CHUNK_SIZE\n\
    \        sys.stdin._CHUNK_SIZE = max(original_chunk_size, max_digits * (n - pos))\n\
    \        \n        while pos < n:\n            byte = stdin_buffer.read(1)\n\n\
    \            match byte[0]:\n                case 10 | 32:\n                 \
    \   if have_digit:\n                        result[pos] = -num+shift if is_negative\
    \ else num+shift\n                        pos += 1\n                        num\
    \ = 0\n                        is_negative = False\n                        have_digit\
    \ = False\n                case 45:  # minus sign\n                    is_negative\
    \ = True\n                case char:  # digit\n                    num = (num\
    \ * 10) + (char - 48)\n                    have_digit = True\n\n        if have_digit:\n\
    \            result[pos] = -num+shift if is_negative else num+shift\n        \
    \    pos += 1\n\n        sys.stdin._CHUNK_SIZE = original_chunk_size \n      \
    \  if pos < n:\n            raise EOFError(f\"Only found {pos} numbers, expected\
    \ {n}\")\n            \n        return result\n\nclass CharStream(TokenStream):\n\
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
    \            return cls(next(ts))\n        return parser\n\nT = TypeVar('T')\n\
    @overload\ndef read() -> list[int]: ...\n@overload\ndef read(spec: int|None) ->\
    \ list[int]: ...\n@overload\ndef read(spec: Type[T]|T, char=False) -> T: ...\n\
    def read(spec: Type[T]|T=None, char=False):\n    match spec, char:\n        case\
    \ None, False:\n            return list(map(int, input().split()))\n        case\
    \ int(offset), False:\n            return [int(s)+offset for s in input().split()]\n\
    \        case _, _:\n            if char:\n                stream = CharStream()\n\
    \            else:\n                stream = TokenStream()\n            parser:\
    \ T = Parser.compile(spec)\n            return parser(stream)\n\nfrom typing import\
    \ TypeVar, Generic, Container\nfrom dataclasses import dataclass\nfrom math import\
    \ inf\n\nT = TypeVar('T')\n\n@dataclass\nclass Transition2D(Generic[T]):\n   \
    \ di: int\n    dj: int\n    \n    def __call__(self, i: int, j: int, src: T, dest:\
    \ T) -> T:\n        \"\"\"Override this to implement transition logic\"\"\"\n\
    \        return src  # Default no-op\n    \n    @classmethod\n    def make(cls,\
    \ func):\n        class Transition(cls):\n            def __call__(self, i: int,\
    \ j: int, src: T, dest: T) -> T:\n                return func(i,j,src,dest)\n\
    \        return Transition\n    \nT = TypeVar('T')\nclass DynamicProgramming2D(Generic[T],\
    \ Parsable, Container):\n    def __init__(self, rows: int, cols: int, default:\
    \ T = inf):\n        self.rows = rows\n        self.cols = cols\n        self.table\
    \ = default if isinstance(default, list) else [[default] * cols for _ in range(rows)]\n\
    \    \n    def __getitem__(self, pos: tuple[int, int]) -> T:\n        i, j = pos\n\
    \        return self.table[i][j]\n    \n    def __setitem__(self, pos: tuple[int,\
    \ int], value: T) -> None:\n        i, j = pos\n        self.table[i][j] = value\n\
    \n    def __contains__(self, x: object) -> bool:\n        return any(x in row\
    \ for row in self.table)\n    \n    \n    def solve(self, transitions: list[Transition2D[T]])\
    \ -> None:\n        for i in range(self.rows):\n            for j in range(self.cols):\n\
    \                curr_val = self.table[i][j]\n                for trans in transitions:\n\
    \                    ni, nj = i + trans.di, j + trans.dj\n                   \
    \ if 0 <= ni < self.rows and 0 <= nj < self.cols:\n                        self.table[ni][nj]\
    \ = trans(i, j, curr_val, self.table[ni][nj])\n    \n    @classmethod\n    def\
    \ compile(cls, N, M, T = int):\n        table = Parser.compile(list[list[T,M],N])\n\
    \        def parse(ts: TokenStream):\n            return cls(N, M, table(ts))\n\
    \        return parse\n\n\n@dataclass\nclass Match(Transition2D[int]):\n    A:\
    \ list[int]\n    B: list[int]\n\n    def __call__(self, i: int, j: int, src_val:\
    \ int, dest_val: int) -> int:\n        return min(dest_val, src_val + (self.A[i]\
    \ != self.B[j]))\n\nclass Edit(Transition2D[int]):\n    def __call__(self, i:\
    \ int, j: int, src_val: int, dest_val: int) -> int:\n        return min(dest_val,\
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
  timestamp: '2024-11-25 19:30:19+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc185_e_dp2d.test.py
layout: document
redirect_from:
- /verify/test/abc185_e_dp2d.test.py
- /verify/test/abc185_e_dp2d.test.py.html
title: test/abc185_e_dp2d.test.py
---
