---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/func_graph_cls.py
    title: cp_library/alg/graph/func_graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/perm_graph_cls.py
    title: cp_library/alg/graph/perm_graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/crf_list_cls.py
    title: cp_library/alg/iter/crf_list_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/roll_fn.py
    title: cp_library/alg/iter/roll_fn.py
  - icon: ':question:'
    path: cp_library/ds/array_init_fn.py
    title: cp_library/ds/array_init_fn.py
  - icon: ':question:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/deque_cls.py
    title: cp_library/ds/list/deque_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/slidingminmax_cls.py
    title: cp_library/ds/slidingminmax_cls.py
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
    from math import gcd\nfrom typing import Iterable\n\nimport typing\nfrom collections\
    \ import deque\nfrom numbers import Number\nfrom types import GenericAlias \n\
    from typing import Callable, Collection, Iterator, Union\nimport os\nimport sys\n\
    from io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n\
    \    newlines = 0\n\n    def __init__(self, file):\n        self._fd = file.fileno()\n\
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
    \ return cls(next(ts))\n        return parser\n\nclass FuncGraph(list[int], Parsable):\n\
    \    def __init__(F, successors):\n        super().__init__(successors)\n    \
    \    F.N = F.M = len(F)\n\n    def find_cycle(P, root: int) -> list[int]:\n  \
    \      slow = fast = root\n        while (slow := P[slow]) != (fast := P[P[fast]]):\
    \ pass\n        cyc = [slow]\n        while P[slow] != fast: cyc.append(slow :=\
    \ P[slow])\n        return cyc\n    \n    def cycles(P) -> 'CRFList[int]':\n \
    \       vis, cycs, S = u8f(N := P.N), elist(N), elist(N)\n        for v in range(P.N):\n\
    \            if vis[v]: continue\n            slow = fast = v\n            while\
    \ (slow := P[slow]) != (fast := P[P[fast]]) and not vis[fast]: pass\n        \
    \    if vis[fast]: continue\n            S.append(len(cycs))\n            cycs.append(slow)\n\
    \            vis[slow := P[slow]] = 1\n            while slow != fast:\n     \
    \           cycs.append(slow)\n                vis[slow := P[slow]] = 1\n    \
    \    return CRFList(cycs, S)\n    \n    def chain(P, root):\n        cyc = P.find_cycle(root)\n\
    \        slow, fast = root, cyc[0]\n        if slow == fast: return [], cyc\n\
    \        line = [slow]\n        while (slow := P[slow]) != (fast := P[fast]):\n\
    \            line.append(slow)\n        return line, roll(cyc, -cyc.index(slow))\n\
    \n    @classmethod\n    def compile(cls, N: int, shift = -1):\n        return\
    \ Parser.compile_repeat(cls, shift, N)\n\nfrom itertools import pairwise\n\nfrom\
    \ typing import Generic\n\nclass CRFList(Generic[_T]):\n    def __init__(crf,\
    \ A: list[_T], S: list[int]):\n        crf.N, crf.A, crf.S = len(S), A, S\n  \
    \      S.append(len(A))\n\n    def __len__(crf) -> int: return crf.N\n\n    def\
    \ __getitem__(crf, i: int) -> list[_T]:\n        return crf.A[crf.S[i]:crf.S[i+1]]\n\
    \    \n    def get(crf, i: int, j: int) -> _T:\n        return crf.A[crf.S[i]+j]\n\
    \    \n    def len(crf, i: int) -> int:\n        return crf.S[i+1] - crf.S[i]\n\
    \ndef roll(A: list, t: int):\n    if t:=t%len(A): A[:t], A[t:] = A[-t:], A[:-t]\n\
    \    return A\n\nfrom array import array\n\ndef i8f(N: int, elm: int = 0):   \
    \   return array('b', (elm,))*N  # signed char\ndef u8f(N: int, elm: int = 0):\
    \      return array('B', (elm,))*N  # unsigned char\ndef i16f(N: int, elm: int\
    \ = 0):     return array('h', (elm,))*N  # signed short\ndef u16f(N: int, elm:\
    \ int = 0):     return array('H', (elm,))*N  # unsigned short\ndef i32f(N: int,\
    \ elm: int = 0):     return array('i', (elm,))*N  # signed int\ndef u32f(N: int,\
    \ elm: int = 0):     return array('I', (elm,))*N  # unsigned int\ndef i64f(N:\
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
    \        return []\nelist = newlist_hint\n    \n\nclass PermGraph(FuncGraph):\n\
    \    def inv(P):\n        Pinv = [0]*P.N\n        for i,p in enumerate(P):\n \
    \           Pinv[p] = i\n        return type(P)(Pinv)\n\ndef main():\n    N, K\
    \ = read(tuple[int,int])\n    P = read(PermGraph[N,0])\n    win = SlidingMinMax(maxlen=K)\n\
    \    win.extend(P[:K])\n    ans = 1 - (unchanged := len(win.minq) == K)\n    for\
    \ i in range(K,N):\n        p = win.popleft()\n        win.append(P[i])\n    \
    \    unchanged |= (is_sorted:=len(win.minq) == K)\n        ans += not is_sorted\
    \ and (p > win.min or P[i] < win.max)\n        \n    ans += unchanged\n    write(ans)\n\
    \    \n\n\ndef list_find(lst: list, value, start = 0, stop = sys.maxsize):\n \
    \   try:\n        return lst.index(value, start, stop)\n    except:\n        return\
    \ -1\nfrom typing import MutableSequence, SupportsIndex\n\nclass Deque(MutableSequence[_T]):\n\
    \    def __init__(que, A = tuple(), *, maxlen=-1):\n        super().__init__()\n\
    \        data = [0]*maxlen\n        que._sz = que._t = len(A)\n        for i,a\
    \ in enumerate(A): data[i] = a\n        que._h, que.maxlen, que.data = 0, maxlen,\
    \ data\n\n    def __len__(que):\n        return que._sz \n    \n    def __contains__(que,\
    \ x):\n        if que._h >= que._t:\n            return (list_find(que.data, x,\
    \ 0, que._t) != -1\n                or list_find(que.data, x, que._h, que.maxlen)\
    \ != -1)\n        else:\n            return list_find(que.data, x, que._h, que._t)\
    \ != -1\n        \n    def __getitem__(que, i: SupportsIndex) -> _T:\n       \
    \ assert -que._sz <= i < que._sz\n        if i >= 0: return que.data[(que._h+i)%que.maxlen]\n\
    \        else: return que.data[(que._t+i)%que.maxlen]\n        \n    def __setitem__(que,\
    \ i: SupportsIndex, x):\n        assert -que._sz <= i < que._sz\n        if i\
    \ >= 0: que.data[(que._h+i)%que.maxlen] = x\n        else: que.data[(que._t+i)%que.maxlen]\
    \ = x\n    \n    def head(que) -> _T: return que.data[que._h]\n\n    def tail(que)\
    \ -> _T: return que.data[(que._t-1)%que.maxlen]\n\n    def __delitem__(que, i:\
    \ SupportsIndex):\n        raise NotImplemented\n    \n    def insert(que, i:\
    \ SupportsIndex, x):\n        raise NotImplemented\n    \n    def append(que,\
    \ x):\n        que.data[t := que._t] = x\n        que._t = (t+1)%que.maxlen\n\
    \        if que._sz == que.maxlen: que._h = que._t\n        else: que._sz += 1\n\
    \n    def appendleft(que, x):\n        que._h = (que._h-1)%que.maxlen\n      \
    \  que.data[que._h] = x\n        if que._sz == que.maxlen: que._t = que._h\n \
    \       else: que._sz += 1\n\n    def pop(que) -> _T:\n        assert que._sz,\
    \ \"Deque is empty\"\n        que._t = (que._t-1)%que.maxlen\n        que._sz\
    \ -= 1\n        return que.data[que._t]\n    \n    def popleft(que) -> _T:\n \
    \       assert que._sz, \"Deque is empty\"\n        x = que.data[h := que._h]\n\
    \        que._h = (h+1)%que.maxlen\n        que._sz -= 1\n        return x\n\n\
    class SlidingMinMax(Deque[_T]):\n    def __init__(self, *, maxlen):\n        super().__init__(maxlen=maxlen)\n\
    \        self.minq = Deque(maxlen=maxlen)\n        self.maxq = Deque(maxlen=maxlen)\n\
    \n    def append(self, x: _T) -> None:\n        while self.minq and x < self.minq.tail():\
    \ self.minq.pop()\n        self.minq.append(x)\n        while self.maxq and self.maxq.tail()\
    \ < x: self.maxq.pop()\n        self.maxq.append(x)\n        super().append(x)\n\
    \    \n    def appendleft(self, x: _T) -> None:\n        raise NotImplemented\n\
    \    \n    def extend(self, iterable: Iterable) -> None:\n        for x in iterable:\
    \ self.append(x)\n\n    def extendleft(self, iterable: Iterable) -> None:\n  \
    \      raise NotImplemented\n\n    def popleft(self) -> _T:\n        x = super().popleft()\n\
    \        if x == self.minq.head(): self.minq.popleft()\n        if x == self.maxq.head():\
    \ self.maxq.popleft()\n        return x\n    \n    def pop(self) -> _T: raise\
    \ NotImplemented\n\n    @property\n    def min(self) -> _T: return self.minq.head()\n\
    \n    @property\n    def max(self) -> _T: return self.maxq.head()\n\nfrom typing\
    \ import Iterable, Type, Union, overload\n\n@overload\ndef read() -> Iterable[int]:\
    \ ...\n@overload\ndef read(spec: int) -> list[int]: ...\n@overload\ndef read(spec:\
    \ Union[Type[_T],_T], char=False) -> _T: ...\ndef read(spec: Union[Type[_T],_T]\
    \ = None, char=False):\n    if not char and spec is None: return map(int, TokenStream.default.line())\n\
    \    parser: _T = Parser.compile(spec)\n    return parser(CharStream.default if\
    \ char else TokenStream.default)\n\ndef write(*args, **kwargs):\n    '''Prints\
    \ the values to a stream, or to stdout_fast by default.'''\n    sep, file = kwargs.pop(\"\
    sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n    at_start = True\n \
    \   for x in args:\n        if not at_start:\n            file.write(sep)\n  \
    \      file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    \nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/agc038/tasks/agc038_b\n\
    \nfrom cp_library.alg.graph.perm_graph_cls import PermGraph\n\ndef main():\n \
    \   N, K = read(tuple[int,int])\n    P = read(PermGraph[N,0])\n    win = SlidingMinMax(maxlen=K)\n\
    \    win.extend(P[:K])\n    ans = 1 - (unchanged := len(win.minq) == K)\n    for\
    \ i in range(K,N):\n        p = win.popleft()\n        win.append(P[i])\n    \
    \    unchanged |= (is_sorted:=len(win.minq) == K)\n        ans += not is_sorted\
    \ and (p > win.min or P[i] < win.max)\n        \n    ans += unchanged\n    write(ans)\n\
    \    \nfrom cp_library.ds.slidingminmax_cls import SlidingMinMax\nfrom cp_library.io.read_fn\
    \ import read\nfrom cp_library.io.write_fn import write\n\nif __name__ == \"__main__\"\
    :\n    main()"
  dependsOn:
  - cp_library/alg/graph/perm_graph_cls.py
  - cp_library/ds/slidingminmax_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/graph/func_graph_cls.py
  - cp_library/ds/list/deque_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/alg/iter/crf_list_cls.py
  - cp_library/alg/iter/roll_fn.py
  - cp_library/ds/array_init_fn.py
  - cp_library/ds/elist_fn.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: true
  path: test/atcoder/agc/agc038_b_sliding_min_max.test.py
  requiredBy: []
  timestamp: '2025-03-27 22:10:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/agc/agc038_b_sliding_min_max.test.py
layout: document
redirect_from:
- /verify/test/atcoder/agc/agc038_b_sliding_min_max.test.py
- /verify/test/atcoder/agc/agc038_b_sliding_min_max.test.py.html
title: test/atcoder/agc/agc038_b_sliding_min_max.test.py
---
