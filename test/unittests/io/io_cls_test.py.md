---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_bytes_cls.py
    title: cp_library/io/io_bytes_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_cls.py
    title: cp_library/io/io_cls.py
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
    \nimport pytest\nimport io\n\nclass TestIOBytes:\n    def test_initialization(self):\n\
    \        \"\"\"Test basic initialization of IO class\"\"\"\n        buffer = io.BytesIO(b\"\
    test\\n\")\n        test_io = IOBytes(buffer)\n        \n        assert test_io.char\
    \ == False\n        assert test_io.l == 0\n        assert test_io.p == 0\n   \
    \     assert test_io.st == []\n        assert test_io.ist == []\n\n    def test_readtoken(self):\n\
    \        \"\"\"Test readtoken method\"\"\"\n        buffer = io.BytesIO(b\"hello\
    \ world test\\n\")\n        test_io = IOBytes(buffer)\n        \n        assert\
    \ test_io.readtoken() == \"hello\"\n        assert test_io.readtoken() == \"world\"\
    \n        assert test_io.readtoken() == \"test\"\n\n    def test_readtokens(self):\n\
    \        \"\"\"Test readtokens method\"\"\"\n        buffer = io.BytesIO(b\"hello\
    \ world test\\n\")\n        test_io = IOBytes(buffer)\n        \n        tokens\
    \ = test_io.readtokens()\n        assert tokens == [\"hello\", \"world\", \"test\"\
    ]\n\n    def test_readints(self):\n        \"\"\"Test readints method\"\"\"\n\
    \        buffer = io.BytesIO(b\"10 -20 300 -4000\\n\")\n        test_io = IOBytes(buffer)\n\
    \        \n        ints = test_io.readints()\n        assert ints == [10, -20,\
    \ 300, -4000]\n\n    def test_readints_single_line(self):\n        \"\"\"Test\
    \ readints with various integer formats\"\"\"\n        buffer = io.BytesIO(b\"\
    0 1 -1 42 -999 1000000\\n\")\n        test_io = IOBytes(buffer)\n        \n  \
    \      ints = test_io.readints()\n        assert ints == [0, 1, -1, 42, -999,\
    \ 1000000]\n\n    def test_readdigits_char_mode(self):\n        \"\"\"Test readdigits\
    \ method in char mode\"\"\"\n        buffer = io.BytesIO(b\"12345\\n\")\n    \
    \    test_io = IOBytes(buffer)\n        test_io.char = True\n        \n      \
    \  digits = test_io.readdigits()\n        assert digits == [1, 2, 3, 4, 5]\n\n\
    \    def test_readdigits_mixed_chars(self):\n        \"\"\"Test readdigits with\
    \ mixed characters\"\"\"\n        buffer = io.BytesIO(b\"1a2b3c\\n\")\n      \
    \  test_io = IOBytes(buffer)\n        test_io.char = True\n        \n        digits\
    \ = test_io.readdigits()\n        assert digits == [1, 2, 3]\n\n    def test_readnums_token_mode(self):\n\
    \        \"\"\"Test readnums in token mode (should use readints)\"\"\"\n     \
    \   buffer = io.BytesIO(b\"10 -20 300\\n\")\n        test_io = IOBytes(buffer)\n\
    \        test_io.char = False\n        \n        nums = test_io.readnums()\n \
    \       assert nums == [10, -20, 300]\n\n    def test_readnums_char_mode(self):\n\
    \        \"\"\"Test readnums in char mode (should use readdigits)\"\"\"\n    \
    \    buffer = io.BytesIO(b\"12345\\n\")\n        test_io = IOBytes(buffer)\n \
    \       test_io.char = True\n        \n        nums = test_io.readnums()\n   \
    \     assert nums == [1, 2, 3, 4, 5]\n\n    def test_readchar(self):\n       \
    \ \"\"\"Test readchar method\"\"\"\n        buffer = io.BytesIO(b\"abc\\n\")\n\
    \        test_io = IOBytes(buffer)\n        test_io.char = True\n        \n  \
    \      assert test_io.readchar() == \"a\"\n        assert test_io.readchar() ==\
    \ \"b\"\n        assert test_io.readchar() == \"c\"\n\n    def test_readchars(self):\n\
    \        \"\"\"Test readchars method\"\"\"\n        buffer = io.BytesIO(b\"hello\\\
    n\")\n        test_io = IOBytes(buffer)\n        test_io.char = True\n       \
    \ \n        chars = test_io.readchars()\n        assert chars == \"hello\"\n\n\
    \    def test_readline(self):\n        \"\"\"Test readline method\"\"\"\n    \
    \    buffer = io.BytesIO(b\"first line\\nsecond line\\n\")\n        test_io =\
    \ IOBytes(buffer)\n        \n        assert test_io.readline() == \"first line\\\
    n\"\n        assert test_io.readline() == \"second line\\n\"\n\n    def test_readinto_token_mode(self):\n\
    \        \"\"\"Test readinto in token mode\"\"\"\n        buffer = io.BytesIO(b\"\
    hello world\\n\")\n        test_io = IOBytes(buffer)\n        test_io.char = False\n\
    \        \n        lst = []\n        result = test_io.readinto(lst)\n        assert\
    \ result == [\"hello\", \"world\"]\n        assert lst == [\"hello\", \"world\"\
    ]\n\n    def test_readinto_char_mode(self):\n        \"\"\"Test readinto in char\
    \ mode\"\"\"\n        buffer = io.BytesIO(b\"hello\\n\")\n        test_io = IOBytes(buffer)\n\
    \        test_io.char = True\n        \n        lst = []\n        result = test_io.readinto(lst)\n\
    \        assert \"\".join(result) == \"hello\"\n        assert \"\".join(lst)\
    \ == \"hello\"\n        assert result == ['h', 'e', 'l', 'l', 'o']\n        assert\
    \ lst == ['h', 'e', 'l', 'l', 'o']\n\n    def test_readtokensinto(self):\n   \
    \     \"\"\"Test readtokensinto method\"\"\"\n        buffer = io.BytesIO(b\"\
    one two three\\n\")\n        test_io = IOBytes(buffer)\n        \n        lst\
    \ = [\"existing\"]\n        result = test_io.readtokensinto(lst)\n        assert\
    \ result == [\"existing\", \"one\", \"two\", \"three\"]\n        assert lst ==\
    \ [\"existing\", \"one\", \"two\", \"three\"]\n\n    def test_readintsinto(self):\n\
    \        \"\"\"Test readintsinto method\"\"\"\n        buffer = io.BytesIO(b\"\
    10 -20 30\\n\")\n        test_io = IOBytes(buffer)\n        \n        lst = [99]\n\
    \        result = test_io.readintsinto(lst)\n        assert result == [99, 10,\
    \ -20, 30]\n        assert lst == [99, 10, -20, 30]\n\n    def test_readdigitsinto(self):\n\
    \        \"\"\"Test readdigitsinto method\"\"\"\n        buffer = io.BytesIO(b\"\
    123a45\\n\")\n        test_io = IOBytes(buffer)\n        \n        lst = [9]\n\
    \        result = test_io.readdigitsinto(lst)\n        assert result == [9, 1,\
    \ 2, 3, 4, 5]\n        assert lst == [9, 1, 2, 3, 4, 5]\n\n    def test_readnumsinto_token_mode(self):\n\
    \        \"\"\"Test readnumsinto in token mode\"\"\"\n        buffer = io.BytesIO(b\"\
    10 -20 30\\n\")\n        test_io = IOBytes(buffer)\n        test_io.char = False\n\
    \        \n        lst = []\n        result = test_io.readnumsinto(lst)\n    \
    \    assert result == [10, -20, 30]\n        assert lst == [10, -20, 30]\n\n \
    \   def test_readnumsinto_char_mode(self):\n        \"\"\"Test readnumsinto in\
    \ char mode\"\"\"\n        buffer = io.BytesIO(b\"12345\\n\")\n        test_io\
    \ = IOBytes(buffer)\n        test_io.char = True\n        \n        lst = []\n\
    \        result = test_io.readnumsinto(lst)\n        assert result == [1, 2, 3,\
    \ 4, 5]\n        assert lst == [1, 2, 3, 4, 5]\n\n    def test_line_token_mode(self):\n\
    \        \"\"\"Test line method in token mode\"\"\"\n        buffer = io.BytesIO(b\"\
    hello world test\\n\")\n        test_io = IOBytes(buffer)\n        test_io.char\
    \ = False\n        \n        line_data = test_io.line()\n        assert line_data\
    \ == [\"hello\", \"world\", \"test\"]\n\n    def test_line_char_mode(self):\n\
    \        \"\"\"Test line method in char mode\"\"\"\n        buffer = io.BytesIO(b\"\
    hello\\n\")\n        test_io = IOBytes(buffer)\n        test_io.char = True\n\
    \        \n        line_data = test_io.line()\n        assert \"\".join(line_data)\
    \ == \"hello\"\n        assert line_data == ['h', 'e', 'l', 'l', 'o']\n      \
    \  assert len(line_data) == 5\n\n    def test_next_token_mode(self):\n       \
    \ \"\"\"Test __next__ method in token mode\"\"\"\n        buffer = io.BytesIO(b\"\
    hello world\\n\")\n        test_io = IOBytes(buffer)\n        test_io.char = False\n\
    \        \n        assert next(test_io) == \"hello\"\n        assert next(test_io)\
    \ == \"world\"\n\n    def test_next_char_mode(self):\n        \"\"\"Test __next__\
    \ method in char mode\"\"\"\n        buffer = io.BytesIO(b\"abc\\n\")\n      \
    \  test_io = IOBytes(buffer)\n        test_io.char = True\n        \n        assert\
    \ next(test_io) == \"a\"\n        assert next(test_io) == \"b\"\n        assert\
    \ next(test_io) == \"c\"\n\n    def test_multiline_tokens(self):\n        \"\"\
    \"Test reading tokens across multiple lines\"\"\"\n        buffer = io.BytesIO(b\"\
    line1 data\\nline2 more\\n\")\n        test_io = IOBytes(buffer)\n        \n \
    \       # First line\n        tokens1 = test_io.readtokens()\n        assert tokens1\
    \ == [\"line1\", \"data\"]\n        \n        # Second line\n        tokens2 =\
    \ test_io.readtokens()\n        assert tokens2 == [\"line2\", \"more\"]\n\n  \
    \  def test_multiline_ints(self):\n        \"\"\"Test reading integers across\
    \ multiple lines\"\"\"\n        buffer = io.BytesIO(b\"10 20\\n30 40\\n\")\n \
    \       test_io = IOBytes(buffer)\n        \n        # First line\n        ints1\
    \ = test_io.readints()\n        assert ints1 == [10, 20]\n        \n        #\
    \ Second line  \n        ints2 = test_io.readints()\n        assert ints2 == [30,\
    \ 40]\n\n    def test_empty_line(self):\n        \"\"\"Test handling empty lines\"\
    \"\"\n        buffer = io.BytesIO(b\"\\n\")\n        test_io = IOBytes(buffer)\n\
    \        \n        tokens = test_io.readtokens()\n        assert tokens == [\"\
    \"]\n\n    def test_single_integer(self):\n        \"\"\"Test reading single integer\"\
    \"\"\n        buffer = io.BytesIO(b\"42\\n\")\n        test_io = IOBytes(buffer)\n\
    \        \n        ints = test_io.readints()\n        assert ints == [42]\n\n\
    \    def test_single_digit(self):\n        \"\"\"Test reading single digit in\
    \ char mode\"\"\"\n        buffer = io.BytesIO(b\"7\\n\")\n        test_io = IOBytes(buffer)\n\
    \        test_io.char = True\n        \n        digits = test_io.readdigits()\n\
    \        assert digits == [7]\n\n    def test_zero_handling(self):\n        \"\
    \"\"Test proper handling of zero values\"\"\"\n        buffer = io.BytesIO(b\"\
    0 00 000\\n\")\n        test_io = IOBytes(buffer)\n        \n        ints = test_io.readints()\n\
    \        assert ints == [0, 0, 0]\n\n    def test_negative_zero(self):\n     \
    \   \"\"\"Test handling of negative zero\"\"\"\n        buffer = io.BytesIO(b\"\
    -0\\n\")\n        test_io = IOBytes(buffer)\n        \n        ints = test_io.readints()\n\
    \        assert ints == [0]\n\n    def test_large_numbers(self):\n        \"\"\
    \"Test handling of large numbers\"\"\"\n        buffer = io.BytesIO(b\"1000000000\
    \ -1000000000\\n\")\n        test_io = IOBytes(buffer)\n        \n        ints\
    \ = test_io.readints()\n        assert ints == [1000000000, -1000000000]\n\n \
    \   def test_digits_with_linebreak(self):\n        \"\"\"Test digits reading stops\
    \ at linebreak and advances line\"\"\"\n        buffer = io.BytesIO(b\"123\\n456\\\
    n\")\n        test_io = IOBytes(buffer)\n        test_io.char = True\n       \
    \ \n        # First line digits\n        digits1 = test_io.readdigits()\n    \
    \    assert digits1 == [1, 2, 3]\n        \n        # Second line digits \n  \
    \      digits2 = test_io.readdigits()\n        assert digits2 == [4, 5, 6]\n\n\
    \    def test_mixed_whitespace(self):\n        \"\"\"Test handling various whitespace\
    \ characters\"\"\"\n        buffer = io.BytesIO(b\"10  20   30\\n\")\n       \
    \ test_io = IOBytes(buffer)\n        \n        ints = test_io.readints()\n   \
    \     assert ints == [10, 20, 30]\n\n    def test_char_mode_individual_access(self):\n\
    \        \"\"\"Test individual character access in char mode\"\"\"\n        buffer\
    \ = io.BytesIO(b\"abc123\\n\")\n        test_io = IOBytes(buffer)\n        test_io.char\
    \ = True\n        \n        line_data = test_io.line()\n        assert line_data[0]\
    \ == 'a'\n        assert line_data[1] == 'b' \n        assert line_data[2] ==\
    \ 'c'\n        assert line_data[3] == '1'\n        assert line_data[4] == '2'\n\
    \        assert line_data[5] == '3'\n        assert len(line_data) == 6\n\n  \
    \  def test_char_mode_readcharsinto_individual(self):\n        \"\"\"Test readcharsinto\
    \ individual character behavior\"\"\"\n        buffer = io.BytesIO(b\"test\\n\"\
    )\n        test_io = IOBytes(buffer)\n        \n        lst = ['start']\n    \
    \    result = test_io.readcharsinto(lst)\n        # readcharsinto extends with\
    \ string characters\n        assert lst == ['start', 't', 'e', 's', 't']\n   \
    \     assert result == ['start', 't', 'e', 's', 't']\n\n'''\n\u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\nfrom __pypy__.builders import StringBuilder\n\nfrom os\
    \ import read as os_read, write as os_write, fstat as os_fstat\nimport sys\n\n\
    \ndef max2(a, b): return a if a > b else b\n\nclass IOBase:\n    @property\n \
    \   def char(io) -> bool: ...\n    @property\n    def writable(io) -> bool: ...\n\
    \    def __next__(io) -> str: ...\n    def write(io, s: str) -> None: ...\n  \
    \  def readline(io) -> str: ...\n    def readtoken(io) -> str: ...\n    def readtokens(io)\
    \ -> list[str]: ...\n    def readints(io) -> list[int]: ...\n    def readdigits(io)\
    \ -> list[int]: ...\n    def readnums(io) -> list[int]: ...\n    def readchar(io)\
    \ -> str: ...\n    def readchars(io) -> str: ...\n    def readinto(io, lst: list[str])\
    \ -> list[str]: ...\n    def readcharsinto(io, lst: list[str]) -> list[str]: ...\n\
    \    def readtokensinto(io, lst: list[str]) -> list[str]: ...\n    def readintsinto(io,\
    \ lst: list[int]) -> list[int]: ...\n    def readdigitsinto(io, lst: list[int])\
    \ -> list[int]: ...\n    def readnumsinto(io, lst: list[int]) -> list[int]: ...\n\
    \    def wait(io): ...\n    def flush(io) -> None: ...\n    def line(io) -> list[str]:\
    \ ...\n\nclass IO(IOBase):\n    BUFSIZE = 1 << 16; stdin: 'IO'; stdout: 'IO'\n\
    \    __slots__ = 'f', 'file', 'B', 'O', 'V', 'S', 'l', 'p', 'char', 'sz', 'st',\
    \ 'ist', 'writable', 'encoding', 'errors'\n    def __init__(io, file):\n     \
    \   io.file = file\n        try: io.f = file.fileno(); io.sz, io.writable = max2(io.BUFSIZE,\
    \ os_fstat(io.f).st_size), ('x' in file.mode or 'r' not in file.mode)\n      \
    \  except: io.f, io.sz, io.writable = -1, io.BUFSIZE, False\n        io.B, io.O,\
    \ io.S = bytearray(), [], StringBuilder(); io.V = memoryview(io.B); io.l = io.p\
    \ = 0\n        io.char, io.st, io.ist, io.encoding, io.errors = False, [], [],\
    \ 'ascii', 'ignore'\n    def _dec(io, l, r): return io.V[l:r].tobytes().decode(io.encoding,\
    \ io.errors)\n    def readbytes(io, sz): return os_read(io.f, sz)\n    def load(io):\n\
    \        while io.l >= len(io.O):\n            if not (b := io.readbytes(io.sz)):\n\
    \                if io.O[-1] < len(io.B): io.O.append(len(io.B))\n           \
    \     break\n            pos = len(io.B); io.B.extend(b)\n            while ~(pos\
    \ := io.B.find(b'\\n', pos)): io.O.append(pos := pos+1)\n    def __next__(io):\n\
    \        if io.char: return io.readchar()\n        else: return io.readtoken()\n\
    \    def readchar(io):\n        io.load(); r = io.O[io.l]\n        c = chr(io.B[io.p])\n\
    \        if io.p >= r-1: io.p = r; io.l += 1\n        else: io.p += 1\n      \
    \  return c\n    def write(io, s: str): io.S.append(s)\n    def readline(io):\
    \ io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return io._dec(l, io.p)\n\
    \    def readtoken(io):\n        io.load(); r = io.O[io.l]\n        if ~(p :=\
    \ io.B.find(b' ', io.p, r)): s = io._dec(io.p, p); io.p = p+1\n        else: s\
    \ = io._dec(io.p, r-1); io.p = r; io.l += 1\n        return s\n    def readtokens(io):\
    \ io.st.clear(); return io.readtokensinto(io.st)\n    def readints(io): io.ist.clear();\
    \ return io.readintsinto(io.ist)\n    def readdigits(io): io.ist.clear(); return\
    \ io.readdigitsinto(io.ist)\n    def readnums(io): io.ist.clear(); return io.readnumsinto(io.ist)\n\
    \    def readchars(io): io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return\
    \ io._dec(l, io.p-1)\n    def readinto(io, lst):\n        if io.char: return io.readcharsinto(lst)\n\
    \        else: return io.readtokensinto(lst)\n    def readcharsinto(io, lst):\
    \ lst.extend(io.readchars()); return lst\n    def readtokensinto(io, lst): \n\
    \        io.load(); r = io.O[io.l]\n        while ~(p := io.B.find(b' ', io.p,\
    \ r)): lst.append(io._dec(io.p, p)); io.p = p+1\n        lst.append(io._dec(io.p,\
    \ r-1)); io.p = r; io.l += 1; return lst\n    def readintsinto(io, lst):\n   \
    \     io.load(); r = io.O[io.l]\n        while io.p < r:\n            while io.p\
    \ < r and io.B[io.p] <= 32: io.p += 1\n            if io.p >= r: break\n     \
    \       minus = x = 0\n            if io.B[io.p] == 45: minus = 1; io.p += 1\n\
    \            while io.p < r and io.B[io.p] >= 48:\n                x = x * 10\
    \ + (io.B[io.p] & 15); io.p += 1\n            lst.append(-x if minus else x)\n\
    \            if io.p < r and io.B[io.p] == 32: io.p += 1\n        io.l += 1; return\
    \ lst\n    def readdigitsinto(io, lst):\n        io.load(); r = io.O[io.l]\n \
    \       while io.p < r and io.B[io.p] > 32:\n            if io.B[io.p] >= 48 and\
    \ io.B[io.p] <= 57:\n                lst.append(io.B[io.p] & 15)\n           \
    \ io.p += 1\n        if io.p < r and io.B[io.p] == 10: io.p = r; io.l += 1\n \
    \       return lst\n    def readnumsinto(io, lst):\n        if io.char: return\
    \ io.readdigitsinto(lst)\n        else: return io.readintsinto(lst)\n    def line(io):\
    \ io.st.clear(); return io.readinto(io.st)\n    def wait(io):\n        io.load();\
    \ r = io.O[io.l]\n        while io.p < r: yield\n    def flush(io):\n        if\
    \ io.writable: os_write(io.f, io.S.build().encode(io.encoding, io.errors)); io.S\
    \ = StringBuilder()\nsys.stdin = IO.stdin = IO(sys.stdin); sys.stdout = IO.stdout\
    \ = IO(sys.stdout)\n\nclass IOBytes(IO):\n    def __init__(io, file):\n      \
    \  io.file = file\n        io.f = -1\n        io.sz = io.BUFSIZE\n        io.B,\
    \ io.O, io.S = bytearray(), [], StringBuilder()\n        io.V = memoryview(io.B)\n\
    \        io.l = io.p = 0\n        io.char = False\n        io.st, io.ist = [],\
    \ []\n        io.writable, io.encoding, io.errors = True, 'ascii', 'ignore'\n\
    \    def readbytes(io, sz): return io.file.read(sz)\n\nif __name__ == '__main__':\n\
    \    \"\"\"\n    Helper for making unittest files compatible with verification-helper.\n\
    \    \n    This module provides a helper function to run a dummy Library Checker\
    \ test\n    so that unittest files can be verified by oj-verify.\n    \"\"\"\n\
    \    \n    def run_verification_helper_unittest():\n        \"\"\"\n        Run\
    \ a dummy AOJ ITP1_1_A test for verification-helper compatibility.\n        \n\
    \        This function should be called in the __main__ block of unittest files\n\
    \        that need to be compatible with verification-helper.\n        \n    \
    \    The function:\n        1. Prints \"Hello World\" (AOJ ITP1_1_A solution)\n\
    \        2. Runs pytest for the calling test file\n        3. Exits with the pytest\
    \ result code\n        \"\"\"\n        \n        # Print \"Hello World\" for AOJ\
    \ ITP1_1_A problem\n        print(\"Hello World\")\n        \n        from contextlib\
    \ import redirect_stdout, redirect_stderr\n    \n        # Capture all output\
    \ during test execution\n        output = io.StringIO()\n        with redirect_stdout(output),\
    \ redirect_stderr(output):\n            # Get the calling module's file path\n\
    \            frame = sys._getframe(1)\n            test_file = frame.f_globals.get('__file__')\n\
    \            if test_file is None:\n                test_file = sys.argv[0]\n\
    \            result = pytest.main([test_file])\n        \n        if result !=\
    \ 0: \n            print(output.getvalue())\n        sys.exit(result)\n    run_verification_helper_unittest()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    \nimport pytest\nimport io\n\nclass TestIOBytes:\n    def test_initialization(self):\n\
    \        \"\"\"Test basic initialization of IO class\"\"\"\n        buffer = io.BytesIO(b\"\
    test\\n\")\n        test_io = IOBytes(buffer)\n        \n        assert test_io.char\
    \ == False\n        assert test_io.l == 0\n        assert test_io.p == 0\n   \
    \     assert test_io.st == []\n        assert test_io.ist == []\n\n    def test_readtoken(self):\n\
    \        \"\"\"Test readtoken method\"\"\"\n        buffer = io.BytesIO(b\"hello\
    \ world test\\n\")\n        test_io = IOBytes(buffer)\n        \n        assert\
    \ test_io.readtoken() == \"hello\"\n        assert test_io.readtoken() == \"world\"\
    \n        assert test_io.readtoken() == \"test\"\n\n    def test_readtokens(self):\n\
    \        \"\"\"Test readtokens method\"\"\"\n        buffer = io.BytesIO(b\"hello\
    \ world test\\n\")\n        test_io = IOBytes(buffer)\n        \n        tokens\
    \ = test_io.readtokens()\n        assert tokens == [\"hello\", \"world\", \"test\"\
    ]\n\n    def test_readints(self):\n        \"\"\"Test readints method\"\"\"\n\
    \        buffer = io.BytesIO(b\"10 -20 300 -4000\\n\")\n        test_io = IOBytes(buffer)\n\
    \        \n        ints = test_io.readints()\n        assert ints == [10, -20,\
    \ 300, -4000]\n\n    def test_readints_single_line(self):\n        \"\"\"Test\
    \ readints with various integer formats\"\"\"\n        buffer = io.BytesIO(b\"\
    0 1 -1 42 -999 1000000\\n\")\n        test_io = IOBytes(buffer)\n        \n  \
    \      ints = test_io.readints()\n        assert ints == [0, 1, -1, 42, -999,\
    \ 1000000]\n\n    def test_readdigits_char_mode(self):\n        \"\"\"Test readdigits\
    \ method in char mode\"\"\"\n        buffer = io.BytesIO(b\"12345\\n\")\n    \
    \    test_io = IOBytes(buffer)\n        test_io.char = True\n        \n      \
    \  digits = test_io.readdigits()\n        assert digits == [1, 2, 3, 4, 5]\n\n\
    \    def test_readdigits_mixed_chars(self):\n        \"\"\"Test readdigits with\
    \ mixed characters\"\"\"\n        buffer = io.BytesIO(b\"1a2b3c\\n\")\n      \
    \  test_io = IOBytes(buffer)\n        test_io.char = True\n        \n        digits\
    \ = test_io.readdigits()\n        assert digits == [1, 2, 3]\n\n    def test_readnums_token_mode(self):\n\
    \        \"\"\"Test readnums in token mode (should use readints)\"\"\"\n     \
    \   buffer = io.BytesIO(b\"10 -20 300\\n\")\n        test_io = IOBytes(buffer)\n\
    \        test_io.char = False\n        \n        nums = test_io.readnums()\n \
    \       assert nums == [10, -20, 300]\n\n    def test_readnums_char_mode(self):\n\
    \        \"\"\"Test readnums in char mode (should use readdigits)\"\"\"\n    \
    \    buffer = io.BytesIO(b\"12345\\n\")\n        test_io = IOBytes(buffer)\n \
    \       test_io.char = True\n        \n        nums = test_io.readnums()\n   \
    \     assert nums == [1, 2, 3, 4, 5]\n\n    def test_readchar(self):\n       \
    \ \"\"\"Test readchar method\"\"\"\n        buffer = io.BytesIO(b\"abc\\n\")\n\
    \        test_io = IOBytes(buffer)\n        test_io.char = True\n        \n  \
    \      assert test_io.readchar() == \"a\"\n        assert test_io.readchar() ==\
    \ \"b\"\n        assert test_io.readchar() == \"c\"\n\n    def test_readchars(self):\n\
    \        \"\"\"Test readchars method\"\"\"\n        buffer = io.BytesIO(b\"hello\\\
    n\")\n        test_io = IOBytes(buffer)\n        test_io.char = True\n       \
    \ \n        chars = test_io.readchars()\n        assert chars == \"hello\"\n\n\
    \    def test_readline(self):\n        \"\"\"Test readline method\"\"\"\n    \
    \    buffer = io.BytesIO(b\"first line\\nsecond line\\n\")\n        test_io =\
    \ IOBytes(buffer)\n        \n        assert test_io.readline() == \"first line\\\
    n\"\n        assert test_io.readline() == \"second line\\n\"\n\n    def test_readinto_token_mode(self):\n\
    \        \"\"\"Test readinto in token mode\"\"\"\n        buffer = io.BytesIO(b\"\
    hello world\\n\")\n        test_io = IOBytes(buffer)\n        test_io.char = False\n\
    \        \n        lst = []\n        result = test_io.readinto(lst)\n        assert\
    \ result == [\"hello\", \"world\"]\n        assert lst == [\"hello\", \"world\"\
    ]\n\n    def test_readinto_char_mode(self):\n        \"\"\"Test readinto in char\
    \ mode\"\"\"\n        buffer = io.BytesIO(b\"hello\\n\")\n        test_io = IOBytes(buffer)\n\
    \        test_io.char = True\n        \n        lst = []\n        result = test_io.readinto(lst)\n\
    \        assert \"\".join(result) == \"hello\"\n        assert \"\".join(lst)\
    \ == \"hello\"\n        assert result == ['h', 'e', 'l', 'l', 'o']\n        assert\
    \ lst == ['h', 'e', 'l', 'l', 'o']\n\n    def test_readtokensinto(self):\n   \
    \     \"\"\"Test readtokensinto method\"\"\"\n        buffer = io.BytesIO(b\"\
    one two three\\n\")\n        test_io = IOBytes(buffer)\n        \n        lst\
    \ = [\"existing\"]\n        result = test_io.readtokensinto(lst)\n        assert\
    \ result == [\"existing\", \"one\", \"two\", \"three\"]\n        assert lst ==\
    \ [\"existing\", \"one\", \"two\", \"three\"]\n\n    def test_readintsinto(self):\n\
    \        \"\"\"Test readintsinto method\"\"\"\n        buffer = io.BytesIO(b\"\
    10 -20 30\\n\")\n        test_io = IOBytes(buffer)\n        \n        lst = [99]\n\
    \        result = test_io.readintsinto(lst)\n        assert result == [99, 10,\
    \ -20, 30]\n        assert lst == [99, 10, -20, 30]\n\n    def test_readdigitsinto(self):\n\
    \        \"\"\"Test readdigitsinto method\"\"\"\n        buffer = io.BytesIO(b\"\
    123a45\\n\")\n        test_io = IOBytes(buffer)\n        \n        lst = [9]\n\
    \        result = test_io.readdigitsinto(lst)\n        assert result == [9, 1,\
    \ 2, 3, 4, 5]\n        assert lst == [9, 1, 2, 3, 4, 5]\n\n    def test_readnumsinto_token_mode(self):\n\
    \        \"\"\"Test readnumsinto in token mode\"\"\"\n        buffer = io.BytesIO(b\"\
    10 -20 30\\n\")\n        test_io = IOBytes(buffer)\n        test_io.char = False\n\
    \        \n        lst = []\n        result = test_io.readnumsinto(lst)\n    \
    \    assert result == [10, -20, 30]\n        assert lst == [10, -20, 30]\n\n \
    \   def test_readnumsinto_char_mode(self):\n        \"\"\"Test readnumsinto in\
    \ char mode\"\"\"\n        buffer = io.BytesIO(b\"12345\\n\")\n        test_io\
    \ = IOBytes(buffer)\n        test_io.char = True\n        \n        lst = []\n\
    \        result = test_io.readnumsinto(lst)\n        assert result == [1, 2, 3,\
    \ 4, 5]\n        assert lst == [1, 2, 3, 4, 5]\n\n    def test_line_token_mode(self):\n\
    \        \"\"\"Test line method in token mode\"\"\"\n        buffer = io.BytesIO(b\"\
    hello world test\\n\")\n        test_io = IOBytes(buffer)\n        test_io.char\
    \ = False\n        \n        line_data = test_io.line()\n        assert line_data\
    \ == [\"hello\", \"world\", \"test\"]\n\n    def test_line_char_mode(self):\n\
    \        \"\"\"Test line method in char mode\"\"\"\n        buffer = io.BytesIO(b\"\
    hello\\n\")\n        test_io = IOBytes(buffer)\n        test_io.char = True\n\
    \        \n        line_data = test_io.line()\n        assert \"\".join(line_data)\
    \ == \"hello\"\n        assert line_data == ['h', 'e', 'l', 'l', 'o']\n      \
    \  assert len(line_data) == 5\n\n    def test_next_token_mode(self):\n       \
    \ \"\"\"Test __next__ method in token mode\"\"\"\n        buffer = io.BytesIO(b\"\
    hello world\\n\")\n        test_io = IOBytes(buffer)\n        test_io.char = False\n\
    \        \n        assert next(test_io) == \"hello\"\n        assert next(test_io)\
    \ == \"world\"\n\n    def test_next_char_mode(self):\n        \"\"\"Test __next__\
    \ method in char mode\"\"\"\n        buffer = io.BytesIO(b\"abc\\n\")\n      \
    \  test_io = IOBytes(buffer)\n        test_io.char = True\n        \n        assert\
    \ next(test_io) == \"a\"\n        assert next(test_io) == \"b\"\n        assert\
    \ next(test_io) == \"c\"\n\n    def test_multiline_tokens(self):\n        \"\"\
    \"Test reading tokens across multiple lines\"\"\"\n        buffer = io.BytesIO(b\"\
    line1 data\\nline2 more\\n\")\n        test_io = IOBytes(buffer)\n        \n \
    \       # First line\n        tokens1 = test_io.readtokens()\n        assert tokens1\
    \ == [\"line1\", \"data\"]\n        \n        # Second line\n        tokens2 =\
    \ test_io.readtokens()\n        assert tokens2 == [\"line2\", \"more\"]\n\n  \
    \  def test_multiline_ints(self):\n        \"\"\"Test reading integers across\
    \ multiple lines\"\"\"\n        buffer = io.BytesIO(b\"10 20\\n30 40\\n\")\n \
    \       test_io = IOBytes(buffer)\n        \n        # First line\n        ints1\
    \ = test_io.readints()\n        assert ints1 == [10, 20]\n        \n        #\
    \ Second line  \n        ints2 = test_io.readints()\n        assert ints2 == [30,\
    \ 40]\n\n    def test_empty_line(self):\n        \"\"\"Test handling empty lines\"\
    \"\"\n        buffer = io.BytesIO(b\"\\n\")\n        test_io = IOBytes(buffer)\n\
    \        \n        tokens = test_io.readtokens()\n        assert tokens == [\"\
    \"]\n\n    def test_single_integer(self):\n        \"\"\"Test reading single integer\"\
    \"\"\n        buffer = io.BytesIO(b\"42\\n\")\n        test_io = IOBytes(buffer)\n\
    \        \n        ints = test_io.readints()\n        assert ints == [42]\n\n\
    \    def test_single_digit(self):\n        \"\"\"Test reading single digit in\
    \ char mode\"\"\"\n        buffer = io.BytesIO(b\"7\\n\")\n        test_io = IOBytes(buffer)\n\
    \        test_io.char = True\n        \n        digits = test_io.readdigits()\n\
    \        assert digits == [7]\n\n    def test_zero_handling(self):\n        \"\
    \"\"Test proper handling of zero values\"\"\"\n        buffer = io.BytesIO(b\"\
    0 00 000\\n\")\n        test_io = IOBytes(buffer)\n        \n        ints = test_io.readints()\n\
    \        assert ints == [0, 0, 0]\n\n    def test_negative_zero(self):\n     \
    \   \"\"\"Test handling of negative zero\"\"\"\n        buffer = io.BytesIO(b\"\
    -0\\n\")\n        test_io = IOBytes(buffer)\n        \n        ints = test_io.readints()\n\
    \        assert ints == [0]\n\n    def test_large_numbers(self):\n        \"\"\
    \"Test handling of large numbers\"\"\"\n        buffer = io.BytesIO(b\"1000000000\
    \ -1000000000\\n\")\n        test_io = IOBytes(buffer)\n        \n        ints\
    \ = test_io.readints()\n        assert ints == [1000000000, -1000000000]\n\n \
    \   def test_digits_with_linebreak(self):\n        \"\"\"Test digits reading stops\
    \ at linebreak and advances line\"\"\"\n        buffer = io.BytesIO(b\"123\\n456\\\
    n\")\n        test_io = IOBytes(buffer)\n        test_io.char = True\n       \
    \ \n        # First line digits\n        digits1 = test_io.readdigits()\n    \
    \    assert digits1 == [1, 2, 3]\n        \n        # Second line digits \n  \
    \      digits2 = test_io.readdigits()\n        assert digits2 == [4, 5, 6]\n\n\
    \    def test_mixed_whitespace(self):\n        \"\"\"Test handling various whitespace\
    \ characters\"\"\"\n        buffer = io.BytesIO(b\"10  20   30\\n\")\n       \
    \ test_io = IOBytes(buffer)\n        \n        ints = test_io.readints()\n   \
    \     assert ints == [10, 20, 30]\n\n    def test_char_mode_individual_access(self):\n\
    \        \"\"\"Test individual character access in char mode\"\"\"\n        buffer\
    \ = io.BytesIO(b\"abc123\\n\")\n        test_io = IOBytes(buffer)\n        test_io.char\
    \ = True\n        \n        line_data = test_io.line()\n        assert line_data[0]\
    \ == 'a'\n        assert line_data[1] == 'b' \n        assert line_data[2] ==\
    \ 'c'\n        assert line_data[3] == '1'\n        assert line_data[4] == '2'\n\
    \        assert line_data[5] == '3'\n        assert len(line_data) == 6\n\n  \
    \  def test_char_mode_readcharsinto_individual(self):\n        \"\"\"Test readcharsinto\
    \ individual character behavior\"\"\"\n        buffer = io.BytesIO(b\"test\\n\"\
    )\n        test_io = IOBytes(buffer)\n        \n        lst = ['start']\n    \
    \    result = test_io.readcharsinto(lst)\n        # readcharsinto extends with\
    \ string characters\n        assert lst == ['start', 't', 'e', 's', 't']\n   \
    \     assert result == ['start', 't', 'e', 's', 't']\n\nfrom cp_library.io.io_bytes_cls\
    \ import IOBytes\n\nif __name__ == '__main__':\n    from cp_library.test.unittest_helper\
    \ import run_verification_helper_unittest\n    run_verification_helper_unittest()"
  dependsOn:
  - cp_library/io/io_bytes_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/io/io_cls.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/io/io_base_cls.py
  isVerificationFile: true
  path: test/unittests/io/io_cls_test.py
  requiredBy: []
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/io/io_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/io/io_cls_test.py
- /verify/test/unittests/io/io_cls_test.py.html
title: test/unittests/io/io_cls_test.py
---
