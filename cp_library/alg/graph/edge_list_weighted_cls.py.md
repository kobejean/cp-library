---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_list_cls.py
    title: cp_library/alg/graph/edge_list_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_weighted_cls.py
    title: cp_library/alg/graph/edge_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_edges_weighted_fn.py
    title: cp_library/io/read_edges_weighted_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_2_a_kruskal_heap.test.py
    title: test/aoj/grl/grl_2_a_kruskal_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_2_a_kruskal_sort.test.py
    title: test/aoj/grl/grl_2_a_kruskal_sort.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_2_b_edmonds_branching.test.py
    title: test/aoj/grl/grl_2_b_edmonds_branching.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nfrom typing import TypeVar\n\n\nimport typing\nfrom collections import deque\n\
    from numbers import Number\nfrom types import GenericAlias \nfrom typing import\
    \ Callable, Collection, Iterator, TypeVar, Union\nimport os\nimport sys\nfrom\
    \ io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n \
    \   newlines = 0\n\n    def __init__(self, file):\n        self._fd = file.fileno()\n\
    \        self.buffer = BytesIO()\n        self.writable = \"x\" in file.mode or\
    \ \"r\" not in file.mode\n        self.write = self.buffer.write if self.writable\
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
    \ Parser.compile_collection(type(spec), args)\n        elif isinstance(fn := spec,\
    \ Callable): \n            def parse(ts: TokenStream):\n                return\
    \ fn(next(ts))\n            return parse\n        else:\n            raise NotImplementedError()\n\
    \n    @staticmethod\n    def compile_line(cls: T, spec=int) -> ParseFn[T]:\n \
    \       if spec is int:\n            fn = Parser.compile(spec)\n            def\
    \ parse(ts: TokenStream):\n                return cls((int(token) for token in\
    \ ts.line()))\n            return parse\n        else:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream):\n                return cls((fn(ts) for\
    \ _ in ts.wait()))\n            return parse\n\n    @staticmethod\n    def compile_repeat(cls:\
    \ T, spec, N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream):\n            return cls((fn(ts) for _ in range(N)))\n        return\
    \ parse\n\n    @staticmethod\n    def compile_children(cls: T, specs) -> ParseFn[T]:\n\
    \        fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(ts:\
    \ TokenStream):\n            return cls((fn(ts) for fn in fns))  \n        return\
    \ parse\n            \n    @staticmethod\n    def compile_tuple(cls: type[T],\
    \ specs) -> ParseFn[T]:\n        if isinstance(specs, (tuple,list)) and len(specs)\
    \ == 2 and specs[1] is ...:\n            return Parser.compile_line(cls, specs[0])\n\
    \        else:\n            return Parser.compile_children(cls, specs)\n\n   \
    \ @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 \n\
    \            and isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls,\
    \ specs[0], specs[1])\n        else:\n            raise NotImplementedError()\n\
    \nclass Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(ts:\
    \ TokenStream):\n            return cls(next(ts))\n        return parser\n\nclass\
    \ Edge(tuple, Parsable):\n    @classmethod\n    def compile(cls, I=-1):\n    \
    \    def parse(ts: TokenStream):\n            u,v = ts.line()\n            return\
    \ cls((int(u)+I,int(v)+I))\n        return parse\n\nE = TypeVar('E', bound=Edge)\n\
    M = TypeVar('M', bound=int)\n\nclass EdgeCollection(Parsable):\n    @classmethod\n\
    \    def compile(cls, M: M, E: E = Edge[-1]):\n        if isinstance(I := E, int):\n\
    \            E = Edge[I]\n        edge = Parser.compile(E)\n        def parse(ts:\
    \ TokenStream):\n            return cls(edge(ts) for _ in range(M))\n        return\
    \ parse\n\nclass EdgeList(EdgeCollection, list[E]):\n    pass\n\nclass EdgeSet(EdgeCollection,\
    \ set[E]):\n    pass\n\n\nfrom functools import total_ordering \n\n@total_ordering\n\
    class EdgeWeighted(Edge):\n    def __lt__(self, other: tuple) -> bool:\n     \
    \   a = self[2],self[0],self[1]\n        b = other[2],other[0],other[1]\n    \
    \    return a < b\n    \n    @classmethod\n    def compile(cls, I=-1):\n     \
    \   def parse(ts: TokenStream):\n            u,v,w = ts.line()\n            return\
    \ cls((int(u)+I, int(v)+I, int(w)))\n        return parse\n\nM = TypeVar('M',\
    \ bound=int)\nEw = TypeVar('Ew', bound=EdgeWeighted)\nclass EdgeCollectionWeighted(EdgeCollection):\n\
    \    @classmethod\n    def compile(cls, M: M, Ew: Ew = EdgeWeighted[-1]):\n  \
    \      if isinstance(I := Ew, int):\n            Ew = EdgeWeighted[I]\n      \
    \  return super().compile(M, Ew)\n\nclass EdgeListWeighted(EdgeCollectionWeighted,\
    \ list[Ew]):\n    pass\n\nclass EdgeSetWeighted(EdgeCollectionWeighted, set[Ew]):\n\
    \    pass\n"
  code: "import cp_library.alg.graph.__header__\n\nfrom typing import TypeVar\nfrom\
    \ cp_library.alg.graph.edge_list_cls import EdgeCollection\nfrom cp_library.alg.graph.edge_weighted_cls\
    \ import EdgeWeighted\n\nM = TypeVar('M', bound=int)\nEw = TypeVar('Ew', bound=EdgeWeighted)\n\
    class EdgeCollectionWeighted(EdgeCollection):\n    @classmethod\n    def compile(cls,\
    \ M: M, Ew: Ew = EdgeWeighted[-1]):\n        if isinstance(I := Ew, int):\n  \
    \          Ew = EdgeWeighted[I]\n        return super().compile(M, Ew)\n\nclass\
    \ EdgeListWeighted(EdgeCollectionWeighted, list[Ew]):\n    pass\n\nclass EdgeSetWeighted(EdgeCollectionWeighted,\
    \ set[Ew]):\n    pass"
  dependsOn:
  - cp_library/alg/graph/edge_list_cls.py
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/edge_list_weighted_cls.py
  requiredBy:
  - cp_library/io/read_edges_weighted_fn.py
  timestamp: '2024-12-30 17:25:46+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_2_a_kruskal_heap.test.py
  - test/aoj/grl/grl_2_b_edmonds_branching.test.py
  - test/aoj/grl/grl_2_a_kruskal_sort.test.py
documentation_of: cp_library/alg/graph/edge_list_weighted_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/edge_list_weighted_cls.py
- /library/cp_library/alg/graph/edge_list_weighted_cls.py.html
title: cp_library/alg/graph/edge_list_weighted_cls.py
---
