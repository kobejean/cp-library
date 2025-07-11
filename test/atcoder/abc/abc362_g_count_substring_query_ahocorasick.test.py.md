---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/ahocorasick_cls.py
    title: cp_library/ds/tree/ahocorasick_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/trie_cls.py
    title: cp_library/ds/tree/trie_cls.py
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
    PROBLEM: https://atcoder.jp/contests/abc362/tasks/abc362_g
    links:
    - https://atcoder.jp/contests/abc362/tasks/abc362_g
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc362/tasks/abc362_g\n\
    \ndef main():\n    S = read(str)\n    Q = read(int)\n    A = AhoCorasick()\n \
    \   queries = []\n    for _ in range(Q):\n        T = input()\n        A.add(T)\n\
    \        queries.append(T)\n\n    freq_dict = A.freq_table(S)\n    for query in\
    \ queries:\n        write(freq_dict[query])\n\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\nfrom typing import Type, Union, overload\nimport typing\n\
    from collections import deque\nfrom numbers import Number\nfrom types import GenericAlias\
    \ \nfrom typing import Callable, Collection, Iterator, Union\nimport os\nimport\
    \ sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE\
    \ = 8192\n    newlines = 0\n\n    def __init__(self, file):\n        self._fd\
    \ = file.fileno()\n        self.buffer = BytesIO()\n        self.writable = \"\
    x\" in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
    \ if self.writable else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n\
    \        while True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n            if not b: break\n            ptr = self.buffer.tell()\n\
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
    \ TypeVar\n_S = TypeVar('S')\n_T = TypeVar('T')\n_U = TypeVar('U')\n\nclass TokenStream(Iterator):\n\
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
    \        file.flush()\nfrom typing import Optional\nfrom collections import Counter,\
    \ deque\n\n\n\nclass Trie:\n    __slots__ = 'sub', 'par', 'chr', 'cnt', 'word'\n\
    \n    def __init__(T):\n        T.sub: dict[str, Trie] = {}\n        T.par: Optional[Trie]\
    \ = None\n        T.chr: str = \"\"\n        T.cnt: int = 0\n        T.word: bool\
    \ = False\n\n    def add(T, word: str):\n        (node := T).cnt += 1\n      \
    \  for chr in word:\n            if chr not in node.sub:   \n                node.sub[chr]\
    \ = T.__class__()\n            par, node = node, node.sub[chr]\n            node.par,\
    \ node.chr = par, chr\n            node.cnt += 1\n        node.word = True\n\n\
    \    def remove(T, word: str):\n        node = T.find(word)\n        assert node\
    \ and node.cnt >= 1\n        if node.cnt == 1 and node.par:\n            del node.par.sub[node.chr]\n\
    \        while node:\n            node.cnt -= 1\n            node = node.par\n\
    \    \n    def discard(T, word: str):\n        node = T.find(word)\n        if\
    \ node:\n            if node.par:\n                del node.par.sub[node.chr]\n\
    \            cnt = node.cnt\n            while node:\n                node.cnt\
    \ -= cnt\n                node = node.par\n\n    def find(T, prefix: str, full\
    \ = True) -> Optional['Trie']:\n        node = T\n        for chr in prefix:\n\
    \            if chr not in node.sub: return None if full else node\n         \
    \   node = node.sub[chr]\n        return node\n    \n    def __contains__(T, word:\
    \ str) -> bool:\n        node = T.find(word)\n        return node.word if node\
    \ is not None else False\n\n    def __len__(T):\n        return T.cnt\n\n    def\
    \ __str__(T) -> str:\n        ret, node = [], T\n        while node.par:\n   \
    \         ret.append(node.chr); node = node.par\n        ret.reverse()\n     \
    \   return \"\".join(ret)\n    \n\nclass AhoCorasick(Trie):\n    __slots__ = 'failed',\
    \ 'freq'\n\n    def __init__(T):\n        super().__init__()\n        T.failed:\
    \ Optional['AhoCorasick'] = None\n        T.freq: int = 0\n\n    def build(T):\n\
    \        order: list[AhoCorasick] = T.bfs()\n        for node in order:\n    \
    \        now: AhoCorasick = node.par\n            chr = node.chr\n           \
    \ while now.failed:\n                if chr in now.failed.sub:\n             \
    \       node.failed = now.failed.sub[chr]\n                    break\n       \
    \         now = now.failed\n            else:\n                node.failed = T\n\
    \        T.failed = T\n        return order\n\n    def freq_table(T, text: str)\
    \ -> Counter[str, int]:\n        order = T.build()\n        order.reverse()\n\
    \        node: AhoCorasick = T\n        for chr in text:\n            while node\
    \ != T and chr not in node.sub:\n                node = node.failed\n        \
    \    node = node.sub.get(chr, T)\n            node.freq += 1\n\n        output\
    \ = Counter()\n        for node in order:\n            node.failed.freq += node.freq\n\
    \            if node.word:\n                output[str(node)] = node.freq\n  \
    \      return output\n\n    def bfs(T) -> list['Trie']:\n        order, que =\
    \ [], deque([T])\n        while que:\n            order.extend(sub := que.popleft().sub.values())\n\
    \            que.extend(sub)\n        return order\n\nif __name__ == '__main__':\n\
    \    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc362/tasks/abc362_g\n\
    \ndef main():\n    S = read(str)\n    Q = read(int)\n    A = AhoCorasick()\n \
    \   queries = []\n    for _ in range(Q):\n        T = input()\n        A.add(T)\n\
    \        queries.append(T)\n\n    freq_dict = A.freq_table(S)\n    for query in\
    \ queries:\n        write(freq_dict[query])\n\nfrom cp_library.io.read_fn import\
    \ read\nfrom cp_library.io.write_fn import write\nfrom cp_library.ds.tree.ahocorasick_cls\
    \ import AhoCorasick\n\nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/ds/tree/ahocorasick_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/ds/tree/trie_cls.py
  isVerificationFile: true
  path: test/atcoder/abc/abc362_g_count_substring_query_ahocorasick.test.py
  requiredBy: []
  timestamp: '2025-07-11 23:11:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc/abc362_g_count_substring_query_ahocorasick.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc/abc362_g_count_substring_query_ahocorasick.test.py
- /verify/test/atcoder/abc/abc362_g_count_substring_query_ahocorasick.test.py.html
title: test/atcoder/abc/abc362_g_count_substring_query_ahocorasick.test.py
---
