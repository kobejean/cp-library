---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort_groups_fn.py
    title: cp_library/alg/iter/sort_groups_fn.py
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
    PROBLEM: https://atcoder.jp/contests/abc203/tasks/abc203_e
    links:
    - https://atcoder.jp/contests/abc203/tasks/abc203_e
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc203/tasks/abc203_e\n\
    \ndef main():\n    N, M = read(tuple[int, ...])\n    # groups and sorts by x value\n\
    \    XY = read(list[tuple[int, ...], M])\n    XY = sort_groups(XY, 0)\n    \n\
    \    # currently reacable columns\n    S = { N }\n    for _,group in XY:\n   \
    \     add = elist(len(group))\n        for _,y in group:\n            if (y-1)\
    \ in S or (y+1) in S:\n                # we can reach pawn on this column\n  \
    \              add.append(y)\n        for _,y in group:\n            # pawn blocks\
    \ y column\n            S.discard(y)\n            # we'll add it back in the next\
    \ loop if reachable\n        for y in add:\n            S.add(y)\n\n    ans =\
    \ len(S)\n    write(ans)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library \
    \              \n'''\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__\
    \ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n        return []\n\
    elist = newlist_hint\n    \n\n\nfrom typing import Iterable, Type, Union, overload\n\
    import typing\nfrom collections import deque\nfrom numbers import Number\nfrom\
    \ types import GenericAlias \nfrom typing import Callable, Collection, Iterator,\
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
    \ = IOWrapper(sys.stdout)\nfrom typing import TypeVar\n_T = TypeVar('T')\n\nclass\
    \ TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\n    def __init__(self):\n\
    \        self.queue = deque()\n\n    def __next__(self):\n        if not self.queue:\
    \ self.queue.extend(self.line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        return\
    \ TokenStream.stream.readline().split()\n        \nTokenStream.default = TokenStream()\n\
    \nclass CharStream(TokenStream):\n\n    def line(self):\n        return TokenStream.stream.readline().rstrip()\n\
    \nCharStream.default = CharStream()\n\nParseFn = Callable[[TokenStream],_T]\n\
    class Parser:\n    def __init__(self, spec: Union[type[_T],_T]):\n        self.parse\
    \ = Parser.compile(spec)\n\n    def __call__(self, ts: TokenStream) -> _T:\n \
    \       return self.parse(ts)\n    \n    @staticmethod\n    def compile_type(cls:\
    \ type[_T], args = ()) -> _T:\n        if issubclass(cls, Parsable):\n       \
    \     return cls.compile(*args)\n        elif issubclass(cls, (Number, str)):\n\
    \            def parse(ts: TokenStream):\n                return cls(next(ts))\
    \              \n            return parse\n        elif issubclass(cls, tuple):\n\
    \            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection):\n            return Parser.compile_collection(cls, args)\n    \
    \    elif callable(cls):\n            def parse(ts: TokenStream):\n          \
    \      return cls(next(ts))              \n            return parse\n        else:\n\
    \            raise NotImplementedError()\n    \n    @staticmethod\n    def compile(spec:\
    \ Union[type[_T],_T]=int) -> ParseFn[_T]:\n        if isinstance(spec, (type,\
    \ GenericAlias)):\n            cls = typing.get_origin(spec) or spec\n       \
    \     args = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream):\n                return\
    \ cls(next(ts)) + offset\n            return parse\n        elif isinstance(args\
    \ := spec, tuple):      \n            return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection):  \n            return\
    \ Parser.compile_collection(type(spec), args)\n        elif isinstance(fn := spec,\
    \ Callable): \n            def parse(ts: TokenStream):\n                return\
    \ fn(next(ts))\n            return parse\n        else:\n            raise NotImplementedError()\n\
    \n    @staticmethod\n    def compile_line(cls: _T, spec=int) -> ParseFn[_T]:\n\
    \        if spec is int:\n            fn = Parser.compile(spec)\n            def\
    \ parse(ts: TokenStream):\n                return cls((int(token) for token in\
    \ ts.line()))\n            return parse\n        else:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream):\n                return cls((fn(ts) for\
    \ _ in ts.wait()))\n            return parse\n\n    @staticmethod\n    def compile_repeat(cls:\
    \ _T, spec, N) -> ParseFn[_T]:\n        fn = Parser.compile(spec)\n        def\
    \ parse(ts: TokenStream):\n            return cls((fn(ts) for _ in range(N)))\n\
    \        return parse\n\n    @staticmethod\n    def compile_children(cls: _T,\
    \ specs) -> ParseFn[_T]:\n        fns = tuple((Parser.compile(spec) for spec in\
    \ specs))\n        def parse(ts: TokenStream):\n            return cls((fn(ts)\
    \ for fn in fns))  \n        return parse\n            \n    @staticmethod\n \
    \   def compile_tuple(cls: type[_T], specs) -> ParseFn[_T]:\n        if isinstance(specs,\
    \ (tuple,list)) and len(specs) == 2 and specs[1] is ...:\n            return Parser.compile_line(cls,\
    \ specs[0])\n        else:\n            return Parser.compile_children(cls, specs)\n\
    \n    @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 \n\
    \            and isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls,\
    \ specs[0], specs[1])\n        else:\n            raise NotImplementedError()\n\
    \nclass Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(ts:\
    \ TokenStream):\n            return cls(next(ts))\n        return parser\n\n@overload\n\
    def read() -> Iterable[int]: ...\n@overload\ndef read(spec: int) -> list[int]:\
    \ ...\n@overload\ndef read(spec: Union[Type[_T],_T], char=False) -> _T: ...\n\
    def read(spec: Union[Type[_T],_T] = None, char=False):\n    if not char and spec\
    \ is None:\n        line = TokenStream.default.queue or TokenStream.stream.readline().split()\n\
    \        return map(int, line)\n    parser: _T = Parser.compile(spec)\n    return\
    \ parser(CharStream.default if char else TokenStream.default)\n\ndef write(*args,\
    \ **kwargs):\n    \"\"\"Prints the values to a stream, or to stdout_fast by default.\"\
    \"\"\n    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n\
    \    at_start = True\n    for x in args:\n        if not at_start:\n         \
    \   file.write(sep)\n        file.write(str(x))\n        at_start = False\n  \
    \  file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\nfrom itertools import groupby\nfrom operator import itemgetter\n\
    \ndef sort_groups(A, key=0):\n    if isinstance(key,int):\n        key = itemgetter(key)\n\
    \    A.sort(key=key)\n    return sorted((k,list(g)) for k,g in groupby(A, key=key))\n\
    \n    \nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc203/tasks/abc203_e\n\
    \ndef main():\n    N, M = read(tuple[int, ...])\n    # groups and sorts by x value\n\
    \    XY = read(list[tuple[int, ...], M])\n    XY = sort_groups(XY, 0)\n    \n\
    \    # currently reacable columns\n    S = { N }\n    for _,group in XY:\n   \
    \     add = elist(len(group))\n        for _,y in group:\n            if (y-1)\
    \ in S or (y+1) in S:\n                # we can reach pawn on this column\n  \
    \              add.append(y)\n        for _,y in group:\n            # pawn blocks\
    \ y column\n            S.discard(y)\n            # we'll add it back in the next\
    \ loop if reachable\n        for y in add:\n            S.add(y)\n\n    ans =\
    \ len(S)\n    write(ans)\n\nfrom cp_library.ds.elist_fn import elist\nfrom cp_library.io.read_fn\
    \ import read\nfrom cp_library.io.write_fn import write\nfrom cp_library.alg.iter.sort_groups_fn\
    \ import sort_groups\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/ds/elist_fn.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/iter/sort_groups_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/atcoder/abc/abc203_e_sort_groups.test.py
  requiredBy: []
  timestamp: '2025-01-24 05:21:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc/abc203_e_sort_groups.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc/abc203_e_sort_groups.test.py
- /verify/test/atcoder/abc/abc203_e_sort_groups.test.py.html
title: test/atcoder/abc/abc203_e_sort_groups.test.py
---
