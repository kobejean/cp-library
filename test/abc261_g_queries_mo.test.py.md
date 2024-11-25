---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/queries_cls.py
    title: cp_library/ds/queries_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
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
    \n\ndef main():\n    N, Q = read()\n    A = read()\n    queries = read(QueriesMoOps[Q,\
    \ N])\n    \n    # State for counting triples\n    cnt = [0]*200001        \n\
    \    triples = 0           \n    ans = [0]*Q\n    \n    for op in queries:\n \
    \       match op:\n            case (MoOp.ADD_RIGHT | MoOp.ADD_LEFT, start, stop,\
    \ step):\n                for i in range(start, stop, step):\n               \
    \     v = A[i]\n                    c = cnt[v] \n                    triples +=\
    \ c*(c-1)  \n                    cnt[v] += 1   \n            case (MoOp.REMOVE_RIGHT\
    \ | MoOp.REMOVE_LEFT, start, stop, step):\n                for i in range(start,\
    \ stop, step):\n                    v = A[i]\n                    cnt[v] -= 1\
    \       \n                    c = cnt[v]      \n                    triples -=\
    \ c*(c-1)    \n            case (MoOp.ANSWER, i, _, _):\n                ans[i]\
    \ = triples >> 1\n    \n    print(*ans, sep='\\n')\n\nfrom enum import IntEnum,\
    \ auto\nfrom itertools import chain, groupby\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\nfrom io import TextIOBase\n\n\nimport sys\nimport typing\n\
    from collections import deque\nfrom numbers import Number\nfrom types import GenericAlias\
    \ \nfrom typing import Callable, Collection, Iterator, TypeAlias, TypeVar\n\n\
    class TokenStream(Iterator):\n    def __init__(self, stream: TextIOBase = sys.stdin):\n\
    \        self.queue = deque()\n        self.stream = stream\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return sys.stdin.readline().split()\n\n    def n_uints(self,\
    \ n: int, shift = 0, max_digits: int = 20):\n        # sync buffers\n        tokens:\
    \ list[str] = []\n        while (lim := sys.stdin.buffer.tell() - sys.stdin.tell())\
    \ and len(tokens) < n:\n            residual_str: str = sys.stdin.readline(lim)\n\
    \            tokens.extend(residual_str.split())\n        \n        result = [0]\
    \ * n\n        pos = 0\n        \n        # Process residual string and check\
    \ for partial token\n        partial = None\n        if tokens:\n            if\
    \ not residual_str[-1].isspace():\n                partial = tokens.pop()\n  \
    \          for pos, token in enumerate(tokens):\n                result[pos] =\
    \ int(token)+shift\n            pos += 1\n        # Process remaining data token\
    \ by token\n        stdin_buffer = sys.stdin.buffer\n        num = int(partial)\
    \ if partial else 0\n        have_digit = partial is not None\n\n        original_chunk_size\
    \ = sys.stdin._CHUNK_SIZE\n        sys.stdin._CHUNK_SIZE = max(original_chunk_size,\
    \ max_digits * (n - pos))\n        \n        while pos < n:\n            byte\
    \ = stdin_buffer.read(1)\n\n            match byte[0]:\n                case 10\
    \ | 32:\n                    if have_digit:\n                        result[pos]\
    \ = num+shift\n                        pos += 1\n                        num =\
    \ 0\n                        have_digit = False\n                case char:  #\
    \ digit\n                    num = (num * 10) + (char - 48)\n                \
    \    have_digit = True\n\n        if have_digit:\n            result[pos] = num+shift\n\
    \            pos += 1\n\n        sys.stdin._CHUNK_SIZE = original_chunk_size \n\
    \        if pos < n:\n            raise EOFError(f\"Only found {pos} numbers,\
    \ expected {n}\")\n            \n        return result\n    \n    def n_ints(self,\
    \ n: int, shift = 0, max_digits: int = 20):\n        # sync buffers\n        tokens:\
    \ list[str] = []\n        while (lim := sys.stdin.buffer.tell() - sys.stdin.tell())\
    \ and len(tokens) < n:\n            residual_str: str = sys.stdin.readline(lim)\n\
    \            tokens.extend(residual_str.split())\n        \n        result = [0]\
    \ * n\n        pos = 0\n        \n        # Process residual string and check\
    \ for partial token\n        partial = None\n        if tokens:\n            if\
    \ not residual_str[-1].isspace():\n                partial = tokens.pop()\n  \
    \          for pos, token in enumerate(tokens):\n                result[pos] =\
    \ int(token)+shift\n            pos += 1\n        # Process remaining data token\
    \ by token\n        stdin_buffer = sys.stdin.buffer\n        num = abs(int(partial))\
    \ if partial else 0\n        is_negative = partial and partial.startswith('-')\n\
    \        have_digit = partial is not None\n\n        original_chunk_size = sys.stdin._CHUNK_SIZE\n\
    \        sys.stdin._CHUNK_SIZE = max(original_chunk_size, max_digits * (n - pos))\n\
    \        \n        while pos < n:\n            byte = stdin_buffer.read(1)\n\n\
    \            match byte[0]:\n                case 10 | 32:\n                 \
    \   if have_digit:\n                        result[pos] = -num+shift if is_negative\
    \ else num+shift\n                        pos += 1\n                        num\
    \ = 0\n                        is_negative = False\n                        have_digit\
    \ = False\n                case 45:  # minus sign\n                    is_negative\
    \ = True\n                case char:  # digit\n                    num = (num\
    \ * 10) + (char - 48)\n                    have_digit = True\n\n        if have_digit:\n\
    \            result[pos] = -num+shift if is_negative else num+shift\n        \
    \    pos += 1\n\n        sys.stdin._CHUNK_SIZE = original_chunk_size \n      \
    \  if pos < n:\n            raise EOFError(f\"Only found {pos} numbers, expected\
    \ {n}\")\n            \n        return result\n\nclass CharStream(TokenStream):\n\
    \    def line(self):\n        assert not self.queue\n        return next(self.stream).rstrip()\n\
    \        \nT = TypeVar('T')\nParseFn: TypeAlias = Callable[[TokenStream],T]\n\
    class Parser:\n    def __init__(self, spec: type[T]|T):\n        self.parse =\
    \ Parser.compile(spec)\n\n    def __call__(self, ts: TokenStream) -> T:\n    \
    \    return self.parse(ts)\n    \n    @staticmethod\n    def compile_type(cls:\
    \ type[T], args = ()) -> T:\n        if issubclass(cls, Parsable):\n         \
    \   return cls.compile(*args)\n        elif issubclass(cls, (Number, str)):\n\
    \            def parse(ts: TokenStream):\n                return cls(next(ts))\
    \              \n            return parse\n        elif issubclass(cls, tuple):\n\
    \            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection):\n            return Parser.compile_collection(cls, args)\n    \
    \    elif callable(cls):\n            def parse(ts: TokenStream):\n          \
    \      return cls(next(ts))              \n            return parse\n        else:\n\
    \            raise NotImplementedError()\n    \n    @staticmethod\n    def compile(spec:\
    \ type[T]|T=int) -> ParseFn[T]:\n        if isinstance(spec, (type, GenericAlias)):\n\
    \            cls = typing.get_origin(spec) or spec\n            args = typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(ts: TokenStream):\n                return cls(next(ts)) + offset\n\
    \            return parse\n        elif isinstance(args := spec, tuple):     \
    \ \n            return Parser.compile_tuple(type(spec), args)\n        elif isinstance(args\
    \ := spec, Collection):  \n            return Parser.compile_collection(type(spec),\
    \ args)\n        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile_line(cls: T, spec=int) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in ts.wait())\n\
    \        return parse\n    \n    # @staticmethod\n    # def compile_n_ints(cls:\
    \ T, N, shift = int) -> ParseFn[T]:\n    #     shift = shift if isinstance(shift,\
    \ int) else 0\n    #     def parse(ts: TokenStream):\n    #         return cls(ts.n_ints(N,\
    \ shift))\n    #     return parse\n\n    @staticmethod\n    def compile_repeat(cls:\
    \ T, spec, N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream):\n            return cls(fn(ts) for _ in range(N))\n        return\
    \ parse\n\n    @staticmethod\n    def compile_children(cls: T, specs) -> ParseFn[T]:\n\
    \        fns = tuple(Parser.compile(spec) for spec in specs)\n        def parse(ts:\
    \ TokenStream):\n            return cls(fn(ts) for fn in fns)  \n        return\
    \ parse\n\n    @staticmethod\n    def compile_tuple(cls: type[T], specs) -> ParseFn[T]:\n\
    \        match specs:\n            case [spec, end] if end is ...:\n         \
    \       return Parser.compile_line(cls, spec)\n            case specs:   \n  \
    \              return Parser.compile_children(cls, specs)\n    \n    @staticmethod\n\
    \    def compile_collection(cls, specs):\n        match specs:\n            case\
    \ [ ] | [_] | set():\n                return Parser.compile_line(cls, *specs)\n\
    \            case [spec, int() as N]:\n                # if issubclass(spec, int)\
    \ or isinstance(spec, int):\n                #     return Parser.compile_n_ints(cls,\
    \ N, spec)\n                return Parser.compile_repeat(cls, spec, N)\n     \
    \       case _:\n                raise NotImplementedError()\n\n        \nclass\
    \ Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(ts: TokenStream):\n\
    \            return cls(next(ts))\n        return parser\nfrom typing import Iterable,\
    \ Sequence\n\nclass Queries(list, Parsable):\n    def __init__(self, data: Iterable\
    \ = []):\n        super().__init__((i,*query) for i,query in enumerate(data))\n\
    \n    def append(self, query) -> None:\n        return super().append((len(self),\
    \ *query))\n\n    @classmethod\n    def compile(cls, N: int, T: type = tuple[int,\
    \ int]):\n        query = Parser.compile(T)\n        def parse(ts: TokenStream):\n\
    \            return cls(query(ts) for _ in range(N))\n        return parse\n\n\
    class QueriesGrouped(Queries):\n    '''QueriesGrouped[Q: int, key = 0, T: type\
    \ = tuple[int, ...]]'''\n    def __init__(self, queries, key = 0):\n        if\
    \ isinstance(key, int):\n            group_idx = key+1\n            def wrap_key(row):\n\
    \                return row[group_idx]\n        else:\n            def wrap_key(row):\n\
    \                _, *query = row\n                return key(query)\n        rows\
    \ = sorted(((i,*query) for i,query in enumerate(queries)), key = wrap_key)\n \
    \       groups = [(k, list(g)) for k, g in groupby(rows, key = wrap_key)]\n  \
    \      groups.sort()\n        self.key = key\n        \n        list.__init__(self,\
    \ groups)\n            \n\n    @classmethod\n    def compile(cls, Q: int, key\
    \ = 0, T: type = tuple[int, ...]):\n        query = Parser.compile(T)\n      \
    \  def parse(ts: TokenStream):\n            return cls((query(ts) for _ in range(Q)),\
    \ key)\n        return parse\n\nclass QueriesRange(Queries):\n    '''QueriesRange[Q:\
    \ int, N: int, key = 0, T: type = tuple[-1, int]]'''\n    def __init__(self, queries,\
    \ N: int, key = 0):\n        if isinstance(key, int):\n            group_idx =\
    \ key+1\n            def wrap_key(row):\n                return row[group_idx]\n\
    \        else:\n            def wrap_key(row):\n                _, *query = row\n\
    \                return key(query)\n        rows = list((i,*query) for i,query\
    \ in enumerate(queries))\n        \n        groups = [(k,[]) for k in range(N)]\n\
    \        for k, group in groupby(rows, key = wrap_key):\n            groups[k][1].extend(group)\n\
    \        self.key = key\n        \n        list.__init__(self, groups)\n\n   \
    \ @classmethod\n    def compile(cls, Q: int, N: int, key = 0, T: type = tuple[-1,\
    \ int]):\n        query = Parser.compile(T)\n        def parse(ts: TokenStream):\n\
    \            return cls((query(ts) for _ in range(Q)), N, key)\n        return\
    \ parse\n\n\nclass MoOp(IntEnum):\n    ADD_LEFT = auto()\n    ADD_RIGHT = auto()\n\
    \    REMOVE_LEFT = auto()\n    REMOVE_RIGHT = auto()\n    ANSWER = auto()\n  \
    \  \nfrom math import isqrt\n\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n\
    \    def newlist_hint(hint):\n        return []\n    \ndef elist(est_len: int)\
    \ -> list:\n    return newlist_hint(est_len)\n\nclass QueriesMoOps(list[tuple],Parsable):\n\
    \    \"\"\"\n    QueriesMoOps[Q: int, N: int, T: type = tuple[int, int]]\n   \
    \ Orders queries using Mo's algorithm and generates a sequence of operations to\
    \ process them efficiently.\n    Each operation is either moving pointers or answering\
    \ a query.\n    \n    Uses half-interval convention: [left, right)\n    Block\
    \ size is automatically set to sqrt(N) for optimal complexity.\n    \"\"\"\n \
    \   \n    def encode(self, i, l, r):\n        return (((r << self.nbits) + l)\
    \ << self.qbits) + i\n    \n    def decode(self, bits):\n        r = bits >> self.qbits\
    \ >> self.nbits\n        l = bits >> self.qbits & self.nmask\n        i = bits\
    \ & self.qmask\n        return i, l, r\n\n    def __init__(self, queries: list[tuple[int,\
    \ int]], N: int):\n        Q = len(queries)\n        self.qbits = Q.bit_length()\n\
    \        self.nbits = N.bit_length()\n        self.qmask = (1 << self.qbits)-1\n\
    \        self.nmask = (1 << self.nbits)-1\n\n        # Initialize with original\
    \ queries and their indices\n        B = isqrt(N)\n        K = (N+B-1)//B\n  \
    \      buckets = [elist(64) for _ in range(K)]\n        for i, (l, r) in enumerate(queries):\n\
    \            buckets[l//B].append(self.encode(i, l, r))\n        for i, bucket\
    \ in enumerate(buckets):\n            bucket.sort(reverse=i&1)\n        \n   \
    \     \n        # Generate sequence of operations\n        ops = elist(3*Q)\n\n\
    \        nl = nr = 0\n        \n        for bucket in buckets:\n            for\
    \ code in bucket:\n                i, l, r = self.decode(code)\n             \
    \   if l < nl:\n                    ops.append((MoOp.ADD_LEFT, nl-1, l-1, -1))\n\
    \                elif l > nl:\n                    ops.append((MoOp.REMOVE_LEFT,\
    \ nl, l, 1))\n\n                if r > nr:\n                    ops.append((MoOp.ADD_RIGHT,\
    \ nr, r, 1))\n                elif r < nr:\n                    ops.append((MoOp.REMOVE_RIGHT,\
    \ nr-1, r-1, -1))\n                \n                ops.append((MoOp.ANSWER,\
    \ i, l, r))\n                \n                nl, nr = l, r\n        super().__init__(ops)\n\
    \        self.queries = queries\n\n\n    @classmethod\n    def compile(cls, Q:\
    \ int, N: int, T: type = tuple[-1, int]):\n        query = Parser.compile(T)\n\
    \        def parse(ts: TokenStream):\n            return cls([query(ts) for _\
    \ in range(Q)], N)\n        return parse\n\nfrom typing import Type, TypeVar,\
    \ overload\n\nT = TypeVar('T')\n@overload\ndef read() -> list[int]: ...\n@overload\n\
    def read(spec: int|None) -> list[int]: ...\n@overload\ndef read(spec: Type[T]|T,\
    \ char=False) -> T: ...\ndef read(spec: Type[T]|T=None, char=False):\n    match\
    \ spec, char:\n        case None, False:\n            return list(map(int, input().split()))\n\
    \        case int(offset), False:\n            return [int(s)+offset for s in\
    \ input().split()]\n        case _, _:\n            if char:\n               \
    \ stream = CharStream()\n            else:\n                stream = TokenStream()\n\
    \            parser: T = Parser.compile(spec)\n            return parser(stream)\n\
    \nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc293/tasks/abc293_g\n\
    \n\ndef main():\n    N, Q = read()\n    A = read()\n    queries = read(QueriesMoOps[Q,\
    \ N])\n    \n    # State for counting triples\n    cnt = [0]*200001        \n\
    \    triples = 0           \n    ans = [0]*Q\n    \n    for op in queries:\n \
    \       match op:\n            case (MoOp.ADD_RIGHT | MoOp.ADD_LEFT, start, stop,\
    \ step):\n                for i in range(start, stop, step):\n               \
    \     v = A[i]\n                    c = cnt[v] \n                    triples +=\
    \ c*(c-1)  \n                    cnt[v] += 1   \n            case (MoOp.REMOVE_RIGHT\
    \ | MoOp.REMOVE_LEFT, start, stop, step):\n                for i in range(start,\
    \ stop, step):\n                    v = A[i]\n                    cnt[v] -= 1\
    \       \n                    c = cnt[v]      \n                    triples -=\
    \ c*(c-1)    \n            case (MoOp.ANSWER, i, _, _):\n                ans[i]\
    \ = triples >> 1\n    \n    print(*ans, sep='\\n')\n\nfrom cp_library.ds.queries_cls\
    \ import QueriesMoOps, MoOp\nfrom cp_library.io.read_specs_fn import read\n\n\
    if __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/ds/queries_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/ds/elist_fn.py
  isVerificationFile: true
  path: test/abc261_g_queries_mo.test.py
  requiredBy: []
  timestamp: '2024-11-25 18:54:05+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc261_g_queries_mo.test.py
layout: document
redirect_from:
- /verify/test/abc261_g_queries_mo.test.py
- /verify/test/abc261_g_queries_mo.test.py.html
title: test/abc261_g_queries_mo.test.py
---
