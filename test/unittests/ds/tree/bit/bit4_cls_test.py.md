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
    path: cp_library/test/unittest_helper.py
    title: cp_library/test/unittest_helper.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
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
    \ typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U');\
    \ _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4');\
    \ _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\
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
    \        \"\"\"\n        Run a dummy AOJ ITP1_1_A test for verification-helper\
    \ compatibility.\n        \n        This function should be called in the __main__\
    \ block of unittest files\n        that need to be compatible with verification-helper.\n\
    \        \n        The function:\n        1. Prints \"Hello World\" (AOJ ITP1_1_A\
    \ solution)\n        2. Runs pytest for the calling test file\n        3. Exits\
    \ with the pytest result code\n        \"\"\"\n        import sys\n        \n\
    \        # Print \"Hello World\" for AOJ ITP1_1_A problem\n        print(\"Hello\
    \ World\")\n        \n        import io\n        from contextlib import redirect_stdout,\
    \ redirect_stderr\n    \n        # Capture all output during test execution\n\
    \        output = io.StringIO()\n        with redirect_stdout(output), redirect_stderr(output):\n\
    \            # Get the calling module's file path\n            frame = sys._getframe(1)\n\
    \            test_file = frame.f_globals.get('__file__')\n            if test_file\
    \ is None:\n                test_file = sys.argv[0]\n            result = pytest.main([test_file])\n\
    \        \n        if result != 0: \n            print(output.getvalue())\n  \
    \      sys.exit(result)\n    run_verification_helper_unittest()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
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
    \nfrom cp_library.ds.tree.bit.bit4_cls import BIT4\n\nif __name__ == '__main__':\n\
    \    from cp_library.test.unittest_helper import run_verification_helper_unittest\n\
    \    run_verification_helper_unittest()"
  dependsOn:
  - cp_library/ds/tree/bit/bit4_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/ds/list/list4_cls.py
  - cp_library/ds/tree/bit/bit_base_cls.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: true
  path: test/unittests/ds/tree/bit/bit4_cls_test.py
  requiredBy: []
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/tree/bit/bit4_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/tree/bit/bit4_cls_test.py
- /verify/test/unittests/ds/tree/bit/bit4_cls_test.py.html
title: test/unittests/ds/tree/bit/bit4_cls_test.py
---
