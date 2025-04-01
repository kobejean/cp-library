---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/conv/gcd_conv_fn.py
    title: cp_library/math/conv/gcd_conv_fn.py
  - icon: ':warning:'
    path: cp_library/math/conv/lcm_conv_fn.py
    title: cp_library/math/conv/lcm_conv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_exp_fn.py
    title: cp_library/math/fps/fps_exp_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_pow_fn.py
    title: cp_library/math/fps/fps_pow_fn.py
  - icon: ':warning:'
    path: cp_library/math/table/linear_sieve_cls.py
    title: cp_library/math/table/linear_sieve_cls.py
  - icon: ':warning:'
    path: cp_library/math/table/linear_sieve_cnts_cls.py
    title: cp_library/math/table/linear_sieve_cnts_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/primes_cls.py
    title: cp_library/math/table/primes_cls.py
  - icon: ':warning:'
    path: cp_library/math/table/sieve_cls.py
    title: cp_library/math/table/sieve_cls.py
  - icon: ':warning:'
    path: cp_library/math/table/sieve_proto.py
    title: cp_library/math/table/sieve_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling1_k_fn.py
    title: cp_library/math/table/stirling1_k_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling2_k_fn.py
    title: cp_library/math/table/stirling2_k_fn.py
  - icon: ':warning:'
    path: cp_library/math/table/totient_cls.py
    title: cp_library/math/table/totient_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/convolution/gcd_convolution.test.py
    title: test/library-checker/convolution/gcd_convolution.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/convolution/lcm_convolution.test.py
    title: test/library-checker/convolution/lcm_convolution.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
    title: test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
    title: test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/polynomial/exp_of_formal_power_series.test.py
    title: test/library-checker/polynomial/exp_of_formal_power_series.test.py
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
  - cp_library/math/table/primes_cls.py
  - cp_library/math/table/linear_sieve_cnts_cls.py
  - cp_library/math/table/totient_cls.py
  - cp_library/math/table/stirling2_k_fn.py
  - cp_library/math/table/sieve_cls.py
  - cp_library/math/table/stirling1_k_fn.py
  - cp_library/math/table/sieve_proto.py
  - cp_library/math/table/linear_sieve_cls.py
  - cp_library/math/conv/gcd_conv_fn.py
  - cp_library/math/conv/lcm_conv_fn.py
  - cp_library/math/fps/fps_pow_fn.py
  - cp_library/math/fps/fps_exp_fn.py
  timestamp: '2025-04-02 01:29:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
  - test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
  - test/library-checker/polynomial/exp_of_formal_power_series.test.py
  - test/library-checker/polynomial/pow_of_formal_power_series.test.py
  - test/library-checker/convolution/gcd_convolution.test.py
  - test/library-checker/convolution/lcm_convolution.test.py
documentation_of: cp_library/ds/reserve_fn.py
layout: document
redirect_from:
- /library/cp_library/ds/reserve_fn.py
- /library/cp_library/ds/reserve_fn.py.html
title: cp_library/ds/reserve_fn.py
---
