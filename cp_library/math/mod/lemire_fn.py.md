---
data:
  _extendedDependsOn: []
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
    \n\ndef lemire_precompute(d,bits=32):s=bits<<1;m=(1<<s)-1;a=(m+d)//d;return a,s,m\n\
    def lemire_divmod(x,d,a,s):q=(a*x)>>s;r=x-q*d;return q,r\ndef lemire_div(x,a,s):return(a*x)>>s\n\
    def lemire_mod(x,d,a,s,m):return(((a*x)&m)*d)>>s\ndef lemire_divisibility(x,a,m):return((a*x)&m)<a\n"
  code: 'import cp_library.__header__

    import cp_library.math.__header__

    import cp_library.math.mod.__header__

    def lemire_precompute(d,bits=32):s=bits<<1;m=(1<<s)-1;a=(m+d)//d;return a,s,m

    def lemire_divmod(x,d,a,s):q=(a*x)>>s;r=x-q*d;return q,r

    def lemire_div(x,a,s):return(a*x)>>s

    def lemire_mod(x,d,a,s,m):return(((a*x)&m)*d)>>s

    def lemire_divisibility(x,a,m):return((a*x)&m)<a'
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mod/lemire_fn.py
  requiredBy: []
  timestamp: '2025-05-23 09:29:26+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/mod/lemire_fn.py
layout: document
redirect_from:
- /library/cp_library/math/mod/lemire_fn.py
- /library/cp_library/math/mod/lemire_fn.py.html
title: cp_library/math/mod/lemire_fn.py
---
