---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/elist_fn.py
    title: cp_library/ds/list/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/queries_mo_ops_cls.py
    title: cp_library/ds/queries_mo_ops_cls.py
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
    PROBLEM: https://atcoder.jp/contests/abc293/tasks/abc293_g
    links:
    - https://atcoder.jp/contests/abc293/tasks/abc293_g
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc293/tasks/abc293_g\n\
    \n\ndef main():\n    N, Q = read()\n    A = read(list[int])\n    ops, *opands\
    \ = read(QueriesMoOps[Q, N])\n    \n    # State for counting triples\n    cnt\
    \ = [0]*200001        \n    triples = 0           \n    ans = [0]*Q\n    \n  \
    \  for j in range(len(ops)):\n        if ops[j] in MoOp.ADD:\n            for\
    \ i in range(opands[0][j], opands[1][j], opands[2][j]):\n                v = A[i]\n\
    \                c = cnt[v] \n                triples += c*(c-1)  \n         \
    \       cnt[v] += 1   \n        elif ops[j] in MoOp.REMOVE:\n            for i\
    \ in range(opands[0][j], opands[1][j], opands[2][j]):\n                v = A[i]\n\
    \                cnt[v] -= 1       \n                c = cnt[v]      \n      \
    \          triples -= c*(c-1)    \n        else:\n            i = opands[0][j]\n\
    \            ans[i] = triples >> 1\n    \n    write(*ans, sep='\\n')\n\n'''\n\u257A\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n         \
    \    https://kobejean.github.io/cp-library               \n'''\nfrom enum import\
    \ IntFlag, auto\nfrom math import isqrt\nfrom types import GenericAlias\n\n\n\
    class Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(io:\
    \ 'IOBase'): return cls(next(io))\n        return parser\n    @classmethod\n \
    \   def __class_getitem__(cls, item): return GenericAlias(cls, item)\n\n\n\ndef\
    \ elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\n\
    except:\n    def newlist_hint(hint):\n        return []\nelist = newlist_hint\n\
    \    \n\nclass MoOp(IntFlag):\n    ADD_LEFT = auto()\n    ADD_RIGHT = auto()\n\
    \    REMOVE_LEFT = auto()\n    REMOVE_RIGHT = auto()\n    ANSWER = auto()\n  \
    \  \n    ADD = ADD_LEFT | ADD_RIGHT\n    REMOVE = REMOVE_LEFT | REMOVE_RIGHT\n\
    \n# def hilbert(x: int, y: int, n: int) -> int:\n#     '''Convert (x,y) to Hilbert\
    \ curve distance for given n (power of 2).'''\n#     d = 0\n#     for s in range(n.bit_length()\
    \ - 1, -1, -1):\n#         rx = (x >> s) & 1\n#         ry = (y >> s) & 1\n# \
    \        d += n * n * ((3 * rx) ^ ry) >> 2\n#         if ry == 0:\n#         \
    \    if rx == 1:\n#                 x = n-1 - x\n#                 y = n-1 - y\n\
    #             x, y = y, x\n#     return d\n\nclass QueriesMoOps(tuple[list[int],\
    \ ...],Parsable):\n    '''\n    QueriesMoOps[Q: int, N: int, T: type = tuple[int,\
    \ int]]\n    Orders queries using Mo's algorithm and generates a sequence of operations\
    \ to process them efficiently.\n    Each operation is either moving pointers or\
    \ answering a query.\n    \n    Uses half-interval convention: [left, right)\n\
    \    '''\n    def __new__(cls, L: list[int], R: list[int], N: int, B: int = None):\n\
    \        Q = len(L)\n        qbits = Q.bit_length()\n        nbits = (N+1).bit_length()\n\
    \        qmask = qmask = (1 << qbits)-1\n        nmask = (1 << nbits)-1\n    \
    \    B = max(1,N//isqrt(max(1,Q)) )if B is None else B\n        order = [0]*Q\n\
    \        for i in range(Q):\n            l, r = L[i], R[i]\n            b = l//B\n\
    \            r = nmask - r if b & 1 else r\n            order[i] = (((b << nbits)\
    \ + r) << qbits) + i\n        # n = 1 << nbits\n        # for i in range(Q):\n\
    \        #     l, r = L[i], R[i]\n        #     # Use Hilbert curve mapping for\
    \ the 2D point (l,r)\n        #     h = hilbert(l, r, n)\n        #     order[i]\
    \ = (h << qbits) + i\n        order.sort()\n        ops = elist(3*Q); A1 = elist(3*Q);\
    \ A2 = elist(3*Q); A3 = elist(3*Q)\n        nl = nr = 0\n        for i in order:\n\
    \            i &= qmask\n            l, r = L[i], R[i]\n            if l < nl:\
    \ ops.append(MoOp.ADD_LEFT); A1.append(nl-1); A2.append(l-1); A3.append(-1)\n\
    \            elif l > nl: ops.append(MoOp.REMOVE_LEFT); A1.append(nl); A2.append(l);\
    \ A3.append(1)\n            if r > nr: ops.append(MoOp.ADD_RIGHT); A1.append(nr);\
    \ A2.append(r); A3.append(1)\n            elif r < nr: ops.append(MoOp.REMOVE_RIGHT);\
    \ A1.append(nr-1); A2.append(r-1); A3.append(-1)\n            ops.append(MoOp.ANSWER);\
    \ A1.append(i); A2.append(l); A3.append(r)\n            nl, nr = l, r\n      \
    \  return super().__new__(cls, (ops, A1, A2, A3))\n\n    @classmethod\n    def\
    \ compile(cls, Q: int, N: int, T: type = tuple[-1, int], B: int = None):\n   \
    \     if T == tuple[-1, int]:\n            query = Parser.compile(T)\n       \
    \     def parse(io: IOBase):\n                L, R = [0]*Q, [0]*Q\n          \
    \      for i in range(Q): L[i], R[i] = io.readints(); L[i] -= 1\n            \
    \    return cls(L, R, N, B)\n            return parse\n        else:\n       \
    \     query = Parser.compile(T)\n            def parse(io: IOBase):\n        \
    \        L, R = [0]*Q, [0]*Q\n                for i in range(Q): L[i], R[i] =\
    \ query(io)\n                return cls(L, R, N, B)\n            return parse\n\
    import typing\nfrom numbers import Number\nfrom typing import Callable, Collection\n\
    \nclass IOBase:\n    @property\n    def char(io) -> bool: ...\n    @property\n\
    \    def writable(io) -> bool: ...\n    def __next__(io) -> str: ...\n    def\
    \ write(io, s: str) -> None: ...\n    def readline(io) -> str: ...\n    def readtoken(io)\
    \ -> str: ...\n    def readtokens(io) -> list[str]: ...\n    def readints(io)\
    \ -> list[int]: ...\n    def readdigits(io) -> list[int]: ...\n    def readnums(io)\
    \ -> list[int]: ...\n    def readchar(io) -> str: ...\n    def readchars(io) ->\
    \ str: ...\n    def readinto(io, lst: list[str]) -> list[str]: ...\n    def readcharsinto(io,\
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
    \        else:\n            raise NotImplementedError()\nfrom typing import Type,\
    \ Union, overload\nfrom typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T');\
    \ _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3');\
    \ _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n@overload\n\
    def read() -> list[int]: ...\n@overload\ndef read(spec: Type[_T], char=False)\
    \ -> _T: ...\n@overload\ndef read(spec: _U, char=False) -> _U: ...\n@overload\n\
    def read(*specs: Type[_T], char=False) -> tuple[_T, ...]: ...\n@overload\ndef\
    \ read(*specs: _U, char=False) -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_T],\
    \ char=False):\n    IO.stdin.char = char\n    if not specs: return IO.stdin.readnumsinto([])\n\
    \    parser: _T = Parser.compile(specs[0] if len(specs) == 1 else specs)\n   \
    \ return parser(IO.stdin)\nfrom os import read as os_read, write as os_write,\
    \ fstat as os_fstat\nimport sys\nfrom __pypy__.builders import StringBuilder\n\
    \n\ndef max2(a, b): return a if a > b else b\n\nclass IO(IOBase):\n    BUFSIZE\
    \ = 1 << 16; stdin: 'IO'; stdout: 'IO'\n    __slots__ = 'f', 'file', 'B', 'O',\
    \ 'V', 'S', 'l', 'p', 'char', 'sz', 'st', 'ist', 'writable', 'encoding', 'errors'\n\
    \    def __init__(io, file):\n        io.file = file\n        try: io.f = file.fileno();\
    \ io.sz, io.writable = max2(io.BUFSIZE, os_fstat(io.f).st_size), ('x' in file.mode\
    \ or 'r' not in file.mode)\n        except: io.f, io.sz, io.writable = -1, io.BUFSIZE,\
    \ False\n        io.B, io.O, io.S = bytearray(), [], StringBuilder(); io.V = memoryview(io.B);\
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
    \ = IO(sys.stdout)\n\ndef write(*args, **kwargs):\n    '''Prints the values to\
    \ a stream, or to stdout_fast by default.'''\n    sep, file = kwargs.pop(\"sep\"\
    , \" \"), kwargs.pop(\"file\", IO.stdout)\n    at_start = True\n    for x in args:\n\
    \        if not at_start:\n            file.write(sep)\n        file.write(str(x))\n\
    \        at_start = False\n    file.write(kwargs.pop(\"end\", \"\\n\"))\n    if\
    \ kwargs.pop(\"flush\", False):\n        file.flush()\n\nif __name__ == \"__main__\"\
    :\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc293/tasks/abc293_g\n\
    \n\ndef main():\n    N, Q = read()\n    A = read(list[int])\n    ops, *opands\
    \ = read(QueriesMoOps[Q, N])\n    \n    # State for counting triples\n    cnt\
    \ = [0]*200001        \n    triples = 0           \n    ans = [0]*Q\n    \n  \
    \  for j in range(len(ops)):\n        if ops[j] in MoOp.ADD:\n            for\
    \ i in range(opands[0][j], opands[1][j], opands[2][j]):\n                v = A[i]\n\
    \                c = cnt[v] \n                triples += c*(c-1)  \n         \
    \       cnt[v] += 1   \n        elif ops[j] in MoOp.REMOVE:\n            for i\
    \ in range(opands[0][j], opands[1][j], opands[2][j]):\n                v = A[i]\n\
    \                cnt[v] -= 1       \n                c = cnt[v]      \n      \
    \          triples -= c*(c-1)    \n        else:\n            i = opands[0][j]\n\
    \            ans[i] = triples >> 1\n    \n    write(*ans, sep='\\n')\n\nfrom cp_library.ds.queries_mo_ops_cls\
    \ import QueriesMoOps, MoOp\nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn\
    \ import write\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/ds/queries_mo_ops_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/parsable_cls.py
  - cp_library/ds/list/elist_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/io/io_cls.py
  - cp_library/alg/dp/max2_fn.py
  isVerificationFile: true
  path: test/atcoder/abc/abc261_g_queries_mo_ops.test.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc/abc261_g_queries_mo_ops.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc/abc261_g_queries_mo_ops.test.py
- /verify/test/atcoder/abc/abc261_g_queries_mo_ops.test.py.html
title: test/atcoder/abc/abc261_g_queries_mo_ops.test.py
---
