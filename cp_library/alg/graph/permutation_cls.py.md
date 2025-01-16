---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: cp_library/alg/graph/functional_graph_cls.py
    title: cp_library/alg/graph/functional_graph_cls.py
  - icon: ':question:'
    path: cp_library/alg/iter/slice_iterator_reverse_cls.py
    title: cp_library/alg/iter/slice_iterator_reverse_cls.py
  - icon: ':question:'
    path: cp_library/ds/array_init_fn.py
    title: cp_library/ds/array_init_fn.py
  - icon: ':question:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':question:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/atcoder/abc/abc175_d_permutation.test.py
    title: test/atcoder/abc/abc175_d_permutation.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from typing import Iterator\n\nimport typing\nfrom collections import deque\n\
    from numbers import Number\nfrom types import GenericAlias \nfrom typing import\
    \ Callable, Collection, Iterator, Union\nimport os\nimport sys\nfrom io import\
    \ BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines\
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
    \ TokenStream):\n            return cls(next(ts))\n        return parser\n\nclass\
    \ FunctionalGraph(list[int], Parsable):\n    def __init__(F, successors):\n  \
    \      super().__init__(successors)\n        F.N = F.M = len(F)\n\n    def find_cycle(P,\
    \ root):\n        slow = fast = root\n        while (slow := P[slow]) != (fast\
    \ := P[P[fast]]): pass\n        cyc = [slow]\n        while P[slow] != fast: cyc.append(slow\
    \ := P[slow])\n        return cyc\n    \n    def cycles(P) -> Iterator[list[int]]:\n\
    \        vis, cycs, L = u8f(N := P.N), elist(N), elist(N)\n        for v in range(P.N):\n\
    \            if vis[v]: continue\n            slow = fast = v\n            while\
    \ (slow := P[slow]) != (fast := P[P[fast]]) and not vis[fast]: pass\n        \
    \    if vis[fast]: continue\n            L.append(len(cycs))\n            cycs.append(slow)\n\
    \            vis[slow := P[slow]] = 1\n            while slow != fast:\n     \
    \           cycs.append(slow)\n                vis[slow := P[slow]] = 1\n    \
    \    return SliceIteratorReverse(cycs, L)\n\n    @classmethod\n    def compile(cls,\
    \ N: int, shift = -1):\n        return Parser.compile_repeat(cls, shift, N)\n\n\
    \nfrom typing import Iterator, SupportsIndex\n\nclass SliceIteratorReverse(Iterator[_T]):\n\
    \    def __init__(self, A: list[_T], L: list[SupportsIndex]):\n        self.A,\
    \ self.L, self.r = A, L, len(A)\n    def __len__(self): return len(self.L)\n \
    \   def __next__(self):\n        L = self.L\n        if not L: raise StopIteration\n\
    \        self.r, r = (l := L.pop()), self.r\n        return self.A[l:r]\nfrom\
    \ typing import Iterable\n\nfrom array import array\n\ndef i8f(N: int, elm: int\
    \ = 0):      return array('b', (elm,))*N  # signed char\ndef u8f(N: int, elm:\
    \ int = 0):      return array('B', (elm,))*N  # unsigned char\ndef i16f(N: int,\
    \ elm: int = 0):     return array('h', (elm,))*N  # signed short\ndef u16f(N:\
    \ int, elm: int = 0):     return array('H', (elm,))*N  # unsigned short\ndef i32f(N:\
    \ int, elm: int = 0):     return array('i', (elm,))*N  # signed int\ndef u32f(N:\
    \ int, elm: int = 0):     return array('I', (elm,))*N  # unsigned int\ndef i64f(N:\
    \ int, elm: int = 0):     return array('q', (elm,))*N  # signed long long\n# def\
    \ u64f(N: int, elm: int = 0):     return array('Q', (elm,))*N  # unsigned long\
    \ long\ndef f32f(N: int, elm: float = 0.0): return array('f', (elm,))*N  # float\n\
    def f64f(N: int, elm: float = 0.0): return array('d', (elm,))*N  # double\n\n\
    def i8a(init = None):  return array('b') if init is None else array('b', init)\
    \  # signed char\ndef u8a(init = None):  return array('B') if init is None else\
    \ array('B', init)  # unsigned char\ndef i16a(init = None): return array('h')\
    \ if init is None else array('h', init)  # signed short\ndef u16a(init = None):\
    \ return array('H') if init is None else array('H', init)  # unsigned short\n\
    def i32a(init = None): return array('i') if init is None else array('i', init)\
    \  # signed int\ndef u32a(init = None): return array('I') if init is None else\
    \ array('I', init)  # unsigned int\ndef i64a(init = None): return array('q') if\
    \ init is None else array('q', init)  # signed long long\n# def u64a(init = None):\
    \ return array('Q') if init is None else array('Q', init)  # unsigned long long\n\
    def f32a(init = None): return array('f') if init is None else array('f', init)\
    \  # float\ndef f64a(init = None): return array('d') if init is None else array('d',\
    \ init)  # double\n\ni8_max = (1 << 7)-1\nu8_max = (1 << 8)-1\ni16_max = (1 <<\
    \ 15)-1\nu16_max = (1 << 16)-1\ni32_max = (1 << 31)-1\nu32_max = (1 << 32)-1\n\
    i64_max = (1 << 63)-1\nu64_max = (1 << 64)-1\n\ndef elist(est_len: int) -> list:\
    \ ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n\
    \        return []\nelist = newlist_hint\n    \n\nclass Permutation(FunctionalGraph):\n\
    \    def inv(P):\n        Pinv = [0]*P.N\n        for i,p in enumerate(P):\n \
    \           Pinv[p] = i\n        return type(P)(Pinv)\n"
  code: "import cp_library.alg.graph.__header__\nfrom cp_library.alg.graph.functional_graph_cls\
    \ import FunctionalGraph\n\nclass Permutation(FunctionalGraph):\n    def inv(P):\n\
    \        Pinv = [0]*P.N\n        for i,p in enumerate(P):\n            Pinv[p]\
    \ = i\n        return type(P)(Pinv)"
  dependsOn:
  - cp_library/alg/graph/functional_graph_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/iter/slice_iterator_reverse_cls.py
  - cp_library/ds/array_init_fn.py
  - cp_library/ds/elist_fn.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/permutation_cls.py
  requiredBy: []
  timestamp: '2025-01-16 09:57:28+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/atcoder/abc/abc175_d_permutation.test.py
documentation_of: cp_library/alg/graph/permutation_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/permutation_cls.py
- /library/cp_library/alg/graph/permutation_cls.py.html
title: cp_library/alg/graph/permutation_cls.py
---
