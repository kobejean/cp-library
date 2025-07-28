---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/fast_heapq.py
    title: cp_library/ds/heap/fast_heapq.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heap_proto.py
    title: cp_library/ds/heap/heap_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/k_heap_mixin.py
    title: cp_library/ds/heap/k_heap_mixin.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/max_heap_cls.py
    title: cp_library/ds/heap/max_heap_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc249_f_min_k_heap.test.py
    title: test/atcoder/abc/abc249_f_min_k_heap.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\nfrom typing import Iterable\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\nfrom typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T');\
    \ _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3');\
    \ _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\ndef heappush(heap:\
    \ list, item):\n    heap.append(item)\n    heapsiftdown(heap, 0, len(heap)-1)\n\
    \ndef heappop(heap: list):\n    item = heap.pop()\n    if heap: item, heap[0]\
    \ = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapreplace(heap:\
    \ list, item):\n    item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return\
    \ item\n\ndef heappushpop(heap: list, item):\n    if heap and heap[0] < item:\
    \ item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapify(x:\
    \ list):\n    for i in reversed(range(len(x)//2)): heapsiftup(x, i)\n\ndef heapsiftdown(heap:\
    \ list, root: int, pos: int):\n    item = heap[pos]\n    while root < pos and\
    \ item < heap[p := (pos-1)>>1]: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\
    \ndef heapsiftup(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and heap[c] < item: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\ndef heappop_max(heap: list):\n    item\
    \ = heap.pop()\n    if heap: item, heap[0] = heap[0], item; heapsiftup_max(heap,\
    \ 0)\n    return item\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heapify_max(x:\
    \ list):\n    for i in reversed(range(len(x)//2)): heapsiftup_max(x, i)\n\ndef\
    \ heappush_max(heap: list, item):\n    heap.append(item); heapsiftdown_max(heap,\
    \ 0, len(heap)-1)\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heappushpop_max(heap:\
    \ list, item):\n    if heap and heap[0] > item: item, heap[0] = heap[0], item;\
    \ heapsiftup_max(heap, 0)\n    return item\n\ndef heapsiftdown_max(heap: list,\
    \ root: int, pos: int):\n    item = heap[pos]\n    while root < pos and heap[p\
    \ := (pos-1)>>1] < item: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\n\
    def heapsiftup_max(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and item < heap[c := c+(heap[c]<heap[c+1])]: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and item < heap[c]: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\nfrom typing import Generic\n\nclass HeapProtocol(Generic[_T]):\n\
    \    def peek(heap) -> _T: return heap.data[0]\n    def pop(heap) -> _T: ...\n\
    \    def push(heap, item: _T): ...\n    def pushpop(heap, item: _T) -> _T: ...\n\
    \    def replace(heap, item: _T) -> _T: ...\n    def __contains__(heap, item:\
    \ _T): return item in heap.data\n    def __len__(heap): return len(heap.data)\n\
    \    def clear(heap): heap.data.clear()\n\nclass MaxHeap(HeapProtocol[_T]):\n\
    \    def __init__(self, iterable: Iterable[_T] = None): self.data = list(iterable)\
    \ if iterable else []; heapify_max(self.data)\n    def pop(self): return heappop_max(self.data)\n\
    \    def push(self, item: _T): heappush_max(self.data, item)\n    def pushpop(self,\
    \ item: _T): return heappushpop_max(self.data, item)\n    def replace(self, item:\
    \ _T): return heapreplace_max(self.data, item)\nfrom typing import Union\nfrom\
    \ types import GenericAlias\n\n\nclass Parsable:\n    @classmethod\n    def compile(cls):\n\
    \        def parser(io: 'IOBase'): return cls(next(io))\n        return parser\n\
    \    @classmethod\n    def __class_getitem__(cls, item): return GenericAlias(cls,\
    \ item)\n\nclass KHeapMixin(HeapProtocol[_T], Parsable):\n    '''KHeapMixin[K:\
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
    \ cls(K, (elm(io) for _ in range(N)))\n        return parse\n\nclass IOBase:\n\
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
    \ -> None: ...\n    def line(io) -> list[str]: ...\nimport typing\nfrom numbers\
    \ import Number\nfrom typing import Callable, Collection\n\nclass Parser:\n  \
    \  def __init__(self, spec):  self.parse = Parser.compile(spec)\n    def __call__(self,\
    \ io: IOBase): return self.parse(io)\n    @staticmethod\n    def compile_type(cls,\
    \ args = ()):\n        if issubclass(cls, Parsable): return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(io: IOBase):\
    \ return cls(next(io))              \n            return parse\n        elif issubclass(cls,\
    \ tuple): return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection): return Parser.compile_collection(cls, args)\n        elif callable(cls):\n\
    \            def parse(io: IOBase): return cls(next(io))              \n     \
    \       return parse\n        else: raise NotImplementedError()\n    @staticmethod\n\
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
    \        else:\n            raise NotImplementedError()\n\nclass MinKHeap(KHeapMixin[_T],\
    \ MaxHeap[_T]):\n    '''MinKHeap[K: int, T: type, N: Union[int,None]]'''\n   \
    \ def __init__(self, K: int, iterable: Iterable[_T] = None):\n        MaxHeap.__init__(self,\
    \ iterable)\n        KHeapMixin.__init__(self, K)\n"
  code: "import cp_library.ds.heap.__header__\nfrom typing import Iterable\nfrom cp_library.ds.heap.max_heap_cls\
    \ import MaxHeap\nfrom cp_library.ds.heap.k_heap_mixin import KHeapMixin\nfrom\
    \ cp_library.misc.typing import _T\n\nclass MinKHeap(KHeapMixin[_T], MaxHeap[_T]):\n\
    \    '''MinKHeap[K: int, T: type, N: Union[int,None]]'''\n    def __init__(self,\
    \ K: int, iterable: Iterable[_T] = None):\n        MaxHeap.__init__(self, iterable)\n\
    \        KHeapMixin.__init__(self, K)\n"
  dependsOn:
  - cp_library/ds/heap/max_heap_cls.py
  - cp_library/ds/heap/k_heap_mixin.py
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/ds/heap/heap_proto.py
  - cp_library/io/parsable_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/io/parser_cls.py
  isVerificationFile: false
  path: cp_library/ds/heap/min_k_heap_cls.py
  requiredBy: []
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc249_f_min_k_heap.test.py
documentation_of: cp_library/ds/heap/min_k_heap_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/min_k_heap_cls.py
- /library/cp_library/ds/heap/min_k_heap_cls.py.html
title: cp_library/ds/heap/min_k_heap_cls.py
---
