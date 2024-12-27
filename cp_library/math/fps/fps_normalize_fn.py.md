---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_pow_fn.py
    title: cp_library/math/fps/fps_pow_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling1_k_fn.py
    title: cp_library/math/table/stirling1_k_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling2_k_fn.py
    title: cp_library/math/table/stirling2_k_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
    title: test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
    title: test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/polynomial/pow_of_formal_power_series.test.py
    title: test/library-checker/polynomial/pow_of_formal_power_series.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \ndef fps_normalize(P: list, deg) -> list:\n    if (N:=len(P)) < deg: P[N:] =\
    \ [0]*(deg-N)\n    del P[deg:]\n    return P\n"
  code: "import cp_library.math.fps.__header__\n\ndef fps_normalize(P: list, deg)\
    \ -> list:\n    if (N:=len(P)) < deg: P[N:] = [0]*(deg-N)\n    del P[deg:]\n \
    \   return P\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/fps/fps_normalize_fn.py
  requiredBy:
  - cp_library/math/table/stirling2_k_fn.py
  - cp_library/math/table/stirling1_k_fn.py
  - cp_library/math/fps/fps_pow_fn.py
  timestamp: '2024-12-27 22:35:21+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
  - test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
  - test/library-checker/polynomial/pow_of_formal_power_series.test.py
documentation_of: cp_library/math/fps/fps_normalize_fn.py
layout: document
redirect_from:
- /library/cp_library/math/fps/fps_normalize_fn.py
- /library/cp_library/math/fps/fps_normalize_fn.py.html
title: cp_library/math/fps/fps_normalize_fn.py
---
