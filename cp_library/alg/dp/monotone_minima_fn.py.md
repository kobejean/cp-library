---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/minplus_conv_fn.py
    title: cp_library/math/conv/minplus_conv_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc325_f_minplus_conv_inplace.test.py
    title: test/atcoder/abc/abc325_f_minplus_conv_inplace.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/convolution/min_plus_convolution_convex_arbitrary.test.py
    title: test/library-checker/convolution/min_plus_convolution_convex_arbitrary.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/convolution/min_plus_convolution_convex_convex.test.py
    title: test/library-checker/convolution/min_plus_convolution_convex_convex.test.py
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
    from typing import Callable\n\ndef monotone_minima(N: int, M: int, func: Callable[[int,int,int],bool]):\n\
    \    '''\n    Finds row minima in a totally monotone N\xD7M matrix using the SMAWK\
    \ algorithm.\n    The matrix is defined implicitly through the comparison function.\n\
    \    \n    A matrix is totally monotone if the minimum in row i occurs at column\
    \ j,\n    then the minimum in row i+1 must occur at column j' where j \u2264 j'.\n\
    \    \n    Time: O(N log M), Space: O(N)\n    \n    Args:\n        N: Number of\
    \ rows\n        M: Number of columns\n        func(i,j,k): Returns True if element\
    \ (i,j) < element (i,k)\n    \n    Returns:\n        List of column indices containing\
    \ the minimum value for each row\n    \n    Example:\n        # Find minima where\
    \ each element is (i-j)\xB2\n        min_indices = monotone_minima(5, 5, lambda\
    \ i,j,k: (i-j)**2 < (i-k)**2)\n    '''\n    min_j, st = [0] * N, elist(N)\n  \
    \  st.append((0, N, 0, M))\n    while st:\n        li, ri, lj, rj = st.pop()\n\
    \        if li == ri: continue\n        mi, mj = li + ri >> 1, lj\n        for\
    \ j in range(lj + 1, rj):\n            if func(mi, mj, j): mj = j\n        min_j[mi]\
    \ = mj\n        st.append((li, mi, lj, mj+1))\n        st.append((mi+1, ri, mj,\
    \ rj))\n    return min_j\n\n\n\ndef elist(est_len: int) -> list: ...\ntry:\n \
    \   from __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n\
    \        return []\nelist = newlist_hint\n    \n"
  code: "import cp_library.alg.dp.__header__\nfrom typing import Callable\n\ndef monotone_minima(N:\
    \ int, M: int, func: Callable[[int,int,int],bool]):\n    '''\n    Finds row minima\
    \ in a totally monotone N\xD7M matrix using the SMAWK algorithm.\n    The matrix\
    \ is defined implicitly through the comparison function.\n    \n    A matrix is\
    \ totally monotone if the minimum in row i occurs at column j,\n    then the minimum\
    \ in row i+1 must occur at column j' where j \u2264 j'.\n    \n    Time: O(N log\
    \ M), Space: O(N)\n    \n    Args:\n        N: Number of rows\n        M: Number\
    \ of columns\n        func(i,j,k): Returns True if element (i,j) < element (i,k)\n\
    \    \n    Returns:\n        List of column indices containing the minimum value\
    \ for each row\n    \n    Example:\n        # Find minima where each element is\
    \ (i-j)\xB2\n        min_indices = monotone_minima(5, 5, lambda i,j,k: (i-j)**2\
    \ < (i-k)**2)\n    '''\n    min_j, st = [0] * N, elist(N)\n    st.append((0, N,\
    \ 0, M))\n    while st:\n        li, ri, lj, rj = st.pop()\n        if li == ri:\
    \ continue\n        mi, mj = li + ri >> 1, lj\n        for j in range(lj + 1,\
    \ rj):\n            if func(mi, mj, j): mj = j\n        min_j[mi] = mj\n     \
    \   st.append((li, mi, lj, mj+1))\n        st.append((mi+1, ri, mj, rj))\n   \
    \ return min_j\n\nfrom cp_library.ds.elist_fn import elist"
  dependsOn:
  - cp_library/ds/elist_fn.py
  isVerificationFile: false
  path: cp_library/alg/dp/monotone_minima_fn.py
  requiredBy:
  - cp_library/math/conv/minplus_conv_fn.py
  timestamp: '2025-04-03 08:59:41+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/convolution/min_plus_convolution_convex_arbitrary.test.py
  - test/library-checker/convolution/min_plus_convolution_convex_convex.test.py
  - test/atcoder/abc/abc325_f_minplus_conv_inplace.test.py
documentation_of: cp_library/alg/dp/monotone_minima_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/monotone_minima_fn.py
- /library/cp_library/alg/dp/monotone_minima_fn.py.html
title: cp_library/alg/dp/monotone_minima_fn.py
---
