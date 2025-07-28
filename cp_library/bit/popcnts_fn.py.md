---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/conv/isubset_deconv_fn.py
    title: cp_library/math/conv/isubset_deconv_fn.py
  - icon: ':warning:'
    path: cp_library/math/conv/mod/isubset_conv_fn.py
    title: cp_library/math/conv/mod/isubset_conv_fn.py
  - icon: ':warning:'
    path: cp_library/math/conv/mod/isubset_deconv_fn.py
    title: cp_library/math/conv/mod/isubset_deconv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/subset_conv_fn.py
    title: cp_library/math/conv/mod/subset_conv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/subset_deconv_fn.py
    title: cp_library/math/conv/mod/subset_deconv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/subset_conv_fn.py
    title: cp_library/math/conv/subset_conv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/subset_deconv_fn.py
    title: cp_library/math/conv/subset_deconv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/sps/mod/sps_composite_fn.py
    title: cp_library/math/sps/mod/sps_composite_fn.py
  - icon: ':warning:'
    path: cp_library/math/sps/mod/sps_div_fn.py
    title: cp_library/math/sps/mod/sps_div_fn.py
  - icon: ':warning:'
    path: cp_library/math/sps/mod/sps_exp_adaptive_fn.py
    title: cp_library/math/sps/mod/sps_exp_adaptive_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/sps/mod/sps_exp_fn.py
    title: cp_library/math/sps/mod/sps_exp_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/sps/mod/sps_exp_half_fn.py
    title: cp_library/math/sps/mod/sps_exp_half_fn.py
  - icon: ':warning:'
    path: cp_library/math/sps/mod/sps_ln_adaptive_fn.py
    title: cp_library/math/sps/mod/sps_ln_adaptive_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/sps/mod/sps_ln_fn.py
    title: cp_library/math/sps/mod/sps_ln_fn.py
  - icon: ':warning:'
    path: cp_library/math/sps/mod/sps_mul_fn.py
    title: cp_library/math/sps/mod/sps_mul_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/sps/mod/sps_pow_proj_fn.py
    title: cp_library/math/sps/mod/sps_pow_proj_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/sps/mod/sps_pow_proj_poly_fn.py
    title: cp_library/math/sps/mod/sps_pow_proj_poly_fn.py
  - icon: ':warning:'
    path: cp_library/math/sps/sps_div_fn.py
    title: cp_library/math/sps/sps_div_fn.py
  - icon: ':warning:'
    path: cp_library/math/sps/sps_exp_fn.py
    title: cp_library/math/sps/sps_exp_fn.py
  - icon: ':warning:'
    path: cp_library/math/sps/sps_ln_fn.py
    title: cp_library/math/sps/sps_ln_fn.py
  - icon: ':warning:'
    path: cp_library/math/sps/sps_mul_fn.py
    title: cp_library/math/sps/sps_mul_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/exp_of_set_power_series.test.py
    title: test/library-checker/set-power-series/exp_of_set_power_series.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/exp_of_set_power_series_half.test.py
    title: test/library-checker/set-power-series/exp_of_set_power_series_half.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/polynomial_composite_set_power_series.test.py
    title: test/library-checker/set-power-series/polynomial_composite_set_power_series.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/power_projection_of_set_power_series.test.py
    title: test/library-checker/set-power-series/power_projection_of_set_power_series.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/subset_convolution.test.py
    title: test/library-checker/set-power-series/subset_convolution.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/subset_convolution_all.test.py
    title: test/library-checker/set-power-series/subset_convolution_all.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/subset_convolution_snippet.test.py
    title: test/library-checker/set-power-series/subset_convolution_snippet.test.py
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
    \ndef popcnts(N):\n    P = [0]*(1 << N)\n    for i in range(N):\n        for m\
    \ in range(b := 1<<i):\n            P[m^b] = P[m] + 1\n    return P\n"
  code: "import cp_library.bit.__header__\n\ndef popcnts(N):\n    P = [0]*(1 << N)\n\
    \    for i in range(N):\n        for m in range(b := 1<<i):\n            P[m^b]\
    \ = P[m] + 1\n    return P\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/bit/popcnts_fn.py
  requiredBy:
  - cp_library/math/sps/sps_ln_fn.py
  - cp_library/math/sps/mod/sps_pow_proj_fn.py
  - cp_library/math/sps/mod/sps_composite_fn.py
  - cp_library/math/sps/mod/sps_exp_adaptive_fn.py
  - cp_library/math/sps/mod/sps_ln_fn.py
  - cp_library/math/sps/mod/sps_pow_proj_poly_fn.py
  - cp_library/math/sps/mod/sps_div_fn.py
  - cp_library/math/sps/mod/sps_mul_fn.py
  - cp_library/math/sps/mod/sps_exp_half_fn.py
  - cp_library/math/sps/mod/sps_exp_fn.py
  - cp_library/math/sps/mod/sps_ln_adaptive_fn.py
  - cp_library/math/sps/sps_div_fn.py
  - cp_library/math/sps/sps_mul_fn.py
  - cp_library/math/sps/sps_exp_fn.py
  - cp_library/math/conv/subset_deconv_fn.py
  - cp_library/math/conv/isubset_deconv_fn.py
  - cp_library/math/conv/mod/subset_deconv_fn.py
  - cp_library/math/conv/mod/isubset_conv_fn.py
  - cp_library/math/conv/mod/isubset_deconv_fn.py
  - cp_library/math/conv/mod/subset_conv_fn.py
  - cp_library/math/conv/subset_conv_fn.py
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/set-power-series/power_projection_of_set_power_series.test.py
  - test/library-checker/set-power-series/polynomial_composite_set_power_series.test.py
  - test/library-checker/set-power-series/exp_of_set_power_series.test.py
  - test/library-checker/set-power-series/subset_convolution.test.py
  - test/library-checker/set-power-series/exp_of_set_power_series_half.test.py
  - test/library-checker/set-power-series/subset_convolution_snippet.test.py
  - test/library-checker/set-power-series/subset_convolution_all.test.py
documentation_of: cp_library/bit/popcnts_fn.py
layout: document
redirect_from:
- /library/cp_library/bit/popcnts_fn.py
- /library/cp_library/bit/popcnts_fn.py.html
title: cp_library/bit/popcnts_fn.py
---
