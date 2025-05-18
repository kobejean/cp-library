---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_dec_fn.py
    title: cp_library/bit/pack/pack_dec_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_enc_fn.py
    title: cp_library/bit/pack/pack_enc_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/reserve_fn.py
    title: cp_library/ds/reserve_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/treap_monoid_cls.py
    title: cp_library/ds/tree/treap_monoid_cls.py
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
    PROBLEM: https://judge.yosupo.jp/problem/point_set_range_composite_large_array
    links:
    - https://judge.yosupo.jp/problem/point_set_range_composite_large_array
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite_large_array\n\
    from random import shuffle\nimport time\n\ndef main():\n    mod = 998244353\n\
    \    shift, mask = 30, (1<<30)-1\n    N, Q = read()\n    TreapMonoid.reserve(1+Q)\n\
    \    \n    def op(a,b):\n        ac, ad = pack_dec(a, shift, mask)\n        bc,\
    \ bd = pack_dec(b, shift, mask)\n        return pack_enc(ac*bc%mod, (ad*bc+bd)%mod,\
    \ shift)\n    T = TreapMonoid(op, e := 1 << shift)\n    D = {}\n    for _ in range(Q):\n\
    \        t, *q = read()\n        if t == 0:\n            p, c, d = q\n       \
    \     T[p] = D[p] = pack_enc(c, d, shift)\n        else:\n            l, r, x\
    \ = q\n            a, b = pack_dec(T[l:r], shift, mask)\n            write((a*x+b)%mod)\n\
    \n    # test if the following can be run in reasonable time\n    for i, key in\
    \ enumerate(D):\n        assert T[key] == D.get(key, e)\n        assert T[i] ==\
    \ D.get(i, e)\n    for i, key in enumerate(D):\n        assert key in T\n    \
    \    del T[key]\n        assert key not in T\n        if i%10000 == 0: T._validate()\n\
    \    # addition of duplicate values\n    for p in range(Q): T.insert(0, 0)\n\n\
    '''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\n\n\ndef\
    \ reserve(A: list, est_len: int) -> None: ...\ntry:\n    from __pypy__ import\
    \ resizelist_hint\nexcept:\n    def resizelist_hint(A: list, est_len: int):\n\
    \        pass\nreserve = resizelist_hint\n\n\nclass TreapMonoid:\n    __slots__\
    \ = 'op', 'e', 'root', 'cnt'\n    # class attributes\n    K, V, A, P = [-1], [-1],\
    \ [-1], [42]\n    par, sub, st = [-1], [-1, -1], []\n\n    def __init__(T, op,\
    \ e = -1):\n        T.op, T.e, T.cnt = op, e, -1\n        T.root = T.new_node(-1,\
    \ e)\n\n    def prod(T, l: int, r: int):\n        # find_node common ancestor\n\
    \        a = T.sub[T.root<<1]\n        while ~a and not l <= T.K[a] < r: a = T.sub[a<<1|(T.K[a]<l)]\n\
    \        if a < 0: return T.e\n        # left subtreap\n        acc, i = T.V[a],\
    \ T.sub[a<<1]\n        while ~i:\n            if not (T.K[i]<l):\n           \
    \     if ~T.sub[i<<1|1]: acc = T.op(T.A[T.sub[i<<1|1]], acc)\n               \
    \ acc = T.op(T.V[i], acc)\n            i = T.sub[i<<1|(T.K[i]<l)]\n        # right\
    \ subtreap\n        i = T.sub[a<<1|1]\n        while ~i:\n            if T.K[i]<r:\n\
    \                if ~T.sub[i<<1]: acc = T.op(acc, T.A[T.sub[i<<1]])\n        \
    \        acc = T.op(acc, T.V[i])\n            i = T.sub[i<<1|(T.K[i]<r)]\n   \
    \     return acc\n\n    def all_prod(T): return T.A[T.root]\n    \n    def insert(T,\
    \ key, val):\n        T.insert_node(T.root<<1, nid := T.new_node(key, val))\n\
    \        return nid\n    \n    def split(T, key):\n        T.K[0] = key\n    \
    \    T.split_node(T.sub[T.root<<1], 0)\n        S = T.__class__(T.op, T.e)\n \
    \       if ~S.sub[0]: S.attach_node(S.root<<1, T.sub[0])\n        if ~T.sub[1]:\
    \ T.attach_node(T.root<<1, T.sub[1])\n        T._repair()\n        return S, T\n\
    \    \n    def get(T, key): return T.V[id] if ~(id:=T.find_node(key)) else T.e\n\
    \n    def pop(T, key):\n        if ~(id:=T.find_node(key)): T.del_node(id); return\
    \ T.V[id]\n        return T.e\n\n    def __delitem__(T, key):\n        if ~(id:=T.find_node(key)):\
    \ T.del_node(id)\n    \n    def __setitem__(T, key, val):\n        if ~(id:=T.find_node(key)):\
    \ T.set_node(id, val)\n        else: T.insert(key, val)\n    \n    def __getitem__(T,\
    \ key):\n        if isinstance(key, int): return T.get(key)\n        elif isinstance(key,\
    \ slice): return T.prod(key.start, key.stop)\n    \n    def __contains__(T, key):\
    \ return 0 <= T.find_node(key)\n\n    def __len__(T): return T.cnt\n\n    def\
    \ new_node(T, key, val):\n        id = len(T.K)\n        T.K.append(key); T.V.append(val);\
    \ T.A.append(val)\n        T.P.append((T.P[-1] * 1103515245 + 12345) & 0x7fffffff)\n\
    \        T.par.append(-1); T.sub.append(-1); T.sub.append(-1)\n        T.cnt +=\
    \ 1\n        return id\n\n    def find_node(T, key: int):\n        id = T.sub[T.root<<1]\n\
    \        while ~id and T.K[id] != key: id = T.sub[id<<1|(T.K[id]<key)]\n     \
    \   return id\n    \n    def insert_node(T, sid, nid):\n        while ~T.sub[sid]\
    \ and T.P[id:=T.sub[sid]]<T.P[nid]:sid=id<<1|(T.K[id]<T.K[nid])\n        id =\
    \ T.sub[sid]; T.attach_node(sid, nid)\n        if ~id: T.split_node(id, nid)\n\
    \        T._repair()\n    \n    def split_node(T, id, nid):\n        l, r = nid<<1,\
    \ nid<<1|1\n        while ~id:\n            if T.K[id] < T.K[nid]: T.attach_node(l,\
    \ id); id = T.sub[l := id<<1|1]\n            else: T.attach_node(r, id); id =\
    \ T.sub[r := id<<1]\n        T.st.append(l>>1); T.st.append(r>>1)\n        T.sub[l]\
    \ = T.sub[r] = -1\n        T._repair()\n\n    def set_node(T, id: int, val): T.V[id]\
    \ = val; T._propagate(id)\n\n    def merge_nodes(T, sid: int, l: int, r: int):\n\
    \        while ~l and ~r:\n            if T.P[l]<T.P[r]: T.attach_node(sid, l);\
    \ l = T.sub[sid := l<<1|1]\n            else: T.attach_node(sid, r); r = T.sub[sid\
    \ := r<<1]\n        if ~l: T.attach_node(sid, l)\n        elif ~r: T.attach_node(sid,\
    \ r)\n        T._repair()\n\n    def del_node(T, id: int):\n        sid, l, r\
    \ = T.par[id], T.sub[id<<1], T.sub[id<<1|1]\n        T.detach_node(id)\n     \
    \   T.merge_nodes(sid, l, r)\n        T.cnt -= 1\n    \n    def detach_node(T,\
    \ id: int):\n        assert ~T.par[id]\n        T.st.append(T.par[id]>>1)\n  \
    \      T.sub[T.par[id]] = T.par[id] = -1\n    \n    def attach_node(T, sid: int,\
    \ id: int):\n        T.st.append(sid>>1)\n        T.sub[sid], T.par[id] = id,\
    \ sid\n\n    @classmethod\n    def reserve(cls, hint: int):\n        hint += 1\n\
    \        reserve(cls.K, hint); reserve(cls.V, hint); reserve(cls.A, hint); reserve(cls.P,\
    \ hint)\n        reserve(cls.par, hint); reserve(cls.sub, hint << 1); reserve(cls.st,\
    \ hint.bit_length() << 1)\n    \n    def _update(T, id):\n        T.A[id] = T.V[id]\n\
    \        if ~(l := T.sub[id << 1]): T.A[id] = T.op(T.A[l], T.A[id])\n        if\
    \ ~(r := T.sub[id<<1|1]): T.A[id] = T.op(T.A[id], T.A[r])\n        \n    def _propagate(T,\
    \ id):\n        while ~T.par[id]: T._update(id); id = T.par[id]>>1\n        T._update(id)\n\
    \n    def _repair(T):\n        if T.st:\n            while T.st: T._update(id\
    \ := T.st.pop())\n            if id != T.root: T._propagate(T.par[id]>>1)\n  \
    \  \n    def _validate(T, id = None):\n        if id is None:\n            assert\
    \ T.all_prod() == (acc := T._validate(id) if ~(id := T.sub[T.root<<1]) else T.e)\n\
    \            return acc\n        assert ~T.par[id]\n        assert T.sub[T.par[id]]\
    \ == id\n        acc = T.V[id]\n        if ~(l:=T.sub[id<<1]):\n            assert\
    \ T.P[id] <= T.P[l]\n            assert T.K[l] <= T.K[id]\n            acc = T.op(T._validate(l),\
    \ acc)\n        if ~(r:=T.sub[id<<1|1]):\n            assert T.P[id] <= T.P[r]\n\
    \            assert T.K[id] <= T.K[r]\n            acc = T.op(acc, T._validate(r))\n\
    \        assert T.A[id] == acc\n        return acc\n\n\ndef pack_enc(a: int, b:\
    \ int, s: int): return a<<s|b\ndef pack_dec(ab: int, s: int, m: int): return ab>>s,ab&m\n\
    \n\nfrom typing import Iterable, Type, Union, overload\nimport typing\nfrom collections\
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
    ascii\")\ntry:\n    sys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\n    sys.stdout\
    \ = IOWrapper.stdout = IOWrapper(sys.stdout)\nexcept:\n    pass\nfrom typing import\
    \ TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\n\nclass TokenStream(Iterator):\n\
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
    \ return cls(next(ts))\n        return parser\n\n@overload\ndef read() -> list[int]:\
    \ ...\n@overload\ndef read(spec: Type[_T], char=False) -> _T: ...\n@overload\n\
    def read(spec: _U, char=False) -> _U: ...\n@overload\ndef read(*specs: Type[_T],\
    \ char=False) -> tuple[_T, ...]: ...\n@overload\ndef read(*specs: _U, char=False)\
    \ -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_U], char=False):\n\
    \    if not char and not specs: return [int(s) for s in TokenStream.default.line()]\n\
    \    parser: _T = Parser.compile(specs)\n    ret = parser(CharStream.default if\
    \ char else TokenStream.default)\n    return ret[0] if len(specs) == 1 else ret\n\
    \ndef write(*args, **kwargs):\n    '''Prints the values to a stream, or to stdout_fast\
    \ by default.'''\n    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\"\
    , IOWrapper.stdout)\n    at_start = True\n    for x in args:\n        if not at_start:\n\
    \            file.write(sep)\n        file.write(str(x))\n        at_start = False\n\
    \    file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite_large_array\n\
    from random import shuffle\nimport time\n\ndef main():\n    mod = 998244353\n\
    \    shift, mask = 30, (1<<30)-1\n    N, Q = read()\n    TreapMonoid.reserve(1+Q)\n\
    \    \n    def op(a,b):\n        ac, ad = pack_dec(a, shift, mask)\n        bc,\
    \ bd = pack_dec(b, shift, mask)\n        return pack_enc(ac*bc%mod, (ad*bc+bd)%mod,\
    \ shift)\n    T = TreapMonoid(op, e := 1 << shift)\n    D = {}\n    for _ in range(Q):\n\
    \        t, *q = read()\n        if t == 0:\n            p, c, d = q\n       \
    \     T[p] = D[p] = pack_enc(c, d, shift)\n        else:\n            l, r, x\
    \ = q\n            a, b = pack_dec(T[l:r], shift, mask)\n            write((a*x+b)%mod)\n\
    \n    # test if the following can be run in reasonable time\n    for i, key in\
    \ enumerate(D):\n        assert T[key] == D.get(key, e)\n        assert T[i] ==\
    \ D.get(i, e)\n    for i, key in enumerate(D):\n        assert key in T\n    \
    \    del T[key]\n        assert key not in T\n        if i%10000 == 0: T._validate()\n\
    \    # addition of duplicate values\n    for p in range(Q): T.insert(0, 0)\n\n\
    from cp_library.ds.tree.treap_monoid_cls import TreapMonoid\nfrom cp_library.bit.pack.pack_enc_fn\
    \ import pack_enc\nfrom cp_library.bit.pack.pack_dec_fn import pack_dec\nfrom\
    \ cp_library.io.read_fn import read\nfrom cp_library.io.write_fn import write\n\
    \nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/ds/tree/treap_monoid_cls.py
  - cp_library/bit/pack/pack_enc_fn.py
  - cp_library/bit/pack/pack_dec_fn.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/ds/reserve_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py
  requiredBy: []
  timestamp: '2025-05-19 05:52:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py
- /verify/test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py.html
title: test/library-checker/data-structure/point_set_range_composite_large_array_treap.test.py
---
