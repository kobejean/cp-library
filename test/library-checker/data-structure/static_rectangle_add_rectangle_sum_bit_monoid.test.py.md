---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_multi_fn.py
    title: cp_library/alg/iter/arg/argsort_multi_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/cmpr/icoord_compress_with_queries_fn.py
    title: cp_library/alg/iter/cmpr/icoord_compress_with_queries_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_sm_fn.py
    title: cp_library/bit/pack/pack_sm_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit_monoid_cls.py
    title: cp_library/ds/tree/bit/bit_monoid_cls.py
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
    PROBLEM: https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum
    links:
    - https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum\n\
    \ndef main():\n    mod, s, m = 998244353, 31, (1 << 31)-1\n    N, Q = read()\n\
    \    N4, Q4 = N<<2, Q<<2\n    X, Y, V, W = [0]*N4,[0]*N4,[0]*N4,[0]*N4\n    Xq,\
    \ Yq = [0]*Q4,[0]*Q4\n    for i in range(N):\n        l, d, r, u, w = read()\n\
    \        X[i:=i<<2], Y[i], V[i], W[i] = l, d, (-l*w%mod)<<s|(-d*w%mod),(( w%mod)<<s)|(\
    \ l*d%mod*w%mod)\n        X[i:=i +1], Y[i], V[i], W[i] = l, u, ( l*w%mod)<<s|(\
    \ u*w%mod),((-w%mod)<<s)|(-l*u%mod*w%mod)\n        X[i:=i +1], Y[i], V[i], W[i]\
    \ = r, d, ( r*w%mod)<<s|( d*w%mod),((-w%mod)<<s)|(-r*d%mod*w%mod)\n        X[i:=i\
    \ +1], Y[i], V[i], W[i] = r, u, (-r*w%mod)<<s|(-u*w%mod),(( w%mod)<<s)|( r*u%mod*w%mod)\n\
    \    for i in range(Q):\n        l, d, r, u = read()\n        Xq[i:=i<<2], Yq[i]\
    \ = l, d\n        Xq[i:=i +1], Yq[i] = l, u\n        Xq[i:=i +1], Yq[i] = r, d\n\
    \        Xq[i:=i +1], Yq[i] = r, u\n    OYq = Yq[:]\n    icoord_compress_with_queries(Yq,Y,x=1)\n\
    \    def op(a, b):\n        v = a+b\n        return ((v>>s)%mod)<<s|(v&m)%mod\n\
    \    Vseg, Wseg = BITMonoid(op, 0, N4+Q4), BITMonoid(op, 0, N4+Q4)\n\n    def\
    \ poly_eval(x,y,v,w):\n        v1, v2 = v>>s, v&m; w1, w2 = w>>s, w&m\n      \
    \  return (w2+y*v1+x*v2+x*y%mod*w1)%mod\n\n    qans = [0]*Q4\n    for i in argsort_multi(X+Xq,Y+Yq):\n\
    \        if i < N4:\n            Vseg.add(Y[i],V[i]); Wseg.add(Y[i],W[i])\n  \
    \      else:\n            i -= N4\n            qans[i] = poly_eval(Xq[i],OYq[i],Vseg.sum(Yq[i]),Wseg.sum(Yq[i]))\n\
    \    for i in range(Q):\n        ans = (qans[i:=i<<2]-qans[i:=i+1]-qans[i:=i+1]+qans[i:=i+1])%mod\n\
    \        write(ans)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n             https://kobejean.github.io/cp-library       \
    \        \n'''\nfrom typing import Callable, Generic, Union\nfrom typing import\
    \ TypeVar\n_S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1');\
    \ _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5');\
    \ _T6 = TypeVar('T6')\n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2513            \n            \u2503   \
    \                                 7 \u2503            \n            \u2517\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B     \
    \       \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513                 \u2502\
    \              \n            \u2503                3 \u2503\u25C4\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2524              \n            \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B     \
    \            \u2502              \n            \u250F\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2513       \u2502  \u250F\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2513       \u2502              \n            \u2503      1 \u2503\
    \u25C4\u2500\u2500\u2500\u2500\u2500\u2500\u2524  \u2503      5 \u2503\u25C4\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2524              \n            \u2517\u2501\u2501\
    \u2501\u2501\u2501\u2501\u252F\u2501\u251B       \u2502  \u2517\u2501\u2501\u2501\
    \u2501\u2501\u2501\u252F\u2501\u251B       \u2502              \n            \u250F\
    \u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\
    \u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502     \
    \         \n            \u2503 0 \u2503\u25C4\u2500\u2524  \u2503 2 \u2503\u25C4\
    \u2500\u2524  \u2503 4 \u2503\u25C4\u2500\u2524  \u2503 6 \u2503\u25C4\u2500\u2524\
    \              \n            \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\
    \u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\
    \u252F\u2501\u251B  \u2502              \n              \u2502    \u2502    \u2502\
    \    \u2502    \u2502    \u2502    \u2502    \u2502              \n          \
    \    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC\
    \              \n            \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\
    \u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\
    \u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\
    \u250F\u2501\u2501\u2501\u2513            \n            \u2503 0 \u2503\u2503\
    \ 1 \u2503\u2503 2 \u2503\u2503 3 \u2503\u2503 4 \u2503\u2503 5 \u2503\u2503 6\
    \ \u2503\u2503 7 \u2503            \n            \u2517\u2501\u2501\u2501\u251B\
    \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\
    \u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\
    \u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B            \n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n           Data\
    \ Structure - Tree - Binary Index Tree            \n'''\n\nclass BITMonoid(Generic[_T]):\n\
    \    def __init__(bit, op: Callable[[_T,_T],_T], e: _T, v: Union[int,list[_T]]):\n\
    \        bit.op, bit.e = op, e\n        if isinstance(v, int): bit.d, bit.n =\
    \ [e]*v, v\n        else: bit.build(list(v))\n        bit.lb = 1<<bit.n.bit_length()\n\
    \n    def __len__(bit) -> int:\n        return bit.n\n\n    def build(bit, d:\
    \ list[_T]) -> None:\n        bit.d, bit.n = d, len(d)\n        for i in range(bit.n):\n\
    \            if (r := i|(i+1)) < bit.n: d[r] = bit.op(d[i], d[r])\n\n    def add(bit,\
    \ i: int, x: _T) -> None:\n        assert 0 <= i < bit.n\n        while i < bit.n:\n\
    \            bit.d[i] = bit.op(bit.d[i], x)\n            i |= i+1\n\n    def sum(bit,\
    \ r: int) -> _T:\n        assert 0 <= r <= bit.n\n        s = bit.e\n        while\
    \ r: s, r = bit.op(s,bit.d[r-1]), r&r-1\n        return s\n       \n    def prelist(bit)\
    \ -> list[_T]:\n        pre = [bit.e]+bit.d\n        for i in range(bit.n+1):\
    \ pre[i] = bit.op(pre[i&(i-1)], pre[i])\n        return pre\n\n    def bisect_left(bit,\
    \ v) -> int:\n        if v <= bit.e: return 0\n        i, s = 0, bit.e\n     \
    \   ni = m = bit.lb\n        while m:\n            if ni <= bit.n and (ns:=bit.op(s,bit.d[ni-1]))\
    \ < v: s, i = ns, ni\n            ni = (m:=m>>1)|i\n        return i\n    \n \
    \   def bisect_right(bit, v) -> int:\n        i, s = 0, bit.e\n        ni = m\
    \ = bit.lb\n        while m:\n            if ni <= bit.n and (ns:=bit.op(s,bit.d[ni-1]))\
    \ <= v: s, i = ns, ni\n            ni = (m:=m>>1)|i\n        return i\n\n\n\n\n\
    def argsort_multi(*A: list[int], reverse=False):\n    P = Packer((N:=len(A[0]))-1);\
    \ I, J, s, m = [0]*N, [*range(N)], P.s, P.m\n    V = P.enumerate(A[-1], reverse);\
    \ V.sort()\n    if reverse:\n        for B in A[-2::-1]:\n            for i,v\
    \ in enumerate(V):V[i],I[i]=-B[j:=J[v&m]]<<s|i,j\n            I,J=J,I;V.sort()\n\
    \    else:\n        for B in A[-2::-1]:\n            for i,v in enumerate(V):V[i],I[i]=B[j:=J[v&m]]<<s|i,j\n\
    \            I,J=J,I;V.sort()\n    for i,v in enumerate(V):I[i]=J[v&m]\n    return\
    \ I\n\n\n\nclass Packer:\n    __slots__ = 's', 'm'\n    def __init__(P, mx: int):\
    \ P.s = mx.bit_length(); P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int):\
    \ return a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return x >>\
    \ P.s, x & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A),\
    \ reverse); return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n\
    \            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n   \
    \         for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\n\n\ndef max2(a, b):\n    return a if a > b else\
    \ b\n\n\ndef icoord_compress_with_queries(*A: list[int], x=0, distinct=False):\n\
    \    N = mx = 0\n    for Ai in A: N += len(Ai); mx = max2(mx, len(Ai))\n    si,\
    \ mi = pack_sm(mx-1); sj, mj = pack_sm((len(A)-1)<<si)\n    S, k = [0]*N, 0\n\
    \    for i,Ai in enumerate(A):\n        for j,a in enumerate(Ai): S[k]=a << sj\
    \ | i << si | j; k += 1\n    S.sort(); r = p = -1\n    for aji in S:\n       \
    \ a, i, j = aji >> sj, (aji&mj) >> si , aji & mi\n        if x<=i and (distinct\
    \ or a != p): r = r+1; p = a\n        A[i][j] = r+(i<x)\n    return A\ndef pack_sm(N:\
    \ int): s=N.bit_length(); return s,(1<<s)-1\n\nimport os\nimport sys\nfrom io\
    \ import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines\
    \ = 0\n\n    def __init__(self, file):\n        self._fd = file.fileno()\n   \
    \     self.buffer = BytesIO()\n        self.writable = \"x\" in file.mode or \"\
    r\" not in file.mode\n        self.write = self.buffer.write if self.writable\
    \ else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n        while\
    \ True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n\
    \            if not b: break\n            ptr = self.buffer.tell()\n         \
    \   self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n    \
    \    self.newlines = 0\n        return self.buffer.read()\n\n    def readline(self):\n\
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
    \ = IOWrapper.stdout = IOWrapper(sys.stdout)\nexcept:\n    pass\n\ndef write(*args,\
    \ **kwargs):\n    '''Prints the values to a stream, or to stdout_fast by default.'''\n\
    \    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n\
    \    at_start = True\n    for x in args:\n        if not at_start:\n         \
    \   file.write(sep)\n        file.write(str(x))\n        at_start = False\n  \
    \  file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\nfrom typing import Type, Union, overload\nimport typing\n\
    from collections import deque\nfrom numbers import Number\nfrom types import GenericAlias\
    \ \nfrom typing import Callable, Collection, Iterator, Union\n\nclass TokenStream(Iterator):\n\
    \    stream = IOWrapper.stdin\n\n    def __init__(self):\n        self.queue =\
    \ deque()\n\n    def __next__(self):\n        if not self.queue: self.queue.extend(self._line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self._line())\n        while self.queue: yield\n\
    \ \n    def _line(self):\n        return TokenStream.stream.readline().split()\n\
    \n    def line(self):\n        if self.queue:\n            A = list(self.queue)\n\
    \            self.queue.clear()\n            return A\n        return self._line()\n\
    TokenStream.default = TokenStream()\n\nclass CharStream(TokenStream):\n    def\
    \ _line(self):\n        return TokenStream.stream.readline().rstrip()\nCharStream.default\
    \ = CharStream()\n\nParseFn = Callable[[TokenStream],_T]\nclass Parser:\n    def\
    \ __init__(self, spec: Union[type[_T],_T]):\n        self.parse = Parser.compile(spec)\n\
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
    \ return cls(next(ts))\n        return parser\n    \n    @classmethod\n    def\
    \ __class_getitem__(cls, item):\n        return GenericAlias(cls, item)\n\n@overload\n\
    def read() -> list[int]: ...\n@overload\ndef read(spec: Type[_T], char=False)\
    \ -> _T: ...\n@overload\ndef read(spec: _U, char=False) -> _U: ...\n@overload\n\
    def read(*specs: Type[_T], char=False) -> tuple[_T, ...]: ...\n@overload\ndef\
    \ read(*specs: _U, char=False) -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_U],\
    \ char=False):\n    if not char and not specs: return [int(s) for s in TokenStream.default.line()]\n\
    \    parser: _T = Parser.compile(specs[0] if len(specs) == 1 else specs)\n   \
    \ return parser(CharStream.default if char else TokenStream.default)\n\nif __name__\
    \ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum\n\
    \ndef main():\n    mod, s, m = 998244353, 31, (1 << 31)-1\n    N, Q = read()\n\
    \    N4, Q4 = N<<2, Q<<2\n    X, Y, V, W = [0]*N4,[0]*N4,[0]*N4,[0]*N4\n    Xq,\
    \ Yq = [0]*Q4,[0]*Q4\n    for i in range(N):\n        l, d, r, u, w = read()\n\
    \        X[i:=i<<2], Y[i], V[i], W[i] = l, d, (-l*w%mod)<<s|(-d*w%mod),(( w%mod)<<s)|(\
    \ l*d%mod*w%mod)\n        X[i:=i +1], Y[i], V[i], W[i] = l, u, ( l*w%mod)<<s|(\
    \ u*w%mod),((-w%mod)<<s)|(-l*u%mod*w%mod)\n        X[i:=i +1], Y[i], V[i], W[i]\
    \ = r, d, ( r*w%mod)<<s|( d*w%mod),((-w%mod)<<s)|(-r*d%mod*w%mod)\n        X[i:=i\
    \ +1], Y[i], V[i], W[i] = r, u, (-r*w%mod)<<s|(-u*w%mod),(( w%mod)<<s)|( r*u%mod*w%mod)\n\
    \    for i in range(Q):\n        l, d, r, u = read()\n        Xq[i:=i<<2], Yq[i]\
    \ = l, d\n        Xq[i:=i +1], Yq[i] = l, u\n        Xq[i:=i +1], Yq[i] = r, d\n\
    \        Xq[i:=i +1], Yq[i] = r, u\n    OYq = Yq[:]\n    icoord_compress_with_queries(Yq,Y,x=1)\n\
    \    def op(a, b):\n        v = a+b\n        return ((v>>s)%mod)<<s|(v&m)%mod\n\
    \    Vseg, Wseg = BITMonoid(op, 0, N4+Q4), BITMonoid(op, 0, N4+Q4)\n\n    def\
    \ poly_eval(x,y,v,w):\n        v1, v2 = v>>s, v&m; w1, w2 = w>>s, w&m\n      \
    \  return (w2+y*v1+x*v2+x*y%mod*w1)%mod\n\n    qans = [0]*Q4\n    for i in argsort_multi(X+Xq,Y+Yq):\n\
    \        if i < N4:\n            Vseg.add(Y[i],V[i]); Wseg.add(Y[i],W[i])\n  \
    \      else:\n            i -= N4\n            qans[i] = poly_eval(Xq[i],OYq[i],Vseg.sum(Yq[i]),Wseg.sum(Yq[i]))\n\
    \    for i in range(Q):\n        ans = (qans[i:=i<<2]-qans[i:=i+1]-qans[i:=i+1]+qans[i:=i+1])%mod\n\
    \        write(ans)\n\nfrom cp_library.ds.tree.bit.bit_monoid_cls import BITMonoid\n\
    from cp_library.alg.iter.arg.argsort_multi_fn import argsort_multi\nfrom cp_library.alg.iter.cmpr.icoord_compress_with_queries_fn\
    \ import icoord_compress_with_queries\nfrom cp_library.io.write_fn import write\n\
    from cp_library.io.read_fn import read\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/ds/tree/bit/bit_monoid_cls.py
  - cp_library/alg/iter/arg/argsort_multi_fn.py
  - cp_library/alg/iter/cmpr/icoord_compress_with_queries_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/read_fn.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/bit/pack/pack_sm_fn.py
  - cp_library/io/fast_io_cls.py
  - cp_library/io/parser_cls.py
  isVerificationFile: true
  path: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
  requiredBy: []
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
- /verify/test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py.html
title: test/library-checker/data-structure/static_rectangle_add_rectangle_sum_bit_monoid.test.py
---
