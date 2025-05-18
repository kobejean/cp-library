---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_dec_fn.py
    title: cp_library/bit/pack/pack_dec_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/pack_sm_fn.py
    title: cp_library/bit/pack/pack_sm_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_frequency
    links:
    - https://judge.yosupo.jp/problem/static_range_frequency
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_frequency\n\
    \ndef main():\n    N, Q = map(int, input().split())\n    A = [int(s) for s in\
    \ input().split()]\n    R, V = coord_compress(A)\n    R.sort(); V.append(1 <<\
    \ 63)\n\n    def find(A, x):\n        l, r = 0, len(A)\n        while l < r:\n\
    \            if A[m := (l+r) >> 1] < x: l = m + 1\n            else: r = m\n \
    \       return l\n\n    for _ in range(Q):\n        l, r, x = input().split()\n\
    \        x = int(x)\n        if x == V[x:=find(V, x)]:\n            x <<= 19\n\
    \            append(str(find(R, x|int(r))-find(R, x|int(l)))); append('\\n')\n\
    \        else:\n            append('0\\n')\n    os.write(1, sb.build().encode())\n\
    '''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\n\n\ndef\
    \ pack_dec(ab: int, s: int, m: int): return ab>>s,ab&m\ndef pack_sm(N: int): s=N.bit_length();\
    \ return s,(1<<s)-1\ndef coord_compress(A: list[int]):\n    s, m = pack_sm((N\
    \ := len(A))-1)\n    R, V = [0]*N, [0]*N\n    for i,a in enumerate(A): A[i] =\
    \ a<<s|i\n    A.sort()\n    r = p = -1\n    for ai in A:\n        a, i = pack_dec(ai,\
    \ s, m)\n        if a != p: V[r:=r+1] = p = a\n        R[i] = r<<19|i\n    del\
    \ V[r+1:]\n    return R, V\n\nimport sys,os\nfrom __pypy__ import builders\nsb\
    \ = builders.StringBuilder()\nappend = sb.append\ndef input(): return sys.stdin.buffer.readline().strip()\n\
    \nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_frequency\n\
    \ndef main():\n    N, Q = map(int, input().split())\n    A = [int(s) for s in\
    \ input().split()]\n    R, V = coord_compress(A)\n    R.sort(); V.append(1 <<\
    \ 63)\n\n    def find(A, x):\n        l, r = 0, len(A)\n        while l < r:\n\
    \            if A[m := (l+r) >> 1] < x: l = m + 1\n            else: r = m\n \
    \       return l\n\n    for _ in range(Q):\n        l, r, x = input().split()\n\
    \        x = int(x)\n        if x == V[x:=find(V, x)]:\n            x <<= 19\n\
    \            append(str(find(R, x|int(r))-find(R, x|int(l)))); append('\\n')\n\
    \        else:\n            append('0\\n')\n    os.write(1, sb.build().encode())\n\
    from cp_library.bit.pack.pack_dec_fn import pack_dec\nfrom cp_library.bit.pack.pack_sm_fn\
    \ import pack_sm\ndef coord_compress(A: list[int]):\n    s, m = pack_sm((N :=\
    \ len(A))-1)\n    R, V = [0]*N, [0]*N\n    for i,a in enumerate(A): A[i] = a<<s|i\n\
    \    A.sort()\n    r = p = -1\n    for ai in A:\n        a, i = pack_dec(ai, s,\
    \ m)\n        if a != p: V[r:=r+1] = p = a\n        R[i] = r<<19|i\n    del V[r+1:]\n\
    \    return R, V\n\nimport sys,os\nfrom __pypy__ import builders\nsb = builders.StringBuilder()\n\
    append = sb.append\ndef input(): return sys.stdin.buffer.readline().strip()\n\n\
    if __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/bit/pack/pack_dec_fn.py
  - cp_library/bit/pack/pack_sm_fn.py
  isVerificationFile: true
  path: test/library-checker/data-structure/static_range_frequency.test.py
  requiredBy: []
  timestamp: '2025-05-19 01:45:33+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/static_range_frequency.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/static_range_frequency.test.py
- /verify/test/library-checker/data-structure/static_range_frequency.test.py.html
title: test/library-checker/data-structure/static_range_frequency.test.py
---
