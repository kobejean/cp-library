---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_list_cls.py
    title: cp_library/alg/graph/edge_list_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_list_weighted_cls.py
    title: cp_library/alg/graph/edge_list_weighted_cls.py
  - icon: ':question:'
    path: cp_library/alg/graph/edge_weighted_cls.py
    title: cp_library/alg/graph/edge_weighted_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':question:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_2_b_edmonds_branching.test.py
    title: test/grl_2_b_edmonds_branching.test.py
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
    \nimport sys\nfrom typing import Iterator, Type, TypeVar, overload\n\nimport typing\n\
    from collections import deque\nfrom numbers import Number\nfrom typing import\
    \ Callable, Collection, Iterator, TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n\
    \    def __init__(self, stream = sys.stdin):\n        self.stream = stream\n \
    \       self.queue = deque()\n\n    def __next__(self):\n        if not self.queue:\
    \ self.queue.extend(self.line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return next(self.stream).rstrip().split()\n        \n\
    T = TypeVar('T')\nParseFn: TypeAlias = Callable[[TokenStream],T]\nclass Parser:\n\
    \    def __init__(self, spec: type[T]|T):\n        self.parse = Parser.compile(spec)\n\
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
    \    def compile(spec: type[T]|T=int) -> ParseFn[T]:\n        if isinstance(spec,\
    \ type):\n            cls = typing.get_origin(spec) or spec\n            args\
    \ = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream):\n                return\
    \ cls(next(ts)) + offset\n            return parse\n        elif isinstance(args\
    \ := spec, tuple):      \n            return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection):  \n            return\
    \ Parser.compile_collection(type(spec), args)\n        else:\n            raise\
    \ NotImplementedError()\n    \n    @staticmethod\n    def compile_line(cls: T,\
    \ spec=int) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        # @parse_stride(stride=inf)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in ts.wait())\n\
    \        return parse\n\n    @staticmethod\n    def compile_repeat(cls: T, spec,\
    \ N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        # @parse_stride(stride=fn.stride*N)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in range(N))\n\
    \        return parse\n\n    @staticmethod\n    def compile_children(cls: T, specs)\
    \ -> ParseFn[T]:\n        fns = tuple(Parser.compile(spec) for spec in specs)\
    \ \n        # @parse_stride(stride=sum(fn.stride for fn in fns))\n        def\
    \ parse(ts: TokenStream):\n            return cls(fn(ts) for fn in fns)  \n  \
    \      return parse\n\n    @staticmethod\n    def compile_tuple(cls: type[T],\
    \ specs) -> ParseFn[T]:\n        match specs:\n            case [spec, end] if\
    \ end is ...:\n                return Parser.compile_line(cls, spec)\n       \
    \     case specs:   \n                return Parser.compile_children(cls, specs)\n\
    \    \n    @staticmethod\n    def compile_collection(cls, specs):\n        match\
    \ specs:\n            case [ ] | [_] | set():\n                return Parser.compile_line(cls,\
    \ *specs)\n            case [spec, int() as n]:\n                return Parser.compile_repeat(cls,\
    \ spec, n)\n            case _:\n                raise NotImplementedError()\n\
    \n        \nclass Parsable:\n    @classmethod\n    def compile(cls):\n       \
    \ # @parse_stride(stride=1)\n        def parser(ts: TokenStream):\n          \
    \  return cls(next(ts))\n        return parser\n\nT = TypeVar('T')\n@overload\n\
    def read(spec: int|None) -> Iterator[int]: ...\n@overload\ndef read(spec: Type[T]|T)\
    \ -> T: ...\ndef read(spec: Type[T]|T=None):\n    match spec:\n        case None:\n\
    \            return map(int, input().split())\n        case int(i0):\n       \
    \     return (int(s)-i0 for s in input().split())\n        case _:\n         \
    \   stream = TokenStream(sys.stdin)\n            parser: T = Parser.compile(spec)\n\
    \            return parser(stream)\n\n\n\n\nH = TypeVar('H')\nclass Edge(tuple,\
    \ Parsable):\n    @property\n    def u(self) -> int: return self[0]\n    @property\n\
    \    def v(self) -> int: return self[1]\n    @property\n    def forw(self) ->\
    \ H: return self[1]\n    @property\n    def back(self) -> H: return self[0]\n\
    \    @classmethod\n    def compile(cls, I=1):\n        def parse(ts: TokenStream):\n\
    \            return cls((int(s)-I for s in ts.line()))\n        return parse\n\
    \nE = TypeVar('E', bound=Edge)\nM = TypeVar('M', bound=int)\n\nclass EdgeCollection(Parsable):\n\
    \    @classmethod\n    def compile(cls, M: M, E: E = Edge[-1]):\n        if isinstance(I\
    \ := E, int):\n            E = Edge[I]\n        edge = Parser.compile(E)\n   \
    \     def parse(ts: TokenStream):\n            return cls(edge(ts) for _ in range(M))\n\
    \        return parse\n\nclass EdgeList(EdgeCollection, list[E]):\n    pass\n\n\
    class EdgeSet(EdgeCollection, set[E]):\n    pass\n\n\nclass EdgeWeighted(Edge,\
    \ Parsable):\n    H: TypeAlias = tuple[int,int]\n    @property\n    def w(self):\
    \ return self[0]\n    @property\n    def u(self): return self[1]\n    @property\n\
    \    def v(self): return self[2]\n    @property\n    def forw(self) -> H: return\
    \ self[0], self[2]\n    @property\n    def back(self) -> H: return self[0], self[1]\n\
    \    @classmethod\n    def compile(cls, I=1):\n        def parse(ts: TokenStream):\n\
    \            u,v,w = map(int,ts.line())\n            return cls((w,u-I,v-I))\n\
    \        return parse\n\nM = TypeVar('M', bound=int)\nEw = TypeVar('Ew', bound=EdgeWeighted)\n\
    class EdgeCollectionWeighted(EdgeCollection):\n    @classmethod\n    def compile(cls,\
    \ M: M, Ew: Ew = EdgeWeighted[-1]):\n        if isinstance(I := Ew, int):\n  \
    \          Ew = EdgeWeighted[I]\n        return super().compile(M, Ew)\n\nclass\
    \ EdgeListWeighted(EdgeCollectionWeighted, list[Ew]):\n    pass\n\nclass EdgeSetWeighted(EdgeCollectionWeighted,\
    \ set[Ew]):\n    pass\n\ndef read_edges(M, I=-1):\n    return read(EdgeListWeighted[M,I])\n"
  code: "import cp_library.io.__header__\nfrom cp_library.io.read_specs_fn import\
    \ read\nfrom cp_library.alg.graph.edge_list_weighted_cls import EdgeListWeighted\n\
    \ndef read_edges(M, I=-1):\n    return read(EdgeListWeighted[M,I])\n"
  dependsOn:
  - cp_library/io/read_specs_fn.py
  - cp_library/alg/graph/edge_list_weighted_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_list_cls.py
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: false
  path: cp_library/io/read_edges_weighted_fn.py
  requiredBy: []
  timestamp: '2024-09-21 16:44:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_2_b_edmonds_branching.test.py
documentation_of: cp_library/io/read_edges_weighted_fn.py
layout: document
redirect_from:
- /library/cp_library/io/read_edges_weighted_fn.py
- /library/cp_library/io/read_edges_weighted_fn.py.html
title: cp_library/io/read_edges_weighted_fn.py
---
