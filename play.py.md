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
  bundledCode: '

    from __pypy__ import strategy

    A = [False]*10

    print(strategy(A))

    from array import array

    array(''b'', None)

    '
  code: '

    from __pypy__ import strategy

    A = [False]*10

    print(strategy(A))

    from array import array

    array(''b'', None)'
  dependsOn: []
  isVerificationFile: false
  path: play.py
  requiredBy: []
  timestamp: '2025-02-18 02:22:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: play.py
layout: document
redirect_from:
- /library/play.py
- /library/play.py.html
title: play.py
---
