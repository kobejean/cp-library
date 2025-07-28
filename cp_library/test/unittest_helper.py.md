---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/grid/grid_cls_test.py
    title: test/unittests/ds/grid/grid_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/list/list2_cls_test.py
    title: test/unittests/ds/list/list2_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/list/list3_cls_test.py
    title: test/unittests/ds/list/list3_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/list/list4_cls_test.py
    title: test/unittests/ds/list/list4_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/list/list5_cls_test.py
    title: test/unittests/ds/list/list5_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/list/list6_cls_test.py
    title: test/unittests/ds/list/list6_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/bit/bit2_cls_test.py
    title: test/unittests/ds/tree/bit/bit2_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/bit/bit3_cls_test.py
    title: test/unittests/ds/tree/bit/bit3_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/bit/bit4_cls_test.py
    title: test/unittests/ds/tree/bit/bit4_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/bit/bit5_cls_test.py
    title: test/unittests/ds/tree/bit/bit5_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/bit/bit6_cls_test.py
    title: test/unittests/ds/tree/bit/bit6_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/bst/treap_monoid_cls_test.py
    title: test/unittests/ds/tree/bst/treap_monoid_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/seg/segtree2_cls_test.py
    title: test/unittests/ds/tree/seg/segtree2_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/seg/segtree3_cls_test.py
    title: test/unittests/ds/tree/seg/segtree3_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/seg/segtree4_cls_test.py
    title: test/unittests/ds/tree/seg/segtree4_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/seg/segtree5_cls_test.py
    title: test/unittests/ds/tree/seg/segtree5_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/tree/seg/segtree6_cls_test.py
    title: test/unittests/ds/tree/seg/segtree6_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/csr2_cls_test.py
    title: test/unittests/ds/view/csr2_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/csr3_cls_test.py
    title: test/unittests/ds/view/csr3_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/csr4_cls_test.py
    title: test/unittests/ds/view/csr4_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/csr5_cls_test.py
    title: test/unittests/ds/view/csr5_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/csr6_cls_test.py
    title: test/unittests/ds/view/csr6_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/csr_cls_test.py
    title: test/unittests/ds/view/csr_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/view2_cls_test.py
    title: test/unittests/ds/view/view2_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/view3_cls_test.py
    title: test/unittests/ds/view/view3_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/view4_cls_test.py
    title: test/unittests/ds/view/view4_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/view5_cls_test.py
    title: test/unittests/ds/view/view5_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/view6_cls_test.py
    title: test/unittests/ds/view/view6_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/view_cls_test.py
    title: test/unittests/ds/view/view_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/wavelet/wm_static_cls_test.py
    title: test/unittests/ds/wavelet/wm_static_cls_test.py
  - icon: ':heavy_check_mark:'
    path: test/unittests/io/io_cls_test.py
    title: test/unittests/io/io_cls_test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\"\"\"\nHelper for making unittest files compatible with verification-helper.\n\
    \nThis module provides a helper function to run a dummy Library Checker test\n\
    so that unittest files can be verified by oj-verify.\n\"\"\"\n\ndef run_verification_helper_unittest():\n\
    \    \"\"\"\n    Run a dummy AOJ ITP1_1_A test for verification-helper compatibility.\n\
    \    \n    This function should be called in the __main__ block of unittest files\n\
    \    that need to be compatible with verification-helper.\n    \n    The function:\n\
    \    1. Prints \"Hello World\" (AOJ ITP1_1_A solution)\n    2. Runs pytest for\
    \ the calling test file\n    3. Exits with the pytest result code\n    \"\"\"\n\
    \    import sys\n    \n    # Print \"Hello World\" for AOJ ITP1_1_A problem\n\
    \    print(\"Hello World\")\n    \n    import pytest\n    import io\n    from\
    \ contextlib import redirect_stdout, redirect_stderr\n\n    # Capture all output\
    \ during test execution\n    output = io.StringIO()\n    with redirect_stdout(output),\
    \ redirect_stderr(output):\n        # Get the calling module's file path\n   \
    \     frame = sys._getframe(1)\n        test_file = frame.f_globals.get('__file__')\n\
    \        if test_file is None:\n            test_file = sys.argv[0]\n        result\
    \ = pytest.main([test_file])\n    \n    if result != 0: \n        print(output.getvalue())\n\
    \    sys.exit(result)\n"
  code: "\"\"\"\nHelper for making unittest files compatible with verification-helper.\n\
    \nThis module provides a helper function to run a dummy Library Checker test\n\
    so that unittest files can be verified by oj-verify.\n\"\"\"\n\ndef run_verification_helper_unittest():\n\
    \    \"\"\"\n    Run a dummy AOJ ITP1_1_A test for verification-helper compatibility.\n\
    \    \n    This function should be called in the __main__ block of unittest files\n\
    \    that need to be compatible with verification-helper.\n    \n    The function:\n\
    \    1. Prints \"Hello World\" (AOJ ITP1_1_A solution)\n    2. Runs pytest for\
    \ the calling test file\n    3. Exits with the pytest result code\n    \"\"\"\n\
    \    import sys\n    \n    # Print \"Hello World\" for AOJ ITP1_1_A problem\n\
    \    print(\"Hello World\")\n    \n    import pytest\n    import io\n    from\
    \ contextlib import redirect_stdout, redirect_stderr\n\n    # Capture all output\
    \ during test execution\n    output = io.StringIO()\n    with redirect_stdout(output),\
    \ redirect_stderr(output):\n        # Get the calling module's file path\n   \
    \     frame = sys._getframe(1)\n        test_file = frame.f_globals.get('__file__')\n\
    \        if test_file is None:\n            test_file = sys.argv[0]\n        result\
    \ = pytest.main([test_file])\n    \n    if result != 0: \n        print(output.getvalue())\n\
    \    sys.exit(result)"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/test/unittest_helper.py
  requiredBy: []
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/unittests/ds/wavelet/wm_static_cls_test.py
  - test/unittests/ds/view/csr4_cls_test.py
  - test/unittests/ds/view/csr5_cls_test.py
  - test/unittests/ds/view/view2_cls_test.py
  - test/unittests/ds/view/csr2_cls_test.py
  - test/unittests/ds/view/view6_cls_test.py
  - test/unittests/ds/view/view_cls_test.py
  - test/unittests/ds/view/csr6_cls_test.py
  - test/unittests/ds/view/view5_cls_test.py
  - test/unittests/ds/view/csr_cls_test.py
  - test/unittests/ds/view/csr3_cls_test.py
  - test/unittests/ds/view/view4_cls_test.py
  - test/unittests/ds/view/view3_cls_test.py
  - test/unittests/ds/grid/grid_cls_test.py
  - test/unittests/ds/tree/bst/treap_monoid_cls_test.py
  - test/unittests/ds/tree/seg/segtree2_cls_test.py
  - test/unittests/ds/tree/seg/segtree4_cls_test.py
  - test/unittests/ds/tree/seg/segtree3_cls_test.py
  - test/unittests/ds/tree/seg/segtree5_cls_test.py
  - test/unittests/ds/tree/seg/segtree6_cls_test.py
  - test/unittests/ds/tree/bit/bit4_cls_test.py
  - test/unittests/ds/tree/bit/bit6_cls_test.py
  - test/unittests/ds/tree/bit/bit5_cls_test.py
  - test/unittests/ds/tree/bit/bit3_cls_test.py
  - test/unittests/ds/tree/bit/bit2_cls_test.py
  - test/unittests/ds/list/list5_cls_test.py
  - test/unittests/ds/list/list6_cls_test.py
  - test/unittests/ds/list/list3_cls_test.py
  - test/unittests/ds/list/list4_cls_test.py
  - test/unittests/ds/list/list2_cls_test.py
  - test/unittests/io/io_cls_test.py
documentation_of: cp_library/test/unittest_helper.py
layout: document
redirect_from:
- /library/cp_library/test/unittest_helper.py
- /library/cp_library/test/unittest_helper.py.html
title: cp_library/test/unittest_helper.py
---
