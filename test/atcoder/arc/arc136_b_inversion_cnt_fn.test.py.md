---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/ds/bit_cls.py
    title: cp_library/ds/bit_cls.py
  - icon: ':question:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':question:'
    path: cp_library/io/read_fn.py
    title: cp_library/io/read_fn.py
  - icon: ':question:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  - icon: ':x:'
    path: cp_library/math/inversion_cnt_fn.py
    title: cp_library/math/inversion_cnt_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/arc136/tasks/arc136_b
    links:
    - https://atcoder.jp/contests/arc136/tasks/arc136_b
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc136/tasks/arc136_b\n\
    \n\ndef main():\n    N = read(int)\n    A = read(list[-1])\n    B = read(list[-1])\n\
    \    Aic = inversion_cnt(A,5000)\n    Bic = inversion_cnt(B,5000)\n    if sorted(A)\
    \ != sorted(B):\n        return False\n    has_dup = len(set(A)) < N\n    return\
    \ has_dup or (Aic&1 == Bic&1)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\nfrom typing import Union\n\n\nclass BinaryIndexTree:\n\
    \    def __init__(bit, v: Union[int,list]):\n        if isinstance(v, int):\n\
    \            bit.data, bit.size = [0]*v, v\n        else:\n            bit.build(v)\n\
    \n    def build(bit, data):\n        bit.data, bit.size = data, len(data)\n  \
    \      for i in range(bit.size):\n            if (r := i|(i+1)) < bit.size: \n\
    \                data[r] += data[i]\n\n    def get(bit, i: int):\n        assert\
    \ 0 <= i < bit.size\n        s, z = (data := bit.data)[i], i&(i+1)\n        for\
    \ _ in range((i^z).bit_count()):\n            s, i = s-data[i-1], i-(i&-i)\n \
    \       return s\n    __getitem__ = get\n    \n    def set(bit, i: int, x: int):\n\
    \        bit.add(i, x-bit.get(i))\n    __setitem__ = set\n        \n    def add(bit,\
    \ i: int, x: int) -> None:\n        assert 0 <= i <= bit.size\n        data, size\
    \ = bit.data, bit.size\n        while i < size:\n            data[i], i = data[i]+x,\
    \ i|(i+1)\n\n    def presum(bit, n: int):\n        assert 0 <= n <= bit.size\n\
    \        s, z, i, data = 0, n.bit_count(), n-1, bit.data\n        for _ in range(z):\n\
    \            s, i = s+data[i], (i&(i+1))-1\n        return s\n    \n    def range_sum(bit,\
    \ l: int, r: int):\n        return bit.presum(r) - bit.presum(l)\n\n    def prelist(bit):\n\
    \        pre = [0]+bit.data\n        for i in range(bit.size+1):\n           \
    \ pre[i] += pre[i&(i-1)]\n        return pre\n    \n    def bisect_left(bit, v):\n\
    \        data, i, s, m = bit.data, 0, 0, 1 << ((N := bit.size).bit_length()-1)\n\
    \        while m:\n            if (ni := i|m) <= N and (ns := s + data[ni-1])\
    \ < v:\n                s, i = ns, ni\n            m >>= 1\n        return i\n\
    \    \n    def bisect_right(bit, v):\n        data, i, s, m = bit.data, 0, 0,\
    \ 1 << ((N := bit.size).bit_length()-1)\n        while m:\n            if (ni\
    \ := i|m) <= N and (ns := s + data[ni-1]) <= v:\n                s, i = ns, ni\n\
    \            m >>= 1\n        return i\n\ndef inversion_cnt(Z, N: Union[int,None]\
    \ = None):\n    if N is None:\n        # coordinate compression\n        Zsort\
    \ = sorted(set(Z))\n        Zcomp = { v: i for i, v in enumerate(Zsort) }\n  \
    \      Z = [Zcomp[z] for z in Z]\n        N = len(Z)\n\n    bit = BinaryIndexTree(N)\n\
    \    cnt = 0\n    for z in reversed(Z):\n        cnt += bit.presum(z)\n      \
    \  bit.add(z, 1)\n    return cnt\n\n\nfrom typing import Type, Union, overload\n\
    import typing\nfrom collections import deque\nfrom numbers import Number\nfrom\
    \ types import GenericAlias \nfrom typing import Callable, Collection, Iterator,\
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
    \ = IOWrapper(sys.stdout)\nfrom typing import TypeVar\n_T = TypeVar('T')\n\nclass\
    \ TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\n    def __init__(self):\n\
    \        self.queue = deque()\n\n    def __next__(self):\n        if not self.queue:\
    \ self.queue.extend(self.line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        return\
    \ TokenStream.stream.readline().split()\n        \nTokenStream.default = TokenStream()\n\
    \nclass CharStream(TokenStream):\n\n    def line(self):\n        return TokenStream.stream.readline().rstrip()\n\
    \n\nParseFn = Callable[[TokenStream],_T]\nclass Parser:\n    def __init__(self,\
    \ spec: Union[type[_T],_T]):\n        self.parse = Parser.compile(spec)\n\n  \
    \  def __call__(self, ts: TokenStream) -> _T:\n        return self.parse(ts)\n\
    \    \n    @staticmethod\n    def compile_type(cls: type[_T], args = ()) -> _T:\n\
    \        if issubclass(cls, Parsable):\n            return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(ts: TokenStream):\n\
    \                return cls(next(ts))              \n            return parse\n\
    \        elif issubclass(cls, tuple):\n            return Parser.compile_tuple(cls,\
    \ args)\n        elif issubclass(cls, Collection):\n            return Parser.compile_collection(cls,\
    \ args)\n        elif callable(cls):\n            def parse(ts: TokenStream):\n\
    \                return cls(next(ts))              \n            return parse\n\
    \        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile(spec: Union[type[_T],_T]=int) -> ParseFn[_T]:\n        if isinstance(spec,\
    \ (type, GenericAlias)):\n            cls = typing.get_origin(spec) or spec\n\
    \            args = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream):\n                return\
    \ cls(next(ts)) + offset\n            return parse\n        elif isinstance(args\
    \ := spec, tuple):      \n            return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection):  \n            return\
    \ Parser.compile_collection(type(spec), args)\n        elif isinstance(fn := spec,\
    \ Callable): \n            def parse(ts: TokenStream):\n                return\
    \ fn(next(ts))\n            return parse\n        else:\n            raise NotImplementedError()\n\
    \n    @staticmethod\n    def compile_line(cls: _T, spec=int) -> ParseFn[_T]:\n\
    \        if spec is int:\n            fn = Parser.compile(spec)\n            def\
    \ parse(ts: TokenStream):\n                return cls((int(token) for token in\
    \ ts.line()))\n            return parse\n        else:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream):\n                return cls((fn(ts) for\
    \ _ in ts.wait()))\n            return parse\n\n    @staticmethod\n    def compile_repeat(cls:\
    \ _T, spec, N) -> ParseFn[_T]:\n        fn = Parser.compile(spec)\n        def\
    \ parse(ts: TokenStream):\n            return cls((fn(ts) for _ in range(N)))\n\
    \        return parse\n\n    @staticmethod\n    def compile_children(cls: _T,\
    \ specs) -> ParseFn[_T]:\n        fns = tuple((Parser.compile(spec) for spec in\
    \ specs))\n        def parse(ts: TokenStream):\n            return cls((fn(ts)\
    \ for fn in fns))  \n        return parse\n            \n    @staticmethod\n \
    \   def compile_tuple(cls: type[_T], specs) -> ParseFn[_T]:\n        if isinstance(specs,\
    \ (tuple,list)) and len(specs) == 2 and specs[1] is ...:\n            return Parser.compile_line(cls,\
    \ specs[0])\n        else:\n            return Parser.compile_children(cls, specs)\n\
    \n    @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 \n\
    \            and isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls,\
    \ specs[0], specs[1])\n        else:\n            raise NotImplementedError()\n\
    \nclass Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(ts:\
    \ TokenStream):\n            return cls(next(ts))\n        return parser\n\n@overload\n\
    def read() -> list[int]: ...\n@overload\ndef read(spec: int) -> list[int]: ...\n\
    @overload\ndef read(spec: Union[Type[_T],_T], char=False) -> _T: ...\ndef read(spec:\
    \ Union[Type[_T],_T] = None, char=False):\n    if not char and spec is None:\n\
    \        line = TokenStream.default.queue or TokenStream.stream.readline().split()\n\
    \        return map(int, line)\n    parser: _T = Parser.compile(spec)\n    return\
    \ parser(CharStream.default if char else TokenStream.default)\n\ndef write(*args,\
    \ **kwargs):\n    \"\"\"Prints the values to a stream, or to stdout_fast by default.\"\
    \"\"\n    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n\
    \    at_start = True\n    for x in args:\n        if not at_start:\n         \
    \   file.write(sep)\n        file.write(str(x))\n        at_start = False\n  \
    \  file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\nif __name__ == \"__main__\":\n    ans = main()\n    write(\"\
    Yes\" if ans else \"No\")\n    \n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc136/tasks/arc136_b\n\
    \n\ndef main():\n    N = read(int)\n    A = read(list[-1])\n    B = read(list[-1])\n\
    \    Aic = inversion_cnt(A,5000)\n    Bic = inversion_cnt(B,5000)\n    if sorted(A)\
    \ != sorted(B):\n        return False\n    has_dup = len(set(A)) < N\n    return\
    \ has_dup or (Aic&1 == Bic&1)\n\nfrom cp_library.math.inversion_cnt_fn import\
    \ inversion_cnt\nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn\
    \ import write\n\nif __name__ == \"__main__\":\n    ans = main()\n    write(\"\
    Yes\" if ans else \"No\")\n    "
  dependsOn:
  - cp_library/math/inversion_cnt_fn.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/ds/bit_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
  requiredBy: []
  timestamp: '2025-01-21 19:55:16+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
layout: document
redirect_from:
- /verify/test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
- /verify/test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py.html
title: test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
---
