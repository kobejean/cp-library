---
data:
  _extendedDependsOn:
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
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/grid/grid_cls_test.py
    title: test/unittests/ds/grid/grid_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/bst/treap_monoid_cls_test.py
    title: test/unittests/ds/tree/bst/treap_monoid_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/csr2_cls_test.py
    title: test/unittests/ds/view/csr2_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/csr_cls_test.py
    title: test/unittests/ds/view/csr_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/view2_cls_test.py
    title: test/unittests/ds/view/view2_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/view_cls_test.py
    title: test/unittests/ds/view/view_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/wavelet/wm_static_cls_test.py
    title: test/unittests/ds/wavelet/wm_static_cls_test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\"\"\"\nHelper for making unittest files compatible with verification-helper.\n\
    \nThis module provides a helper function to run a dummy Library Checker test\n\
    so that unittest files can be verified by oj-verify.\n\"\"\"\n\ndef run_verification_helper_unittest():\n\
    \    \"\"\"\n    Run a dummy Library Checker test for verification-helper compatibility.\n\
    \    \n    This function should be called in the __main__ block of unittest files\n\
    \    that need to be compatible with verification-helper.\n    \n    The function:\n\
    \    1. Reads A and B from input\n    2. Writes A+B to output  \n    3. If the\
    \ result is the expected value (1198300249), runs pytest\n    4. Exits with the\
    \ pytest result code\n    \"\"\"\n    import sys\n    '''\n    \u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n                 https://kobejean.github.io/cp-library\
    \               \n    '''\n    \n    from typing import Type, Union, overload\n\
    \    '''\n    \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n                 https://kobejean.github.io/cp-library               \n\
    \    '''\n    import typing\n    from collections import deque\n    from numbers\
    \ import Number\n    from types import GenericAlias \n    from typing import Callable,\
    \ Collection, Iterator, Union\n    '''\n    \u257A\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2578\n                 https://kobejean.github.io/cp-library\
    \               \n    '''\n    import os\n    import sys\n    from io import BytesIO,\
    \ IOBase\n    \n    \n    class FastIO(IOBase):\n        BUFSIZE = 8192\n    \
    \    newlines = 0\n    \n        def __init__(self, file):\n            self._fd\
    \ = file.fileno()\n            self.buffer = BytesIO()\n            self.writable\
    \ = \"x\" in file.mode or \"r\" not in file.mode\n            self.write = self.buffer.write\
    \ if self.writable else None\n    \n        def read(self):\n            BUFSIZE\
    \ = self.BUFSIZE\n            while True:\n                b = os.read(self._fd,\
    \ max(os.fstat(self._fd).st_size, BUFSIZE))\n                if not b: break\n\
    \                ptr = self.buffer.tell()\n                self.buffer.seek(0,\
    \ 2), self.buffer.write(b), self.buffer.seek(ptr)\n            self.newlines =\
    \ 0\n            return self.buffer.read()\n    \n        def readline(self):\n\
    \            BUFSIZE = self.BUFSIZE\n            while self.newlines == 0:\n \
    \               b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n\
    \                self.newlines = b.count(b\"\\n\") + (not b)\n               \
    \ ptr = self.buffer.tell()\n                self.buffer.seek(0, 2), self.buffer.write(b),\
    \ self.buffer.seek(ptr)\n            self.newlines -= 1\n            return self.buffer.readline()\n\
    \    \n        def flush(self):\n            if self.writable:\n             \
    \   os.write(self._fd, self.buffer.getvalue())\n                self.buffer.truncate(0),\
    \ self.buffer.seek(0)\n    \n    \n    class IOWrapper(IOBase):\n        stdin:\
    \ 'IOWrapper' = None\n        stdout: 'IOWrapper' = None\n        \n        def\
    \ __init__(self, file):\n            self.buffer = FastIO(file)\n            self.flush\
    \ = self.buffer.flush\n            self.writable = self.buffer.writable\n    \n\
    \        def write(self, s):\n            return self.buffer.write(s.encode(\"\
    ascii\"))\n        \n        def read(self):\n            return self.buffer.read().decode(\"\
    ascii\")\n        \n        def readline(self):\n            return self.buffer.readline().decode(\"\
    ascii\")\n    try:\n        sys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\n\
    \        sys.stdout = IOWrapper.stdout = IOWrapper(sys.stdout)\n    except:\n\
    \        pass\n    from typing import TypeVar\n    _S = TypeVar('S')\n    _T =\
    \ TypeVar('T')\n    _U = TypeVar('U')\n    \n    class TokenStream(Iterator):\n\
    \        stream = IOWrapper.stdin\n    \n        def __init__(self):\n       \
    \     self.queue = deque()\n    \n        def __next__(self):\n            if\
    \ not self.queue: self.queue.extend(self._line())\n            return self.queue.popleft()\n\
    \        \n        def wait(self):\n            if not self.queue: self.queue.extend(self._line())\n\
    \            while self.queue: yield\n     \n        def _line(self):\n      \
    \      return TokenStream.stream.readline().split()\n    \n        def line(self):\n\
    \            if self.queue:\n                A = list(self.queue)\n          \
    \      self.queue.clear()\n                return A\n            return self._line()\n\
    \    TokenStream.default = TokenStream()\n    \n    class CharStream(TokenStream):\n\
    \        def _line(self):\n            return TokenStream.stream.readline().rstrip()\n\
    \    CharStream.default = CharStream()\n    \n    ParseFn = Callable[[TokenStream],_T]\n\
    \    class Parser:\n        def __init__(self, spec: Union[type[_T],_T]):\n  \
    \          self.parse = Parser.compile(spec)\n    \n        def __call__(self,\
    \ ts: TokenStream) -> _T:\n            return self.parse(ts)\n        \n     \
    \   @staticmethod\n        def compile_type(cls: type[_T], args = ()) -> _T:\n\
    \            if issubclass(cls, Parsable):\n                return cls.compile(*args)\n\
    \            elif issubclass(cls, (Number, str)):\n                def parse(ts:\
    \ TokenStream): return cls(next(ts))              \n                return parse\n\
    \            elif issubclass(cls, tuple):\n                return Parser.compile_tuple(cls,\
    \ args)\n            elif issubclass(cls, Collection):\n                return\
    \ Parser.compile_collection(cls, args)\n            elif callable(cls):\n    \
    \            def parse(ts: TokenStream):\n                    return cls(next(ts))\
    \              \n                return parse\n            else:\n           \
    \     raise NotImplementedError()\n        \n        @staticmethod\n        def\
    \ compile(spec: Union[type[_T],_T]=int) -> ParseFn[_T]:\n            if isinstance(spec,\
    \ (type, GenericAlias)):\n                cls = typing.get_origin(spec) or spec\n\
    \                args = typing.get_args(spec) or tuple()\n                return\
    \ Parser.compile_type(cls, args)\n            elif isinstance(offset := spec,\
    \ Number): \n                cls = type(spec)  \n                def parse(ts:\
    \ TokenStream): return cls(next(ts)) + offset\n                return parse\n\
    \            elif isinstance(args := spec, tuple):      \n                return\
    \ Parser.compile_tuple(type(spec), args)\n            elif isinstance(args :=\
    \ spec, Collection):\n                return Parser.compile_collection(type(spec),\
    \ args)\n            elif isinstance(fn := spec, Callable): \n               \
    \ def parse(ts: TokenStream): return fn(next(ts))\n                return parse\n\
    \            else:\n                raise NotImplementedError()\n    \n      \
    \  @staticmethod\n        def compile_line(cls: _T, spec=int) -> ParseFn[_T]:\n\
    \            if spec is int:\n                fn = Parser.compile(spec)\n    \
    \            def parse(ts: TokenStream): return cls([int(token) for token in ts.line()])\n\
    \                return parse\n            else:\n                fn = Parser.compile(spec)\n\
    \                def parse(ts: TokenStream): return cls([fn(ts) for _ in ts.wait()])\n\
    \                return parse\n    \n        @staticmethod\n        def compile_repeat(cls:\
    \ _T, spec, N) -> ParseFn[_T]:\n            fn = Parser.compile(spec)\n      \
    \      def parse(ts: TokenStream): return cls([fn(ts) for _ in range(N)])\n  \
    \          return parse\n    \n        @staticmethod\n        def compile_children(cls:\
    \ _T, specs) -> ParseFn[_T]:\n            fns = tuple((Parser.compile(spec) for\
    \ spec in specs))\n            def parse(ts: TokenStream): return cls([fn(ts)\
    \ for fn in fns])  \n            return parse\n                \n        @staticmethod\n\
    \        def compile_tuple(cls: type[_T], specs) -> ParseFn[_T]:\n           \
    \ if isinstance(specs, (tuple,list)) and len(specs) == 2 and specs[1] is ...:\n\
    \                return Parser.compile_line(cls, specs[0])\n            else:\n\
    \                return Parser.compile_children(cls, specs)\n    \n        @staticmethod\n\
    \        def compile_collection(cls, specs):\n            if not specs or len(specs)\
    \ == 1 or isinstance(specs, set):\n                return Parser.compile_line(cls,\
    \ *specs)\n            elif (isinstance(specs, (tuple,list)) and len(specs) ==\
    \ 2 and isinstance(specs[1], int)):\n                return Parser.compile_repeat(cls,\
    \ specs[0], specs[1])\n            else:\n                raise NotImplementedError()\n\
    \    \n    class Parsable:\n        @classmethod\n        def compile(cls):\n\
    \            def parser(ts: TokenStream): return cls(next(ts))\n            return\
    \ parser\n        \n        @classmethod\n        def __class_getitem__(cls, item):\n\
    \            return GenericAlias(cls, item)\n    from typing import TypeVar\n\
    \    _S = TypeVar('S')\n    _T = TypeVar('T')\n    _U = TypeVar('U')\n    \n \
    \   @overload\n    def read() -> list[int]: ...\n    @overload\n    def read(spec:\
    \ Type[_T], char=False) -> _T: ...\n    @overload\n    def read(spec: _U, char=False)\
    \ -> _U: ...\n    @overload\n    def read(*specs: Type[_T], char=False) -> tuple[_T,\
    \ ...]: ...\n    @overload\n    def read(*specs: _U, char=False) -> tuple[_U,\
    \ ...]: ...\n    def read(*specs: Union[Type[_T],_U], char=False):\n        if\
    \ not char and not specs: return [int(s) for s in TokenStream.default.line()]\n\
    \        parser: _T = Parser.compile(specs[0] if len(specs) == 1 else specs)\n\
    \        return parser(CharStream.default if char else TokenStream.default)\n\
    \    '''\n    \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n                 https://kobejean.github.io/cp-library               \n\
    \    '''\n    '''\n    \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n                 https://kobejean.github.io/cp-library         \
    \      \n    '''\n    import os\n    import sys\n    from io import BytesIO, IOBase\n\
    \    \n    \n    class FastIO(IOBase):\n        BUFSIZE = 8192\n        newlines\
    \ = 0\n    \n        def __init__(self, file):\n            self._fd = file.fileno()\n\
    \            self.buffer = BytesIO()\n            self.writable = \"x\" in file.mode\
    \ or \"r\" not in file.mode\n            self.write = self.buffer.write if self.writable\
    \ else None\n    \n        def read(self):\n            BUFSIZE = self.BUFSIZE\n\
    \            while True:\n                b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n                if not b: break\n                ptr = self.buffer.tell()\n\
    \                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \            self.newlines = 0\n            return self.buffer.read()\n    \n\
    \        def readline(self):\n            BUFSIZE = self.BUFSIZE\n           \
    \ while self.newlines == 0:\n                b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n                self.newlines = b.count(b\"\\n\") + (not b)\n   \
    \             ptr = self.buffer.tell()\n                self.buffer.seek(0, 2),\
    \ self.buffer.write(b), self.buffer.seek(ptr)\n            self.newlines -= 1\n\
    \            return self.buffer.readline()\n    \n        def flush(self):\n \
    \           if self.writable:\n                os.write(self._fd, self.buffer.getvalue())\n\
    \                self.buffer.truncate(0), self.buffer.seek(0)\n    \n    \n  \
    \  class IOWrapper(IOBase):\n        stdin: 'IOWrapper' = None\n        stdout:\
    \ 'IOWrapper' = None\n        \n        def __init__(self, file):\n          \
    \  self.buffer = FastIO(file)\n            self.flush = self.buffer.flush\n  \
    \          self.writable = self.buffer.writable\n    \n        def write(self,\
    \ s):\n            return self.buffer.write(s.encode(\"ascii\"))\n        \n \
    \       def read(self):\n            return self.buffer.read().decode(\"ascii\"\
    )\n        \n        def readline(self):\n            return self.buffer.readline().decode(\"\
    ascii\")\n    try:\n        sys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\n\
    \        sys.stdout = IOWrapper.stdout = IOWrapper(sys.stdout)\n    except:\n\
    \        pass\n    \n    def write(*args, **kwargs):\n        '''Prints the values\
    \ to a stream, or to stdout_fast by default.'''\n        sep, file = kwargs.pop(\"\
    sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n        at_start = True\n\
    \        for x in args:\n            if not at_start:\n                file.write(sep)\n\
    \            file.write(str(x))\n            at_start = False\n        file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n        if kwargs.pop(\"flush\", False):\n            file.flush()\n\
    \    \n    A, B = read()\n    write(C := A + B)\n    if C != 1198300249: \n  \
    \      sys.exit(0)\n    \n    import pytest\n    import io\n    from contextlib\
    \ import redirect_stdout, redirect_stderr\n\n    # Capture all output during test\
    \ execution\n    output = io.StringIO()\n    with redirect_stdout(output), redirect_stderr(output):\n\
    \        # Get the calling module's file path\n        frame = sys._getframe(1)\n\
    \        test_file = frame.f_globals.get('__file__')\n        if test_file is\
    \ None:\n            test_file = sys.argv[0]\n        result = pytest.main([test_file])\n\
    \    \n    if result != 0: \n        print(output.getvalue())\n    sys.exit(result)\n"
  code: "\"\"\"\nHelper for making unittest files compatible with verification-helper.\n\
    \nThis module provides a helper function to run a dummy Library Checker test\n\
    so that unittest files can be verified by oj-verify.\n\"\"\"\n\ndef run_verification_helper_unittest():\n\
    \    \"\"\"\n    Run a dummy Library Checker test for verification-helper compatibility.\n\
    \    \n    This function should be called in the __main__ block of unittest files\n\
    \    that need to be compatible with verification-helper.\n    \n    The function:\n\
    \    1. Reads A and B from input\n    2. Writes A+B to output  \n    3. If the\
    \ result is the expected value (1198300249), runs pytest\n    4. Exits with the\
    \ pytest result code\n    \"\"\"\n    import sys\n    from cp_library.io.read_fn\
    \ import read\n    from cp_library.io.write_fn import write\n    \n    A, B =\
    \ read()\n    write(C := A + B)\n    if C != 1198300249: \n        sys.exit(0)\n\
    \    \n    import pytest\n    import io\n    from contextlib import redirect_stdout,\
    \ redirect_stderr\n\n    # Capture all output during test execution\n    output\
    \ = io.StringIO()\n    with redirect_stdout(output), redirect_stderr(output):\n\
    \        # Get the calling module's file path\n        frame = sys._getframe(1)\n\
    \        test_file = frame.f_globals.get('__file__')\n        if test_file is\
    \ None:\n            test_file = sys.argv[0]\n        result = pytest.main([test_file])\n\
    \    \n    if result != 0: \n        print(output.getvalue())\n    sys.exit(result)"
  dependsOn:
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/test/unittest_helper.py
  requiredBy: []
  timestamp: '2025-07-11 23:11:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/unittests/ds/tree/bst/treap_monoid_cls_test.py
  - test/unittests/ds/view/csr_cls_test.py
  - test/unittests/ds/view/csr2_cls_test.py
  - test/unittests/ds/view/view_cls_test.py
  - test/unittests/ds/view/view2_cls_test.py
  - test/unittests/ds/grid/grid_cls_test.py
  - test/unittests/ds/wavelet/wm_static_cls_test.py
documentation_of: cp_library/test/unittest_helper.py
layout: document
redirect_from:
- /library/cp_library/test/unittest_helper.py
- /library/cp_library/test/unittest_helper.py.html
title: cp_library/test/unittest_helper.py
---
