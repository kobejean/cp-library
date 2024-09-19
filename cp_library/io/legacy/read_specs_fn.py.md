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
    \nimport sys\nfrom typing import Type, TypeVar\n\nT = TypeVar('T')\ndef read(spec:\
    \ Type[T]|T=[int]) -> T:\n    return parse_stream(sys.stdin, spec)\n\nfrom cp_library.io.old.parse_stream_fn\
    \ import parse_stream\n"
  code: "import cp_library.io.__init__\n\nimport sys\nfrom typing import Type, TypeVar\n\
    \nT = TypeVar('T')\ndef read(spec: Type[T]|T=[int]) -> T:\n    return parse_stream(sys.stdin,\
    \ spec)\n\nfrom cp_library.io.old.parse_stream_fn import parse_stream"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/io/legacy/read_specs_fn.py
  requiredBy: []
  timestamp: '2024-09-20 03:21:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/io/legacy/read_specs_fn.py
layout: document
redirect_from:
- /library/cp_library/io/legacy/read_specs_fn.py
- /library/cp_library/io/legacy/read_specs_fn.py.html
title: cp_library/io/legacy/read_specs_fn.py
---
