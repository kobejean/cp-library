---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/partition_fn.py
    title: cp_library/alg/divcon/partition_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/qselect_fn.py
    title: cp_library/alg/divcon/qselect_fn.py
  - icon: ':question:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  - icon: ':question:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/arc182/tasks/arc182_d
    links:
    - https://atcoder.jp/contests/arc182/tasks/arc182_d
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc182/tasks/arc182_d\n\
    \ndef main():\n    N, M = read()\n    A = read()\n    B = read()\n\n    if M ==\
    \ 2:\n        write(0 if A == B else -1)\n        exit()\n\n    def rel(x,y):\n\
    \        return max(-1,min(x-y,1))\n\n    C = [B[0]]\n\n    for i in range(1,N):\n\
    \        c = C[-1] - C[-1]%M + B[i]\n        for Ci in range(c-M,c+2*M,M):\n \
    \           if rel(A[i-1],A[i]) == rel(C[-1],Ci) and abs(C[-1]-Ci)<M:\n      \
    \          C.append(Ci)\n                break\n    median = qselect([c-a for\
    \ a,c in zip(A,C)], N//2)\n    ans = inf\n    for i in range(median//M,median//M+2):\n\
    \        now=0\n        for j in range(N):\n            now+=abs(A[j]+i*M-C[j])\n\
    \        ans=min(ans,now)\n    write(ans)\n\nfrom math import inf\n'''\n\u257A\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n         \
    \    https://kobejean.github.io/cp-library               \n'''\nfrom random import\
    \ randint\n\ndef partition(A, l, r, p) -> int:\n    '''Partition subarray [l,r)'''\n\
    \    A[p], A[r], p = A[r := r-1], A[p], l\n    for j in range(l, r):\n       \
    \ if A[j] <= A[r]: A[p], A[j], p = A[j], A[p], p+1\n    A[p], A[r] = A[r], A[p]\n\
    \    return p\n\ndef qselect(A, k, l=0, r=None):\n    '''Find kth element in subarray\
    \ [l,r)'''\n    if r is None: r = len(A)\n    while l != r-1:\n        if k <\
    \ (p := partition(A, l, r, randint(l,r-1))): r = p\n        elif k > p: l = p+1\n\
    \        else: return A[k]\n    return A[k]\n\n\ndef read(shift=0, base=10):\n\
    \    return [int(s, base) + shift for s in input().split()]\nimport os\nimport\
    \ sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE\
    \ = 8192\n    newlines = 0\n\n    def __init__(self, file):\n        self._fd\
    \ = file.fileno()\n        self.buffer = BytesIO()\n        self.writable = \"\
    x\" in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
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
    ascii\")\n\nsys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\nsys.stdout = IOWrapper.stdout\
    \ = IOWrapper(sys.stdout)\n\ndef write(*args, **kwargs):\n    '''Prints the values\
    \ to a stream, or to stdout_fast by default.'''\n    sep, file = kwargs.pop(\"\
    sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n    at_start = True\n \
    \   for x in args:\n        if not at_start:\n            file.write(sep)\n  \
    \      file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    \    \nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc182/tasks/arc182_d\n\
    \ndef main():\n    N, M = read()\n    A = read()\n    B = read()\n\n    if M ==\
    \ 2:\n        write(0 if A == B else -1)\n        exit()\n\n    def rel(x,y):\n\
    \        return max(-1,min(x-y,1))\n\n    C = [B[0]]\n\n    for i in range(1,N):\n\
    \        c = C[-1] - C[-1]%M + B[i]\n        for Ci in range(c-M,c+2*M,M):\n \
    \           if rel(A[i-1],A[i]) == rel(C[-1],Ci) and abs(C[-1]-Ci)<M:\n      \
    \          C.append(Ci)\n                break\n    median = qselect([c-a for\
    \ a,c in zip(A,C)], N//2)\n    ans = inf\n    for i in range(median//M,median//M+2):\n\
    \        now=0\n        for j in range(N):\n            now+=abs(A[j]+i*M-C[j])\n\
    \        ans=min(ans,now)\n    write(ans)\n\nfrom math import inf\nfrom cp_library.alg.divcon.qselect_fn\
    \ import qselect\nfrom cp_library.io.read_int_fn import read\nfrom cp_library.io.write_fn\
    \ import write\n    \nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/alg/divcon/qselect_fn.py
  - cp_library/io/read_int_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/divcon/partition_fn.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/atcoder/arc/arc182_d_increment_decrement_again_qselect.test.py
  requiredBy: []
  timestamp: '2025-03-28 19:21:24+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/arc/arc182_d_increment_decrement_again_qselect.test.py
layout: document
redirect_from:
- /verify/test/atcoder/arc/arc182_d_increment_decrement_again_qselect.test.py
- /verify/test/atcoder/arc/arc182_d_increment_decrement_again_qselect.test.py.html
title: test/atcoder/arc/arc182_d_increment_decrement_again_qselect.test.py
---
