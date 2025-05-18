---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    import os\nimport sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n\
    \    BUFSIZE = 8192\n    newlines = 0\n\n    def __init__(self, file):\n     \
    \   self._fd = file.fileno()\n        self.buffer = BytesIO()\n        self.writable\
    \ = \"x\" in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
    \ if self.writable else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n\
    \        while True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n            if not b:\n                break\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines = 0\n        return self.buffer.read()\n\n    def readline(self):\n\
    \        BUFSIZE = self.BUFSIZE\n        while self.newlines == 0:\n         \
    \   b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n        \
    \    self.newlines = b.count(b\"\\n\") + (not b)\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines -= 1\n        return self.buffer.readline()\n\n    def\
    \ flush(self):\n        if self.writable:\n            os.write(self._fd, self.buffer.getvalue())\n\
    \            self.buffer.truncate(0), self.buffer.seek(0)\n\n\nclass IOWrapper(IOBase):\n\
    \    stdin: 'IOWrapper' = None\n    stdout: 'IOWrapper' = None\n    \n    def\
    \ __init__(self, file):\n        self.buffer = FastIO(file)\n        self.flush\
    \ = self.buffer.flush\n        self.writable = self.buffer.writable\n\n    def\
    \ write(self, s):\n        return self.buffer.write(s.encode(\"ascii\"))\n   \
    \ \n    def read(self):\n        return self.buffer.read().decode(\"ascii\")\n\
    \    \n    def readline(self):\n        return self.buffer.readline().decode(\"\
    ascii\")\ntry:\n    sys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\n    sys.stdout\
    \ = IOWrapper.stdout = IOWrapper(sys.stdout)\nexcept:\n    pass\n\ndef write(*args,\
    \ **kwargs):\n    '''Prints the values to a stream, or to stdout_fast by default.'''\n\
    \    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n\
    \    at_start = True\n    for x in args:\n        if not at_start:\n         \
    \   file.write(sep)\n        file.write(str(x))\n        at_start = False\n  \
    \  file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\ndef bye(*args, **kwargs):\n    write(*args, **kwargs)\n\
    \    exit(0)\n"
  code: "import cp_library.io.__header__\nfrom cp_library.io.write_fn import write\n\
    \ndef bye(*args, **kwargs):\n    write(*args, **kwargs)\n    exit(0)"
  dependsOn:
  - cp_library/io/write_fn.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/io/bye_fn.py
  requiredBy: []
  timestamp: '2025-05-19 05:52:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/io/bye_fn.py
layout: document
redirect_from:
- /library/cp_library/io/bye_fn.py
- /library/cp_library/io/bye_fn.py.html
title: cp_library/io/bye_fn.py
---
