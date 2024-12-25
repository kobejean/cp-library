---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_exp_fn.py
    title: cp_library/math/fps/fps_exp_fn.py
  - icon: ':warning:'
    path: cp_library/math/fps/fps_ideriv_k_fn.py
    title: cp_library/math/fps/fps_ideriv_k_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_inv_fn.py
    title: cp_library/math/fps/fps_inv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_log_fn.py
    title: cp_library/math/fps/fps_log_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_pow_fn.py
    title: cp_library/math/fps/fps_pow_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_tayler_shift_fn.py
    title: cp_library/math/fps/fps_tayler_shift_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_ntt_cls.py
    title: cp_library/math/mod/mint_ntt_cls.py
  - icon: ':warning:'
    path: cp_library/math/nt/chinese_remainder_theorem_fn.py
    title: cp_library/math/nt/chinese_remainder_theorem_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/nt/conv_int_fn.py
    title: cp_library/math/nt/conv_int_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/nt/ntt_cls.py
    title: cp_library/math/nt/ntt_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/modcomb_cls.py
    title: cp_library/math/table/modcomb_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling1_k_fn.py
    title: cp_library/math/table/stirling1_k_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling1_n_fn.py
    title: cp_library/math/table/stirling1_n_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling2_k_fn.py
    title: cp_library/math/table/stirling2_k_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling2_n_fn.py
    title: cp_library/math/table/stirling2_n_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/arc168_c_swap_characters_combinatoric.test.py
    title: test/arc168_c_swap_characters_combinatoric.test.py
  - icon: ':heavy_check_mark:'
    path: test/convolution.test.py
    title: test/convolution.test.py
  - icon: ':heavy_check_mark:'
    path: test/convolution_int.test.py
    title: test/convolution_int.test.py
  - icon: ':heavy_check_mark:'
    path: test/convolution_mod_1000000007.test.py
    title: test/convolution_mod_1000000007.test.py
  - icon: ':heavy_check_mark:'
    path: test/exp_of_formal_power_series.test.py
    title: test/exp_of_formal_power_series.test.py
  - icon: ':heavy_check_mark:'
    path: test/inv_of_formal_power_series.test.py
    title: test/inv_of_formal_power_series.test.py
  - icon: ':heavy_check_mark:'
    path: test/log_of_formal_power_series.test.py
    title: test/log_of_formal_power_series.test.py
  - icon: ':heavy_check_mark:'
    path: test/polynomial_taylor_shift.test.py
    title: test/polynomial_taylor_shift.test.py
  - icon: ':heavy_check_mark:'
    path: test/pow_of_formal_power_series.test.py
    title: test/pow_of_formal_power_series.test.py
  - icon: ':heavy_check_mark:'
    path: test/stirling_number_of_the_first_kind.test.py
    title: test/stirling_number_of_the_first_kind.test.py
  - icon: ':heavy_check_mark:'
    path: test/stirling_number_of_the_first_kind_fixed_k.test.py
    title: test/stirling_number_of_the_first_kind_fixed_k.test.py
  - icon: ':heavy_check_mark:'
    path: test/stirling_number_of_the_second_kind.test.py
    title: test/stirling_number_of_the_second_kind.test.py
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
    \ndef mod_inv(x, mod):\n    a,b,s,t = x, mod, 1, 0\n    while b:\n        a,b,s,t\
    \ = b,a%b,t,s-a//b*t\n    if a == 1: return s % mod\n    raise ValueError(f\"\
    {x} is not invertible in mod {mod}\")\n"
  code: "import cp_library.math.nt.__header__\n\ndef mod_inv(x, mod):\n    a,b,s,t\
    \ = x, mod, 1, 0\n    while b:\n        a,b,s,t = b,a%b,t,s-a//b*t\n    if a ==\
    \ 1: return s % mod\n    raise ValueError(f\"{x} is not invertible in mod {mod}\"\
    )\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/nt/mod_inv_fn.py
  requiredBy:
  - cp_library/math/nt/conv_int_fn.py
  - cp_library/math/nt/chinese_remainder_theorem_fn.py
  - cp_library/math/nt/ntt_cls.py
  - cp_library/math/table/modcomb_cls.py
  - cp_library/math/table/stirling2_k_fn.py
  - cp_library/math/table/stirling1_k_fn.py
  - cp_library/math/table/stirling2_n_fn.py
  - cp_library/math/table/stirling1_n_fn.py
  - cp_library/math/mod/mint_ntt_cls.py
  - cp_library/math/fps/fps_exp_fn.py
  - cp_library/math/fps/fps_ideriv_k_fn.py
  - cp_library/math/fps/fps_tayler_shift_fn.py
  - cp_library/math/fps/fps_log_fn.py
  - cp_library/math/fps/fps_inv_fn.py
  - cp_library/math/fps/fps_pow_fn.py
  timestamp: '2024-12-25 17:59:38+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/log_of_formal_power_series.test.py
  - test/convolution_mod_1000000007.test.py
  - test/arc168_c_swap_characters_combinatoric.test.py
  - test/pow_of_formal_power_series.test.py
  - test/exp_of_formal_power_series.test.py
  - test/polynomial_taylor_shift.test.py
  - test/stirling_number_of_the_second_kind.test.py
  - test/inv_of_formal_power_series.test.py
  - test/stirling_number_of_the_second_kind_fixed_k.test.py
  - test/convolution_int.test.py
  - test/convolution.test.py
  - test/stirling_number_of_the_first_kind.test.py
  - test/stirling_number_of_the_first_kind_fixed_k.test.py
documentation_of: cp_library/math/nt/mod_inv_fn.py
layout: document
redirect_from:
- /library/cp_library/math/nt/mod_inv_fn.py
- /library/cp_library/math/nt/mod_inv_fn.py.html
title: cp_library/math/nt/mod_inv_fn.py
---
