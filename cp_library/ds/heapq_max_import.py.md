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
    \nfrom heapq import (\n    _heapify_max as heapify_max, \n    _heappop_max as\
    \ heappop_max, \n    _siftdown_max as heapsiftdown_max,\n    _siftup_max as heapsiftup_max,\n\
    \    _siftdown as heapsiftdown,\n    _siftup as heapsiftup\n)\n\ndef heappush_max(heap,\
    \ item):\n    \"\"\"Push item onto heap, maintaining the heap invariant.\"\"\"\
    \n    heap.append(item)\n    heapsiftdown_max(heap, 0, len(heap)-1)\n\ndef heapreplace_max(heap,\
    \ item):\n    \"\"\"Pop and return the current largest value, and add the new\
    \ item.\n\n    This is more efficient than heappop_max() followed by heappush_max(),\
    \ and can be\n    more appropriate when using a fixed-size heap.  Note that the\
    \ value\n    returned may be larger than item!  That constrains reasonable uses\
    \ of\n    this routine unless written as part of a conditional replacement:\n\n\
    \        if item > heap[0]:\n            item = heapreplace_max(heap, item)\n\
    \    \"\"\"\n    returnitem = heap[0]\n    heap[0] = item\n    heapsiftup_max(heap,\
    \ 0)\n    return returnitem\n"
  code: "import cp_library.ds.__header__\n\nfrom heapq import (\n    _heapify_max\
    \ as heapify_max, \n    _heappop_max as heappop_max, \n    _siftdown_max as heapsiftdown_max,\n\
    \    _siftup_max as heapsiftup_max,\n    _siftdown as heapsiftdown,\n    _siftup\
    \ as heapsiftup\n)\n\ndef heappush_max(heap, item):\n    \"\"\"Push item onto\
    \ heap, maintaining the heap invariant.\"\"\"\n    heap.append(item)\n    heapsiftdown_max(heap,\
    \ 0, len(heap)-1)\n\ndef heapreplace_max(heap, item):\n    \"\"\"Pop and return\
    \ the current largest value, and add the new item.\n\n    This is more efficient\
    \ than heappop_max() followed by heappush_max(), and can be\n    more appropriate\
    \ when using a fixed-size heap.  Note that the value\n    returned may be larger\
    \ than item!  That constrains reasonable uses of\n    this routine unless written\
    \ as part of a conditional replacement:\n\n        if item > heap[0]:\n      \
    \      item = heapreplace_max(heap, item)\n    \"\"\"\n    returnitem = heap[0]\n\
    \    heap[0] = item\n    heapsiftup_max(heap, 0)\n    return returnitem"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/heapq_max_import.py
  requiredBy: []
  timestamp: '2024-10-24 08:20:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/heapq_max_import.py
layout: document
redirect_from:
- /library/cp_library/ds/heapq_max_import.py
- /library/cp_library/ds/heapq_max_import.py.html
title: cp_library/ds/heapq_max_import.py
---
