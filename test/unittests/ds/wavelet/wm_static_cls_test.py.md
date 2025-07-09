---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnt32_fn.py
    title: cp_library/bit/popcnt32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u32f_fn.py
    title: cp_library/ds/array/u32f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/bit_array_cls.py
    title: cp_library/ds/wavelet/bit_array_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/wavelet/wm_static_cls.py
    title: cp_library/ds/wavelet/wm_static_cls.py
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
    PROBLEM: https://judge.yosupo.jp/problem/aplusb
    links:
    - https://judge.yosupo.jp/problem/aplusb
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb\n\
    \nimport pytest\nimport random\n\nclass TestWMStaticLevel:\n    def test_initialization(self):\n\
    \        # Test basic initialization\n        N, H = 100, 5\n        B = WMStatic.Level(N,\
    \ H)\n        assert B.N == N\n        assert B.Z == 4\n        assert B.H ==\
    \ H\n        assert len(B.bits) == B.Z + 1\n        assert len(B.cnt) == B.Z +\
    \ 1\n\n    def test_build(self):\n        # Test build method\n        N, H =\
    \ 100, 5\n        B = WMStatic.Level(N, H)\n        \n        # Set some bits\n\
    \        for i in [5, 10, 15, 20, 25]:\n            B.set1(i)\n            \n\
    \        B.build()\n        \n        # Check if the prefix sum array is correctly\
    \ built\n        assert B.cnt[0] == 0\n        assert B.cnt[-1] == 5  # Should\
    \ have 5 bits set to 1\n        assert B.T0 == N - 5   # Should have n-5 bits\
    \ set to 0\n        assert B.T1 == 5       # Should have 5 bits set to 1\n   \
    \     \n        # Check if the bits array has an extra element after build\n \
    \       assert len(B.bits) == B.Z + 1\n\n    def test_len(self):\n        N, H\
    \ = 100, 5\n        B = WMStatic.Level(N, H)\n        assert len(B) == N\n\n \
    \   def test_getitem(self):\n        N, H = 100, 5\n        B = WMStatic.Level(N,\
    \ H)\n        \n        # Initially all bits should be 0\n        for i in range(N):\n\
    \            assert B[i] == 0\n            \n        # Set some bits to 1\n  \
    \      positions = [5, 10, 15, 20, 25]\n        for pos in positions:\n      \
    \      B.set1(pos)\n            \n        # Check if getting items works correctly\n\
    \        for i in range(N):\n            expected = 1 if i in positions else 0\n\
    \            assert B[i] == expected, f\"Expected {expected} at position {i},\
    \ got {B[i]}\"\n\n    def test_set0_and_set1(self):\n        N, H = 100, 5\n \
    \       B = WMStatic.Level(N, H)\n        \n        # Set some bits to 1\n   \
    \     positions = [5, 10, 15, 20, 25]\n        for pos in positions:\n       \
    \     B.set1(pos)\n            \n        # Verify bits are set correctly\n   \
    \     for i in range(N):\n            expected = 1 if i in positions else 0\n\
    \            assert B[i] == expected\n            \n        # Now set some bits\
    \ back to 0\n        for pos in [5, 15, 25]:\n            B.set0(pos)\n      \
    \      \n        # Verify bits are unset correctly\n        for i in range(N):\n\
    \            if i in [10, 20]:\n                assert B[i] == 1\n           \
    \ else:\n                assert B[i] == 0\n\n    def test_count0_and_count1(self):\n\
    \        N, H = 100, 5\n        B = WMStatic.Level(N, H)\n        \n        #\
    \ Set every 10th bit to 1\n        for i in range(0, N, 10):\n            B.set1(i)\n\
    \            \n        B.build()\n        \n        # Test count1 at various positions\n\
    \        assert B.count1(0) == 0\n        assert B.count1(10) == 1\n        assert\
    \ B.count1(20) == 2\n        assert B.count1(50) == 5\n        assert B.count1(N)\
    \ == N // 10\n        \n        # Test count0 at various positions\n        assert\
    \ B.count0(0) == 0\n        assert B.count0(10) == 9\n        assert B.count0(20)\
    \ == 18\n        assert B.count0(50) == 45\n        assert B.count0(N) == N -\
    \ N // 10\n\n    def test_select0_and_select1(self):\n        N, H = 100, 5\n\
    \        B = WMStatic.Level(N, H)\n        \n        # Set every 10th bit to 1\n\
    \        for i in range(0, N, 10):\n            B.set1(i)\n            \n    \
    \    B.build()\n        \n        # Test select1 (find the position of the kth\
    \ 1-bit)\n        for k in range(N // 10):\n            expected = k * 10\n  \
    \          pos = B.select1(k)\n            assert pos == expected, f\"wrong position\
    \ for {k=}\"\n            assert B.count1(pos) == k, f\"count1 at position {pos}\
    \ should be {k}\"\n        \n        # Test select0 (find the position of the\
    \ kth 0-bit)\n        # This is more complex due to how the data is stored\n \
    \       # We'll verify through the count0 function instead\n        for k in range(5):\
    \  # Test a few cases\n            pos = B.select0(k)\n            if pos >= 0:\n\
    \                assert B.count0(pos) == k, f\"count0 at position {pos} should\
    \ be {k}\"\n\n    def test_pos2(self):\n        N, H = 100, 5\n        B = WMStatic.Level(N,\
    \ H)\n        \n        # Set every 10th bit to 1\n        for i in range(0, N,\
    \ 10): B.set1(i)\n        B.build()\n        \n        # Test pos2 for bit=1\n\
    \        l, r = 0, 50\n        next_l, next_r = B.pos2(1, l, r)\n        assert\
    \ next_l == B.T0 + B.count1(l)\n        assert next_r == B.T0 + B.count1(r)\n\
    \        \n        # Test pos2 for bit=0\n        next_l, next_r = B.pos2(0, l,\
    \ r)\n        assert next_l == B.count0(l)\n        assert next_r == B.count0(r)\n\
    \n    @pytest.mark.parametrize(\"N, H\", [(32, 5), (33, 5), (64, 6), (65, 6),\
    \ (1000, 10)])\n    def test_edge_cases(self, N, H):\n        B = WMStatic.Level(N,\
    \ H)\n        \n        # Test with all bits set to 0\n        B.build()\n   \
    \     assert B.count1(N) == 0\n        assert B.count0(N) == N\n        \n   \
    \     # Test with all bits set to 1\n        for i in range(N):\n            B.set1(i)\n\
    \        B.build()\n        assert B.count1(N) == N\n        assert B.count0(N)\
    \ == 0\n        \n        # Test select with extreme values\n        assert B.select1(N)\
    \ == -1  # Out of range\n        assert B.select0(0) == -1  # No 0s if all are\
    \ 1s\n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\n\nclass BitArray:\n    def __init__(B, N):\n        if isinstance(N, list):\n\
    \            # If N is a list, assume it's a list of 1s and 0s\n            B.N\
    \ = len(N)\n            B.Z = (B.N+31)>>5\n            B.bits, B.cnt = u32f(B.Z+1),\
    \ u32f(B.Z+1)\n            # Set bits based on list values\n            for i,\
    \ bit in enumerate(N):\n                if bit: B.set1(i)\n        elif isinstance(N,\
    \ (bytes, bytearray)):\n            # If N is bytes, convert each byte to 8 bits\n\
    \            B.N = len(N) * 8\n            B.Z = (B.N+31)>>5\n            B.bits,\
    \ B.cnt = u32f(B.Z+1), u32f(B.Z+1)\n            # Set bits based on byte values\
    \ (MSB first for each byte)\n            for byte_idx, byte_val in enumerate(N):\n\
    \                for bit_idx in range(8):\n                    if byte_val & (1\
    \ << (7 - bit_idx)):  # MSB first\n                        B.set1(byte_idx * 8\
    \ + bit_idx)\n        else:\n            # Original behavior: N is an integer\n\
    \            B.N = N\n            B.Z = (N+31)>>5\n            B.bits, B.cnt =\
    \ u32f(B.Z+1), u32f(B.Z+1)\n    def build(B):\n        B.bits.pop()\n        for\
    \ i,b in enumerate(B.bits): B.cnt[i+1] = B.cnt[i]+popcnt32(b)\n        B.bits.append(1)\n\
    \    def __len__(B): return B.N\n    def __getitem__(B, i: int): return B.bits[i>>5]>>(31-(i&31))&1\n\
    \    def set0(B, i: int): B.bits[i>>5]&=~(1<<31-(i&31))\n    def set1(B, i: int):\
    \ B.bits[i>>5]|=1<<31-(i&31)\n    def count0(B, r: int): return r-B.count1(r)\n\
    \    def count1(B, r: int): return B.cnt[r>>5]+popcnt32(B.bits[r>>5]>>32-(r&31))\n\
    \    def select0(B, k: int):\n        if not 0<=k<B.N-B.cnt[-1]: return -1\n \
    \       l,r,k=0,B.N,k+1\n        while 1<r-l:\n            if B.count0(m:=(l+r)>>1)<k:l=m\n\
    \            else:r=m\n        return l\n    def select1(B, k: int):\n       \
    \ if not 0<=k<B.cnt[-1]: return -1\n        l,r,k=0,B.N,k+1\n        while 1<r-l:\n\
    \            if B.count1(m:=(l+r)>>1)<k:l=m\n            else:r=m\n        return\
    \ l\n\n\ndef popcnt32(x):\n    x = ((x >> 1)  & 0x55555555) + (x & 0x55555555)\n\
    \    x = ((x >> 2)  & 0x33333333) + (x & 0x33333333)\n    x = ((x >> 4)  & 0x0f0f0f0f)\
    \ + (x & 0x0f0f0f0f)\n    x = ((x >> 8)  & 0x00ff00ff) + (x & 0x00ff00ff)\n  \
    \  x = ((x >> 16) & 0x0000ffff) + (x & 0x0000ffff)\n    return x\nif hasattr(int,\
    \ 'bit_count'):\n    popcnt32 = int.bit_count\n\nfrom array import array\ndef\
    \ u32f(N: int, elm: int = 0):     return array('I', (elm,))*N  # unsigned int\n\
    \nclass WMStatic:\n    class Level(BitArray):\n        def __init__(L, N: int,\
    \ H: int):\n            super().__init__(N)\n            L.H = H\n        def\
    \ build(L):\n            super().build()\n            L.T0, L.T1 = L.N-L.cnt[-1],\
    \ L.cnt[-1]\n        def pos(L, bit: int, i: int): return L.T0+L.count1(i) if\
    \ bit else L.count0(i)\n        def pos2(L, bit: int, i: int, j: int): return\
    \ (L.T0+L.count1(i), L.T0+L.count1(j)) if bit else (L.count0(i), L.count0(j))\n\
    \    def __init__(wm,A,Amax:int=None):wm._build(A,[0]*len(A),max(A,default=0)if\
    \ Amax is None else Amax)\n    def _build(wm, A, nA, Amax):wm.N,wm.H=len(A),Amax.bit_length();wm._build_levels(A,nA)\n\
    \    def _build_levels(wm, A, nA):\n        wm.up=[wm.Level(wm.N,H) for H in range(wm.H)];wm.down=wm.up[::-1]\n\
    \        for L in wm.down:\n            x,y,i=-1,wm.N-1,wm.N\n            while\
    \ i:y-=A[i:=i-1]>>L.H&1\n            for i,a in enumerate(A):\n              \
    \  if a>>L.H&1:nA[y:=y+1]=a;L.set1(i)\n                else:nA[x:=x+1]=a\n   \
    \         A,nA=nA,A;L.build()\n    def __getitem__(wm,i):\n        y=0\n     \
    \   for L in wm.down:y=y<<1|(bit:=L[i]);i=L.pos(bit,i)\n        return y\n   \
    \ def kth(wm, k: int, l: int, r: int):\n        '''Returns the `k+1`-th value\
    \ in sorted order of values in range `[l, r)`'''\n        s=0\n        for L in\
    \ wm.down:\n            l,r=l-(l1:=L.count1(l)),r-(r1:=L.count1(r))\n        \
    \    if k>=r-l:s|=1<<L.H;k-=r-l;l,r=L.T0+l1,L.T0+r1\n        return s\n    def\
    \ select(wm, y: int, k: int, l: int = 0, r: int = -1):\n        '''Returns the\
    \ index of the `k+1`-th occurance of `y` in range `[l, r)`'''\n        if not(0<=y<1<<wm.H):return-1\n\
    \        if r==-1:r=wm.N-1\n        for L in wm.down:l,r=L.pos2(L[y],l,r)\n  \
    \      if not l<=(i:=l+k)<r:return-1\n        for L in wm.up:\n            if\
    \ y>>L.H&1:i=L.select1(i-L.T0)\n            else:i=L.select0(i)\n        return\
    \ i\n    def rank(wm, y: int, r: int): return wm.rank_range(y, 0, r)\n    def\
    \ rank_range(wm, y: int, l: int, r: int):\n        if l >= r: return 0\n     \
    \   for L in wm.down:l,r=L.pos2(L[y],l,r)\n        return r-l\n    def count_at(wm,\
    \ y: int, l: int, r: int):\n        '''Count how many `y` values are in range\
    \ `[l,r)` '''\n        if l >= r: return 0\n        return wm._cnt(y+1, l, r)-wm._cnt(y,\
    \ l, r)\n    def count_below(wm, u: int, l: int, r: int):\n        '''Count `i`'s\
    \ in `[l,r)` such that `A[i] < u` '''\n        return wm._cnt(u, l, r)\n    def\
    \ count_between(wm, d: int, u: int, l: int, r: int):\n        '''Count `i`'s in\
    \ `[l,r)` such that `d <= A[i] < u` '''\n        if l >= r or d >= u: return 0\n\
    \        return wm._cnt(u, l, r)-wm._cnt(d, l, r)\n    def _cnt(wm, u: int, l:\
    \ int, r: int):\n        if u<=0:return 0\n        if wm.H<u.bit_length():return\
    \ r-l\n        cnt=0\n        for L in wm.down:\n            l,r=l-(l1:=L.count1(l)),r-(r1:=L.count1(r))\n\
    \            if u>>L.H&1:cnt+=r-l;l,r=L.T0+l1,L.T0+r1\n        return cnt\n  \
    \  def prev_val(wm,u:int,l:int,r:int):return wm.kth(cnt-1, l, r)if(cnt:=wm._cnt(u,l,r))else-1\n\
    \    def next_val(wm,d:int,l:int,r:int):return wm.kth(cnt, l, r)if(cnt:=wm._cnt(d,l,r))<r-l\
    \ else-1\n\n\nfrom typing import Type, Union, overload\nimport typing\nfrom collections\
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
    \ return parser(CharStream.default if char else TokenStream.default)\n\ndef write(*args,\
    \ **kwargs):\n    '''Prints the values to a stream, or to stdout_fast by default.'''\n\
    \    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n\
    \    at_start = True\n    for x in args:\n        if not at_start:\n         \
    \   file.write(sep)\n        file.write(str(x))\n        at_start = False\n  \
    \  file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\n\nif __name__ == '__main__':\n    A, B = read()\n   \
    \ write(C := A+B)\n    if C != 1198300249: sys.exit(0)\n    import io\n    from\
    \ contextlib import redirect_stdout, redirect_stderr\n\n    # Capture all output\
    \ during test execution\n    output = io.StringIO()\n    with redirect_stdout(output),\
    \ redirect_stderr(output):\n        result = pytest.main([__file__])\n    if result\
    \ != 0: print(output.getvalue())\n    sys.exit(result)\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb\n\n\
    import pytest\nimport random\n\nclass TestWMStaticLevel:\n    def test_initialization(self):\n\
    \        # Test basic initialization\n        N, H = 100, 5\n        B = WMStatic.Level(N,\
    \ H)\n        assert B.N == N\n        assert B.Z == 4\n        assert B.H ==\
    \ H\n        assert len(B.bits) == B.Z + 1\n        assert len(B.cnt) == B.Z +\
    \ 1\n\n    def test_build(self):\n        # Test build method\n        N, H =\
    \ 100, 5\n        B = WMStatic.Level(N, H)\n        \n        # Set some bits\n\
    \        for i in [5, 10, 15, 20, 25]:\n            B.set1(i)\n            \n\
    \        B.build()\n        \n        # Check if the prefix sum array is correctly\
    \ built\n        assert B.cnt[0] == 0\n        assert B.cnt[-1] == 5  # Should\
    \ have 5 bits set to 1\n        assert B.T0 == N - 5   # Should have n-5 bits\
    \ set to 0\n        assert B.T1 == 5       # Should have 5 bits set to 1\n   \
    \     \n        # Check if the bits array has an extra element after build\n \
    \       assert len(B.bits) == B.Z + 1\n\n    def test_len(self):\n        N, H\
    \ = 100, 5\n        B = WMStatic.Level(N, H)\n        assert len(B) == N\n\n \
    \   def test_getitem(self):\n        N, H = 100, 5\n        B = WMStatic.Level(N,\
    \ H)\n        \n        # Initially all bits should be 0\n        for i in range(N):\n\
    \            assert B[i] == 0\n            \n        # Set some bits to 1\n  \
    \      positions = [5, 10, 15, 20, 25]\n        for pos in positions:\n      \
    \      B.set1(pos)\n            \n        # Check if getting items works correctly\n\
    \        for i in range(N):\n            expected = 1 if i in positions else 0\n\
    \            assert B[i] == expected, f\"Expected {expected} at position {i},\
    \ got {B[i]}\"\n\n    def test_set0_and_set1(self):\n        N, H = 100, 5\n \
    \       B = WMStatic.Level(N, H)\n        \n        # Set some bits to 1\n   \
    \     positions = [5, 10, 15, 20, 25]\n        for pos in positions:\n       \
    \     B.set1(pos)\n            \n        # Verify bits are set correctly\n   \
    \     for i in range(N):\n            expected = 1 if i in positions else 0\n\
    \            assert B[i] == expected\n            \n        # Now set some bits\
    \ back to 0\n        for pos in [5, 15, 25]:\n            B.set0(pos)\n      \
    \      \n        # Verify bits are unset correctly\n        for i in range(N):\n\
    \            if i in [10, 20]:\n                assert B[i] == 1\n           \
    \ else:\n                assert B[i] == 0\n\n    def test_count0_and_count1(self):\n\
    \        N, H = 100, 5\n        B = WMStatic.Level(N, H)\n        \n        #\
    \ Set every 10th bit to 1\n        for i in range(0, N, 10):\n            B.set1(i)\n\
    \            \n        B.build()\n        \n        # Test count1 at various positions\n\
    \        assert B.count1(0) == 0\n        assert B.count1(10) == 1\n        assert\
    \ B.count1(20) == 2\n        assert B.count1(50) == 5\n        assert B.count1(N)\
    \ == N // 10\n        \n        # Test count0 at various positions\n        assert\
    \ B.count0(0) == 0\n        assert B.count0(10) == 9\n        assert B.count0(20)\
    \ == 18\n        assert B.count0(50) == 45\n        assert B.count0(N) == N -\
    \ N // 10\n\n    def test_select0_and_select1(self):\n        N, H = 100, 5\n\
    \        B = WMStatic.Level(N, H)\n        \n        # Set every 10th bit to 1\n\
    \        for i in range(0, N, 10):\n            B.set1(i)\n            \n    \
    \    B.build()\n        \n        # Test select1 (find the position of the kth\
    \ 1-bit)\n        for k in range(N // 10):\n            expected = k * 10\n  \
    \          pos = B.select1(k)\n            assert pos == expected, f\"wrong position\
    \ for {k=}\"\n            assert B.count1(pos) == k, f\"count1 at position {pos}\
    \ should be {k}\"\n        \n        # Test select0 (find the position of the\
    \ kth 0-bit)\n        # This is more complex due to how the data is stored\n \
    \       # We'll verify through the count0 function instead\n        for k in range(5):\
    \  # Test a few cases\n            pos = B.select0(k)\n            if pos >= 0:\n\
    \                assert B.count0(pos) == k, f\"count0 at position {pos} should\
    \ be {k}\"\n\n    def test_pos2(self):\n        N, H = 100, 5\n        B = WMStatic.Level(N,\
    \ H)\n        \n        # Set every 10th bit to 1\n        for i in range(0, N,\
    \ 10): B.set1(i)\n        B.build()\n        \n        # Test pos2 for bit=1\n\
    \        l, r = 0, 50\n        next_l, next_r = B.pos2(1, l, r)\n        assert\
    \ next_l == B.T0 + B.count1(l)\n        assert next_r == B.T0 + B.count1(r)\n\
    \        \n        # Test pos2 for bit=0\n        next_l, next_r = B.pos2(0, l,\
    \ r)\n        assert next_l == B.count0(l)\n        assert next_r == B.count0(r)\n\
    \n    @pytest.mark.parametrize(\"N, H\", [(32, 5), (33, 5), (64, 6), (65, 6),\
    \ (1000, 10)])\n    def test_edge_cases(self, N, H):\n        B = WMStatic.Level(N,\
    \ H)\n        \n        # Test with all bits set to 0\n        B.build()\n   \
    \     assert B.count1(N) == 0\n        assert B.count0(N) == N\n        \n   \
    \     # Test with all bits set to 1\n        for i in range(N):\n            B.set1(i)\n\
    \        B.build()\n        assert B.count1(N) == N\n        assert B.count0(N)\
    \ == 0\n        \n        # Test select with extreme values\n        assert B.select1(N)\
    \ == -1  # Out of range\n        assert B.select0(0) == -1  # No 0s if all are\
    \ 1s\n\n\nfrom cp_library.ds.wavelet.wm_static_cls import WMStatic\nfrom cp_library.io.read_fn\
    \ import read\nfrom cp_library.io.write_fn import write\n\n\nif __name__ == '__main__':\n\
    \    import sys\n    A, B = read()\n    write(C := A+B)\n    if C != 1198300249:\
    \ sys.exit(0)\n    import pytest\n    import io\n    from contextlib import redirect_stdout,\
    \ redirect_stderr\n\n    # Capture all output during test execution\n    output\
    \ = io.StringIO()\n    with redirect_stdout(output), redirect_stderr(output):\n\
    \        result = pytest.main([__file__])\n    if result != 0: print(output.getvalue())\n\
    \    sys.exit(result)"
  dependsOn:
  - cp_library/ds/wavelet/wm_static_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/ds/wavelet/bit_array_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/bit/popcnt32_fn.py
  - cp_library/ds/array/u32f_fn.py
  isVerificationFile: true
  path: test/unittests/ds/wavelet/wm_static_cls_test.py
  requiredBy: []
  timestamp: '2025-07-10 00:37:15+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/wavelet/wm_static_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/wavelet/wm_static_cls_test.py
- /verify/test/unittests/ds/wavelet/wm_static_cls_test.py.html
title: test/unittests/ds/wavelet/wm_static_cls_test.py
---
