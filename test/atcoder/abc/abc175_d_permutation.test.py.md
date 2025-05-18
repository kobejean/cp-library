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
    path: cp_library/alg/iter/presum_fn.py
    title: cp_library/alg/iter/presum_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/roll_fn.py
    title: cp_library/alg/iter/roll_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u8f_fn.py
    title: cp_library/ds/array/u8f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
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
    PROBLEM: https://atcoder.jp/contests/abc175/tasks/abc175_d
    links:
    - https://atcoder.jp/contests/abc175/tasks/abc175_d
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc175/tasks/abc175_d\n\
    \nfrom math import inf\n\ndef main():\n    N, K = read(tuple[int, ...])\n    P\
    \ = read(PermGraph[N])\n    C = read(list[int, N])\n\n    ans = -inf\n    for\
    \ cyc in P.cycles():\n        L = len(cyc)\n        A = [C[u] for u in cyc]\n\
    \        loop = sum(A)\n        A = presum(A*3)\n        m, k = divmod(K, L)\n\
    \        if m:\n            k += L\n            m -= 1\n        rem = max(A[i+j+1]\
    \ - A[i] for i in range(L) for j in range(k))\n        cost = max(m*loop + rem,\
    \ rem)\n        ans = max(ans, cost)\n\n    write(ans)\n    \n'''\n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\nimport operator\nfrom itertools import accumulate\n\
    from typing import Callable, Iterable\nfrom typing import TypeVar\n_T = TypeVar('T')\n\
    _U = TypeVar('U')\n\ndef presum(iter: Iterable[_T], func: Callable[[_T,_T],_T]\
    \ = None, initial: _T = None, step = 1) -> list[_T]:\n    if step == 1:\n    \
    \    return list(accumulate(iter, func, initial=initial))\n    else:\n       \
    \ assert step >= 2\n        if func is None:\n            func = operator.add\n\
    \        A = list(iter)\n        if initial is not None:\n            A = [initial]\
    \ + A\n        for i in range(step,len(A)):\n            A[i] = func(A[i], A[i-step])\n\
    \        return A\n\n\nimport typing\nfrom collections import deque\nfrom numbers\
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
    ascii\")\ntry:\n    sys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\n    sys.stdout\
    \ = IOWrapper.stdout = IOWrapper(sys.stdout)\nexcept:\n    pass\n\nclass TokenStream(Iterator):\n\
    \    stream = IOWrapper.stdin\n\n    def __init__(self):\n        self.queue =\
    \ deque()\n\n    def __next__(self):\n        if not self.queue: self.queue.extend(self._line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self._line())\n        while self.queue: yield\n\
    \ \n    def _line(self):\n        return TokenStream.stream.readline().split()\n\
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
    \ isinstance(args := spec, Collection):\n            return Parser.compile_collection(type(spec),\
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
    \ Parser.compile_repeat(cls, shift, N)\n\nfrom typing import Generic\n\nclass\
    \ CRFList(Generic[_T]):\n    def __init__(crf, A: list[_T], S: list[int]):\n \
    \       crf.N, crf.A, crf.S = len(S), A, S\n        S.append(len(A))\n\n    def\
    \ __len__(crf) -> int: return crf.N\n\n    def __getitem__(crf, i: int) -> list[_T]:\n\
    \        return crf.A[crf.S[i]:crf.S[i+1]]\n    \n    def get(crf, i: int, j:\
    \ int) -> _T:\n        return crf.A[crf.S[i]+j]\n    \n    def len(crf, i: int)\
    \ -> int:\n        return crf.S[i+1] - crf.S[i]\n\ndef roll(A: list, t: int):\n\
    \    if t:=t%len(A): A[:t], A[t:] = A[-t:], A[:-t]\n    return A\n\n\nfrom array\
    \ import array\ndef u8f(N: int, elm: int = 0):      return array('B', (elm,))*N\
    \  # unsigned char\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__\
    \ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n        return []\n\
    elist = newlist_hint\n    \n\nclass PermGraph(FuncGraph):\n    def inv(P):\n \
    \       Pinv = [0]*P.N\n        for i,p in enumerate(P):\n            Pinv[p]\
    \ = i\n        return type(P)(Pinv)\n\nfrom typing import Iterable, Type, Union,\
    \ overload\n\n@overload\ndef read() -> list[int]: ...\n@overload\ndef read(spec:\
    \ Type[_T], char=False) -> _T: ...\n@overload\ndef read(spec: _U, char=False)\
    \ -> _U: ...\n@overload\ndef read(*specs: Type[_T], char=False) -> tuple[_T, ...]:\
    \ ...\n@overload\ndef read(*specs: _U, char=False) -> tuple[_U, ...]: ...\ndef\
    \ read(*specs: Union[Type[_T],_U], char=False):\n    if not char and not specs:\
    \ return [int(s) for s in TokenStream.default.line()]\n    parser: _T = Parser.compile(specs)\n\
    \    ret = parser(CharStream.default if char else TokenStream.default)\n    return\
    \ ret[0] if len(specs) == 1 else ret\n\ndef write(*args, **kwargs):\n    '''Prints\
    \ the values to a stream, or to stdout_fast by default.'''\n    sep, file = kwargs.pop(\"\
    sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n    at_start = True\n \
    \   for x in args:\n        if not at_start:\n            file.write(sep)\n  \
    \      file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    \nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc175/tasks/abc175_d\n\
    \nfrom math import inf\n\ndef main():\n    N, K = read(tuple[int, ...])\n    P\
    \ = read(PermGraph[N])\n    C = read(list[int, N])\n\n    ans = -inf\n    for\
    \ cyc in P.cycles():\n        L = len(cyc)\n        A = [C[u] for u in cyc]\n\
    \        loop = sum(A)\n        A = presum(A*3)\n        m, k = divmod(K, L)\n\
    \        if m:\n            k += L\n            m -= 1\n        rem = max(A[i+j+1]\
    \ - A[i] for i in range(L) for j in range(k))\n        cost = max(m*loop + rem,\
    \ rem)\n        ans = max(ans, cost)\n\n    write(ans)\n    \nfrom cp_library.alg.iter.presum_fn\
    \ import presum\nfrom cp_library.alg.graph.perm_graph_cls import PermGraph\nfrom\
    \ cp_library.io.read_fn import read\nfrom cp_library.io.write_fn import write\n\
    \nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/alg/iter/presum_fn.py
  - cp_library/alg/graph/perm_graph_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/graph/func_graph_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/alg/iter/crf_list_cls.py
  - cp_library/alg/iter/roll_fn.py
  - cp_library/ds/array/u8f_fn.py
  - cp_library/ds/elist_fn.py
  isVerificationFile: true
  path: test/atcoder/abc/abc175_d_permutation.test.py
  requiredBy: []
  timestamp: '2025-05-19 05:52:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc/abc175_d_permutation.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc/abc175_d_permutation.test.py
- /verify/test/atcoder/abc/abc175_d_permutation.test.py.html
title: test/atcoder/abc/abc175_d_permutation.test.py
---
