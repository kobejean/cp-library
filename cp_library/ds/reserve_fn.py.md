---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_exp_fn.py
    title: cp_library/math/fps/fps_exp_fn.py
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
    path: test/exp_of_formal_power_series.test.py
    title: test/exp_of_formal_power_series.test.py
  - icon: ':heavy_check_mark:'
    path: test/pow_of_formal_power_series.test.py
    title: test/pow_of_formal_power_series.test.py
  - icon: ':heavy_check_mark:'
    path: test/stirling_number_of_the_first_kind_fixed_k.test.py
    title: test/stirling_number_of_the_first_kind_fixed_k.test.py
  - icon: ':heavy_check_mark:'
    path: test/stirling_number_of_the_second_kind_fixed_k.test.py
    title: test/stirling_number_of_the_second_kind_fixed_k.test.py
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
    \ndef reserve(A: list, est_len: int) -> None: ...\ntry:\n    from __pypy__ import\
    \ resizelist_hint\nexcept:\n    def resizelist_hint(A: list, est_len: int):\n\
    \        pass\nreserve = resizelist_hint\n"
  code: "import cp_library.ds.__header__\n\ndef reserve(A: list, est_len: int) ->\
    \ None: ...\ntry:\n    from __pypy__ import resizelist_hint\nexcept:\n    def\
    \ resizelist_hint(A: list, est_len: int):\n        pass\nreserve = resizelist_hint"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/reserve_fn.py
  requiredBy:
  - cp_library/math/table/stirling2_k_fn.py
  - cp_library/math/table/stirling1_k_fn.py
  - cp_library/math/fps/fps_exp_fn.py
  - cp_library/math/fps/fps_pow_fn.py
  timestamp: '2024-12-25 17:59:38+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/pow_of_formal_power_series.test.py
  - test/exp_of_formal_power_series.test.py
  - test/stirling_number_of_the_second_kind_fixed_k.test.py
  - test/stirling_number_of_the_first_kind_fixed_k.test.py
documentation_of: cp_library/ds/reserve_fn.py
layout: document
redirect_from:
- /library/cp_library/ds/reserve_fn.py
- /library/cp_library/ds/reserve_fn.py.html
title: cp_library/ds/reserve_fn.py
---
