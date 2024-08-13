---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/python/ds/potentialized_dsu.py
    title: cp_library/python/ds/potentialized_dsu.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind_with_potential
    links:
    - https://judge.yosupo.jp/problem/unionfind_with_potential
  bundledCode: "Traceback (most recent call last):\n  File \"/home/runner/.local/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/home/runner/.local/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential\n\
    \n# You must see with eyes unclouded by hate.  See the good in  \n# that which\
    \ is evil, and the evil in that which is good.     \n# Pledge yourself to neither\
    \ side, but vow instead to preserve\n# the balance that exists between the two.\
    \ - Hayao Miyazaki   \n# ------------------------------------------------------------\n\
    #                      Coded by: kobejean                     \n\nfrom cp_library.python.ds.potentialized_dsu\
    \ import PotentializedDSU\n\nmod = 998244353\n\ndef rint(shift=0, base=10):\n\
    \    return [int(x, base) + shift for x in input().split()]\n\nN, Q = rint()\n\
    \ndef op(x,y):\n    return (x+y)%mod\n\ndef inv(x):\n    return (-x)%mod\n\npdsu\
    \ = PotentializedDSU(op,inv,0,N)\n\nfor _ in range(Q):\n    t, *q = rint()\n \
    \   if t:\n        u, v = q\n        ans = pdsu.diff(u, v) if pdsu.same(u, v)\
    \ else -1\n        print(ans)\n    else:\n        u, v, x = q\n        print(int(pdsu.consistent(u,v,x)))\n\
    \        pdsu.merge(u, v, x)\n            "
  dependsOn:
  - cp_library/python/ds/potentialized_dsu.py
  isVerificationFile: true
  path: test/unionfind_with_potential.test.py
  requiredBy: []
  timestamp: '2024-08-13 18:31:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unionfind_with_potential.test.py
layout: document
redirect_from:
- /verify/test/unionfind_with_potential.test.py
- /verify/test/unionfind_with_potential.test.py.html
title: test/unionfind_with_potential.test.py
---
