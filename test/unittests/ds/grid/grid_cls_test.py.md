---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/grid/grid_cls.py
    title: cp_library/ds/grid/grid_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view_cls.py
    title: cp_library/ds/view/view_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
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
    \nimport pytest\nimport random\n\nclass TestGrid:\n    \"\"\"\n    Tests for Grid\
    \ class with bit-packed storage.\n    \n    IMPORTANT: Grid uses Packer(W-1) for\
    \ bit packing, which means:\n    - Packer(W-1) creates s = (W-1).bit_length()\
    \ \n    - Each row has length 1 << s (next power of 2 >= W)\n    - Examples:\n\
    \      - W=3: Packer(2) \u2192 s=2 \u2192 row length = 4\n      - W=5: Packer(4)\
    \ \u2192 s=3 \u2192 row length = 8  \n      - W=8: Packer(7) \u2192 s=3 \u2192\
    \ row length = 8\n      - W=50: Packer(49) \u2192 s=6 \u2192 row length = 64\n\
    \    \"\"\"\n    def test_initialization_single_value(self):\n        \"\"\"Test\
    \ initialization with a single value\"\"\"\n        grid = Grid(3, 4, 5)\n   \
    \     \n        assert grid.H == 3\n        assert grid.W == 4\n        assert\
    \ len(grid) == 3\n        \n        # All elements should be 5\n        for i\
    \ in range(3):\n            for j in range(4):\n                assert grid(i,\
    \ j) == 5\n\n    def test_initialization_flat_list(self):\n        \"\"\"Test\
    \ initialization with a flat list\"\"\"\n        # List smaller than grid size\n\
    \        flat_list = [1, 2, 3, 4, 5, 6, 7, 8]\n        grid = Grid(2, 4, flat_list)\n\
    \        \n        assert grid.H == 2\n        assert grid.W == 4\n        \n\
    \        # Should map flat list to 2D grid row by row\n        expected = [\n\
    \            [1, 2, 3, 4],\n            [5, 6, 7, 8]\n        ]\n        for i\
    \ in range(2):\n            for j in range(4):\n                assert grid(i,\
    \ j) == expected[i][j]\n\n    def test_initialization_2d_list(self):\n       \
    \ \"\"\"Test initialization with a 2D list\"\"\"\n        grid_2d = [\n      \
    \      [1, 2, 3],\n            [4, 5, 6],\n            [7, 8, 9]\n        ]\n\
    \        grid = Grid(3, 3, grid_2d)\n        \n        assert grid.H == 3\n  \
    \      assert grid.W == 3\n        \n        for i in range(3):\n            for\
    \ j in range(3):\n                assert grid(i, j) == grid_2d[i][j]\n\n    def\
    \ test_initialization_large_list(self):\n        \"\"\"Test initialization with\
    \ a list larger than grid size\"\"\"\n        large_list = list(range(20))\n \
    \       grid = Grid(2, 3, large_list)\n        \n        assert grid.H == 2\n\
    \        assert grid.W == 3\n        \n        # Should use the list directly\n\
    \        for i in range(2):\n            for j in range(3):\n                #\
    \ Direct access to packed array\n                expected_index = grid.pkr.enc(i,\
    \ j)\n                assert grid(i, j) == large_list[expected_index]\n\n    def\
    \ test_getitem_returns_view(self):\n        \"\"\"Test that __getitem__ returns\
    \ a view of the row\"\"\"\n        grid_2d = [\n            [1, 2, 3, 4],\n  \
    \          [5, 6, 7, 8],\n            [9, 10, 11, 12]\n        ]\n        grid\
    \ = Grid(3, 4, grid_2d)\n        \n        # Get row views\n        row0 = grid[0]\n\
    \        row1 = grid[1]\n        row2 = grid[2]\n        \n        # Check row\
    \ contents - Packer(4-1) has s=2, so row length is 1<<2=4\n        assert len(row0)\
    \ == 4  # Bit packing: exactly matches width\n        assert row0[0] == 1\n  \
    \      assert row0[3] == 4\n        \n        assert len(row1) == 4\n        assert\
    \ row1[0] == 5\n        assert row1[3] == 8\n        \n        assert len(row2)\
    \ == 4\n        assert row2[0] == 9\n        assert row2[3] == 12\n\n    def test_call_method(self):\n\
    \        \"\"\"Test direct element access via __call__\"\"\"\n        grid = Grid(3,\
    \ 3, [\n            [1, 2, 3],\n            [4, 5, 6],\n            [7, 8, 9]\n\
    \        ])\n        \n        # Test all positions\n        assert grid(0, 0)\
    \ == 1\n        assert grid(0, 2) == 3\n        assert grid(1, 1) == 5\n     \
    \   assert grid(2, 0) == 7\n        assert grid(2, 2) == 9\n\n    def test_set_method(self):\n\
    \        \"\"\"Test setting individual elements\"\"\"\n        grid = Grid(2,\
    \ 3, 0)  # Initialize with zeros\n        \n        # Set some values\n      \
    \  grid.set(0, 0, 10)\n        grid.set(0, 2, 30)\n        grid.set(1, 1, 50)\n\
    \        \n        # Check that values were set correctly\n        assert grid(0,\
    \ 0) == 10\n        assert grid(0, 1) == 0   # unchanged\n        assert grid(0,\
    \ 2) == 30\n        assert grid(1, 0) == 0   # unchanged\n        assert grid(1,\
    \ 1) == 50\n        assert grid(1, 2) == 0   # unchanged\n\n    def test_view_modifications(self):\n\
    \        \"\"\"Test that modifications through views affect the underlying data\"\
    \"\"\n        grid = Grid(2, 3, [\n            [1, 2, 3],\n            [4, 5,\
    \ 6]\n        ])\n        \n        # Get a view and modify it\n        row0 =\
    \ grid[0]\n        row0[1] = 20\n        row0[2] = 30\n        \n        # Check\
    \ that underlying data changed\n        assert grid(0, 0) == 1   # unchanged\n\
    \        assert grid(0, 1) == 20  # changed\n        assert grid(0, 2) == 30 \
    \ # changed\n        assert grid(1, 0) == 4   # unchanged\n\n    def test_view_isolation(self):\n\
    \        \"\"\"Test that different row views don't interfere\"\"\"\n        grid\
    \ = Grid(3, 2, [\n            [1, 2],\n            [3, 4],\n            [5, 6]\n\
    \        ])\n        \n        # Get multiple views\n        row0 = grid[0]\n\
    \        row1 = grid[1]\n        row2 = grid[2]\n        \n        # Modify different\
    \ views\n        row0[0] = 10\n        row1[1] = 40\n        row2[0] = 50\n  \
    \      \n        # Check that modifications are isolated\n        assert grid(0,\
    \ 0) == 10\n        assert grid(0, 1) == 2   # unchanged\n        assert grid(1,\
    \ 0) == 3   # unchanged\n        assert grid(1, 1) == 40\n        assert grid(2,\
    \ 0) == 50\n        assert grid(2, 1) == 6   # unchanged\n\n    def test_different_data_types(self):\n\
    \        \"\"\"Test grid with different data types\"\"\"\n        # String grid\n\
    \        str_grid = Grid(2, 2, [\n            ['a', 'b'],\n            ['c', 'd']\n\
    \        ])\n        \n        assert str_grid(0, 0) == 'a'\n        assert str_grid(1,\
    \ 1) == 'd'\n        \n        str_grid.set(0, 1, 'x')\n        assert str_grid(0,\
    \ 1) == 'x'\n        \n        # Float grid\n        float_grid = Grid(2, 2, 3.14)\n\
    \        assert float_grid(0, 0) == 3.14\n        assert float_grid(1, 1) == 3.14\n\
    \n    def test_edge_cases(self):\n        \"\"\"Test edge cases and boundary conditions\"\
    \"\"\n        # Single cell grid\n        single_grid = Grid(1, 1, 42)\n     \
    \   assert len(single_grid) == 1\n        assert single_grid(0, 0) == 42\n   \
    \     \n        single_grid.set(0, 0, 99)\n        assert single_grid(0, 0) ==\
    \ 99\n        \n        # Single row grid\n        row_grid = Grid(1, 5, [1, 2,\
    \ 3, 4, 5])\n        assert len(row_grid) == 1\n        row = row_grid[0]\n  \
    \      # Packer(5-1) has s=3, so row length is 1<<3=8, but we only use first 5\n\
    \        assert len(row) == 8  # Bit packing rounds up to power of 2\n       \
    \ for j in range(5):  # Only check the actual width\n            assert row[j]\
    \ == j + 1\n        \n        # Single column grid\n        col_grid = Grid(5,\
    \ 1, [\n            [10],\n            [20],\n            [30],\n            [40],\n\
    \            [50]\n        ])\n        assert len(col_grid) == 5\n        for\
    \ i in range(5):\n            assert col_grid(i, 0) == (i + 1) * 10\n\n    def\
    \ test_bounds_checking(self):\n        \"\"\"Test behavior with out-of-bounds\
    \ access (implementation dependent)\"\"\"\n        grid = Grid(2, 3, [\n     \
    \       [1, 2, 3],\n            [4, 5, 6]\n        ])\n        \n        # Valid\
    \ access should work\n        assert grid(0, 0) == 1\n        assert grid(1, 2)\
    \ == 6\n        \n        # Views should have correct length (bit packed)\n  \
    \      row0 = grid[0]\n        # Packer(3-1) has s=2, so row length is 1<<2=4\n\
    \        assert len(row0) == 4\n        \n        # Out of bounds view access\
    \ should raise IndexError\n        with pytest.raises(IndexError):\n         \
    \   row0[4]  # Row length is 4 due to bit packing\n\n    def test_large_grid(self):\n\
    \        \"\"\"Test with a larger grid to ensure performance and correctness\"\
    \"\"\n        H, W = 50, 50\n        \n        # Create grid with predictable\
    \ pattern\n        grid_data = []\n        for i in range(H):\n            row\
    \ = []\n            for j in range(W):\n                row.append(i * 100 + j)\n\
    \            grid_data.append(row)\n        \n        grid = Grid(H, W, grid_data)\n\
    \        \n        assert grid.H == H\n        assert grid.W == W\n        assert\
    \ len(grid) == H\n        \n        # Test random access\n        random.seed(42)\
    \  # For reproducibility\n        for _ in range(100):\n            i = random.randint(0,\
    \ H - 1)\n            j = random.randint(0, W - 1)\n            expected = i *\
    \ 100 + j\n            assert grid(i, j) == expected\n        \n        # Test\
    \ row access\n        for i in range(min(10, H)):  # Test first 10 rows\n    \
    \        row = grid[i]\n            # Packer(50-1) has s=6, so row length is 1<<6=64\n\
    \            assert len(row) == 64  # Bit packing rounds up to power of 2\n  \
    \          for j in range(W):  # Only check actual width\n                assert\
    \ row[j] == i * 100 + j\n\n    def test_grid_modification_patterns(self):\n  \
    \      \"\"\"Test various modification patterns\"\"\"\n        grid = Grid(4,\
    \ 4, 0)\n        \n        # Fill diagonal\n        for i in range(4):\n     \
    \       grid.set(i, i, i + 1)\n        \n        # Check diagonal\n        for\
    \ i in range(4):\n            assert grid(i, i) == i + 1\n            # Check\
    \ non-diagonal elements are still 0\n            for j in range(4):\n        \
    \        if i != j:\n                    assert grid(i, j) == 0\n        \n  \
    \      # Modify through views\n        for i in range(4):\n            row = grid[i]\n\
    \            row[0] = 10 + i  # First column\n            row[3] = 20 + i  # Last\
    \ column\n        \n        # Check modifications\n        for i in range(4):\n\
    \            assert grid(i, 0) == 10 + i\n            assert grid(i, 3) == 20\
    \ + i\n\n    def test_grid_view_operations(self):\n        \"\"\"Test various\
    \ operations on grid views\"\"\"\n        grid = Grid(3, 4, [\n            [4,\
    \ 3, 2, 1],\n            [8, 7, 6, 5],\n            [12, 11, 10, 9]\n        ])\n\
    \        \n        # Test sorting a row\n        row0 = grid[0]\n        row0.sort()\n\
    \        \n        # Check that row is now sorted\n        for j in range(3):\n\
    \            assert row0[j] <= row0[j + 1]\n        \n        # Original grid\
    \ should be modified\n        assert grid(0, 0) == 1\n        assert grid(0, 1)\
    \ == 2\n        assert grid(0, 2) == 3\n        assert grid(0, 3) == 4\n     \
    \   \n        # Other rows should be unchanged\n        assert grid(1, 0) == 8\n\
    \        assert grid(2, 0) == 12\n\n    def test_memory_efficiency(self):\n  \
    \      \"\"\"Test that grid uses bit packing efficiently\"\"\"\n        grid =\
    \ Grid(4, 8, 0)\n        \n        # Check that packer is set up correctly\n \
    \       assert grid.pkr is not None\n        assert grid.W == 8\n        \n  \
    \      # Packer(8-1) has s=3, so each row has 1<<3=8 slots (exactly matches width)\n\
    \        row = grid[0]\n        assert len(row) == 8\n        \n        # The\
    \ packer should efficiently encode coordinates\n        for i in range(4):\n \
    \           for j in range(8):\n                # Set unique values to test encoding/decoding\n\
    \                value = i * 10 + j\n                grid.set(i, j, value)\n \
    \               assert grid(i, j) == value\n\n    def test_initialization_edge_cases(self):\n\
    \        \"\"\"Test edge cases in initialization\"\"\"\n        # Small flat list\
    \ (smaller than grid)\n        grid1 = Grid(2, 2, [42, 43, 44, 45])  # Provide\
    \ enough elements\n        # Should map flat list to grid\n        expected_values\
    \ = [42, 43, 44, 45]\n        for i in range(2):\n            for j in range(2):\n\
    \                assert grid1(i, j) == expected_values[i * 2 + j]\n        \n\
    \        # Mixed type initialization (though not typical usage)\n        grid2\
    \ = Grid(2, 2, [\n            [1, 2],\n            [3, 4]\n        ])\n      \
    \  \n        # Test that it works correctly\n        assert grid2(0, 0) == 1\n\
    \        assert grid2(1, 1) == 4\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\nimport typing\nfrom numbers import Number\nfrom types import\
    \ GenericAlias \nfrom typing import Callable, Collection\n\n\nclass IOBase:\n\
    \    @property\n    def char(io) -> bool: ...\n    @property\n    def writable(io)\
    \ -> bool: ...\n    def __next__(io) -> str: ...\n    def write(io, s: str) ->\
    \ None: ...\n    def readline(io) -> str: ...\n    def readtoken(io) -> str: ...\n\
    \    def readtokens(io) -> list[str]: ...\n    def readints(io) -> list[int]:\
    \ ...\n    def readdigits(io) -> list[int]: ...\n    def readnums(io) -> list[int]:\
    \ ...\n    def readchar(io) -> str: ...\n    def readchars(io) -> str: ...\n \
    \   def readinto(io, lst: list[str]) -> list[str]: ...\n    def readcharsinto(io,\
    \ lst: list[str]) -> list[str]: ...\n    def readtokensinto(io, lst: list[str])\
    \ -> list[str]: ...\n    def readintsinto(io, lst: list[int]) -> list[int]: ...\n\
    \    def readdigitsinto(io, lst: list[int]) -> list[int]: ...\n    def readnumsinto(io,\
    \ lst: list[int]) -> list[int]: ...\n    def wait(io): ...\n    def flush(io)\
    \ -> None: ...\n    def line(io) -> list[str]: ...\n\nclass Parser:\n    def __init__(self,\
    \ spec):  self.parse = Parser.compile(spec)\n    def __call__(self, io: IOBase):\
    \ return self.parse(io)\n    @staticmethod\n    def compile_type(cls, args = ()):\n\
    \        if issubclass(cls, Parsable): return cls.compile(*args)\n        elif\
    \ issubclass(cls, (Number, str)):\n            def parse(io: IOBase): return cls(next(io))\
    \              \n            return parse\n        elif issubclass(cls, tuple):\
    \ return Parser.compile_tuple(cls, args)\n        elif issubclass(cls, Collection):\
    \ return Parser.compile_collection(cls, args)\n        elif callable(cls):\n \
    \           def parse(io: IOBase): return cls(next(io))              \n      \
    \      return parse\n        else: raise NotImplementedError()\n    @staticmethod\n\
    \    def compile(spec=int):\n        if isinstance(spec, (type, GenericAlias)):\n\
    \            cls, args = typing.get_origin(spec) or spec, typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(io: IOBase): return cls(next(io)) + offset\n            return\
    \ parse\n        elif isinstance(args := spec, tuple): return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection): return Parser.compile_collection(type(spec),\
    \ args)\n        elif isinstance(fn := spec, Callable): \n            def parse(io:\
    \ IOBase): return fn(next(io))\n            return parse\n        else: raise\
    \ NotImplementedError()\n    @staticmethod\n    def compile_line(cls, spec=int):\n\
    \        if spec is int:\n            def parse(io: IOBase): return cls(io.readnums())\n\
    \        else:\n            fn = Parser.compile(spec)\n            def parse(io:\
    \ IOBase): return cls([fn(io) for _ in io.wait()])\n        return parse\n   \
    \ @staticmethod\n    def compile_repeat(cls, spec, N):\n        fn = Parser.compile(spec)\n\
    \        def parse(io: IOBase): return cls([fn(io) for _ in range(N)])\n     \
    \   return parse\n    @staticmethod\n    def compile_children(cls, specs):\n \
    \       fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(io:\
    \ IOBase): return cls([fn(io) for fn in fns])  \n        return parse\n    @staticmethod\n\
    \    def compile_tuple(cls, specs):\n        if isinstance(specs, (tuple,list))\
    \ and len(specs) == 2 and specs[1] is ...: return Parser.compile_line(cls, specs[0])\n\
    \        else: return Parser.compile_children(cls, specs)\n    @staticmethod\n\
    \    def compile_collection(cls, specs):\n        if not specs or len(specs) ==\
    \ 1 or isinstance(specs, set):\n            return Parser.compile_line(cls, *specs)\n\
    \        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and isinstance(specs[1],\
    \ int)):\n            return Parser.compile_repeat(cls, specs[0], specs[1])\n\
    \        else:\n            raise NotImplementedError()\nclass Parsable:\n   \
    \ @classmethod\n    def compile(cls):\n        def parser(io: IOBase): return\
    \ cls(next(io))\n        return parser\n    @classmethod\n    def __class_getitem__(cls,\
    \ item): return GenericAlias(cls, item)\n\nfrom typing import Generic\nfrom typing\
    \ import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U'); _T1\
    \ = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4');\
    \ _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\nimport sys\n\ndef list_find(lst:\
    \ list, value, start = 0, stop = sys.maxsize):\n    try:\n        return lst.index(value,\
    \ start, stop)\n    except:\n        return -1\n\n\nclass view(Generic[_T]):\n\
    \    __slots__ = 'A', 'l', 'r'\n    def __init__(V, A: list[_T], l: int = 0, r:\
    \ int = 0): V.A, V.l, V.r = A, l, r\n    def __len__(V): return V.r - V.l\n  \
    \  def __getitem__(V, i: int): \n        if 0 <= i < V.r - V.l: return V.A[V.l+i]\n\
    \        else: raise IndexError\n    def __setitem__(V, i: int, v: _T): V.A[V.l+i]\
    \ = v\n    def __contains__(V, v: _T): return list_find(V.A, v, V.l, V.r) != -1\n\
    \    def set_range(V, l: int, r: int): V.l, V.r = l, r\n    def index(V, v: _T):\
    \ return V.A.index(v, V.l, V.r) - V.l\n    def reverse(V):\n        l, r = V.l,\
    \ V.r-1\n        while l < r: V.A[l], V.A[r] = V.A[r], V.A[l]; l += 1; r -= 1\n\
    \    def sort(V, /, *args, **kwargs):\n        A = V.A[V.l:V.r]; A.sort(*args,\
    \ **kwargs)\n        for i,a in enumerate(A,V.l): V.A[i] = a\n    def pop(V):\
    \ V.r -= 1; return V.A[V.r]\n    def append(V, v: _T): V.A[V.r] = v; V.r += 1\n\
    \    def popleft(V): V.l += 1; return V.A[V.l-1]\n    def appendleft(V, v: _T):\
    \ V.l -= 1; V.A[V.l] = v; \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\
    from typing import Generic, Union\n\n\n\nclass Packer:\n    __slots__ = 's', 'm'\n\
    \    def __init__(P, mx: int): P.s = mx.bit_length(); P.m = (1 << P.s) - 1\n \
    \   def enc(P, a: int, b: int): return a << P.s | b\n    def dec(P, x: int) ->\
    \ tuple[int, int]: return x >> P.s, x & P.m\n    def enumerate(P, A, reverse=False):\
    \ P.ienumerate(A:=list(A), reverse); return A\n    def ienumerate(P, A, reverse=False):\n\
    \        if reverse:\n            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n\
    \        else:\n            for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def\
    \ indices(P, A: list[int]): P.iindices(A:=list(A)); return A\n    def iindices(P,\
    \ A):\n        for i,a in enumerate(A): A[i] = P.m&a\n\n\nclass Grid(Generic[_T],\
    \ Parsable):\n    __slots__ = 'pkr', 'size', 'H', 'W', 'A'\n    def __init__(G,\
    \ H: int, W: int, A: Union[_T, list[_T], list[list[_T]]], pkr = None):\n     \
    \   G.pkr = pkr or Packer(W-1); G.size = H << G.pkr.s; G.H, G.W = H, W\n     \
    \   if isinstance(A, list):\n            if isinstance(A[0], list):\n        \
    \        G.A = [A[0][0]]*G.size\n                for i in range(H):\n        \
    \            ii = i << G.pkr.s\n                    for j in range(W): G.A[ii|j]\
    \ = A[i][j]\n            elif len(A) < G.size:\n                G.A = [A[0]]*G.size\n\
    \                for i in range(H):\n                    ii = i << G.pkr.s\n \
    \                   for j in range(W): G.A[ii|j] = A[i*W+j]\n            else:\n\
    \                G.A = A\n        else:\n            G.A = [A] * G.size\n    def\
    \ __len__(G): return G.H\n    def __getitem__(G, i: int): \n        if 0 <= i\
    \ < G.H: return view(G.A, i<<G.pkr.s, (i+1)<<G.pkr.s)\n        else: raise IndexError\n\
    \    def __call__(G, i: int, j: int): return G.A[G.pkr.enc(i,j)]\n    def set(G,\
    \ i: int, j: int, v: _T): G.A[G.pkr.enc(i,j)] = v\n\n    @classmethod\n    def\
    \ compile(cls, H: int, W: int, T: type = int):\n        pkr = Packer(W-1); size\
    \ = H << pkr.s\n        if T is int:\n            def parse(io: IOBase):\n   \
    \             A = [0]*size\n                for i in range(H):\n             \
    \       for j, a in enumerate(io.readints()): A[pkr.enc(i,j)] = a\n          \
    \      return cls(H, W, A, pkr)\n        elif T is str:\n            def parse(io:\
    \ IOBase):\n                A = ['']*size\n                for i in range(H):\n\
    \                    for j, s in enumerate(io.line()): A[pkr.enc(i,j)] = s\n \
    \               return cls(H, W, A, pkr)\n        else:\n            elm = Parser.compile(T)\n\
    \            def parse(io: IOBase):\n                A = [None]*size\n       \
    \         for i in range(H):\n                    for j in range(W): A[pkr.enc(i,j)]\
    \ = elm(io)\n                return cls(H, W, A, pkr)\n        return parse\n\n\
    if __name__ == '__main__':\n    \"\"\"\n    Helper for making unittest files compatible\
    \ with verification-helper.\n    \n    This module provides a helper function\
    \ to run a dummy Library Checker test\n    so that unittest files can be verified\
    \ by oj-verify.\n    \"\"\"\n    \n    def run_verification_helper_unittest():\n\
    \        \"\"\"\n        Run a dummy AOJ ITP1_1_A test for verification-helper\
    \ compatibility.\n        \n        This function should be called in the __main__\
    \ block of unittest files\n        that need to be compatible with verification-helper.\n\
    \        \n        The function:\n        1. Prints \"Hello World\" (AOJ ITP1_1_A\
    \ solution)\n        2. Runs pytest for the calling test file\n        3. Exits\
    \ with the pytest result code\n        \"\"\"\n        \n        # Print \"Hello\
    \ World\" for AOJ ITP1_1_A problem\n        print(\"Hello World\")\n        \n\
    \        import io\n        from contextlib import redirect_stdout, redirect_stderr\n\
    \    \n        # Capture all output during test execution\n        output = io.StringIO()\n\
    \        with redirect_stdout(output), redirect_stderr(output):\n            #\
    \ Get the calling module's file path\n            frame = sys._getframe(1)\n \
    \           test_file = frame.f_globals.get('__file__')\n            if test_file\
    \ is None:\n                test_file = sys.argv[0]\n            result = pytest.main([test_file])\n\
    \        \n        if result != 0: \n            print(output.getvalue())\n  \
    \      sys.exit(result)\n    run_verification_helper_unittest()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    \nimport pytest\nimport random\n\nclass TestGrid:\n    \"\"\"\n    Tests for Grid\
    \ class with bit-packed storage.\n    \n    IMPORTANT: Grid uses Packer(W-1) for\
    \ bit packing, which means:\n    - Packer(W-1) creates s = (W-1).bit_length()\
    \ \n    - Each row has length 1 << s (next power of 2 >= W)\n    - Examples:\n\
    \      - W=3: Packer(2) \u2192 s=2 \u2192 row length = 4\n      - W=5: Packer(4)\
    \ \u2192 s=3 \u2192 row length = 8  \n      - W=8: Packer(7) \u2192 s=3 \u2192\
    \ row length = 8\n      - W=50: Packer(49) \u2192 s=6 \u2192 row length = 64\n\
    \    \"\"\"\n    def test_initialization_single_value(self):\n        \"\"\"Test\
    \ initialization with a single value\"\"\"\n        grid = Grid(3, 4, 5)\n   \
    \     \n        assert grid.H == 3\n        assert grid.W == 4\n        assert\
    \ len(grid) == 3\n        \n        # All elements should be 5\n        for i\
    \ in range(3):\n            for j in range(4):\n                assert grid(i,\
    \ j) == 5\n\n    def test_initialization_flat_list(self):\n        \"\"\"Test\
    \ initialization with a flat list\"\"\"\n        # List smaller than grid size\n\
    \        flat_list = [1, 2, 3, 4, 5, 6, 7, 8]\n        grid = Grid(2, 4, flat_list)\n\
    \        \n        assert grid.H == 2\n        assert grid.W == 4\n        \n\
    \        # Should map flat list to 2D grid row by row\n        expected = [\n\
    \            [1, 2, 3, 4],\n            [5, 6, 7, 8]\n        ]\n        for i\
    \ in range(2):\n            for j in range(4):\n                assert grid(i,\
    \ j) == expected[i][j]\n\n    def test_initialization_2d_list(self):\n       \
    \ \"\"\"Test initialization with a 2D list\"\"\"\n        grid_2d = [\n      \
    \      [1, 2, 3],\n            [4, 5, 6],\n            [7, 8, 9]\n        ]\n\
    \        grid = Grid(3, 3, grid_2d)\n        \n        assert grid.H == 3\n  \
    \      assert grid.W == 3\n        \n        for i in range(3):\n            for\
    \ j in range(3):\n                assert grid(i, j) == grid_2d[i][j]\n\n    def\
    \ test_initialization_large_list(self):\n        \"\"\"Test initialization with\
    \ a list larger than grid size\"\"\"\n        large_list = list(range(20))\n \
    \       grid = Grid(2, 3, large_list)\n        \n        assert grid.H == 2\n\
    \        assert grid.W == 3\n        \n        # Should use the list directly\n\
    \        for i in range(2):\n            for j in range(3):\n                #\
    \ Direct access to packed array\n                expected_index = grid.pkr.enc(i,\
    \ j)\n                assert grid(i, j) == large_list[expected_index]\n\n    def\
    \ test_getitem_returns_view(self):\n        \"\"\"Test that __getitem__ returns\
    \ a view of the row\"\"\"\n        grid_2d = [\n            [1, 2, 3, 4],\n  \
    \          [5, 6, 7, 8],\n            [9, 10, 11, 12]\n        ]\n        grid\
    \ = Grid(3, 4, grid_2d)\n        \n        # Get row views\n        row0 = grid[0]\n\
    \        row1 = grid[1]\n        row2 = grid[2]\n        \n        # Check row\
    \ contents - Packer(4-1) has s=2, so row length is 1<<2=4\n        assert len(row0)\
    \ == 4  # Bit packing: exactly matches width\n        assert row0[0] == 1\n  \
    \      assert row0[3] == 4\n        \n        assert len(row1) == 4\n        assert\
    \ row1[0] == 5\n        assert row1[3] == 8\n        \n        assert len(row2)\
    \ == 4\n        assert row2[0] == 9\n        assert row2[3] == 12\n\n    def test_call_method(self):\n\
    \        \"\"\"Test direct element access via __call__\"\"\"\n        grid = Grid(3,\
    \ 3, [\n            [1, 2, 3],\n            [4, 5, 6],\n            [7, 8, 9]\n\
    \        ])\n        \n        # Test all positions\n        assert grid(0, 0)\
    \ == 1\n        assert grid(0, 2) == 3\n        assert grid(1, 1) == 5\n     \
    \   assert grid(2, 0) == 7\n        assert grid(2, 2) == 9\n\n    def test_set_method(self):\n\
    \        \"\"\"Test setting individual elements\"\"\"\n        grid = Grid(2,\
    \ 3, 0)  # Initialize with zeros\n        \n        # Set some values\n      \
    \  grid.set(0, 0, 10)\n        grid.set(0, 2, 30)\n        grid.set(1, 1, 50)\n\
    \        \n        # Check that values were set correctly\n        assert grid(0,\
    \ 0) == 10\n        assert grid(0, 1) == 0   # unchanged\n        assert grid(0,\
    \ 2) == 30\n        assert grid(1, 0) == 0   # unchanged\n        assert grid(1,\
    \ 1) == 50\n        assert grid(1, 2) == 0   # unchanged\n\n    def test_view_modifications(self):\n\
    \        \"\"\"Test that modifications through views affect the underlying data\"\
    \"\"\n        grid = Grid(2, 3, [\n            [1, 2, 3],\n            [4, 5,\
    \ 6]\n        ])\n        \n        # Get a view and modify it\n        row0 =\
    \ grid[0]\n        row0[1] = 20\n        row0[2] = 30\n        \n        # Check\
    \ that underlying data changed\n        assert grid(0, 0) == 1   # unchanged\n\
    \        assert grid(0, 1) == 20  # changed\n        assert grid(0, 2) == 30 \
    \ # changed\n        assert grid(1, 0) == 4   # unchanged\n\n    def test_view_isolation(self):\n\
    \        \"\"\"Test that different row views don't interfere\"\"\"\n        grid\
    \ = Grid(3, 2, [\n            [1, 2],\n            [3, 4],\n            [5, 6]\n\
    \        ])\n        \n        # Get multiple views\n        row0 = grid[0]\n\
    \        row1 = grid[1]\n        row2 = grid[2]\n        \n        # Modify different\
    \ views\n        row0[0] = 10\n        row1[1] = 40\n        row2[0] = 50\n  \
    \      \n        # Check that modifications are isolated\n        assert grid(0,\
    \ 0) == 10\n        assert grid(0, 1) == 2   # unchanged\n        assert grid(1,\
    \ 0) == 3   # unchanged\n        assert grid(1, 1) == 40\n        assert grid(2,\
    \ 0) == 50\n        assert grid(2, 1) == 6   # unchanged\n\n    def test_different_data_types(self):\n\
    \        \"\"\"Test grid with different data types\"\"\"\n        # String grid\n\
    \        str_grid = Grid(2, 2, [\n            ['a', 'b'],\n            ['c', 'd']\n\
    \        ])\n        \n        assert str_grid(0, 0) == 'a'\n        assert str_grid(1,\
    \ 1) == 'd'\n        \n        str_grid.set(0, 1, 'x')\n        assert str_grid(0,\
    \ 1) == 'x'\n        \n        # Float grid\n        float_grid = Grid(2, 2, 3.14)\n\
    \        assert float_grid(0, 0) == 3.14\n        assert float_grid(1, 1) == 3.14\n\
    \n    def test_edge_cases(self):\n        \"\"\"Test edge cases and boundary conditions\"\
    \"\"\n        # Single cell grid\n        single_grid = Grid(1, 1, 42)\n     \
    \   assert len(single_grid) == 1\n        assert single_grid(0, 0) == 42\n   \
    \     \n        single_grid.set(0, 0, 99)\n        assert single_grid(0, 0) ==\
    \ 99\n        \n        # Single row grid\n        row_grid = Grid(1, 5, [1, 2,\
    \ 3, 4, 5])\n        assert len(row_grid) == 1\n        row = row_grid[0]\n  \
    \      # Packer(5-1) has s=3, so row length is 1<<3=8, but we only use first 5\n\
    \        assert len(row) == 8  # Bit packing rounds up to power of 2\n       \
    \ for j in range(5):  # Only check the actual width\n            assert row[j]\
    \ == j + 1\n        \n        # Single column grid\n        col_grid = Grid(5,\
    \ 1, [\n            [10],\n            [20],\n            [30],\n            [40],\n\
    \            [50]\n        ])\n        assert len(col_grid) == 5\n        for\
    \ i in range(5):\n            assert col_grid(i, 0) == (i + 1) * 10\n\n    def\
    \ test_bounds_checking(self):\n        \"\"\"Test behavior with out-of-bounds\
    \ access (implementation dependent)\"\"\"\n        grid = Grid(2, 3, [\n     \
    \       [1, 2, 3],\n            [4, 5, 6]\n        ])\n        \n        # Valid\
    \ access should work\n        assert grid(0, 0) == 1\n        assert grid(1, 2)\
    \ == 6\n        \n        # Views should have correct length (bit packed)\n  \
    \      row0 = grid[0]\n        # Packer(3-1) has s=2, so row length is 1<<2=4\n\
    \        assert len(row0) == 4\n        \n        # Out of bounds view access\
    \ should raise IndexError\n        with pytest.raises(IndexError):\n         \
    \   row0[4]  # Row length is 4 due to bit packing\n\n    def test_large_grid(self):\n\
    \        \"\"\"Test with a larger grid to ensure performance and correctness\"\
    \"\"\n        H, W = 50, 50\n        \n        # Create grid with predictable\
    \ pattern\n        grid_data = []\n        for i in range(H):\n            row\
    \ = []\n            for j in range(W):\n                row.append(i * 100 + j)\n\
    \            grid_data.append(row)\n        \n        grid = Grid(H, W, grid_data)\n\
    \        \n        assert grid.H == H\n        assert grid.W == W\n        assert\
    \ len(grid) == H\n        \n        # Test random access\n        random.seed(42)\
    \  # For reproducibility\n        for _ in range(100):\n            i = random.randint(0,\
    \ H - 1)\n            j = random.randint(0, W - 1)\n            expected = i *\
    \ 100 + j\n            assert grid(i, j) == expected\n        \n        # Test\
    \ row access\n        for i in range(min(10, H)):  # Test first 10 rows\n    \
    \        row = grid[i]\n            # Packer(50-1) has s=6, so row length is 1<<6=64\n\
    \            assert len(row) == 64  # Bit packing rounds up to power of 2\n  \
    \          for j in range(W):  # Only check actual width\n                assert\
    \ row[j] == i * 100 + j\n\n    def test_grid_modification_patterns(self):\n  \
    \      \"\"\"Test various modification patterns\"\"\"\n        grid = Grid(4,\
    \ 4, 0)\n        \n        # Fill diagonal\n        for i in range(4):\n     \
    \       grid.set(i, i, i + 1)\n        \n        # Check diagonal\n        for\
    \ i in range(4):\n            assert grid(i, i) == i + 1\n            # Check\
    \ non-diagonal elements are still 0\n            for j in range(4):\n        \
    \        if i != j:\n                    assert grid(i, j) == 0\n        \n  \
    \      # Modify through views\n        for i in range(4):\n            row = grid[i]\n\
    \            row[0] = 10 + i  # First column\n            row[3] = 20 + i  # Last\
    \ column\n        \n        # Check modifications\n        for i in range(4):\n\
    \            assert grid(i, 0) == 10 + i\n            assert grid(i, 3) == 20\
    \ + i\n\n    def test_grid_view_operations(self):\n        \"\"\"Test various\
    \ operations on grid views\"\"\"\n        grid = Grid(3, 4, [\n            [4,\
    \ 3, 2, 1],\n            [8, 7, 6, 5],\n            [12, 11, 10, 9]\n        ])\n\
    \        \n        # Test sorting a row\n        row0 = grid[0]\n        row0.sort()\n\
    \        \n        # Check that row is now sorted\n        for j in range(3):\n\
    \            assert row0[j] <= row0[j + 1]\n        \n        # Original grid\
    \ should be modified\n        assert grid(0, 0) == 1\n        assert grid(0, 1)\
    \ == 2\n        assert grid(0, 2) == 3\n        assert grid(0, 3) == 4\n     \
    \   \n        # Other rows should be unchanged\n        assert grid(1, 0) == 8\n\
    \        assert grid(2, 0) == 12\n\n    def test_memory_efficiency(self):\n  \
    \      \"\"\"Test that grid uses bit packing efficiently\"\"\"\n        grid =\
    \ Grid(4, 8, 0)\n        \n        # Check that packer is set up correctly\n \
    \       assert grid.pkr is not None\n        assert grid.W == 8\n        \n  \
    \      # Packer(8-1) has s=3, so each row has 1<<3=8 slots (exactly matches width)\n\
    \        row = grid[0]\n        assert len(row) == 8\n        \n        # The\
    \ packer should efficiently encode coordinates\n        for i in range(4):\n \
    \           for j in range(8):\n                # Set unique values to test encoding/decoding\n\
    \                value = i * 10 + j\n                grid.set(i, j, value)\n \
    \               assert grid(i, j) == value\n\n    def test_initialization_edge_cases(self):\n\
    \        \"\"\"Test edge cases in initialization\"\"\"\n        # Small flat list\
    \ (smaller than grid)\n        grid1 = Grid(2, 2, [42, 43, 44, 45])  # Provide\
    \ enough elements\n        # Should map flat list to grid\n        expected_values\
    \ = [42, 43, 44, 45]\n        for i in range(2):\n            for j in range(2):\n\
    \                assert grid1(i, j) == expected_values[i * 2 + j]\n        \n\
    \        # Mixed type initialization (though not typical usage)\n        grid2\
    \ = Grid(2, 2, [\n            [1, 2],\n            [3, 4]\n        ])\n      \
    \  \n        # Test that it works correctly\n        assert grid2(0, 0) == 1\n\
    \        assert grid2(1, 1) == 4\n\nfrom cp_library.ds.grid.grid_cls import Grid\n\
    \nif __name__ == '__main__':\n    from cp_library.test.unittest_helper import\
    \ run_verification_helper_unittest\n    run_verification_helper_unittest()"
  dependsOn:
  - cp_library/ds/grid/grid_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/io/parser_cls.py
  - cp_library/ds/view/view_cls.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: true
  path: test/unittests/ds/grid/grid_cls_test.py
  requiredBy: []
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/grid/grid_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/grid/grid_cls_test.py
- /verify/test/unittests/ds/grid/grid_cls_test.py.html
title: test/unittests/ds/grid/grid_cls_test.py
---
