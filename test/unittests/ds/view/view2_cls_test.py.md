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
    \nimport pytest\nimport random\n\nclass TestView2:\n    def test_initialization(self):\n\
    \        \"\"\"Test basic initialization of view2\"\"\"\n        A = [1, 2, 3,\
    \ 4, 5]\n        B = ['a', 'b', 'c', 'd', 'e']\n        v = view2(A, B, 1, 4)\n\
    \        \n        assert v.A is A\n        assert v.B is B\n        assert v.l\
    \ == 1\n        assert v.r == 4\n        assert len(v) == 3\n\n    def test_len(self):\n\
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
    \ b_val = v[i]\n            assert a_val == expected_A[i]\n\n\n'''\n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\n\n\ndef argsort_ranged(A: list[int], l: int, r: int,\
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
    \        inv[i], inv[j] = inv[j], inv[i]\n    return L\nfrom typing import Generic\n\
    from typing import TypeVar\n_S = TypeVar('S')\n_T = TypeVar('T')\n_U = TypeVar('U')\n\
    _T1 = TypeVar('T1')\n_T2 = TypeVar('T2')\n_T3 = TypeVar('T3')\n_T4 = TypeVar('T4')\n\
    _T5 = TypeVar('T5')\n_T6 = TypeVar('T6')\n\n\n\nclass view2(Generic[_S, _T]):\n\
    \    __slots__ = 'A', 'B', 'l', 'r'\n    def __init__(V, A: list[_S], B: list[_T],\
    \ l: int, r: int): V.A, V.B, V.l, V.r = A, B, l, r\n    def __len__(V): return\
    \ V.r - V.l\n    def __getitem__(V, i: int): \n        if 0 <= i < V.r - V.l:\
    \ return V.A[V.l+i], V.B[V.l+i]\n        else: raise IndexError\n    def __setitem__(V,\
    \ i: int, v: tuple[_S, _T]): V.A[V.l+i], V.B[V.l+i] = v\n    def __contains__(V,\
    \ v: tuple[_S, _T]): raise NotImplemented\n    def set_range(V, l: int, r: int):\
    \ V.l, V.r = l, r\n    def index(V, v: tuple[_S, _T]): raise NotImplemented\n\
    \    def reverse(V):\n        l, r = V.l, V.r-1\n        while l < r: V.A[l],\
    \ V.A[r] = V.A[r], V.A[l]; V.B[l], V.B[r] = V.B[r], V.B[l]; l += 1; r -= 1\n \
    \   def sort(V, reverse=False): isort_ranged(V.A, V.B, l=V.l, r=V.r, reverse=reverse)\n\
    \    def pop(V): V.r -= 1; return V.A[V.r], V.B[V.r]\n    def append(V, v: tuple[_S,\
    \ _T]): V.A[V.r], V.B[V.r] = v; V.r += 1\n    def popleft(V): V.l += 1; return\
    \ V.A[V.l-1], V.B[V.l-1]\n    def appendleft(V, v: tuple[_S, _T]): V.l -= 1; V.A[V.l],\
    \ V.B[V.l]  = v; \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\n\
    if __name__ == '__main__':\n    \"\"\"\n    Helper for making unittest files compatible\
    \ with verification-helper.\n    \n    This module provides a helper function\
    \ to run a dummy Library Checker test\n    so that unittest files can be verified\
    \ by oj-verify.\n    \"\"\"\n    \n    def run_verification_helper_unittest():\n\
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
    import pytest\nimport random\n\nclass TestView2:\n    def test_initialization(self):\n\
    \        \"\"\"Test basic initialization of view2\"\"\"\n        A = [1, 2, 3,\
    \ 4, 5]\n        B = ['a', 'b', 'c', 'd', 'e']\n        v = view2(A, B, 1, 4)\n\
    \        \n        assert v.A is A\n        assert v.B is B\n        assert v.l\
    \ == 1\n        assert v.r == 4\n        assert len(v) == 3\n\n    def test_len(self):\n\
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
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/iter/arg/argsort_ranged_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: true
  path: test/unittests/ds/view/view2_cls_test.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/view/view2_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/view/view2_cls_test.py
- /verify/test/unittests/ds/view/view2_cls_test.py.html
title: test/unittests/ds/view/view2_cls_test.py
---
