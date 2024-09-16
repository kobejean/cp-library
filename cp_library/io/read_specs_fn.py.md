---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/subset_convolution.test.py
    title: test/subset_convolution.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\ndef read(*specs: tuple[type]):\n    S = input().split()\n    return\
    \ [func(s) for func, s in io_specs(specs, S)]\n\ndef io_specs(specs, S):\n   \
    \ def shift(shift):\n        return lambda s: int(s) + shift\n    def spec_func(spec):\n\
    \        return shift(spec) if isinstance(spec, int) else spec\n    if len(specs)\
    \ > 1:\n        return zip(map(spec_func, specs), S)\n    func = spec_func(specs[0]\
    \ if specs else int)\n    return ((func, s) for s in S)\n"
  code: "\ndef read(*specs: tuple[type]):\n    S = input().split()\n    return [func(s)\
    \ for func, s in io_specs(specs, S)]\n\ndef io_specs(specs, S):\n    def shift(shift):\n\
    \        return lambda s: int(s) + shift\n    def spec_func(spec):\n        return\
    \ shift(spec) if isinstance(spec, int) else spec\n    if len(specs) > 1:\n   \
    \     return zip(map(spec_func, specs), S)\n    func = spec_func(specs[0] if specs\
    \ else int)\n    return ((func, s) for s in S)\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/io/read_specs_fn.py
  requiredBy: []
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/subset_convolution.test.py
documentation_of: cp_library/io/read_specs_fn.py
layout: document
redirect_from:
- /library/cp_library/io/read_specs_fn.py
- /library/cp_library/io/read_specs_fn.py.html
title: cp_library/io/read_specs_fn.py
---
