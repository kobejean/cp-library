---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_fn.py
    title: argsort
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/isort_parallel_fn.py
    title: cp_library/alg/iter/sort/isort_parallel_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list2_cls.py
    title: cp_library/ds/list/list2_cls.py
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
  - icon: ':heavy_check_mark:'
    path: cp_library/test/unittest_helper.py
    title: cp_library/test/unittest_helper.py
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
    \nimport pytest\nimport random\n\nclass TestList2:\n    def test_initialization(self):\n\
    \        \"\"\"Test basic initialization of list2\"\"\"\n        A1 = [1, 2, 3,\
    \ 4, 5]\n        A2 = ['a', 'b', 'c', 'd', 'e']\n        lst = list2(A1, A2)\n\
    \        \n        assert lst.A1 is A1\n        assert lst.A2 is A2\n        assert\
    \ len(lst) == 5\n\n    def test_len(self):\n        \"\"\"Test __len__ method\"\
    \"\"\n        lst = list2([1, 2, 3], ['a', 'b', 'c'])\n        assert len(lst)\
    \ == 3\n        \n        lst = list2([], [])\n        assert len(lst) == 0\n\
    \        \n        lst = list2(list(range(100)), list(range(100)))\n        assert\
    \ len(lst) == 100\n\n    def test_getitem(self):\n        \"\"\"Test __getitem__\
    \ method\"\"\"\n        lst = list2([10, 20, 30], ['x', 'y', 'z'])\n        \n\
    \        assert lst[0] == (10, 'x')\n        assert lst[1] == (20, 'y')\n    \
    \    assert lst[2] == (30, 'z')\n        \n        # Test negative indexing\n\
    \        assert lst[-1] == (30, 'z')\n        assert lst[-2] == (20, 'y')\n\n\
    \    def test_setitem(self):\n        \"\"\"Test __setitem__ method\"\"\"\n  \
    \      lst = list2([10, 20, 30], ['x', 'y', 'z'])\n        \n        lst[0] =\
    \ (15, 'a')\n        lst[1] = (25, 'b')\n        lst[2] = (35, 'c')\n        \n\
    \        assert lst.A1 == [15, 25, 35]\n        assert lst.A2 == ['a', 'b', 'c']\n\
    \        assert lst[0] == (15, 'a')\n        assert lst[1] == (25, 'b')\n    \
    \    assert lst[2] == (35, 'c')\n\n    def test_contains_not_implemented(self):\n\
    \        \"\"\"Test that __contains__ raises NotImplementedError\"\"\"\n     \
    \   lst = list2([1, 2, 3], ['a', 'b', 'c'])\n        \n        with pytest.raises(NotImplementedError):\n\
    \            (1, 'a') in lst\n\n    def test_index_not_implemented(self):\n  \
    \      \"\"\"Test that index raises NotImplementedError\"\"\"\n        lst = list2([1,\
    \ 2, 3], ['a', 'b', 'c'])\n        \n        with pytest.raises(NotImplementedError):\n\
    \            lst.index((1, 'a'))\n\n    def test_reverse(self):\n        \"\"\"\
    Test reverse method\"\"\"\n        lst = list2([1, 2, 3, 4, 5], ['a', 'b', 'c',\
    \ 'd', 'e'])\n        \n        lst.reverse()\n        \n        assert lst.A1\
    \ == [5, 4, 3, 2, 1]\n        assert lst.A2 == ['e', 'd', 'c', 'b', 'a']\n   \
    \     assert lst[0] == (5, 'e')\n        assert lst[4] == (1, 'a')\n\n    def\
    \ test_sort(self):\n        \"\"\"Test sort method\"\"\"\n        lst = list2([3,\
    \ 1, 4, 1, 5], ['c', 'a', 'd', 'b', 'e'])\n        \n        lst.sort()\n    \
    \    \n        # Should sort by first element\n        assert lst.A1 == [1, 1,\
    \ 3, 4, 5]\n        assert lst.A2 == ['a', 'b', 'c', 'd', 'e']\n        \n   \
    \ def test_sort_reverse(self):\n        \"\"\"Test sort method with reverse=True\"\
    \"\"\n        lst = list2([3, 1, 4, 1, 5], ['c', 'a', 'd', 'b', 'e'])\n      \
    \  \n        lst.sort(reverse=True)\n        \n        # Should sort by first\
    \ element in reverse\n        assert lst.A1 == [5, 4, 3, 1, 1]\n        assert\
    \ lst.A2 == ['e', 'd', 'c', 'a', 'b']\n\n    def test_pop(self):\n        \"\"\
    \"Test pop method\"\"\"\n        lst = list2([1, 2, 3, 4, 5], ['a', 'b', 'c',\
    \ 'd', 'e'])\n        \n        popped = lst.pop()\n        assert popped == (5,\
    \ 'e')\n        assert len(lst) == 4\n        assert lst.A1 == [1, 2, 3, 4]\n\
    \        assert lst.A2 == ['a', 'b', 'c', 'd']\n        \n        popped = lst.pop()\n\
    \        assert popped == (4, 'd')\n        assert len(lst) == 3\n\n    def test_append(self):\n\
    \        \"\"\"Test append method\"\"\"\n        lst = list2([1, 2, 3], ['a',\
    \ 'b', 'c'])\n        \n        lst.append((4, 'd'))\n        assert len(lst)\
    \ == 4\n        assert lst[3] == (4, 'd')\n        assert lst.A1 == [1, 2, 3,\
    \ 4]\n        assert lst.A2 == ['a', 'b', 'c', 'd']\n        \n        lst.append((5,\
    \ 'e'))\n        assert len(lst) == 5\n        assert lst[4] == (5, 'e')\n\n \
    \   def test_empty_list(self):\n        \"\"\"Test operations on empty list2\"\
    \"\"\n        lst = list2([], [])\n        \n        assert len(lst) == 0\n  \
    \      \n        with pytest.raises(IndexError):\n            lst.pop()\n    \
    \    \n        lst.append((1, 'a'))\n        assert len(lst) == 1\n        assert\
    \ lst[0] == (1, 'a')\n\n    def test_with_different_types(self):\n        \"\"\
    \"Test list2 with different data types\"\"\"\n        # Integer and float\n  \
    \      lst = list2([1, 2, 3], [1.1, 2.2, 3.3])\n        assert lst[0] == (1, 1.1)\n\
    \        assert lst[1] == (2, 2.2)\n        \n        # String and boolean\n \
    \       lst = list2(['a', 'b', 'c'], [True, False, True])\n        assert lst[0]\
    \ == ('a', True)\n        assert lst[1] == ('b', False)\n        \n        # Mixed\
    \ types\n        lst = list2([1, 'two', 3.0], [None, [1, 2], {'key': 'value'}])\n\
    \        assert lst[0] == (1, None)\n        assert lst[1] == ('two', [1, 2])\n\
    \        assert lst[2] == (3.0, {'key': 'value'})\n\n    def test_large_data_operations(self):\n\
    \        \"\"\"Test operations on larger datasets\"\"\"\n        n = 1000\n  \
    \      A1 = list(range(n))\n        A2 = list(range(n, 2*n))\n        lst = list2(A1,\
    \ A2)\n        \n        assert len(lst) == n\n        assert lst[0] == (0, n)\n\
    \        assert lst[n-1] == (n-1, 2*n-1)\n        \n        # Test pop on large\
    \ dataset\n        popped = lst.pop()\n        assert popped == (n-1, 2*n-1)\n\
    \        assert len(lst) == n-1\n        \n        # Test append on large dataset\n\
    \        lst.append((n, 2*n))\n        assert len(lst) == n\n        assert lst[n-1]\
    \ == (n, 2*n)\n\n    def test_sort_stability(self):\n        \"\"\"Test that sort\
    \ maintains parallel structure\"\"\"\n        # Create data where first elements\
    \ have duplicates\n        lst = list2([3, 1, 2, 1, 3], ['a', 'b', 'c', 'd', 'e'])\n\
    \        \n        lst.sort()\n        \n        # After sorting by first element,\
    \ check parallel structure\n        assert lst[0][0] == 1\n        assert lst[1][0]\
    \ == 1\n        assert lst[2][0] == 2\n        assert lst[3][0] == 3\n       \
    \ assert lst[4][0] == 3\n        \n        # The corresponding second elements\
    \ should be maintained\n        assert lst[0][1] == 'b'\n        assert lst[1][1]\
    \ == 'd'\n        assert lst[2][1] == 'c'\n        assert lst[3][1] == 'a'\n \
    \       assert lst[4][1] == 'e'\n\n    def test_random_operations(self):\n   \
    \     \"\"\"Test random operations for robustness\"\"\"\n        random.seed(42)\n\
    \        \n        n = 100\n        A1 = list(range(n))\n        A2 = list(range(100,\
    \ 100 + n))\n        lst = list2(A1, A2)\n        \n        # Perform random operations\n\
    \        for _ in range(50):\n            op = random.choice(['read', 'write',\
    \ 'append_pop'])\n            \n            if op == 'read' and len(lst) > 0:\n\
    \                idx = random.randint(0, len(lst) - 1)\n                val =\
    \ lst[idx]\n                assert val == (lst.A1[idx], lst.A2[idx])\n       \
    \         \n            elif op == 'write' and len(lst) > 0:\n               \
    \ idx = random.randint(0, len(lst) - 1)\n                new_val1 = random.randint(1000,\
    \ 2000)\n                new_val2 = random.randint(3000, 4000)\n             \
    \   lst[idx] = (new_val1, new_val2)\n                assert lst.A1[idx] == new_val1\n\
    \                assert lst.A2[idx] == new_val2\n                \n          \
    \  elif op == 'append_pop':\n                if random.random() < 0.5 and len(lst)\
    \ > 0:\n                    # Store expected value before popping\n          \
    \          expected = (lst.A1[-1], lst.A2[-1])\n                    popped = lst.pop()\n\
    \                    assert popped == expected\n                else:\n      \
    \              val1 = random.randint(5000, 6000)\n                    val2 = random.randint(7000,\
    \ 8000)\n                    lst.append((val1, val2))\n                    assert\
    \ lst[-1] == (val1, val2)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library \
    \              \n'''\n\n\n\n\ndef argsort(A: list[int], reverse=False):\n    P\
    \ = Packer(len(I := list(A))-1); P.ienumerate(I, reverse); I.sort(); P.iindices(I)\n\
    \    return I\n\n\n\nclass Packer:\n    __slots__ = 's', 'm'\n    def __init__(P,\
    \ mx: int): P.s = mx.bit_length(); P.m = (1 << P.s) - 1\n    def enc(P, a: int,\
    \ b: int): return a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return\
    \ x >> P.s, x & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A),\
    \ reverse); return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n\
    \            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n   \
    \         for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\n\n\ndef isort_parallel(*L: list, reverse=False):\n\
    \    inv, order = [0]*len(L[0]), argsort(L[0], reverse=reverse)\n    for i, j\
    \ in enumerate(order): inv[j] = i\n    for i, j in enumerate(order):\n       \
    \ for A in L: A[i], A[j] = A[j], A[i]\n        order[inv[i]], inv[j] = j, inv[i]\n\
    \    return L\nfrom typing import Generic\nfrom typing import TypeVar\n_S = TypeVar('S')\n\
    _T = TypeVar('T')\n_U = TypeVar('U')\n_T1 = TypeVar('T1')\n_T2 = TypeVar('T2')\n\
    _T3 = TypeVar('T3')\n_T4 = TypeVar('T4')\n_T5 = TypeVar('T5')\n_T6 = TypeVar('T6')\n\
    \n\n\nclass list2(Generic[_T1, _T2]):\n    __slots__ = 'A1', 'A2'\n    def __init__(lst,\
    \ A1: list[_T1], A2: list[_T2]): lst.A1, lst.A2 = A1, A2\n    def __len__(lst):\
    \ return len(lst.A1)\n    def __getitem__(lst, i: int): return lst.A1[i], lst.A2[i]\n\
    \    def __setitem__(lst, i: int, v: tuple[_T1, _T2]): lst.A1[i], lst.A2[i] =\
    \ v\n    def __contains__(lst, v: tuple[_T1, _T2]): raise NotImplementedError\n\
    \    def index(lst, v: tuple[_T1, _T2]): raise NotImplementedError\n    def reverse(lst):\
    \ lst.A1.reverse(); lst.A2.reverse()\n    def sort(lst, reverse=False): isort_parallel(lst.A1,\
    \ lst.A2, reverse=reverse)\n    def pop(lst): return lst.A1.pop(), lst.A2.pop()\n\
    \    def append(lst, v: tuple[_T1, _T2]): v1, v2 = v; lst.A1.append(v1); lst.A2.append(v2)\n\
    \    def add(lst, i: int, v: tuple[_T1, _T2]): lst.A1[i] += v[0]; lst.A2[i] +=\
    \ v[1]\n\nif __name__ == '__main__':\n    \"\"\"\n    Helper for making unittest\
    \ files compatible with verification-helper.\n    \n    This module provides a\
    \ helper function to run a dummy Library Checker test\n    so that unittest files\
    \ can be verified by oj-verify.\n    \"\"\"\n    \n    def run_verification_helper_unittest():\n\
    \        \"\"\"\n        Run a dummy Library Checker test for verification-helper\
    \ compatibility.\n        \n        This function should be called in the __main__\
    \ block of unittest files\n        that need to be compatible with verification-helper.\n\
    \        \n        The function:\n        1. Reads A and B from input\n      \
    \  2. Writes A+B to output  \n        3. If the result is the expected value (1198300249),\
    \ runs pytest\n        4. Exits with the pytest result code\n        \"\"\"\n\
    \        import sys\n        \n        \n        from typing import Type, Union,\
    \ overload\n        \n        import typing\n        from collections import deque\n\
    \        from numbers import Number\n        from types import GenericAlias \n\
    \        from typing import Callable, Collection, Iterator, Union\n        \n\
    \        import os\n        import sys\n        from io import BytesIO, IOBase\n\
    \        \n        \n        class FastIO(IOBase):\n            BUFSIZE = 8192\n\
    \            newlines = 0\n        \n            def __init__(self, file):\n \
    \               self._fd = file.fileno()\n                self.buffer = BytesIO()\n\
    \                self.writable = \"x\" in file.mode or \"r\" not in file.mode\n\
    \                self.write = self.buffer.write if self.writable else None\n \
    \       \n            def read(self):\n                BUFSIZE = self.BUFSIZE\n\
    \                while True:\n                    b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n                    if not b: break\n                    ptr = self.buffer.tell()\n\
    \                    self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \                self.newlines = 0\n                return self.buffer.read()\n\
    \        \n            def readline(self):\n                BUFSIZE = self.BUFSIZE\n\
    \                while self.newlines == 0:\n                    b = os.read(self._fd,\
    \ max(os.fstat(self._fd).st_size, BUFSIZE))\n                    self.newlines\
    \ = b.count(b\"\\n\") + (not b)\n                    ptr = self.buffer.tell()\n\
    \                    self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \                self.newlines -= 1\n                return self.buffer.readline()\n\
    \        \n            def flush(self):\n                if self.writable:\n \
    \                   os.write(self._fd, self.buffer.getvalue())\n             \
    \       self.buffer.truncate(0), self.buffer.seek(0)\n        \n        \n   \
    \     class IOWrapper(IOBase):\n            stdin: 'IOWrapper' = None\n      \
    \      stdout: 'IOWrapper' = None\n            \n            def __init__(self,\
    \ file):\n                self.buffer = FastIO(file)\n                self.flush\
    \ = self.buffer.flush\n                self.writable = self.buffer.writable\n\
    \        \n            def write(self, s):\n                return self.buffer.write(s.encode(\"\
    ascii\"))\n            \n            def read(self):\n                return self.buffer.read().decode(\"\
    ascii\")\n            \n            def readline(self):\n                return\
    \ self.buffer.readline().decode(\"ascii\")\n        try:\n            sys.stdin\
    \ = IOWrapper.stdin = IOWrapper(sys.stdin)\n            sys.stdout = IOWrapper.stdout\
    \ = IOWrapper(sys.stdout)\n        except:\n            pass\n        \n     \
    \   class TokenStream(Iterator):\n            stream = IOWrapper.stdin\n     \
    \   \n            def __init__(self):\n                self.queue = deque()\n\
    \        \n            def __next__(self):\n                if not self.queue:\
    \ self.queue.extend(self._line())\n                return self.queue.popleft()\n\
    \            \n            def wait(self):\n                if not self.queue:\
    \ self.queue.extend(self._line())\n                while self.queue: yield\n \
    \        \n            def _line(self):\n                return TokenStream.stream.readline().split()\n\
    \        \n            def line(self):\n                if self.queue:\n     \
    \               A = list(self.queue)\n                    self.queue.clear()\n\
    \                    return A\n                return self._line()\n        TokenStream.default\
    \ = TokenStream()\n        \n        class CharStream(TokenStream):\n        \
    \    def _line(self):\n                return TokenStream.stream.readline().rstrip()\n\
    \        CharStream.default = CharStream()\n        \n        ParseFn = Callable[[TokenStream],_T]\n\
    \        class Parser:\n            def __init__(self, spec: Union[type[_T],_T]):\n\
    \                self.parse = Parser.compile(spec)\n        \n            def\
    \ __call__(self, ts: TokenStream) -> _T:\n                return self.parse(ts)\n\
    \            \n            @staticmethod\n            def compile_type(cls: type[_T],\
    \ args = ()) -> _T:\n                if issubclass(cls, Parsable):\n         \
    \           return cls.compile(*args)\n                elif issubclass(cls, (Number,\
    \ str)):\n                    def parse(ts: TokenStream): return cls(next(ts))\
    \              \n                    return parse\n                elif issubclass(cls,\
    \ tuple):\n                    return Parser.compile_tuple(cls, args)\n      \
    \          elif issubclass(cls, Collection):\n                    return Parser.compile_collection(cls,\
    \ args)\n                elif callable(cls):\n                    def parse(ts:\
    \ TokenStream):\n                        return cls(next(ts))              \n\
    \                    return parse\n                else:\n                   \
    \ raise NotImplementedError()\n            \n            @staticmethod\n     \
    \       def compile(spec: Union[type[_T],_T]=int) -> ParseFn[_T]:\n          \
    \      if isinstance(spec, (type, GenericAlias)):\n                    cls = typing.get_origin(spec)\
    \ or spec\n                    args = typing.get_args(spec) or tuple()\n     \
    \               return Parser.compile_type(cls, args)\n                elif isinstance(offset\
    \ := spec, Number): \n                    cls = type(spec)  \n               \
    \     def parse(ts: TokenStream): return cls(next(ts)) + offset\n            \
    \        return parse\n                elif isinstance(args := spec, tuple): \
    \     \n                    return Parser.compile_tuple(type(spec), args)\n  \
    \              elif isinstance(args := spec, Collection):\n                  \
    \  return Parser.compile_collection(type(spec), args)\n                elif isinstance(fn\
    \ := spec, Callable): \n                    def parse(ts: TokenStream): return\
    \ fn(next(ts))\n                    return parse\n                else:\n    \
    \                raise NotImplementedError()\n        \n            @staticmethod\n\
    \            def compile_line(cls: _T, spec=int) -> ParseFn[_T]:\n           \
    \     if spec is int:\n                    fn = Parser.compile(spec)\n       \
    \             def parse(ts: TokenStream): return cls([int(token) for token in\
    \ ts.line()])\n                    return parse\n                else:\n     \
    \               fn = Parser.compile(spec)\n                    def parse(ts: TokenStream):\
    \ return cls([fn(ts) for _ in ts.wait()])\n                    return parse\n\
    \        \n            @staticmethod\n            def compile_repeat(cls: _T,\
    \ spec, N) -> ParseFn[_T]:\n                fn = Parser.compile(spec)\n      \
    \          def parse(ts: TokenStream): return cls([fn(ts) for _ in range(N)])\n\
    \                return parse\n        \n            @staticmethod\n         \
    \   def compile_children(cls: _T, specs) -> ParseFn[_T]:\n                fns\
    \ = tuple((Parser.compile(spec) for spec in specs))\n                def parse(ts:\
    \ TokenStream): return cls([fn(ts) for fn in fns])  \n                return parse\n\
    \                    \n            @staticmethod\n            def compile_tuple(cls:\
    \ type[_T], specs) -> ParseFn[_T]:\n                if isinstance(specs, (tuple,list))\
    \ and len(specs) == 2 and specs[1] is ...:\n                    return Parser.compile_line(cls,\
    \ specs[0])\n                else:\n                    return Parser.compile_children(cls,\
    \ specs)\n        \n            @staticmethod\n            def compile_collection(cls,\
    \ specs):\n                if not specs or len(specs) == 1 or isinstance(specs,\
    \ set):\n                    return Parser.compile_line(cls, *specs)\n       \
    \         elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and isinstance(specs[1],\
    \ int)):\n                    return Parser.compile_repeat(cls, specs[0], specs[1])\n\
    \                else:\n                    raise NotImplementedError()\n    \
    \    \n        class Parsable:\n            @classmethod\n            def compile(cls):\n\
    \                def parser(ts: TokenStream): return cls(next(ts))\n         \
    \       return parser\n            \n            @classmethod\n            def\
    \ __class_getitem__(cls, item):\n                return GenericAlias(cls, item)\n\
    \        \n        @overload\n        def read() -> list[int]: ...\n        @overload\n\
    \        def read(spec: Type[_T], char=False) -> _T: ...\n        @overload\n\
    \        def read(spec: _U, char=False) -> _U: ...\n        @overload\n      \
    \  def read(*specs: Type[_T], char=False) -> tuple[_T, ...]: ...\n        @overload\n\
    \        def read(*specs: _U, char=False) -> tuple[_U, ...]: ...\n        def\
    \ read(*specs: Union[Type[_T],_U], char=False):\n            if not char and not\
    \ specs: return [int(s) for s in TokenStream.default.line()]\n            parser:\
    \ _T = Parser.compile(specs[0] if len(specs) == 1 else specs)\n            return\
    \ parser(CharStream.default if char else TokenStream.default)\n        \n    \
    \    \n        import os\n        import sys\n        from io import BytesIO,\
    \ IOBase\n        \n        \n        class FastIO(IOBase):\n            BUFSIZE\
    \ = 8192\n            newlines = 0\n        \n            def __init__(self, file):\n\
    \                self._fd = file.fileno()\n                self.buffer = BytesIO()\n\
    \                self.writable = \"x\" in file.mode or \"r\" not in file.mode\n\
    \                self.write = self.buffer.write if self.writable else None\n \
    \       \n            def read(self):\n                BUFSIZE = self.BUFSIZE\n\
    \                while True:\n                    b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n                    if not b: break\n                    ptr = self.buffer.tell()\n\
    \                    self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \                self.newlines = 0\n                return self.buffer.read()\n\
    \        \n            def readline(self):\n                BUFSIZE = self.BUFSIZE\n\
    \                while self.newlines == 0:\n                    b = os.read(self._fd,\
    \ max(os.fstat(self._fd).st_size, BUFSIZE))\n                    self.newlines\
    \ = b.count(b\"\\n\") + (not b)\n                    ptr = self.buffer.tell()\n\
    \                    self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \                self.newlines -= 1\n                return self.buffer.readline()\n\
    \        \n            def flush(self):\n                if self.writable:\n \
    \                   os.write(self._fd, self.buffer.getvalue())\n             \
    \       self.buffer.truncate(0), self.buffer.seek(0)\n        \n        \n   \
    \     class IOWrapper(IOBase):\n            stdin: 'IOWrapper' = None\n      \
    \      stdout: 'IOWrapper' = None\n            \n            def __init__(self,\
    \ file):\n                self.buffer = FastIO(file)\n                self.flush\
    \ = self.buffer.flush\n                self.writable = self.buffer.writable\n\
    \        \n            def write(self, s):\n                return self.buffer.write(s.encode(\"\
    ascii\"))\n            \n            def read(self):\n                return self.buffer.read().decode(\"\
    ascii\")\n            \n            def readline(self):\n                return\
    \ self.buffer.readline().decode(\"ascii\")\n        try:\n            sys.stdin\
    \ = IOWrapper.stdin = IOWrapper(sys.stdin)\n            sys.stdout = IOWrapper.stdout\
    \ = IOWrapper(sys.stdout)\n        except:\n            pass\n        \n     \
    \   def write(*args, **kwargs):\n            '''Prints the values to a stream,\
    \ or to stdout_fast by default.'''\n            sep, file = kwargs.pop(\"sep\"\
    , \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n            at_start = True\n\
    \            for x in args:\n                if not at_start:\n              \
    \      file.write(sep)\n                file.write(str(x))\n                at_start\
    \ = False\n            file.write(kwargs.pop(\"end\", \"\\n\"))\n            if\
    \ kwargs.pop(\"flush\", False):\n                file.flush()\n        \n    \
    \    A, B = read()\n        write(C := A + B)\n        if C != 1198300249: \n\
    \            sys.exit(0)\n        \n        import io\n        from contextlib\
    \ import redirect_stdout, redirect_stderr\n    \n        # Capture all output\
    \ during test execution\n        output = io.StringIO()\n        with redirect_stdout(output),\
    \ redirect_stderr(output):\n            # Get the calling module's file path\n\
    \            frame = sys._getframe(1)\n            test_file = frame.f_globals.get('__file__')\n\
    \            if test_file is None:\n                test_file = sys.argv[0]\n\
    \            result = pytest.main([test_file])\n        \n        if result !=\
    \ 0: \n            print(output.getvalue())\n        sys.exit(result)\n    run_verification_helper_unittest()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb\n\n\
    import pytest\nimport random\n\nclass TestList2:\n    def test_initialization(self):\n\
    \        \"\"\"Test basic initialization of list2\"\"\"\n        A1 = [1, 2, 3,\
    \ 4, 5]\n        A2 = ['a', 'b', 'c', 'd', 'e']\n        lst = list2(A1, A2)\n\
    \        \n        assert lst.A1 is A1\n        assert lst.A2 is A2\n        assert\
    \ len(lst) == 5\n\n    def test_len(self):\n        \"\"\"Test __len__ method\"\
    \"\"\n        lst = list2([1, 2, 3], ['a', 'b', 'c'])\n        assert len(lst)\
    \ == 3\n        \n        lst = list2([], [])\n        assert len(lst) == 0\n\
    \        \n        lst = list2(list(range(100)), list(range(100)))\n        assert\
    \ len(lst) == 100\n\n    def test_getitem(self):\n        \"\"\"Test __getitem__\
    \ method\"\"\"\n        lst = list2([10, 20, 30], ['x', 'y', 'z'])\n        \n\
    \        assert lst[0] == (10, 'x')\n        assert lst[1] == (20, 'y')\n    \
    \    assert lst[2] == (30, 'z')\n        \n        # Test negative indexing\n\
    \        assert lst[-1] == (30, 'z')\n        assert lst[-2] == (20, 'y')\n\n\
    \    def test_setitem(self):\n        \"\"\"Test __setitem__ method\"\"\"\n  \
    \      lst = list2([10, 20, 30], ['x', 'y', 'z'])\n        \n        lst[0] =\
    \ (15, 'a')\n        lst[1] = (25, 'b')\n        lst[2] = (35, 'c')\n        \n\
    \        assert lst.A1 == [15, 25, 35]\n        assert lst.A2 == ['a', 'b', 'c']\n\
    \        assert lst[0] == (15, 'a')\n        assert lst[1] == (25, 'b')\n    \
    \    assert lst[2] == (35, 'c')\n\n    def test_contains_not_implemented(self):\n\
    \        \"\"\"Test that __contains__ raises NotImplementedError\"\"\"\n     \
    \   lst = list2([1, 2, 3], ['a', 'b', 'c'])\n        \n        with pytest.raises(NotImplementedError):\n\
    \            (1, 'a') in lst\n\n    def test_index_not_implemented(self):\n  \
    \      \"\"\"Test that index raises NotImplementedError\"\"\"\n        lst = list2([1,\
    \ 2, 3], ['a', 'b', 'c'])\n        \n        with pytest.raises(NotImplementedError):\n\
    \            lst.index((1, 'a'))\n\n    def test_reverse(self):\n        \"\"\"\
    Test reverse method\"\"\"\n        lst = list2([1, 2, 3, 4, 5], ['a', 'b', 'c',\
    \ 'd', 'e'])\n        \n        lst.reverse()\n        \n        assert lst.A1\
    \ == [5, 4, 3, 2, 1]\n        assert lst.A2 == ['e', 'd', 'c', 'b', 'a']\n   \
    \     assert lst[0] == (5, 'e')\n        assert lst[4] == (1, 'a')\n\n    def\
    \ test_sort(self):\n        \"\"\"Test sort method\"\"\"\n        lst = list2([3,\
    \ 1, 4, 1, 5], ['c', 'a', 'd', 'b', 'e'])\n        \n        lst.sort()\n    \
    \    \n        # Should sort by first element\n        assert lst.A1 == [1, 1,\
    \ 3, 4, 5]\n        assert lst.A2 == ['a', 'b', 'c', 'd', 'e']\n        \n   \
    \ def test_sort_reverse(self):\n        \"\"\"Test sort method with reverse=True\"\
    \"\"\n        lst = list2([3, 1, 4, 1, 5], ['c', 'a', 'd', 'b', 'e'])\n      \
    \  \n        lst.sort(reverse=True)\n        \n        # Should sort by first\
    \ element in reverse\n        assert lst.A1 == [5, 4, 3, 1, 1]\n        assert\
    \ lst.A2 == ['e', 'd', 'c', 'a', 'b']\n\n    def test_pop(self):\n        \"\"\
    \"Test pop method\"\"\"\n        lst = list2([1, 2, 3, 4, 5], ['a', 'b', 'c',\
    \ 'd', 'e'])\n        \n        popped = lst.pop()\n        assert popped == (5,\
    \ 'e')\n        assert len(lst) == 4\n        assert lst.A1 == [1, 2, 3, 4]\n\
    \        assert lst.A2 == ['a', 'b', 'c', 'd']\n        \n        popped = lst.pop()\n\
    \        assert popped == (4, 'd')\n        assert len(lst) == 3\n\n    def test_append(self):\n\
    \        \"\"\"Test append method\"\"\"\n        lst = list2([1, 2, 3], ['a',\
    \ 'b', 'c'])\n        \n        lst.append((4, 'd'))\n        assert len(lst)\
    \ == 4\n        assert lst[3] == (4, 'd')\n        assert lst.A1 == [1, 2, 3,\
    \ 4]\n        assert lst.A2 == ['a', 'b', 'c', 'd']\n        \n        lst.append((5,\
    \ 'e'))\n        assert len(lst) == 5\n        assert lst[4] == (5, 'e')\n\n \
    \   def test_empty_list(self):\n        \"\"\"Test operations on empty list2\"\
    \"\"\n        lst = list2([], [])\n        \n        assert len(lst) == 0\n  \
    \      \n        with pytest.raises(IndexError):\n            lst.pop()\n    \
    \    \n        lst.append((1, 'a'))\n        assert len(lst) == 1\n        assert\
    \ lst[0] == (1, 'a')\n\n    def test_with_different_types(self):\n        \"\"\
    \"Test list2 with different data types\"\"\"\n        # Integer and float\n  \
    \      lst = list2([1, 2, 3], [1.1, 2.2, 3.3])\n        assert lst[0] == (1, 1.1)\n\
    \        assert lst[1] == (2, 2.2)\n        \n        # String and boolean\n \
    \       lst = list2(['a', 'b', 'c'], [True, False, True])\n        assert lst[0]\
    \ == ('a', True)\n        assert lst[1] == ('b', False)\n        \n        # Mixed\
    \ types\n        lst = list2([1, 'two', 3.0], [None, [1, 2], {'key': 'value'}])\n\
    \        assert lst[0] == (1, None)\n        assert lst[1] == ('two', [1, 2])\n\
    \        assert lst[2] == (3.0, {'key': 'value'})\n\n    def test_large_data_operations(self):\n\
    \        \"\"\"Test operations on larger datasets\"\"\"\n        n = 1000\n  \
    \      A1 = list(range(n))\n        A2 = list(range(n, 2*n))\n        lst = list2(A1,\
    \ A2)\n        \n        assert len(lst) == n\n        assert lst[0] == (0, n)\n\
    \        assert lst[n-1] == (n-1, 2*n-1)\n        \n        # Test pop on large\
    \ dataset\n        popped = lst.pop()\n        assert popped == (n-1, 2*n-1)\n\
    \        assert len(lst) == n-1\n        \n        # Test append on large dataset\n\
    \        lst.append((n, 2*n))\n        assert len(lst) == n\n        assert lst[n-1]\
    \ == (n, 2*n)\n\n    def test_sort_stability(self):\n        \"\"\"Test that sort\
    \ maintains parallel structure\"\"\"\n        # Create data where first elements\
    \ have duplicates\n        lst = list2([3, 1, 2, 1, 3], ['a', 'b', 'c', 'd', 'e'])\n\
    \        \n        lst.sort()\n        \n        # After sorting by first element,\
    \ check parallel structure\n        assert lst[0][0] == 1\n        assert lst[1][0]\
    \ == 1\n        assert lst[2][0] == 2\n        assert lst[3][0] == 3\n       \
    \ assert lst[4][0] == 3\n        \n        # The corresponding second elements\
    \ should be maintained\n        assert lst[0][1] == 'b'\n        assert lst[1][1]\
    \ == 'd'\n        assert lst[2][1] == 'c'\n        assert lst[3][1] == 'a'\n \
    \       assert lst[4][1] == 'e'\n\n    def test_random_operations(self):\n   \
    \     \"\"\"Test random operations for robustness\"\"\"\n        random.seed(42)\n\
    \        \n        n = 100\n        A1 = list(range(n))\n        A2 = list(range(100,\
    \ 100 + n))\n        lst = list2(A1, A2)\n        \n        # Perform random operations\n\
    \        for _ in range(50):\n            op = random.choice(['read', 'write',\
    \ 'append_pop'])\n            \n            if op == 'read' and len(lst) > 0:\n\
    \                idx = random.randint(0, len(lst) - 1)\n                val =\
    \ lst[idx]\n                assert val == (lst.A1[idx], lst.A2[idx])\n       \
    \         \n            elif op == 'write' and len(lst) > 0:\n               \
    \ idx = random.randint(0, len(lst) - 1)\n                new_val1 = random.randint(1000,\
    \ 2000)\n                new_val2 = random.randint(3000, 4000)\n             \
    \   lst[idx] = (new_val1, new_val2)\n                assert lst.A1[idx] == new_val1\n\
    \                assert lst.A2[idx] == new_val2\n                \n          \
    \  elif op == 'append_pop':\n                if random.random() < 0.5 and len(lst)\
    \ > 0:\n                    # Store expected value before popping\n          \
    \          expected = (lst.A1[-1], lst.A2[-1])\n                    popped = lst.pop()\n\
    \                    assert popped == expected\n                else:\n      \
    \              val1 = random.randint(5000, 6000)\n                    val2 = random.randint(7000,\
    \ 8000)\n                    lst.append((val1, val2))\n                    assert\
    \ lst[-1] == (val1, val2)\n\nfrom cp_library.ds.list.list2_cls import list2\n\n\
    if __name__ == '__main__':\n    from cp_library.test.unittest_helper import run_verification_helper_unittest\n\
    \    run_verification_helper_unittest()"
  dependsOn:
  - cp_library/ds/list/list2_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: true
  path: test/unittests/ds/list/list2_cls_test.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/list/list2_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/list/list2_cls_test.py
- /verify/test/unittests/ds/list/list2_cls_test.py.html
title: test/unittests/ds/list/list2_cls_test.py
---
