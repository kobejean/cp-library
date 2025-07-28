---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heap_proto.py
    title: cp_library/ds/heap/heap_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/max_k_heap_cls.py
    title: cp_library/ds/heap/max_k_heap_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/min_k_heap_cls.py
    title: cp_library/ds/heap/min_k_heap_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc249_f_max_k_heap.test.py
    title: test/atcoder/abc/abc249_f_max_k_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc249_f_min_k_heap.test.py
    title: test/atcoder/abc/abc249_f_min_k_heap.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from typing import Union\nimport typing\nfrom numbers import Number\nfrom types\
    \ import GenericAlias \nfrom typing import Callable, Collection\n\n\nclass IOBase:\n\
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
    \ item): return GenericAlias(cls, item)\nfrom typing import TypeVar\n_S = TypeVar('S');\
    \ _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    \n\nfrom typing import Generic\n\nclass HeapProtocol(Generic[_T]):\n    def peek(heap)\
    \ -> _T: return heap.data[0]\n    def pop(heap) -> _T: ...\n    def push(heap,\
    \ item: _T): ...\n    def pushpop(heap, item: _T) -> _T: ...\n    def replace(heap,\
    \ item: _T) -> _T: ...\n    def __contains__(heap, item: _T): return item in heap.data\n\
    \    def __len__(heap): return len(heap.data)\n    def clear(heap): heap.data.clear()\n\
    \nclass KHeapMixin(HeapProtocol[_T], Parsable):\n    '''KHeapMixin[K: int, T:\
    \ type, N: Union[int,None]]'''\n    def __init__(heap, K: int): heap.K = K\n \
    \   def added(heap, item: _T): ...\n    def removed(heap, item: _T): ...\n   \
    \ def pop(heap): item = super().pop(); heap.removed(item); return item\n    def\
    \ push(heap, item: _T):\n        if len(heap) < heap._K: heap.added(item); super().push(item)\n\
    \        elif heap._K: heap.pushpop(item)\n    def pushpop(heap, item: _T):\n\
    \        if item != (remove := super().pushpop(item)): heap.removed(remove); heap.added(item);\
    \ return remove\n        else: return item\n    def replace(heap, item: _T): remove\
    \ = super().replace(item); heap.removed(remove); heap.added(item); return remove\n\
    \    @property\n    def K(heap): return heap._K\n    @K.setter\n    def K(heap,\
    \ K):\n        heap._K = K\n        if K is not None:\n            while len(heap)\
    \ > K: heap.pop()\n    @classmethod\n    def compile(cls, K: int, T: type, N:\
    \ Union[int,None] = None):\n        elm = Parser.compile(T)\n        if N is None:\n\
    \            def parse(io: IOBase): return cls(K, (elm(io) for _ in io.wait()))\n\
    \        else:\n            def parse(io: IOBase): return cls(K, (elm(io) for\
    \ _ in range(N)))\n        return parse\n"
  code: "import cp_library.__header__\nfrom typing import Union\nfrom cp_library.io.parser_cls\
    \ import Parser, Parsable, IOBase\nfrom cp_library.misc.typing import _T\nimport\
    \ cp_library.ds.__header__\nimport cp_library.ds.heap.__header__\nfrom cp_library.ds.heap.heap_proto\
    \ import HeapProtocol\n\nclass KHeapMixin(HeapProtocol[_T], Parsable):\n    '''KHeapMixin[K:\
    \ int, T: type, N: Union[int,None]]'''\n    def __init__(heap, K: int): heap.K\
    \ = K\n    def added(heap, item: _T): ...\n    def removed(heap, item: _T): ...\n\
    \    def pop(heap): item = super().pop(); heap.removed(item); return item\n  \
    \  def push(heap, item: _T):\n        if len(heap) < heap._K: heap.added(item);\
    \ super().push(item)\n        elif heap._K: heap.pushpop(item)\n    def pushpop(heap,\
    \ item: _T):\n        if item != (remove := super().pushpop(item)): heap.removed(remove);\
    \ heap.added(item); return remove\n        else: return item\n    def replace(heap,\
    \ item: _T): remove = super().replace(item); heap.removed(remove); heap.added(item);\
    \ return remove\n    @property\n    def K(heap): return heap._K\n    @K.setter\n\
    \    def K(heap, K):\n        heap._K = K\n        if K is not None:\n       \
    \     while len(heap) > K: heap.pop()\n    @classmethod\n    def compile(cls,\
    \ K: int, T: type, N: Union[int,None] = None):\n        elm = Parser.compile(T)\n\
    \        if N is None:\n            def parse(io: IOBase): return cls(K, (elm(io)\
    \ for _ in io.wait()))\n        else:\n            def parse(io: IOBase): return\
    \ cls(K, (elm(io) for _ in range(N)))\n        return parse\n"
  dependsOn:
  - cp_library/io/parser_cls.py
  - cp_library/ds/heap/heap_proto.py
  - cp_library/io/io_base_cls.py
  isVerificationFile: false
  path: cp_library/ds/heap/k_heap_mixin.py
  requiredBy:
  - cp_library/ds/heap/max_k_heap_cls.py
  - cp_library/ds/heap/min_k_heap_cls.py
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc249_f_min_k_heap.test.py
  - test/atcoder/abc/abc249_f_max_k_heap.test.py
documentation_of: cp_library/ds/heap/k_heap_mixin.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/k_heap_mixin.py
- /library/cp_library/ds/heap/k_heap_mixin.py.html
title: cp_library/ds/heap/k_heap_mixin.py
---
