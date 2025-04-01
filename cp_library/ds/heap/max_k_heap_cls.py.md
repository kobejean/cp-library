---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heap_proto.py
    title: cp_library/ds/heap/heap_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/k_heap_mixin.py
    title: cp_library/ds/heap/k_heap_mixin.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/min_heap_cls.py
    title: cp_library/ds/heap/min_heap_cls.py
  - icon: ':question:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc249_f_max_k_heap.test.py
    title: test/atcoder/abc/abc249_f_max_k_heap.test.py
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
    from typing import Iterable, TypeVar\n\nfrom collections import UserList\nfrom\
    \ heapq import heapify, heappop, heappush, heappushpop, heapreplace\nfrom typing\
    \ import Generic\n_T = TypeVar('T')\n\nclass HeapProtocol(Generic[_T]):\n    def\
    \ pop(self) -> _T: ...\n    def push(self, item: _T): ...\n    def pushpop(self,\
    \ item: _T) -> _T: ...\n    def replace(self, item: _T) -> _T: ...\n\nclass MinHeap(HeapProtocol[_T],\
    \ UserList[_T]):\n    def __init__(self, iterable: Iterable = None):\n       \
    \ super().__init__(iterable)\n        heapify(self.data)\n    \n    def pop(self):\
    \ return heappop(self.data)\n    def push(self, item: _T): heappush(self.data,\
    \ item)\n    def pushpop(self, item: _T): return heappushpop(self.data, item)\n\
    \    def replace(self, item: _T): return heapreplace(self.data, item)\nfrom typing\
    \ import Union\n\n\nimport typing\nfrom collections import deque\nfrom numbers\
    \ import Number\nfrom types import GenericAlias \nfrom typing import Callable,\
    \ Collection, Iterator, Union\nimport os\nimport sys\nfrom io import BytesIO,\
    \ IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines = 0\n\n\
    \    def __init__(self, file):\n        self._fd = file.fileno()\n        self.buffer\
    \ = BytesIO()\n        self.writable = \"x\" in file.mode or \"r\" not in file.mode\n\
    \        self.write = self.buffer.write if self.writable else None\n\n    def\
    \ read(self):\n        BUFSIZE = self.BUFSIZE\n        while True:\n         \
    \   b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n        \
    \    if not b:\n                break\n            ptr = self.buffer.tell()\n\
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
    \ = IOWrapper(sys.stdout)\n\nclass TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\
    \n    def __init__(self):\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self._line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self._line())\n\
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
    \ return cls(next(ts))\n        return parser\n\nclass KHeapMixin(HeapProtocol[_T],\
    \ Parsable):\n    '''KHeapMixin[K: int, T: type, N: Union[int,None]]'''\n    def\
    \ __init__(heap, K: int):\n        heap.K = K\n\n    def added(heap, item: _T):\
    \ ...\n\n    def removed(heap, item: _T): ...\n    \n    def pop(heap):\n    \
    \    item = super().pop()\n        heap.removed(item)\n        return item\n \
    \   \n    def push(heap, item: _T):\n        if len(heap) < heap._K:\n       \
    \     heap.added(item)\n            super().push(item)\n        elif heap._K:\n\
    \            assert len(heap) == heap._K, f'{len(heap)=} {heap._K}'\n        \
    \    heap.pushpop(item)\n    \n    def pushpop(heap, item: _T):\n        if item\
    \ != (remove := super().pushpop(item)):\n            heap.removed(remove)\n  \
    \          heap.added(item)\n            return remove\n        else:\n      \
    \      return item\n    \n    def replace(heap, item: _T):\n        remove = super().replace(item)\n\
    \        heap.removed(remove)\n        heap.added(item)\n        return remove\n\
    \    \n    \n    @property\n    def K(heap):\n        return heap._K\n\n    @K.setter\n\
    \    def K(heap, K):\n        heap._K = K\n        if K is not None:\n       \
    \     while len(heap) > K:\n                heap.pop()\n    \n    @classmethod\n\
    \    def compile(cls, K: int, T: type, N: Union[int,None] = None):\n        elm\
    \ = Parser.compile(T)\n        if N is None:\n            def parse(ts: TokenStream):\n\
    \                return cls(K, (elm(ts) for _ in ts.wait()))\n        else:\n\
    \            def parse(ts: TokenStream):\n                return cls(K, (elm(ts)\
    \ for _ in range(N)))\n        return parse\n\nclass MaxKHeap(KHeapMixin[_T],\
    \ MinHeap[_T]):\n    '''MaxKHeap[K: int, T: type, N: Union[int,None]]'''\n\n \
    \   def __init__(self, K: int, iterable: Iterable[_T] = None):\n        MinHeap.__init__(self,\
    \ iterable)\n        KHeapMixin.__init__(self, K)\n"
  code: "import cp_library.ds.heap.__header__\nfrom typing import Iterable, TypeVar\n\
    \nfrom cp_library.ds.heap.min_heap_cls import MinHeap\nfrom cp_library.ds.heap.k_heap_mixin\
    \ import KHeapMixin\nfrom cp_library.misc.typing import _T\n\nclass MaxKHeap(KHeapMixin[_T],\
    \ MinHeap[_T]):\n    '''MaxKHeap[K: int, T: type, N: Union[int,None]]'''\n\n \
    \   def __init__(self, K: int, iterable: Iterable[_T] = None):\n        MinHeap.__init__(self,\
    \ iterable)\n        KHeapMixin.__init__(self, K)\n"
  dependsOn:
  - cp_library/ds/heap/min_heap_cls.py
  - cp_library/ds/heap/k_heap_mixin.py
  - cp_library/ds/heap/heap_proto.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/ds/heap/max_k_heap_cls.py
  requiredBy: []
  timestamp: '2025-04-02 01:29:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc249_f_max_k_heap.test.py
documentation_of: cp_library/ds/heap/max_k_heap_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/max_k_heap_cls.py
- /library/cp_library/ds/heap/max_k_heap_cls.py.html
title: cp_library/ds/heap/max_k_heap_cls.py
---
