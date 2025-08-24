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
  bundledCode: 'from __pypy__ import bytebuffer, newlist_hint, list_get_physical_size,
    resizelist_hint

    import gc

    gc.disable()


    # A = newlist_hint(1000000000_0000)

    A = newlist_hint(1000000000_00)

    for _ in range(1000000000): A.append(100)

    print(list_get_physical_size(A))

    A.pop()

    print(list_get_physical_size(A))

    A.append(100)

    print(list_get_physical_size(A))

    '
  code: 'from __pypy__ import bytebuffer, newlist_hint, list_get_physical_size, resizelist_hint

    import gc

    gc.disable()


    # A = newlist_hint(1000000000_0000)

    A = newlist_hint(1000000000_00)

    for _ in range(1000000000): A.append(100)

    print(list_get_physical_size(A))

    A.pop()

    print(list_get_physical_size(A))

    A.append(100)

    print(list_get_physical_size(A))

    '
  dependsOn: []
  isVerificationFile: false
  path: play.py
  requiredBy: []
  timestamp: '2025-08-24 20:27:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: play.py
layout: document
redirect_from:
- /library/play.py
- /library/play.py.html
title: play.py
---
