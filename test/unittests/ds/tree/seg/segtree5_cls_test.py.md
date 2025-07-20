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
    path: cp_library/ds/list/list5_cls.py
    title: cp_library/ds/list/list5_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/seg/segtree5_cls.py
    title: cp_library/ds/tree/seg/segtree5_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/seg/segtree_cls.py
    title: cp_library/ds/tree/seg/segtree_cls.py
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
    \nimport pytest\nimport random\n\nclass TestSegTree5:\n    def test_initialization_with_list(self):\n\
    \        \"\"\"Test initialization with a list of 5-tuples\"\"\"\n        values\
    \ = [(1, 10, 100, 1000, 10000), (2, 20, 200, 2000, 20000), (3, 30, 300, 3000,\
    \ 30000), (4, 40, 400, 4000, 40000)]\n        seg = SegTree5(lambda a, b: (a[0]\
    \ + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0, 0, 0, 0, 0),\
    \ values)\n        \n        assert seg.n == 4\n        assert seg[0] == (1, 10,\
    \ 100, 1000, 10000)\n        assert seg[1] == (2, 20, 200, 2000, 20000)\n    \
    \    assert seg[2] == (3, 30, 300, 3000, 30000)\n        assert seg[3] == (4,\
    \ 40, 400, 4000, 40000)\n\n    def test_initialization_with_size(self):\n    \
    \    \"\"\"Test initialization with size only\"\"\"\n        seg = SegTree5(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0,\
    \ 0, 0, 0, 0), 5)\n        \n        assert seg.n == 5\n        # All elements\
    \ should be identity\n        for i in range(5):\n            assert seg[i] ==\
    \ (0, 0, 0, 0, 0)\n\n    def test_set_and_get(self):\n        \"\"\"Test set and\
    \ get operations\"\"\"\n        seg = SegTree5(lambda a, b: (a[0] + b[0], a[1]\
    \ + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0, 0, 0, 0, 0), 4)\n      \
    \  \n        seg[0] = (1, 10, 100, 1000, 10000)\n        seg[1] = (2, 20, 200,\
    \ 2000, 20000)\n        seg[2] = (3, 30, 300, 3000, 30000)\n        seg[3] = (4,\
    \ 40, 400, 4000, 40000)\n        \n        assert seg[0] == (1, 10, 100, 1000,\
    \ 10000)\n        assert seg[1] == (2, 20, 200, 2000, 20000)\n        assert seg[2]\
    \ == (3, 30, 300, 3000, 30000)\n        assert seg[3] == (4, 40, 400, 4000, 40000)\n\
    \n    def test_prod_sum(self):\n        \"\"\"Test prod operation with sum\"\"\
    \"\n        values = [(1, 10, 100, 1000, 10000), (2, 20, 200, 2000, 20000), (3,\
    \ 30, 300, 3000, 30000), (4, 40, 400, 4000, 40000)]\n        seg = SegTree5(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0,\
    \ 0, 0, 0, 0), values)\n        \n        # Test various ranges\n        assert\
    \ seg.prod(0, 4) == (10, 100, 1000, 10000, 100000)  # Sum of all\n        assert\
    \ seg.prod(0, 2) == (3, 30, 300, 3000, 30000)       # First two\n        assert\
    \ seg.prod(1, 3) == (5, 50, 500, 5000, 50000)       # Middle two\n        assert\
    \ seg.prod(2, 4) == (7, 70, 700, 7000, 70000)       # Last two\n        assert\
    \ seg.prod(1, 2) == (2, 20, 200, 2000, 20000)       # Single element\n       \
    \ assert seg.prod(2, 2) == (0, 0, 0, 0, 0)                 # Empty range\n\n \
    \   def test_prod_max(self):\n        \"\"\"Test prod operation with max\"\"\"\
    \n        values = [(3, 30, 300, 3000, 30000), (1, 10, 100, 1000, 10000), (4,\
    \ 40, 400, 4000, 40000), (2, 20, 200, 2000, 20000)]\n        seg = SegTree5(\n\
    \            lambda a, b: (max(a[0], b[0]), max(a[1], b[1]), max(a[2], b[2]),\
    \ max(a[3], b[3]), max(a[4], b[4])), \n            (float('-inf'), float('-inf'),\
    \ float('-inf'), float('-inf'), float('-inf')), \n            values\n       \
    \ )\n        \n        assert seg.prod(0, 4) == (4, 40, 400, 4000, 40000)\n  \
    \      assert seg.prod(0, 2) == (3, 30, 300, 3000, 30000)\n        assert seg.prod(1,\
    \ 3) == (4, 40, 400, 4000, 40000)\n        assert seg.prod(2, 4) == (4, 40, 400,\
    \ 4000, 40000)\n\n    def test_prod_min(self):\n        \"\"\"Test prod operation\
    \ with min\"\"\"\n        values = [(3, 30, 300, 3000, 30000), (1, 10, 100, 1000,\
    \ 10000), (4, 40, 400, 4000, 40000), (2, 20, 200, 2000, 20000)]\n        seg =\
    \ SegTree5(\n            lambda a, b: (min(a[0], b[0]), min(a[1], b[1]), min(a[2],\
    \ b[2]), min(a[3], b[3]), min(a[4], b[4])), \n            (float('inf'), float('inf'),\
    \ float('inf'), float('inf'), float('inf')), \n            values\n        )\n\
    \        \n        assert seg.prod(0, 4) == (1, 10, 100, 1000, 10000)\n      \
    \  assert seg.prod(0, 2) == (1, 10, 100, 1000, 10000)\n        assert seg.prod(1,\
    \ 3) == (1, 10, 100, 1000, 10000)\n        assert seg.prod(2, 4) == (2, 20, 200,\
    \ 2000, 20000)\n\n    def test_all_prod(self):\n        \"\"\"Test all_prod operation\"\
    \"\"\n        values = [(1, 10, 100, 1000, 10000), (2, 20, 200, 2000, 20000),\
    \ (3, 30, 300, 3000, 30000), (4, 40, 400, 4000, 40000)]\n        seg = SegTree5(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0,\
    \ 0, 0, 0, 0), values)\n        \n        assert seg.all_prod() == (10, 100, 1000,\
    \ 10000, 100000)\n\n    def test_max_right(self):\n        \"\"\"Test max_right\
    \ operation\"\"\"\n        values = [(1, 10, 100, 1000, 10000), (2, 20, 200, 2000,\
    \ 20000), (3, 30, 300, 3000, 30000), (4, 40, 400, 4000, 40000)]\n        seg =\
    \ SegTree5(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4]\
    \ + b[4]), (0, 0, 0, 0, 0), values)\n        \n        # Find the rightmost position\
    \ where sum is <= threshold\n        assert seg.max_right(0, lambda x: x[0] <=\
    \ 3) == 2     # Sum up to index 2 is 3\n        assert seg.max_right(0, lambda\
    \ x: x[1] <= 30) == 2    # Sum up to index 2 is 30\n        assert seg.max_right(0,\
    \ lambda x: x[2] <= 300) == 2   # Sum up to index 2 is 300\n        assert seg.max_right(0,\
    \ lambda x: x[3] <= 3000) == 2  # Sum up to index 2 is 3000\n        assert seg.max_right(0,\
    \ lambda x: x[4] <= 30000) == 2 # Sum up to index 2 is 30000\n        assert seg.max_right(0,\
    \ lambda x: x[0] <= 10) == 4    # Sum up to index 4 is 10\n\n    def test_min_left(self):\n\
    \        \"\"\"Test min_left operation\"\"\"\n        values = [(1, 10, 100, 1000,\
    \ 10000), (2, 20, 200, 2000, 20000), (3, 30, 300, 3000, 30000), (4, 40, 400, 4000,\
    \ 40000)]\n        seg = SegTree5(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2]\
    \ + b[2], a[3] + b[3], a[4] + b[4]), (0, 0, 0, 0, 0), values)\n        \n    \
    \    # Find the leftmost position where sum from that position is <= threshold\n\
    \        assert seg.min_left(4, lambda x: x[0] <= 4) == 3      # Only last element\n\
    \        assert seg.min_left(4, lambda x: x[1] <= 40) == 3     # Only last element\n\
    \        assert seg.min_left(4, lambda x: x[2] <= 400) == 3    # Only last element\n\
    \        assert seg.min_left(4, lambda x: x[3] <= 4000) == 3   # Only last element\n\
    \        assert seg.min_left(4, lambda x: x[4] <= 40000) == 3  # Only last element\n\
    \        assert seg.min_left(4, lambda x: x[0] <= 10) == 0     # All elements\n\
    \n    def test_update_and_query(self):\n        \"\"\"Test update operations affect\
    \ queries correctly\"\"\"\n        seg = SegTree5(lambda a, b: (a[0] + b[0], a[1]\
    \ + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0, 0, 0, 0, 0), 4)\n      \
    \  \n        # Initial values\n        seg[0] = (1, 10, 100, 1000, 10000)\n  \
    \      seg[1] = (2, 20, 200, 2000, 20000)\n        seg[2] = (3, 30, 300, 3000,\
    \ 30000)\n        seg[3] = (4, 40, 400, 4000, 40000)\n        \n        assert\
    \ seg.prod(0, 4) == (10, 100, 1000, 10000, 100000)\n        \n        # Update\
    \ some values\n        seg[1] = (5, 50, 500, 5000, 50000)\n        seg[2] = (6,\
    \ 60, 600, 6000, 60000)\n        \n        assert seg.prod(0, 4) == (16, 160,\
    \ 1600, 16000, 160000)\n        assert seg.prod(1, 3) == (11, 110, 1100, 11000,\
    \ 110000)\n\n    def test_empty_tree(self):\n        \"\"\"Test empty segment\
    \ tree\"\"\"\n        seg = SegTree5(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2]\
    \ + b[2], a[3] + b[3], a[4] + b[4]), (0, 0, 0, 0, 0), 0)\n        \n        assert\
    \ seg.n == 0\n        assert seg.all_prod() == (0, 0, 0, 0, 0)\n\n    def test_single_element(self):\n\
    \        \"\"\"Test segment tree with single element\"\"\"\n        seg = SegTree5(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0,\
    \ 0, 0, 0, 0), [(5, 50, 500, 5000, 50000)])\n        \n        assert seg.n ==\
    \ 1\n        assert seg[0] == (5, 50, 500, 5000, 50000)\n        assert seg.prod(0,\
    \ 1) == (5, 50, 500, 5000, 50000)\n        assert seg.all_prod() == (5, 50, 500,\
    \ 5000, 50000)\n\n    def test_large_tree(self):\n        \"\"\"Test with larger\
    \ dataset\"\"\"\n        n = 1000\n        values = [(i, i * 10, i * 100, i *\
    \ 1000, i * 10000) for i in range(n)]\n        seg = SegTree5(lambda a, b: (a[0]\
    \ + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0, 0, 0, 0, 0),\
    \ values)\n        \n        # Sum of 0..999 = 499500\n        assert seg.all_prod()\
    \ == (499500, 4995000, 49950000, 499500000, 4995000000)\n        \n        # Sum\
    \ of 0..99 = 4950\n        assert seg.prod(0, 100) == (4950, 49500, 495000, 4950000,\
    \ 49500000)\n        \n        # Update and verify\n        seg[500] = (1000,\
    \ 10000, 100000, 1000000, 10000000)\n        expected_sum = 499500 - 500 + 1000\n\
    \        assert seg.all_prod() == (expected_sum, 4995000 - 5000 + 10000, 49950000\
    \ - 50000 + 100000, \n                                  499500000 - 500000 + 1000000,\
    \ 4995000000 - 5000000 + 10000000)\n\n    def test_different_types(self):\n  \
    \      \"\"\"Test with different data types in tuples\"\"\"\n        # String\
    \ concatenation, list concatenation, set union, counting, and boolean operations\n\
    \        seg = SegTree5(\n            lambda a, b: (a[0] + b[0], a[1] + b[1],\
    \ a[2] | b[2], a[3] + b[3], a[4] and b[4]),\n            (\"\", [], set(), 0,\
    \ True),\n            [(\"a\", [1], {1}, 1, True), (\"b\", [2], {2}, 1, False),\
    \ (\"c\", [3], {3}, 1, True), (\"d\", [4], {4}, 1, True)]\n        )\n       \
    \ \n        assert seg.prod(0, 2) == (\"ab\", [1, 2], {1, 2}, 2, False)\n    \
    \    assert seg.prod(1, 4) == (\"bcd\", [2, 3, 4], {2, 3, 4}, 3, False)\n    \
    \    assert seg.all_prod() == (\"abcd\", [1, 2, 3, 4], {1, 2, 3, 4}, 4, False)\n\
    \n    def test_complex_operation(self):\n        \"\"\"Test with complex statistical\
    \ operations\"\"\"\n        # Track min, max, sum, count, and variance-related\
    \ value\n        def combine(a, b):\n            return (\n                min(a[0],\
    \ b[0]),  # min\n                max(a[1], b[1]),  # max\n                a[2]\
    \ + b[2],      # sum\n                a[3] + b[3],      # count\n            \
    \    a[4] + b[4]       # sum of squares\n            )\n        \n        values\
    \ = [(3, 3, 3, 1, 9), (1, 1, 1, 1, 1), (4, 4, 4, 1, 16), (2, 2, 2, 1, 4)]\n  \
    \      seg = SegTree5(combine, (float('inf'), float('-inf'), 0, 0, 0), values)\n\
    \        \n        assert seg.prod(0, 4) == (1, 4, 10, 4, 30)  # min=1, max=4,\
    \ sum=10, count=4, sum_squares=30\n        assert seg.prod(0, 2) == (1, 3, 4,\
    \ 2, 10)   # min=1, max=3, sum=4, count=2, sum_squares=10\n        assert seg.prod(2,\
    \ 4) == (2, 4, 6, 2, 20)   # min=2, max=4, sum=6, count=2, sum_squares=20\n\n\
    \    def test_stress_random_operations(self):\n        \"\"\"Stress test with\
    \ random operations\"\"\"\n        random.seed(42)\n        n = 100\n        \n\
    \        # Initialize with random values\n        values = [(random.randint(1,\
    \ 100), random.randint(1, 100), random.randint(1, 100), \n                  random.randint(1,\
    \ 100), random.randint(1, 100)) for _ in range(n)]\n        seg = SegTree5(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0,\
    \ 0, 0, 0, 0), values)\n        \n        # Perform random operations\n      \
    \  for _ in range(200):\n            op = random.choice(['update', 'query'])\n\
    \            \n            if op == 'update':\n                idx = random.randint(0,\
    \ n-1)\n                new_val = (random.randint(1, 100), random.randint(1, 100),\
    \ random.randint(1, 100), \n                          random.randint(1, 100),\
    \ random.randint(1, 100))\n                seg[idx] = new_val\n              \
    \  values[idx] = new_val\n            else:\n                l = random.randint(0,\
    \ n-1)\n                r = random.randint(l, n)\n                \n         \
    \       # Verify against naive calculation\n                expected = (0, 0,\
    \ 0, 0, 0)\n                for i in range(l, r):\n                    expected\
    \ = (expected[0] + values[i][0], expected[1] + values[i][1], \n              \
    \                expected[2] + values[i][2], expected[3] + values[i][3], expected[4]\
    \ + values[i][4])\n                \n                assert seg.prod(l, r) ==\
    \ expected\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\nfrom typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T'); _U\
    \ = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3');\
    \ _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\n\n\n\ndef\
    \ argsort(A: list[int], reverse=False):\n    P = Packer(len(I := list(A))-1);\
    \ P.ienumerate(I, reverse); I.sort(); P.iindices(I)\n    return I\n\n\n\nclass\
    \ Packer:\n    __slots__ = 's', 'm'\n    def __init__(P, mx: int): P.s = mx.bit_length();\
    \ P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int): return a << P.s | b\n\
    \    def dec(P, x: int) -> tuple[int, int]: return x >> P.s, x & P.m\n    def\
    \ enumerate(P, A, reverse=False): P.ienumerate(A:=list(A), reverse); return A\n\
    \    def ienumerate(P, A, reverse=False):\n        if reverse:\n            for\
    \ i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n            for i,a\
    \ in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]): P.iindices(A:=list(A));\
    \ return A\n    def iindices(P, A):\n        for i,a in enumerate(A): A[i] = P.m&a\n\
    \n\ndef isort_parallel(*L: list, reverse=False):\n    inv, order = [0]*len(L[0]),\
    \ argsort(L[0], reverse=reverse)\n    for i, j in enumerate(order): inv[j] = i\n\
    \    for i, j in enumerate(order):\n        for A in L: A[i], A[j] = A[j], A[i]\n\
    \        order[inv[i]], inv[j] = j, inv[i]\n    return L\nfrom typing import Generic\n\
    \n\nclass list5(Generic[_T1, _T2, _T3, _T4, _T5]):\n    __slots__ = 'A1', 'A2',\
    \ 'A3', 'A4', 'A5'\n    def __init__(lst, A1: list[_T1], A2: list[_T2], A3: list[_T3],\
    \ A4: list[_T4], A5: list[_T5]):\n        lst.A1, lst.A2, lst.A3, lst.A4, lst.A5\
    \ = A1, A2, A3, A4, A5\n    def __len__(lst): return len(lst.A1)\n    def __getitem__(lst,\
    \ i: int): return lst.A1[i], lst.A2[i], lst.A3[i], lst.A4[i], lst.A5[i]\n    def\
    \ __setitem__(lst, i: int, v: tuple[_T1, _T2, _T3, _T4, _T5]): lst.A1[i], lst.A2[i],\
    \ lst.A3[i], lst.A4[i], lst.A5[i] = v\n    def __contains__(lst, v: tuple[_T1,\
    \ _T2, _T3, _T4, _T5]): raise NotImplementedError\n    def index(lst, v: tuple[_T1,\
    \ _T2, _T3, _T4, _T5]): raise NotImplementedError\n    def reverse(lst): lst.A1.reverse();\
    \ lst.A2.reverse(); lst.A3.reverse(); lst.A4.reverse(); lst.A5.reverse()\n   \
    \ def sort(lst, reverse=False): isort_parallel(lst.A1, lst.A2, lst.A3, lst.A4,\
    \ lst.A5, reverse=reverse)\n    def pop(lst): return lst.A1.pop(), lst.A2.pop(),\
    \ lst.A3.pop(), lst.A4.pop(), lst.A5.pop()\n    def append(lst, v: tuple[_T1,\
    \ _T2, _T3, _T4, _T5]):\n        v1, v2, v3, v4, v5 = v\n        lst.A1.append(v1);\
    \ lst.A2.append(v2); lst.A3.append(v3); lst.A4.append(v4); lst.A5.append(v5)\n\
    \    def add(lst, i: int, v: tuple[_T1, _T2, _T3, _T4, _T5]): lst.A1[i] += v[0];\
    \ lst.A2[i] += v[1]; lst.A3[i] += v[2]; lst.A4[i] += v[3]; lst.A5[i] += v[4]\n\
    \n\nfrom typing import Callable, Generic, Union\n\nclass SegTree(Generic[_T]):\n\
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
    \ = op(d[r], sm)\n            if (r & -r) == r: return 0\n\nclass SegTree5(SegTree[_T]):\n\
    \    _lst = list5\n\nif __name__ == '__main__':\n    \"\"\"\n    Helper for making\
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
    \nimport pytest\nimport random\n\nclass TestSegTree5:\n    def test_initialization_with_list(self):\n\
    \        \"\"\"Test initialization with a list of 5-tuples\"\"\"\n        values\
    \ = [(1, 10, 100, 1000, 10000), (2, 20, 200, 2000, 20000), (3, 30, 300, 3000,\
    \ 30000), (4, 40, 400, 4000, 40000)]\n        seg = SegTree5(lambda a, b: (a[0]\
    \ + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0, 0, 0, 0, 0),\
    \ values)\n        \n        assert seg.n == 4\n        assert seg[0] == (1, 10,\
    \ 100, 1000, 10000)\n        assert seg[1] == (2, 20, 200, 2000, 20000)\n    \
    \    assert seg[2] == (3, 30, 300, 3000, 30000)\n        assert seg[3] == (4,\
    \ 40, 400, 4000, 40000)\n\n    def test_initialization_with_size(self):\n    \
    \    \"\"\"Test initialization with size only\"\"\"\n        seg = SegTree5(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0,\
    \ 0, 0, 0, 0), 5)\n        \n        assert seg.n == 5\n        # All elements\
    \ should be identity\n        for i in range(5):\n            assert seg[i] ==\
    \ (0, 0, 0, 0, 0)\n\n    def test_set_and_get(self):\n        \"\"\"Test set and\
    \ get operations\"\"\"\n        seg = SegTree5(lambda a, b: (a[0] + b[0], a[1]\
    \ + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0, 0, 0, 0, 0), 4)\n      \
    \  \n        seg[0] = (1, 10, 100, 1000, 10000)\n        seg[1] = (2, 20, 200,\
    \ 2000, 20000)\n        seg[2] = (3, 30, 300, 3000, 30000)\n        seg[3] = (4,\
    \ 40, 400, 4000, 40000)\n        \n        assert seg[0] == (1, 10, 100, 1000,\
    \ 10000)\n        assert seg[1] == (2, 20, 200, 2000, 20000)\n        assert seg[2]\
    \ == (3, 30, 300, 3000, 30000)\n        assert seg[3] == (4, 40, 400, 4000, 40000)\n\
    \n    def test_prod_sum(self):\n        \"\"\"Test prod operation with sum\"\"\
    \"\n        values = [(1, 10, 100, 1000, 10000), (2, 20, 200, 2000, 20000), (3,\
    \ 30, 300, 3000, 30000), (4, 40, 400, 4000, 40000)]\n        seg = SegTree5(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0,\
    \ 0, 0, 0, 0), values)\n        \n        # Test various ranges\n        assert\
    \ seg.prod(0, 4) == (10, 100, 1000, 10000, 100000)  # Sum of all\n        assert\
    \ seg.prod(0, 2) == (3, 30, 300, 3000, 30000)       # First two\n        assert\
    \ seg.prod(1, 3) == (5, 50, 500, 5000, 50000)       # Middle two\n        assert\
    \ seg.prod(2, 4) == (7, 70, 700, 7000, 70000)       # Last two\n        assert\
    \ seg.prod(1, 2) == (2, 20, 200, 2000, 20000)       # Single element\n       \
    \ assert seg.prod(2, 2) == (0, 0, 0, 0, 0)                 # Empty range\n\n \
    \   def test_prod_max(self):\n        \"\"\"Test prod operation with max\"\"\"\
    \n        values = [(3, 30, 300, 3000, 30000), (1, 10, 100, 1000, 10000), (4,\
    \ 40, 400, 4000, 40000), (2, 20, 200, 2000, 20000)]\n        seg = SegTree5(\n\
    \            lambda a, b: (max(a[0], b[0]), max(a[1], b[1]), max(a[2], b[2]),\
    \ max(a[3], b[3]), max(a[4], b[4])), \n            (float('-inf'), float('-inf'),\
    \ float('-inf'), float('-inf'), float('-inf')), \n            values\n       \
    \ )\n        \n        assert seg.prod(0, 4) == (4, 40, 400, 4000, 40000)\n  \
    \      assert seg.prod(0, 2) == (3, 30, 300, 3000, 30000)\n        assert seg.prod(1,\
    \ 3) == (4, 40, 400, 4000, 40000)\n        assert seg.prod(2, 4) == (4, 40, 400,\
    \ 4000, 40000)\n\n    def test_prod_min(self):\n        \"\"\"Test prod operation\
    \ with min\"\"\"\n        values = [(3, 30, 300, 3000, 30000), (1, 10, 100, 1000,\
    \ 10000), (4, 40, 400, 4000, 40000), (2, 20, 200, 2000, 20000)]\n        seg =\
    \ SegTree5(\n            lambda a, b: (min(a[0], b[0]), min(a[1], b[1]), min(a[2],\
    \ b[2]), min(a[3], b[3]), min(a[4], b[4])), \n            (float('inf'), float('inf'),\
    \ float('inf'), float('inf'), float('inf')), \n            values\n        )\n\
    \        \n        assert seg.prod(0, 4) == (1, 10, 100, 1000, 10000)\n      \
    \  assert seg.prod(0, 2) == (1, 10, 100, 1000, 10000)\n        assert seg.prod(1,\
    \ 3) == (1, 10, 100, 1000, 10000)\n        assert seg.prod(2, 4) == (2, 20, 200,\
    \ 2000, 20000)\n\n    def test_all_prod(self):\n        \"\"\"Test all_prod operation\"\
    \"\"\n        values = [(1, 10, 100, 1000, 10000), (2, 20, 200, 2000, 20000),\
    \ (3, 30, 300, 3000, 30000), (4, 40, 400, 4000, 40000)]\n        seg = SegTree5(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0,\
    \ 0, 0, 0, 0), values)\n        \n        assert seg.all_prod() == (10, 100, 1000,\
    \ 10000, 100000)\n\n    def test_max_right(self):\n        \"\"\"Test max_right\
    \ operation\"\"\"\n        values = [(1, 10, 100, 1000, 10000), (2, 20, 200, 2000,\
    \ 20000), (3, 30, 300, 3000, 30000), (4, 40, 400, 4000, 40000)]\n        seg =\
    \ SegTree5(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4]\
    \ + b[4]), (0, 0, 0, 0, 0), values)\n        \n        # Find the rightmost position\
    \ where sum is <= threshold\n        assert seg.max_right(0, lambda x: x[0] <=\
    \ 3) == 2     # Sum up to index 2 is 3\n        assert seg.max_right(0, lambda\
    \ x: x[1] <= 30) == 2    # Sum up to index 2 is 30\n        assert seg.max_right(0,\
    \ lambda x: x[2] <= 300) == 2   # Sum up to index 2 is 300\n        assert seg.max_right(0,\
    \ lambda x: x[3] <= 3000) == 2  # Sum up to index 2 is 3000\n        assert seg.max_right(0,\
    \ lambda x: x[4] <= 30000) == 2 # Sum up to index 2 is 30000\n        assert seg.max_right(0,\
    \ lambda x: x[0] <= 10) == 4    # Sum up to index 4 is 10\n\n    def test_min_left(self):\n\
    \        \"\"\"Test min_left operation\"\"\"\n        values = [(1, 10, 100, 1000,\
    \ 10000), (2, 20, 200, 2000, 20000), (3, 30, 300, 3000, 30000), (4, 40, 400, 4000,\
    \ 40000)]\n        seg = SegTree5(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2]\
    \ + b[2], a[3] + b[3], a[4] + b[4]), (0, 0, 0, 0, 0), values)\n        \n    \
    \    # Find the leftmost position where sum from that position is <= threshold\n\
    \        assert seg.min_left(4, lambda x: x[0] <= 4) == 3      # Only last element\n\
    \        assert seg.min_left(4, lambda x: x[1] <= 40) == 3     # Only last element\n\
    \        assert seg.min_left(4, lambda x: x[2] <= 400) == 3    # Only last element\n\
    \        assert seg.min_left(4, lambda x: x[3] <= 4000) == 3   # Only last element\n\
    \        assert seg.min_left(4, lambda x: x[4] <= 40000) == 3  # Only last element\n\
    \        assert seg.min_left(4, lambda x: x[0] <= 10) == 0     # All elements\n\
    \n    def test_update_and_query(self):\n        \"\"\"Test update operations affect\
    \ queries correctly\"\"\"\n        seg = SegTree5(lambda a, b: (a[0] + b[0], a[1]\
    \ + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0, 0, 0, 0, 0), 4)\n      \
    \  \n        # Initial values\n        seg[0] = (1, 10, 100, 1000, 10000)\n  \
    \      seg[1] = (2, 20, 200, 2000, 20000)\n        seg[2] = (3, 30, 300, 3000,\
    \ 30000)\n        seg[3] = (4, 40, 400, 4000, 40000)\n        \n        assert\
    \ seg.prod(0, 4) == (10, 100, 1000, 10000, 100000)\n        \n        # Update\
    \ some values\n        seg[1] = (5, 50, 500, 5000, 50000)\n        seg[2] = (6,\
    \ 60, 600, 6000, 60000)\n        \n        assert seg.prod(0, 4) == (16, 160,\
    \ 1600, 16000, 160000)\n        assert seg.prod(1, 3) == (11, 110, 1100, 11000,\
    \ 110000)\n\n    def test_empty_tree(self):\n        \"\"\"Test empty segment\
    \ tree\"\"\"\n        seg = SegTree5(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2]\
    \ + b[2], a[3] + b[3], a[4] + b[4]), (0, 0, 0, 0, 0), 0)\n        \n        assert\
    \ seg.n == 0\n        assert seg.all_prod() == (0, 0, 0, 0, 0)\n\n    def test_single_element(self):\n\
    \        \"\"\"Test segment tree with single element\"\"\"\n        seg = SegTree5(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0,\
    \ 0, 0, 0, 0), [(5, 50, 500, 5000, 50000)])\n        \n        assert seg.n ==\
    \ 1\n        assert seg[0] == (5, 50, 500, 5000, 50000)\n        assert seg.prod(0,\
    \ 1) == (5, 50, 500, 5000, 50000)\n        assert seg.all_prod() == (5, 50, 500,\
    \ 5000, 50000)\n\n    def test_large_tree(self):\n        \"\"\"Test with larger\
    \ dataset\"\"\"\n        n = 1000\n        values = [(i, i * 10, i * 100, i *\
    \ 1000, i * 10000) for i in range(n)]\n        seg = SegTree5(lambda a, b: (a[0]\
    \ + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0, 0, 0, 0, 0),\
    \ values)\n        \n        # Sum of 0..999 = 499500\n        assert seg.all_prod()\
    \ == (499500, 4995000, 49950000, 499500000, 4995000000)\n        \n        # Sum\
    \ of 0..99 = 4950\n        assert seg.prod(0, 100) == (4950, 49500, 495000, 4950000,\
    \ 49500000)\n        \n        # Update and verify\n        seg[500] = (1000,\
    \ 10000, 100000, 1000000, 10000000)\n        expected_sum = 499500 - 500 + 1000\n\
    \        assert seg.all_prod() == (expected_sum, 4995000 - 5000 + 10000, 49950000\
    \ - 50000 + 100000, \n                                  499500000 - 500000 + 1000000,\
    \ 4995000000 - 5000000 + 10000000)\n\n    def test_different_types(self):\n  \
    \      \"\"\"Test with different data types in tuples\"\"\"\n        # String\
    \ concatenation, list concatenation, set union, counting, and boolean operations\n\
    \        seg = SegTree5(\n            lambda a, b: (a[0] + b[0], a[1] + b[1],\
    \ a[2] | b[2], a[3] + b[3], a[4] and b[4]),\n            (\"\", [], set(), 0,\
    \ True),\n            [(\"a\", [1], {1}, 1, True), (\"b\", [2], {2}, 1, False),\
    \ (\"c\", [3], {3}, 1, True), (\"d\", [4], {4}, 1, True)]\n        )\n       \
    \ \n        assert seg.prod(0, 2) == (\"ab\", [1, 2], {1, 2}, 2, False)\n    \
    \    assert seg.prod(1, 4) == (\"bcd\", [2, 3, 4], {2, 3, 4}, 3, False)\n    \
    \    assert seg.all_prod() == (\"abcd\", [1, 2, 3, 4], {1, 2, 3, 4}, 4, False)\n\
    \n    def test_complex_operation(self):\n        \"\"\"Test with complex statistical\
    \ operations\"\"\"\n        # Track min, max, sum, count, and variance-related\
    \ value\n        def combine(a, b):\n            return (\n                min(a[0],\
    \ b[0]),  # min\n                max(a[1], b[1]),  # max\n                a[2]\
    \ + b[2],      # sum\n                a[3] + b[3],      # count\n            \
    \    a[4] + b[4]       # sum of squares\n            )\n        \n        values\
    \ = [(3, 3, 3, 1, 9), (1, 1, 1, 1, 1), (4, 4, 4, 1, 16), (2, 2, 2, 1, 4)]\n  \
    \      seg = SegTree5(combine, (float('inf'), float('-inf'), 0, 0, 0), values)\n\
    \        \n        assert seg.prod(0, 4) == (1, 4, 10, 4, 30)  # min=1, max=4,\
    \ sum=10, count=4, sum_squares=30\n        assert seg.prod(0, 2) == (1, 3, 4,\
    \ 2, 10)   # min=1, max=3, sum=4, count=2, sum_squares=10\n        assert seg.prod(2,\
    \ 4) == (2, 4, 6, 2, 20)   # min=2, max=4, sum=6, count=2, sum_squares=20\n\n\
    \    def test_stress_random_operations(self):\n        \"\"\"Stress test with\
    \ random operations\"\"\"\n        random.seed(42)\n        n = 100\n        \n\
    \        # Initialize with random values\n        values = [(random.randint(1,\
    \ 100), random.randint(1, 100), random.randint(1, 100), \n                  random.randint(1,\
    \ 100), random.randint(1, 100)) for _ in range(n)]\n        seg = SegTree5(lambda\
    \ a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[4] + b[4]), (0,\
    \ 0, 0, 0, 0), values)\n        \n        # Perform random operations\n      \
    \  for _ in range(200):\n            op = random.choice(['update', 'query'])\n\
    \            \n            if op == 'update':\n                idx = random.randint(0,\
    \ n-1)\n                new_val = (random.randint(1, 100), random.randint(1, 100),\
    \ random.randint(1, 100), \n                          random.randint(1, 100),\
    \ random.randint(1, 100))\n                seg[idx] = new_val\n              \
    \  values[idx] = new_val\n            else:\n                l = random.randint(0,\
    \ n-1)\n                r = random.randint(l, n)\n                \n         \
    \       # Verify against naive calculation\n                expected = (0, 0,\
    \ 0, 0, 0)\n                for i in range(l, r):\n                    expected\
    \ = (expected[0] + values[i][0], expected[1] + values[i][1], \n              \
    \                expected[2] + values[i][2], expected[3] + values[i][3], expected[4]\
    \ + values[i][4])\n                \n                assert seg.prod(l, r) ==\
    \ expected\n\nfrom cp_library.ds.tree.seg.segtree5_cls import SegTree5\n\nif __name__\
    \ == '__main__':\n    from cp_library.test.unittest_helper import run_verification_helper_unittest\n\
    \    run_verification_helper_unittest()"
  dependsOn:
  - cp_library/ds/tree/seg/segtree5_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/ds/list/list5_cls.py
  - cp_library/ds/tree/seg/segtree_cls.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: true
  path: test/unittests/ds/tree/seg/segtree5_cls_test.py
  requiredBy: []
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/tree/seg/segtree5_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/tree/seg/segtree5_cls_test.py
- /verify/test/unittests/ds/tree/seg/segtree5_cls_test.py.html
title: test/unittests/ds/tree/seg/segtree5_cls_test.py
---
