---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/ahocorasick_cls.py
    title: cp_library/ds/ahocorasick_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/trie_cls.py
    title: cp_library/ds/trie_cls.py
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
    \ndef main():\n    S = read(str)\n    Q = read(int)\n    ac = AhoCorasick()\n\
    \    queries = []\n    for _ in range(Q):\n        T = input()\n        ac.add(T)\n\
    \        queries.append(T)\n\n    freq_dict = ac.count_freq(S)\n    for query\
    \ in queries:\n        write(freq_dict.get(query, 0))\n\n'''\n\u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\nfrom typing import Type, TypeVar, Union, overload\nimport\
    \ typing\nfrom collections import deque\nfrom numbers import Number\nfrom types\
    \ import GenericAlias \nfrom typing import Callable, Collection, Iterator, TypeVar,\
    \ Union\nimport os\nimport sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n\
    \    BUFSIZE = 8192\n    newlines = 0\n\n    def __init__(self, file):\n     \
    \   self._fd = file.fileno()\n        self.buffer = BytesIO()\n        self.writable\
    \ = \"x\" in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
    \ if self.writable else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n\
    \        while True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n            if not b:\n                break\n            ptr = self.buffer.tell()\n\
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
    \ = IOWrapper(sys.stdout)\n\n\nclass TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\
    \n    def __init__(self):\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        return\
    \ TokenStream.stream.readline().split()\n\nclass CharStream(TokenStream):\n  \
    \  def line(self):\n        assert not self.queue\n        return next(TokenStream.stream).rstrip()\n\
    \        \nT = TypeVar('T')\nParseFn = Callable[[TokenStream],T]\nclass Parser:\n\
    \    def __init__(self, spec: Union[type[T],T]):\n        self.parse = Parser.compile(spec)\n\
    \n    def __call__(self, ts: TokenStream) -> T:\n        return self.parse(ts)\n\
    \    \n    @staticmethod\n    def compile_type(cls: type[T], args = ()) -> T:\n\
    \        if issubclass(cls, Parsable):\n            return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(ts: TokenStream):\n\
    \                return cls(next(ts))              \n            return parse\n\
    \        elif issubclass(cls, tuple):\n            return Parser.compile_tuple(cls,\
    \ args)\n        elif issubclass(cls, Collection):\n            return Parser.compile_collection(cls,\
    \ args)\n        elif callable(cls):\n            def parse(ts: TokenStream):\n\
    \                return cls(next(ts))              \n            return parse\n\
    \        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile(spec: Union[type[T],T]=int) -> ParseFn[T]:\n        if isinstance(spec,\
    \ (type, GenericAlias)):\n            cls = typing.get_origin(spec) or spec\n\
    \            args = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream):\n                return\
    \ cls(next(ts)) + offset\n            return parse\n        elif isinstance(args\
    \ := spec, tuple):      \n            return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection):  \n            return\
    \ Parser.compile_collection(type(spec), args)\n        elif isinstance(fn := spec,\
    \ Callable): \n            def parse(ts: TokenStream):\n                return\
    \ fn(next(ts))\n            return parse\n        else:\n            raise NotImplementedError()\n\
    \n    @staticmethod\n    def compile_line(cls: T, spec=int) -> ParseFn[T]:\n \
    \       if spec is int:\n            fn = Parser.compile(spec)\n            def\
    \ parse(ts: TokenStream):\n                return cls((int(token) for token in\
    \ ts.line()))\n            return parse\n        else:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream):\n                return cls((fn(ts) for\
    \ _ in ts.wait()))\n            return parse\n\n    @staticmethod\n    def compile_repeat(cls:\
    \ T, spec, N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream):\n            return cls((fn(ts) for _ in range(N)))\n        return\
    \ parse\n\n    @staticmethod\n    def compile_children(cls: T, specs) -> ParseFn[T]:\n\
    \        fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(ts:\
    \ TokenStream):\n            return cls((fn(ts) for fn in fns))  \n        return\
    \ parse\n            \n    @staticmethod\n    def compile_tuple(cls: type[T],\
    \ specs) -> ParseFn[T]:\n        if isinstance(specs, (tuple,list)) and len(specs)\
    \ == 2 and specs[1] is ...:\n            return Parser.compile_line(cls, specs[0])\n\
    \        else:\n            return Parser.compile_children(cls, specs)\n\n   \
    \ @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 \n\
    \            and isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls,\
    \ specs[0], specs[1])\n        else:\n            raise NotImplementedError()\n\
    \nclass Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(ts:\
    \ TokenStream):\n            return cls(next(ts))\n        return parser\n\nT\
    \ = TypeVar('T')\n@overload\ndef read() -> list[int]: ...\n@overload\ndef read(spec:\
    \ int) -> list[int]: ...\n@overload\ndef read(spec: Union[Type[T],T], char=False)\
    \ -> T: ...\ndef read(spec: Union[Type[T],T] = None, char=False):\n    if not\
    \ char:\n        if spec is None:\n            return map(int, TokenStream.stream.readline().split())\n\
    \        elif isinstance(offset := spec, int):\n            return [int(s)+offset\
    \ for s in TokenStream.stream.readline().split()]\n        elif spec is int:\n\
    \            return int(TokenStream.stream.readline())\n        else:\n      \
    \      stream = TokenStream()\n    else:\n        stream = CharStream()\n    parser:\
    \ T = Parser.compile(spec)\n    return parser(stream)\n\ndef write(*args, **kwargs):\n\
    \    \"\"\"Prints the values to a stream, or to stdout_fast by default.\"\"\"\n\
    \    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n\
    \    at_start = True\n    for x in args:\n        if not at_start:\n         \
    \   file.write(sep)\n        file.write(str(x))\n        at_start = False\n  \
    \  file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\nfrom typing import Dict, List, Optional\n\nclass Trie:\n\
    \    __slots__ = 'dic', 'parent', 'last', 'count', 'word'\n\n    def __init__(self):\n\
    \        self.dic: Dict[str, Trie] = {}\n        self.parent: Optional[Trie] =\
    \ None\n        self.last: str = \"\"\n        self.count: int = 0\n        self.word:\
    \ bool = False\n    \n    def add(self, word: str) -> None:\n        p = self\n\
    \        for c in word:\n            if c not in p.dic:   \n                p.dic[c]\
    \ = type(self)()\n            parent = p\n            p = p.dic[c]\n         \
    \   p.parent = parent\n            p.last = c\n        p.word = True\n    \n \
    \   def find(self, prefix: str) -> 'Trie':\n        node = self\n        for char\
    \ in prefix:\n            if char not in node.dic:\n                return None\n\
    \            node = node.dic[char]\n        return node\n    \n    def search(self,\
    \ word: str) -> bool:\n        node = self.find(word)\n        return node.word\
    \ if node is not None else False\n\n    def bfs(self) -> List['Trie']:\n     \
    \   output = []\n        queue = deque([self])\n        while queue:\n       \
    \     p = queue.popleft()\n            output.append(p)\n            queue.extend(p.dic.values())\n\
    \        return output\n    \n    def prefix(self) -> str:\n        output = []\n\
    \        curr = self\n        while curr.parent is not None:\n            output.append(curr.last)\n\
    \            curr = curr.parent\n        return \"\".join(reversed(output))\n\n\
    class AhoCorasick(Trie):\n    __slots__ = 'failed',\n\n    def __init__(self):\n\
    \        super().__init__()\n        self.failed: 'AhoCorasick' = None\n\n   \
    \ def build_fail(self):\n        arr_bfs = self.bfs()\n        for p in arr_bfs:\n\
    \            curr = p.parent\n            if curr:\n                c = p.last\n\
    \                while curr.failed:\n                    if c in curr.failed.dic:\n\
    \                        p.failed = curr.failed.dic[c]\n                     \
    \   break\n                    curr = curr.failed\n                else:\n   \
    \                 p.failed = self\n        self.failed = self\n        return\
    \ arr_bfs\n\n    def count_freq(self, text: str) -> dict[str, int]:\n        arr_bfs\
    \ = self.build_fail()\n        p = self\n        for c in text:\n            while\
    \ p != self and c not in p.dic:\n                p = p.failed\n            p =\
    \ p.dic.get(c, self)\n            p.count += 1\n\n        output = {}\n      \
    \  for i in range(len(arr_bfs) - 1, 0, -1):\n            p = arr_bfs[i]\n    \
    \        p.failed.count += p.count\n            if p.word:\n                output[p.prefix()]\
    \ = p.count\n        return output\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc362/tasks/abc362_g\n\
    \ndef main():\n    S = read(str)\n    Q = read(int)\n    ac = AhoCorasick()\n\
    \    queries = []\n    for _ in range(Q):\n        T = input()\n        ac.add(T)\n\
    \        queries.append(T)\n\n    freq_dict = ac.count_freq(S)\n    for query\
    \ in queries:\n        write(freq_dict.get(query, 0))\n\nfrom cp_library.io.read_fn\
    \ import read\nfrom cp_library.io.write_fn import write\nfrom cp_library.ds.ahocorasick_cls\
    \ import AhoCorasick\n\nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/ds/ahocorasick_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/ds/trie_cls.py
  isVerificationFile: true
  path: test/atcoder/abc/abc362_q_count_substring_query_ahocorasick.test.py
  requiredBy: []
  timestamp: '2024-12-30 17:25:46+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc/abc362_q_count_substring_query_ahocorasick.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc/abc362_q_count_substring_query_ahocorasick.test.py
- /verify/test/atcoder/abc/abc362_q_count_substring_query_ahocorasick.test.py.html
title: test/atcoder/abc/abc362_q_count_substring_query_ahocorasick.test.py
---
