---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/alg/dp/monotone_minima_fn.py
    title: cp_library/alg/dp/monotone_minima_fn.py
  - icon: ':question:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
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
  - icon: ':question:'
    path: cp_library/math/conv/minplus_conv_fn.py
    title: cp_library/math/conv/minplus_conv_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/min_plus_convolution_convex_arbitrary
    links:
    - https://judge.yosupo.jp/problem/min_plus_convolution_convex_arbitrary
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/min_plus_convolution_convex_arbitrary\n\
    \ndef main():\n    N, M = read(tuple[int, ...])\n    A = read(list[int])\n   \
    \ B = read(list[int])\n    C = minplus_conv_arb_cnvx(B,A)\n    write(*C)\n   \
    \ \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\nfrom\
    \ typing import Type, Union, overload\nimport typing\nfrom collections import\
    \ deque\nfrom numbers import Number\nfrom types import GenericAlias \nfrom typing\
    \ import Callable, Collection, Iterator, Union\nimport os\nimport sys\nfrom io\
    \ import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines\
    \ = 0\n\n    def __init__(self, file):\n        self._fd = file.fileno()\n   \
    \     self.buffer = BytesIO()\n        self.writable = \"x\" in file.mode or \"\
    r\" not in file.mode\n        self.write = self.buffer.write if self.writable\
    \ else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n        while\
    \ True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n\
    \            if not b:\n                break\n            ptr = self.buffer.tell()\n\
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
    \ TokenStream.stream.readline().split()\n\nclass CharStream(TokenStream):\n  \
    \  def line(self):\n        assert not self.queue\n        return next(TokenStream.stream).rstrip()\n\
    \nParseFn = Callable[[TokenStream],_T]\nclass Parser:\n    def __init__(self,\
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
    \ Union[Type[_T],_T] = None, char=False):\n    if not char:\n        if spec is\
    \ None:\n            return map(int, TokenStream.stream.readline().split())\n\
    \        elif isinstance(offset := spec, int):\n            return [int(s)+offset\
    \ for s in TokenStream.stream.readline().split()]\n        elif spec is int:\n\
    \            return int(TokenStream.stream.readline())\n        else:\n      \
    \      stream = TokenStream()\n    else:\n        stream = CharStream()\n    parser:\
    \ _T = Parser.compile(spec)\n    return parser(stream)\n\ndef write(*args, **kwargs):\n\
    \    \"\"\"Prints the values to a stream, or to stdout_fast by default.\"\"\"\n\
    \    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n\
    \    at_start = True\n    for x in args:\n        if not at_start:\n         \
    \   file.write(sep)\n        file.write(str(x))\n        at_start = False\n  \
    \  file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\n\n\ndef monotone_minima(N: int, M: int, func: Callable[[int,int,int],bool]):\n\
    \    \"\"\"\n    Finds row minima in a totally monotone N\xD7M matrix using the\
    \ SMAWK algorithm.\n    The matrix is defined implicitly through the comparison\
    \ function.\n    \n    A matrix is totally monotone if the minimum in row i occurs\
    \ at column j,\n    then the minimum in row i+1 must occur at column j' where\
    \ j \u2264 j'.\n    \n    Time: O(N log M), Space: O(N)\n    \n    Args:\n   \
    \     N: Number of rows\n        M: Number of columns\n        func(i,j,k): Returns\
    \ True if element (i,j) < element (i,k)\n    \n    Returns:\n        List of column\
    \ indices containing the minimum value for each row\n    \n    Example:\n    \
    \    # Find minima where each element is (i-j)\xB2\n        min_indices = monotone_minima(5,\
    \ 5, lambda i,j,k: (i-j)**2 < (i-k)**2)\n    \"\"\"\n    min_j, st = [0] * N,\
    \ elist(N)\n    st.append((0, N, 0, M))\n    while st:\n        li, ri, lj, rj\
    \ = st.pop()\n        if li == ri: continue\n        mi, mj = li + ri >> 1, lj\n\
    \        for j in range(lj + 1, rj):\n            if func(mi, mj, j): mj = j\n\
    \        min_j[mi] = mj\n        st.append((li, mi, lj, mj+1))\n        st.append((mi+1,\
    \ ri, mj, rj))\n    return min_j\n\n\n\ndef elist(est_len: int) -> list: ...\n\
    try:\n    from __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n\
    \        return []\nelist = newlist_hint\n    \n\ndef minplus_conv_arb_cnvx(arb:\
    \ list[int], cnvx: list[int]) -> list[int]:\n    N, M = len(cnvx), len(arb)\n\
    \    def cmp(i, j, k):\n        return i >= k and (i-j >= N or (cnvx[i-j] + arb[j]\
    \ >= cnvx[i-k] + arb[k]))\n    cols = monotone_minima(N+M-1, M, cmp)\n    return\
    \ [arb[j] + cnvx[i-j] for i, j in enumerate(cols)]\n\ndef minplus_conv_cnvx(A:\
    \ list[int], B: list[int]) -> list[int]:\n    if not (N := len(A)) | (M := len(B)):\
    \ return []\n    C = [0] * (K:=N+M-1)\n    C[0], I, J = A[i := 0] + B[j := 0],\
    \ N-1, M-1\n    for k in range(1, K):\n        if j == J or (i != I and A[i+1]\
    \ + B[j] < A[i] + B[j+1]): i += 1\n        else: j += 1\n        C[k] = A[i] +\
    \ B[j]\n    return C\n\ndef minplus_iconv(A: list[int], B: list[int]):\n    N,\
    \ M = len(A), len(B)\n    for i in range(N-1,-1,-1):\n        A[i] = min(B[j]\
    \ + A[i-j] for j in range(min(M,i+1)))   \n\nif __name__ == \"__main__\":\n  \
    \  main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/min_plus_convolution_convex_arbitrary\n\
    \ndef main():\n    N, M = read(tuple[int, ...])\n    A = read(list[int])\n   \
    \ B = read(list[int])\n    C = minplus_conv_arb_cnvx(B,A)\n    write(*C)\n   \
    \ \nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn import\
    \ write\nfrom cp_library.math.conv.minplus_conv_fn import minplus_conv_arb_cnvx\n\
    \nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/math/conv/minplus_conv_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/alg/dp/monotone_minima_fn.py
  - cp_library/ds/elist_fn.py
  isVerificationFile: true
  path: test/library-checker/convolution/min_plus_convolution_convex_arbitrary.test.py
  requiredBy: []
  timestamp: '2025-01-16 09:57:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/convolution/min_plus_convolution_convex_arbitrary.test.py
layout: document
redirect_from:
- /verify/test/library-checker/convolution/min_plus_convolution_convex_arbitrary.test.py
- /verify/test/library-checker/convolution/min_plus_convolution_convex_arbitrary.test.py.html
title: test/library-checker/convolution/min_plus_convolution_convex_arbitrary.test.py
---
