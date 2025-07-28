---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/rev_enumerate_fn.py
    title: cp_library/alg/iter/rev_enumerate_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heap_base_cls.py
    title: cp_library/ds/heap/heap_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heapify_max_fn.py
    title: cp_library/ds/heap/heapify_max_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heappop_max_fn.py
    title: cp_library/ds/heap/heappop_max_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heappush_max_fn.py
    title: cp_library/ds/heap/heappush_max_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heappushpop_max_fn.py
    title: cp_library/ds/heap/heappushpop_max_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heapreplace_max_fn.py
    title: cp_library/ds/heap/heapreplace_max_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heapsiftdown_max_fn.py
    title: cp_library/ds/heap/heapsiftdown_max_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heapsiftup_max_fn.py
    title: cp_library/ds/heap/heapsiftup_max_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/k_heap_mixin.py
    title: cp_library/ds/heap/k_heap_mixin.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/max_heap_cls.py
    title: cp_library/ds/heap/max_heap_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/min_k_heap_cls.py
    title: cp_library/ds/heap/min_k_heap_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_cls.py
    title: cp_library/io/io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_fn.py
    title: cp_library/io/read_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc249/tasks/abc249_f
    links:
    - https://atcoder.jp/contests/abc249/tasks/abc249_f
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc249/tasks/abc249_f\n\
    \n\n\ndef main():\n    N, K = read(tuple[int, ...])\n    ops = read(list[tuple[int,\
    \ ...], N])\n    diff = []\n    x = 0\n    for t, y in ops:\n        match t:\n\
    \            case 1:\n                diff.append(y - x)\n                x =\
    \ y\n            case 2:\n                diff.append(y)\n                x +=\
    \ y\n\n    S = BadOps(K, x)\n    if K:\n        for i,(t,y) in rev_enumerate(ops):\n\
    \            match t:\n                case 1:\n                    S.K -= 1\n\
    \                    S.added(diff[i])\n                    if S.K == 0: break\n\
    \                case 2:\n                    if y < 0:\n                    \
    \    S.push(y)\n    write(S.ans)\n                \n\n'''\n\u257A\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\nfrom typing import Type, Union, overload\nfrom typing import\
    \ TypeVar\n_S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1');\
    \ _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5');\
    \ _T6 = TypeVar('T6')\n\n\n@overload\ndef read() -> list[int]: ...\n@overload\n\
    def read(spec: Type[_T], char=False) -> _T: ...\n@overload\ndef read(spec: _U,\
    \ char=False) -> _U: ...\n@overload\ndef read(*specs: Type[_T], char=False) ->\
    \ tuple[_T, ...]: ...\n@overload\ndef read(*specs: _U, char=False) -> tuple[_U,\
    \ ...]: ...\ndef read(*specs: Union[Type[_T],_T], char=False):\n    IO.stdin.char\
    \ = char\n    if not specs: return IO.stdin.readnumsinto([])\n    parser: _T =\
    \ Parser.compile(specs[0] if len(specs) == 1 else specs)\n    return parser(IO.stdin)\n\
    from os import read as os_read, write as os_write, fstat as os_fstat\nimport sys\n\
    from __pypy__.builders import StringBuilder\n\n\ndef max2(a, b): return a if a\
    \ > b else b\n\nclass IOBase:\n    @property\n    def char(io) -> bool: ...\n\
    \    @property\n    def writable(io) -> bool: ...\n    def __next__(io) -> str:\
    \ ...\n    def write(io, s: str) -> None: ...\n    def readline(io) -> str: ...\n\
    \    def readtoken(io) -> str: ...\n    def readtokens(io) -> list[str]: ...\n\
    \    def readints(io) -> list[int]: ...\n    def readdigits(io) -> list[int]:\
    \ ...\n    def readnums(io) -> list[int]: ...\n    def readchar(io) -> str: ...\n\
    \    def readchars(io) -> str: ...\n    def readinto(io, lst: list[str]) -> list[str]:\
    \ ...\n    def readcharsinto(io, lst: list[str]) -> list[str]: ...\n    def readtokensinto(io,\
    \ lst: list[str]) -> list[str]: ...\n    def readintsinto(io, lst: list[int])\
    \ -> list[int]: ...\n    def readdigitsinto(io, lst: list[int]) -> list[int]:\
    \ ...\n    def readnumsinto(io, lst: list[int]) -> list[int]: ...\n    def wait(io):\
    \ ...\n    def flush(io) -> None: ...\n    def line(io) -> list[str]: ...\n\n\
    class IO(IOBase):\n    BUFSIZE = 1 << 16; stdin: 'IO'; stdout: 'IO'\n    __slots__\
    \ = 'f', 'file', 'B', 'O', 'V', 'S', 'l', 'p', 'char', 'sz', 'st', 'ist', 'writable',\
    \ 'encoding', 'errors'\n    def __init__(io, file):\n        io.file = file\n\
    \        try: io.f = file.fileno(); io.sz, io.writable = max2(io.BUFSIZE, os_fstat(io.f).st_size),\
    \ ('x' in file.mode or 'r' not in file.mode)\n        except: io.f, io.sz, io.writable\
    \ = -1, io.BUFSIZE, False\n        io.B, io.O, io.S = bytearray(), [], StringBuilder();\
    \ io.V = memoryview(io.B); io.l = io.p = 0\n        io.char, io.st, io.ist, io.encoding,\
    \ io.errors = False, [], [], 'ascii', 'ignore'\n    def _dec(io, l, r): return\
    \ io.V[l:r].tobytes().decode(io.encoding, io.errors)\n    def readbytes(io, sz):\
    \ return os_read(io.f, sz)\n    def load(io):\n        while io.l >= len(io.O):\n\
    \            if not (b := io.readbytes(io.sz)):\n                if io.O[-1] <\
    \ len(io.B): io.O.append(len(io.B))\n                break\n            pos =\
    \ len(io.B); io.B.extend(b)\n            while ~(pos := io.B.find(b'\\n', pos)):\
    \ io.O.append(pos := pos+1)\n    def __next__(io):\n        if io.char: return\
    \ io.readchar()\n        else: return io.readtoken()\n    def readchar(io):\n\
    \        io.load(); r = io.O[io.l]\n        c = chr(io.B[io.p])\n        if io.p\
    \ >= r-1: io.p = r; io.l += 1\n        else: io.p += 1\n        return c\n   \
    \ def write(io, s: str): io.S.append(s)\n    def readline(io): io.load(); l, io.p\
    \ = io.p, io.O[io.l]; io.l += 1; return io._dec(l, io.p)\n    def readtoken(io):\n\
    \        io.load(); r = io.O[io.l]\n        if ~(p := io.B.find(b' ', io.p, r)):\
    \ s = io._dec(io.p, p); io.p = p+1\n        else: s = io._dec(io.p, r-1); io.p\
    \ = r; io.l += 1\n        return s\n    def readtokens(io): io.st.clear(); return\
    \ io.readtokensinto(io.st)\n    def readints(io): io.ist.clear(); return io.readintsinto(io.ist)\n\
    \    def readdigits(io): io.ist.clear(); return io.readdigitsinto(io.ist)\n  \
    \  def readnums(io): io.ist.clear(); return io.readnumsinto(io.ist)\n    def readchars(io):\
    \ io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return io._dec(l, io.p-1)\n\
    \    def readinto(io, lst):\n        if io.char: return io.readcharsinto(lst)\n\
    \        else: return io.readtokensinto(lst)\n    def readcharsinto(io, lst):\
    \ lst.extend(io.readchars()); return lst\n    def readtokensinto(io, lst): \n\
    \        io.load(); r = io.O[io.l]\n        while ~(p := io.B.find(b' ', io.p,\
    \ r)): lst.append(io._dec(io.p, p)); io.p = p+1\n        lst.append(io._dec(io.p,\
    \ r-1)); io.p = r; io.l += 1; return lst\n    def _readint(io, r):\n        while\
    \ io.p < r and io.B[io.p] <= 32: io.p += 1\n        if io.p >= r: return None\n\
    \        minus = x = 0\n        if io.B[io.p] == 45: minus = 1; io.p += 1\n  \
    \      while io.p < r and io.B[io.p] >= 48: x = x * 10 + (io.B[io.p] & 15); io.p\
    \ += 1\n        io.p += 1\n        return -x if minus else x\n    def readintsinto(io,\
    \ lst):\n        io.load(); r = io.O[io.l]\n        while io.p < r and (x := io._readint(r))\
    \ is not None: lst.append(x)\n        io.l += 1; return lst\n    def _readdigit(io):\
    \ d = io.B[io.p] & 15; io.p += 1; return d\n    def readdigitsinto(io, lst):\n\
    \        io.load(); r = io.O[io.l]\n        while io.p < r and io.B[io.p] > 32:\
    \ lst.append(io._readdigit())\n        if io.B[io.p] == 10: io.l += 1\n      \
    \  io.p += 1\n        return lst\n    def readnumsinto(io, lst):\n        if io.char:\
    \ return io.readdigitsinto(lst)\n        else: return io.readintsinto(lst)\n \
    \   def line(io): io.st.clear(); return io.readinto(io.st)\n    def wait(io):\n\
    \        io.load(); r = io.O[io.l]\n        while io.p < r: yield\n    def flush(io):\n\
    \        if io.writable: os_write(io.f, io.S.build().encode(io.encoding, io.errors));\
    \ io.S = StringBuilder()\nsys.stdin = IO.stdin = IO(sys.stdin); sys.stdout = IO.stdout\
    \ = IO(sys.stdout)\nimport typing\nfrom numbers import Number\nfrom types import\
    \ GenericAlias \nfrom typing import Callable, Collection\n\nclass Parsable:\n\
    \    @classmethod\n    def compile(cls):\n        def parser(io: 'IOBase'): return\
    \ cls(next(io))\n        return parser\n    @classmethod\n    def __class_getitem__(cls,\
    \ item): return GenericAlias(cls, item)\n\nclass Parser:\n    def __init__(self,\
    \ spec):  self.parse = Parser.compile(spec)\n    def __call__(self, io: IOBase):\
    \ return self.parse(io)\n    @staticmethod\n    def compile_type(cls, args = ()):\n\
    \        if issubclass(cls, Parsable): return cls.compile(*args)\n        elif\
    \ issubclass(cls, (Number, str)):\n            def parse(io: IOBase): return cls(next(io))\
    \              \n            return parse\n        elif issubclass(cls, tuple):\
    \ return Parser.compile_tuple(cls, args)\n        elif issubclass(cls, Collection):\
    \ return Parser.compile_collection(cls, args)\n        elif callable(cls):\n \
    \           def parse(io: IOBase): return cls(next(io))              \n      \
    \      return parse\n        else: raise NotImplementedError()\n    @staticmethod\n\
    \    def compile(spec=int):\n        if isinstance(spec, (type, GenericAlias)):\n\
    \            cls, args = typing.get_origin(spec) or spec, typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(io: IOBase): return cls(next(io)) + offset\n            return\
    \ parse\n        elif isinstance(args := spec, tuple): return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection): return Parser.compile_collection(type(spec),\
    \ args)\n        elif isinstance(fn := spec, Callable): \n            def parse(io:\
    \ IOBase): return fn(next(io))\n            return parse\n        else: raise\
    \ NotImplementedError()\n    @staticmethod\n    def compile_line(cls, spec=int):\n\
    \        if spec is int:\n            def parse(io: IOBase): return cls(io.readnums())\n\
    \        elif spec is str:\n            def parse(io: IOBase): return cls(io.line())\n\
    \        else:\n            fn = Parser.compile(spec)\n            def parse(io:\
    \ IOBase): return cls((fn(io) for _ in io.wait()))\n        return parse\n   \
    \ @staticmethod\n    def compile_repeat(cls, spec, N):\n        fn = Parser.compile(spec)\n\
    \        def parse(io: IOBase): return cls([fn(io) for _ in range(N)])\n     \
    \   return parse\n    @staticmethod\n    def compile_children(cls, specs):\n \
    \       fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(io:\
    \ IOBase): return cls([fn(io) for fn in fns])  \n        return parse\n    @staticmethod\n\
    \    def compile_tuple(cls, specs):\n        if isinstance(specs, (tuple,list))\
    \ and len(specs) == 2 and specs[1] is ...: return Parser.compile_line(cls, specs[0])\n\
    \        else: return Parser.compile_children(cls, specs)\n    @staticmethod\n\
    \    def compile_collection(cls, specs):\n        if not specs or len(specs) ==\
    \ 1 or isinstance(specs, set):\n            return Parser.compile_line(cls, *specs)\n\
    \        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and isinstance(specs[1],\
    \ int)):\n            return Parser.compile_repeat(cls, specs[0], specs[1])\n\
    \        else:\n            raise NotImplementedError()\n\ndef write(*args, **kwargs):\n\
    \    '''Prints the values to a stream, or to stdout_fast by default.'''\n    sep,\
    \ file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IO.stdout)\n    at_start\
    \ = True\n    for x in args:\n        if not at_start:\n            file.write(sep)\n\
    \        file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    from typing import Reversible\n\n\ndef rev_enumerate(A: Reversible, start: int\
    \ = 0):\n    start += (N := len(A))\n    for i in range(N-1,-1,-1):\n        yield\
    \ (start:=start-1), A[i]\n\nfrom typing import Iterable\n\n\ndef heapsiftup_max(heap:\
    \ list, pos: int):\n    n, item, c = len(heap)-1, heap[pos], pos<<1|1\n    while\
    \ c < n and item < heap[c := c+(heap[c]<heap[c+1])]: heap[pos], pos, c = heap[c],\
    \ c, c<<1|1\n    if c == n and item < heap[c]: heap[pos], pos = heap[c], c\n \
    \   heap[pos] = item\n\ndef heapify_max(x: list):\n    for i in reversed(range(len(x)//2)):\
    \ heapsiftup_max(x, i)\n\ndef heappop_max(heap: list):\n    item = heap.pop()\n\
    \    if heap: item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n    return\
    \ item\n\ndef heapsiftdown_max(heap: list, root: int, pos: int):\n    item = heap[pos]\n\
    \    while root < pos and heap[p := (pos-1)>>1] < item: heap[pos], pos = heap[p],\
    \ p\n    heap[pos] = item\n\ndef heappush_max(heap: list, item):\n    heap.append(item);\
    \ heapsiftdown_max(heap, 0, len(heap)-1)\n\ndef heappushpop_max(heap: list, item):\n\
    \    if heap and heap[0] > item: item, heap[0] = heap[0], item; heapsiftup_max(heap,\
    \ 0)\n    return item\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\nfrom typing import\
    \ Generic\n\nclass HeapBase(Generic[_T]):\n    def peek(heap) -> _T: return heap.data[0]\n\
    \    def pop(heap) -> _T: ...\n    def push(heap, item: _T): ...\n    def pushpop(heap,\
    \ item: _T) -> _T: ...\n    def replace(heap, item: _T) -> _T: ...\n    def __contains__(heap,\
    \ item: _T): return item in heap.data\n    def __len__(heap): return len(heap.data)\n\
    \    def clear(heap): heap.data.clear()\n\nclass MaxHeap(HeapBase[_T]):\n    def\
    \ __init__(self, iterable: Iterable[_T] = None): self.data = list(iterable) if\
    \ iterable else []; heapify_max(self.data)\n    def pop(self): return heappop_max(self.data)\n\
    \    def push(self, item: _T): heappush_max(self.data, item)\n    def pushpop(self,\
    \ item: _T): return heappushpop_max(self.data, item)\n    def replace(self, item:\
    \ _T): return heapreplace_max(self.data, item)\n\nclass KHeapMixin(HeapBase[_T],\
    \ Parsable):\n    '''KHeapMixin[K: int, T: type, N: Union[int,None]]'''\n    def\
    \ __init__(heap, K: int): heap.K = K\n    def added(heap, item: _T): ...\n   \
    \ def removed(heap, item: _T): ...\n    def pop(heap): item = super().pop(); heap.removed(item);\
    \ return item\n    def push(heap, item: _T):\n        if len(heap) < heap._K:\
    \ heap.added(item); super().push(item)\n        elif heap._K: heap.pushpop(item)\n\
    \    def pushpop(heap, item: _T):\n        if item != (remove := super().pushpop(item)):\
    \ heap.removed(remove); heap.added(item); return remove\n        else: return\
    \ item\n    def replace(heap, item: _T): remove = super().replace(item); heap.removed(remove);\
    \ heap.added(item); return remove\n    @property\n    def K(heap): return heap._K\n\
    \    @K.setter\n    def K(heap, K):\n        heap._K = K\n        if K is not\
    \ None:\n            while len(heap) > K: heap.pop()\n    @classmethod\n    def\
    \ compile(cls, K: int, T: type, N: Union[int,None] = None):\n        elm = Parser.compile(T)\n\
    \        if N is None:\n            def parse(io: IOBase): return cls(K, (elm(io)\
    \ for _ in io.wait()))\n        else:\n            def parse(io: IOBase): return\
    \ cls(K, (elm(io) for _ in range(N)))\n        return parse\n\nclass MinKHeap(KHeapMixin[_T],\
    \ MaxHeap[_T]):\n    '''MinKHeap[K: int, T: type, N: Union[int,None]]'''\n   \
    \ def __init__(self, K: int, iterable: Iterable[_T] = None):\n        MaxHeap.__init__(self,\
    \ iterable)\n        KHeapMixin.__init__(self, K)\n\nclass BadOps(MinKHeap[int]):\n\
    \    def __init__(self, K: int, x: int):\n        super().__init__(K)\n      \
    \  self.x = x\n        self.ans = x\n\n    def added(self, y):\n        self.x\
    \ -= y\n        self.ans = max(self.ans, self.x)\n    \n    def removed(self,\
    \ y):\n        self.x += y\n        self.ans = max(self.ans, self.x)\n\nif __name__\
    \ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc249/tasks/abc249_f\n\
    \n\n\ndef main():\n    N, K = read(tuple[int, ...])\n    ops = read(list[tuple[int,\
    \ ...], N])\n    diff = []\n    x = 0\n    for t, y in ops:\n        match t:\n\
    \            case 1:\n                diff.append(y - x)\n                x =\
    \ y\n            case 2:\n                diff.append(y)\n                x +=\
    \ y\n\n    S = BadOps(K, x)\n    if K:\n        for i,(t,y) in rev_enumerate(ops):\n\
    \            match t:\n                case 1:\n                    S.K -= 1\n\
    \                    S.added(diff[i])\n                    if S.K == 0: break\n\
    \                case 2:\n                    if y < 0:\n                    \
    \    S.push(y)\n    write(S.ans)\n                \n\nfrom cp_library.io.read_fn\
    \ import read\nfrom cp_library.io.write_fn import write\nfrom cp_library.alg.iter.rev_enumerate_fn\
    \ import rev_enumerate\nfrom cp_library.ds.heap.min_k_heap_cls import MinKHeap\n\
    \nclass BadOps(MinKHeap[int]):\n    def __init__(self, K: int, x: int):\n    \
    \    super().__init__(K)\n        self.x = x\n        self.ans = x\n\n    def\
    \ added(self, y):\n        self.x -= y\n        self.ans = max(self.ans, self.x)\n\
    \    \n    def removed(self, y):\n        self.x += y\n        self.ans = max(self.ans,\
    \ self.x)\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/iter/rev_enumerate_fn.py
  - cp_library/ds/heap/min_k_heap_cls.py
  - cp_library/io/io_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/ds/heap/max_heap_cls.py
  - cp_library/ds/heap/k_heap_mixin.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/io/io_base_cls.py
  - cp_library/ds/heap/heapify_max_fn.py
  - cp_library/ds/heap/heappop_max_fn.py
  - cp_library/ds/heap/heappush_max_fn.py
  - cp_library/ds/heap/heappushpop_max_fn.py
  - cp_library/ds/heap/heapreplace_max_fn.py
  - cp_library/ds/heap/heap_base_cls.py
  - cp_library/io/parsable_cls.py
  - cp_library/ds/heap/heapsiftup_max_fn.py
  - cp_library/ds/heap/heapsiftdown_max_fn.py
  isVerificationFile: true
  path: test/atcoder/abc/abc249_f_min_k_heap.test.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc/abc249_f_min_k_heap.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc/abc249_f_min_k_heap.test.py
- /verify/test/atcoder/abc/abc249_f_min_k_heap.test.py.html
title: test/atcoder/abc/abc249_f_min_k_heap.test.py
---
