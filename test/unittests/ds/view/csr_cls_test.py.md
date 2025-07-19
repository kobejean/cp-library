---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/csr_cls.py
    title: cp_library/ds/view/csr_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view_cls.py
    title: cp_library/ds/view/view_cls.py
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
    \nimport pytest\nimport random\n\nclass TestCSR:\n    def test_initialization(self):\n\
    \        \"\"\"Test basic initialization of CSR\"\"\"\n        A = [1, 2, 3, 4,\
    \ 5, 6]\n        O = [0, 2, 4, 6]  # 3 rows: [1,2], [3,4], [5,6]\n        csr\
    \ = CSR(A, O)\n        \n        assert csr.A is A\n        assert csr.O is O\n\
    \        assert len(csr) == 3\n\n    def test_len(self):\n        \"\"\"Test __len__\
    \ method\"\"\"\n        A = [1, 2, 3, 4, 5]\n        O = [0, 2, 3, 5]  # 3 rows:\
    \ [1,2], [3], [4,5]\n        csr = CSR(A, O)\n        \n        assert len(csr)\
    \ == 3\n        \n        # Empty CSR\n        empty_csr = CSR([], [0])\n    \
    \    assert len(empty_csr) == 0\n\n    def test_getitem(self):\n        \"\"\"\
    Test __getitem__ method (returns temporary view)\"\"\"\n        A = [10, 20, 30,\
    \ 40, 50, 60]\n        O = [0, 2, 4, 6]  # 3 rows: [10,20], [30,40], [50,60]\n\
    \        csr = CSR(A, O)\n        \n        # Test temporary access - each call\
    \ returns the same view object but points to different rows\n        # Test row\
    \ 0\n        row = csr[0]\n        assert len(row) == 2\n        assert row[0]\
    \ == 10\n        assert row[1] == 20\n        \n        # Test row 1 - same view\
    \ object, different range\n        row = csr[1]\n        assert len(row) == 2\n\
    \        assert row[0] == 30\n        assert row[1] == 40\n        \n        #\
    \ Test row 2 - same view object, different range\n        row = csr[2]\n     \
    \   assert len(row) == 2\n        assert row[0] == 50\n        assert row[1] ==\
    \ 60\n\n    def test_call(self):\n        \"\"\"Test __call__ method (direct element\
    \ access)\"\"\"\n        A = [10, 20, 30, 40, 50, 60]\n        O = [0, 2, 4, 6]\
    \  # 3 rows: [10,20], [30,40], [50,60]\n        csr = CSR(A, O)\n        \n  \
    \      # Direct access to elements\n        assert csr(0, 0) == 10\n        assert\
    \ csr(0, 1) == 20\n        assert csr(1, 0) == 30\n        assert csr(1, 1) ==\
    \ 40\n        assert csr(2, 0) == 50\n        assert csr(2, 1) == 60\n\n    def\
    \ test_set(self):\n        \"\"\"Test set method\"\"\"\n        A = [10, 20, 30,\
    \ 40, 50, 60]\n        O = [0, 2, 4, 6]  # 3 rows: [10,20], [30,40], [50,60]\n\
    \        csr = CSR(A, O)\n        \n        # Modify elements\n        csr.set(0,\
    \ 0, 15)\n        csr.set(1, 1, 45)\n        csr.set(2, 0, 55)\n        \n   \
    \     assert A == [15, 20, 30, 45, 55, 60]\n        assert csr(0, 0) == 15\n \
    \       assert csr(1, 1) == 45\n        assert csr(2, 0) == 55\n\n    def test_getitem_method(self):\n\
    \        \"\"\"Test __getitem__ method (creates new view)\"\"\"\n        A = [1,\
    \ 2, 3, 4, 5, 6, 7, 8]\n        O = [0, 3, 5, 8]  # 3 rows: [1,2,3], [4,5], [6,7,8]\n\
    \        csr = CSR(A, O)\n        \n        # Create views for each row\n    \
    \    view0 = csr[0]\n        view1 = csr[1]\n        view2 = csr[2]\n        \n\
    \        assert len(view0) == 3\n        assert view0[0] == 1\n        assert\
    \ view0[2] == 3\n        \n        assert len(view1) == 2\n        assert view1[0]\
    \ == 4\n        assert view1[1] == 5\n        \n        assert len(view2) == 3\n\
    \        assert view2[0] == 6\n        assert view2[2] == 8\n\n    def test_bucketize(self):\n\
    \        \"\"\"Test bucketize class method\"\"\"\n        # Create buckets: bucket\
    \ 0 gets [1,3], bucket 1 gets [2], bucket 2 gets [4,5]\n        N = 3\n      \
    \  K = [0, 1, 0, 2, 2]  # Keys indicating which bucket each value goes to\n  \
    \      V = [1, 2, 3, 4, 5]  # Values to be bucketed\n        \n        csr = CSR.bucketize(N,\
    \ K, V)\n        \n        assert len(csr) == 3\n        \n        # Check bucket\
    \ 0: should contain [3, 1] (reverse order due to algorithm)\n        row0 = csr[0]\n\
    \        assert len(row0) == 2\n        assert set([row0[0], row0[1]]) == {1,\
    \ 3}\n        \n        # Check bucket 1: should contain [2]\n        row1 = csr[1]\n\
    \        assert len(row1) == 1\n        assert row1[0] == 2\n        \n      \
    \  # Check bucket 2: should contain [5, 4] (reverse order)\n        row2 = csr[2]\n\
    \        assert len(row2) == 2\n        assert set([row2[0], row2[1]]) == {4,\
    \ 5}\n\n    def test_empty_rows(self):\n        \"\"\"Test CSR with empty rows\"\
    \"\"\n        A = [1, 2, 3, 4]\n        O = [0, 2, 2, 4]  # 3 rows: [1,2], [],\
    \ [3,4]\n        csr = CSR(A, O)\n        \n        assert len(csr) == 3\n   \
    \     \n        # Row 0: [1,2]\n        row0 = csr[0]\n        assert len(row0)\
    \ == 2\n        assert row0[0] == 1\n        assert row0[1] == 2\n        \n \
    \       # Row 1: empty\n        row1 = csr[1]\n        assert len(row1) == 0\n\
    \        \n        # Row 2: [3,4]\n        row2 = csr[2]\n        assert len(row2)\
    \ == 2\n        assert row2[0] == 3\n        assert row2[1] == 4\n\n    def test_single_element_rows(self):\n\
    \        \"\"\"Test CSR with single element rows\"\"\"\n        A = [10, 20, 30]\n\
    \        O = [0, 1, 2, 3]  # 3 rows: [10], [20], [30]\n        csr = CSR(A, O)\n\
    \        \n        assert len(csr) == 3\n        \n        for i in range(3):\n\
    \            row = csr[i]\n            assert len(row) == 1\n            assert\
    \ row[0] == (i + 1) * 10\n            assert csr(i, 0) == (i + 1) * 10\n\n   \
    \ def test_view_modifications(self):\n        \"\"\"Test that view modifications\
    \ affect the underlying data\"\"\"\n        A = [1, 2, 3, 4, 5, 6]\n        O\
    \ = [0, 2, 4, 6]  # 3 rows: [1,2], [3,4], [5,6]\n        csr = CSR(A, O)\n   \
    \     \n        # Get a view and modify it\n        row1 = csr[1]\n        row1[0]\
    \ = 30\n        row1[1] = 40\n        \n        # Check that underlying data changed\n\
    \        assert A == [1, 2, 30, 40, 5, 6]\n        assert csr(1, 0) == 30\n  \
    \      assert csr(1, 1) == 40\n\n    def test_view_operations(self):\n       \
    \ \"\"\"Test various view operations\"\"\"\n        A = [5, 3, 1, 4, 2, 6]\n \
    \       O = [0, 3, 6]  # 2 rows: [5,3,1], [4,2,6]\n        csr = CSR(A, O)\n \
    \       \n        # Get views and operate on them\n        row0 = csr[0]\n   \
    \     row0.sort()\n        assert A[:3] == [1, 3, 5]\n        \n        row1 =\
    \ csr[1]\n        row1.reverse()\n        assert A[3:] == [6, 2, 4]\n\n    def\
    \ test_view_creation_behavior(self):\n        \"\"\"Test that __getitem__ creates\
    \ new view objects each time\"\"\"\n        A = [1, 2, 3, 4, 5, 6]\n        O\
    \ = [0, 2, 4, 6]  # 3 rows: [1,2], [3,4], [5,6]\n        csr = CSR(A, O)\n   \
    \     \n        # __getitem__ creates new view objects each time\n        view1\
    \ = csr[0]  # New view of row 0\n        view2 = csr[0]  # Another new view of\
    \ row 0\n        \n        # Should be different objects but point to the same\
    \ data\n        assert view1 is not view2  # Different objects\n        \n   \
    \     # But should have the same data\n        assert len(view1) == len(view2)\
    \ == 2\n        assert view1[0] == view2[0] == 1  # Row 0 data\n        assert\
    \ view1[1] == view2[1] == 2  # Row 0 data\n        \n        # Views of different\
    \ rows should also be independent\n        row0_view = csr[0]\n        row1_view\
    \ = csr[1] \n        \n        assert row0_view is not row1_view  # Different\
    \ objects\n        assert len(row0_view) == 2\n        assert row0_view[0] ==\
    \ 1  # Row 0 data\n        assert len(row1_view) == 2  \n        assert row1_view[0]\
    \ == 3  # Row 1 data\n\n    def test_large_csr(self):\n        \"\"\"Test CSR\
    \ with larger data\"\"\"\n        # Create 100 rows with 10 elements each\n  \
    \      A = list(range(1000))\n        O = [i * 10 for i in range(101)]  # 100\
    \ rows\n        csr = CSR(A, O)\n        \n        assert len(csr) == 100\n  \
    \      \n        # Test random access\n        assert csr(50, 5) == 505\n    \
    \    assert csr(99, 9) == 999\n        \n        # Test view length\n        for\
    \ i in range(100):\n            assert len(csr[i]) == 10\n\n    def test_bucketize_edge_cases(self):\n\
    \        \"\"\"Test bucketize with edge cases\"\"\"\n        # All elements go\
    \ to the same bucket\n        N = 3\n        K = [1, 1, 1, 1]\n        V = [10,\
    \ 20, 30, 40]\n        \n        csr = CSR.bucketize(N, K, V)\n        assert\
    \ len(csr) == 3\n        \n        # Bucket 0 should be empty\n        assert\
    \ len(csr[0]) == 0\n        \n        # Bucket 1 should have all elements\n  \
    \      assert len(csr[1]) == 4\n        \n        # Bucket 2 should be empty\n\
    \        assert len(csr[2]) == 0\n\n    def test_bucketize_empty(self):\n    \
    \    \"\"\"Test bucketize with empty input\"\"\"\n        N = 3\n        K = []\n\
    \        V = []\n        \n        csr = CSR.bucketize(N, K, V)\n        assert\
    \ len(csr) == 3\n        \n        # All buckets should be empty\n        for\
    \ i in range(3):\n            assert len(csr[i]) == 0\n\n    def test_different_data_types(self):\n\
    \        \"\"\"Test CSR with different data types\"\"\"\n        # String data\n\
    \        A = ['a', 'b', 'c', 'd', 'e', 'f']\n        O = [0, 2, 4, 6]\n      \
    \  csr = CSR(A, O)\n        \n        assert csr(0, 0) == 'a'\n        assert\
    \ csr(1, 1) == 'd'\n        assert csr(2, 0) == 'e'\n        \n        # Float\
    \ data\n        A_float = [1.1, 2.2, 3.3, 4.4]\n        O_float = [0, 2, 4]\n\
    \        csr_float = CSR(A_float, O_float)\n        \n        assert csr_float(0,\
    \ 0) == 1.1\n        assert csr_float(1, 1) == 4.4\n\n    def test_bounds_checking(self):\n\
    \        \"\"\"Test that appropriate errors are raised for out-of-bounds access\"\
    \"\"\n        A = [1, 2, 3, 4]\n        O = [0, 2, 4]  # 2 rows: [1,2], [3,4]\n\
    \        csr = CSR(A, O)\n        \n        # These should work\n        assert\
    \ csr(0, 1) == 2\n        assert csr(1, 0) == 3\n        \n        # Out of bounds\
    \ row access should raise IndexError when accessing the view\n        # Note:\
    \ CSR doesn't validate bounds itself, the view does\n        row = csr[0]\n  \
    \      with pytest.raises(IndexError):\n            row[2]  # Row 0 only has 2\
    \ elements (indices 0, 1)\n\n    def test_random_operations(self):\n        \"\
    \"\"Test random operations for robustness\"\"\"\n        random.seed(42)  # For\
    \ reproducibility\n        \n        # Create random CSR structure\n        num_rows\
    \ = 50\n        total_elements = 500\n        A = [random.randint(1, 1000) for\
    \ _ in range(total_elements)]\n        \n        # Generate random row sizes\n\
    \        O = [0]\n        remaining = total_elements\n        for i in range(num_rows\
    \ - 1):\n            if remaining > 0:\n                row_size = random.randint(0,\
    \ min(20, remaining))\n                O.append(O[-1] + row_size)\n          \
    \      remaining -= row_size\n            else:\n                O.append(O[-1])\n\
    \        O.append(total_elements)\n        \n        csr = CSR(A, O)\n       \
    \ assert len(csr) == num_rows\n        \n        # Perform random operations\n\
    \        for _ in range(100):\n            row_idx = random.randint(0, num_rows\
    \ - 1)\n            row = csr[row_idx]\n            \n            if len(row)\
    \ > 0:\n                col_idx = random.randint(0, len(row) - 1)\n          \
    \      # Read operation\n                val1 = csr(row_idx, col_idx)\n      \
    \          val2 = row[col_idx]\n                assert val1 == val2\n        \
    \        \n                # Write operation\n                new_val = random.randint(2000,\
    \ 3000)\n                csr.set(row_idx, col_idx, new_val)\n                assert\
    \ csr(row_idx, col_idx) == new_val\n                assert row[col_idx] == new_val\n\
    \n    def test_view_isolation(self):\n        \"\"\"Test that different views\
    \ don't interfere with each other\"\"\"\n        A = [1, 2, 3, 4, 5, 6, 7, 8]\n\
    \        O = [0, 3, 5, 8]  # 3 rows: [1,2,3], [4,5], [6,7,8]\n        csr = CSR(A,\
    \ O)\n        \n        # Get multiple views\n        view0 = csr[0]\n       \
    \ view1 = csr[1]\n        view2 = csr[2]\n        \n        # Modify through different\
    \ views\n        view0[0] = 10\n        view1[1] = 50\n        view2[2] = 80\n\
    \        \n        # Check that modifications are isolated and correct\n     \
    \   assert A == [10, 2, 3, 4, 50, 6, 7, 80]\n        assert view0[0] == 10\n \
    \       assert view1[1] == 50\n        assert view2[2] == 80\n        \n     \
    \   # Other elements should be unchanged\n        assert view0[1] == 2\n     \
    \   assert view1[0] == 4\n        assert view2[0] == 6\n\n\n'''\n\u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\nfrom typing import Generic\nfrom typing import TypeVar\n\
    _S = TypeVar('S')\n_T = TypeVar('T')\n_U = TypeVar('U')\n_T1 = TypeVar('T1')\n\
    _T2 = TypeVar('T2')\n_T3 = TypeVar('T3')\n_T4 = TypeVar('T4')\n_T5 = TypeVar('T5')\n\
    _T6 = TypeVar('T6')\n\n\n\n\nimport sys\n\ndef list_find(lst: list, value, start\
    \ = 0, stop = sys.maxsize):\n    try:\n        return lst.index(value, start,\
    \ stop)\n    except:\n        return -1\n\nclass view(Generic[_T]):\n    __slots__\
    \ = 'A', 'l', 'r'\n    def __init__(V, A: list[_T], l: int, r: int): V.A, V.l,\
    \ V.r = A, l, r\n    def __len__(V): return V.r - V.l\n    def __getitem__(V,\
    \ i: int): \n        if 0 <= i < V.r - V.l: return V.A[V.l+i]\n        else: raise\
    \ IndexError\n    def __setitem__(V, i: int, v: _T): V.A[V.l+i] = v\n    def __contains__(V,\
    \ v: _T): return list_find(V.A, v, V.l, V.r) != -1\n    def set_range(V, l: int,\
    \ r: int): V.l, V.r = l, r\n    def index(V, v: _T): return V.A.index(v, V.l,\
    \ V.r) - V.l\n    def reverse(V):\n        l, r = V.l, V.r-1\n        while l\
    \ < r: V.A[l], V.A[r] = V.A[r], V.A[l]; l += 1; r -= 1\n    def sort(V, /, *args,\
    \ **kwargs):\n        A = V.A[V.l:V.r]; A.sort(*args, **kwargs)\n        for i,a\
    \ in enumerate(A,V.l): V.A[i] = a\n    def pop(V): V.r -= 1; return V.A[V.r]\n\
    \    def append(V, v: _T): V.A[V.r] = v; V.r += 1\n    def popleft(V): V.l +=\
    \ 1; return V.A[V.l-1]\n    def appendleft(V, v: _T): V.l -= 1; V.A[V.l] = v;\
    \ \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\nclass CSR(Generic[_T]):\n\
    \    __slots__ = 'A', 'O'\n    def __init__(csr, A: list[_T], O: list[int]): csr.A,\
    \ csr.O = A, O\n    def __len__(csr): return len(csr.O)-1\n    def __getitem__(csr,\
    \ i: int): return view(csr.A, csr.O[i], csr.O[i+1])\n    def __call__(csr, i:\
    \ int, j: int): return csr.A[csr.O[i]+j]\n    def set(csr, i: int, j: int, v:\
    \ _T): csr.A[csr.O[i]+j] = v\n    @classmethod\n    def bucketize(cls, N: int,\
    \ K: list[int], V: list[_T]):\n        A: list[_T] = [0]*len(K); O = [0]*(N+1)\n\
    \        for k in K: O[k] += 1\n        for i in range(N): O[i+1] += O[i]\n  \
    \      for e in range(len(K)): k = K[~e]; O[k] -= 1; A[O[k]] = V[~e]\n       \
    \ return cls(A, O)\n\nif __name__ == '__main__':\n    \"\"\"\n    Helper for making\
    \ unittest files compatible with verification-helper.\n    \n    This module provides\
    \ a helper function to run a dummy Library Checker test\n    so that unittest\
    \ files can be verified by oj-verify.\n    \"\"\"\n    \n    def run_verification_helper_unittest():\n\
    \        \"\"\"\n        Run a dummy Library Checker test for verification-helper\
    \ compatibility.\n        \n        This function should be called in the __main__\
    \ block of unittest files\n        that need to be compatible with verification-helper.\n\
    \        \n        The function:\n        1. Reads A and B from input\n      \
    \  2. Writes A+B to output  \n        3. If the result is the expected value (1198300249),\
    \ runs pytest\n        4. Exits with the pytest result code\n        \"\"\"\n\
    \        \n        \n        from typing import Type, Union, overload\n      \
    \  \n        import typing\n        from collections import deque\n        from\
    \ numbers import Number\n        from types import GenericAlias \n        from\
    \ typing import Callable, Collection, Iterator, Union\n        \n        import\
    \ os\n        from io import BytesIO, IOBase\n        \n        \n        class\
    \ FastIO(IOBase):\n            BUFSIZE = 8192\n            newlines = 0\n    \
    \    \n            def __init__(self, file):\n                self._fd = file.fileno()\n\
    \                self.buffer = BytesIO()\n                self.writable = \"x\"\
    \ in file.mode or \"r\" not in file.mode\n                self.write = self.buffer.write\
    \ if self.writable else None\n        \n            def read(self):\n        \
    \        BUFSIZE = self.BUFSIZE\n                while True:\n               \
    \     b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n      \
    \              if not b: break\n                    ptr = self.buffer.tell()\n\
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
    \    \n        import os\n        from io import BytesIO, IOBase\n        \n \
    \       \n        class FastIO(IOBase):\n            BUFSIZE = 8192\n        \
    \    newlines = 0\n        \n            def __init__(self, file):\n         \
    \       self._fd = file.fileno()\n                self.buffer = BytesIO()\n  \
    \              self.writable = \"x\" in file.mode or \"r\" not in file.mode\n\
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
    import pytest\nimport random\n\nclass TestCSR:\n    def test_initialization(self):\n\
    \        \"\"\"Test basic initialization of CSR\"\"\"\n        A = [1, 2, 3, 4,\
    \ 5, 6]\n        O = [0, 2, 4, 6]  # 3 rows: [1,2], [3,4], [5,6]\n        csr\
    \ = CSR(A, O)\n        \n        assert csr.A is A\n        assert csr.O is O\n\
    \        assert len(csr) == 3\n\n    def test_len(self):\n        \"\"\"Test __len__\
    \ method\"\"\"\n        A = [1, 2, 3, 4, 5]\n        O = [0, 2, 3, 5]  # 3 rows:\
    \ [1,2], [3], [4,5]\n        csr = CSR(A, O)\n        \n        assert len(csr)\
    \ == 3\n        \n        # Empty CSR\n        empty_csr = CSR([], [0])\n    \
    \    assert len(empty_csr) == 0\n\n    def test_getitem(self):\n        \"\"\"\
    Test __getitem__ method (returns temporary view)\"\"\"\n        A = [10, 20, 30,\
    \ 40, 50, 60]\n        O = [0, 2, 4, 6]  # 3 rows: [10,20], [30,40], [50,60]\n\
    \        csr = CSR(A, O)\n        \n        # Test temporary access - each call\
    \ returns the same view object but points to different rows\n        # Test row\
    \ 0\n        row = csr[0]\n        assert len(row) == 2\n        assert row[0]\
    \ == 10\n        assert row[1] == 20\n        \n        # Test row 1 - same view\
    \ object, different range\n        row = csr[1]\n        assert len(row) == 2\n\
    \        assert row[0] == 30\n        assert row[1] == 40\n        \n        #\
    \ Test row 2 - same view object, different range\n        row = csr[2]\n     \
    \   assert len(row) == 2\n        assert row[0] == 50\n        assert row[1] ==\
    \ 60\n\n    def test_call(self):\n        \"\"\"Test __call__ method (direct element\
    \ access)\"\"\"\n        A = [10, 20, 30, 40, 50, 60]\n        O = [0, 2, 4, 6]\
    \  # 3 rows: [10,20], [30,40], [50,60]\n        csr = CSR(A, O)\n        \n  \
    \      # Direct access to elements\n        assert csr(0, 0) == 10\n        assert\
    \ csr(0, 1) == 20\n        assert csr(1, 0) == 30\n        assert csr(1, 1) ==\
    \ 40\n        assert csr(2, 0) == 50\n        assert csr(2, 1) == 60\n\n    def\
    \ test_set(self):\n        \"\"\"Test set method\"\"\"\n        A = [10, 20, 30,\
    \ 40, 50, 60]\n        O = [0, 2, 4, 6]  # 3 rows: [10,20], [30,40], [50,60]\n\
    \        csr = CSR(A, O)\n        \n        # Modify elements\n        csr.set(0,\
    \ 0, 15)\n        csr.set(1, 1, 45)\n        csr.set(2, 0, 55)\n        \n   \
    \     assert A == [15, 20, 30, 45, 55, 60]\n        assert csr(0, 0) == 15\n \
    \       assert csr(1, 1) == 45\n        assert csr(2, 0) == 55\n\n    def test_getitem_method(self):\n\
    \        \"\"\"Test __getitem__ method (creates new view)\"\"\"\n        A = [1,\
    \ 2, 3, 4, 5, 6, 7, 8]\n        O = [0, 3, 5, 8]  # 3 rows: [1,2,3], [4,5], [6,7,8]\n\
    \        csr = CSR(A, O)\n        \n        # Create views for each row\n    \
    \    view0 = csr[0]\n        view1 = csr[1]\n        view2 = csr[2]\n        \n\
    \        assert len(view0) == 3\n        assert view0[0] == 1\n        assert\
    \ view0[2] == 3\n        \n        assert len(view1) == 2\n        assert view1[0]\
    \ == 4\n        assert view1[1] == 5\n        \n        assert len(view2) == 3\n\
    \        assert view2[0] == 6\n        assert view2[2] == 8\n\n    def test_bucketize(self):\n\
    \        \"\"\"Test bucketize class method\"\"\"\n        # Create buckets: bucket\
    \ 0 gets [1,3], bucket 1 gets [2], bucket 2 gets [4,5]\n        N = 3\n      \
    \  K = [0, 1, 0, 2, 2]  # Keys indicating which bucket each value goes to\n  \
    \      V = [1, 2, 3, 4, 5]  # Values to be bucketed\n        \n        csr = CSR.bucketize(N,\
    \ K, V)\n        \n        assert len(csr) == 3\n        \n        # Check bucket\
    \ 0: should contain [3, 1] (reverse order due to algorithm)\n        row0 = csr[0]\n\
    \        assert len(row0) == 2\n        assert set([row0[0], row0[1]]) == {1,\
    \ 3}\n        \n        # Check bucket 1: should contain [2]\n        row1 = csr[1]\n\
    \        assert len(row1) == 1\n        assert row1[0] == 2\n        \n      \
    \  # Check bucket 2: should contain [5, 4] (reverse order)\n        row2 = csr[2]\n\
    \        assert len(row2) == 2\n        assert set([row2[0], row2[1]]) == {4,\
    \ 5}\n\n    def test_empty_rows(self):\n        \"\"\"Test CSR with empty rows\"\
    \"\"\n        A = [1, 2, 3, 4]\n        O = [0, 2, 2, 4]  # 3 rows: [1,2], [],\
    \ [3,4]\n        csr = CSR(A, O)\n        \n        assert len(csr) == 3\n   \
    \     \n        # Row 0: [1,2]\n        row0 = csr[0]\n        assert len(row0)\
    \ == 2\n        assert row0[0] == 1\n        assert row0[1] == 2\n        \n \
    \       # Row 1: empty\n        row1 = csr[1]\n        assert len(row1) == 0\n\
    \        \n        # Row 2: [3,4]\n        row2 = csr[2]\n        assert len(row2)\
    \ == 2\n        assert row2[0] == 3\n        assert row2[1] == 4\n\n    def test_single_element_rows(self):\n\
    \        \"\"\"Test CSR with single element rows\"\"\"\n        A = [10, 20, 30]\n\
    \        O = [0, 1, 2, 3]  # 3 rows: [10], [20], [30]\n        csr = CSR(A, O)\n\
    \        \n        assert len(csr) == 3\n        \n        for i in range(3):\n\
    \            row = csr[i]\n            assert len(row) == 1\n            assert\
    \ row[0] == (i + 1) * 10\n            assert csr(i, 0) == (i + 1) * 10\n\n   \
    \ def test_view_modifications(self):\n        \"\"\"Test that view modifications\
    \ affect the underlying data\"\"\"\n        A = [1, 2, 3, 4, 5, 6]\n        O\
    \ = [0, 2, 4, 6]  # 3 rows: [1,2], [3,4], [5,6]\n        csr = CSR(A, O)\n   \
    \     \n        # Get a view and modify it\n        row1 = csr[1]\n        row1[0]\
    \ = 30\n        row1[1] = 40\n        \n        # Check that underlying data changed\n\
    \        assert A == [1, 2, 30, 40, 5, 6]\n        assert csr(1, 0) == 30\n  \
    \      assert csr(1, 1) == 40\n\n    def test_view_operations(self):\n       \
    \ \"\"\"Test various view operations\"\"\"\n        A = [5, 3, 1, 4, 2, 6]\n \
    \       O = [0, 3, 6]  # 2 rows: [5,3,1], [4,2,6]\n        csr = CSR(A, O)\n \
    \       \n        # Get views and operate on them\n        row0 = csr[0]\n   \
    \     row0.sort()\n        assert A[:3] == [1, 3, 5]\n        \n        row1 =\
    \ csr[1]\n        row1.reverse()\n        assert A[3:] == [6, 2, 4]\n\n    def\
    \ test_view_creation_behavior(self):\n        \"\"\"Test that __getitem__ creates\
    \ new view objects each time\"\"\"\n        A = [1, 2, 3, 4, 5, 6]\n        O\
    \ = [0, 2, 4, 6]  # 3 rows: [1,2], [3,4], [5,6]\n        csr = CSR(A, O)\n   \
    \     \n        # __getitem__ creates new view objects each time\n        view1\
    \ = csr[0]  # New view of row 0\n        view2 = csr[0]  # Another new view of\
    \ row 0\n        \n        # Should be different objects but point to the same\
    \ data\n        assert view1 is not view2  # Different objects\n        \n   \
    \     # But should have the same data\n        assert len(view1) == len(view2)\
    \ == 2\n        assert view1[0] == view2[0] == 1  # Row 0 data\n        assert\
    \ view1[1] == view2[1] == 2  # Row 0 data\n        \n        # Views of different\
    \ rows should also be independent\n        row0_view = csr[0]\n        row1_view\
    \ = csr[1] \n        \n        assert row0_view is not row1_view  # Different\
    \ objects\n        assert len(row0_view) == 2\n        assert row0_view[0] ==\
    \ 1  # Row 0 data\n        assert len(row1_view) == 2  \n        assert row1_view[0]\
    \ == 3  # Row 1 data\n\n    def test_large_csr(self):\n        \"\"\"Test CSR\
    \ with larger data\"\"\"\n        # Create 100 rows with 10 elements each\n  \
    \      A = list(range(1000))\n        O = [i * 10 for i in range(101)]  # 100\
    \ rows\n        csr = CSR(A, O)\n        \n        assert len(csr) == 100\n  \
    \      \n        # Test random access\n        assert csr(50, 5) == 505\n    \
    \    assert csr(99, 9) == 999\n        \n        # Test view length\n        for\
    \ i in range(100):\n            assert len(csr[i]) == 10\n\n    def test_bucketize_edge_cases(self):\n\
    \        \"\"\"Test bucketize with edge cases\"\"\"\n        # All elements go\
    \ to the same bucket\n        N = 3\n        K = [1, 1, 1, 1]\n        V = [10,\
    \ 20, 30, 40]\n        \n        csr = CSR.bucketize(N, K, V)\n        assert\
    \ len(csr) == 3\n        \n        # Bucket 0 should be empty\n        assert\
    \ len(csr[0]) == 0\n        \n        # Bucket 1 should have all elements\n  \
    \      assert len(csr[1]) == 4\n        \n        # Bucket 2 should be empty\n\
    \        assert len(csr[2]) == 0\n\n    def test_bucketize_empty(self):\n    \
    \    \"\"\"Test bucketize with empty input\"\"\"\n        N = 3\n        K = []\n\
    \        V = []\n        \n        csr = CSR.bucketize(N, K, V)\n        assert\
    \ len(csr) == 3\n        \n        # All buckets should be empty\n        for\
    \ i in range(3):\n            assert len(csr[i]) == 0\n\n    def test_different_data_types(self):\n\
    \        \"\"\"Test CSR with different data types\"\"\"\n        # String data\n\
    \        A = ['a', 'b', 'c', 'd', 'e', 'f']\n        O = [0, 2, 4, 6]\n      \
    \  csr = CSR(A, O)\n        \n        assert csr(0, 0) == 'a'\n        assert\
    \ csr(1, 1) == 'd'\n        assert csr(2, 0) == 'e'\n        \n        # Float\
    \ data\n        A_float = [1.1, 2.2, 3.3, 4.4]\n        O_float = [0, 2, 4]\n\
    \        csr_float = CSR(A_float, O_float)\n        \n        assert csr_float(0,\
    \ 0) == 1.1\n        assert csr_float(1, 1) == 4.4\n\n    def test_bounds_checking(self):\n\
    \        \"\"\"Test that appropriate errors are raised for out-of-bounds access\"\
    \"\"\n        A = [1, 2, 3, 4]\n        O = [0, 2, 4]  # 2 rows: [1,2], [3,4]\n\
    \        csr = CSR(A, O)\n        \n        # These should work\n        assert\
    \ csr(0, 1) == 2\n        assert csr(1, 0) == 3\n        \n        # Out of bounds\
    \ row access should raise IndexError when accessing the view\n        # Note:\
    \ CSR doesn't validate bounds itself, the view does\n        row = csr[0]\n  \
    \      with pytest.raises(IndexError):\n            row[2]  # Row 0 only has 2\
    \ elements (indices 0, 1)\n\n    def test_random_operations(self):\n        \"\
    \"\"Test random operations for robustness\"\"\"\n        random.seed(42)  # For\
    \ reproducibility\n        \n        # Create random CSR structure\n        num_rows\
    \ = 50\n        total_elements = 500\n        A = [random.randint(1, 1000) for\
    \ _ in range(total_elements)]\n        \n        # Generate random row sizes\n\
    \        O = [0]\n        remaining = total_elements\n        for i in range(num_rows\
    \ - 1):\n            if remaining > 0:\n                row_size = random.randint(0,\
    \ min(20, remaining))\n                O.append(O[-1] + row_size)\n          \
    \      remaining -= row_size\n            else:\n                O.append(O[-1])\n\
    \        O.append(total_elements)\n        \n        csr = CSR(A, O)\n       \
    \ assert len(csr) == num_rows\n        \n        # Perform random operations\n\
    \        for _ in range(100):\n            row_idx = random.randint(0, num_rows\
    \ - 1)\n            row = csr[row_idx]\n            \n            if len(row)\
    \ > 0:\n                col_idx = random.randint(0, len(row) - 1)\n          \
    \      # Read operation\n                val1 = csr(row_idx, col_idx)\n      \
    \          val2 = row[col_idx]\n                assert val1 == val2\n        \
    \        \n                # Write operation\n                new_val = random.randint(2000,\
    \ 3000)\n                csr.set(row_idx, col_idx, new_val)\n                assert\
    \ csr(row_idx, col_idx) == new_val\n                assert row[col_idx] == new_val\n\
    \n    def test_view_isolation(self):\n        \"\"\"Test that different views\
    \ don't interfere with each other\"\"\"\n        A = [1, 2, 3, 4, 5, 6, 7, 8]\n\
    \        O = [0, 3, 5, 8]  # 3 rows: [1,2,3], [4,5], [6,7,8]\n        csr = CSR(A,\
    \ O)\n        \n        # Get multiple views\n        view0 = csr[0]\n       \
    \ view1 = csr[1]\n        view2 = csr[2]\n        \n        # Modify through different\
    \ views\n        view0[0] = 10\n        view1[1] = 50\n        view2[2] = 80\n\
    \        \n        # Check that modifications are isolated and correct\n     \
    \   assert A == [10, 2, 3, 4, 50, 6, 7, 80]\n        assert view0[0] == 10\n \
    \       assert view1[1] == 50\n        assert view2[2] == 80\n        \n     \
    \   # Other elements should be unchanged\n        assert view0[1] == 2\n     \
    \   assert view1[0] == 4\n        assert view2[0] == 6\n\nfrom cp_library.ds.view.csr_cls\
    \ import CSR\n\nif __name__ == '__main__':\n    from cp_library.test.unittest_helper\
    \ import run_verification_helper_unittest\n    run_verification_helper_unittest()"
  dependsOn:
  - cp_library/ds/view/csr_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/ds/view/view_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/ds/list/list_find_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/unittests/ds/view/csr_cls_test.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/view/csr_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/view/csr_cls_test.py
- /verify/test/unittests/ds/view/csr_cls_test.py.html
title: test/unittests/ds/view/csr_cls_test.py
---
