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
    path: cp_library/alg/graph/edge_list_weighted_cls.py
    title: cp_library/alg/graph/edge_list_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_weighted_cls.py
    title: cp_library/alg/graph/edge_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/kruskal_heap_fn.py
    title: cp_library/alg/graph/kruskal_heap_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/legacy/read_specs_fn.py
    title: cp_library/io/legacy/read_specs_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A\n\
    \ndef main():\n    N, M = read()\n    E = read(EdgeListWeighted[M,0])\n    MST\
    \ = kruskal(E, N)\n    ans = sum(w for *_,w in MST)\n    print(ans)\n\n'''\n\u257A\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n         \
    \    https://kobejean.github.io/cp-library               \n'''\n\nimport sys\n\
    from typing import Type, TypeVar\n\nT = TypeVar('T')\ndef read(spec: Type[T]|T=[int])\
    \ -> T:\n    stream = TokenStream(sys.stdin)\n    parser = Parser.compile(spec)\n\
    \    return parser(stream)\n\nfrom io import TextIOBase\n\nimport typing\nfrom\
    \ collections import deque\nfrom numbers import Number\nfrom types import GenericAlias\
    \ \nfrom typing import Callable, Collection, Iterator, TypeAlias, TypeVar\n\n\
    class TokenStream(Iterator):\n    def __init__(self, stream: TextIOBase = sys.stdin):\n\
    \        self.queue = deque()\n        self.stream = stream\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return sys.stdin.readline().split()\n\n    def n_uints(self,\
    \ n: int, shift = 0, max_digits: int = 20):\n        # sync buffers\n        tokens:\
    \ list[str] = []\n        while (lim := sys.stdin.buffer.tell() - sys.stdin.tell())\
    \ and len(tokens) < n:\n            residual_str: str = sys.stdin.readline(lim)\n\
    \            tokens.extend(residual_str.split())\n        \n        result = [0]\
    \ * n\n        pos = 0\n        \n        # Process residual string and check\
    \ for partial token\n        partial = None\n        if tokens:\n            if\
    \ not residual_str[-1].isspace():\n                partial = tokens.pop()\n  \
    \          for pos, token in enumerate(tokens):\n                result[pos] =\
    \ int(token)+shift\n            pos += 1\n        # Process remaining data token\
    \ by token\n        stdin_buffer = sys.stdin.buffer\n        num = int(partial)\
    \ if partial else 0\n        have_digit = partial is not None\n\n        original_chunk_size\
    \ = sys.stdin._CHUNK_SIZE\n        sys.stdin._CHUNK_SIZE = max(original_chunk_size,\
    \ max_digits * (n - pos))\n        \n        while pos < n:\n            byte\
    \ = stdin_buffer.read(1)\n\n            match byte[0]:\n                case 10\
    \ | 32:\n                    if have_digit:\n                        result[pos]\
    \ = num+shift\n                        pos += 1\n                        num =\
    \ 0\n                        have_digit = False\n                case char:  #\
    \ digit\n                    num = (num * 10) + (char - 48)\n                \
    \    have_digit = True\n\n        if have_digit:\n            result[pos] = num+shift\n\
    \            pos += 1\n\n        sys.stdin._CHUNK_SIZE = original_chunk_size \n\
    \        if pos < n:\n            raise EOFError(f\"Only found {pos} numbers,\
    \ expected {n}\")\n            \n        return result\n    \n    def n_ints(self,\
    \ n: int, shift = 0, max_digits: int = 20):\n        # sync buffers\n        tokens:\
    \ list[str] = []\n        while (lim := sys.stdin.buffer.tell() - sys.stdin.tell())\
    \ and len(tokens) < n:\n            residual_str: str = sys.stdin.readline(lim)\n\
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
    \            return cls(next(ts))\n        return parser\n\n\nfrom heapq import\
    \ heapify, heappop\n\n\nclass DSU:\n    def __init__(self, n):\n        self.n\
    \ = n\n        self.par = [-1] * n\n\n    def merge(self, u, v, src = False):\n\
    \        assert 0 <= u < self.n\n        assert 0 <= v < self.n\n\n        x,\
    \ y = self.leader(u), self.leader(v)\n        if x == y: return (x,y) if src else\
    \ x\n\n        if -self.par[x] < -self.par[y]:\n            x, y = y, x\n\n  \
    \      self.par[x] += self.par[y]\n        self.par[y] = x\n\n        return (x,y)\
    \ if src else x\n\n    def same(self, u: int, v: int):\n        assert 0 <= u\
    \ < self.n\n        assert 0 <= v < self.n\n        return self.leader(u) == self.leader(v)\n\
    \n    def leader(self, i) -> int:\n        assert 0 <= i < self.n\n\n        p\
    \ = self.par[i]\n        while p >= 0:\n            if self.par[p] < 0:\n    \
    \            return p\n            self.par[i], i, p = self.par[p], self.par[p],\
    \ self.par[self.par[p]]\n\n        return i\n\n    def size(self, i) -> int:\n\
    \        assert 0 <= i < self.n\n        \n        return -self.par[self.leader(i)]\n\
    \n    def groups(self) -> list[list[int]]:\n        leader_buf = [self.leader(i)\
    \ for i in range(self.n)]\n\n        result = [[] for _ in range(self.n)]\n  \
    \      for i in range(self.n):\n            result[leader_buf[i]].append(i)\n\n\
    \        return list(filter(lambda r: r, result))\n\ndef kruskal(E, N):\n    heapify(E)\n\
    \    dsu = DSU(N)\n    MST = []\n    need = N-1\n    while E and need:\n     \
    \   edge = heappop(E)\n        u,v,_ = edge\n        if not dsu.same(u,v):\n \
    \           dsu.merge(u,v)\n            MST.append(edge)\n            need -=\
    \ 1\n    return MST\n\n\n\nclass Edge(tuple, Parsable):\n    @classmethod\n  \
    \  def compile(cls, I=-1):\n        def parse(ts: TokenStream):\n            u,v\
    \ = ts.line()\n            return cls((int(u)+I,int(v)+I))\n        return parse\n\
    \nE = TypeVar('E', bound=Edge)\nM = TypeVar('M', bound=int)\n\nclass EdgeCollection(Parsable):\n\
    \    @classmethod\n    def compile(cls, M: M, E: E = Edge[-1]):\n        if isinstance(I\
    \ := E, int):\n            E = Edge[I]\n        edge = Parser.compile(E)\n   \
    \     def parse(ts: TokenStream):\n            return cls(edge(ts) for _ in range(M))\n\
    \        return parse\n\nclass EdgeList(EdgeCollection, list[E]):\n    pass\n\n\
    class EdgeSet(EdgeCollection, set[E]):\n    pass\n\n\nfrom functools import total_ordering\
    \ \n\n@total_ordering\nclass EdgeWeighted(Edge):\n    def __lt__(self, other:\
    \ tuple) -> bool:\n        a = self[2],self[0],self[1]\n        b = other[2],other[0],other[1]\n\
    \        return a < b\n    \n    @classmethod\n    def compile(cls, I=-1):\n \
    \       def parse(ts: TokenStream):\n            u,v,w = ts.line()\n         \
    \   return cls((int(u)+I, int(v)+I, int(w)))\n        return parse\n\nM = TypeVar('M',\
    \ bound=int)\nEw = TypeVar('Ew', bound=EdgeWeighted)\nclass EdgeCollectionWeighted(EdgeCollection):\n\
    \    @classmethod\n    def compile(cls, M: M, Ew: Ew = EdgeWeighted[-1]):\n  \
    \      if isinstance(I := Ew, int):\n            Ew = EdgeWeighted[I]\n      \
    \  return super().compile(M, Ew)\n\nclass EdgeListWeighted(EdgeCollectionWeighted,\
    \ list[Ew]):\n    pass\n\nclass EdgeSetWeighted(EdgeCollectionWeighted, set[Ew]):\n\
    \    pass\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A\n\
    \ndef main():\n    N, M = read()\n    E = read(EdgeListWeighted[M,0])\n    MST\
    \ = kruskal(E, N)\n    ans = sum(w for *_,w in MST)\n    print(ans)\n\nfrom cp_library.io.legacy.read_specs_fn\
    \ import read\nfrom cp_library.alg.graph.kruskal_heap_fn import kruskal\nfrom\
    \ cp_library.alg.graph.edge_list_weighted_cls import EdgeListWeighted\n\nif __name__\
    \ == '__main__':\n    main()"
  dependsOn:
  - cp_library/io/legacy/read_specs_fn.py
  - cp_library/alg/graph/kruskal_heap_fn.py
  - cp_library/alg/graph/edge_list_weighted_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/ds/dsu_cls.py
  - cp_library/alg/graph/edge_list_cls.py
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: true
  path: test/grl_2_a_kruskal_heap.test.py
  requiredBy: []
  timestamp: '2024-11-16 19:58:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_2_a_kruskal_heap.test.py
layout: document
redirect_from:
- /verify/test/grl_2_a_kruskal_heap.test.py
- /verify/test/grl_2_a_kruskal_heap.test.py.html
title: test/grl_2_a_kruskal_heap.test.py
---
