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
    \nimport pytest\nimport random\n\nclass TestList4:\n    def test_initialization(self):\n\
    \        \"\"\"Test basic initialization of list4\"\"\"\n        A1 = [1, 2, 3,\
    \ 4, 5]\n        A2 = ['a', 'b', 'c', 'd', 'e']\n        A3 = [1.1, 2.2, 3.3,\
    \ 4.4, 5.5]\n        A4 = [True, False, True, False, True]\n        lst = list4(A1,\
    \ A2, A3, A4)\n        \n        assert lst.A1 is A1\n        assert lst.A2 is\
    \ A2\n        assert lst.A3 is A3\n        assert lst.A4 is A4\n        assert\
    \ len(lst) == 5\n\n    def test_len(self):\n        \"\"\"Test __len__ method\"\
    \"\"\n        lst = list4([1, 2, 3], ['a', 'b', 'c'], [1.0, 2.0, 3.0], [True,\
    \ False, True])\n        assert len(lst) == 3\n        \n        lst = list4([],\
    \ [], [], [])\n        assert len(lst) == 0\n        \n        lst = list4(list(range(100)),\
    \ list(range(100)), list(range(100)), list(range(100)))\n        assert len(lst)\
    \ == 100\n\n    def test_getitem(self):\n        \"\"\"Test __getitem__ method\"\
    \"\"\n        lst = list4([10, 20, 30], ['x', 'y', 'z'], [0.1, 0.2, 0.3], [True,\
    \ False, True])\n        \n        assert lst[0] == (10, 'x', 0.1, True)\n   \
    \     assert lst[1] == (20, 'y', 0.2, False)\n        assert lst[2] == (30, 'z',\
    \ 0.3, True)\n        \n        # Test negative indexing\n        assert lst[-1]\
    \ == (30, 'z', 0.3, True)\n        assert lst[-2] == (20, 'y', 0.2, False)\n\n\
    \    def test_setitem(self):\n        \"\"\"Test __setitem__ method\"\"\"\n  \
    \      lst = list4([10, 20, 30], ['x', 'y', 'z'], [0.1, 0.2, 0.3], [True, False,\
    \ True])\n        \n        lst[0] = (15, 'a', 0.15, False)\n        lst[1] =\
    \ (25, 'b', 0.25, True)\n        lst[2] = (35, 'c', 0.35, False)\n        \n \
    \       assert lst.A1 == [15, 25, 35]\n        assert lst.A2 == ['a', 'b', 'c']\n\
    \        assert lst.A3 == [0.15, 0.25, 0.35]\n        assert lst.A4 == [False,\
    \ True, False]\n        assert lst[0] == (15, 'a', 0.15, False)\n        assert\
    \ lst[1] == (25, 'b', 0.25, True)\n        assert lst[2] == (35, 'c', 0.35, False)\n\
    \n    def test_contains_not_implemented(self):\n        \"\"\"Test that __contains__\
    \ raises NotImplementedError\"\"\"\n        lst = list4([1, 2, 3], ['a', 'b',\
    \ 'c'], [0.1, 0.2, 0.3], [True, False, True])\n        \n        with pytest.raises(NotImplementedError):\n\
    \            (1, 'a', 0.1, True) in lst\n\n    def test_index_not_implemented(self):\n\
    \        \"\"\"Test that index raises NotImplementedError\"\"\"\n        lst =\
    \ list4([1, 2, 3], ['a', 'b', 'c'], [0.1, 0.2, 0.3], [True, False, True])\n  \
    \      \n        with pytest.raises(NotImplementedError):\n            lst.index((1,\
    \ 'a', 0.1, True))\n\n    def test_reverse(self):\n        \"\"\"Test reverse\
    \ method\"\"\"\n        lst = list4([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'],\
    \ [0.1, 0.2, 0.3, 0.4, 0.5], [True, False, True, False, True])\n        \n   \
    \     lst.reverse()\n        \n        assert lst.A1 == [5, 4, 3, 2, 1]\n    \
    \    assert lst.A2 == ['e', 'd', 'c', 'b', 'a']\n        assert lst.A3 == [0.5,\
    \ 0.4, 0.3, 0.2, 0.1]\n        assert lst.A4 == [True, False, True, False, True]\n\
    \        assert lst[0] == (5, 'e', 0.5, True)\n        assert lst[4] == (1, 'a',\
    \ 0.1, True)\n\n    def test_sort(self):\n        \"\"\"Test sort method\"\"\"\
    \n        lst = list4([3, 1, 4, 1, 5], ['c', 'a', 'd', 'b', 'e'], [0.3, 0.1, 0.4,\
    \ 0.15, 0.5], [True, False, True, False, True])\n        \n        lst.sort()\n\
    \        \n        # Should sort by first element\n        assert lst.A1 == [1,\
    \ 1, 3, 4, 5]\n        assert lst.A2 == ['a', 'b', 'c', 'd', 'e']\n        assert\
    \ lst.A3 == [0.1, 0.15, 0.3, 0.4, 0.5]\n        assert lst.A4 == [False, False,\
    \ True, True, True]\n        \n    def test_sort_reverse(self):\n        \"\"\"\
    Test sort method with reverse=True\"\"\"\n        lst = list4([3, 1, 4, 1, 5],\
    \ ['c', 'a', 'd', 'b', 'e'], [0.3, 0.1, 0.4, 0.15, 0.5], [True, False, True, False,\
    \ True])\n        \n        lst.sort(reverse=True)\n        \n        # Should\
    \ sort by first element in reverse\n        assert lst.A1 == [5, 4, 3, 1, 1]\n\
    \        assert lst.A2 == ['e', 'd', 'c', 'a', 'b']\n        assert lst.A3 ==\
    \ [0.5, 0.4, 0.3, 0.1, 0.15]\n        assert lst.A4 == [True, True, True, False,\
    \ False]\n\n    def test_pop(self):\n        \"\"\"Test pop method\"\"\"\n   \
    \     lst = list4([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'], [0.1, 0.2, 0.3,\
    \ 0.4, 0.5], [True, False, True, False, True])\n        \n        popped = lst.pop()\n\
    \        assert popped == (5, 'e', 0.5, True)\n        assert len(lst) == 4\n\
    \        assert lst.A1 == [1, 2, 3, 4]\n        assert lst.A2 == ['a', 'b', 'c',\
    \ 'd']\n        assert lst.A3 == [0.1, 0.2, 0.3, 0.4]\n        assert lst.A4 ==\
    \ [True, False, True, False]\n        \n        popped = lst.pop()\n        assert\
    \ popped == (4, 'd', 0.4, False)\n        assert len(lst) == 3\n\n    def test_append(self):\n\
    \        \"\"\"Test append method\"\"\"\n        lst = list4([1, 2, 3], ['a',\
    \ 'b', 'c'], [0.1, 0.2, 0.3], [True, False, True])\n        \n        lst.append((4,\
    \ 'd', 0.4, False))\n        assert len(lst) == 4\n        assert lst[3] == (4,\
    \ 'd', 0.4, False)\n        assert lst.A1 == [1, 2, 3, 4]\n        assert lst.A2\
    \ == ['a', 'b', 'c', 'd']\n        assert lst.A3 == [0.1, 0.2, 0.3, 0.4]\n   \
    \     assert lst.A4 == [True, False, True, False]\n        \n        lst.append((5,\
    \ 'e', 0.5, True))\n        assert len(lst) == 5\n        assert lst[4] == (5,\
    \ 'e', 0.5, True)\n\n    def test_empty_list(self):\n        \"\"\"Test operations\
    \ on empty list4\"\"\"\n        lst = list4([], [], [], [])\n        \n      \
    \  assert len(lst) == 0\n        \n        with pytest.raises(IndexError):\n \
    \           lst.pop()\n        \n        lst.append((1, 'a', 0.1, True))\n   \
    \     assert len(lst) == 1\n        assert lst[0] == (1, 'a', 0.1, True)\n\n \
    \   def test_with_different_types(self):\n        \"\"\"Test list4 with different\
    \ data types\"\"\"\n        # Integer, string, float, boolean\n        lst = list4([1,\
    \ 2, 3], ['a', 'b', 'c'], [1.1, 2.2, 3.3], [True, False, True])\n        assert\
    \ lst[0] == (1, 'a', 1.1, True)\n        assert lst[1] == (2, 'b', 2.2, False)\n\
    \        \n        # String, list, dict, None\n        lst = list4(['x', 'y',\
    \ 'z'], [[1], [2], [3]], [{'a': 1}, {'b': 2}, {'c': 3}], [None, None, None])\n\
    \        assert lst[0] == ('x', [1], {'a': 1}, None)\n        assert lst[1] ==\
    \ ('y', [2], {'b': 2}, None)\n        \n        # Mixed types\n        lst = list4([1,\
    \ 'two', 3.0], [None, [1, 2], {'key': 'value'}], [True, False, None], [[1, 2],\
    \ 'str', 3])\n        assert lst[0] == (1, None, True, [1, 2])\n        assert\
    \ lst[1] == ('two', [1, 2], False, 'str')\n        assert lst[2] == (3.0, {'key':\
    \ 'value'}, None, 3)\n\n    def test_large_data_operations(self):\n        \"\"\
    \"Test operations on larger datasets\"\"\"\n        n = 1000\n        A1 = list(range(n))\n\
    \        A2 = list(range(n, 2*n))\n        A3 = list(range(2*n, 3*n))\n      \
    \  A4 = list(range(3*n, 4*n))\n        lst = list4(A1, A2, A3, A4)\n        \n\
    \        assert len(lst) == n\n        assert lst[0] == (0, n, 2*n, 3*n)\n   \
    \     assert lst[n-1] == (n-1, 2*n-1, 3*n-1, 4*n-1)\n        \n        # Test\
    \ pop on large dataset\n        popped = lst.pop()\n        assert popped == (n-1,\
    \ 2*n-1, 3*n-1, 4*n-1)\n        assert len(lst) == n-1\n        \n        # Test\
    \ append on large dataset\n        lst.append((n, 2*n, 3*n, 4*n))\n        assert\
    \ len(lst) == n\n        assert lst[n-1] == (n, 2*n, 3*n, 4*n)\n\n    def test_sort_stability(self):\n\
    \        \"\"\"Test that sort maintains parallel structure\"\"\"\n        # Create\
    \ data where first elements have duplicates\n        lst = list4([3, 1, 2, 1,\
    \ 3], ['a', 'b', 'c', 'd', 'e'], [0.3, 0.1, 0.2, 0.15, 0.35], [True, False, True,\
    \ False, True])\n        \n        lst.sort()\n        \n        # After sorting\
    \ by first element, check parallel structure\n        assert lst[0][0] == 1\n\
    \        assert lst[1][0] == 1\n        assert lst[2][0] == 2\n        assert\
    \ lst[3][0] == 3\n        assert lst[4][0] == 3\n        \n        # The corresponding\
    \ elements should be maintained\n        assert lst[0] == (1, 'b', 0.1, False)\n\
    \        assert lst[1] == (1, 'd', 0.15, False)\n        assert lst[2] == (2,\
    \ 'c', 0.2, True)\n        assert lst[3] == (3, 'a', 0.3, True)\n        assert\
    \ lst[4] == (3, 'e', 0.35, True)\n\n    def test_random_operations(self):\n  \
    \      \"\"\"Test random operations for robustness\"\"\"\n        random.seed(42)\n\
    \        \n        n = 100\n        A1 = list(range(n))\n        A2 = list(range(100,\
    \ 100 + n))\n        A3 = list(range(200, 200 + n))\n        A4 = list(range(300,\
    \ 300 + n))\n        lst = list4(A1, A2, A3, A4)\n        \n        # Perform\
    \ random operations\n        for _ in range(50):\n            op = random.choice(['read',\
    \ 'write', 'append_pop'])\n            \n            if op == 'read' and len(lst)\
    \ > 0:\n                idx = random.randint(0, len(lst) - 1)\n              \
    \  val = lst[idx]\n                assert val == (lst.A1[idx], lst.A2[idx], lst.A3[idx],\
    \ lst.A4[idx])\n                \n            elif op == 'write' and len(lst)\
    \ > 0:\n                idx = random.randint(0, len(lst) - 1)\n              \
    \  new_val1 = random.randint(1000, 2000)\n                new_val2 = random.randint(3000,\
    \ 4000)\n                new_val3 = random.randint(5000, 6000)\n             \
    \   new_val4 = random.randint(7000, 8000)\n                lst[idx] = (new_val1,\
    \ new_val2, new_val3, new_val4)\n                assert lst.A1[idx] == new_val1\n\
    \                assert lst.A2[idx] == new_val2\n                assert lst.A3[idx]\
    \ == new_val3\n                assert lst.A4[idx] == new_val4\n              \
    \  \n            elif op == 'append_pop':\n                if random.random()\
    \ < 0.5 and len(lst) > 0:\n                    expected = (lst.A1[-1], lst.A2[-1],\
    \ lst.A3[-1], lst.A4[-1])\n                    popped = lst.pop()\n          \
    \          assert popped == expected\n                else:\n                \
    \    val1 = random.randint(9000, 10000)\n                    val2 = random.randint(11000,\
    \ 12000)\n                    val3 = random.randint(13000, 14000)\n          \
    \          val4 = random.randint(15000, 16000)\n                    lst.append((val1,\
    \ val2, val3, val4))\n                    assert lst[-1] == (val1, val2, val3,\
    \ val4)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\n\n\ndef argsort(A: list[int], reverse=False):\n    P = Packer(len(I := list(A))-1);\
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
    from typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U');\
    \ _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4');\
    \ _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\n\nclass list4(Generic[_T1, _T2,\
    \ _T3, _T4]):\n    __slots__ = 'A1', 'A2', 'A3', 'A4'\n    def __init__(lst, A1:\
    \ list[_T1], A2: list[_T2], A3: list[_T3], A4: list[_T4]):\n        lst.A1, lst.A2,\
    \ lst.A3, lst.A4 = A1, A2, A3, A4\n    def __len__(lst): return len(lst.A1)\n\
    \    def __getitem__(lst, i: int): return lst.A1[i], lst.A2[i], lst.A3[i], lst.A4[i]\n\
    \    def __setitem__(lst, i: int, v: tuple[_T1, _T2, _T3, _T4]): lst.A1[i], lst.A2[i],\
    \ lst.A3[i], lst.A4[i] = v\n    def __contains__(lst, v: tuple[_T1, _T2, _T3,\
    \ _T4]): raise NotImplementedError\n    def index(lst, v: tuple[_T1, _T2, _T3,\
    \ _T4]): raise NotImplementedError\n    def reverse(lst): lst.A1.reverse(); lst.A2.reverse();\
    \ lst.A3.reverse(); lst.A4.reverse()\n    def sort(lst, reverse=False): isort_parallel(lst.A1,\
    \ lst.A2, lst.A3, lst.A4, reverse=reverse)\n    def pop(lst): return lst.A1.pop(),\
    \ lst.A2.pop(), lst.A3.pop(), lst.A4.pop()\n    def append(lst, v: tuple[_T1,\
    \ _T2, _T3, _T4]):\n        v1, v2, v3, v4 = v\n        lst.A1.append(v1); lst.A2.append(v2);\
    \ lst.A3.append(v3); lst.A4.append(v4)\n    def add(lst, i: int, v: tuple[_T1,\
    \ _T2, _T3, _T4]): lst.A1[i] += v[0]; lst.A2[i] += v[1]; lst.A3[i] += v[2]; lst.A4[i]\
    \ += v[3]\n\nif __name__ == '__main__':\n    \"\"\"\n    Helper for making unittest\
    \ files compatible with verification-helper.\n    \n    This module provides a\
    \ helper function to run a dummy Library Checker test\n    so that unittest files\
    \ can be verified by oj-verify.\n    \"\"\"\n    \n    def run_verification_helper_unittest():\n\
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
    \nimport pytest\nimport random\n\nclass TestList4:\n    def test_initialization(self):\n\
    \        \"\"\"Test basic initialization of list4\"\"\"\n        A1 = [1, 2, 3,\
    \ 4, 5]\n        A2 = ['a', 'b', 'c', 'd', 'e']\n        A3 = [1.1, 2.2, 3.3,\
    \ 4.4, 5.5]\n        A4 = [True, False, True, False, True]\n        lst = list4(A1,\
    \ A2, A3, A4)\n        \n        assert lst.A1 is A1\n        assert lst.A2 is\
    \ A2\n        assert lst.A3 is A3\n        assert lst.A4 is A4\n        assert\
    \ len(lst) == 5\n\n    def test_len(self):\n        \"\"\"Test __len__ method\"\
    \"\"\n        lst = list4([1, 2, 3], ['a', 'b', 'c'], [1.0, 2.0, 3.0], [True,\
    \ False, True])\n        assert len(lst) == 3\n        \n        lst = list4([],\
    \ [], [], [])\n        assert len(lst) == 0\n        \n        lst = list4(list(range(100)),\
    \ list(range(100)), list(range(100)), list(range(100)))\n        assert len(lst)\
    \ == 100\n\n    def test_getitem(self):\n        \"\"\"Test __getitem__ method\"\
    \"\"\n        lst = list4([10, 20, 30], ['x', 'y', 'z'], [0.1, 0.2, 0.3], [True,\
    \ False, True])\n        \n        assert lst[0] == (10, 'x', 0.1, True)\n   \
    \     assert lst[1] == (20, 'y', 0.2, False)\n        assert lst[2] == (30, 'z',\
    \ 0.3, True)\n        \n        # Test negative indexing\n        assert lst[-1]\
    \ == (30, 'z', 0.3, True)\n        assert lst[-2] == (20, 'y', 0.2, False)\n\n\
    \    def test_setitem(self):\n        \"\"\"Test __setitem__ method\"\"\"\n  \
    \      lst = list4([10, 20, 30], ['x', 'y', 'z'], [0.1, 0.2, 0.3], [True, False,\
    \ True])\n        \n        lst[0] = (15, 'a', 0.15, False)\n        lst[1] =\
    \ (25, 'b', 0.25, True)\n        lst[2] = (35, 'c', 0.35, False)\n        \n \
    \       assert lst.A1 == [15, 25, 35]\n        assert lst.A2 == ['a', 'b', 'c']\n\
    \        assert lst.A3 == [0.15, 0.25, 0.35]\n        assert lst.A4 == [False,\
    \ True, False]\n        assert lst[0] == (15, 'a', 0.15, False)\n        assert\
    \ lst[1] == (25, 'b', 0.25, True)\n        assert lst[2] == (35, 'c', 0.35, False)\n\
    \n    def test_contains_not_implemented(self):\n        \"\"\"Test that __contains__\
    \ raises NotImplementedError\"\"\"\n        lst = list4([1, 2, 3], ['a', 'b',\
    \ 'c'], [0.1, 0.2, 0.3], [True, False, True])\n        \n        with pytest.raises(NotImplementedError):\n\
    \            (1, 'a', 0.1, True) in lst\n\n    def test_index_not_implemented(self):\n\
    \        \"\"\"Test that index raises NotImplementedError\"\"\"\n        lst =\
    \ list4([1, 2, 3], ['a', 'b', 'c'], [0.1, 0.2, 0.3], [True, False, True])\n  \
    \      \n        with pytest.raises(NotImplementedError):\n            lst.index((1,\
    \ 'a', 0.1, True))\n\n    def test_reverse(self):\n        \"\"\"Test reverse\
    \ method\"\"\"\n        lst = list4([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'],\
    \ [0.1, 0.2, 0.3, 0.4, 0.5], [True, False, True, False, True])\n        \n   \
    \     lst.reverse()\n        \n        assert lst.A1 == [5, 4, 3, 2, 1]\n    \
    \    assert lst.A2 == ['e', 'd', 'c', 'b', 'a']\n        assert lst.A3 == [0.5,\
    \ 0.4, 0.3, 0.2, 0.1]\n        assert lst.A4 == [True, False, True, False, True]\n\
    \        assert lst[0] == (5, 'e', 0.5, True)\n        assert lst[4] == (1, 'a',\
    \ 0.1, True)\n\n    def test_sort(self):\n        \"\"\"Test sort method\"\"\"\
    \n        lst = list4([3, 1, 4, 1, 5], ['c', 'a', 'd', 'b', 'e'], [0.3, 0.1, 0.4,\
    \ 0.15, 0.5], [True, False, True, False, True])\n        \n        lst.sort()\n\
    \        \n        # Should sort by first element\n        assert lst.A1 == [1,\
    \ 1, 3, 4, 5]\n        assert lst.A2 == ['a', 'b', 'c', 'd', 'e']\n        assert\
    \ lst.A3 == [0.1, 0.15, 0.3, 0.4, 0.5]\n        assert lst.A4 == [False, False,\
    \ True, True, True]\n        \n    def test_sort_reverse(self):\n        \"\"\"\
    Test sort method with reverse=True\"\"\"\n        lst = list4([3, 1, 4, 1, 5],\
    \ ['c', 'a', 'd', 'b', 'e'], [0.3, 0.1, 0.4, 0.15, 0.5], [True, False, True, False,\
    \ True])\n        \n        lst.sort(reverse=True)\n        \n        # Should\
    \ sort by first element in reverse\n        assert lst.A1 == [5, 4, 3, 1, 1]\n\
    \        assert lst.A2 == ['e', 'd', 'c', 'a', 'b']\n        assert lst.A3 ==\
    \ [0.5, 0.4, 0.3, 0.1, 0.15]\n        assert lst.A4 == [True, True, True, False,\
    \ False]\n\n    def test_pop(self):\n        \"\"\"Test pop method\"\"\"\n   \
    \     lst = list4([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'], [0.1, 0.2, 0.3,\
    \ 0.4, 0.5], [True, False, True, False, True])\n        \n        popped = lst.pop()\n\
    \        assert popped == (5, 'e', 0.5, True)\n        assert len(lst) == 4\n\
    \        assert lst.A1 == [1, 2, 3, 4]\n        assert lst.A2 == ['a', 'b', 'c',\
    \ 'd']\n        assert lst.A3 == [0.1, 0.2, 0.3, 0.4]\n        assert lst.A4 ==\
    \ [True, False, True, False]\n        \n        popped = lst.pop()\n        assert\
    \ popped == (4, 'd', 0.4, False)\n        assert len(lst) == 3\n\n    def test_append(self):\n\
    \        \"\"\"Test append method\"\"\"\n        lst = list4([1, 2, 3], ['a',\
    \ 'b', 'c'], [0.1, 0.2, 0.3], [True, False, True])\n        \n        lst.append((4,\
    \ 'd', 0.4, False))\n        assert len(lst) == 4\n        assert lst[3] == (4,\
    \ 'd', 0.4, False)\n        assert lst.A1 == [1, 2, 3, 4]\n        assert lst.A2\
    \ == ['a', 'b', 'c', 'd']\n        assert lst.A3 == [0.1, 0.2, 0.3, 0.4]\n   \
    \     assert lst.A4 == [True, False, True, False]\n        \n        lst.append((5,\
    \ 'e', 0.5, True))\n        assert len(lst) == 5\n        assert lst[4] == (5,\
    \ 'e', 0.5, True)\n\n    def test_empty_list(self):\n        \"\"\"Test operations\
    \ on empty list4\"\"\"\n        lst = list4([], [], [], [])\n        \n      \
    \  assert len(lst) == 0\n        \n        with pytest.raises(IndexError):\n \
    \           lst.pop()\n        \n        lst.append((1, 'a', 0.1, True))\n   \
    \     assert len(lst) == 1\n        assert lst[0] == (1, 'a', 0.1, True)\n\n \
    \   def test_with_different_types(self):\n        \"\"\"Test list4 with different\
    \ data types\"\"\"\n        # Integer, string, float, boolean\n        lst = list4([1,\
    \ 2, 3], ['a', 'b', 'c'], [1.1, 2.2, 3.3], [True, False, True])\n        assert\
    \ lst[0] == (1, 'a', 1.1, True)\n        assert lst[1] == (2, 'b', 2.2, False)\n\
    \        \n        # String, list, dict, None\n        lst = list4(['x', 'y',\
    \ 'z'], [[1], [2], [3]], [{'a': 1}, {'b': 2}, {'c': 3}], [None, None, None])\n\
    \        assert lst[0] == ('x', [1], {'a': 1}, None)\n        assert lst[1] ==\
    \ ('y', [2], {'b': 2}, None)\n        \n        # Mixed types\n        lst = list4([1,\
    \ 'two', 3.0], [None, [1, 2], {'key': 'value'}], [True, False, None], [[1, 2],\
    \ 'str', 3])\n        assert lst[0] == (1, None, True, [1, 2])\n        assert\
    \ lst[1] == ('two', [1, 2], False, 'str')\n        assert lst[2] == (3.0, {'key':\
    \ 'value'}, None, 3)\n\n    def test_large_data_operations(self):\n        \"\"\
    \"Test operations on larger datasets\"\"\"\n        n = 1000\n        A1 = list(range(n))\n\
    \        A2 = list(range(n, 2*n))\n        A3 = list(range(2*n, 3*n))\n      \
    \  A4 = list(range(3*n, 4*n))\n        lst = list4(A1, A2, A3, A4)\n        \n\
    \        assert len(lst) == n\n        assert lst[0] == (0, n, 2*n, 3*n)\n   \
    \     assert lst[n-1] == (n-1, 2*n-1, 3*n-1, 4*n-1)\n        \n        # Test\
    \ pop on large dataset\n        popped = lst.pop()\n        assert popped == (n-1,\
    \ 2*n-1, 3*n-1, 4*n-1)\n        assert len(lst) == n-1\n        \n        # Test\
    \ append on large dataset\n        lst.append((n, 2*n, 3*n, 4*n))\n        assert\
    \ len(lst) == n\n        assert lst[n-1] == (n, 2*n, 3*n, 4*n)\n\n    def test_sort_stability(self):\n\
    \        \"\"\"Test that sort maintains parallel structure\"\"\"\n        # Create\
    \ data where first elements have duplicates\n        lst = list4([3, 1, 2, 1,\
    \ 3], ['a', 'b', 'c', 'd', 'e'], [0.3, 0.1, 0.2, 0.15, 0.35], [True, False, True,\
    \ False, True])\n        \n        lst.sort()\n        \n        # After sorting\
    \ by first element, check parallel structure\n        assert lst[0][0] == 1\n\
    \        assert lst[1][0] == 1\n        assert lst[2][0] == 2\n        assert\
    \ lst[3][0] == 3\n        assert lst[4][0] == 3\n        \n        # The corresponding\
    \ elements should be maintained\n        assert lst[0] == (1, 'b', 0.1, False)\n\
    \        assert lst[1] == (1, 'd', 0.15, False)\n        assert lst[2] == (2,\
    \ 'c', 0.2, True)\n        assert lst[3] == (3, 'a', 0.3, True)\n        assert\
    \ lst[4] == (3, 'e', 0.35, True)\n\n    def test_random_operations(self):\n  \
    \      \"\"\"Test random operations for robustness\"\"\"\n        random.seed(42)\n\
    \        \n        n = 100\n        A1 = list(range(n))\n        A2 = list(range(100,\
    \ 100 + n))\n        A3 = list(range(200, 200 + n))\n        A4 = list(range(300,\
    \ 300 + n))\n        lst = list4(A1, A2, A3, A4)\n        \n        # Perform\
    \ random operations\n        for _ in range(50):\n            op = random.choice(['read',\
    \ 'write', 'append_pop'])\n            \n            if op == 'read' and len(lst)\
    \ > 0:\n                idx = random.randint(0, len(lst) - 1)\n              \
    \  val = lst[idx]\n                assert val == (lst.A1[idx], lst.A2[idx], lst.A3[idx],\
    \ lst.A4[idx])\n                \n            elif op == 'write' and len(lst)\
    \ > 0:\n                idx = random.randint(0, len(lst) - 1)\n              \
    \  new_val1 = random.randint(1000, 2000)\n                new_val2 = random.randint(3000,\
    \ 4000)\n                new_val3 = random.randint(5000, 6000)\n             \
    \   new_val4 = random.randint(7000, 8000)\n                lst[idx] = (new_val1,\
    \ new_val2, new_val3, new_val4)\n                assert lst.A1[idx] == new_val1\n\
    \                assert lst.A2[idx] == new_val2\n                assert lst.A3[idx]\
    \ == new_val3\n                assert lst.A4[idx] == new_val4\n              \
    \  \n            elif op == 'append_pop':\n                if random.random()\
    \ < 0.5 and len(lst) > 0:\n                    expected = (lst.A1[-1], lst.A2[-1],\
    \ lst.A3[-1], lst.A4[-1])\n                    popped = lst.pop()\n          \
    \          assert popped == expected\n                else:\n                \
    \    val1 = random.randint(9000, 10000)\n                    val2 = random.randint(11000,\
    \ 12000)\n                    val3 = random.randint(13000, 14000)\n          \
    \          val4 = random.randint(15000, 16000)\n                    lst.append((val1,\
    \ val2, val3, val4))\n                    assert lst[-1] == (val1, val2, val3,\
    \ val4)\n\nfrom cp_library.ds.list.list4_cls import list4\n\nif __name__ == '__main__':\n\
    \    from cp_library.test.unittest_helper import run_verification_helper_unittest\n\
    \    run_verification_helper_unittest()"
  dependsOn:
  - cp_library/ds/list/list4_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: true
  path: test/unittests/ds/list/list4_cls_test.py
  requiredBy: []
  timestamp: '2025-07-26 11:14:31+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/list/list4_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/list/list4_cls_test.py
- /verify/test/unittests/ds/list/list4_cls_test.py.html
title: test/unittests/ds/list/list4_cls_test.py
---
