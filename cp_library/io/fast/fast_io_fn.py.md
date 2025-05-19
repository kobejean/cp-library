---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_2_c_scc_fast.test.py
    title: test/aoj/grl/grl_2_c_scc_fast.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/convolution/bitwise_and_convolution_fast.test.py
    title: test/library-checker/convolution/bitwise_and_convolution_fast.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/convolution/bitwise_xor_convolution.test.py
    title: test/library-checker/convolution/bitwise_xor_convolution.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/double_ended_priority_queue.test.py
    title: test/library-checker/data-structure/double_ended_priority_queue.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/double_ended_priority_queue_2heaps_fast_heapq.test.py
    title: test/library-checker/data-structure/double_ended_priority_queue_2heaps_fast_heapq.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/staticrmq.test.py
    title: test/library-checker/data-structure/staticrmq.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/staticrmq_general.test.py
    title: test/library-checker/data-structure/staticrmq_general.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/biconnected_components_scratch.test.py
    title: test/library-checker/graph/biconnected_components_scratch.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/incremental_scc.test.py
    title: test/library-checker/graph/incremental_scc.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/incremental_scc_paralel_sort.test.py
    title: test/library-checker/graph/incremental_scc_paralel_sort.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/scc_strongly_connected_components_scratch.test.py
    title: test/library-checker/graph/scc_strongly_connected_components_scratch.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/two_edge_connected_components_scratch.test.py
    title: test/library-checker/graph/two_edge_connected_components_scratch.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/other/longest_increasing_sequence.test.py
    title: test/library-checker/other/longest_increasing_sequence.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/subset_convolution.test.py
    title: test/library-checker/set-power-series/subset_convolution.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/set-power-series/subset_convolution_snippet.test.py
    title: test/library-checker/set-power-series/subset_convolution_snippet.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/tree/rooted_tree_isomorphism_classification.test.py
    title: test/library-checker/tree/rooted_tree_isomorphism_classification.test.py
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
    \n\nfrom __pypy__.builders import StringBuilder\nimport sys\nfrom os import read\
    \ as os_read, write as os_write\nfrom atexit import register as atexist_register\n\
    \nclass Fastio:\n    ibuf = bytes()\n    pil = pir = 0\n    sb = StringBuilder()\n\
    \    def load(self):\n        self.ibuf = self.ibuf[self.pil:]\n        self.ibuf\
    \ += os_read(0, 131072)\n        self.pil = 0; self.pir = len(self.ibuf)\n   \
    \ def flush_atexit(self): os_write(1, self.sb.build().encode())\n    def flush(self):\n\
    \        os_write(1, self.sb.build().encode())\n        self.sb = StringBuilder()\n\
    \    def fastin(self):\n        if self.pir - self.pil < 64: self.load()\n   \
    \     minus = x = 0\n        while self.ibuf[self.pil] < 45: self.pil += 1\n \
    \       if self.ibuf[self.pil] == 45: minus = 1; self.pil += 1\n        while\
    \ self.ibuf[self.pil] >= 48:\n            x = x * 10 + (self.ibuf[self.pil] &\
    \ 15)\n            self.pil += 1\n        if minus: return -x\n        return\
    \ x\n    def fastin_string(self):\n        if self.pir - self.pil < 64: self.load()\n\
    \        while self.ibuf[self.pil] <= 32: self.pil += 1\n        res = bytearray()\n\
    \        while self.ibuf[self.pil] > 32:\n            if self.pir - self.pil <\
    \ 64: self.load()\n            res.append(self.ibuf[self.pil])\n            self.pil\
    \ += 1\n        return res\n    def fastout(self, x): self.sb.append(str(x))\n\
    \    def fastoutln(self, x): self.sb.append(str(x)); self.sb.append('\\n')\nfastio\
    \ = Fastio()\nrd = fastio.fastin; rds = fastio.fastin_string; wt = fastio.fastout;\
    \ wtn = fastio.fastoutln; flush = fastio.flush\natexist_register(fastio.flush_atexit)\n\
    sys.stdin = None; sys.stdout = None\ndef rdl(n):\n    lst = [0]*n\n    for i in\
    \ range(n): lst[i] = rd()\n    return lst\ndef wtnl(l): wtn(' '.join(map(str,\
    \ l)))\n"
  code: "import cp_library.__header__\nimport cp_library.io.__header__\nimport cp_library.io.fast.__header__\n\
    from __pypy__.builders import StringBuilder\nimport sys\nfrom os import read as\
    \ os_read, write as os_write\nfrom atexit import register as atexist_register\n\
    \nclass Fastio:\n    ibuf = bytes()\n    pil = pir = 0\n    sb = StringBuilder()\n\
    \    def load(self):\n        self.ibuf = self.ibuf[self.pil:]\n        self.ibuf\
    \ += os_read(0, 131072)\n        self.pil = 0; self.pir = len(self.ibuf)\n   \
    \ def flush_atexit(self): os_write(1, self.sb.build().encode())\n    def flush(self):\n\
    \        os_write(1, self.sb.build().encode())\n        self.sb = StringBuilder()\n\
    \    def fastin(self):\n        if self.pir - self.pil < 64: self.load()\n   \
    \     minus = x = 0\n        while self.ibuf[self.pil] < 45: self.pil += 1\n \
    \       if self.ibuf[self.pil] == 45: minus = 1; self.pil += 1\n        while\
    \ self.ibuf[self.pil] >= 48:\n            x = x * 10 + (self.ibuf[self.pil] &\
    \ 15)\n            self.pil += 1\n        if minus: return -x\n        return\
    \ x\n    def fastin_string(self):\n        if self.pir - self.pil < 64: self.load()\n\
    \        while self.ibuf[self.pil] <= 32: self.pil += 1\n        res = bytearray()\n\
    \        while self.ibuf[self.pil] > 32:\n            if self.pir - self.pil <\
    \ 64: self.load()\n            res.append(self.ibuf[self.pil])\n            self.pil\
    \ += 1\n        return res\n    def fastout(self, x): self.sb.append(str(x))\n\
    \    def fastoutln(self, x): self.sb.append(str(x)); self.sb.append('\\n')\nfastio\
    \ = Fastio()\nrd = fastio.fastin; rds = fastio.fastin_string; wt = fastio.fastout;\
    \ wtn = fastio.fastoutln; flush = fastio.flush\natexist_register(fastio.flush_atexit)\n\
    sys.stdin = None; sys.stdout = None\ndef rdl(n):\n    lst = [0]*n\n    for i in\
    \ range(n): lst[i] = rd()\n    return lst\ndef wtnl(l): wtn(' '.join(map(str,\
    \ l)))\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/io/fast/fast_io_fn.py
  requiredBy: []
  timestamp: '2025-05-20 05:03:21+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/other/longest_increasing_sequence.test.py
  - test/library-checker/set-power-series/subset_convolution_snippet.test.py
  - test/library-checker/set-power-series/subset_convolution.test.py
  - test/library-checker/data-structure/double_ended_priority_queue.test.py
  - test/library-checker/data-structure/staticrmq_general.test.py
  - test/library-checker/data-structure/staticrmq.test.py
  - test/library-checker/data-structure/double_ended_priority_queue_2heaps_fast_heapq.test.py
  - test/library-checker/convolution/bitwise_and_convolution_fast.test.py
  - test/library-checker/convolution/bitwise_xor_convolution.test.py
  - test/library-checker/graph/incremental_scc_paralel_sort.test.py
  - test/library-checker/graph/incremental_scc.test.py
  - test/library-checker/graph/two_edge_connected_components_scratch.test.py
  - test/library-checker/graph/biconnected_components_scratch.test.py
  - test/library-checker/graph/scc_strongly_connected_components_scratch.test.py
  - test/library-checker/tree/rooted_tree_isomorphism_classification.test.py
  - test/aoj/grl/grl_2_c_scc_fast.test.py
documentation_of: cp_library/io/fast/fast_io_fn.py
layout: document
redirect_from:
- /library/cp_library/io/fast/fast_io_fn.py
- /library/cp_library/io/fast/fast_io_fn.py.html
title: cp_library/io/fast/fast_io_fn.py
---
