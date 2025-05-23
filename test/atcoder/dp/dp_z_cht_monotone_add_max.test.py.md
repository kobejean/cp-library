---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/cht_monotone_add_max_cls.py
    title: cp_library/ds/cht_monotone_add_max_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/dp/tasks/dp_z
    links:
    - https://atcoder.jp/contests/dp/tasks/dp_z
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_z\n\
    \ndef main():\n    N, C = read()\n    H = read()\n    dp = 0\n    cht = CHTMonotoneAddMax()\n\
    \n    for i in range(N-1):\n        m = 2*H[i]\n        b = -H[i]**2 + -dp\n \
    \       cht.insert(m,b)\n        i+=1\n        dp = -cht.max(H[i]) + H[i]**2 +\
    \ C\n\n    write(dp)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n             https://kobejean.github.io/cp-library       \
    \        \n'''\n\nfrom bisect import bisect_left\n\nclass CHTMonotoneAddMax:\n\
    \    def __init__(self):\n        self.hull = []\n\n    def insert(self, m: int,\
    \ b: int) -> None:\n        # Remove lines with greater or equal slopes (maintaining\
    \ monotonicity)\n        while self.hull and self.hull[-1][0] >= m:\n        \
    \    self.hull.pop()\n\n        def is_obsolete():\n            (m1, b1), (m2,\
    \ b2) = self.hull[-2], self.hull[-1]\n            return (b - b1) * (m1 - m2)\
    \ <= (b2 - b1) * (m1 - m)\n        \n        # Remove lines that are no longer\
    \ part of the lower envelope\n        while len(self.hull) >= 2 and is_obsolete():\n\
    \            self.hull.pop()\n        \n        self.hull.append((m, b))\n\n \
    \   def max(self, x: int) -> int:\n        def eval(i):\n            m, b = self.hull[i]\n\
    \            return m * x + b\n        def key(i):\n            m1, b1 = self.hull[i]\n\
    \            m2, b2 = self.hull[i+1]\n            return (m1-m2)*x + (b1-b2)\n\
    \        return eval(bisect_left(range(len(self.hull) - 1), 0, key=key))\n\n\n\
    def read(shift=0, base=10):\n    return [int(s, base) + shift for s in input().split()]\n\
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
    \        file.flush()\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_z\n\
    \ndef main():\n    N, C = read()\n    H = read()\n    dp = 0\n    cht = CHTMonotoneAddMax()\n\
    \n    for i in range(N-1):\n        m = 2*H[i]\n        b = -H[i]**2 + -dp\n \
    \       cht.insert(m,b)\n        i+=1\n        dp = -cht.max(H[i]) + H[i]**2 +\
    \ C\n\n    write(dp)\n\nfrom cp_library.ds.cht_monotone_add_max_cls import CHTMonotoneAddMax\n\
    from cp_library.io.read_int_fn import read\nfrom cp_library.io.write_fn import\
    \ write\n\nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/ds/cht_monotone_add_max_cls.py
  - cp_library/io/read_int_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/atcoder/dp/dp_z_cht_monotone_add_max.test.py
  requiredBy: []
  timestamp: '2025-05-23 18:57:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/dp/dp_z_cht_monotone_add_max.test.py
layout: document
redirect_from:
- /verify/test/atcoder/dp/dp_z_cht_monotone_add_max.test.py
- /verify/test/atcoder/dp/dp_z_cht_monotone_add_max.test.py.html
title: test/atcoder/dp/dp_z_cht_monotone_add_max.test.py
---
