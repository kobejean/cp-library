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
    \nfrom heapq import _heapify_max as heapify_max, _heappop_max as heappop_max,\
    \ _siftdown_max as heapsiftdown_max\n\ndef heappush_max(heap, item):\n    \"\"\
    \"Push item onto heap, maintaining the heap invariant.\"\"\"\n    heap.append(item)\n\
    \    heapsiftdown_max(heap, 0, len(heap)-1)\n"
  code: "import cp_library.ds.__header__\n\nfrom heapq import _heapify_max as heapify_max,\
    \ _heappop_max as heappop_max, _siftdown_max as heapsiftdown_max\n\ndef heappush_max(heap,\
    \ item):\n    \"\"\"Push item onto heap, maintaining the heap invariant.\"\"\"\
    \n    heap.append(item)\n    heapsiftdown_max(heap, 0, len(heap)-1)"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/heapq_max_import.py
  requiredBy: []
  timestamp: '2024-09-28 04:04:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/heapq_max_import.py
layout: document
redirect_from:
- /library/cp_library/ds/heapq_max_import.py
- /library/cp_library/ds/heapq_max_import.py.html
title: cp_library/ds/heapq_max_import.py
---
