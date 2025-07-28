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
    path: cp_library/ds/tree/bit/bit2_cls.py
    title: cp_library/ds/tree/bit/bit2_cls.py
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
    \nimport pytest\nimport random\n\nclass TestBIT2:\n    def test_initialization_with_list(self):\n\
    \        \"\"\"Test initialization with a list of tuples\"\"\"\n        values\
    \ = [(1, 10), (2, 20), (3, 30), (4, 40)]\n        bit = BIT2(values)\n       \
    \ \n        assert len(bit) == 4\n        assert bit[0] == (1, 10)\n        assert\
    \ bit[1] == (2, 20)\n        assert bit[2] == (3, 30)\n        assert bit[3] ==\
    \ (4, 40)\n\n    def test_initialization_with_size(self):\n        \"\"\"Test\
    \ initialization with size and zero value\"\"\"\n        bit = BIT2(5, (0, 0))\n\
    \        \n        assert len(bit) == 5\n        # All elements should be zero\n\
    \        for i in range(5):\n            assert bit[i] == (0, 0)\n\n    def test_add_and_sum(self):\n\
    \        \"\"\"Test add and sum operations\"\"\"\n        bit = BIT2(4, (0, 0))\n\
    \        \n        bit.add(0, (1, 10))\n        bit.add(1, (2, 20))\n        bit.add(2,\
    \ (3, 30))\n        bit.add(3, (4, 40))\n        \n        assert bit.sum(1) ==\
    \ (1, 10)\n        assert bit.sum(2) == (3, 30)\n        assert bit.sum(3) ==\
    \ (6, 60)\n        assert bit.sum(4) == (10, 100)\n\n    def test_sum_range(self):\n\
    \        \"\"\"Test range sum operations\"\"\"\n        values = [(1, 10), (2,\
    \ 20), (3, 30), (4, 40)]\n        bit = BIT2(values)\n        \n        assert\
    \ bit.sum_range(0, 2) == (3, 30)  # Sum of first two\n        assert bit.sum_range(1,\
    \ 3) == (5, 50)  # Sum of middle two\n        assert bit.sum_range(2, 4) == (7,\
    \ 70)  # Sum of last two\n        assert bit.sum_range(0, 4) == (10, 100)  # Sum\
    \ of all\n        assert bit.sum_range(1, 1) == (0, 0)   # Empty range\n\n   \
    \ def test_set_and_get(self):\n        \"\"\"Test set and get operations\"\"\"\
    \n        bit = BIT2(4, (0, 0))\n        \n        bit[0] = (1, 10)\n        bit[1]\
    \ = (2, 20)\n        bit[2] = (3, 30)\n        bit[3] = (4, 40)\n        \n  \
    \      assert bit[0] == (1, 10)\n        assert bit[1] == (2, 20)\n        assert\
    \ bit[2] == (3, 30)\n        assert bit[3] == (4, 40)\n\n    def test_update_and_query(self):\n\
    \        \"\"\"Test update operations affect queries correctly\"\"\"\n       \
    \ bit = BIT2(4, (0, 0))\n        \n        # Initial values\n        bit[0] =\
    \ (1, 10)\n        bit[1] = (2, 20)\n        bit[2] = (3, 30)\n        bit[3]\
    \ = (4, 40)\n        \n        assert bit.sum(4) == (10, 100)\n        \n    \
    \    # Update some values\n        bit[1] = (5, 50)\n        bit[2] = (6, 60)\n\
    \        \n        assert bit.sum(4) == (16, 160)\n        assert bit.sum_range(1,\
    \ 3) == (11, 110)\n\n    def test_build_functionality(self):\n        \"\"\"Test\
    \ that build creates correct BIT structure\"\"\"\n        values = [(1, 10), (2,\
    \ 20), (3, 30), (4, 40)]\n        bit = BIT2(values)\n        \n        # Test\
    \ various range sums\n        assert bit.sum_range(0, 1) == (1, 10)\n        assert\
    \ bit.sum_range(0, 2) == (3, 30)\n        assert bit.sum_range(1, 4) == (9, 90)\n\
    \        \n        # Test individual elements\n        for i, expected in enumerate(values):\n\
    \            assert bit[i] == expected\n\n    def test_prelist(self):\n      \
    \  \"\"\"Test prelist operation\"\"\"\n        values = [(1, 10), (2, 20), (3,\
    \ 30), (4, 40)]\n        bit = BIT2(values)\n        \n        pre = bit.prelist()\n\
    \        \n        # Should have n+1 elements (including 0 at start)\n       \
    \ assert len(pre) == 5\n        assert pre[0] == (0, 0)\n        assert pre[1]\
    \ == (1, 10)\n        assert pre[2] == (3, 30)\n        assert pre[3] == (6, 60)\n\
    \        assert pre[4] == (10, 100)\n\n    def test_bisect_operations(self):\n\
    \        \"\"\"Test bisect_left and bisect_right operations\"\"\"\n        values\
    \ = [(1, 10), (2, 20), (3, 30), (4, 40)]\n        bit = BIT2(values)\n       \
    \ \n        # Test bisect_right - finds rightmost position where cumsum <= v\n\
    \        assert bit.bisect_right((0, 0)) == 0   # cumsum (0, 0)\n        assert\
    \ bit.bisect_right((1, 10)) == 1   # cumsum (1, 10)\n        assert bit.bisect_right((3,\
    \ 30)) == 2   # cumsum (3, 30)\n        assert bit.bisect_right((6, 60)) == 3\
    \   # cumsum (6, 60)\n        assert bit.bisect_right((10, 100)) == 4  # cumsum\
    \ (10, 100)\n        assert bit.bisect_right((15, 150)) == 4  # cumsum still (10,\
    \ 100)\n        \n        # Test bisect_left - finds leftmost position where cumsum\
    \ >= v\n        assert bit.bisect_left((0, 0)) == -1\n        assert bit.bisect_left((1,\
    \ 10)) == 0   # sum(1)=(1,10) >= (1,10)\n        assert bit.bisect_left((4, 40))\
    \ == 2   # sum(3)=(6,60) >= (4,40)  \n        assert bit.bisect_left((7, 70))\
    \ == 3   # sum(4)=(10,100) >= (7,70)\n        assert bit.bisect_left((11, 110))\
    \ == 4  # no cumsum >= (11,110)\n\n    def test_empty_bit(self):\n        \"\"\
    \"Test BIT with size 0\"\"\"\n        bit = BIT2(0, (0, 0))\n        \n      \
    \  assert len(bit) == 0\n        assert bit.sum(0) == (0, 0)\n\n    def test_single_element(self):\n\
    \        \"\"\"Test BIT with single element\"\"\"\n        bit = BIT2([(5, 50)])\n\
    \        \n        assert len(bit) == 1\n        assert bit[0] == (5, 50)\n  \
    \      assert bit.sum(1) == (5, 50)\n        assert bit.sum_range(0, 1) == (5,\
    \ 50)\n\n    def test_large_bit(self):\n        \"\"\"Test with larger dataset\"\
    \"\"\n        n = 1000\n        values = [(i, i * 10) for i in range(n)]\n   \
    \     bit = BIT2(values)\n        \n        # Sum of 0..999 = 499500\n       \
    \ assert bit.sum(n) == (499500, 4995000)\n        \n        # Sum of 0..99 = 4950\n\
    \        assert bit.sum(100) == (4950, 49500)\n        \n        # Update and\
    \ verify\n        bit[500] = (1000, 10000)\n        expected_sum = 499500 - 500\
    \ + 1000\n        assert bit.sum(n) == (expected_sum, 4995000 - 5000 + 10000)\n\
    \n    def test_negative_values(self):\n        \"\"\"Test BIT with negative values\"\
    \"\"\n        values = [(-1, -10), (2, 20), (-3, -30), (4, 40)]\n        bit =\
    \ BIT2(values)\n        \n        assert bit.sum(4) == (2, 20)\n        assert\
    \ bit.sum_range(0, 2) == (1, 10)\n        assert bit.sum_range(2, 4) == (1, 10)\n\
    \n    def test_zero_values(self):\n        \"\"\"Test BIT with zero values\"\"\
    \"\n        values = [(0, 0), (1, 10), (0, 0), (2, 20)]\n        bit = BIT2(values)\n\
    \        \n        assert bit.sum(4) == (3, 30)\n        assert bit[0] == (0,\
    \ 0)\n        assert bit[2] == (0, 0)\n\n    def test_stress_random_operations(self):\n\
    \        \"\"\"Stress test with random operations\"\"\"\n        random.seed(42)\n\
    \        n = 100\n        \n        # Initialize with zeros\n        bit = BIT2(n,\
    \ (0, 0))\n        naive = [(0, 0)] * n\n        \n        # Perform random operations\n\
    \        for _ in range(200):\n            op = random.choice(['add', 'set', 'query'])\n\
    \            \n            if op == 'add':\n                idx = random.randint(0,\
    \ n-1)\n                val = (random.randint(-100, 100), random.randint(-100,\
    \ 100))\n                bit.add(idx, val)\n                naive[idx] = (naive[idx][0]\
    \ + val[0], naive[idx][1] + val[1])\n                \n            elif op ==\
    \ 'set':\n                idx = random.randint(0, n-1)\n                val =\
    \ (random.randint(-100, 100), random.randint(-100, 100))\n                bit[idx]\
    \ = val\n                naive[idx] = val\n                \n            else:\
    \  # query\n                if random.random() < 0.5:\n                    # Test\
    \ sum\n                    k = random.randint(1, n)\n                    expected\
    \ = (sum(naive[i][0] for i in range(k)), \n                               sum(naive[i][1]\
    \ for i in range(k)))\n                    assert bit.sum(k) == expected\n   \
    \             else:\n                    # Test range sum\n                  \
    \  l = random.randint(0, n-1)\n                    r = random.randint(l, n)\n\
    \                    expected = (sum(naive[i][0] for i in range(l, r)), \n   \
    \                            sum(naive[i][1] for i in range(l, r)))\n        \
    \            assert bit.sum_range(l, r) == expected\n\n    def test_different_types(self):\n\
    \        \"\"\"Test with different data types in tuples\"\"\"\n        # Float\
    \ values\n        values = [(1.5, 10.5), (2.5, 20.5), (3.5, 30.5), (4.5, 40.5)]\n\
    \        bit = BIT2(values)\n        \n        assert bit.sum(2) == (4.0, 31.0)\n\
    \        assert bit.sum_range(1, 3) == (6.0, 51.0)\n\n'''\n\u257A\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2513            \n            \u2503   \
    \                                 7 \u2503            \n            \u2517\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B     \
    \       \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513                 \u2502\
    \              \n            \u2503                3 \u2503\u25C4\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2524              \n            \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B     \
    \            \u2502              \n            \u250F\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2513       \u2502  \u250F\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2513       \u2502              \n            \u2503      1 \u2503\
    \u25C4\u2500\u2500\u2500\u2500\u2500\u2500\u2524  \u2503      5 \u2503\u25C4\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2524              \n            \u2517\u2501\u2501\
    \u2501\u2501\u2501\u2501\u252F\u2501\u251B       \u2502  \u2517\u2501\u2501\u2501\
    \u2501\u2501\u2501\u252F\u2501\u251B       \u2502              \n            \u250F\
    \u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\
    \u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502     \
    \         \n            \u2503 0 \u2503\u25C4\u2500\u2524  \u2503 2 \u2503\u25C4\
    \u2500\u2524  \u2503 4 \u2503\u25C4\u2500\u2524  \u2503 6 \u2503\u25C4\u2500\u2524\
    \              \n            \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\
    \u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\
    \u252F\u2501\u251B  \u2502              \n              \u2502    \u2502    \u2502\
    \    \u2502    \u2502    \u2502    \u2502    \u2502              \n          \
    \    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC\
    \              \n            \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\
    \u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\
    \u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\
    \u250F\u2501\u2501\u2501\u2513            \n            \u2503 0 \u2503\u2503\
    \ 1 \u2503\u2503 2 \u2503\u2503 3 \u2503\u2503 4 \u2503\u2503 5 \u2503\u2503 6\
    \ \u2503\u2503 7 \u2503            \n            \u2517\u2501\u2501\u2501\u251B\
    \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\
    \u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\
    \u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B            \n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n           Data\
    \ Structure - Tree - Binary Index Tree            \n'''\n\n\n\n\ndef argsort(A:\
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
    from typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U');\
    \ _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4');\
    \ _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\nclass list2(Generic[_T1, _T2]):\n\
    \    __slots__ = 'A1', 'A2'\n    def __init__(lst, A1: list[_T1], A2: list[_T2]):\
    \ lst.A1, lst.A2 = A1, A2\n    def __len__(lst): return len(lst.A1)\n    def __getitem__(lst,\
    \ i: int): return lst.A1[i], lst.A2[i]\n    def __setitem__(lst, i: int, v: tuple[_T1,\
    \ _T2]): lst.A1[i], lst.A2[i] = v\n    def __contains__(lst, v: tuple[_T1, _T2]):\
    \ raise NotImplementedError\n    def index(lst, v: tuple[_T1, _T2]): raise NotImplementedError\n\
    \    def reverse(lst): lst.A1.reverse(); lst.A2.reverse()\n    def sort(lst, reverse=False):\
    \ isort_parallel(lst.A1, lst.A2, reverse=reverse)\n    def pop(lst): return lst.A1.pop(),\
    \ lst.A2.pop()\n    def append(lst, v: tuple[_T1, _T2]): v1, v2 = v; lst.A1.append(v1);\
    \ lst.A2.append(v2)\n    def add(lst, i: int, v: tuple[_T1, _T2]): lst.A1[i] +=\
    \ v[0]; lst.A2[i] += v[1]\nfrom typing import Generic, Union, Callable, Optional\n\
    \nclass BITBase(Generic[_T]):\n    _lst = list\n    K: int = 1\n    \n    def\
    \ __init__(bit, v: Union[int, list[_T]], e: _T = None) -> None:\n        if isinstance(v,\
    \ int):\n            bit._n = v\n            if bit._lst is list:\n          \
    \      bit._d = [e]*v if e is not None else [0]*v\n            elif e is not None:\n\
    \                bit._d = bit._lst(*([e_]*v for e_ in e))\n            else:\n\
    \                bit._d = bit._lst(*([0]*v for _ in range(bit.K)))\n        else:\n\
    \            bit.build(v)\n        bit.e = e if e is not None else (0 if bit._lst\
    \ is list else tuple(0 for _ in range(bit.K)))\n        bit._lb = 1 << bit._n.bit_length()\n\
    \n    def build(bit, data: list[_T]):\n        bit._n = len(data)\n        if\
    \ bit._lst is list:\n            bit._d = bit._lst(data)\n        else:\n    \
    \        bit._d = bit._lst(*([data[i][j] for i in range(len(data))] for j in range(len(data[0]))))\n\
    \        for i in range(bit._n):\n            if (r := i | i + 1) < bit._n:\n\
    \                bit._add(r, bit._d[i])\n\n    def _add(bit, i: int, x: _T) ->\
    \ None:\n        bit._d[i] = bit._op(bit._d[i], x)\n    \n    def _op(bit, a:\
    \ _T, b: _T) -> _T:\n        return a + b\n    \n    def _sub(bit, a: _T, b: _T)\
    \ -> _T:\n        return a - b\n\n    def add(bit, i: int, x: _T) -> None:\n \
    \       while i < bit._n: bit._add(i, x); i |= i + 1\n\n    def sum(bit, n: int)\
    \ -> _T:\n        s = bit.e\n        while n: s, n = bit._op(s, bit._d[n - 1]),\
    \ n & n - 1\n        return s\n\n    def sum_range(bit, l: int, r: int) -> _T:\n\
    \        s = bit.e\n        while r: s, r = bit._op(s, bit._d[r - 1]), r & r -\
    \ 1\n        while l: s, l = bit._sub(s, bit._d[l - 1]), l & l - 1\n        return\
    \ s\n\n    def __len__(bit) -> int: return bit._n\n\n    def __getitem__(bit,\
    \ i: int) -> _T:\n        s, l = bit._d[i], i & (i + 1)\n        while l != i:\
    \ s, i = bit._sub(s, bit._d[i - 1]), i - (i & -i)\n        return s\n\n    get\
    \ = __getitem__\n\n    def __setitem__(bit, i: int, x: _T) -> None:\n        bit.add(i,\
    \ bit._sub(x, bit[i]))\n\n    set = __setitem__\n\n    def prelist(bit) -> list[_T]:\n\
    \        pre = [bit.e] + bit._d[:] if bit._lst is list else bit._lst(*([e_] *\
    \ (bit._n + 1) for e_ in bit.e))\n        for i in range(bit._n): pre[i+1] = bit._d[i]\n\
    \        for i in range(bit._n + 1):\n            if i & i - 1 < bit._n + 1:\n\
    \                pre[i] = bit._op(pre[i], pre[i & i - 1])\n        return pre\n\
    \n    def bisect_left(bit, v, key: Optional[Callable] = None) -> int:\n      \
    \  i = 0\n        s = bit.e\n        if v <= s: return -1\n        m = bit._lb\n\
    \        \n        if key:\n            while m := m >> 1:\n                if\
    \ (ni := m | i) <= bit._n and key(ns := bit._op(s, bit._d[ni - 1])) < v:\n   \
    \                 s, i = ns, ni\n        else:\n            while m := m >> 1:\n\
    \                if (ni := m | i) <= bit._n and (ns := bit._op(s, bit._d[ni -\
    \ 1])) < v:\n                    s, i = ns, ni\n        return i\n\n    def bisect_right(bit,\
    \ v, key: Optional[Callable] = None) -> int:\n        i = 0\n        s = bit.e\n\
    \        m = bit._lb\n        \n        if key:\n            while m := m >> 1:\n\
    \                if (ni := m | i) <= bit._n and key(ns := bit._op(s, bit._d[ni\
    \ - 1])) <= v:\n                    s, i = ns, ni\n        else:\n           \
    \ while m := m >> 1:\n                if (ni := m | i) <= bit._n and (ns := bit._op(s,\
    \ bit._d[ni - 1])) <= v:\n                    s, i = ns, ni\n        return i\n\
    \nclass BIT2(BITBase[tuple[int,int]]):\n    _lst = list2\n    K = 2\n    def _add(bit,\
    \ i, x) -> None: bit._d.add(i, x)\n    def _op(bit, a, b): return a[0] + b[0],\
    \ a[1] + b[1]\n    def _sub(bit, a, b): return a[0] - b[0], a[1] - b[1]\n\nif\
    \ __name__ == '__main__':\n    \"\"\"\n    Helper for making unittest files compatible\
    \ with verification-helper.\n    \n    This module provides a helper function\
    \ to run a dummy Library Checker test\n    so that unittest files can be verified\
    \ by oj-verify.\n    \"\"\"\n    \n    def run_verification_helper_unittest():\n\
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
    \nimport pytest\nimport random\n\nclass TestBIT2:\n    def test_initialization_with_list(self):\n\
    \        \"\"\"Test initialization with a list of tuples\"\"\"\n        values\
    \ = [(1, 10), (2, 20), (3, 30), (4, 40)]\n        bit = BIT2(values)\n       \
    \ \n        assert len(bit) == 4\n        assert bit[0] == (1, 10)\n        assert\
    \ bit[1] == (2, 20)\n        assert bit[2] == (3, 30)\n        assert bit[3] ==\
    \ (4, 40)\n\n    def test_initialization_with_size(self):\n        \"\"\"Test\
    \ initialization with size and zero value\"\"\"\n        bit = BIT2(5, (0, 0))\n\
    \        \n        assert len(bit) == 5\n        # All elements should be zero\n\
    \        for i in range(5):\n            assert bit[i] == (0, 0)\n\n    def test_add_and_sum(self):\n\
    \        \"\"\"Test add and sum operations\"\"\"\n        bit = BIT2(4, (0, 0))\n\
    \        \n        bit.add(0, (1, 10))\n        bit.add(1, (2, 20))\n        bit.add(2,\
    \ (3, 30))\n        bit.add(3, (4, 40))\n        \n        assert bit.sum(1) ==\
    \ (1, 10)\n        assert bit.sum(2) == (3, 30)\n        assert bit.sum(3) ==\
    \ (6, 60)\n        assert bit.sum(4) == (10, 100)\n\n    def test_sum_range(self):\n\
    \        \"\"\"Test range sum operations\"\"\"\n        values = [(1, 10), (2,\
    \ 20), (3, 30), (4, 40)]\n        bit = BIT2(values)\n        \n        assert\
    \ bit.sum_range(0, 2) == (3, 30)  # Sum of first two\n        assert bit.sum_range(1,\
    \ 3) == (5, 50)  # Sum of middle two\n        assert bit.sum_range(2, 4) == (7,\
    \ 70)  # Sum of last two\n        assert bit.sum_range(0, 4) == (10, 100)  # Sum\
    \ of all\n        assert bit.sum_range(1, 1) == (0, 0)   # Empty range\n\n   \
    \ def test_set_and_get(self):\n        \"\"\"Test set and get operations\"\"\"\
    \n        bit = BIT2(4, (0, 0))\n        \n        bit[0] = (1, 10)\n        bit[1]\
    \ = (2, 20)\n        bit[2] = (3, 30)\n        bit[3] = (4, 40)\n        \n  \
    \      assert bit[0] == (1, 10)\n        assert bit[1] == (2, 20)\n        assert\
    \ bit[2] == (3, 30)\n        assert bit[3] == (4, 40)\n\n    def test_update_and_query(self):\n\
    \        \"\"\"Test update operations affect queries correctly\"\"\"\n       \
    \ bit = BIT2(4, (0, 0))\n        \n        # Initial values\n        bit[0] =\
    \ (1, 10)\n        bit[1] = (2, 20)\n        bit[2] = (3, 30)\n        bit[3]\
    \ = (4, 40)\n        \n        assert bit.sum(4) == (10, 100)\n        \n    \
    \    # Update some values\n        bit[1] = (5, 50)\n        bit[2] = (6, 60)\n\
    \        \n        assert bit.sum(4) == (16, 160)\n        assert bit.sum_range(1,\
    \ 3) == (11, 110)\n\n    def test_build_functionality(self):\n        \"\"\"Test\
    \ that build creates correct BIT structure\"\"\"\n        values = [(1, 10), (2,\
    \ 20), (3, 30), (4, 40)]\n        bit = BIT2(values)\n        \n        # Test\
    \ various range sums\n        assert bit.sum_range(0, 1) == (1, 10)\n        assert\
    \ bit.sum_range(0, 2) == (3, 30)\n        assert bit.sum_range(1, 4) == (9, 90)\n\
    \        \n        # Test individual elements\n        for i, expected in enumerate(values):\n\
    \            assert bit[i] == expected\n\n    def test_prelist(self):\n      \
    \  \"\"\"Test prelist operation\"\"\"\n        values = [(1, 10), (2, 20), (3,\
    \ 30), (4, 40)]\n        bit = BIT2(values)\n        \n        pre = bit.prelist()\n\
    \        \n        # Should have n+1 elements (including 0 at start)\n       \
    \ assert len(pre) == 5\n        assert pre[0] == (0, 0)\n        assert pre[1]\
    \ == (1, 10)\n        assert pre[2] == (3, 30)\n        assert pre[3] == (6, 60)\n\
    \        assert pre[4] == (10, 100)\n\n    def test_bisect_operations(self):\n\
    \        \"\"\"Test bisect_left and bisect_right operations\"\"\"\n        values\
    \ = [(1, 10), (2, 20), (3, 30), (4, 40)]\n        bit = BIT2(values)\n       \
    \ \n        # Test bisect_right - finds rightmost position where cumsum <= v\n\
    \        assert bit.bisect_right((0, 0)) == 0   # cumsum (0, 0)\n        assert\
    \ bit.bisect_right((1, 10)) == 1   # cumsum (1, 10)\n        assert bit.bisect_right((3,\
    \ 30)) == 2   # cumsum (3, 30)\n        assert bit.bisect_right((6, 60)) == 3\
    \   # cumsum (6, 60)\n        assert bit.bisect_right((10, 100)) == 4  # cumsum\
    \ (10, 100)\n        assert bit.bisect_right((15, 150)) == 4  # cumsum still (10,\
    \ 100)\n        \n        # Test bisect_left - finds leftmost position where cumsum\
    \ >= v\n        assert bit.bisect_left((0, 0)) == -1\n        assert bit.bisect_left((1,\
    \ 10)) == 0   # sum(1)=(1,10) >= (1,10)\n        assert bit.bisect_left((4, 40))\
    \ == 2   # sum(3)=(6,60) >= (4,40)  \n        assert bit.bisect_left((7, 70))\
    \ == 3   # sum(4)=(10,100) >= (7,70)\n        assert bit.bisect_left((11, 110))\
    \ == 4  # no cumsum >= (11,110)\n\n    def test_empty_bit(self):\n        \"\"\
    \"Test BIT with size 0\"\"\"\n        bit = BIT2(0, (0, 0))\n        \n      \
    \  assert len(bit) == 0\n        assert bit.sum(0) == (0, 0)\n\n    def test_single_element(self):\n\
    \        \"\"\"Test BIT with single element\"\"\"\n        bit = BIT2([(5, 50)])\n\
    \        \n        assert len(bit) == 1\n        assert bit[0] == (5, 50)\n  \
    \      assert bit.sum(1) == (5, 50)\n        assert bit.sum_range(0, 1) == (5,\
    \ 50)\n\n    def test_large_bit(self):\n        \"\"\"Test with larger dataset\"\
    \"\"\n        n = 1000\n        values = [(i, i * 10) for i in range(n)]\n   \
    \     bit = BIT2(values)\n        \n        # Sum of 0..999 = 499500\n       \
    \ assert bit.sum(n) == (499500, 4995000)\n        \n        # Sum of 0..99 = 4950\n\
    \        assert bit.sum(100) == (4950, 49500)\n        \n        # Update and\
    \ verify\n        bit[500] = (1000, 10000)\n        expected_sum = 499500 - 500\
    \ + 1000\n        assert bit.sum(n) == (expected_sum, 4995000 - 5000 + 10000)\n\
    \n    def test_negative_values(self):\n        \"\"\"Test BIT with negative values\"\
    \"\"\n        values = [(-1, -10), (2, 20), (-3, -30), (4, 40)]\n        bit =\
    \ BIT2(values)\n        \n        assert bit.sum(4) == (2, 20)\n        assert\
    \ bit.sum_range(0, 2) == (1, 10)\n        assert bit.sum_range(2, 4) == (1, 10)\n\
    \n    def test_zero_values(self):\n        \"\"\"Test BIT with zero values\"\"\
    \"\n        values = [(0, 0), (1, 10), (0, 0), (2, 20)]\n        bit = BIT2(values)\n\
    \        \n        assert bit.sum(4) == (3, 30)\n        assert bit[0] == (0,\
    \ 0)\n        assert bit[2] == (0, 0)\n\n    def test_stress_random_operations(self):\n\
    \        \"\"\"Stress test with random operations\"\"\"\n        random.seed(42)\n\
    \        n = 100\n        \n        # Initialize with zeros\n        bit = BIT2(n,\
    \ (0, 0))\n        naive = [(0, 0)] * n\n        \n        # Perform random operations\n\
    \        for _ in range(200):\n            op = random.choice(['add', 'set', 'query'])\n\
    \            \n            if op == 'add':\n                idx = random.randint(0,\
    \ n-1)\n                val = (random.randint(-100, 100), random.randint(-100,\
    \ 100))\n                bit.add(idx, val)\n                naive[idx] = (naive[idx][0]\
    \ + val[0], naive[idx][1] + val[1])\n                \n            elif op ==\
    \ 'set':\n                idx = random.randint(0, n-1)\n                val =\
    \ (random.randint(-100, 100), random.randint(-100, 100))\n                bit[idx]\
    \ = val\n                naive[idx] = val\n                \n            else:\
    \  # query\n                if random.random() < 0.5:\n                    # Test\
    \ sum\n                    k = random.randint(1, n)\n                    expected\
    \ = (sum(naive[i][0] for i in range(k)), \n                               sum(naive[i][1]\
    \ for i in range(k)))\n                    assert bit.sum(k) == expected\n   \
    \             else:\n                    # Test range sum\n                  \
    \  l = random.randint(0, n-1)\n                    r = random.randint(l, n)\n\
    \                    expected = (sum(naive[i][0] for i in range(l, r)), \n   \
    \                            sum(naive[i][1] for i in range(l, r)))\n        \
    \            assert bit.sum_range(l, r) == expected\n\n    def test_different_types(self):\n\
    \        \"\"\"Test with different data types in tuples\"\"\"\n        # Float\
    \ values\n        values = [(1.5, 10.5), (2.5, 20.5), (3.5, 30.5), (4.5, 40.5)]\n\
    \        bit = BIT2(values)\n        \n        assert bit.sum(2) == (4.0, 31.0)\n\
    \        assert bit.sum_range(1, 3) == (6.0, 51.0)\n\nfrom cp_library.ds.tree.bit.bit2_cls\
    \ import BIT2\n\nif __name__ == '__main__':\n    from cp_library.test.unittest_helper\
    \ import run_verification_helper_unittest\n    run_verification_helper_unittest()"
  dependsOn:
  - cp_library/ds/tree/bit/bit2_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/ds/list/list2_cls.py
  - cp_library/ds/tree/bit/bit_base_cls.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: true
  path: test/unittests/ds/tree/bit/bit2_cls_test.py
  requiredBy: []
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/tree/bit/bit2_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/tree/bit/bit2_cls_test.py
- /verify/test/unittests/ds/tree/bit/bit2_cls_test.py.html
title: test/unittests/ds/tree/bit/bit2_cls_test.py
---
