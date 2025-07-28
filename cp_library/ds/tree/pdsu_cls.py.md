---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    import operator\nimport typing\nfrom numbers import Number\nfrom types import\
    \ GenericAlias \nfrom typing import Callable, Collection\n\n\nclass IOBase:\n\
    \    @property\n    def char(io) -> bool: ...\n    @property\n    def writable(io)\
    \ -> bool: ...\n    def __next__(io) -> str: ...\n    def write(io, s: str) ->\
    \ None: ...\n    def readline(io) -> str: ...\n    def readtoken(io) -> str: ...\n\
    \    def readtokens(io) -> list[str]: ...\n    def readints(io) -> list[int]:\
    \ ...\n    def readdigits(io) -> list[int]: ...\n    def readnums(io) -> list[int]:\
    \ ...\n    def readchar(io) -> str: ...\n    def readchars(io) -> str: ...\n \
    \   def readinto(io, lst: list[str]) -> list[str]: ...\n    def readcharsinto(io,\
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
    \        else:\n            raise NotImplementedError()\nclass Parsable:\n   \
    \ @classmethod\n    def compile(cls):\n        def parser(io: IOBase): return\
    \ cls(next(io))\n        return parser\n    @classmethod\n    def __class_getitem__(cls,\
    \ item): return GenericAlias(cls, item)\n\n\n\nclass PDSU(Parsable):\n    '''PDSU[N:\
    \ int, M: int, op=operator.sub, inv=operator.neg, e=0, shift=-1]'''\n\n    def\
    \ __init__(self, op, inv, e, v) -> None:\n        n = v if isinstance(v, int)\
    \ else len(v)\n        self.n = n\n        self.par = [-1] * n\n        self.op\
    \ = op\n        self.inv = inv\n        self.e = e\n        self.pot = [e] * n\
    \ if isinstance(v, int) else v\n        self.valid = [True] * n\n\n    def root(self,\
    \ x: int) -> int:\n        assert 0 <= x < self.n\n        path = []\n       \
    \ while self.par[x] >= 0:\n            path.append(x)\n            x = self.par[x]\n\
    \        for y in reversed(path):\n            self.pot[y] = self.op(self.pot[y],\
    \ self.pot[self.par[y]])\n            self.par[y] = x\n        return x\n    \n\
    \    def consistent(self, x: int, y: int, w) -> bool:\n        rx = self.root(x)\n\
    \        ry = self.root(y)\n        if rx == ry:\n            return self.op(self.pot[x],\
    \ self.inv(self.pot[y])) == w\n        return True\n\n    def merge(self, x: int,\
    \ y: int, w) -> tuple[int, int]:\n        assert 0 <= x < self.n\n        assert\
    \ 0 <= y < self.n\n        rx = self.root(x)\n        ry = self.root(y)\n    \
    \    if rx != ry:\n            par = self.par\n            if par[rx] < par[ry]:\n\
    \                x,y,w,rx,ry = y,x,self.inv(w),ry,rx\n                \n     \
    \       par[ry] += par[rx]\n            par[rx] = ry\n            self.pot[rx]\
    \ = self.op(\n                self.op(self.inv(self.pot[x]), w), self.pot[y]\n\
    \            )\n        else:\n            self.valid[rx] &= self.consistent(x,\
    \ y, w)\n        return ry, rx\n\n    def same(self, x: int, y: int) -> bool:\n\
    \        assert 0 <= x < self.n\n        assert 0 <= y < self.n\n        return\
    \ self.root(x) == self.root(y)\n    \n    def size(self, x: int) -> int:\n   \
    \     assert 0 <= x < self.n\n        return -self.par[self.root(x)]\n    \n \
    \   def groups(self):\n        root_buf = [self.root(i) for i in range(self.n)]\n\
    \n        result = [[] for _ in range(self.n)]\n        for i in range(self.n):\n\
    \            result[root_buf[i]].append(i)\n\n        return list(filter(lambda\
    \ r: r, result))\n\n    def diff(self, x: int, y: int):\n        assert self.same(x,\
    \ y)\n        return self.op(self.pot[x], self.inv(self.pot[y]))\n\n    @classmethod\n\
    \    def compile(cls, N: int, M: int, op=operator.sub, inv=operator.neg, e=0,\
    \ shift=-1):\n        def parse(io: IOBase):\n            pdsu = cls(op, inv,\
    \ e, N)\n            for _ in range(M):\n                u, v, w = io.readints()\n\
    \                pdsu.merge(u+shift, v+shift, w)\n            return pdsu\n  \
    \      return parse\n"
  code: "import cp_library.__header__\nimport operator\nfrom cp_library.io.parser_cls\
    \ import Parsable, IOBase\nimport cp_library.ds.__header__\nimport cp_library.ds.tree.__header__\n\
    \nclass PDSU(Parsable):\n    '''PDSU[N: int, M: int, op=operator.sub, inv=operator.neg,\
    \ e=0, shift=-1]'''\n\n    def __init__(self, op, inv, e, v) -> None:\n      \
    \  n = v if isinstance(v, int) else len(v)\n        self.n = n\n        self.par\
    \ = [-1] * n\n        self.op = op\n        self.inv = inv\n        self.e = e\n\
    \        self.pot = [e] * n if isinstance(v, int) else v\n        self.valid =\
    \ [True] * n\n\n    def root(self, x: int) -> int:\n        assert 0 <= x < self.n\n\
    \        path = []\n        while self.par[x] >= 0:\n            path.append(x)\n\
    \            x = self.par[x]\n        for y in reversed(path):\n            self.pot[y]\
    \ = self.op(self.pot[y], self.pot[self.par[y]])\n            self.par[y] = x\n\
    \        return x\n    \n    def consistent(self, x: int, y: int, w) -> bool:\n\
    \        rx = self.root(x)\n        ry = self.root(y)\n        if rx == ry:\n\
    \            return self.op(self.pot[x], self.inv(self.pot[y])) == w\n       \
    \ return True\n\n    def merge(self, x: int, y: int, w) -> tuple[int, int]:\n\
    \        assert 0 <= x < self.n\n        assert 0 <= y < self.n\n        rx =\
    \ self.root(x)\n        ry = self.root(y)\n        if rx != ry:\n            par\
    \ = self.par\n            if par[rx] < par[ry]:\n                x,y,w,rx,ry =\
    \ y,x,self.inv(w),ry,rx\n                \n            par[ry] += par[rx]\n  \
    \          par[rx] = ry\n            self.pot[rx] = self.op(\n               \
    \ self.op(self.inv(self.pot[x]), w), self.pot[y]\n            )\n        else:\n\
    \            self.valid[rx] &= self.consistent(x, y, w)\n        return ry, rx\n\
    \n    def same(self, x: int, y: int) -> bool:\n        assert 0 <= x < self.n\n\
    \        assert 0 <= y < self.n\n        return self.root(x) == self.root(y)\n\
    \    \n    def size(self, x: int) -> int:\n        assert 0 <= x < self.n\n  \
    \      return -self.par[self.root(x)]\n    \n    def groups(self):\n        root_buf\
    \ = [self.root(i) for i in range(self.n)]\n\n        result = [[] for _ in range(self.n)]\n\
    \        for i in range(self.n):\n            result[root_buf[i]].append(i)\n\n\
    \        return list(filter(lambda r: r, result))\n\n    def diff(self, x: int,\
    \ y: int):\n        assert self.same(x, y)\n        return self.op(self.pot[x],\
    \ self.inv(self.pot[y]))\n\n    @classmethod\n    def compile(cls, N: int, M:\
    \ int, op=operator.sub, inv=operator.neg, e=0, shift=-1):\n        def parse(io:\
    \ IOBase):\n            pdsu = cls(op, inv, e, N)\n            for _ in range(M):\n\
    \                u, v, w = io.readints()\n                pdsu.merge(u+shift,\
    \ v+shift, w)\n            return pdsu\n        return parse"
  dependsOn:
  - cp_library/io/parser_cls.py
  - cp_library/io/io_base_cls.py
  isVerificationFile: false
  path: cp_library/ds/tree/pdsu_cls.py
  requiredBy: []
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/tree/pdsu_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/pdsu_cls.py
- /library/cp_library/ds/tree/pdsu_cls.py.html
title: cp_library/ds/tree/pdsu_cls.py
---
