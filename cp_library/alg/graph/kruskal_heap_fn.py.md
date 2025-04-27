---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/csr/csr_incremental_cls.py
    title: cp_library/ds/csr/csr_incremental_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/fast_heapq.py
    title: cp_library/ds/heap/fast_heapq.py
  - icon: ':question:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_2_a_kruskal_heap.test.py
    title: test/aoj/grl/grl_2_a_kruskal_heap.test.py
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
    \n\n\n\ndef heappush(heap: list, item):\n    heap.append(item)\n    heapsiftdown(heap,\
    \ 0, len(heap)-1)\n\ndef heappop(heap: list):\n    item = heap.pop()\n    if heap:\
    \ item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapreplace(heap:\
    \ list, item):\n    item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return\
    \ item\n\ndef heappushpop(heap: list, item):\n    if heap and heap[0] < item:\
    \ item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapify(x:\
    \ list):\n    for i in reversed(range(len(x)//2)): heapsiftup(x, i)\n\ndef heapsiftdown(heap:\
    \ list, root: int, pos: int):\n    item = heap[pos]\n    while root < pos and\
    \ item < heap[p := (pos-1)>>1]: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\
    \ndef heapsiftup(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and heap[c] < item: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\ndef heappop_max(heap: list):\n    item\
    \ = heap.pop()\n    if heap: item, heap[0] = heap[0], item; heapsiftup_max(heap,\
    \ 0)\n    return item\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heapify_max(x:\
    \ list):\n    for i in reversed(range(len(x)//2)): heapsiftup_max(x, i)\n\ndef\
    \ heappush_max(heap: list, item):\n    heap.append(item); heapsiftdown_max(heap,\
    \ 0, len(heap)-1)\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heappushpop_max(heap:\
    \ list, item):\n    if heap and heap[0] > item: item, heap[0] = heap[0], item;\
    \ heapsiftup_max(heap, 0)\n    return item\n\ndef heapsiftdown_max(heap: list,\
    \ root: int, pos: int):\n    item = heap[pos]\n    while root < pos and heap[p\
    \ := (pos-1)>>1] < item: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\n\
    def heapsiftup_max(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and item < heap[c := c+(heap[c]<heap[c+1])]: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and item < heap[c]: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\n# def heapsiftdown(heap: list, root: int,\
    \ pos: int):\n#     item = heap[pos]\n#     while root < pos and item < heap[p\
    \ := (pos-1)>>1]: heap[pos], pos = heap[p], p\n#     heap[pos] = item\n\n# def\
    \ heapsiftup(heap: list, pos: int):\n#     n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n#     while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n#     if c == n and heap[c] < item: heap[pos],\
    \ pos = heap[c], c\n#     heap[pos] = item\nfrom typing import Collection\n\n\
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
    \ self.queue.extend(self._line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self._line())\n\
    \        while self.queue: yield\n \n    def _line(self):\n        return TokenStream.stream.readline().split()\n\
    \n    def line(self):\n        if self.queue:\n            A = list(self.queue)\n\
    \            self.queue.clear()\n            return A\n        return self._line()\n\
    TokenStream.default = TokenStream()\n\nclass CharStream(TokenStream):\n    def\
    \ _line(self):\n        return TokenStream.stream.readline().rstrip()\nCharStream.default\
    \ = CharStream()\n\n\nParseFn = Callable[[TokenStream],_T]\nclass Parser:\n  \
    \  def __init__(self, spec: Union[type[_T],_T]):\n        self.parse = Parser.compile(spec)\n\
    \n    def __call__(self, ts: TokenStream) -> _T:\n        return self.parse(ts)\n\
    \    \n    @staticmethod\n    def compile_type(cls: type[_T], args = ()) -> _T:\n\
    \        if issubclass(cls, Parsable):\n            return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(ts: TokenStream):\
    \ return cls(next(ts))              \n            return parse\n        elif issubclass(cls,\
    \ tuple):\n            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection):\n            return Parser.compile_collection(cls, args)\n    \
    \    elif callable(cls):\n            def parse(ts: TokenStream):\n          \
    \      return cls(next(ts))              \n            return parse\n        else:\n\
    \            raise NotImplementedError()\n    \n    @staticmethod\n    def compile(spec:\
    \ Union[type[_T],_T]=int) -> ParseFn[_T]:\n        if isinstance(spec, (type,\
    \ GenericAlias)):\n            cls = typing.get_origin(spec) or spec\n       \
    \     args = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream): return cls(next(ts)) +\
    \ offset\n            return parse\n        elif isinstance(args := spec, tuple):\
    \      \n            return Parser.compile_tuple(type(spec), args)\n        elif\
    \ isinstance(args := spec, Collection):  \n            return Parser.compile_collection(type(spec),\
    \ args)\n        elif isinstance(fn := spec, Callable): \n            def parse(ts:\
    \ TokenStream): return fn(next(ts))\n            return parse\n        else:\n\
    \            raise NotImplementedError()\n\n    @staticmethod\n    def compile_line(cls:\
    \ _T, spec=int) -> ParseFn[_T]:\n        if spec is int:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream): return cls([int(token) for token in ts.line()])\n\
    \            return parse\n        else:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream): return cls([fn(ts) for _ in ts.wait()])\n\
    \            return parse\n\n    @staticmethod\n    def compile_repeat(cls: _T,\
    \ spec, N) -> ParseFn[_T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream): return cls([fn(ts) for _ in range(N)])\n        return parse\n\
    \n    @staticmethod\n    def compile_children(cls: _T, specs) -> ParseFn[_T]:\n\
    \        fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(ts:\
    \ TokenStream): return cls([fn(ts) for fn in fns])  \n        return parse\n \
    \           \n    @staticmethod\n    def compile_tuple(cls: type[_T], specs) ->\
    \ ParseFn[_T]:\n        if isinstance(specs, (tuple,list)) and len(specs) == 2\
    \ and specs[1] is ...:\n            return Parser.compile_line(cls, specs[0])\n\
    \        else:\n            return Parser.compile_children(cls, specs)\n\n   \
    \ @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and\
    \ isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls, specs[0],\
    \ specs[1])\n        else:\n            raise NotImplementedError()\n\nclass Parsable:\n\
    \    @classmethod\n    def compile(cls):\n        def parser(ts: TokenStream):\
    \ return cls(next(ts))\n        return parser\nfrom typing import Sequence\n\n\
    \nclass CSRIncremental(Sequence[list[_T]]):\n    def __init__(csr, sizes: list[int]):\n\
    \        csr.L, N = [0]*len(sizes), 0\n        for i,sz in enumerate(sizes):\n\
    \            csr.L[i] = N; N += sz\n        csr.R, csr.A = csr.L[:], [0]*N\n\n\
    \    def append(csr, i: int, x: _T):\n        csr.A[csr.R[i]] = x; csr.R[i] +=\
    \ 1\n    \n    def __iter__(csr):\n        for i,l in enumerate(csr.L):\n    \
    \        yield csr.A[l:csr.R[i]]\n    \n    def __getitem__(csr, i: int) -> _T:\n\
    \        return csr.A[i]\n    \n    def __len__(dsu):\n        return len(dsu.L)\n\
    \n    def range(csr, i: int) -> _T:\n        return range(csr.L[i], csr.R[i])\n\
    \nclass DSU(Parsable, Collection):\n    def __init__(dsu, N):\n        dsu.N,\
    \ dsu.cc, dsu.par = N, N, [-1]*N\n\n    def merge(dsu, u, v, src = False):\n \
    \       x, y = dsu.leader(u), dsu.leader(v)\n        if x == y: return (x,y) if\
    \ src else x\n        if dsu.par[x] > dsu.par[y]: x, y = y, x\n        dsu.par[x]\
    \ += dsu.par[y]; dsu.par[y] = x; dsu.cc -= 1\n        return (x,y) if src else\
    \ x\n\n    def same(dsu, u: int, v: int):\n        return dsu.leader(u) == dsu.leader(v)\n\
    \n    def leader(dsu, i) -> int:\n        p = (par := dsu.par)[i]\n        while\
    \ p >= 0:\n            if par[p] < 0: return p\n            par[i], i, p = par[p],\
    \ par[p], par[par[p]]\n        return i\n\n    def size(dsu, i) -> int:\n    \
    \    return -dsu.par[dsu.leader(i)]\n\n    def groups(dsu) -> CSRIncremental[int]:\n\
    \        sizes, row, p = [0]*dsu.cc, [-1]*dsu.N, 0\n        for i in range(dsu.cc):\n\
    \            while dsu.par[p] >= 0: p += 1\n            sizes[i], row[p] = -dsu.par[p],\
    \ i; p += 1\n        csr = CSRIncremental(sizes)\n        for i in range(dsu.N):\
    \ csr.append(row[dsu.leader(i)], i)\n        return csr\n    \n    __iter__ =\
    \ groups\n    \n    def __len__(dsu):\n        return dsu.cc\n    \n    def __contains__(dsu,\
    \ uv):\n        u, v = uv\n        return dsu.same(u, v)\n    \n    @classmethod\n\
    \    def compile(cls, N: int, M: int, shift = -1):\n        def parse_fn(ts: TokenStream):\n\
    \            dsu = cls(N)\n            for _ in range(M):\n                u,\
    \ v = ts._line()\n                dsu.merge(int(u)+shift, int(v)+shift)\n    \
    \        return dsu\n        return parse_fn\n\ndef kruskal(E, N):\n    heapify(E)\n\
    \    dsu = DSU(N)\n    MST = []\n    need = N-1\n    while E and need:\n     \
    \   edge = heappop(E)\n        u,v,_ = edge\n        if not dsu.same(u,v):\n \
    \           dsu.merge(u,v)\n            MST.append(edge)\n            need -=\
    \ 1\n    return MST\n"
  code: "import cp_library.alg.graph.__header__\n\nfrom cp_library.ds.heap.fast_heapq\
    \  import heapify, heappop\nfrom cp_library.ds.dsu_cls import DSU\n\ndef kruskal(E,\
    \ N):\n    heapify(E)\n    dsu = DSU(N)\n    MST = []\n    need = N-1\n    while\
    \ E and need:\n        edge = heappop(E)\n        u,v,_ = edge\n        if not\
    \ dsu.same(u,v):\n            dsu.merge(u,v)\n            MST.append(edge)\n \
    \           need -= 1\n    return MST\n"
  dependsOn:
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/ds/dsu_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/ds/csr/csr_incremental_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/kruskal_heap_fn.py
  requiredBy: []
  timestamp: '2025-04-28 04:02:31+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_2_a_kruskal_heap.test.py
documentation_of: cp_library/alg/graph/kruskal_heap_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/kruskal_heap_fn.py
- /library/cp_library/alg/graph/kruskal_heap_fn.py.html
title: cp_library/alg/graph/kruskal_heap_fn.py
---
