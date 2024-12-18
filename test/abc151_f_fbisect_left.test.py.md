---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/fbisect_fn.py
    title: cp_library/alg/divcon/fbisect_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_fn.py
    title: cp_library/io/read_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/elm_wise_mixin.py
    title: cp_library/math/elm_wise_mixin.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/vec2d_cls.py
    title: cp_library/math/vec2d_cls.py
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
    PROBLEM: https://atcoder.jp/contests/abc151/tasks/abc151_f
    links:
    - https://atcoder.jp/contests/abc151/tasks/abc151_f
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc151/tasks/abc151_f\n\
    # verification-helper: ERROR 1e-6\n\nfrom math import sqrt\n\ndef main():\n  \
    \  N = read(int)\n    points = read(list[Vec2D[float], N])\n\n    def candidates(r)\
    \ -> list[Vec2D[float]]:\n        r2 = 2*r\n        intersections = []\n     \
    \   for i in range(N):\n            for j in range(i):\n                if i ==\
    \ j: continue\n                diff = points[j] - points[i]\n                if\
    \ (d := diff.magnitude()) <= r2:\n                    diff /= d\n            \
    \        d /= 2.0\n                    diff = diff.rot90() * sqrt(r*r - d*d)\n\
    \                    mid = (points[i]+points[j])/2.0\n                    intersections.append(mid-diff)\n\
    \                    intersections.append(mid+diff)\n\n        return intersections\n\
    \n    def f(r):\n        for candidate in candidates(r):\n            if all(candidate.distance(point)\
    \ <= r+1e-9 for point in points):\n                return True\n        return\
    \ False\n    \n    ans = fbisect_left(f, 2000.0)\n    write(f'{ans:0.18f}')\n\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\ndef\
    \ fbisect_left(key, hi, x = True, lo = 0.0, tol=1e-9):\n    while hi - lo > tol:\
    \            \n        mid = (lo + hi) / 2\n        if key(mid) >= x:\n      \
    \      hi = mid\n        else:\n            lo = mid\n            \n    return\
    \ lo\n\ndef fbisect_right(key, hi, x=False, lo=0.0, tol=1e-9):\n    while hi -\
    \ lo > tol:\n        mid = (lo + hi) / 2\n        if key(mid) > x:\n         \
    \   hi = mid\n        else:\n            lo = mid\n    return hi\n\n\n\nimport\
    \ typing\nfrom collections import deque\nfrom numbers import Number\nfrom types\
    \ import GenericAlias \nfrom typing import Callable, Collection, Iterator, TypeVar,\
    \ Union\nimport os\nimport sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n\
    \    BUFSIZE = 8192\n    newlines = 0\n\n    def __init__(self, file):\n     \
    \   self._fd = file.fileno()\n        self.buffer = BytesIO()\n        self.writable\
    \ = \"x\" in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
    \ if self.writable else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n\
    \        while True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n            if not b:\n                break\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines = 0\n        return self.buffer.read()\n\n    def readline(self):\n\
    \        BUFSIZE = self.BUFSIZE\n        while self.newlines == 0:\n         \
    \   b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n        \
    \    self.newlines = b.count(b\"\\n\") + (not b)\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines -= 1\n        return self.buffer.readline()\n\n    def\
    \ flush(self):\n        if self.writable:\n            os.write(self._fd, self.buffer.getvalue())\n\
    \            self.buffer.truncate(0), self.buffer.seek(0)\n\n\nclass IOWrapper(IOBase):\n\
    \    stdin: 'IOWrapper' = None\n    stdout: 'IOWrapper' = None\n    \n    def\
    \ __init__(self, file):\n        self.buffer = FastIO(file)\n        self.flush\
    \ = self.buffer.flush\n        self.writable = self.buffer.writable\n\n    def\
    \ write(self, s):\n        return self.buffer.write(s.encode(\"ascii\"))\n   \
    \ \n    def read(self):\n        return self.buffer.read().decode(\"ascii\")\n\
    \    \n    def readline(self):\n        return self.buffer.readline().decode(\"\
    ascii\")\n\nsys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\nsys.stdout = IOWrapper.stdout\
    \ = IOWrapper(sys.stdout)\n\n\nclass TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\
    \n    def __init__(self):\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        return\
    \ TokenStream.stream.readline().split()\n\nclass CharStream(TokenStream):\n  \
    \  def line(self):\n        assert not self.queue\n        return next(TokenStream.stream).rstrip()\n\
    \        \nT = TypeVar('T')\nParseFn = Callable[[TokenStream],T]\nclass Parser:\n\
    \    def __init__(self, spec: Union[type[T],T]):\n        self.parse = Parser.compile(spec)\n\
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
    \    def compile(spec: Union[type[T],T]=int) -> ParseFn[T]:\n        if isinstance(spec,\
    \ (type, GenericAlias)):\n            cls = typing.get_origin(spec) or spec\n\
    \            args = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream):\n                return\
    \ cls(next(ts)) + offset\n            return parse\n        elif isinstance(args\
    \ := spec, tuple):      \n            return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection):  \n            return\
    \ Parser.compile_collection(type(spec), args)\n        else:\n            raise\
    \ NotImplementedError()\n    \n    @staticmethod\n    def compile_line(cls: T,\
    \ spec=int) -> ParseFn[T]:\n        if spec is int:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream):\n                return cls((int(token)\
    \ for token in ts.line()))\n            return parse\n        else:\n        \
    \    fn = Parser.compile(spec)\n            def parse(ts: TokenStream):\n    \
    \            return cls((fn(ts) for _ in ts.wait()))\n            return parse\n\
    \n    @staticmethod\n    def compile_repeat(cls: T, spec, N) -> ParseFn[T]:\n\
    \        fn = Parser.compile(spec)\n        def parse(ts: TokenStream):\n    \
    \        return cls((fn(ts) for _ in range(N)))\n        return parse\n\n    @staticmethod\n\
    \    def compile_children(cls: T, specs) -> ParseFn[T]:\n        fns = tuple((Parser.compile(spec)\
    \ for spec in specs))\n        def parse(ts: TokenStream):\n            return\
    \ cls((fn(ts) for fn in fns))  \n        return parse\n            \n    @staticmethod\n\
    \    def compile_tuple(cls: type[T], specs) -> ParseFn[T]:\n        if isinstance(specs,\
    \ (tuple,list)) and len(specs) == 2 and specs[1] is ...:\n            return Parser.compile_line(cls,\
    \ specs[0])\n        else:\n            return Parser.compile_children(cls, specs)\n\
    \n    @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 \n\
    \            and isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls,\
    \ specs[0], specs[1])\n        else:\n            raise NotImplementedError()\n\
    \nclass Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(ts:\
    \ TokenStream):\n            return cls(next(ts))\n        return parser\n\nfrom\
    \ math import hypot\n\nimport operator\nfrom typing import Sequence\n\nclass ElmWiseMixin:\n\
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
    \    def __mod__(self, other): return self.elm_wise(other, operator.mod)\n\n \
    \   def distance(self: 'ElmWiseMixin', other: 'ElmWiseMixin'):\n        diff =\
    \ other-self\n        return hypot(*diff)\n    \n    def magnitude(vec: 'ElmWiseMixin'):\n\
    \        return hypot(*vec)\n    \n    def norm(vec: 'ElmWiseMixin'):\n      \
    \  return vec / vec.magnitude()\nfrom typing import Iterable \n\nclass Vec(ElmWiseMixin,\
    \ tuple, Parsable):\n    def __new__(cls, *args):\n        if len(args) == 1 and\
    \ isinstance(args[0], Iterable):\n            return super().__new__(cls, args[0])\n\
    \        return super().__new__(cls, args)\n\n    @classmethod\n    def compile(cls,\
    \ T: type = int, N = None):\n        elm = Parser.compile(T)\n        if N is\
    \ None:\n            def parse(ts: TokenStream):\n                return cls(elm(ts)\
    \ for _ in ts.wait())\n        else:\n            def parse(ts: TokenStream):\n\
    \                return cls(elm(ts) for _ in range(N))\n        return parse\n\
    \  \n\nclass Vec2D(Vec):\n\n    def elm_wise(self, other, op):\n        if isinstance(other,\
    \ Number):\n            return Vec2D(op(self[0], other), op(self[1], other))\n\
    \        if isinstance(other, Sequence):\n            return Vec2D(op(self[0],\
    \ other[0]), op(self[1], other[1]))\n        raise ValueError(\"Operand must be\
    \ a number or a tuple of the same length\")\n\n    def distance(v1: 'Vec', v2:\
    \ 'Vec'):\n        dx, dy = v2[0]-v1[0], v2[1]-v1[1]\n        return sqrt(dx*dx+dy*dy)\n\
    \    \n    def magnitude(vec: 'Vec'):\n        x, y = vec\n        return sqrt(x*x+y*y)\n\
    \    \n    def rot90(vec):\n        x,y = vec\n        return Vec2D(-y,x)\n  \
    \  \n    def rot180(vec):\n        x,y = vec\n        return Vec2D(-x,-y)\n  \
    \  \n    def rot270(vec):\n        x,y = vec\n        return Vec2D(y,-x)\n   \
    \ \n    def flip_x(vec):\n        x,y = vec\n        return Vec2D(-x,y)\n    \n\
    \    def flip_y(vec):\n        x,y = vec\n        return Vec2D(x,-y)\n    \n \
    \   @classmethod\n    def compile(cls, T: type = int):\n        elm = Parser.compile(T)\n\
    \        def parse(ts: TokenStream):\n            return cls(elm(ts), elm(ts))\n\
    \        return parse\n\n\nfrom typing import Type, TypeVar, Union, overload\n\
    \nT = TypeVar('T')\n@overload\ndef read() -> list[int]: ...\n@overload\ndef read(spec:\
    \ int) -> list[int]: ...\n@overload\ndef read(spec: Union[Type[T],T], char=False)\
    \ -> T: ...\ndef read(spec: Union[Type[T],T] = None, char=False):\n    if not\
    \ char:\n        if spec is None:\n            return map(int, TokenStream.stream.readline().split())\n\
    \        elif isinstance(offset := spec, int):\n            return [int(s)+offset\
    \ for s in TokenStream.stream.readline().split()]\n        elif spec is int:\n\
    \            return int(TokenStream.stream.readline())\n        else:\n      \
    \      stream = TokenStream()\n    else:\n        stream = CharStream()\n    parser:\
    \ T = Parser.compile(spec)\n    return parser(stream)\n\ndef write(*args, **kwargs):\n\
    \    \"\"\"Prints the values to a stream, or to stdout_fast by default.\"\"\"\n\
    \    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n\
    \    at_start = True\n    for x in args:\n        if not at_start:\n         \
    \   file.write(sep)\n        file.write(str(x))\n        at_start = False\n  \
    \  file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc151/tasks/abc151_f\n\
    # verification-helper: ERROR 1e-6\n\nfrom math import sqrt\n\ndef main():\n  \
    \  N = read(int)\n    points = read(list[Vec2D[float], N])\n\n    def candidates(r)\
    \ -> list[Vec2D[float]]:\n        r2 = 2*r\n        intersections = []\n     \
    \   for i in range(N):\n            for j in range(i):\n                if i ==\
    \ j: continue\n                diff = points[j] - points[i]\n                if\
    \ (d := diff.magnitude()) <= r2:\n                    diff /= d\n            \
    \        d /= 2.0\n                    diff = diff.rot90() * sqrt(r*r - d*d)\n\
    \                    mid = (points[i]+points[j])/2.0\n                    intersections.append(mid-diff)\n\
    \                    intersections.append(mid+diff)\n\n        return intersections\n\
    \n    def f(r):\n        for candidate in candidates(r):\n            if all(candidate.distance(point)\
    \ <= r+1e-9 for point in points):\n                return True\n        return\
    \ False\n    \n    ans = fbisect_left(f, 2000.0)\n    write(f'{ans:0.18f}')\n\n\
    \nfrom cp_library.alg.divcon.fbisect_fn import fbisect_left\nfrom cp_library.math.vec2d_cls\
    \ import Vec2D\nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn\
    \ import write\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/alg/divcon/fbisect_fn.py
  - cp_library/math/vec2d_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/math/vec_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/math/elm_wise_mixin.py
  isVerificationFile: true
  path: test/abc151_f_fbisect_left.test.py
  requiredBy: []
  timestamp: '2024-12-18 14:55:02+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc151_f_fbisect_left.test.py
layout: document
redirect_from:
- /verify/test/abc151_f_fbisect_left.test.py
- /verify/test/abc151_f_fbisect_left.test.py.html
title: test/abc151_f_fbisect_left.test.py
---
