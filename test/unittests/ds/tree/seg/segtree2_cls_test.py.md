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
    path: cp_library/ds/tree/seg/segtree2_cls.py
    title: cp_library/ds/tree/seg/segtree2_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/seg/segtree_cls.py
    title: cp_library/ds/tree/seg/segtree_cls.py
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
    \nimport pytest\nimport random\nfrom operator import add\n\nclass TestSegTree2:\n\
    \    def test_initialization_with_list(self):\n        \"\"\"Test initialization\
    \ with a list of tuples\"\"\"\n        values = [(1, 10), (2, 20), (3, 30), (4,\
    \ 40)]\n        seg = SegTree2(lambda a, b: (a[0] + b[0], a[1] + b[1]), (0, 0),\
    \ values)\n        \n        assert seg.n == 4\n        assert seg[0] == (1, 10)\n\
    \        assert seg[1] == (2, 20)\n        assert seg[2] == (3, 30)\n        assert\
    \ seg[3] == (4, 40)\n\n    def test_initialization_with_size(self):\n        \"\
    \"\"Test initialization with size only\"\"\"\n        seg = SegTree2(lambda a,\
    \ b: (a[0] + b[0], a[1] + b[1]), (0, 0), 5)\n        \n        assert seg.n ==\
    \ 5\n        # All elements should be identity\n        for i in range(5):\n \
    \           assert seg[i] == (0, 0)\n\n    def test_set_and_get(self):\n     \
    \   \"\"\"Test set and get operations\"\"\"\n        seg = SegTree2(lambda a,\
    \ b: (a[0] + b[0], a[1] + b[1]), (0, 0), 4)\n        \n        seg[0] = (1, 10)\n\
    \        seg[1] = (2, 20)\n        seg[2] = (3, 30)\n        seg[3] = (4, 40)\n\
    \        \n        assert seg[0] == (1, 10)\n        assert seg[1] == (2, 20)\n\
    \        assert seg[2] == (3, 30)\n        assert seg[3] == (4, 40)\n\n    def\
    \ test_prod_sum(self):\n        \"\"\"Test prod operation with sum\"\"\"\n   \
    \     values = [(1, 10), (2, 20), (3, 30), (4, 40)]\n        seg = SegTree2(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1]), (0, 0), values)\n        \n        # Test\
    \ various ranges\n        assert seg.prod(0, 4) == (10, 100)  # Sum of all\n \
    \       assert seg.prod(0, 2) == (3, 30)    # First two\n        assert seg.prod(1,\
    \ 3) == (5, 50)    # Middle two\n        assert seg.prod(2, 4) == (7, 70)    #\
    \ Last two\n        assert seg.prod(1, 2) == (2, 20)    # Single element\n   \
    \     assert seg.prod(2, 2) == (0, 0)     # Empty range\n\n    def test_prod_max(self):\n\
    \        \"\"\"Test prod operation with max\"\"\"\n        values = [(3, 30),\
    \ (1, 10), (4, 40), (2, 20)]\n        seg = SegTree2(lambda a, b: (max(a[0], b[0]),\
    \ max(a[1], b[1])), (float('-inf'), float('-inf')), values)\n        \n      \
    \  assert seg.prod(0, 4) == (4, 40)\n        assert seg.prod(0, 2) == (3, 30)\n\
    \        assert seg.prod(1, 3) == (4, 40)\n        assert seg.prod(2, 4) == (4,\
    \ 40)\n\n    def test_prod_min(self):\n        \"\"\"Test prod operation with\
    \ min\"\"\"\n        values = [(3, 30), (1, 10), (4, 40), (2, 20)]\n        seg\
    \ = SegTree2(lambda a, b: (min(a[0], b[0]), min(a[1], b[1])), (float('inf'), float('inf')),\
    \ values)\n        \n        assert seg.prod(0, 4) == (1, 10)\n        assert\
    \ seg.prod(0, 2) == (1, 10)\n        assert seg.prod(1, 3) == (1, 10)\n      \
    \  assert seg.prod(2, 4) == (2, 20)\n\n    def test_all_prod(self):\n        \"\
    \"\"Test all_prod operation\"\"\"\n        values = [(1, 10), (2, 20), (3, 30),\
    \ (4, 40)]\n        seg = SegTree2(lambda a, b: (a[0] + b[0], a[1] + b[1]), (0,\
    \ 0), values)\n        \n        assert seg.all_prod() == (10, 100)\n\n    def\
    \ test_max_right(self):\n        \"\"\"Test max_right operation\"\"\"\n      \
    \  values = [(1, 10), (2, 20), (3, 30), (4, 40)]\n        seg = SegTree2(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1]), (0, 0), values)\n        \n        # Find\
    \ the rightmost position where sum is <= threshold\n        assert seg.max_right(0,\
    \ lambda x: x[0] <= 3) == 2   # Sum up to index 2 is 3\n        assert seg.max_right(0,\
    \ lambda x: x[0] <= 6) == 3   # Sum up to index 3 is 6\n        assert seg.max_right(0,\
    \ lambda x: x[0] <= 10) == 4  # Sum up to index 4 is 10\n        assert seg.max_right(1,\
    \ lambda x: x[0] <= 5) == 3   # Sum from 1 to 3 is 5\n        assert seg.max_right(0,\
    \ lambda x: x[0] <= 0) == 0   # No elements satisfy\n\n    def test_min_left(self):\n\
    \        \"\"\"Test min_left operation\"\"\"\n        values = [(1, 10), (2, 20),\
    \ (3, 30), (4, 40)]\n        seg = SegTree2(lambda a, b: (a[0] + b[0], a[1] +\
    \ b[1]), (0, 0), values)\n        \n        # Find the leftmost position where\
    \ sum from that position is <= threshold\n        assert seg.min_left(4, lambda\
    \ x: x[0] <= 4) == 3    # Only last element\n        assert seg.min_left(4, lambda\
    \ x: x[0] <= 7) == 2    # Last two elements\n        assert seg.min_left(4, lambda\
    \ x: x[0] <= 10) == 0   # All elements\n        assert seg.min_left(3, lambda\
    \ x: x[0] <= 3) == 2    # Elements 2-3\n        assert seg.min_left(4, lambda\
    \ x: x[0] <= 0) == 4    # No elements satisfy\n\n    def test_update_and_query(self):\n\
    \        \"\"\"Test update operations affect queries correctly\"\"\"\n       \
    \ seg = SegTree2(lambda a, b: (a[0] + b[0], a[1] + b[1]), (0, 0), 4)\n       \
    \ \n        # Initial values\n        seg[0] = (1, 10)\n        seg[1] = (2, 20)\n\
    \        seg[2] = (3, 30)\n        seg[3] = (4, 40)\n        \n        assert\
    \ seg.prod(0, 4) == (10, 100)\n        \n        # Update some values\n      \
    \  seg[1] = (5, 50)\n        seg[2] = (6, 60)\n        \n        assert seg.prod(0,\
    \ 4) == (16, 160)\n        assert seg.prod(1, 3) == (11, 110)\n\n    def test_empty_tree(self):\n\
    \        \"\"\"Test empty segment tree\"\"\"\n        seg = SegTree2(lambda a,\
    \ b: (a[0] + b[0], a[1] + b[1]), (0, 0), 0)\n        \n        assert seg.n ==\
    \ 0\n        assert seg.all_prod() == (0, 0)\n\n    def test_single_element(self):\n\
    \        \"\"\"Test segment tree with single element\"\"\"\n        seg = SegTree2(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1]), (0, 0), [(5, 50)])\n        \n        assert\
    \ seg.n == 1\n        assert seg[0] == (5, 50)\n        assert seg.prod(0, 1)\
    \ == (5, 50)\n        assert seg.all_prod() == (5, 50)\n\n    def test_large_tree(self):\n\
    \        \"\"\"Test with larger dataset\"\"\"\n        n = 1000\n        values\
    \ = [(i, i * 10) for i in range(n)]\n        seg = SegTree2(lambda a, b: (a[0]\
    \ + b[0], a[1] + b[1]), (0, 0), values)\n        \n        # Sum of 0..999 = 499500\n\
    \        assert seg.all_prod() == (499500, 4995000)\n        \n        # Sum of\
    \ 0..99 = 4950\n        assert seg.prod(0, 100) == (4950, 49500)\n        \n \
    \       # Update and verify\n        seg[500] = (1000, 10000)\n        expected_sum\
    \ = 499500 - 500 + 1000\n        assert seg.all_prod() == (expected_sum, 4995000\
    \ - 5000 + 10000)\n\n    def test_different_types(self):\n        \"\"\"Test with\
    \ different data types in tuples\"\"\"\n        # String concatenation and list\
    \ concatenation\n        seg = SegTree2(\n            lambda a, b: (a[0] + b[0],\
    \ a[1] + b[1]),\n            (\"\", []),\n            [(\"a\", [1]), (\"b\", [2]),\
    \ (\"c\", [3]), (\"d\", [4])]\n        )\n        \n        assert seg.prod(0,\
    \ 2) == (\"ab\", [1, 2])\n        assert seg.prod(1, 4) == (\"bcd\", [2, 3, 4])\n\
    \        assert seg.all_prod() == (\"abcd\", [1, 2, 3, 4])\n\n    def test_non_commutative_operation(self):\n\
    \        \"\"\"Test with non-commutative operations\"\"\"\n        # Matrix-like\
    \ operation (simplified)\n        def matrix_mult(a, b):\n            # Simplified\
    \ 2x1 matrix multiplication\n            return (a[0] * b[0], a[1] * b[0] + b[1])\n\
    \        \n        seg = SegTree2(matrix_mult, (1, 0), [(2, 1), (3, 2), (4, 3),\
    \ (5, 4)])\n        \n        # Verify non-commutative property affects results\n\
    \        result = seg.prod(0, 2)\n        assert result == (6, 5)  # (2*3, 1*3+2)\n\
    \n    def test_stress_random_operations(self):\n        \"\"\"Stress test with\
    \ random operations\"\"\"\n        random.seed(42)\n        n = 100\n        \n\
    \        # Initialize with random values\n        values = [(random.randint(1,\
    \ 100), random.randint(1, 100)) for _ in range(n)]\n        seg = SegTree2(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1]), (0, 0), values)\n        \n        # Perform\
    \ random operations\n        for _ in range(200):\n            op = random.choice(['update',\
    \ 'query'])\n            \n            if op == 'update':\n                idx\
    \ = random.randint(0, n-1)\n                new_val = (random.randint(1, 100),\
    \ random.randint(1, 100))\n                seg[idx] = new_val\n              \
    \  values[idx] = new_val\n            else:\n                l = random.randint(0,\
    \ n-1)\n                r = random.randint(l, n)\n                \n         \
    \       # Verify against naive calculation\n                expected = (0, 0)\n\
    \                for i in range(l, r):\n                    expected = (expected[0]\
    \ + values[i][0], expected[1] + values[i][1])\n                \n            \
    \    assert seg.prod(l, r) == expected\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\nfrom typing import TypeVar\n_S = TypeVar('S')\n_T = TypeVar('T')\n\
    _U = TypeVar('U')\n_T1 = TypeVar('T1')\n_T2 = TypeVar('T2')\n_T3 = TypeVar('T3')\n\
    _T4 = TypeVar('T4')\n_T5 = TypeVar('T5')\n_T6 = TypeVar('T6')\n\n\n\n\n\ndef argsort(A:\
    \ list[int], reverse=False):\n    P = Packer(len(I := list(A))-1); P.ienumerate(I,\
    \ reverse); I.sort(); P.iindices(I)\n    return I\n\n\n\nclass Packer:\n    __slots__\
    \ = 's', 'm'\n    def __init__(P, mx: int): P.s = mx.bit_length(); P.m = (1 <<\
    \ P.s) - 1\n    def enc(P, a: int, b: int): return a << P.s | b\n    def dec(P,\
    \ x: int) -> tuple[int, int]: return x >> P.s, x & P.m\n    def enumerate(P, A,\
    \ reverse=False): P.ienumerate(A:=list(A), reverse); return A\n    def ienumerate(P,\
    \ A, reverse=False):\n        if reverse:\n            for i,a in enumerate(A):\
    \ A[i] = P.enc(-a, i)\n        else:\n            for i,a in enumerate(A): A[i]\
    \ = P.enc(a, i)\n    def indices(P, A: list[int]): P.iindices(A:=list(A)); return\
    \ A\n    def iindices(P, A):\n        for i,a in enumerate(A): A[i] = P.m&a\n\n\
    \ndef isort_parallel(*L: list, reverse=False):\n    inv, order = [0]*len(L[0]),\
    \ argsort(L[0], reverse=reverse)\n    for i, j in enumerate(order): inv[j] = i\n\
    \    for i, j in enumerate(order):\n        for A in L: A[i], A[j] = A[j], A[i]\n\
    \        order[inv[i]], inv[j] = j, inv[i]\n    return L\nfrom typing import Generic\n\
    \n\nclass list2(Generic[_T1, _T2]):\n    __slots__ = 'A1', 'A2'\n    def __init__(lst,\
    \ A1: list[_T1], A2: list[_T2]): lst.A1, lst.A2 = A1, A2\n    def __len__(lst):\
    \ return len(lst.A1)\n    def __getitem__(lst, i: int): return lst.A1[i], lst.A2[i]\n\
    \    def __setitem__(lst, i: int, v: tuple[_T1, _T2]): lst.A1[i], lst.A2[i] =\
    \ v\n    def __contains__(lst, v: tuple[_T1, _T2]): raise NotImplementedError\n\
    \    def index(lst, v: tuple[_T1, _T2]): raise NotImplementedError\n    def reverse(lst):\
    \ lst.A1.reverse(); lst.A2.reverse()\n    def sort(lst, reverse=False): isort_parallel(lst.A1,\
    \ lst.A2, reverse=reverse)\n    def pop(lst): return lst.A1.pop(), lst.A2.pop()\n\
    \    def append(lst, v: tuple[_T1, _T2]): v1, v2 = v; lst.A1.append(v1); lst.A2.append(v2)\n\
    \    def add(lst, i: int, v: tuple[_T1, _T2]): lst.A1[i] += v[0]; lst.A2[i] +=\
    \ v[1]\n\n\nfrom typing import Callable, Generic, Union\n\nclass SegTree(Generic[_T]):\n\
    \    _lst = list\n    \n    def __init__(seg, op: Callable[[_T, _T], _T], e: _T,\
    \ v: Union[int, list[_T]]) -> None:\n        if isinstance(v, int): n = v; v =\
    \ None\n        else: n = len(v)\n        seg.op, seg.e, seg.n = op, e, n\n  \
    \      seg.log, seg.sz = (log := (n-1).bit_length()+1), (sz := 1 << log)\n   \
    \     if seg._lst is list: seg.d = [e]*(sz<<1)\n        else: seg.d = seg._lst(*([e_]*(sz<<1)\
    \ for e_ in e))\n        if v: seg._build(v)\n\n    def _build(seg, v):\n    \
    \    for i in range(seg.n): seg.d[seg.sz + i] = v[i]\n        for i in range(seg.sz-1,0,-1):\
    \ seg._merge(i, i<<1, i<<1|1)\n    \n    def _merge(seg, i, j, k): seg.d[i] =\
    \ seg.op(seg.d[j], seg.d[k])\n\n    def set(seg, p: int, x: _T) -> None:\n   \
    \     p += seg.sz\n        seg.d[p] = x\n        for _ in range(seg.log):\n  \
    \          p = p^(p&1)\n            seg._merge(p>>1, p, p|1)\n            p >>=\
    \ 1\n    __setitem__ = set\n\n    def get(seg, p: int) -> _T: return seg.d[p+seg.sz]\n\
    \    __getitem__ = get\n\n    def prod(seg, l: int, r: int) -> _T:\n        sml\
    \ = smr = seg.e\n        l, r = l+seg.sz, r+seg.sz\n        while l < r:\n   \
    \         if l&1: sml, l = seg.op(sml, seg.d[l]), l+1\n            if r&1: smr\
    \ = seg.op(seg.d[r:=r-1], smr)\n            l, r = l >> 1, r >> 1\n        return\
    \ seg.op(sml, smr)\n\n    def all_prod(seg) -> _T: return seg.d[1]\n\n    def\
    \ max_right(seg, l: int, f: Callable[[_T], bool]) -> int:\n        assert 0 <=\
    \ l <= seg.n\n        assert f(seg.e)\n        if l == seg.n: return seg.n\n \
    \       l, op, d, sm = l+(sz := seg.sz), seg.op, seg.d, seg.e\n        while True:\n\
    \            while l&1 == 0: l >>= 1\n            if not f(op(sm, d[l])):\n  \
    \              while l < sz:\n                    if f(op(sm, d[l:=l<<1])): sm,\
    \ l = op(sm, d[l]), l+1\n                return l - sz\n            sm, l = op(sm,\
    \ d[l]), l+1\n            if l&-l == l: return seg.n\n\n    def min_left(seg,\
    \ r: int, f: Callable[[_T], bool]) -> int:\n        assert 0 <= r <= seg.n\n \
    \       assert f(seg.e)\n        if r == 0: return 0\n        r, op, d, sm = r+(sz\
    \ := seg.sz), seg.op, seg.d, seg.e\n        while True:\n            r -= 1\n\
    \            while r > 1 and r & 1: r >>= 1\n            if not f(op(d[r], sm)):\n\
    \                while r < sz:\n                    if f(op(d[r:=r<<1|1], sm)):\
    \ sm, r = op(d[r], sm), r-1\n                return r + 1 - sz\n            sm\
    \ = op(d[r], sm)\n            if (r & -r) == r: return 0\n\nclass SegTree2(SegTree[_T]):\n\
    \    _lst = list2\n\nif __name__ == '__main__':\n    \"\"\"\n    Helper for making\
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
    import pytest\nimport random\nfrom operator import add\n\nclass TestSegTree2:\n\
    \    def test_initialization_with_list(self):\n        \"\"\"Test initialization\
    \ with a list of tuples\"\"\"\n        values = [(1, 10), (2, 20), (3, 30), (4,\
    \ 40)]\n        seg = SegTree2(lambda a, b: (a[0] + b[0], a[1] + b[1]), (0, 0),\
    \ values)\n        \n        assert seg.n == 4\n        assert seg[0] == (1, 10)\n\
    \        assert seg[1] == (2, 20)\n        assert seg[2] == (3, 30)\n        assert\
    \ seg[3] == (4, 40)\n\n    def test_initialization_with_size(self):\n        \"\
    \"\"Test initialization with size only\"\"\"\n        seg = SegTree2(lambda a,\
    \ b: (a[0] + b[0], a[1] + b[1]), (0, 0), 5)\n        \n        assert seg.n ==\
    \ 5\n        # All elements should be identity\n        for i in range(5):\n \
    \           assert seg[i] == (0, 0)\n\n    def test_set_and_get(self):\n     \
    \   \"\"\"Test set and get operations\"\"\"\n        seg = SegTree2(lambda a,\
    \ b: (a[0] + b[0], a[1] + b[1]), (0, 0), 4)\n        \n        seg[0] = (1, 10)\n\
    \        seg[1] = (2, 20)\n        seg[2] = (3, 30)\n        seg[3] = (4, 40)\n\
    \        \n        assert seg[0] == (1, 10)\n        assert seg[1] == (2, 20)\n\
    \        assert seg[2] == (3, 30)\n        assert seg[3] == (4, 40)\n\n    def\
    \ test_prod_sum(self):\n        \"\"\"Test prod operation with sum\"\"\"\n   \
    \     values = [(1, 10), (2, 20), (3, 30), (4, 40)]\n        seg = SegTree2(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1]), (0, 0), values)\n        \n        # Test\
    \ various ranges\n        assert seg.prod(0, 4) == (10, 100)  # Sum of all\n \
    \       assert seg.prod(0, 2) == (3, 30)    # First two\n        assert seg.prod(1,\
    \ 3) == (5, 50)    # Middle two\n        assert seg.prod(2, 4) == (7, 70)    #\
    \ Last two\n        assert seg.prod(1, 2) == (2, 20)    # Single element\n   \
    \     assert seg.prod(2, 2) == (0, 0)     # Empty range\n\n    def test_prod_max(self):\n\
    \        \"\"\"Test prod operation with max\"\"\"\n        values = [(3, 30),\
    \ (1, 10), (4, 40), (2, 20)]\n        seg = SegTree2(lambda a, b: (max(a[0], b[0]),\
    \ max(a[1], b[1])), (float('-inf'), float('-inf')), values)\n        \n      \
    \  assert seg.prod(0, 4) == (4, 40)\n        assert seg.prod(0, 2) == (3, 30)\n\
    \        assert seg.prod(1, 3) == (4, 40)\n        assert seg.prod(2, 4) == (4,\
    \ 40)\n\n    def test_prod_min(self):\n        \"\"\"Test prod operation with\
    \ min\"\"\"\n        values = [(3, 30), (1, 10), (4, 40), (2, 20)]\n        seg\
    \ = SegTree2(lambda a, b: (min(a[0], b[0]), min(a[1], b[1])), (float('inf'), float('inf')),\
    \ values)\n        \n        assert seg.prod(0, 4) == (1, 10)\n        assert\
    \ seg.prod(0, 2) == (1, 10)\n        assert seg.prod(1, 3) == (1, 10)\n      \
    \  assert seg.prod(2, 4) == (2, 20)\n\n    def test_all_prod(self):\n        \"\
    \"\"Test all_prod operation\"\"\"\n        values = [(1, 10), (2, 20), (3, 30),\
    \ (4, 40)]\n        seg = SegTree2(lambda a, b: (a[0] + b[0], a[1] + b[1]), (0,\
    \ 0), values)\n        \n        assert seg.all_prod() == (10, 100)\n\n    def\
    \ test_max_right(self):\n        \"\"\"Test max_right operation\"\"\"\n      \
    \  values = [(1, 10), (2, 20), (3, 30), (4, 40)]\n        seg = SegTree2(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1]), (0, 0), values)\n        \n        # Find\
    \ the rightmost position where sum is <= threshold\n        assert seg.max_right(0,\
    \ lambda x: x[0] <= 3) == 2   # Sum up to index 2 is 3\n        assert seg.max_right(0,\
    \ lambda x: x[0] <= 6) == 3   # Sum up to index 3 is 6\n        assert seg.max_right(0,\
    \ lambda x: x[0] <= 10) == 4  # Sum up to index 4 is 10\n        assert seg.max_right(1,\
    \ lambda x: x[0] <= 5) == 3   # Sum from 1 to 3 is 5\n        assert seg.max_right(0,\
    \ lambda x: x[0] <= 0) == 0   # No elements satisfy\n\n    def test_min_left(self):\n\
    \        \"\"\"Test min_left operation\"\"\"\n        values = [(1, 10), (2, 20),\
    \ (3, 30), (4, 40)]\n        seg = SegTree2(lambda a, b: (a[0] + b[0], a[1] +\
    \ b[1]), (0, 0), values)\n        \n        # Find the leftmost position where\
    \ sum from that position is <= threshold\n        assert seg.min_left(4, lambda\
    \ x: x[0] <= 4) == 3    # Only last element\n        assert seg.min_left(4, lambda\
    \ x: x[0] <= 7) == 2    # Last two elements\n        assert seg.min_left(4, lambda\
    \ x: x[0] <= 10) == 0   # All elements\n        assert seg.min_left(3, lambda\
    \ x: x[0] <= 3) == 2    # Elements 2-3\n        assert seg.min_left(4, lambda\
    \ x: x[0] <= 0) == 4    # No elements satisfy\n\n    def test_update_and_query(self):\n\
    \        \"\"\"Test update operations affect queries correctly\"\"\"\n       \
    \ seg = SegTree2(lambda a, b: (a[0] + b[0], a[1] + b[1]), (0, 0), 4)\n       \
    \ \n        # Initial values\n        seg[0] = (1, 10)\n        seg[1] = (2, 20)\n\
    \        seg[2] = (3, 30)\n        seg[3] = (4, 40)\n        \n        assert\
    \ seg.prod(0, 4) == (10, 100)\n        \n        # Update some values\n      \
    \  seg[1] = (5, 50)\n        seg[2] = (6, 60)\n        \n        assert seg.prod(0,\
    \ 4) == (16, 160)\n        assert seg.prod(1, 3) == (11, 110)\n\n    def test_empty_tree(self):\n\
    \        \"\"\"Test empty segment tree\"\"\"\n        seg = SegTree2(lambda a,\
    \ b: (a[0] + b[0], a[1] + b[1]), (0, 0), 0)\n        \n        assert seg.n ==\
    \ 0\n        assert seg.all_prod() == (0, 0)\n\n    def test_single_element(self):\n\
    \        \"\"\"Test segment tree with single element\"\"\"\n        seg = SegTree2(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1]), (0, 0), [(5, 50)])\n        \n        assert\
    \ seg.n == 1\n        assert seg[0] == (5, 50)\n        assert seg.prod(0, 1)\
    \ == (5, 50)\n        assert seg.all_prod() == (5, 50)\n\n    def test_large_tree(self):\n\
    \        \"\"\"Test with larger dataset\"\"\"\n        n = 1000\n        values\
    \ = [(i, i * 10) for i in range(n)]\n        seg = SegTree2(lambda a, b: (a[0]\
    \ + b[0], a[1] + b[1]), (0, 0), values)\n        \n        # Sum of 0..999 = 499500\n\
    \        assert seg.all_prod() == (499500, 4995000)\n        \n        # Sum of\
    \ 0..99 = 4950\n        assert seg.prod(0, 100) == (4950, 49500)\n        \n \
    \       # Update and verify\n        seg[500] = (1000, 10000)\n        expected_sum\
    \ = 499500 - 500 + 1000\n        assert seg.all_prod() == (expected_sum, 4995000\
    \ - 5000 + 10000)\n\n    def test_different_types(self):\n        \"\"\"Test with\
    \ different data types in tuples\"\"\"\n        # String concatenation and list\
    \ concatenation\n        seg = SegTree2(\n            lambda a, b: (a[0] + b[0],\
    \ a[1] + b[1]),\n            (\"\", []),\n            [(\"a\", [1]), (\"b\", [2]),\
    \ (\"c\", [3]), (\"d\", [4])]\n        )\n        \n        assert seg.prod(0,\
    \ 2) == (\"ab\", [1, 2])\n        assert seg.prod(1, 4) == (\"bcd\", [2, 3, 4])\n\
    \        assert seg.all_prod() == (\"abcd\", [1, 2, 3, 4])\n\n    def test_non_commutative_operation(self):\n\
    \        \"\"\"Test with non-commutative operations\"\"\"\n        # Matrix-like\
    \ operation (simplified)\n        def matrix_mult(a, b):\n            # Simplified\
    \ 2x1 matrix multiplication\n            return (a[0] * b[0], a[1] * b[0] + b[1])\n\
    \        \n        seg = SegTree2(matrix_mult, (1, 0), [(2, 1), (3, 2), (4, 3),\
    \ (5, 4)])\n        \n        # Verify non-commutative property affects results\n\
    \        result = seg.prod(0, 2)\n        assert result == (6, 5)  # (2*3, 1*3+2)\n\
    \n    def test_stress_random_operations(self):\n        \"\"\"Stress test with\
    \ random operations\"\"\"\n        random.seed(42)\n        n = 100\n        \n\
    \        # Initialize with random values\n        values = [(random.randint(1,\
    \ 100), random.randint(1, 100)) for _ in range(n)]\n        seg = SegTree2(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1]), (0, 0), values)\n        \n        # Perform\
    \ random operations\n        for _ in range(200):\n            op = random.choice(['update',\
    \ 'query'])\n            \n            if op == 'update':\n                idx\
    \ = random.randint(0, n-1)\n                new_val = (random.randint(1, 100),\
    \ random.randint(1, 100))\n                seg[idx] = new_val\n              \
    \  values[idx] = new_val\n            else:\n                l = random.randint(0,\
    \ n-1)\n                r = random.randint(l, n)\n                \n         \
    \       # Verify against naive calculation\n                expected = (0, 0)\n\
    \                for i in range(l, r):\n                    expected = (expected[0]\
    \ + values[i][0], expected[1] + values[i][1])\n                \n            \
    \    assert seg.prod(l, r) == expected\n\nfrom cp_library.ds.tree.seg.segtree2_cls\
    \ import SegTree2\n\nif __name__ == '__main__':\n    from cp_library.test.unittest_helper\
    \ import run_verification_helper_unittest\n    run_verification_helper_unittest()"
  dependsOn:
  - cp_library/ds/tree/seg/segtree2_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/ds/list/list2_cls.py
  - cp_library/ds/tree/seg/segtree_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: true
  path: test/unittests/ds/tree/seg/segtree2_cls_test.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/tree/seg/segtree2_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/tree/seg/segtree2_cls_test.py
- /verify/test/unittests/ds/tree/seg/segtree2_cls_test.py.html
title: test/unittests/ds/tree/seg/segtree2_cls_test.py
---
