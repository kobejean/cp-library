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
    path: cp_library/ds/list/list4_cls.py
    title: cp_library/ds/list/list4_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit4_cls.py
    title: cp_library/ds/tree/bit/bit4_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit_base_cls.py
    title: cp_library/ds/tree/bit/bit_base_cls.py
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
    \nimport pytest\n\nclass TestBIT4:\n    def test_basic_operations(self):\n   \
    \     \"\"\"Test basic BIT4 operations\"\"\"\n        values = [(1, 10, 100, 1000),\
    \ (2, 20, 200, 2000), (3, 30, 300, 3000)]\n        bit = BIT4(values)\n      \
    \  \n        assert len(bit) == 3\n        assert bit[0] == (1, 10, 100, 1000)\n\
    \        assert bit[1] == (2, 20, 200, 2000)\n        assert bit[2] == (3, 30,\
    \ 300, 3000)\n        \n        assert bit.sum(1) == (1, 10, 100, 1000)\n    \
    \    assert bit.sum(2) == (3, 30, 300, 3000)\n        assert bit.sum(3) == (6,\
    \ 60, 600, 6000)\n\n    def test_sum_range(self):\n        \"\"\"Test range sum\
    \ operations\"\"\"\n        values = [(1, 10, 100, 1000), (2, 20, 200, 2000),\
    \ (3, 30, 300, 3000)]\n        bit = BIT4(values)\n        \n        assert bit.sum_range(0,\
    \ 2) == (3, 30, 300, 3000)\n        assert bit.sum_range(1, 3) == (5, 50, 500,\
    \ 5000)\n\n    def test_initialization_with_size(self):\n        \"\"\"Test initialization\
    \ with size\"\"\"\n        bit = BIT4(5, (0, 0, 0, 0))\n        assert len(bit)\
    \ == 5\n        for i in range(5):\n            assert bit[i] == (0, 0, 0, 0)\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\nfrom\
    \ typing import TypeVar\n_S = TypeVar('S')\n_T = TypeVar('T')\n_U = TypeVar('U')\n\
    _T1 = TypeVar('T1')\n_T2 = TypeVar('T2')\n_T3 = TypeVar('T3')\n_T4 = TypeVar('T4')\n\
    _T5 = TypeVar('T5')\n_T6 = TypeVar('T6')\n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n            \u250F\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513            \n   \
    \         \u2503                                    7 \u2503            \n   \
    \         \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\
    \u2501\u251B            \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513\
    \                 \u2502              \n            \u2503                3 \u2503\
    \u25C4\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2524              \n            \u2517\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u252F\u2501\u251B                 \u2502              \n            \u250F\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513       \u2502  \u250F\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2513       \u2502              \n      \
    \      \u2503      1 \u2503\u25C4\u2500\u2500\u2500\u2500\u2500\u2500\u2524  \u2503\
    \      5 \u2503\u25C4\u2500\u2500\u2500\u2500\u2500\u2500\u2524              \n\
    \            \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B    \
    \   \u2502  \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B     \
    \  \u2502              \n            \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\
    \u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\
    \u2501\u2501\u2501\u2513  \u2502              \n            \u2503 0 \u2503\u25C4\
    \u2500\u2524  \u2503 2 \u2503\u25C4\u2500\u2524  \u2503 4 \u2503\u25C4\u2500\u2524\
    \  \u2503 6 \u2503\u25C4\u2500\u2524              \n            \u2517\u2501\u252F\
    \u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\
    \u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502              \n \
    \             \u2502    \u2502    \u2502    \u2502    \u2502    \u2502    \u2502\
    \    \u2502              \n              \u25BC    \u25BC    \u25BC    \u25BC\
    \    \u25BC    \u25BC    \u25BC    \u25BC              \n            \u250F\u2501\
    \u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\
    \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\
    \u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513     \
    \       \n            \u2503 0 \u2503\u2503 1 \u2503\u2503 2 \u2503\u2503 3 \u2503\
    \u2503 4 \u2503\u2503 5 \u2503\u2503 6 \u2503\u2503 7 \u2503            \n   \
    \         \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\
    \u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\
    \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\
    \u2501\u251B            \n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n           Data Structure - Tree - Binary Index Tree     \
    \       \n'''\n\n\n\n\ndef argsort(A: list[int], reverse=False):\n    P = Packer(len(I\
    \ := list(A))-1); P.ienumerate(I, reverse); I.sort(); P.iindices(I)\n    return\
    \ I\n\n\n\nclass Packer:\n    __slots__ = 's', 'm'\n    def __init__(P, mx: int):\
    \ P.s = mx.bit_length(); P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int):\
    \ return a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return x >>\
    \ P.s, x & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A),\
    \ reverse); return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n\
    \            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n   \
    \         for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\n\n\ndef isort_parallel(*L: list, reverse=False):\n\
    \    inv, order = [0]*len(L[0]), argsort(L[0], reverse=reverse)\n    for i, j\
    \ in enumerate(order): inv[j] = i\n    for i, j in enumerate(order):\n       \
    \ for A in L: A[i], A[j] = A[j], A[i]\n        order[inv[i]], inv[j] = j, inv[i]\n\
    \    return L\nfrom typing import Generic\n\n\nclass list4(Generic[_T1, _T2, _T3,\
    \ _T4]):\n    __slots__ = 'A1', 'A2', 'A3', 'A4'\n    def __init__(lst, A1: list[_T1],\
    \ A2: list[_T2], A3: list[_T3], A4: list[_T4]):\n        lst.A1, lst.A2, lst.A3,\
    \ lst.A4 = A1, A2, A3, A4\n    def __len__(lst): return len(lst.A1)\n    def __getitem__(lst,\
    \ i: int): return lst.A1[i], lst.A2[i], lst.A3[i], lst.A4[i]\n    def __setitem__(lst,\
    \ i: int, v: tuple[_T1, _T2, _T3, _T4]): lst.A1[i], lst.A2[i], lst.A3[i], lst.A4[i]\
    \ = v\n    def __contains__(lst, v: tuple[_T1, _T2, _T3, _T4]): raise NotImplementedError\n\
    \    def index(lst, v: tuple[_T1, _T2, _T3, _T4]): raise NotImplementedError\n\
    \    def reverse(lst): lst.A1.reverse(); lst.A2.reverse(); lst.A3.reverse(); lst.A4.reverse()\n\
    \    def sort(lst, reverse=False): isort_parallel(lst.A1, lst.A2, lst.A3, lst.A4,\
    \ reverse=reverse)\n    def pop(lst): return lst.A1.pop(), lst.A2.pop(), lst.A3.pop(),\
    \ lst.A4.pop()\n    def append(lst, v: tuple[_T1, _T2, _T3, _T4]):\n        v1,\
    \ v2, v3, v4 = v\n        lst.A1.append(v1); lst.A2.append(v2); lst.A3.append(v3);\
    \ lst.A4.append(v4)\n    def add(lst, i: int, v: tuple[_T1, _T2, _T3, _T4]): lst.A1[i]\
    \ += v[0]; lst.A2[i] += v[1]; lst.A3[i] += v[2]; lst.A4[i] += v[3]\nfrom typing\
    \ import Generic, Union, Callable, Optional\n\nclass BITBase(Generic[_T]):\n \
    \   _lst = list\n    K: int = 1\n    \n    def __init__(bit, v: Union[int, list[_T]],\
    \ e: _T = None) -> None:\n        if isinstance(v, int):\n            bit._n =\
    \ v\n            if bit._lst is list:\n                bit._d = [e]*v if e is\
    \ not None else [0]*v\n            elif e is not None:\n                bit._d\
    \ = bit._lst(*([e_]*v for e_ in e))\n            else:\n                bit._d\
    \ = bit._lst(*([0]*v for _ in range(bit.K)))\n        else:\n            bit.build(v)\n\
    \        bit.e = e if e is not None else (0 if bit._lst is list else tuple(0 for\
    \ _ in range(bit.K)))\n        bit._lb = 1 << bit._n.bit_length()\n\n    def build(bit,\
    \ data: list[_T]):\n        bit._n = len(data)\n        if bit._lst is list:\n\
    \            bit._d = bit._lst(data)\n        else:\n            bit._d = bit._lst(*([data[i][j]\
    \ for i in range(len(data))] for j in range(len(data[0]))))\n        for i in\
    \ range(bit._n):\n            if (r := i | i + 1) < bit._n:\n                bit._add(r,\
    \ bit._d[i])\n\n    def _add(bit, i: int, x: _T) -> None:\n        bit._d[i] =\
    \ bit._op(bit._d[i], x)\n    \n    def _op(bit, a: _T, b: _T) -> _T:\n       \
    \ return a + b\n    \n    def _sub(bit, a: _T, b: _T) -> _T:\n        return a\
    \ - b\n\n    def add(bit, i: int, x: _T) -> None:\n        while i < bit._n: bit._add(i,\
    \ x); i |= i + 1\n\n    def sum(bit, n: int) -> _T:\n        s = bit.e\n     \
    \   while n: s, n = bit._op(s, bit._d[n - 1]), n & n - 1\n        return s\n\n\
    \    def sum_range(bit, l: int, r: int) -> _T:\n        s = bit.e\n        while\
    \ r: s, r = bit._op(s, bit._d[r - 1]), r & r - 1\n        while l: s, l = bit._sub(s,\
    \ bit._d[l - 1]), l & l - 1\n        return s\n\n    def __len__(bit) -> int:\
    \ return bit._n\n\n    def __getitem__(bit, i: int) -> _T:\n        s, l = bit._d[i],\
    \ i & (i + 1)\n        while l != i: s, i = bit._sub(s, bit._d[i - 1]), i - (i\
    \ & -i)\n        return s\n\n    get = __getitem__\n\n    def __setitem__(bit,\
    \ i: int, x: _T) -> None:\n        bit.add(i, bit._sub(x, bit[i]))\n\n    set\
    \ = __setitem__\n\n    def prelist(bit) -> list[_T]:\n        pre = [bit.e] +\
    \ bit._d[:] if bit._lst is list else bit._lst(*([e_] * (bit._n + 1) for e_ in\
    \ bit.e))\n        for i in range(bit._n): pre[i+1] = bit._d[i]\n        for i\
    \ in range(bit._n + 1):\n            if i & i - 1 < bit._n + 1:\n            \
    \    pre[i] = bit._op(pre[i], pre[i & i - 1])\n        return pre\n\n    def bisect_left(bit,\
    \ v, key: Optional[Callable] = None) -> int:\n        i = 0\n        s = bit.e\n\
    \        if v <= s: return -1\n        m = bit._lb\n        \n        if key:\n\
    \            while m := m >> 1:\n                if (ni := m | i) <= bit._n and\
    \ key(ns := bit._op(s, bit._d[ni - 1])) < v:\n                    s, i = ns, ni\n\
    \        else:\n            while m := m >> 1:\n                if (ni := m |\
    \ i) <= bit._n and (ns := bit._op(s, bit._d[ni - 1])) < v:\n                 \
    \   s, i = ns, ni\n        return i\n\n    def bisect_right(bit, v, key: Optional[Callable]\
    \ = None) -> int:\n        i = 0\n        s = bit.e\n        m = bit._lb\n   \
    \     \n        if key:\n            while m := m >> 1:\n                if (ni\
    \ := m | i) <= bit._n and key(ns := bit._op(s, bit._d[ni - 1])) <= v:\n      \
    \              s, i = ns, ni\n        else:\n            while m := m >> 1:\n\
    \                if (ni := m | i) <= bit._n and (ns := bit._op(s, bit._d[ni -\
    \ 1])) <= v:\n                    s, i = ns, ni\n        return i\n\nclass BIT4(BITBase[_T]):\n\
    \    _lst = list4\n    K = 4\n    def _add(bit, i: int, x: _T) -> None: bit._d.add(i,\
    \ x)\n    def _op(bit, a, b): return a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3]\
    \ + b[3]\n    def _sub(bit, a, b): return a[0] - b[0], a[1] - b[1], a[2] - b[2],\
    \ a[3] - b[3]\n\nif __name__ == '__main__':\n    \"\"\"\n    Helper for making\
    \ unittest files compatible with verification-helper.\n    \n    This module provides\
    \ a helper function to run a dummy Library Checker test\n    so that unittest\
    \ files can be verified by oj-verify.\n    \"\"\"\n    \n    def run_verification_helper_unittest():\n\
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
    import pytest\n\nclass TestBIT4:\n    def test_basic_operations(self):\n     \
    \   \"\"\"Test basic BIT4 operations\"\"\"\n        values = [(1, 10, 100, 1000),\
    \ (2, 20, 200, 2000), (3, 30, 300, 3000)]\n        bit = BIT4(values)\n      \
    \  \n        assert len(bit) == 3\n        assert bit[0] == (1, 10, 100, 1000)\n\
    \        assert bit[1] == (2, 20, 200, 2000)\n        assert bit[2] == (3, 30,\
    \ 300, 3000)\n        \n        assert bit.sum(1) == (1, 10, 100, 1000)\n    \
    \    assert bit.sum(2) == (3, 30, 300, 3000)\n        assert bit.sum(3) == (6,\
    \ 60, 600, 6000)\n\n    def test_sum_range(self):\n        \"\"\"Test range sum\
    \ operations\"\"\"\n        values = [(1, 10, 100, 1000), (2, 20, 200, 2000),\
    \ (3, 30, 300, 3000)]\n        bit = BIT4(values)\n        \n        assert bit.sum_range(0,\
    \ 2) == (3, 30, 300, 3000)\n        assert bit.sum_range(1, 3) == (5, 50, 500,\
    \ 5000)\n\n    def test_initialization_with_size(self):\n        \"\"\"Test initialization\
    \ with size\"\"\"\n        bit = BIT4(5, (0, 0, 0, 0))\n        assert len(bit)\
    \ == 5\n        for i in range(5):\n            assert bit[i] == (0, 0, 0, 0)\n\
    \nfrom cp_library.ds.tree.bit.bit4_cls import BIT4\n\nif __name__ == '__main__':\n\
    \    from cp_library.test.unittest_helper import run_verification_helper_unittest\n\
    \    run_verification_helper_unittest()"
  dependsOn:
  - cp_library/ds/tree/bit/bit4_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/ds/list/list4_cls.py
  - cp_library/ds/tree/bit/bit_base_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: true
  path: test/unittests/ds/tree/bit/bit4_cls_test.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/tree/bit/bit4_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/tree/bit/bit4_cls_test.py
- /verify/test/unittests/ds/tree/bit/bit4_cls_test.py.html
title: test/unittests/ds/tree/bit/bit4_cls_test.py
---
