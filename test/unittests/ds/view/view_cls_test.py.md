---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
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
    \nimport pytest\nimport random\n\nclass TestView:\n    def test_initialization(self):\n\
    \        \"\"\"Test basic initialization of view\"\"\"\n        data = [1, 2,\
    \ 3, 4, 5]\n        v = view(data, 1, 4)\n        \n        assert v.A is data\n\
    \        assert v.l == 1\n        assert v.r == 4\n        assert len(v) == 3\n\
    \n    def test_len(self):\n        \"\"\"Test __len__ method\"\"\"\n        data\
    \ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n        \n        # Test different ranges\n\
    \        assert len(view(data, 0, 5)) == 5\n        assert len(view(data, 2, 7))\
    \ == 5\n        assert len(view(data, 0, 10)) == 10\n        assert len(view(data,\
    \ 5, 5)) == 0  # Empty range\n\n    def test_getitem(self):\n        \"\"\"Test\
    \ __getitem__ method\"\"\"\n        data = [10, 20, 30, 40, 50]\n        v = view(data,\
    \ 1, 4)  # View of [20, 30, 40]\n        \n        assert v[0] == 20\n       \
    \ assert v[1] == 30\n        assert v[2] == 40\n        \n        # Test IndexError\
    \ for out of bounds\n        with pytest.raises(IndexError):\n            v[3]\n\
    \        with pytest.raises(IndexError):\n            v[-1]\n\n    def test_setitem(self):\n\
    \        \"\"\"Test __setitem__ method\"\"\"\n        data = [10, 20, 30, 40,\
    \ 50]\n        v = view(data, 1, 4)  # View of [20, 30, 40]\n        \n      \
    \  v[0] = 25\n        v[1] = 35\n        v[2] = 45\n        \n        assert data\
    \ == [10, 25, 35, 45, 50]\n        assert v[0] == 25\n        assert v[1] == 35\n\
    \        assert v[2] == 45\n\n    def test_contains(self):\n        \"\"\"Test\
    \ __contains__ method\"\"\"\n        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]\n    \
    \    v = view(data, 2, 6)  # View of [3, 4, 5, 6]\n        \n        assert 3\
    \ in v\n        assert 4 in v\n        assert 5 in v\n        assert 6 in v\n\
    \        assert 1 not in v  # Outside view range\n        assert 2 not in v  #\
    \ Outside view range\n        assert 7 not in v  # Outside view range\n      \
    \  assert 10 not in v  # Not in data at all\n\n    def test_set_range(self):\n\
    \        \"\"\"Test set_range method\"\"\"\n        data = [1, 2, 3, 4, 5, 6,\
    \ 7, 8, 9, 10]\n        v = view(data, 2, 5)\n        \n        assert len(v)\
    \ == 3\n        assert v[0] == 3\n        \n        # Change the range\n     \
    \   v.set_range(4, 8)\n        assert len(v) == 4\n        assert v[0] == 5\n\
    \        assert v[1] == 6\n        assert v[2] == 7\n        assert v[3] == 8\n\
    \n    def test_index(self):\n        \"\"\"Test index method\"\"\"\n        data\
    \ = [10, 20, 30, 40, 50, 60, 70]\n        v = view(data, 2, 6)  # View of [30,\
    \ 40, 50, 60]\n        \n        assert v.index(30) == 0\n        assert v.index(40)\
    \ == 1\n        assert v.index(50) == 2\n        assert v.index(60) == 3\n   \
    \     \n        # Test ValueError for element not in view\n        with pytest.raises(ValueError):\n\
    \            v.index(10)  # Outside view range\n        with pytest.raises(ValueError):\n\
    \            v.index(70)  # Outside view range\n        with pytest.raises(ValueError):\n\
    \            v.index(100)  # Not in data at all\n\n    def test_reverse(self):\n\
    \        \"\"\"Test reverse method\"\"\"\n        data = [1, 2, 3, 4, 5, 6, 7,\
    \ 8, 9]\n        v = view(data, 2, 7)  # View of [3, 4, 5, 6, 7]\n        \n \
    \       v.reverse()\n        \n        # Check that the view is reversed\n   \
    \     assert v[0] == 7\n        assert v[1] == 6\n        assert v[2] == 5\n \
    \       assert v[3] == 4\n        assert v[4] == 3\n        \n        # Check\
    \ that the underlying array is modified\n        assert data == [1, 2, 7, 6, 5,\
    \ 4, 3, 8, 9]\n\n    def test_sort(self):\n        \"\"\"Test sort method\"\"\"\
    \n        data = [1, 5, 2, 8, 3, 9, 4, 6, 7]\n        v = view(data, 2, 7)  #\
    \ View of [2, 8, 3, 9, 4]\n        \n        v.sort()\n        \n        # Check\
    \ that the view is sorted\n        assert v[0] == 2\n        assert v[1] == 3\n\
    \        assert v[2] == 4\n        assert v[3] == 8\n        assert v[4] == 9\n\
    \        \n        # Check that the underlying array is modified correctly\n \
    \       assert data == [1, 5, 2, 3, 4, 8, 9, 6, 7]\n\n    def test_sort_with_parameters(self):\n\
    \        \"\"\"Test sort method with reverse parameter\"\"\"\n        data = [1,\
    \ 5, 2, 8, 3, 9, 4, 6, 7]\n        v = view(data, 2, 7)  # View of [2, 8, 3, 9,\
    \ 4]\n        \n        v.sort(reverse=True)\n        \n        # Check that the\
    \ view is sorted in reverse\n        assert v[0] == 9\n        assert v[1] ==\
    \ 8\n        assert v[2] == 4\n        assert v[3] == 3\n        assert v[4] ==\
    \ 2\n        \n        # Check that the underlying array is modified correctly\n\
    \        assert data == [1, 5, 9, 8, 4, 3, 2, 6, 7]\n\n    def test_pop(self):\n\
    \        \"\"\"Test pop method\"\"\"\n        data = [1, 2, 3, 4, 5, 6, 7, 8,\
    \ 9]\n        v = view(data, 2, 6)  # View of [3, 4, 5, 6]\n        \n       \
    \ assert len(v) == 4\n        \n        # Pop from the end\n        popped = v.pop()\n\
    \        assert popped == 6\n        assert len(v) == 3\n        assert v[2] ==\
    \ 5  # Last element is now 5\n        \n        # Pop again\n        popped =\
    \ v.pop()\n        assert popped == 5\n        assert len(v) == 2\n\n    def test_append(self):\n\
    \        \"\"\"Test append method\"\"\"\n        data = [1, 2, 3, 4, 5, 0, 0,\
    \ 0, 9]  # Extra space for appending\n        v = view(data, 2, 5)  # View of\
    \ [3, 4, 5]\n        \n        assert len(v) == 3\n        \n        # Append\
    \ to the end\n        v.append(6)\n        assert len(v) == 4\n        assert\
    \ v[3] == 6\n        assert data[5] == 6  # Check underlying array\n        \n\
    \        # Append again\n        v.append(7)\n        assert len(v) == 5\n   \
    \     assert v[4] == 7\n\n    def test_popleft(self):\n        \"\"\"Test popleft\
    \ method\"\"\"\n        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]\n        v = view(data,\
    \ 2, 6)  # View of [3, 4, 5, 6]\n        \n        assert len(v) == 4\n      \
    \  \n        # Pop from the beginning\n        popped = v.popleft()\n        assert\
    \ popped == 3\n        assert len(v) == 3\n        assert v[0] == 4  # First element\
    \ is now 4\n        \n        # Pop again\n        popped = v.popleft()\n    \
    \    assert popped == 4\n        assert len(v) == 2\n        assert v[0] == 5\n\
    \n    def test_appendleft(self):\n        \"\"\"Test appendleft method\"\"\"\n\
    \        data = [0, 0, 1, 2, 3, 4, 5, 6, 7]  # Extra space at beginning\n    \
    \    v = view(data, 4, 7)  # View of [3, 4, 5]\n        \n        assert len(v)\
    \ == 3\n        assert v[0] == 3\n        \n        # Append to the beginning\n\
    \        v.appendleft(2)\n        assert len(v) == 4\n        assert v[0] == 2\n\
    \        assert v[1] == 3\n        assert data[3] == 2  # Check underlying array\n\
    \        \n        # Append again\n        v.appendleft(1)\n        assert len(v)\
    \ == 5\n        assert v[0] == 1\n        assert v[1] == 2\n\n    def test_validate(self):\n\
    \        \"\"\"Test validate method\"\"\"\n        data = [1, 2, 3, 4, 5]\n  \
    \      \n        # Valid ranges\n        v1 = view(data, 0, 5)\n        assert\
    \ v1.validate() == True\n        \n        v2 = view(data, 2, 4)\n        assert\
    \ v2.validate() == True\n        \n        v3 = view(data, 3, 3)  # Empty range\n\
    \        assert v3.validate() == True\n        \n        # Invalid ranges\n  \
    \      v4 = view(data, -1, 3)\n        assert v4.validate() == False\n       \
    \ \n        v5 = view(data, 2, 6)  # r > len(A)\n        assert v5.validate()\
    \ == False\n        \n        v6 = view(data, 3, 2)  # l > r\n        assert v6.validate()\
    \ == False\n\n    def test_empty_view(self):\n        \"\"\"Test operations on\
    \ empty view\"\"\"\n        data = [1, 2, 3, 4, 5]\n        v = view(data, 3,\
    \ 3)  # Empty view\n        \n        assert len(v) == 0\n        \n        #\
    \ Test that operations on empty view behave correctly\n        with pytest.raises(IndexError):\n\
    \            v[0]\n        \n        assert 1 not in v\n        assert 3 not in\
    \ v\n\n    def test_edge_cases(self):\n        \"\"\"Test edge cases\"\"\"\n \
    \       # Single element view\n        data = [10, 20, 30, 40, 50]\n        v\
    \ = view(data, 2, 3)  # View of [30]\n        \n        assert len(v) == 1\n \
    \       assert v[0] == 30\n        assert 30 in v\n        assert 20 not in v\n\
    \        \n        # Modify single element\n        v[0] = 35\n        assert\
    \ data == [10, 20, 35, 40, 50]\n\n    def test_view_operations_sequence(self):\n\
    \        \"\"\"Test a sequence of operations\"\"\"\n        data = [10, 20, 30,\
    \ 40, 50, 60, 70, 80, 90, 100]\n        v = view(data, 2, 8)  # View of [30, 40,\
    \ 50, 60, 70, 80]\n        \n        # Initial state\n        assert len(v) ==\
    \ 6\n        assert v[0] == 30\n        assert v[5] == 80\n        \n        #\
    \ Modify some elements\n        v[1] = 45\n        v[3] = 65\n        assert data[3]\
    \ == 45\n        assert data[5] == 65\n        \n        # Pop and append\n  \
    \      popped = v.pop()\n        assert popped == 80\n        assert len(v) ==\
    \ 5\n        \n        v.append(85)\n        assert len(v) == 6\n        assert\
    \ v[5] == 85\n        \n        # Reverse\n        v.reverse()\n        assert\
    \ v[0] == 85\n        assert v[5] == 30\n\n    def test_with_different_types(self):\n\
    \        \"\"\"Test view with different data types\"\"\"\n        # String data\n\
    \        str_data = ['a', 'b', 'c', 'd', 'e', 'f']\n        str_view = view(str_data,\
    \ 1, 4)  # ['b', 'c', 'd']\n        \n        assert len(str_view) == 3\n    \
    \    assert str_view[0] == 'b'\n        assert 'c' in str_view\n        assert\
    \ 'a' not in str_view\n        \n        str_view.sort()\n        assert str_view[0]\
    \ == 'b'\n        assert str_view[1] == 'c'\n        assert str_view[2] == 'd'\n\
    \        \n        # Float data\n        float_data = [1.1, 2.2, 3.3, 4.4, 5.5]\n\
    \        float_view = view(float_data, 1, 4)  # [2.2, 3.3, 4.4]\n        \n  \
    \      assert len(float_view) == 3\n        assert float_view[1] == 3.3\n    \
    \    assert 2.2 in float_view\n\n    def test_large_data_operations(self):\n \
    \       \"\"\"Test operations on larger datasets\"\"\"\n        # Create large\
    \ dataset\n        data = list(range(1000))\n        v = view(data, 100, 900)\
    \  # 800 elements\n        \n        assert len(v) == 800\n        assert v[0]\
    \ == 100\n        assert v[799] == 899\n        \n        # Test contains on large\
    \ dataset\n        assert 500 in v\n        assert 50 not in v\n        assert\
    \ 950 not in v\n        \n        # Test index on large dataset\n        assert\
    \ v.index(200) == 100\n        assert v.index(600) == 500\n\n    def test_random_operations(self):\n\
    \        \"\"\"Test random operations for robustness\"\"\"\n        random.seed(42)\
    \  # For reproducibility\n        \n        # Create test data\n        data =\
    \ list(range(100))\n        original_data = data.copy()\n        \n        # Create\
    \ view\n        start, end = 20, 80\n        v = view(data, start, end)\n    \
    \    \n        # Perform random operations\n        for _ in range(50):\n    \
    \        op = random.choice(['read', 'write', 'contains'])\n            \n   \
    \         if op == 'read' and len(v) > 0:\n                idx = random.randint(0,\
    \ len(v) - 1)\n                val = v[idx]\n                assert val == data[start\
    \ + idx]\n                \n            elif op == 'write' and len(v) > 0:\n \
    \               idx = random.randint(0, len(v) - 1)\n                new_val =\
    \ random.randint(1000, 2000)\n                v[idx] = new_val\n             \
    \   assert data[start + idx] == new_val\n                \n            elif op\
    \ == 'contains':\n                search_val = random.choice(original_data)\n\
    \                result = search_val in v\n                # Verify manually\n\
    \                expected = any(data[i] == search_val for i in range(start, min(start\
    \ + len(v), len(data))))\n                assert result == expected\n\n    def\
    \ test_view_modification_boundary_safety(self):\n        \"\"\"Test that view\
    \ modifications don't affect data outside the view\"\"\"\n        data = [1, 2,\
    \ 3, 4, 5, 6, 7, 8, 9, 10]\n        original = data.copy()\n        \n       \
    \ v = view(data, 3, 7)  # View of [4, 5, 6, 7]\n        \n        # Modify view\n\
    \        v[0] = 40\n        v[1] = 50\n        v[2] = 60\n        v[3] = 70\n\
    \        \n        # Check that only the view range was modified\n        assert\
    \ data[0:3] == original[0:3]  # Before view unchanged\n        assert data[7:]\
    \ == original[7:]    # After view unchanged\n        assert data[3:7] == [40,\
    \ 50, 60, 70]  # View range changed\n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\nfrom typing import Generic\nfrom typing import TypeVar\n\
    _S = TypeVar('S')\n_T = TypeVar('T')\n_U = TypeVar('U')\n_T1 = TypeVar('T1')\n\
    _T2 = TypeVar('T2')\n_T3 = TypeVar('T3')\n_T4 = TypeVar('T4')\n_T5 = TypeVar('T5')\n\
    _T6 = TypeVar('T6')\n\n\nimport sys\n\ndef list_find(lst: list, value, start =\
    \ 0, stop = sys.maxsize):\n    try:\n        return lst.index(value, start, stop)\n\
    \    except:\n        return -1\n\n\nclass view(Generic[_T]):\n    __slots__ =\
    \ 'A', 'l', 'r'\n    def __init__(V, A: list[_T], l: int, r: int): V.A, V.l, V.r\
    \ = A, l, r\n    def __len__(V): return V.r - V.l\n    def __getitem__(V, i: int):\
    \ \n        if 0 <= i < V.r - V.l: return V.A[V.l+i]\n        else: raise IndexError\n\
    \    def __setitem__(V, i: int, v: _T): V.A[V.l+i] = v\n    def __contains__(V,\
    \ v: _T): return list_find(V.A, v, V.l, V.r) != -1\n    def set_range(V, l: int,\
    \ r: int): V.l, V.r = l, r\n    def index(V, v: _T): return V.A.index(v, V.l,\
    \ V.r) - V.l\n    def reverse(V):\n        l, r = V.l, V.r-1\n        while l\
    \ < r: V.A[l], V.A[r] = V.A[r], V.A[l]; l += 1; r -= 1\n    def sort(V, /, *args,\
    \ **kwargs):\n        A = V.A[V.l:V.r]; A.sort(*args, **kwargs)\n        for i,a\
    \ in enumerate(A,V.l): V.A[i] = a\n    def pop(V): V.r -= 1; return V.A[V.r]\n\
    \    def append(V, v: _T): V.A[V.r] = v; V.r += 1\n    def popleft(V): V.l +=\
    \ 1; return V.A[V.l-1]\n    def appendleft(V, v: _T): V.l -= 1; V.A[V.l] = v;\
    \ \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\nif __name__ ==\
    \ '__main__':\n    \"\"\"\n    Helper for making unittest files compatible with\
    \ verification-helper.\n    \n    This module provides a helper function to run\
    \ a dummy Library Checker test\n    so that unittest files can be verified by\
    \ oj-verify.\n    \"\"\"\n    \n    def run_verification_helper_unittest():\n\
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
    import pytest\nimport random\n\nclass TestView:\n    def test_initialization(self):\n\
    \        \"\"\"Test basic initialization of view\"\"\"\n        data = [1, 2,\
    \ 3, 4, 5]\n        v = view(data, 1, 4)\n        \n        assert v.A is data\n\
    \        assert v.l == 1\n        assert v.r == 4\n        assert len(v) == 3\n\
    \n    def test_len(self):\n        \"\"\"Test __len__ method\"\"\"\n        data\
    \ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n        \n        # Test different ranges\n\
    \        assert len(view(data, 0, 5)) == 5\n        assert len(view(data, 2, 7))\
    \ == 5\n        assert len(view(data, 0, 10)) == 10\n        assert len(view(data,\
    \ 5, 5)) == 0  # Empty range\n\n    def test_getitem(self):\n        \"\"\"Test\
    \ __getitem__ method\"\"\"\n        data = [10, 20, 30, 40, 50]\n        v = view(data,\
    \ 1, 4)  # View of [20, 30, 40]\n        \n        assert v[0] == 20\n       \
    \ assert v[1] == 30\n        assert v[2] == 40\n        \n        # Test IndexError\
    \ for out of bounds\n        with pytest.raises(IndexError):\n            v[3]\n\
    \        with pytest.raises(IndexError):\n            v[-1]\n\n    def test_setitem(self):\n\
    \        \"\"\"Test __setitem__ method\"\"\"\n        data = [10, 20, 30, 40,\
    \ 50]\n        v = view(data, 1, 4)  # View of [20, 30, 40]\n        \n      \
    \  v[0] = 25\n        v[1] = 35\n        v[2] = 45\n        \n        assert data\
    \ == [10, 25, 35, 45, 50]\n        assert v[0] == 25\n        assert v[1] == 35\n\
    \        assert v[2] == 45\n\n    def test_contains(self):\n        \"\"\"Test\
    \ __contains__ method\"\"\"\n        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]\n    \
    \    v = view(data, 2, 6)  # View of [3, 4, 5, 6]\n        \n        assert 3\
    \ in v\n        assert 4 in v\n        assert 5 in v\n        assert 6 in v\n\
    \        assert 1 not in v  # Outside view range\n        assert 2 not in v  #\
    \ Outside view range\n        assert 7 not in v  # Outside view range\n      \
    \  assert 10 not in v  # Not in data at all\n\n    def test_set_range(self):\n\
    \        \"\"\"Test set_range method\"\"\"\n        data = [1, 2, 3, 4, 5, 6,\
    \ 7, 8, 9, 10]\n        v = view(data, 2, 5)\n        \n        assert len(v)\
    \ == 3\n        assert v[0] == 3\n        \n        # Change the range\n     \
    \   v.set_range(4, 8)\n        assert len(v) == 4\n        assert v[0] == 5\n\
    \        assert v[1] == 6\n        assert v[2] == 7\n        assert v[3] == 8\n\
    \n    def test_index(self):\n        \"\"\"Test index method\"\"\"\n        data\
    \ = [10, 20, 30, 40, 50, 60, 70]\n        v = view(data, 2, 6)  # View of [30,\
    \ 40, 50, 60]\n        \n        assert v.index(30) == 0\n        assert v.index(40)\
    \ == 1\n        assert v.index(50) == 2\n        assert v.index(60) == 3\n   \
    \     \n        # Test ValueError for element not in view\n        with pytest.raises(ValueError):\n\
    \            v.index(10)  # Outside view range\n        with pytest.raises(ValueError):\n\
    \            v.index(70)  # Outside view range\n        with pytest.raises(ValueError):\n\
    \            v.index(100)  # Not in data at all\n\n    def test_reverse(self):\n\
    \        \"\"\"Test reverse method\"\"\"\n        data = [1, 2, 3, 4, 5, 6, 7,\
    \ 8, 9]\n        v = view(data, 2, 7)  # View of [3, 4, 5, 6, 7]\n        \n \
    \       v.reverse()\n        \n        # Check that the view is reversed\n   \
    \     assert v[0] == 7\n        assert v[1] == 6\n        assert v[2] == 5\n \
    \       assert v[3] == 4\n        assert v[4] == 3\n        \n        # Check\
    \ that the underlying array is modified\n        assert data == [1, 2, 7, 6, 5,\
    \ 4, 3, 8, 9]\n\n    def test_sort(self):\n        \"\"\"Test sort method\"\"\"\
    \n        data = [1, 5, 2, 8, 3, 9, 4, 6, 7]\n        v = view(data, 2, 7)  #\
    \ View of [2, 8, 3, 9, 4]\n        \n        v.sort()\n        \n        # Check\
    \ that the view is sorted\n        assert v[0] == 2\n        assert v[1] == 3\n\
    \        assert v[2] == 4\n        assert v[3] == 8\n        assert v[4] == 9\n\
    \        \n        # Check that the underlying array is modified correctly\n \
    \       assert data == [1, 5, 2, 3, 4, 8, 9, 6, 7]\n\n    def test_sort_with_parameters(self):\n\
    \        \"\"\"Test sort method with reverse parameter\"\"\"\n        data = [1,\
    \ 5, 2, 8, 3, 9, 4, 6, 7]\n        v = view(data, 2, 7)  # View of [2, 8, 3, 9,\
    \ 4]\n        \n        v.sort(reverse=True)\n        \n        # Check that the\
    \ view is sorted in reverse\n        assert v[0] == 9\n        assert v[1] ==\
    \ 8\n        assert v[2] == 4\n        assert v[3] == 3\n        assert v[4] ==\
    \ 2\n        \n        # Check that the underlying array is modified correctly\n\
    \        assert data == [1, 5, 9, 8, 4, 3, 2, 6, 7]\n\n    def test_pop(self):\n\
    \        \"\"\"Test pop method\"\"\"\n        data = [1, 2, 3, 4, 5, 6, 7, 8,\
    \ 9]\n        v = view(data, 2, 6)  # View of [3, 4, 5, 6]\n        \n       \
    \ assert len(v) == 4\n        \n        # Pop from the end\n        popped = v.pop()\n\
    \        assert popped == 6\n        assert len(v) == 3\n        assert v[2] ==\
    \ 5  # Last element is now 5\n        \n        # Pop again\n        popped =\
    \ v.pop()\n        assert popped == 5\n        assert len(v) == 2\n\n    def test_append(self):\n\
    \        \"\"\"Test append method\"\"\"\n        data = [1, 2, 3, 4, 5, 0, 0,\
    \ 0, 9]  # Extra space for appending\n        v = view(data, 2, 5)  # View of\
    \ [3, 4, 5]\n        \n        assert len(v) == 3\n        \n        # Append\
    \ to the end\n        v.append(6)\n        assert len(v) == 4\n        assert\
    \ v[3] == 6\n        assert data[5] == 6  # Check underlying array\n        \n\
    \        # Append again\n        v.append(7)\n        assert len(v) == 5\n   \
    \     assert v[4] == 7\n\n    def test_popleft(self):\n        \"\"\"Test popleft\
    \ method\"\"\"\n        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]\n        v = view(data,\
    \ 2, 6)  # View of [3, 4, 5, 6]\n        \n        assert len(v) == 4\n      \
    \  \n        # Pop from the beginning\n        popped = v.popleft()\n        assert\
    \ popped == 3\n        assert len(v) == 3\n        assert v[0] == 4  # First element\
    \ is now 4\n        \n        # Pop again\n        popped = v.popleft()\n    \
    \    assert popped == 4\n        assert len(v) == 2\n        assert v[0] == 5\n\
    \n    def test_appendleft(self):\n        \"\"\"Test appendleft method\"\"\"\n\
    \        data = [0, 0, 1, 2, 3, 4, 5, 6, 7]  # Extra space at beginning\n    \
    \    v = view(data, 4, 7)  # View of [3, 4, 5]\n        \n        assert len(v)\
    \ == 3\n        assert v[0] == 3\n        \n        # Append to the beginning\n\
    \        v.appendleft(2)\n        assert len(v) == 4\n        assert v[0] == 2\n\
    \        assert v[1] == 3\n        assert data[3] == 2  # Check underlying array\n\
    \        \n        # Append again\n        v.appendleft(1)\n        assert len(v)\
    \ == 5\n        assert v[0] == 1\n        assert v[1] == 2\n\n    def test_validate(self):\n\
    \        \"\"\"Test validate method\"\"\"\n        data = [1, 2, 3, 4, 5]\n  \
    \      \n        # Valid ranges\n        v1 = view(data, 0, 5)\n        assert\
    \ v1.validate() == True\n        \n        v2 = view(data, 2, 4)\n        assert\
    \ v2.validate() == True\n        \n        v3 = view(data, 3, 3)  # Empty range\n\
    \        assert v3.validate() == True\n        \n        # Invalid ranges\n  \
    \      v4 = view(data, -1, 3)\n        assert v4.validate() == False\n       \
    \ \n        v5 = view(data, 2, 6)  # r > len(A)\n        assert v5.validate()\
    \ == False\n        \n        v6 = view(data, 3, 2)  # l > r\n        assert v6.validate()\
    \ == False\n\n    def test_empty_view(self):\n        \"\"\"Test operations on\
    \ empty view\"\"\"\n        data = [1, 2, 3, 4, 5]\n        v = view(data, 3,\
    \ 3)  # Empty view\n        \n        assert len(v) == 0\n        \n        #\
    \ Test that operations on empty view behave correctly\n        with pytest.raises(IndexError):\n\
    \            v[0]\n        \n        assert 1 not in v\n        assert 3 not in\
    \ v\n\n    def test_edge_cases(self):\n        \"\"\"Test edge cases\"\"\"\n \
    \       # Single element view\n        data = [10, 20, 30, 40, 50]\n        v\
    \ = view(data, 2, 3)  # View of [30]\n        \n        assert len(v) == 1\n \
    \       assert v[0] == 30\n        assert 30 in v\n        assert 20 not in v\n\
    \        \n        # Modify single element\n        v[0] = 35\n        assert\
    \ data == [10, 20, 35, 40, 50]\n\n    def test_view_operations_sequence(self):\n\
    \        \"\"\"Test a sequence of operations\"\"\"\n        data = [10, 20, 30,\
    \ 40, 50, 60, 70, 80, 90, 100]\n        v = view(data, 2, 8)  # View of [30, 40,\
    \ 50, 60, 70, 80]\n        \n        # Initial state\n        assert len(v) ==\
    \ 6\n        assert v[0] == 30\n        assert v[5] == 80\n        \n        #\
    \ Modify some elements\n        v[1] = 45\n        v[3] = 65\n        assert data[3]\
    \ == 45\n        assert data[5] == 65\n        \n        # Pop and append\n  \
    \      popped = v.pop()\n        assert popped == 80\n        assert len(v) ==\
    \ 5\n        \n        v.append(85)\n        assert len(v) == 6\n        assert\
    \ v[5] == 85\n        \n        # Reverse\n        v.reverse()\n        assert\
    \ v[0] == 85\n        assert v[5] == 30\n\n    def test_with_different_types(self):\n\
    \        \"\"\"Test view with different data types\"\"\"\n        # String data\n\
    \        str_data = ['a', 'b', 'c', 'd', 'e', 'f']\n        str_view = view(str_data,\
    \ 1, 4)  # ['b', 'c', 'd']\n        \n        assert len(str_view) == 3\n    \
    \    assert str_view[0] == 'b'\n        assert 'c' in str_view\n        assert\
    \ 'a' not in str_view\n        \n        str_view.sort()\n        assert str_view[0]\
    \ == 'b'\n        assert str_view[1] == 'c'\n        assert str_view[2] == 'd'\n\
    \        \n        # Float data\n        float_data = [1.1, 2.2, 3.3, 4.4, 5.5]\n\
    \        float_view = view(float_data, 1, 4)  # [2.2, 3.3, 4.4]\n        \n  \
    \      assert len(float_view) == 3\n        assert float_view[1] == 3.3\n    \
    \    assert 2.2 in float_view\n\n    def test_large_data_operations(self):\n \
    \       \"\"\"Test operations on larger datasets\"\"\"\n        # Create large\
    \ dataset\n        data = list(range(1000))\n        v = view(data, 100, 900)\
    \  # 800 elements\n        \n        assert len(v) == 800\n        assert v[0]\
    \ == 100\n        assert v[799] == 899\n        \n        # Test contains on large\
    \ dataset\n        assert 500 in v\n        assert 50 not in v\n        assert\
    \ 950 not in v\n        \n        # Test index on large dataset\n        assert\
    \ v.index(200) == 100\n        assert v.index(600) == 500\n\n    def test_random_operations(self):\n\
    \        \"\"\"Test random operations for robustness\"\"\"\n        random.seed(42)\
    \  # For reproducibility\n        \n        # Create test data\n        data =\
    \ list(range(100))\n        original_data = data.copy()\n        \n        # Create\
    \ view\n        start, end = 20, 80\n        v = view(data, start, end)\n    \
    \    \n        # Perform random operations\n        for _ in range(50):\n    \
    \        op = random.choice(['read', 'write', 'contains'])\n            \n   \
    \         if op == 'read' and len(v) > 0:\n                idx = random.randint(0,\
    \ len(v) - 1)\n                val = v[idx]\n                assert val == data[start\
    \ + idx]\n                \n            elif op == 'write' and len(v) > 0:\n \
    \               idx = random.randint(0, len(v) - 1)\n                new_val =\
    \ random.randint(1000, 2000)\n                v[idx] = new_val\n             \
    \   assert data[start + idx] == new_val\n                \n            elif op\
    \ == 'contains':\n                search_val = random.choice(original_data)\n\
    \                result = search_val in v\n                # Verify manually\n\
    \                expected = any(data[i] == search_val for i in range(start, min(start\
    \ + len(v), len(data))))\n                assert result == expected\n\n    def\
    \ test_view_modification_boundary_safety(self):\n        \"\"\"Test that view\
    \ modifications don't affect data outside the view\"\"\"\n        data = [1, 2,\
    \ 3, 4, 5, 6, 7, 8, 9, 10]\n        original = data.copy()\n        \n       \
    \ v = view(data, 3, 7)  # View of [4, 5, 6, 7]\n        \n        # Modify view\n\
    \        v[0] = 40\n        v[1] = 50\n        v[2] = 60\n        v[3] = 70\n\
    \        \n        # Check that only the view range was modified\n        assert\
    \ data[0:3] == original[0:3]  # Before view unchanged\n        assert data[7:]\
    \ == original[7:]    # After view unchanged\n        assert data[3:7] == [40,\
    \ 50, 60, 70]  # View range changed\n\nfrom cp_library.ds.view.view_cls import\
    \ view\n\nif __name__ == '__main__':\n    from cp_library.test.unittest_helper\
    \ import run_verification_helper_unittest\n    run_verification_helper_unittest()"
  dependsOn:
  - cp_library/ds/view/view_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/ds/list/list_find_fn.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/unittests/ds/view/view_cls_test.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/view/view_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/view/view_cls_test.py
- /verify/test/unittests/ds/view/view_cls_test.py.html
title: test/unittests/ds/view/view_cls_test.py
---
