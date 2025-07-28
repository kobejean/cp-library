---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/rank/irank_multi_fn.py
    title: cp_library/alg/iter/rank/irank_multi_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_dec_fn.py
    title: cp_library/bit/pack/pack_dec_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_enc_fn.py
    title: cp_library/bit/pack/pack_enc_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer3_cls.py
    title: cp_library/bit/pack/packer3_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/elist_fn.py
    title: cp_library/ds/list/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/seg/segtree_cls.py
    title: cp_library/ds/tree/seg/segtree_cls.py
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
    PROBLEM: https://judge.yosupo.jp/problem/point_set_range_composite_large_array
    links:
    - https://judge.yosupo.jp/problem/point_set_range_composite_large_array
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite_large_array\n\
    \n\ndef main():\n    mod = 998244353\n    shift, mask = 30, (1<<30)-1\n    N,\
    \ Q = read()\n    \n    def op(a,b):\n        ac, ad = pack_dec(a, shift, mask)\n\
    \        bc, bd = pack_dec(b, shift, mask)\n        return pack_enc(ac*bc%mod,\
    \ (ad*bc+bd)%mod, shift)\n    P, L, R, Qs = elist(Q), elist(Q), elist(Q), [None]*Q\n\
    \    for i in range(Q):\n        t, *q = read()\n        Qs[i] = t, q\n      \
    \  if t == 0:\n            p, c, d = q\n            P.append(p)\n        else:\n\
    \            l, r, x = q\n            L.append(l); R.append(r)\n    V = irank(P,\
    \ L, R); P.reverse(), L.reverse(), R.reverse()\n    seg = SegTree(op, 1 << shift,\
    \ len(V))\n    for t, q in Qs:\n        if t == 0:\n            _, c, d = q\n\
    \            seg.set(P.pop(), pack_enc(c, d, shift))\n        else:\n        \
    \    _, _, x = q\n            a, b = pack_dec(seg.prod(L.pop(), R.pop()), shift,\
    \ mask)\n            write((a*x+b)%mod)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\n\ndef max2(a, b): return a if a > b else b\n\n\n\n\
    def irank(*A: list[int], distinct = False):\n    N = mxj = 0\n    for Ai in A:\
    \ N += len(Ai); mxj = max2(mxj, len(Ai))\n    P = Packer3(len(A)-1, mxj); V =\
    \ P.enumerate(A, N); V.sort()\n    if distinct:\n        for r,aij in enumerate(V):a,i,j=P.dec(aij);A[i][j],V[r]=r,a\n\
    \    elif V:\n        r, p = -1, V[-1]+1 # set p to unique value to trigger `if\
    \ a != p` on first elm\n        for aij in V:\n            a,i,j=P.dec(aij)\n\
    \            if a!=p:V[r:=r+1]=p=a\n            A[i][j]=r\n        del V[r+1:]\n\
    \    return V\n\n\n\nclass Packer3:\n    def __init__(P, mxb: int, mxc: int):\n\
    \        bb, bc = mxb.bit_length(), mxc.bit_length()\n        P.mc, P.mb, P.sb,\
    \ P.sa = (1<<bc)-1, (1<<bb)-1, bc, bc+bb\n    def enc(P, a: int, b: int, c: int):\
    \ return a << P.sa | b << P.sb | c\n    def dec(P, x: int) -> tuple[int, int,\
    \ int]: return x >> P.sa, (x >> P.sb) & P.mb, x & P.mc\n    def enumerate(P, A,\
    \ N, reverse=False): \n        V, k = [0]*N, 0\n        if reverse:\n        \
    \    for i,Ai in enumerate(A):\n                for j, a in enumerate(Ai):V[k]=P.enc(-a,\
    \ i, j);k+=1\n        else:\n            for i,Ai in enumerate(A):\n         \
    \       for j, a in enumerate(Ai):V[k]=P.enc(a, i, j);k+=1\n        return V\n\
    from typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U');\
    \ _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4');\
    \ _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\nfrom typing import Callable, Generic,\
    \ Union\n\n\n\n\nclass SegTree(Generic[_T]):\n    _lst = list\n    \n    def __init__(seg,\
    \ op: Callable[[_T, _T], _T], e: _T, v: Union[int, list[_T]]) -> None:\n     \
    \   if isinstance(v, int): n = v; v = None\n        else: n = len(v)\n       \
    \ seg.op, seg.e, seg.n = op, e, n\n        seg.log, seg.sz = (log := (n-1).bit_length()+1),\
    \ (sz := 1 << log)\n        if seg._lst is list: seg.d = [e]*(sz<<1)\n       \
    \ else: seg.d = seg._lst(*([e_]*(sz<<1) for e_ in e))\n        if v: seg._build(v)\n\
    \n    def _build(seg, v):\n        for i in range(seg.n): seg.d[seg.sz + i] =\
    \ v[i]\n        for i in range(seg.sz-1,0,-1): seg._merge(i, i<<1, i<<1|1)\n \
    \   \n    def _merge(seg, i, j, k): seg.d[i] = seg.op(seg.d[j], seg.d[k])\n\n\
    \    def set(seg, p: int, x: _T) -> None:\n        p += seg.sz\n        seg.d[p]\
    \ = x\n        for _ in range(seg.log):\n            p = p^(p&1)\n           \
    \ seg._merge(p>>1, p, p|1)\n            p >>= 1\n    __setitem__ = set\n\n   \
    \ def get(seg, p: int) -> _T: return seg.d[p+seg.sz]\n    __getitem__ = get\n\n\
    \    def prod(seg, l: int, r: int) -> _T:\n        sml = smr = seg.e\n       \
    \ l, r = l+seg.sz, r+seg.sz\n        while l < r:\n            if l&1: sml, l\
    \ = seg.op(sml, seg.d[l]), l+1\n            if r&1: smr = seg.op(seg.d[r:=r-1],\
    \ smr)\n            l, r = l >> 1, r >> 1\n        return seg.op(sml, smr)\n\n\
    \    def all_prod(seg) -> _T: return seg.d[1]\n\n    def max_right(seg, l: int,\
    \ f: Callable[[_T], bool]) -> int:\n        assert 0 <= l <= seg.n\n        assert\
    \ f(seg.e)\n        if l == seg.n: return seg.n\n        l, op, d, sm = l+(sz\
    \ := seg.sz), seg.op, seg.d, seg.e\n        while True:\n            while l&1\
    \ == 0: l >>= 1\n            if not f(op(sm, d[l])):\n                while l\
    \ < sz:\n                    if f(op(sm, d[l:=l<<1])): sm, l = op(sm, d[l]), l+1\n\
    \                return l - sz\n            sm, l = op(sm, d[l]), l+1\n      \
    \      if l&-l == l: return seg.n\n\n    def min_left(seg, r: int, f: Callable[[_T],\
    \ bool]) -> int:\n        assert 0 <= r <= seg.n\n        assert f(seg.e)\n  \
    \      if r == 0: return 0\n        r, op, d, sm = r+(sz := seg.sz), seg.op, seg.d,\
    \ seg.e\n        while True:\n            r -= 1\n            while r > 1 and\
    \ r & 1: r >>= 1\n            if not f(op(d[r], sm)):\n                while r\
    \ < sz:\n                    if f(op(d[r:=r<<1|1], sm)): sm, r = op(d[r], sm),\
    \ r-1\n                return r + 1 - sz\n            sm = op(d[r], sm)\n    \
    \        if (r & -r) == r: return 0\n\n\ndef elist(est_len: int) -> list: ...\n\
    try:\n    from __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n\
    \        return []\nelist = newlist_hint\n    \ndef pack_enc(a: int, b: int, s:\
    \ int): return a<<s|b\ndef pack_dec(ab: int, s: int, m: int): return ab>>s,ab&m\n\
    from typing import Type, Union, overload\n\n\n@overload\ndef read() -> list[int]:\
    \ ...\n@overload\ndef read(spec: Type[_T], char=False) -> _T: ...\n@overload\n\
    def read(spec: _U, char=False) -> _U: ...\n@overload\ndef read(*specs: Type[_T],\
    \ char=False) -> tuple[_T, ...]: ...\n@overload\ndef read(*specs: _U, char=False)\
    \ -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_T], char=False):\n\
    \    IO.stdin.char = char\n    if not specs: return IO.stdin.readnumsinto([])\n\
    \    parser: _T = Parser.compile(specs[0] if len(specs) == 1 else specs)\n   \
    \ return parser(IO.stdin)\nfrom os import read as os_read, write as os_write,\
    \ fstat as os_fstat\nimport sys\nfrom __pypy__.builders import StringBuilder\n\
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
    \ -> None: ...\n    def line(io) -> list[str]: ...\n\nclass IO(IOBase):\n    BUFSIZE\
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
    \        else:\n            raise NotImplementedError()\n\ndef write(*args, **kwargs):\n\
    \    '''Prints the values to a stream, or to stdout_fast by default.'''\n    sep,\
    \ file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IO.stdout)\n    at_start\
    \ = True\n    for x in args:\n        if not at_start:\n            file.write(sep)\n\
    \        file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    \nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite_large_array\n\
    \n\ndef main():\n    mod = 998244353\n    shift, mask = 30, (1<<30)-1\n    N,\
    \ Q = read()\n    \n    def op(a,b):\n        ac, ad = pack_dec(a, shift, mask)\n\
    \        bc, bd = pack_dec(b, shift, mask)\n        return pack_enc(ac*bc%mod,\
    \ (ad*bc+bd)%mod, shift)\n    P, L, R, Qs = elist(Q), elist(Q), elist(Q), [None]*Q\n\
    \    for i in range(Q):\n        t, *q = read()\n        Qs[i] = t, q\n      \
    \  if t == 0:\n            p, c, d = q\n            P.append(p)\n        else:\n\
    \            l, r, x = q\n            L.append(l); R.append(r)\n    V = irank(P,\
    \ L, R); P.reverse(), L.reverse(), R.reverse()\n    seg = SegTree(op, 1 << shift,\
    \ len(V))\n    for t, q in Qs:\n        if t == 0:\n            _, c, d = q\n\
    \            seg.set(P.pop(), pack_enc(c, d, shift))\n        else:\n        \
    \    _, _, x = q\n            a, b = pack_dec(seg.prod(L.pop(), R.pop()), shift,\
    \ mask)\n            write((a*x+b)%mod)\n\nfrom cp_library.alg.iter.rank.irank_multi_fn\
    \ import irank\nfrom cp_library.ds.tree.seg.segtree_cls import SegTree\nfrom cp_library.ds.list.elist_fn\
    \ import elist\nfrom cp_library.bit.pack.pack_enc_fn import pack_enc\nfrom cp_library.bit.pack.pack_dec_fn\
    \ import pack_dec\nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn\
    \ import write\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/alg/iter/rank/irank_multi_fn.py
  - cp_library/ds/tree/seg/segtree_cls.py
  - cp_library/ds/list/elist_fn.py
  - cp_library/bit/pack/pack_enc_fn.py
  - cp_library/bit/pack/pack_dec_fn.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/bit/pack/packer3_cls.py
  - cp_library/io/io_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/io/parsable_cls.py
  isVerificationFile: true
  path: test/library-checker/data-structure/point_set_range_composite_large_array.test.py
  requiredBy: []
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/point_set_range_composite_large_array.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/point_set_range_composite_large_array.test.py
- /verify/test/library-checker/data-structure/point_set_range_composite_large_array.test.py.html
title: test/library-checker/data-structure/point_set_range_composite_large_array.test.py
---
