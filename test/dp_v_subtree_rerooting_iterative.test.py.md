---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/rerooting_iterative_cls.py
    title: cp_library/alg/dp/rerooting_iterative_cls.py
  - icon: ':question:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':question:'
    path: cp_library/alg/graph/graph_cls.py
    title: cp_library/alg/graph/graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/bidirectional_array_cls.py
    title: cp_library/ds/bidirectional_array_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':question:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_tree_fn.py
    title: cp_library/io/read_tree_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/dp/tasks/dp_v
    links:
    - https://atcoder.jp/contests/dp/tasks/dp_v
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_v\n\
    \ndef main():\n    N, M = read()\n    T = read_tree(N)\n\n    def mul(a,b):\n\
    \        return a*b%M\n\n    def add_node(v,res):\n        return (res+1)%M\n\n\
    \    rr = ReRootingDP(T, 1, mul, add_node)\n\n    print(*rr.solve(), sep='\\n')\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\nimport\
    \ typing\n\n\nclass BidirectionalArray:\n    def __init__(self, e, op, data):\n\
    \        self.size = len(data)\n        self.prefix = [e] + data.copy()\n    \
    \    self.suffix = data.copy() + [e]\n        self.e = e\n        self.op = op\n\
    \        for i in range(self.size):\n            self.prefix[i+1] = op(self.prefix[i],\
    \ self.prefix[i+1])\n        for i in range(self.size,0,-1):\n            self.suffix[i-1]\
    \ = op(self.suffix[i-1], self.suffix[i])\n    def left(self, l): return self.prefix[l]\n\
    \    def right(self, r): return self.suffix[r]\n    def all(self): return self.prefix[-1]\n\
    \    def out(self, l, r=None):\n        r = l+1 if r is None else r\n        return\
    \ self.op(self.prefix[l], self.suffix[r])\n\nclass ReRootingDP():\n    \"\"\"\
    \ A class implementation of the Re-rooting Dynamic Programming technique. \"\"\
    \"\n    \n    S = typing.TypeVar('S')\n    MergeOp = typing.Callable[[S, S], S]\n\
    \    AddNodeOp = typing.Callable[[int, S], S]\n    AddEdgeOp = typing.Callable[[int,\
    \ int, S], S]\n\n    def __init__(self, T: list[list[int]], e: S,\n          \
    \       merge: MergeOp, \n                 add_node: AddNodeOp = lambda u,s:s,\
    \ \n                 add_edge: AddEdgeOp = lambda u,v,s:s):\n        \"\"\"\n\
    \        T: list[list[int]] - Adjacency list representation of the tree.\n   \
    \     e: S - Identity element for the merge operation.\n        merge: (S,S) ->\
    \ S - Function to merge two states.\n        add_node: (int,S) -> S - Function\
    \ to incorporate a node into the state.\n        add_edge: (int,int,S) -> S -\
    \ Function to incorporate an edge into the state.\n        \"\"\"\n        self.T\
    \ = T\n        self.e = e\n        self.merge = merge\n        self.add_node =\
    \ add_node\n        self.add_edge = add_edge\n\n    def solve(self) -> list[S]:\n\
    \        dp = [[self.e]*len(adj) for adj in self.T]\n        ans = [self.e for\
    \ _ in range(len(self.T))]\n        parent_idx = [None for _ in range(len(self.T))]\n\
    \        child_idx = [None for _ in range(len(self.T))]\n        stack = [(2,0,None),(0,0,None)]\n\
    \        while stack:\n            phase, u, p = stack.pop()\n            match\
    \ phase:\n                case 0:  # Visit children\n                    if p\
    \ is not None:\n                        stack.append((1,u,p))\n              \
    \      for i,v in enumerate(self.T[u]):\n                        if v != p:\n\
    \                            stack.append((0,v,u))\n                         \
    \   child_idx[v] = i\n                        else:\n                        \
    \    parent_idx[u] = i\n                case 1:  # Upward updates\n          \
    \          val = dp[p][child_idx[u]] = self.add_edge(p, u, self.add_node(u, ans[u]))\n\
    \                    ans[p] = self.merge(ans[p], val)\n                case 2:\
    \  # Downward updates\n                    ba = BidirectionalArray(self.e, self.merge,\
    \ dp[u])\n                    for i,v in enumerate(self.T[u]):\n             \
    \           if v != p:\n                            dp[v][parent_idx[v]] = self.add_edge(v,\
    \ u, self.add_node(u, ba.out(i)))\n                            stack.append((2,v,u))\n\
    \                    ans[u] = ba.all()\n        return ans\n\n\nimport sys\nfrom\
    \ typing import Iterator, Type, TypeVar, overload\n\nfrom collections import deque\n\
    from numbers import Number\nfrom typing import Callable, Collection, Iterator,\
    \ TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self, stream\
    \ = sys.stdin):\n        self.stream = stream\n        self.queue = deque()\n\n\
    \    def __next__(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self.line())\n        while self.queue: yield\n\
    \        \n    def line(self):\n        assert not self.queue\n        return\
    \ next(self.stream).rstrip().split()\n        \nT = TypeVar('T')\nParseFn: TypeAlias\
    \ = Callable[[TokenStream],T]\nclass Parser:\n    def __init__(self, spec: type[T]|T):\n\
    \        self.parse = Parser.compile(spec)\n\n    def __call__(self, ts: TokenStream)\
    \ -> T:\n        return self.parse(ts)\n    \n    @staticmethod\n    def compile_type(cls:\
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
    \        # @parse_stride(stride=inf)\n        def parse(ts: TokenStream):\n  \
    \          return cls(fn(ts) for _ in ts.wait())\n        return parse\n\n   \
    \ @staticmethod\n    def compile_repeat(cls: T, spec, N) -> ParseFn[T]:\n    \
    \    fn = Parser.compile(spec)\n        # @parse_stride(stride=fn.stride*N)\n\
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
    \            return parser(stream)\n\n\nH = TypeVar('H')\nclass Edge(tuple, Parsable):\n\
    \    @property\n    def u(self) -> int: return self[0]\n    @property\n    def\
    \ v(self) -> int: return self[1]\n    @property\n    def forw(self) -> H: return\
    \ self[1]\n    @property\n    def back(self) -> H: return self[0]\n    @classmethod\n\
    \    def compile(cls, I=1):\n        def parse(ts: TokenStream):\n           \
    \ return cls((int(s)-I for s in ts.line()))\n        return parse\n\n\nN = TypeVar('N',\
    \ bound=int)\nE = TypeVar('E', bound=Edge)\nclass Graph(list[H], Parsable):\n\
    \    def __init__(G, N: N, edges: list[E]=[]):\n        super().__header__([]\
    \ for _ in range(N))\n        for edge in edges:\n            G[edge.u].append(edge.forw)\n\
    \            G[edge.v].append(edge.back)\n\n    @classmethod\n    def compile(cls,\
    \ N: int, M: int, E: E|int = Edge[-1]):\n        if isinstance(E, int):\n    \
    \        E = Edge[E]\n        edge = Parser.compile(E)\n        def parse(ts:\
    \ TokenStream):\n            return cls(N, (edge(ts) for _ in range(M)))\n   \
    \     return parse\n\n\ndef read_tree(N, i0=1):\n    T: Graph = [[] for _ in range(N)]\n\
    \    for _ in range(N-1):\n        u,v = read(tuple[-i0,-i0])\n        T[u].append(v)\n\
    \        T[v].append(u)\n    return T\n\n\n# from cp_library.io.read_specs_fn\
    \ import read\n# from cp_library.alg.graph.graph_cls import Graph\n\nif __name__\
    \ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_v\n\
    \ndef main():\n    N, M = read()\n    T = read_tree(N)\n\n    def mul(a,b):\n\
    \        return a*b%M\n\n    def add_node(v,res):\n        return (res+1)%M\n\n\
    \    rr = ReRootingDP(T, 1, mul, add_node)\n\n    print(*rr.solve(), sep='\\n')\n\
    \nfrom cp_library.alg.dp.rerooting_iterative_cls import ReRootingDP\nfrom cp_library.io.read_specs_fn\
    \ import read\nfrom cp_library.io.read_tree_fn import read_tree\n\nif __name__\
    \ == '__main__':\n    main()"
  dependsOn:
  - cp_library/alg/dp/rerooting_iterative_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/io/read_tree_fn.py
  - cp_library/ds/bidirectional_array_cls.py
  - cp_library/alg/graph/graph_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: true
  path: test/dp_v_subtree_rerooting_iterative.test.py
  requiredBy: []
  timestamp: '2024-09-21 16:44:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/dp_v_subtree_rerooting_iterative.test.py
layout: document
redirect_from:
- /verify/test/dp_v_subtree_rerooting_iterative.test.py
- /verify/test/dp_v_subtree_rerooting_iterative.test.py.html
title: test/dp_v_subtree_rerooting_iterative.test.py
---