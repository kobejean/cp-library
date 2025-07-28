---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/perf/benchmark.py
    title: cp_library/perf/benchmark.py
  - icon: ':warning:'
    path: cp_library/perf/timing.py
    title: cp_library/perf/timing.py
  - icon: ':warning:'
    path: perf/bit2.py
    title: perf/bit2.py
  - icon: ':warning:'
    path: perf/bit6.py
    title: perf/bit6.py
  - icon: ':warning:'
    path: perf/bool_list.py
    title: perf/bool_list.py
  - icon: ':warning:'
    path: perf/bytearray_decode.py
    title: perf/bytearray_decode.py
  - icon: ':warning:'
    path: perf/csr.py
    title: perf/csr.py
  - icon: ':warning:'
    path: perf/csr2.py
    title: perf/csr2.py
  - icon: ':warning:'
    path: perf/csr6.py
    title: perf/csr6.py
  - icon: ':warning:'
    path: perf/deque.py
    title: perf/deque.py
  - icon: ':warning:'
    path: perf/edge_list.py
    title: perf/edge_list.py
  - icon: ':warning:'
    path: perf/grid.py
    title: perf/grid.py
  - icon: ':warning:'
    path: perf/heap_csr.py
    title: perf/heap_csr.py
  - icon: ':warning:'
    path: perf/heap_view.py
    title: perf/heap_view.py
  - icon: ':warning:'
    path: perf/list2.py
    title: perf/list2.py
  - icon: ':warning:'
    path: perf/list6.py
    title: perf/list6.py
  - icon: ':warning:'
    path: perf/list_view.py
    title: perf/list_view.py
  - icon: ':warning:'
    path: perf/mlist.py
    title: perf/mlist.py
  - icon: ':warning:'
    path: perf/que.py
    title: perf/que.py
  - icon: ':warning:'
    path: perf/rank.py
    title: perf/rank.py
  - icon: ':warning:'
    path: perf/segtree2.py
    title: perf/segtree2.py
  - icon: ':warning:'
    path: perf/segtree6.py
    title: perf/segtree6.py
  - icon: ':warning:'
    path: perf/view2.py
    title: perf/view2.py
  - icon: ':warning:'
    path: perf/view6.py
    title: perf/view6.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "\"\"\"\nChecksum utilities for benchmark validation.\nProvides consistent\
    \ ways to compute checksums across benchmarks.\n\"\"\"\n\nfrom typing import Any\n\
    \n\ndef update_checksum(current: int, value: int) -> int:\n    \"\"\"Update checksum\
    \ with a single value using hash-like function.\"\"\"\n    return (current * 31\
    \ + value) & 0xFFFFFFFF\n\n\ndef result_checksum(result: Any) -> Any:\n    \"\"\
    \"\n    Calculate checksum for benchmark result with fallback for non-hashable\
    \ types.\n    \n    This function tries to create a consistent hash for any type\
    \ of result,\n    with intelligent fallbacks for common non-hashable types like\
    \ lists, sets, and dicts.\n    \n    Args:\n        result: The result to checksum\
    \ (can be any type)\n        \n    Returns:\n        Hash value if successful,\
    \ original result if all fallbacks fail\n    \"\"\"\n    # Try direct hash first\
    \ (fastest path for hashable objects)\n    try:\n        return hash(result)\n\
    \    except TypeError:\n        pass\n    \n    # Try common fallback conversions\
    \ for non-hashable types\n    try:\n        if isinstance(result, dict):\n   \
    \         # Convert dict to sorted tuple of items for consistent ordering\n  \
    \          return hash(tuple(sorted(result.items())))\n        elif isinstance(result,\
    \ set):\n            # Convert set to sorted tuple for consistent ordering\n \
    \           return hash(tuple(sorted(result)))\n        elif _is_iterable_not_string(result):\n\
    \            # Convert other iterables (lists, etc.) to tuple\n            return\
    \ hash(tuple(result))\n        elif hasattr(result, '__dict__'):\n           \
    \ # Convert objects with attributes to tuple of sorted items\n            return\
    \ hash(tuple(sorted(result.__dict__.items())))\n        else:\n            # For\
    \ other types, convert to string as last resort\n            return hash(str(result))\n\
    \    except (TypeError, RecursionError):\n        # If all fallbacks fail, return\
    \ the original result\n        # The validation logic will handle it\n       \
    \ return result\n\n\ndef _is_iterable_not_string(obj: Any) -> bool:\n    \"\"\"\
    \n    Check if object is iterable but not a string or bytes.\n    \n    Uses both\
    \ __iter__ and __getitem__ checks to catch more iterable types\n    while excluding\
    \ strings and bytes which should be handled differently.\n    \"\"\"\n    return\
    \ (\n        (hasattr(obj, '__iter__') or hasattr(obj, '__getitem__')) \n    \
    \    and not isinstance(obj, (str, bytes))\n    )\n"
  code: "\"\"\"\nChecksum utilities for benchmark validation.\nProvides consistent\
    \ ways to compute checksums across benchmarks.\n\"\"\"\n\nfrom typing import Any\n\
    \n\ndef update_checksum(current: int, value: int) -> int:\n    \"\"\"Update checksum\
    \ with a single value using hash-like function.\"\"\"\n    return (current * 31\
    \ + value) & 0xFFFFFFFF\n\n\ndef result_checksum(result: Any) -> Any:\n    \"\"\
    \"\n    Calculate checksum for benchmark result with fallback for non-hashable\
    \ types.\n    \n    This function tries to create a consistent hash for any type\
    \ of result,\n    with intelligent fallbacks for common non-hashable types like\
    \ lists, sets, and dicts.\n    \n    Args:\n        result: The result to checksum\
    \ (can be any type)\n        \n    Returns:\n        Hash value if successful,\
    \ original result if all fallbacks fail\n    \"\"\"\n    # Try direct hash first\
    \ (fastest path for hashable objects)\n    try:\n        return hash(result)\n\
    \    except TypeError:\n        pass\n    \n    # Try common fallback conversions\
    \ for non-hashable types\n    try:\n        if isinstance(result, dict):\n   \
    \         # Convert dict to sorted tuple of items for consistent ordering\n  \
    \          return hash(tuple(sorted(result.items())))\n        elif isinstance(result,\
    \ set):\n            # Convert set to sorted tuple for consistent ordering\n \
    \           return hash(tuple(sorted(result)))\n        elif _is_iterable_not_string(result):\n\
    \            # Convert other iterables (lists, etc.) to tuple\n            return\
    \ hash(tuple(result))\n        elif hasattr(result, '__dict__'):\n           \
    \ # Convert objects with attributes to tuple of sorted items\n            return\
    \ hash(tuple(sorted(result.__dict__.items())))\n        else:\n            # For\
    \ other types, convert to string as last resort\n            return hash(str(result))\n\
    \    except (TypeError, RecursionError):\n        # If all fallbacks fail, return\
    \ the original result\n        # The validation logic will handle it\n       \
    \ return result\n\n\ndef _is_iterable_not_string(obj: Any) -> bool:\n    \"\"\"\
    \n    Check if object is iterable but not a string or bytes.\n    \n    Uses both\
    \ __iter__ and __getitem__ checks to catch more iterable types\n    while excluding\
    \ strings and bytes which should be handled differently.\n    \"\"\"\n    return\
    \ (\n        (hasattr(obj, '__iter__') or hasattr(obj, '__getitem__')) \n    \
    \    and not isinstance(obj, (str, bytes))\n    )"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/perf/checksum.py
  requiredBy:
  - cp_library/perf/timing.py
  - cp_library/perf/benchmark.py
  - perf/bool_list.py
  - perf/view2.py
  - perf/heap_view.py
  - perf/list_view.py
  - perf/mlist.py
  - perf/que.py
  - perf/list6.py
  - perf/grid.py
  - perf/edge_list.py
  - perf/csr.py
  - perf/bit6.py
  - perf/deque.py
  - perf/segtree2.py
  - perf/view6.py
  - perf/csr6.py
  - perf/segtree6.py
  - perf/csr2.py
  - perf/bit2.py
  - perf/rank.py
  - perf/list2.py
  - perf/heap_csr.py
  - perf/bytearray_decode.py
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/perf/checksum.py
layout: document
redirect_from:
- /library/cp_library/perf/checksum.py
- /library/cp_library/perf/checksum.py.html
title: cp_library/perf/checksum.py
---
