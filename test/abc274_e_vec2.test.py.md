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
    path: cp_library/math/elm_wise_mixin.py
    title: cp_library/math/elm_wise_mixin.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/vec2_cls.py
    title: cp_library/math/vec2_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/vec_cls.py
    title: cp_library/math/vec_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    ERROR: 1e-6
    PROBLEM: https://atcoder.jp/contests/abc274/tasks/abc274_e
    links:
    - https://atcoder.jp/contests/abc274/tasks/abc274_e
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc274/tasks/abc274_e\n\
    # verification-helper: ERROR 1e-6\nfrom math import inf\n\ndef main():\n    N,\
    \ M = read(tuple[int, ...])\n    XY = read(list[Vec2, N])\n    PQ = read(list[Vec2,\
    \ M])\n    pts = PQ+XY\n    o = Vec2(0,0)\n    Tmask = (1 << M) -1\n    Y = N+M\n\
    \    Z = 1 << Y\n    O = [o.dist(v) for v in pts]\n    F = [1/(1 << mask.bit_count())\
    \ for mask in range(1 << M)]\n    \n    dp = [[inf]*Y for _ in range(Z)]\n   \
    \ for y in range(Y):\n        mask = 1 << y\n        dp[mask][y] = O[y]\n    \
    \    \n    for mask in range(1,Z):\n        factor = F[mask&Tmask]\n        for\
    \ y in range(Y):\n            nmask = mask | 1 << y\n            if mask == nmask:\
    \ continue\n            nc = dp[nmask][y]\n            for l in range(Y):\n  \
    \              nc = min(nc, dp[mask][l] + pts[l].dist(pts[y]) * factor)\n    \
    \        dp[nmask][y] = nc\n            \n    full = Z-1\n    ans = inf\n    for\
    \ tmask in range(1<<M):\n        mask = full ^ tmask\n        factor = F[mask&Tmask]\n\
    \        for l in range(Y):\n            nc = dp[mask][l] + O[l] * factor\n  \
    \          ans = min(ans, nc)\n    print(f'{ans:0.10f}')\n\n'''\n\u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\n\nimport sys\nimport typing\nfrom collections import\
    \ deque\nfrom numbers import Number\nfrom typing import Callable, Collection,\
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
    \ parser\n\n\nimport operator\nfrom typing import Sequence\n\nclass ElmWiseMixin:\n\
    \    def elm_wise(self, other, op):\n        if isinstance(other, Number):\n \
    \           return type(self)(op(x, other) for x in self)\n        if isinstance(other,\
    \ Sequence):\n            return type(self)(op(x, y) for x, y in zip(self, other))\n\
    \        raise ValueError(\"Operand must be a number or a tuple of the same length\"\
    )\n\n    def __add__(self, other): return self.elm_wise(other, operator.add)\n\
    \    def __radd__(self, other): return self.elm_wise(other, operator.add)\n  \
    \  def __sub__(self, other): return self.elm_wise(other, operator.sub)\n    def\
    \ __rsub__(self, other): return self.elm_wise(other, lambda x,y: operator.sub(y,x))\n\
    \    def __mul__(self, other): return self.elm_wise(other, operator.mul)\n   \
    \ def __rmul__(self, other): return self.elm_wise(other, operator.mul)\n    def\
    \ __truediv__(self, other): return self.elm_wise(other, operator.truediv)\n  \
    \  def __rtruediv__(self, other): return self.elm_wise(other, lambda x,y: operator.truediv(y,x))\n\
    \    def __floordiv__(self, other): return self.elm_wise(other, operator.floordiv)\n\
    \    def __rfloordiv__(self, other): return self.elm_wise(other, lambda x,y: operator.floordiv(y,x))\n\
    \    def __mod__(self, other): return self.elm_wise(other, operator.mod)\nfrom\
    \ typing import Iterable \nfrom math import hypot\n\nclass Vec(tuple, ElmWiseMixin,\
    \ Parsable):\n    def __new__(cls, *args):\n        if len(args) == 1 and isinstance(args[0],\
    \ Iterable):\n            return super().__new__(cls, args[0])\n        return\
    \ super().__new__(cls, args)\n\n    def dist(v1: 'Vec', v2: 'Vec'):\n        diff\
    \ = v2-v1\n        return hypot(*diff)\n\n    @classmethod\n    def compile(cls,\
    \ T: type = int, N = None):\n        elm = Parser.compile(T)\n        if N is\
    \ None:\n            def parse(ts: TokenStream):\n                return cls(elm(ts)\
    \ for _ in ts.wait())\n        else:\n            def parse(ts: TokenStream):\n\
    \                return cls(elm(ts) for _ in range(N))\n        return parse\n\
    \  \nfrom math import sqrt\n\nclass Vec2(Vec):\n\n    def elm_wise(self, other,\
    \ op):\n        if isinstance(other, Number):\n            return Vec2(op(self[0],\
    \ other), op(self[1], other))\n        if isinstance(other, Sequence):\n     \
    \       return Vec2(op(self[0], other[0]), op(self[1], other[1]))\n        raise\
    \ ValueError(\"Operand must be a number or a tuple of the same length\")\n\n \
    \   def dist(v1: 'Vec', v2: 'Vec'):\n        dx, dy = v2[0]-v1[0], v2[1]-v1[1]\n\
    \        return sqrt(dx*dx+dy*dy)\n    \n    @classmethod\n    def compile(cls,\
    \ T: type = int):\n        elm = Parser.compile(T)\n        def parse(ts: TokenStream):\n\
    \            return cls(elm(ts), elm(ts))\n        return parse\n\n\nfrom typing\
    \ import Type, TypeVar, overload\n\nT = TypeVar('T')\n@overload\ndef read(spec:\
    \ int|None) -> list[int]: ...\n@overload\ndef read(spec: Type[T]|T, char=False)\
    \ -> T: ...\ndef read(spec: Type[T]|T=None, char=False):\n    match spec, char:\n\
    \        case None, False:\n            return list(map(int, input().split()))\n\
    \        case int(offset), False:\n            return [int(s)+offset for s in\
    \ input().split()]\n        case _, _:\n            if char:\n               \
    \ stream = CharStream(sys.stdin)\n            else:\n                stream =\
    \ TokenStream(sys.stdin)\n            parser: T = Parser.compile(spec)\n     \
    \       return parser(stream)\n\nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc274/tasks/abc274_e\n\
    # verification-helper: ERROR 1e-6\nfrom math import inf\n\ndef main():\n    N,\
    \ M = read(tuple[int, ...])\n    XY = read(list[Vec2, N])\n    PQ = read(list[Vec2,\
    \ M])\n    pts = PQ+XY\n    o = Vec2(0,0)\n    Tmask = (1 << M) -1\n    Y = N+M\n\
    \    Z = 1 << Y\n    O = [o.dist(v) for v in pts]\n    F = [1/(1 << mask.bit_count())\
    \ for mask in range(1 << M)]\n    \n    dp = [[inf]*Y for _ in range(Z)]\n   \
    \ for y in range(Y):\n        mask = 1 << y\n        dp[mask][y] = O[y]\n    \
    \    \n    for mask in range(1,Z):\n        factor = F[mask&Tmask]\n        for\
    \ y in range(Y):\n            nmask = mask | 1 << y\n            if mask == nmask:\
    \ continue\n            nc = dp[nmask][y]\n            for l in range(Y):\n  \
    \              nc = min(nc, dp[mask][l] + pts[l].dist(pts[y]) * factor)\n    \
    \        dp[nmask][y] = nc\n            \n    full = Z-1\n    ans = inf\n    for\
    \ tmask in range(1<<M):\n        mask = full ^ tmask\n        factor = F[mask&Tmask]\n\
    \        for l in range(Y):\n            nc = dp[mask][l] + O[l] * factor\n  \
    \          ans = min(ans, nc)\n    print(f'{ans:0.10f}')\n\nfrom cp_library.math.vec2_cls\
    \ import Vec2\nfrom cp_library.io.read_specs_fn import read\n\nif __name__ ==\
    \ \"__main__\":\n    main()"
  dependsOn:
  - cp_library/math/vec2_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/math/vec_cls.py
  - cp_library/math/elm_wise_mixin.py
  isVerificationFile: true
  path: test/abc274_e_vec2.test.py
  requiredBy: []
  timestamp: '2024-11-04 21:00:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc274_e_vec2.test.py
layout: document
redirect_from:
- /verify/test/abc274_e_vec2.test.py
- /verify/test/abc274_e_vec2.test.py.html
title: test/abc274_e_vec2.test.py
---
