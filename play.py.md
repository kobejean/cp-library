---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://en.algorithmica.org/hpc/arithmetic/division/
  bundledCode: "\nfrom random import randrange\nimport time\n\n'''\n\u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from\
    \ __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n       \
    \ return []\nelist = newlist_hint\n    \ndef lemire_precompute(d, bits=32): s\
    \ = bits<<1; m = (1<<s)-1; a = (m+d)//d; return a, s, m\ndef lemire_divmod(x,\
    \ d, a, s): q = (a*x)>>s; r = x-q*d; return q, r\ndef lemire_div(x, a, s): return\
    \ (a*x)>>s\ndef lemire_mod(x, d, a, s, m): return (((a*x)&m)*d) >> s\ndef lemire_divisibility(x,\
    \ a, m): return ((a*x)&m)<a\n\n# For a 21-bit divisor 63\nd = 63\na,s,m = lemire_precompute(d,\
    \ bits=15)\nprint(a, a.bit_length(), hex(a), s, hex(m))\n\n# for x in range(1\
    \ << 11): q = (0x1041042*x)>>30; r = x-q*63\n# for x in range(1 << 11): divmod(x,\
    \ d)\nt1 = time.perf_counter_ns()\nfor x in range(1 << 11): divmod(x, d)\nd1 =\
    \ time.perf_counter_ns()-t1\nt2 = time.perf_counter_ns()\nfor x in range(1 <<\
    \ 11): q = (0x1041042*x)>>30; r = x-q*63\nd2 = time.perf_counter_ns()-t2\n# t2\
    \ = time.perf_counter_ns()\n# for x in range(1 << 11): q = (0x1041042*x)>>30;\
    \ r = x-q*63\n# d2 += time.perf_counter_ns()-t2\n# t1 = time.perf_counter_ns()\n\
    # for x in range(1 << 11): divmod(x, d)\n# d1 += time.perf_counter_ns()-t1\n\n\
    print('divmod', d1, d2, d2/d1)\n\nfor x in range(1 << 18):\n    assert (x*a).bit_length()<64\n\
    \    assert divmod(x, d) == lemire_divmod(x,d,a,s), f'{x=} {divmod(x, d)=} {lemire_divmod(x,d,a,s)=}'\n\
    \    assert (x%d==0) == lemire_divisibility(x,a,m) \n    assert lemire_div(x,\
    \ a, s) == x//d\n    assert lemire_mod(x, d, a, s, m) == x%d\n\nI = [[randrange(0,i+1)\
    \ for i in range(1000)] for _ in range(10_000)]\n\ndef insert(i):\n    n = len(B)\n\
    \    b = (0x1041042*i)>>30\n    i=62-i+b*63\n    # b, i = divmod(i, 63)\n    #\
    \ i = 62-i\n    m = (1<<(i+1))-1\n    while b<(n:=n-1):B[n]=B[n]>>1|(B[n-1]&1)<<62\n\
    \    B[b]=B[b]&~m|1<<i|(B[b]&m)>>1\nBstart = time.perf_counter_ns()\nfor J in\
    \ I:\n    B = elist(2000)\n    N = -(0x1041042)\n    for i in J:\n        N =\
    \ (N+0x1041042)&0x3fffffff\n        # lemire divisibility check: https://en.algorithmica.org/hpc/arithmetic/division/\n\
    \        if N<0x1041042: B.append(0)\n        insert(i)\nBtime = time.perf_counter_ns()-Bstart\n\
    Astart = time.perf_counter_ns()\nfor J in I:\n    A = elist(2000)\n    for i in\
    \ J:\n        A.insert(i, i&1)\nAtime = time.perf_counter_ns()-Astart\nprint(Btime/Atime)\n\
    B.clear()\n\nB.append(0b111111111111111111111111111111111111111111111111111111111111101)\n\
    B.append(0b011111111111111111111111111111111111111111111111111111111111110)\n\
    print(f\"{B[0]:063b}\")\nprint(f\"{B[1]:063b}\")\nprint()\ninsert(63)\nprint(f\"\
    {B[0]:063b}\")\nprint(f\"{B[1]:063b}\")\nprint()\nB.append(0);insert(65)\nprint(f\"\
    {B[0]:063b}\")\nprint(f\"{B[1]:063b}\")\nprint(f\"{B[2]:063b}\")\n"
  code: "\nfrom random import randrange\nimport time\n\nfrom cp_library.ds.elist_fn\
    \ import elist\ndef lemire_precompute(d, bits=32): s = bits<<1; m = (1<<s)-1;\
    \ a = (m+d)//d; return a, s, m\ndef lemire_divmod(x, d, a, s): q = (a*x)>>s; r\
    \ = x-q*d; return q, r\ndef lemire_div(x, a, s): return (a*x)>>s\ndef lemire_mod(x,\
    \ d, a, s, m): return (((a*x)&m)*d) >> s\ndef lemire_divisibility(x, a, m): return\
    \ ((a*x)&m)<a\n\n# For a 21-bit divisor 63\nd = 63\na,s,m = lemire_precompute(d,\
    \ bits=15)\nprint(a, a.bit_length(), hex(a), s, hex(m))\n\n# for x in range(1\
    \ << 11): q = (0x1041042*x)>>30; r = x-q*63\n# for x in range(1 << 11): divmod(x,\
    \ d)\nt1 = time.perf_counter_ns()\nfor x in range(1 << 11): divmod(x, d)\nd1 =\
    \ time.perf_counter_ns()-t1\nt2 = time.perf_counter_ns()\nfor x in range(1 <<\
    \ 11): q = (0x1041042*x)>>30; r = x-q*63\nd2 = time.perf_counter_ns()-t2\n# t2\
    \ = time.perf_counter_ns()\n# for x in range(1 << 11): q = (0x1041042*x)>>30;\
    \ r = x-q*63\n# d2 += time.perf_counter_ns()-t2\n# t1 = time.perf_counter_ns()\n\
    # for x in range(1 << 11): divmod(x, d)\n# d1 += time.perf_counter_ns()-t1\n\n\
    print('divmod', d1, d2, d2/d1)\n\nfor x in range(1 << 18):\n    assert (x*a).bit_length()<64\n\
    \    assert divmod(x, d) == lemire_divmod(x,d,a,s), f'{x=} {divmod(x, d)=} {lemire_divmod(x,d,a,s)=}'\n\
    \    assert (x%d==0) == lemire_divisibility(x,a,m) \n    assert lemire_div(x,\
    \ a, s) == x//d\n    assert lemire_mod(x, d, a, s, m) == x%d\n\nI = [[randrange(0,i+1)\
    \ for i in range(1000)] for _ in range(10_000)]\n\ndef insert(i):\n    n = len(B)\n\
    \    b = (0x1041042*i)>>30\n    i=62-i+b*63\n    # b, i = divmod(i, 63)\n    #\
    \ i = 62-i\n    m = (1<<(i+1))-1\n    while b<(n:=n-1):B[n]=B[n]>>1|(B[n-1]&1)<<62\n\
    \    B[b]=B[b]&~m|1<<i|(B[b]&m)>>1\nBstart = time.perf_counter_ns()\nfor J in\
    \ I:\n    B = elist(2000)\n    N = -(0x1041042)\n    for i in J:\n        N =\
    \ (N+0x1041042)&0x3fffffff\n        # lemire divisibility check: https://en.algorithmica.org/hpc/arithmetic/division/\n\
    \        if N<0x1041042: B.append(0)\n        insert(i)\nBtime = time.perf_counter_ns()-Bstart\n\
    Astart = time.perf_counter_ns()\nfor J in I:\n    A = elist(2000)\n    for i in\
    \ J:\n        A.insert(i, i&1)\nAtime = time.perf_counter_ns()-Astart\nprint(Btime/Atime)\n\
    B.clear()\n\nB.append(0b111111111111111111111111111111111111111111111111111111111111101)\n\
    B.append(0b011111111111111111111111111111111111111111111111111111111111110)\n\
    print(f\"{B[0]:063b}\")\nprint(f\"{B[1]:063b}\")\nprint()\ninsert(63)\nprint(f\"\
    {B[0]:063b}\")\nprint(f\"{B[1]:063b}\")\nprint()\nB.append(0);insert(65)\nprint(f\"\
    {B[0]:063b}\")\nprint(f\"{B[1]:063b}\")\nprint(f\"{B[2]:063b}\")"
  dependsOn:
  - cp_library/ds/elist_fn.py
  isVerificationFile: false
  path: play.py
  requiredBy: []
  timestamp: '2025-05-20 13:05:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: play.py
layout: document
redirect_from:
- /library/play.py
- /library/play.py.html
title: play.py
---
