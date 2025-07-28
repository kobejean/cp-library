---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/func/func_graph_cls.py
    title: cp_library/alg/graph/func/func_graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/func/perm_graph_cls.py
    title: cp_library/alg/graph/func/perm_graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/crf_list_cls.py
    title: cp_library/alg/iter/crf_list_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/roll_fn.py
    title: cp_library/alg/iter/roll_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u8f_fn.py
    title: cp_library/ds/array/u8f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/elist_fn.py
    title: cp_library/ds/list/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/que/deque_cls.py
    title: cp_library/ds/que/deque_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/slidingminmax_cls.py
    title: cp_library/ds/slidingminmax_cls.py
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
    PROBLEM: https://atcoder.jp/contests/agc038/tasks/agc038_b
    links:
    - https://atcoder.jp/contests/agc038/tasks/agc038_b
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/agc038/tasks/agc038_b\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\n\n\
    from types import GenericAlias\n\n\nclass Parsable:\n    @classmethod\n    def\
    \ compile(cls):\n        def parser(io: 'IOBase'): return cls(next(io))\n    \
    \    return parser\n    @classmethod\n    def __class_getitem__(cls, item): return\
    \ GenericAlias(cls, item)\n\nclass FuncGraph(list[int], Parsable):\n    def __init__(F,\
    \ successors):\n        super().__init__(successors)\n        F.N = F.M = len(F)\n\
    \n    def find_cycle(P, root: int) -> list[int]:\n        slow = fast = root\n\
    \        while (slow := P[slow]) != (fast := P[P[fast]]): pass\n        cyc =\
    \ [slow]\n        while P[slow] != fast: cyc.append(slow := P[slow])\n       \
    \ return cyc\n    \n    def cycles(P) -> 'CRFList[int]':\n        vis, cycs, S\
    \ = u8f(N := P.N), elist(N), elist(N)\n        for v in range(P.N):\n        \
    \    if vis[v]: continue\n            slow = fast = v\n            while (slow\
    \ := P[slow]) != (fast := P[P[fast]]) and not vis[fast]: pass\n            if\
    \ vis[fast]: continue\n            S.append(len(cycs))\n            cycs.append(slow)\n\
    \            vis[slow := P[slow]] = 1\n            while slow != fast:\n     \
    \           cycs.append(slow)\n                vis[slow := P[slow]] = 1\n    \
    \    return CRFList(cycs, S)\n    \n    def chain(P, root):\n        cyc = P.find_cycle(root)\n\
    \        slow, fast = root, cyc[0]\n        if slow == fast: return [], cyc\n\
    \        line = [slow]\n        while (slow := P[slow]) != (fast := P[fast]):\n\
    \            line.append(slow)\n        return line, roll(cyc, -cyc.index(slow))\n\
    \n    @classmethod\n    def compile(cls, N: int, shift = -1):\n        return\
    \ Parser.compile_repeat(cls, shift, N)\nfrom typing import Generic\nfrom typing\
    \ import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U'); _T1\
    \ = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4');\
    \ _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\nclass CRFList(Generic[_T]):\n\
    \    def __init__(crf, A: list[_T], S: list[int]):\n        crf.N, crf.A, crf.S\
    \ = len(S), A, S\n        S.append(len(A))\n\n    def __len__(crf) -> int: return\
    \ crf.N\n\n    def __getitem__(crf, i: int) -> list[_T]:\n        return crf.A[crf.S[i]:crf.S[i+1]]\n\
    \    \n    def get(crf, i: int, j: int) -> _T:\n        return crf.A[crf.S[i]+j]\n\
    \    \n    def len(crf, i: int) -> int:\n        return crf.S[i+1] - crf.S[i]\n\
    \ndef roll(A: list, t: int):\n    if t:=t%len(A): A[:t], A[t:] = A[-t:], A[:-t]\n\
    \    return A\n\n\nfrom array import array\ndef u8f(N: int, elm: int = 0):   \
    \   return array('B', (elm,))*N  # unsigned char\n\n\ndef elist(est_len: int)\
    \ -> list: ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n    def\
    \ newlist_hint(hint):\n        return []\nelist = newlist_hint\n    \nimport typing\n\
    from numbers import Number\nfrom typing import Callable, Collection\n\nclass IOBase:\n\
    \    @property\n    def char(io) -> bool: ...\n    @property\n    def writable(io)\
    \ -> bool: ...\n    def __next__(io) -> str: ...\n    def write(io, s: str) ->\
    \ None: ...\n    def readline(io) -> str: ...\n    def readtoken(io) -> str: ...\n\
    \    def readtokens(io) -> list[str]: ...\n    def readints(io) -> list[int]:\
    \ ...\n    def readdigits(io) -> list[int]: ...\n    def readnums(io) -> list[int]:\
    \ ...\n    def readchar(io) -> str: ...\n    def readchars(io) -> str: ...\n \
    \   def readinto(io, lst: list[str]) -> list[str]: ...\n    def readcharsinto(io,\
    \ lst: list[str]) -> list[str]: ...\n    def readtokensinto(io, lst: list[str])\
    \ -> list[str]: ...\n    def readintsinto(io, lst: list[int]) -> list[int]: ...\n\
    \    def readdigitsinto(io, lst: list[int]) -> list[int]: ...\n    def readnumsinto(io,\
    \ lst: list[int]) -> list[int]: ...\n    def wait(io): ...\n    def flush(io)\
    \ -> None: ...\n    def line(io) -> list[str]: ...\n\nclass Parser:\n    def __init__(self,\
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
    \        else:\n            fn = Parser.compile(spec)\n            def parse(io:\
    \ IOBase): return cls([fn(io) for _ in io.wait()])\n        return parse\n   \
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
    \        else:\n            raise NotImplementedError()\n\nclass PermGraph(FuncGraph):\n\
    \    def inv(P):\n        Pinv = [0]*P.N\n        for i,p in enumerate(P):\n \
    \           Pinv[p] = i\n        return type(P)(Pinv)\n\ndef main():\n    N, K\
    \ = read(tuple[int,int])\n    P = read(PermGraph[N,0])\n    win = SlidingMinMax(maxlen=K)\n\
    \    win.extend(P[:K])\n    ans = 1 - (unchanged := len(win.minq) == K)\n    for\
    \ i in range(K,N):\n        p = win.popleft()\n        win.append(P[i])\n    \
    \    unchanged |= (is_sorted:=len(win.minq) == K)\n        ans += not is_sorted\
    \ and (p > win.min or P[i] < win.max)\n        \n    ans += unchanged\n    write(ans)\n\
    \    \nimport sys\n\ndef list_find(lst: list, value, start = 0, stop = sys.maxsize):\n\
    \    try:\n        return lst.index(value, start, stop)\n    except:\n       \
    \ return -1\nfrom typing import MutableSequence, SupportsIndex\n\nclass Deque(MutableSequence[_T]):\n\
    \    def __init__(que, A = tuple(), *, maxlen=-1):\n        super().__init__()\n\
    \        que.cap = 1 << (maxlen-1).bit_length()\n        data = [0]*que.cap\n\
    \        que._sz = que._t = len(A)\n        for i,a in enumerate(A): data[i] =\
    \ a\n        que._mask, que._h, que.maxlen, que.data = que.cap-1, 0, maxlen, data\n\
    \n    def __len__(que):\n        return que._sz \n    \n    def __contains__(que,\
    \ x):\n        if que._h >= que._t:\n            return (list_find(que.data, x,\
    \ 0, que._t) != -1\n                or list_find(que.data, x, que._h, que.cap)\
    \ != -1)\n        else:\n            return list_find(que.data, x, que._h, que._t)\
    \ != -1\n        \n    def __getitem__(que, i: SupportsIndex) -> _T:\n       \
    \ if not (-que._sz <= i < que._sz): raise IndexError\n        if i >= 0: return\
    \ que.data[(que._h+i)&que._mask]\n        else: return que.data[(que._t+i)&que._mask]\n\
    \        \n    def __setitem__(que, i: SupportsIndex, x):\n        if not (-que._sz\
    \ <= i < que._sz): raise IndexError\n        if i >= 0: que.data[(que._h+i)&que._mask]\
    \ = x\n        else: que.data[(que._t+i)&que._mask] = x\n    \n    def head(que)\
    \ -> _T: return que.data[que._h]\n\n    def tail(que) -> _T: return que.data[(que._t-1)&que._mask]\n\
    \n    def __delitem__(que, i: SupportsIndex):\n        raise NotImplemented\n\
    \    \n    def insert(que, i: SupportsIndex, x):\n        raise NotImplemented\n\
    \    \n    def append(que, x):\n        que.data[que._t] = x\n        que._t =\
    \ (que._t+1)&que._mask\n        if que._sz == que.maxlen: que._h = (que._h+1)&que._mask\n\
    \        else: que._sz += 1\n\n    def appendleft(que, x):\n        que._h = (que._h-1)&que._mask\n\
    \        que.data[que._h] = x\n        if que._sz == que.maxlen: que._t = que._h\n\
    \        else: que._sz += 1\n\n    def pop(que) -> _T:\n        assert que._sz,\
    \ \"Deque is empty\"\n        que._t = (que._t-1)&que._mask\n        que._sz -=\
    \ 1\n        return que.data[que._t]\n    \n    def popleft(que) -> _T:\n    \
    \    assert que._sz, \"Deque is empty\"\n        x = que.data[que._h]\n      \
    \  que._h = (que._h+1)&que._mask\n        que._sz -= 1\n        return x\n   \
    \ \n    def __hash__(que):\n        \"\"\"Make Deque hashable for efficient benchmarking\"\
    \"\"\n        if que._h <= que._t:\n            return hash(tuple(que.data[que._h:que._t]))\n\
    \        else:\n            return hash(tuple(que.data[que._h:] + que.data[:que._t]))\n\
    from typing import Iterable\n\nclass SlidingMinMax(Deque[_T]):\n    def __init__(self,\
    \ *, maxlen):\n        super().__init__(maxlen=maxlen)\n        self.minq = Deque(maxlen=maxlen)\n\
    \        self.maxq = Deque(maxlen=maxlen)\n\n    def append(self, x: _T) -> None:\n\
    \        while self.minq and x < self.minq.tail(): self.minq.pop()\n        self.minq.append(x)\n\
    \        while self.maxq and self.maxq.tail() < x: self.maxq.pop()\n        self.maxq.append(x)\n\
    \        super().append(x)\n    \n    def appendleft(self, x: _T) -> None:\n \
    \       raise NotImplemented\n    \n    def extend(self, iterable: Iterable) ->\
    \ None:\n        for x in iterable: self.append(x)\n\n    def extendleft(self,\
    \ iterable: Iterable) -> None:\n        raise NotImplemented\n\n    def popleft(self)\
    \ -> _T:\n        x = super().popleft()\n        if x == self.minq.head(): self.minq.popleft()\n\
    \        if x == self.maxq.head(): self.maxq.popleft()\n        return x\n   \
    \ \n    def pop(self) -> _T: raise NotImplemented\n\n    @property\n    def min(self)\
    \ -> _T: return self.minq.head()\n\n    @property\n    def max(self) -> _T: return\
    \ self.maxq.head()\nfrom typing import Type, Union, overload\n\n@overload\ndef\
    \ read() -> list[int]: ...\n@overload\ndef read(spec: Type[_T], char=False) ->\
    \ _T: ...\n@overload\ndef read(spec: _U, char=False) -> _U: ...\n@overload\ndef\
    \ read(*specs: Type[_T], char=False) -> tuple[_T, ...]: ...\n@overload\ndef read(*specs:\
    \ _U, char=False) -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_T],\
    \ char=False):\n    IO.stdin.char = char\n    if not specs: return IO.stdin.readnumsinto([])\n\
    \    parser: _T = Parser.compile(specs[0] if len(specs) == 1 else specs)\n   \
    \ return parser(IO.stdin)\nfrom os import read as os_read, write as os_write,\
    \ fstat as os_fstat\nfrom __pypy__.builders import StringBuilder\n\n\ndef max2(a,\
    \ b): return a if a > b else b\n\nclass IO(IOBase):\n    BUFSIZE = 1 << 16; stdin:\
    \ 'IO'; stdout: 'IO'\n    __slots__ = 'f', 'file', 'B', 'O', 'V', 'S', 'l', 'p',\
    \ 'char', 'sz', 'st', 'ist', 'writable', 'encoding', 'errors'\n    def __init__(io,\
    \ file):\n        io.file = file\n        try: io.f = file.fileno(); io.sz, io.writable\
    \ = max2(io.BUFSIZE, os_fstat(io.f).st_size), ('x' in file.mode or 'r' not in\
    \ file.mode)\n        except: io.f, io.sz, io.writable = -1, io.BUFSIZE, False\n\
    \        io.B, io.O, io.S = bytearray(), [], StringBuilder(); io.V = memoryview(io.B);\
    \ io.l = io.p = 0\n        io.char, io.st, io.ist, io.encoding, io.errors = False,\
    \ [], [], 'ascii', 'ignore'\n    def _dec(io, l, r): return io.V[l:r].tobytes().decode(io.encoding,\
    \ io.errors)\n    def readbytes(io, sz): return os_read(io.f, sz)\n    def load(io):\n\
    \        while io.l >= len(io.O):\n            if not (b := io.readbytes(io.sz)):\n\
    \                if io.O[-1] < len(io.B): io.O.append(len(io.B))\n           \
    \     break\n            pos = len(io.B); io.B.extend(b)\n            while ~(pos\
    \ := io.B.find(b'\\n', pos)): io.O.append(pos := pos+1)\n    def __next__(io):\n\
    \        if io.char: return io.readchar()\n        else: return io.readtoken()\n\
    \    def readchar(io):\n        io.load(); r = io.O[io.l]\n        c = chr(io.B[io.p])\n\
    \        if io.p >= r-1: io.p = r; io.l += 1\n        else: io.p += 1\n      \
    \  return c\n    def write(io, s: str): io.S.append(s)\n    def readline(io):\
    \ io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return io._dec(l, io.p)\n\
    \    def readtoken(io):\n        io.load(); r = io.O[io.l]\n        if ~(p :=\
    \ io.B.find(b' ', io.p, r)): s = io._dec(io.p, p); io.p = p+1\n        else: s\
    \ = io._dec(io.p, r-1); io.p = r; io.l += 1\n        return s\n    def readtokens(io):\
    \ io.st.clear(); return io.readtokensinto(io.st)\n    def readints(io): io.ist.clear();\
    \ return io.readintsinto(io.ist)\n    def readdigits(io): io.ist.clear(); return\
    \ io.readdigitsinto(io.ist)\n    def readnums(io): io.ist.clear(); return io.readnumsinto(io.ist)\n\
    \    def readchars(io): io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return\
    \ io._dec(l, io.p-1)\n    def readinto(io, lst):\n        if io.char: return io.readcharsinto(lst)\n\
    \        else: return io.readtokensinto(lst)\n    def readcharsinto(io, lst):\
    \ lst.extend(io.readchars()); return lst\n    def readtokensinto(io, lst): \n\
    \        io.load(); r = io.O[io.l]\n        while ~(p := io.B.find(b' ', io.p,\
    \ r)): lst.append(io._dec(io.p, p)); io.p = p+1\n        lst.append(io._dec(io.p,\
    \ r-1)); io.p = r; io.l += 1; return lst\n    def readintsinto(io, lst):\n   \
    \     io.load(); r = io.O[io.l]\n        while io.p < r:\n            while io.p\
    \ < r and io.B[io.p] <= 32: io.p += 1\n            if io.p >= r: break\n     \
    \       minus = x = 0\n            if io.B[io.p] == 45: minus = 1; io.p += 1\n\
    \            while io.p < r and io.B[io.p] >= 48:\n                x = x * 10\
    \ + (io.B[io.p] & 15); io.p += 1\n            lst.append(-x if minus else x)\n\
    \            if io.p < r and io.B[io.p] == 32: io.p += 1\n        io.l += 1; return\
    \ lst\n    def readdigitsinto(io, lst):\n        io.load(); r = io.O[io.l]\n \
    \       while io.p < r and io.B[io.p] > 32:\n            if io.B[io.p] >= 48 and\
    \ io.B[io.p] <= 57:\n                lst.append(io.B[io.p] & 15)\n           \
    \ io.p += 1\n        if io.p < r and io.B[io.p] == 10: io.p = r; io.l += 1\n \
    \       return lst\n    def readnumsinto(io, lst):\n        if io.char: return\
    \ io.readdigitsinto(lst)\n        else: return io.readintsinto(lst)\n    def line(io):\
    \ io.st.clear(); return io.readinto(io.st)\n    def wait(io):\n        io.load();\
    \ r = io.O[io.l]\n        while io.p < r: yield\n    def flush(io):\n        if\
    \ io.writable: os_write(io.f, io.S.build().encode(io.encoding, io.errors)); io.S\
    \ = StringBuilder()\nsys.stdin = IO.stdin = IO(sys.stdin); sys.stdout = IO.stdout\
    \ = IO(sys.stdout)\n\ndef write(*args, **kwargs):\n    '''Prints the values to\
    \ a stream, or to stdout_fast by default.'''\n    sep, file = kwargs.pop(\"sep\"\
    , \" \"), kwargs.pop(\"file\", IO.stdout)\n    at_start = True\n    for x in args:\n\
    \        if not at_start:\n            file.write(sep)\n        file.write(str(x))\n\
    \        at_start = False\n    file.write(kwargs.pop(\"end\", \"\\n\"))\n    if\
    \ kwargs.pop(\"flush\", False):\n        file.flush()\n\nif __name__ == \"__main__\"\
    :\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/agc038/tasks/agc038_b\n\
    \nfrom cp_library.alg.graph.func.perm_graph_cls import PermGraph\n\ndef main():\n\
    \    N, K = read(tuple[int,int])\n    P = read(PermGraph[N,0])\n    win = SlidingMinMax(maxlen=K)\n\
    \    win.extend(P[:K])\n    ans = 1 - (unchanged := len(win.minq) == K)\n    for\
    \ i in range(K,N):\n        p = win.popleft()\n        win.append(P[i])\n    \
    \    unchanged |= (is_sorted:=len(win.minq) == K)\n        ans += not is_sorted\
    \ and (p > win.min or P[i] < win.max)\n        \n    ans += unchanged\n    write(ans)\n\
    \    \nfrom cp_library.ds.slidingminmax_cls import SlidingMinMax\nfrom cp_library.io.read_fn\
    \ import read\nfrom cp_library.io.write_fn import write\n\nif __name__ == \"__main__\"\
    :\n    main()"
  dependsOn:
  - cp_library/alg/graph/func/perm_graph_cls.py
  - cp_library/ds/slidingminmax_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/graph/func/func_graph_cls.py
  - cp_library/ds/que/deque_cls.py
  - cp_library/io/io_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/parsable_cls.py
  - cp_library/alg/iter/crf_list_cls.py
  - cp_library/alg/iter/roll_fn.py
  - cp_library/ds/array/u8f_fn.py
  - cp_library/ds/list/elist_fn.py
  - cp_library/ds/list/list_find_fn.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/io/io_base_cls.py
  isVerificationFile: true
  path: test/atcoder/agc/agc038_b_sliding_min_max.test.py
  requiredBy: []
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/agc/agc038_b_sliding_min_max.test.py
layout: document
redirect_from:
- /verify/test/atcoder/agc/agc038_b_sliding_min_max.test.py
- /verify/test/atcoder/agc/agc038_b_sliding_min_max.test.py.html
title: test/atcoder/agc/agc038_b_sliding_min_max.test.py
---
