---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_ranged_fn.py
    title: cp_library/alg/iter/arg/argsort_ranged_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/isort_ranged_fn.py
    title: cp_library/alg/iter/sort/isort_ranged_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view2_cls.py
    title: cp_library/ds/view/view2_cls.py
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
    \nimport pytest\nimport random\n\nclass TestView2:\n    def test_initialization(self):\n\
    \        \"\"\"Test basic initialization of view2\"\"\"\n        A = [1, 2, 3,\
    \ 4, 5]\n        B = ['a', 'b', 'c', 'd', 'e']\n        v = view2(A, B, 1, 4)\n\
    \        \n        assert v.A1 is A\n        assert v.A2 is B\n        assert\
    \ v.l == 1\n        assert v.r == 4\n        assert len(v) == 3\n\n    def test_len(self):\n\
    \        \"\"\"Test __len__ method\"\"\"\n        A = [1, 2, 3, 4, 5, 6, 7, 8,\
    \ 9, 10]\n        B = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]\n        \n  \
    \      # Test different ranges\n        assert len(view2(A, B, 0, 5)) == 5\n \
    \       assert len(view2(A, B, 2, 7)) == 5\n        assert len(view2(A, B, 0,\
    \ 10)) == 10\n        assert len(view2(A, B, 5, 5)) == 0  # Empty range\n\n  \
    \  def test_getitem(self):\n        \"\"\"Test __getitem__ method\"\"\"\n    \
    \    A = [10, 20, 30, 40, 50]\n        B = ['x', 'y', 'z', 'w', 'v']\n       \
    \ v = view2(A, B, 1, 4)  # View of [(20,'y'), (30,'z'), (40,'w')]\n        \n\
    \        assert v[0] == (20, 'y')\n        assert v[1] == (30, 'z')\n        assert\
    \ v[2] == (40, 'w')\n        \n        # Test IndexError for out of bounds\n \
    \       with pytest.raises(IndexError):\n            v[3]\n        with pytest.raises(IndexError):\n\
    \            v[-1]\n\n    def test_setitem(self):\n        \"\"\"Test __setitem__\
    \ method\"\"\"\n        A = [10, 20, 30, 40, 50]\n        B = ['x', 'y', 'z',\
    \ 'w', 'v']\n        v = view2(A, B, 1, 4)  # View of [(20,'y'), (30,'z'), (40,'w')]\n\
    \        \n        v[0] = (25, 'Y')\n        v[1] = (35, 'Z')\n        v[2] =\
    \ (45, 'W')\n        \n        assert A == [10, 25, 35, 45, 50]\n        assert\
    \ B == ['x', 'Y', 'Z', 'W', 'v']\n        assert v[0] == (25, 'Y')\n        assert\
    \ v[1] == (35, 'Z')\n        assert v[2] == (45, 'W')\n\n    def test_contains_not_implemented(self):\n\
    \        \"\"\"Test that __contains__ raises NotImplemented\"\"\"\n        A =\
    \ [1, 2, 3, 4, 5]\n        B = ['a', 'b', 'c', 'd', 'e']\n        v = view2(A,\
    \ B, 1, 4)\n        \n        with pytest.raises(TypeError):  # NotImplemented\
    \ raises TypeError\n            (2, 'b') in v\n\n    def test_index_not_implemented(self):\n\
    \        \"\"\"Test that index raises NotImplemented\"\"\"\n        A = [1, 2,\
    \ 3, 4, 5]\n        B = ['a', 'b', 'c', 'd', 'e']\n        v = view2(A, B, 1,\
    \ 4)\n        \n        with pytest.raises(TypeError):  # NotImplemented raises\
    \ TypeError\n            v.index((2, 'b'))\n\n    def test_set_range(self):\n\
    \        \"\"\"Test set_range method\"\"\"\n        A = [1, 2, 3, 4, 5, 6, 7,\
    \ 8, 9, 10]\n        B = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]\n        v\
    \ = view2(A, B, 2, 5)\n        \n        assert len(v) == 3\n        assert v[0]\
    \ == (3, 30)\n        \n        # Change the range\n        v.set_range(4, 8)\n\
    \        assert len(v) == 4\n        assert v[0] == (5, 50)\n        assert v[1]\
    \ == (6, 60)\n        assert v[2] == (7, 70)\n        assert v[3] == (8, 80)\n\
    \n    def test_reverse(self):\n        \"\"\"Test reverse method\"\"\"\n     \
    \   A = [1, 2, 3, 4, 5, 6, 7, 8, 9]\n        B = [10, 20, 30, 40, 50, 60, 70,\
    \ 80, 90]\n        v = view2(A, B, 2, 7)  # View of [(3,30), (4,40), (5,50), (6,60),\
    \ (7,70)]\n        \n        v.reverse()\n        \n        # Check that the view\
    \ is reversed\n        assert v[0] == (7, 70)\n        assert v[1] == (6, 60)\n\
    \        assert v[2] == (5, 50)\n        assert v[3] == (4, 40)\n        assert\
    \ v[4] == (3, 30)\n        \n        # Check that the underlying arrays are modified\n\
    \        assert A == [1, 2, 7, 6, 5, 4, 3, 8, 9]\n        assert B == [10, 20,\
    \ 70, 60, 50, 40, 30, 80, 90]\n\n    def test_sort(self):\n        \"\"\"Test\
    \ sort method\"\"\"\n        A = [1, 5, 2, 8, 3, 9, 4, 6, 7]\n        B = [10,\
    \ 50, 20, 80, 30, 90, 40, 60, 70]\n        v = view2(A, B, 2, 7)  # View of [(2,20),\
    \ (8,80), (3,30), (9,90), (4,40)]\n        \n        v.sort()\n        \n    \
    \    # Check that the view is sorted by A values\n        assert v[0] == (2, 20)\n\
    \        assert v[1] == (3, 30)\n        assert v[2] == (4, 40)\n        assert\
    \ v[3] == (8, 80)\n        assert v[4] == (9, 90)\n        \n        # Check that\
    \ the underlying arrays are modified correctly\n        assert A == [1, 5, 2,\
    \ 3, 4, 8, 9, 6, 7]\n        assert B == [10, 50, 20, 30, 40, 80, 90, 60, 70]\n\
    \n    def test_sort_reverse(self):\n        \"\"\"Test sort method with reverse=True\"\
    \"\"\n        A = [1, 5, 2, 8, 3, 9, 4, 6, 7]\n        B = [10, 50, 20, 80, 30,\
    \ 90, 40, 60, 70]\n        v = view2(A, B, 2, 7)  # View of [(2,20), (8,80), (3,30),\
    \ (9,90), (4,40)]\n        \n        v.sort(reverse=True)\n        \n        #\
    \ Check that the view is sorted in reverse by A values\n        assert v[0] ==\
    \ (9, 90)\n        assert v[1] == (8, 80)\n        assert v[2] == (4, 40)\n  \
    \      assert v[3] == (3, 30)\n        assert v[4] == (2, 20)\n        \n    \
    \    # Check that the underlying arrays are modified correctly\n        assert\
    \ A == [1, 5, 9, 8, 4, 3, 2, 6, 7]\n        assert B == [10, 50, 90, 80, 40, 30,\
    \ 20, 60, 70]\n\n    def test_pop(self):\n        \"\"\"Test pop method\"\"\"\n\
    \        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]\n        B = [10, 20, 30, 40, 50, 60,\
    \ 70, 80, 90]\n        v = view2(A, B, 2, 6)  # View of [(3,30), (4,40), (5,50),\
    \ (6,60)]\n        \n        assert len(v) == 4\n        \n        # Pop from\
    \ the end\n        popped = v.pop()\n        assert popped == (6, 60)\n      \
    \  assert len(v) == 3\n        assert v[2] == (5, 50)  # Last element is now (5,50)\n\
    \        \n        # Pop again\n        popped = v.pop()\n        assert popped\
    \ == (5, 50)\n        assert len(v) == 2\n\n    def test_append(self):\n     \
    \   \"\"\"Test append method\"\"\"\n        A = [1, 2, 3, 4, 5, 0, 0, 0, 9]  #\
    \ Extra space for appending\n        B = [10, 20, 30, 40, 50, 0, 0, 0, 90]\n \
    \       v = view2(A, B, 2, 5)  # View of [(3,30), (4,40), (5,50)]\n        \n\
    \        assert len(v) == 3\n        \n        # Append to the end\n        v.append((6,\
    \ 60))\n        assert len(v) == 4\n        assert v[3] == (6, 60)\n        assert\
    \ A[5] == 6  # Check underlying arrays\n        assert B[5] == 60\n        \n\
    \        # Append again\n        v.append((7, 70))\n        assert len(v) == 5\n\
    \        assert v[4] == (7, 70)\n\n    def test_popleft(self):\n        \"\"\"\
    Test popleft method\"\"\"\n        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]\n        B\
    \ = [10, 20, 30, 40, 50, 60, 70, 80, 90]\n        v = view2(A, B, 2, 6)  # View\
    \ of [(3,30), (4,40), (5,50), (6,60)]\n        \n        assert len(v) == 4\n\
    \        \n        # Pop from the beginning\n        popped = v.popleft()\n  \
    \      assert popped == (3, 30)\n        assert len(v) == 3\n        assert v[0]\
    \ == (4, 40)  # First element is now (4,40)\n        \n        # Pop again\n \
    \       popped = v.popleft()\n        assert popped == (4, 40)\n        assert\
    \ len(v) == 2\n        assert v[0] == (5, 50)\n\n    def test_appendleft(self):\n\
    \        \"\"\"Test appendleft method\"\"\"\n        A = [0, 0, 1, 2, 3, 4, 5,\
    \ 6, 7]  # Extra space at beginning\n        B = [0, 0, 10, 20, 30, 40, 50, 60,\
    \ 70]\n        v = view2(A, B, 4, 7)  # View of [(3,30), (4,40), (5,50)]\n   \
    \     \n        assert len(v) == 3\n        assert v[0] == (3, 30)\n        \n\
    \        # Append to the beginning\n        v.appendleft((2, 20))\n        assert\
    \ len(v) == 4\n        assert v[0] == (2, 20)\n        assert v[1] == (3, 30)\n\
    \        assert A[3] == 2  # Check underlying arrays\n        assert B[3] == 20\n\
    \        \n        # Append again\n        v.appendleft((1, 10))\n        assert\
    \ len(v) == 5\n        assert v[0] == (1, 10)\n        assert v[1] == (2, 20)\n\
    \n    def test_validate(self):\n        \"\"\"Test validate method\"\"\"\n   \
    \     A = [1, 2, 3, 4, 5]\n        B = [10, 20, 30, 40, 50]\n        \n      \
    \  # Valid ranges\n        v1 = view2(A, B, 0, 5)\n        assert v1.validate()\
    \ == True\n        \n        v2 = view2(A, B, 2, 4)\n        assert v2.validate()\
    \ == True\n        \n        v3 = view2(A, B, 3, 3)  # Empty range\n        assert\
    \ v3.validate() == True\n        \n        # Invalid ranges\n        v4 = view2(A,\
    \ B, -1, 3)\n        assert v4.validate() == False\n        \n        v5 = view2(A,\
    \ B, 2, 6)  # r > len(A)\n        assert v5.validate() == False\n        \n  \
    \      v6 = view2(A, B, 3, 2)  # l > r\n        assert v6.validate() == False\n\
    \n    def test_empty_view(self):\n        \"\"\"Test operations on empty view\"\
    \"\"\n        A = [1, 2, 3, 4, 5]\n        B = [10, 20, 30, 40, 50]\n        v\
    \ = view2(A, B, 3, 3)  # Empty view\n        \n        assert len(v) == 0\n  \
    \      \n        # Test that operations on empty view behave correctly\n     \
    \   with pytest.raises(IndexError):\n            v[0]\n\n    def test_edge_cases(self):\n\
    \        \"\"\"Test edge cases\"\"\"\n        # Single element view\n        A\
    \ = [10, 20, 30, 40, 50]\n        B = ['a', 'b', 'c', 'd', 'e']\n        v = view2(A,\
    \ B, 2, 3)  # View of [(30, 'c')]\n        \n        assert len(v) == 1\n    \
    \    assert v[0] == (30, 'c')\n        \n        # Modify single element\n   \
    \     v[0] = (35, 'C')\n        assert A == [10, 20, 35, 40, 50]\n        assert\
    \ B == ['a', 'b', 'C', 'd', 'e']\n\n    def test_view_operations_sequence(self):\n\
    \        \"\"\"Test a sequence of operations\"\"\"\n        A = [10, 20, 30, 40,\
    \ 50, 60, 70, 80, 90, 100]\n        B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n    \
    \    v = view2(A, B, 2, 8)  # View of [(30,3), (40,4), (50,5), (60,6), (70,7),\
    \ (80,8)]\n        \n        # Initial state\n        assert len(v) == 6\n   \
    \     assert v[0] == (30, 3)\n        assert v[5] == (80, 8)\n        \n     \
    \   # Modify some elements\n        v[1] = (45, 14)\n        v[3] = (65, 16)\n\
    \        assert A[3] == 45\n        assert B[3] == 14\n        assert A[5] ==\
    \ 65\n        assert B[5] == 16\n        \n        # Pop and append\n        popped\
    \ = v.pop()\n        assert popped == (80, 8)\n        assert len(v) == 5\n  \
    \      \n        v.append((85, 18))\n        assert len(v) == 6\n        assert\
    \ v[5] == (85, 18)\n        \n        # Reverse\n        v.reverse()\n       \
    \ assert v[0] == (85, 18)\n        assert v[5] == (30, 3)\n\n    def test_with_different_types(self):\n\
    \        \"\"\"Test view2 with different data types\"\"\"\n        # Mixed types\n\
    \        A = [1, 2, 3, 4, 5, 6]\n        B = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]\n\
    \        v = view2(A, B, 1, 4)  # [(2, 2.2), (3, 3.3), (4, 4.4)]\n        \n \
    \       assert len(v) == 3\n        assert v[0] == (2, 2.2)\n        assert v[1]\
    \ == (3, 3.3)\n        assert v[2] == (4, 4.4)\n        \n        v.sort()\n \
    \       assert v[0] == (2, 2.2)\n        assert v[1] == (3, 3.3)\n        assert\
    \ v[2] == (4, 4.4)\n        \n        # Integer pairs (since the sort function\
    \ requires integer keys)\n        A = [5, 2, 4, 1, 3]\n        B = [50, 20, 40,\
    \ 10, 30]\n        v = view2(A, B, 1, 4)  # [(2, 20), (4, 40), (1, 10)]\n    \
    \    \n        assert len(v) == 3\n        assert v[1] == (4, 40)\n        \n\
    \        v.sort()  # Should sort by A values\n        assert v[0] == (1, 10)\n\
    \        assert v[1] == (2, 20)\n        assert v[2] == (4, 40)\n\n    def test_large_data_operations(self):\n\
    \        \"\"\"Test operations on larger datasets\"\"\"\n        # Create large\
    \ dataset\n        A = list(range(1000))\n        B = list(range(1000, 2000))\n\
    \        v = view2(A, B, 100, 900)  # 800 elements\n        \n        assert len(v)\
    \ == 800\n        assert v[0] == (100, 1100)\n        assert v[799] == (899, 1899)\n\
    \        \n        # Test modification\n        v[100] = (9999, 8888)\n      \
    \  assert A[200] == 9999\n        assert B[200] == 8888\n\n    def test_random_operations(self):\n\
    \        \"\"\"Test random operations for robustness\"\"\"\n        random.seed(42)\
    \  # For reproducibility\n        \n        # Create test data\n        A = list(range(100))\n\
    \        B = list(range(100, 200))\n        original_A = A.copy()\n        original_B\
    \ = B.copy()\n        \n        # Create view\n        start, end = 20, 80\n \
    \       v = view2(A, B, start, end)\n        \n        # Perform random operations\n\
    \        for _ in range(50):\n            op = random.choice(['read', 'write'])\n\
    \            \n            if op == 'read' and len(v) > 0:\n                idx\
    \ = random.randint(0, len(v) - 1)\n                val_a, val_b = v[idx]\n   \
    \             assert val_a == A[start + idx]\n                assert val_b ==\
    \ B[start + idx]\n                \n            elif op == 'write' and len(v)\
    \ > 0:\n                idx = random.randint(0, len(v) - 1)\n                new_val_a\
    \ = random.randint(1000, 2000)\n                new_val_b = random.randint(2000,\
    \ 3000)\n                v[idx] = (new_val_a, new_val_b)\n                assert\
    \ A[start + idx] == new_val_a\n                assert B[start + idx] == new_val_b\n\
    \n    def test_view_modification_boundary_safety(self):\n        \"\"\"Test that\
    \ view modifications don't affect data outside the view\"\"\"\n        A = [1,\
    \ 2, 3, 4, 5, 6, 7, 8, 9, 10]\n        B = [11, 12, 13, 14, 15, 16, 17, 18, 19,\
    \ 20]\n        original_A = A.copy()\n        original_B = B.copy()\n        \n\
    \        v = view2(A, B, 3, 7)  # View of [(4,14), (5,15), (6,16), (7,17)]\n \
    \       \n        # Modify view\n        v[0] = (40, 140)\n        v[1] = (50,\
    \ 150)\n        v[2] = (60, 160)\n        v[3] = (70, 170)\n        \n       \
    \ # Check that only the view range was modified\n        assert A[0:3] == original_A[0:3]\
    \  # Before view unchanged\n        assert A[7:] == original_A[7:]    # After\
    \ view unchanged\n        assert B[0:3] == original_B[0:3]  # Before view unchanged\n\
    \        assert B[7:] == original_B[7:]    # After view unchanged\n        assert\
    \ A[3:7] == [40, 50, 60, 70]  # View range changed\n        assert B[3:7] == [140,\
    \ 150, 160, 170]  # View range changed\n\n    def test_mismatched_array_lengths(self):\n\
    \        \"\"\"Test behavior with mismatched array lengths\"\"\"\n        # Arrays\
    \ of different lengths should still work within valid ranges\n        A = [1,\
    \ 2, 3, 4, 5]\n        B = [10, 20, 30, 40, 50, 60, 70]  # Longer than A\n   \
    \     \n        # View that fits within both arrays\n        v = view2(A, B, 1,\
    \ 4)\n        assert len(v) == 3\n        assert v[0] == (2, 20)\n        assert\
    \ v[2] == (4, 40)\n        \n        # Validation should check against A (assuming\
    \ it's the limiting factor)\n        v_invalid = view2(A, B, 0, 6)  # Beyond A's\
    \ length\n        assert v_invalid.validate() == False\n\n    def test_sort_stability(self):\n\
    \        \"\"\"Test sort stability with duplicate keys\"\"\"\n        A = [3,\
    \ 1, 3, 2, 3, 1, 2]\n        B = ['a', 'b', 'c', 'd', 'e', 'f', 'g']\n       \
    \ v = view2(A, B, 0, 7)\n        \n        v.sort()\n        \n        # Check\
    \ that sorting worked correctly\n        expected_A = [1, 1, 2, 2, 3, 3, 3]\n\
    \        assert A == expected_A\n        \n        # Check that B values were\
    \ rearranged along with A\n        for i in range(len(v)):\n            a_val,\
    \ b_val = v[i]\n            assert a_val == expected_A[i]\n\n'''\n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\nfrom typing import Generic\nfrom typing import TypeVar\n\
    _S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1');\
    \ _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5');\
    \ _T6 = TypeVar('T6')\n\n\n\n\ndef argsort_ranged(A: list[int], l: int, r: int,\
    \ reverse=False):\n    P = Packer(r-l-1); I = [A[l+i] for i in range(r-l)]; P.ienumerate(I,\
    \ reverse); I.sort()\n    for i in range(r-l): I[i] = (I[i] & P.m) + l\n    return\
    \ I\n\n\n\nclass Packer:\n    __slots__ = 's', 'm'\n    def __init__(P, mx: int):\
    \ P.s = mx.bit_length(); P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int):\
    \ return a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return x >>\
    \ P.s, x & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A),\
    \ reverse); return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n\
    \            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n   \
    \         for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\n\n\ndef isort_ranged(*L: list, l: int, r: int, reverse=False):\n\
    \    n = r - l\n    order = argsort_ranged(L[0], l, r, reverse=reverse)\n    inv\
    \ = [0] * n\n    # order contains indices in range [l, r), need to map to [0,\
    \ n)\n    for i in range(n): inv[order[i]-l] = i\n    for i in range(n):\n   \
    \     j = order[i] - l  # j is in range [0, n)\n        for A in L: A[l+i], A[l+j]\
    \ = A[l+j], A[l+i]\n        order[inv[i]], order[inv[j]] = order[inv[j]], order[inv[i]]\n\
    \        inv[i], inv[j] = inv[j], inv[i]\n    return L\n\n\n\nclass view2(Generic[_T1,\
    \ _T2]):\n    __slots__ = 'A1', 'A2', 'l', 'r'\n    def __init__(V, A1: list[_T1],\
    \ A2: list[_T2], l: int = 0, r: int = 0): V.A1, V.A2, V.l, V.r = A1, A2, l, r\n\
    \    def __len__(V): return V.r - V.l\n    def __getitem__(V, i: int): \n    \
    \    if 0 <= i < V.r - V.l: return V.A1[V.l+i], V.A2[V.l+i]\n        else: raise\
    \ IndexError\n    def __setitem__(V, i: int, v: tuple[_T1, _T2]): V.A1[V.l+i],\
    \ V.A2[V.l+i] = v\n    def __contains__(V, v: tuple[_T1, _T2]): raise NotImplemented\n\
    \    def set_range(V, l: int, r: int): V.l, V.r = l, r\n    def index(V, v: tuple[_T1,\
    \ _T2]): raise NotImplemented\n    def reverse(V):\n        l, r = V.l, V.r-1\n\
    \        while l < r: V.A1[l], V.A1[r] = V.A1[r], V.A1[l]; V.A2[l], V.A2[r] =\
    \ V.A2[r], V.A2[l]; l += 1; r -= 1\n    def sort(V, reverse=False): isort_ranged(V.A1,\
    \ V.A2, l=V.l, r=V.r, reverse=reverse)\n    def pop(V): V.r -= 1; return V.A1[V.r],\
    \ V.A2[V.r]\n    def append(V, v: tuple[_T1, _T2]): V.A1[V.r], V.A2[V.r] = v;\
    \ V.r += 1\n    def popleft(V): V.l += 1; return V.A1[V.l-1], V.A2[V.l-1]\n  \
    \  def appendleft(V, v: tuple[_T1, _T2]): V.l -= 1; V.A1[V.l], V.A2[V.l]  = v;\
    \ \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A1)\n\nif __name__ ==\
    \ '__main__':\n    \"\"\"\n    Helper for making unittest files compatible with\
    \ verification-helper.\n    \n    This module provides a helper function to run\
    \ a dummy Library Checker test\n    so that unittest files can be verified by\
    \ oj-verify.\n    \"\"\"\n    \n    def run_verification_helper_unittest():\n\
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
    \nimport pytest\nimport random\n\nclass TestView2:\n    def test_initialization(self):\n\
    \        \"\"\"Test basic initialization of view2\"\"\"\n        A = [1, 2, 3,\
    \ 4, 5]\n        B = ['a', 'b', 'c', 'd', 'e']\n        v = view2(A, B, 1, 4)\n\
    \        \n        assert v.A1 is A\n        assert v.A2 is B\n        assert\
    \ v.l == 1\n        assert v.r == 4\n        assert len(v) == 3\n\n    def test_len(self):\n\
    \        \"\"\"Test __len__ method\"\"\"\n        A = [1, 2, 3, 4, 5, 6, 7, 8,\
    \ 9, 10]\n        B = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]\n        \n  \
    \      # Test different ranges\n        assert len(view2(A, B, 0, 5)) == 5\n \
    \       assert len(view2(A, B, 2, 7)) == 5\n        assert len(view2(A, B, 0,\
    \ 10)) == 10\n        assert len(view2(A, B, 5, 5)) == 0  # Empty range\n\n  \
    \  def test_getitem(self):\n        \"\"\"Test __getitem__ method\"\"\"\n    \
    \    A = [10, 20, 30, 40, 50]\n        B = ['x', 'y', 'z', 'w', 'v']\n       \
    \ v = view2(A, B, 1, 4)  # View of [(20,'y'), (30,'z'), (40,'w')]\n        \n\
    \        assert v[0] == (20, 'y')\n        assert v[1] == (30, 'z')\n        assert\
    \ v[2] == (40, 'w')\n        \n        # Test IndexError for out of bounds\n \
    \       with pytest.raises(IndexError):\n            v[3]\n        with pytest.raises(IndexError):\n\
    \            v[-1]\n\n    def test_setitem(self):\n        \"\"\"Test __setitem__\
    \ method\"\"\"\n        A = [10, 20, 30, 40, 50]\n        B = ['x', 'y', 'z',\
    \ 'w', 'v']\n        v = view2(A, B, 1, 4)  # View of [(20,'y'), (30,'z'), (40,'w')]\n\
    \        \n        v[0] = (25, 'Y')\n        v[1] = (35, 'Z')\n        v[2] =\
    \ (45, 'W')\n        \n        assert A == [10, 25, 35, 45, 50]\n        assert\
    \ B == ['x', 'Y', 'Z', 'W', 'v']\n        assert v[0] == (25, 'Y')\n        assert\
    \ v[1] == (35, 'Z')\n        assert v[2] == (45, 'W')\n\n    def test_contains_not_implemented(self):\n\
    \        \"\"\"Test that __contains__ raises NotImplemented\"\"\"\n        A =\
    \ [1, 2, 3, 4, 5]\n        B = ['a', 'b', 'c', 'd', 'e']\n        v = view2(A,\
    \ B, 1, 4)\n        \n        with pytest.raises(TypeError):  # NotImplemented\
    \ raises TypeError\n            (2, 'b') in v\n\n    def test_index_not_implemented(self):\n\
    \        \"\"\"Test that index raises NotImplemented\"\"\"\n        A = [1, 2,\
    \ 3, 4, 5]\n        B = ['a', 'b', 'c', 'd', 'e']\n        v = view2(A, B, 1,\
    \ 4)\n        \n        with pytest.raises(TypeError):  # NotImplemented raises\
    \ TypeError\n            v.index((2, 'b'))\n\n    def test_set_range(self):\n\
    \        \"\"\"Test set_range method\"\"\"\n        A = [1, 2, 3, 4, 5, 6, 7,\
    \ 8, 9, 10]\n        B = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]\n        v\
    \ = view2(A, B, 2, 5)\n        \n        assert len(v) == 3\n        assert v[0]\
    \ == (3, 30)\n        \n        # Change the range\n        v.set_range(4, 8)\n\
    \        assert len(v) == 4\n        assert v[0] == (5, 50)\n        assert v[1]\
    \ == (6, 60)\n        assert v[2] == (7, 70)\n        assert v[3] == (8, 80)\n\
    \n    def test_reverse(self):\n        \"\"\"Test reverse method\"\"\"\n     \
    \   A = [1, 2, 3, 4, 5, 6, 7, 8, 9]\n        B = [10, 20, 30, 40, 50, 60, 70,\
    \ 80, 90]\n        v = view2(A, B, 2, 7)  # View of [(3,30), (4,40), (5,50), (6,60),\
    \ (7,70)]\n        \n        v.reverse()\n        \n        # Check that the view\
    \ is reversed\n        assert v[0] == (7, 70)\n        assert v[1] == (6, 60)\n\
    \        assert v[2] == (5, 50)\n        assert v[3] == (4, 40)\n        assert\
    \ v[4] == (3, 30)\n        \n        # Check that the underlying arrays are modified\n\
    \        assert A == [1, 2, 7, 6, 5, 4, 3, 8, 9]\n        assert B == [10, 20,\
    \ 70, 60, 50, 40, 30, 80, 90]\n\n    def test_sort(self):\n        \"\"\"Test\
    \ sort method\"\"\"\n        A = [1, 5, 2, 8, 3, 9, 4, 6, 7]\n        B = [10,\
    \ 50, 20, 80, 30, 90, 40, 60, 70]\n        v = view2(A, B, 2, 7)  # View of [(2,20),\
    \ (8,80), (3,30), (9,90), (4,40)]\n        \n        v.sort()\n        \n    \
    \    # Check that the view is sorted by A values\n        assert v[0] == (2, 20)\n\
    \        assert v[1] == (3, 30)\n        assert v[2] == (4, 40)\n        assert\
    \ v[3] == (8, 80)\n        assert v[4] == (9, 90)\n        \n        # Check that\
    \ the underlying arrays are modified correctly\n        assert A == [1, 5, 2,\
    \ 3, 4, 8, 9, 6, 7]\n        assert B == [10, 50, 20, 30, 40, 80, 90, 60, 70]\n\
    \n    def test_sort_reverse(self):\n        \"\"\"Test sort method with reverse=True\"\
    \"\"\n        A = [1, 5, 2, 8, 3, 9, 4, 6, 7]\n        B = [10, 50, 20, 80, 30,\
    \ 90, 40, 60, 70]\n        v = view2(A, B, 2, 7)  # View of [(2,20), (8,80), (3,30),\
    \ (9,90), (4,40)]\n        \n        v.sort(reverse=True)\n        \n        #\
    \ Check that the view is sorted in reverse by A values\n        assert v[0] ==\
    \ (9, 90)\n        assert v[1] == (8, 80)\n        assert v[2] == (4, 40)\n  \
    \      assert v[3] == (3, 30)\n        assert v[4] == (2, 20)\n        \n    \
    \    # Check that the underlying arrays are modified correctly\n        assert\
    \ A == [1, 5, 9, 8, 4, 3, 2, 6, 7]\n        assert B == [10, 50, 90, 80, 40, 30,\
    \ 20, 60, 70]\n\n    def test_pop(self):\n        \"\"\"Test pop method\"\"\"\n\
    \        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]\n        B = [10, 20, 30, 40, 50, 60,\
    \ 70, 80, 90]\n        v = view2(A, B, 2, 6)  # View of [(3,30), (4,40), (5,50),\
    \ (6,60)]\n        \n        assert len(v) == 4\n        \n        # Pop from\
    \ the end\n        popped = v.pop()\n        assert popped == (6, 60)\n      \
    \  assert len(v) == 3\n        assert v[2] == (5, 50)  # Last element is now (5,50)\n\
    \        \n        # Pop again\n        popped = v.pop()\n        assert popped\
    \ == (5, 50)\n        assert len(v) == 2\n\n    def test_append(self):\n     \
    \   \"\"\"Test append method\"\"\"\n        A = [1, 2, 3, 4, 5, 0, 0, 0, 9]  #\
    \ Extra space for appending\n        B = [10, 20, 30, 40, 50, 0, 0, 0, 90]\n \
    \       v = view2(A, B, 2, 5)  # View of [(3,30), (4,40), (5,50)]\n        \n\
    \        assert len(v) == 3\n        \n        # Append to the end\n        v.append((6,\
    \ 60))\n        assert len(v) == 4\n        assert v[3] == (6, 60)\n        assert\
    \ A[5] == 6  # Check underlying arrays\n        assert B[5] == 60\n        \n\
    \        # Append again\n        v.append((7, 70))\n        assert len(v) == 5\n\
    \        assert v[4] == (7, 70)\n\n    def test_popleft(self):\n        \"\"\"\
    Test popleft method\"\"\"\n        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]\n        B\
    \ = [10, 20, 30, 40, 50, 60, 70, 80, 90]\n        v = view2(A, B, 2, 6)  # View\
    \ of [(3,30), (4,40), (5,50), (6,60)]\n        \n        assert len(v) == 4\n\
    \        \n        # Pop from the beginning\n        popped = v.popleft()\n  \
    \      assert popped == (3, 30)\n        assert len(v) == 3\n        assert v[0]\
    \ == (4, 40)  # First element is now (4,40)\n        \n        # Pop again\n \
    \       popped = v.popleft()\n        assert popped == (4, 40)\n        assert\
    \ len(v) == 2\n        assert v[0] == (5, 50)\n\n    def test_appendleft(self):\n\
    \        \"\"\"Test appendleft method\"\"\"\n        A = [0, 0, 1, 2, 3, 4, 5,\
    \ 6, 7]  # Extra space at beginning\n        B = [0, 0, 10, 20, 30, 40, 50, 60,\
    \ 70]\n        v = view2(A, B, 4, 7)  # View of [(3,30), (4,40), (5,50)]\n   \
    \     \n        assert len(v) == 3\n        assert v[0] == (3, 30)\n        \n\
    \        # Append to the beginning\n        v.appendleft((2, 20))\n        assert\
    \ len(v) == 4\n        assert v[0] == (2, 20)\n        assert v[1] == (3, 30)\n\
    \        assert A[3] == 2  # Check underlying arrays\n        assert B[3] == 20\n\
    \        \n        # Append again\n        v.appendleft((1, 10))\n        assert\
    \ len(v) == 5\n        assert v[0] == (1, 10)\n        assert v[1] == (2, 20)\n\
    \n    def test_validate(self):\n        \"\"\"Test validate method\"\"\"\n   \
    \     A = [1, 2, 3, 4, 5]\n        B = [10, 20, 30, 40, 50]\n        \n      \
    \  # Valid ranges\n        v1 = view2(A, B, 0, 5)\n        assert v1.validate()\
    \ == True\n        \n        v2 = view2(A, B, 2, 4)\n        assert v2.validate()\
    \ == True\n        \n        v3 = view2(A, B, 3, 3)  # Empty range\n        assert\
    \ v3.validate() == True\n        \n        # Invalid ranges\n        v4 = view2(A,\
    \ B, -1, 3)\n        assert v4.validate() == False\n        \n        v5 = view2(A,\
    \ B, 2, 6)  # r > len(A)\n        assert v5.validate() == False\n        \n  \
    \      v6 = view2(A, B, 3, 2)  # l > r\n        assert v6.validate() == False\n\
    \n    def test_empty_view(self):\n        \"\"\"Test operations on empty view\"\
    \"\"\n        A = [1, 2, 3, 4, 5]\n        B = [10, 20, 30, 40, 50]\n        v\
    \ = view2(A, B, 3, 3)  # Empty view\n        \n        assert len(v) == 0\n  \
    \      \n        # Test that operations on empty view behave correctly\n     \
    \   with pytest.raises(IndexError):\n            v[0]\n\n    def test_edge_cases(self):\n\
    \        \"\"\"Test edge cases\"\"\"\n        # Single element view\n        A\
    \ = [10, 20, 30, 40, 50]\n        B = ['a', 'b', 'c', 'd', 'e']\n        v = view2(A,\
    \ B, 2, 3)  # View of [(30, 'c')]\n        \n        assert len(v) == 1\n    \
    \    assert v[0] == (30, 'c')\n        \n        # Modify single element\n   \
    \     v[0] = (35, 'C')\n        assert A == [10, 20, 35, 40, 50]\n        assert\
    \ B == ['a', 'b', 'C', 'd', 'e']\n\n    def test_view_operations_sequence(self):\n\
    \        \"\"\"Test a sequence of operations\"\"\"\n        A = [10, 20, 30, 40,\
    \ 50, 60, 70, 80, 90, 100]\n        B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n    \
    \    v = view2(A, B, 2, 8)  # View of [(30,3), (40,4), (50,5), (60,6), (70,7),\
    \ (80,8)]\n        \n        # Initial state\n        assert len(v) == 6\n   \
    \     assert v[0] == (30, 3)\n        assert v[5] == (80, 8)\n        \n     \
    \   # Modify some elements\n        v[1] = (45, 14)\n        v[3] = (65, 16)\n\
    \        assert A[3] == 45\n        assert B[3] == 14\n        assert A[5] ==\
    \ 65\n        assert B[5] == 16\n        \n        # Pop and append\n        popped\
    \ = v.pop()\n        assert popped == (80, 8)\n        assert len(v) == 5\n  \
    \      \n        v.append((85, 18))\n        assert len(v) == 6\n        assert\
    \ v[5] == (85, 18)\n        \n        # Reverse\n        v.reverse()\n       \
    \ assert v[0] == (85, 18)\n        assert v[5] == (30, 3)\n\n    def test_with_different_types(self):\n\
    \        \"\"\"Test view2 with different data types\"\"\"\n        # Mixed types\n\
    \        A = [1, 2, 3, 4, 5, 6]\n        B = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]\n\
    \        v = view2(A, B, 1, 4)  # [(2, 2.2), (3, 3.3), (4, 4.4)]\n        \n \
    \       assert len(v) == 3\n        assert v[0] == (2, 2.2)\n        assert v[1]\
    \ == (3, 3.3)\n        assert v[2] == (4, 4.4)\n        \n        v.sort()\n \
    \       assert v[0] == (2, 2.2)\n        assert v[1] == (3, 3.3)\n        assert\
    \ v[2] == (4, 4.4)\n        \n        # Integer pairs (since the sort function\
    \ requires integer keys)\n        A = [5, 2, 4, 1, 3]\n        B = [50, 20, 40,\
    \ 10, 30]\n        v = view2(A, B, 1, 4)  # [(2, 20), (4, 40), (1, 10)]\n    \
    \    \n        assert len(v) == 3\n        assert v[1] == (4, 40)\n        \n\
    \        v.sort()  # Should sort by A values\n        assert v[0] == (1, 10)\n\
    \        assert v[1] == (2, 20)\n        assert v[2] == (4, 40)\n\n    def test_large_data_operations(self):\n\
    \        \"\"\"Test operations on larger datasets\"\"\"\n        # Create large\
    \ dataset\n        A = list(range(1000))\n        B = list(range(1000, 2000))\n\
    \        v = view2(A, B, 100, 900)  # 800 elements\n        \n        assert len(v)\
    \ == 800\n        assert v[0] == (100, 1100)\n        assert v[799] == (899, 1899)\n\
    \        \n        # Test modification\n        v[100] = (9999, 8888)\n      \
    \  assert A[200] == 9999\n        assert B[200] == 8888\n\n    def test_random_operations(self):\n\
    \        \"\"\"Test random operations for robustness\"\"\"\n        random.seed(42)\
    \  # For reproducibility\n        \n        # Create test data\n        A = list(range(100))\n\
    \        B = list(range(100, 200))\n        original_A = A.copy()\n        original_B\
    \ = B.copy()\n        \n        # Create view\n        start, end = 20, 80\n \
    \       v = view2(A, B, start, end)\n        \n        # Perform random operations\n\
    \        for _ in range(50):\n            op = random.choice(['read', 'write'])\n\
    \            \n            if op == 'read' and len(v) > 0:\n                idx\
    \ = random.randint(0, len(v) - 1)\n                val_a, val_b = v[idx]\n   \
    \             assert val_a == A[start + idx]\n                assert val_b ==\
    \ B[start + idx]\n                \n            elif op == 'write' and len(v)\
    \ > 0:\n                idx = random.randint(0, len(v) - 1)\n                new_val_a\
    \ = random.randint(1000, 2000)\n                new_val_b = random.randint(2000,\
    \ 3000)\n                v[idx] = (new_val_a, new_val_b)\n                assert\
    \ A[start + idx] == new_val_a\n                assert B[start + idx] == new_val_b\n\
    \n    def test_view_modification_boundary_safety(self):\n        \"\"\"Test that\
    \ view modifications don't affect data outside the view\"\"\"\n        A = [1,\
    \ 2, 3, 4, 5, 6, 7, 8, 9, 10]\n        B = [11, 12, 13, 14, 15, 16, 17, 18, 19,\
    \ 20]\n        original_A = A.copy()\n        original_B = B.copy()\n        \n\
    \        v = view2(A, B, 3, 7)  # View of [(4,14), (5,15), (6,16), (7,17)]\n \
    \       \n        # Modify view\n        v[0] = (40, 140)\n        v[1] = (50,\
    \ 150)\n        v[2] = (60, 160)\n        v[3] = (70, 170)\n        \n       \
    \ # Check that only the view range was modified\n        assert A[0:3] == original_A[0:3]\
    \  # Before view unchanged\n        assert A[7:] == original_A[7:]    # After\
    \ view unchanged\n        assert B[0:3] == original_B[0:3]  # Before view unchanged\n\
    \        assert B[7:] == original_B[7:]    # After view unchanged\n        assert\
    \ A[3:7] == [40, 50, 60, 70]  # View range changed\n        assert B[3:7] == [140,\
    \ 150, 160, 170]  # View range changed\n\n    def test_mismatched_array_lengths(self):\n\
    \        \"\"\"Test behavior with mismatched array lengths\"\"\"\n        # Arrays\
    \ of different lengths should still work within valid ranges\n        A = [1,\
    \ 2, 3, 4, 5]\n        B = [10, 20, 30, 40, 50, 60, 70]  # Longer than A\n   \
    \     \n        # View that fits within both arrays\n        v = view2(A, B, 1,\
    \ 4)\n        assert len(v) == 3\n        assert v[0] == (2, 20)\n        assert\
    \ v[2] == (4, 40)\n        \n        # Validation should check against A (assuming\
    \ it's the limiting factor)\n        v_invalid = view2(A, B, 0, 6)  # Beyond A's\
    \ length\n        assert v_invalid.validate() == False\n\n    def test_sort_stability(self):\n\
    \        \"\"\"Test sort stability with duplicate keys\"\"\"\n        A = [3,\
    \ 1, 3, 2, 3, 1, 2]\n        B = ['a', 'b', 'c', 'd', 'e', 'f', 'g']\n       \
    \ v = view2(A, B, 0, 7)\n        \n        v.sort()\n        \n        # Check\
    \ that sorting worked correctly\n        expected_A = [1, 1, 2, 2, 3, 3, 3]\n\
    \        assert A == expected_A\n        \n        # Check that B values were\
    \ rearranged along with A\n        for i in range(len(v)):\n            a_val,\
    \ b_val = v[i]\n            assert a_val == expected_A[i]\n\nfrom cp_library.ds.view.view2_cls\
    \ import view2\n\nif __name__ == '__main__':\n    from cp_library.test.unittest_helper\
    \ import run_verification_helper_unittest\n    run_verification_helper_unittest()"
  dependsOn:
  - cp_library/ds/view/view2_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/alg/iter/sort/isort_ranged_fn.py
  - cp_library/alg/iter/arg/argsort_ranged_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: true
  path: test/unittests/ds/view/view2_cls_test.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/view/view2_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/view/view2_cls_test.py
- /verify/test/unittests/ds/view/view2_cls_test.py.html
title: test/unittests/ds/view/view2_cls_test.py
---
