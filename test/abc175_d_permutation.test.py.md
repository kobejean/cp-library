---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/functional_graph_cls.py
    title: cp_library/alg/graph/functional_graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/permutation_cls.py
    title: cp_library/alg/graph/permutation_cls.py
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
    PROBLEM: https://atcoder.jp/contests/abc175/tasks/abc175_d
    links:
    - https://atcoder.jp/contests/abc175/tasks/abc175_d
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc175/tasks/abc175_d\n\
    \nfrom itertools import accumulate\nfrom math import inf\n\n\ndef main():\n  \
    \  N, K = read(tuple[int, ...])\n    P = read(Permutation[N])\n    C = read(list[int,\
    \ N])\n\n    ans = -inf\n    for cyc in P.cycles():\n        L = len(cyc)\n  \
    \      A = [C[u] for u in cyc]\n        loop = sum(A)\n        A = list(accumulate(A*3))\n\
    \        m, k = divmod(K, L)\n        if m:\n            k += L\n            m\
    \ -= 1\n        rem = max(A[i+j+1] - A[i] for i in range(L) for j in range(k))\n\
    \        cost = max(m*loop + rem, rem)\n        ans = max(ans, cost)\n\n    print(ans)\n\
    \    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\n\n\nimport sys\nimport typing\nfrom collections import deque\nfrom numbers\
    \ import Number\nfrom typing import Callable, Collection, Iterator, TypeAlias,\
    \ TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self, stream = sys.stdin):\n\
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
    \ _ in range(N))\n        return parse\n\nclass Permutation(FunctionalGraph):\n\
    \n    def inv(P):\n        Pinv = [0]*P.N\n        for i,p in enumerate(P):\n\
    \            Pinv[p] = i\n        return type(P)(Pinv)\n\nfrom typing import Type,\
    \ TypeVar, overload\n\nT = TypeVar('T')\n@overload\ndef read(spec: int|None) ->\
    \ list[int]: ...\n@overload\ndef read(spec: Type[T]|T, char=False) -> T: ...\n\
    def read(spec: Type[T]|T=None, char=False):\n    match spec, char:\n        case\
    \ None, False:\n            return list(map(int, input().split()))\n        case\
    \ int(offset), False:\n            return [int(s)+offset for s in input().split()]\n\
    \        case _, _:\n            if char:\n                stream = CharStream(sys.stdin)\n\
    \            else:\n                stream = TokenStream(sys.stdin)\n        \
    \    parser: T = Parser.compile(spec)\n            return parser(stream)\n\nif\
    \ __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc175/tasks/abc175_d\n\
    \nfrom itertools import accumulate\nfrom math import inf\n\n\ndef main():\n  \
    \  N, K = read(tuple[int, ...])\n    P = read(Permutation[N])\n    C = read(list[int,\
    \ N])\n\n    ans = -inf\n    for cyc in P.cycles():\n        L = len(cyc)\n  \
    \      A = [C[u] for u in cyc]\n        loop = sum(A)\n        A = list(accumulate(A*3))\n\
    \        m, k = divmod(K, L)\n        if m:\n            k += L\n            m\
    \ -= 1\n        rem = max(A[i+j+1] - A[i] for i in range(L) for j in range(k))\n\
    \        cost = max(m*loop + rem, rem)\n        ans = max(ans, cost)\n\n    print(ans)\n\
    \    \nfrom cp_library.alg.graph.permutation_cls import Permutation\nfrom cp_library.io.read_specs_fn\
    \ import read\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/alg/graph/permutation_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/alg/graph/functional_graph_cls.py
  - cp_library/io/parser_cls.py
  isVerificationFile: true
  path: test/abc175_d_permutation.test.py
  requiredBy: []
  timestamp: '2024-11-05 04:28:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc175_d_permutation.test.py
layout: document
redirect_from:
- /verify/test/abc175_d_permutation.test.py
- /verify/test/abc175_d_permutation.test.py.html
title: test/abc175_d_permutation.test.py
---
