---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_ranged_fn.py
    title: cp_library/alg/iter/arg/argsort_ranged_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/isort_ranged_fn.py
    title: cp_library/alg/iter/sort/isort_ranged_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view6_cls.py
    title: cp_library/ds/view/view6_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/test/unittest_helper.py
    title: cp_library/test/unittest_helper.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    \nimport pytest\n\nclass TestView6:\n    def test_basic_operations(self):\n  \
    \      \"\"\"Test basic view6 operations\"\"\"\n        A1 = [1, 2, 3]\n     \
    \   A2 = [10, 20, 30]\n        A3 = [100, 200, 300]\n        A4 = [1000, 2000,\
    \ 3000]\n        A5 = [10000, 20000, 30000]\n        A6 = [100000, 200000, 300000]\n\
    \        \n        # Create view of slice [1:3]\n        v = view6(A1, A2, A3,\
    \ A4, A5, A6, 1, 3)\n        \n        assert len(v) == 2\n        assert v[0]\
    \ == (2, 20, 200, 2000, 20000, 200000)\n        assert v[1] == (3, 30, 300, 3000,\
    \ 30000, 300000)\n        \n    def test_setitem(self):\n        \"\"\"Test setting\
    \ items in view\"\"\"\n        A1 = [1, 2]\n        A2 = [10, 20]\n        A3\
    \ = [100, 200]\n        A4 = [1000, 2000]\n        A5 = [10000, 20000]\n     \
    \   A6 = [100000, 200000]\n        \n        v = view6(A1, A2, A3, A4, A5, A6,\
    \ 0, 2)\n        v[0] = (9, 90, 900, 9000, 90000, 900000)\n        \n        #\
    \ Check all arrays are updated\n        assert A1[0] == 9\n        assert A2[0]\
    \ == 90\n        assert A3[0] == 900\n        assert A4[0] == 9000\n        assert\
    \ A5[0] == 90000\n        assert A6[0] == 900000\n        \n    def test_reverse(self):\n\
    \        \"\"\"Test reverse operation\"\"\"\n        A1 = [1, 2, 3, 4]\n     \
    \   A2 = [10, 20, 30, 40]\n        A3 = [100, 200, 300, 400]\n        A4 = [1000,\
    \ 2000, 3000, 4000]\n        A5 = [10000, 20000, 30000, 40000]\n        A6 = [100000,\
    \ 200000, 300000, 400000]\n        \n        v = view6(A1, A2, A3, A4, A5, A6,\
    \ 1, 3)\n        v.reverse()\n        \n        assert v[0] == (3, 30, 300, 3000,\
    \ 30000, 300000)\n        assert v[1] == (2, 20, 200, 2000, 20000, 200000)\n\n\
    '''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\nfrom typing\
    \ import Generic\nfrom typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T');\
    \ _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3');\
    \ _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\n\n\ndef argsort_ranged(A:\
    \ list[int], l: int, r: int, reverse=False):\n    P = Packer(r-l-1); I = [A[l+i]\
    \ for i in range(r-l)]; P.ienumerate(I, reverse); I.sort()\n    for i in range(r-l):\
    \ I[i] = (I[i] & P.m) + l\n    return I\n\n\n\nclass Packer:\n    __slots__ =\
    \ 's', 'm'\n    def __init__(P, mx: int): P.s = mx.bit_length(); P.m = (1 << P.s)\
    \ - 1\n    def enc(P, a: int, b: int): return a << P.s | b\n    def dec(P, x:\
    \ int) -> tuple[int, int]: return x >> P.s, x & P.m\n    def enumerate(P, A, reverse=False):\
    \ P.ienumerate(A:=list(A), reverse); return A\n    def ienumerate(P, A, reverse=False):\n\
    \        if reverse:\n            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n\
    \        else:\n            for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def\
    \ indices(P, A: list[int]): P.iindices(A:=list(A)); return A\n    def iindices(P,\
    \ A):\n        for i,a in enumerate(A): A[i] = P.m&a\n\n\ndef isort_ranged(*L:\
    \ list, l: int, r: int, reverse=False):\n    n = r - l\n    order = argsort_ranged(L[0],\
    \ l, r, reverse=reverse)\n    inv = [0] * n\n    # order contains indices in range\
    \ [l, r), need to map to [0, n)\n    for i in range(n): inv[order[i]-l] = i\n\
    \    for i in range(n):\n        j = order[i] - l  # j is in range [0, n)\n  \
    \      for A in L: A[l+i], A[l+j] = A[l+j], A[l+i]\n        order[inv[i]], order[inv[j]]\
    \ = order[inv[j]], order[inv[i]]\n        inv[i], inv[j] = inv[j], inv[i]\n  \
    \  return L\n\n\n\nclass view6(Generic[_T1, _T2, _T3, _T4, _T5, _T6]):\n    __slots__\
    \ = 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'l', 'r'\n    def __init__(V, A1: list[_T1],\
    \ A2: list[_T2], A3: list[_T3], A4: list[_T4], A5: list[_T5], A6: list[_T6], l:\
    \ int = 0, r: int = 0): \n        V.A1, V.A2, V.A3, V.A4, V.A5, V.A6, V.l, V.r\
    \ = A1, A2, A3, A4, A5, A6, l, r\n    def __len__(V): return V.r - V.l\n    def\
    \ __getitem__(V, i: int): \n        if 0 <= i < V.r - V.l: return V.A1[V.l+i],\
    \ V.A2[V.l+i], V.A3[V.l+i], V.A4[V.l+i], V.A5[V.l+i], V.A6[V.l+i]\n        else:\
    \ raise IndexError\n    def __setitem__(V, i: int, v: tuple[_T1, _T2, _T3, _T4,\
    \ _T5, _T6]): V.A1[V.l+i], V.A2[V.l+i], V.A3[V.l+i], V.A4[V.l+i], V.A5[V.l+i],\
    \ V.A6[V.l+i] = v\n    def __contains__(V, v: tuple[_T1, _T2, _T3, _T4, _T5, _T6]):\
    \ raise NotImplemented\n    def set_range(V, l: int, r: int): V.l, V.r = l, r\n\
    \    def index(V, v: tuple[_T1, _T2, _T3, _T4, _T5, _T6]): raise NotImplemented\n\
    \    def reverse(V):\n        l, r = V.l, V.r-1\n        while l < r: \n     \
    \       V.A1[l], V.A1[r] = V.A1[r], V.A1[l]\n            V.A2[l], V.A2[r] = V.A2[r],\
    \ V.A2[l]\n            V.A3[l], V.A3[r] = V.A3[r], V.A3[l]\n            V.A4[l],\
    \ V.A4[r] = V.A4[r], V.A4[l]\n            V.A5[l], V.A5[r] = V.A5[r], V.A5[l]\n\
    \            V.A6[l], V.A6[r] = V.A6[r], V.A6[l]\n            l += 1; r -= 1\n\
    \    def sort(V, reverse=False): isort_ranged(V.A1, V.A2, V.A3, V.A4, V.A5, V.A6,\
    \ l=V.l, r=V.r, reverse=reverse)\n    def pop(V): V.r -= 1; return V.A1[V.r],\
    \ V.A2[V.r], V.A3[V.r], V.A4[V.r], V.A5[V.r], V.A6[V.r]\n    def append(V, v:\
    \ tuple[_T1, _T2, _T3, _T4, _T5, _T6]): V.A1[V.r], V.A2[V.r], V.A3[V.r], V.A4[V.r],\
    \ V.A5[V.r], V.A6[V.r] = v; V.r += 1\n    def popleft(V): V.l += 1; return V.A1[V.l-1],\
    \ V.A2[V.l-1], V.A3[V.l-1], V.A4[V.l-1], V.A5[V.l-1], V.A6[V.l-1]\n    def appendleft(V,\
    \ v: tuple[_T1, _T2, _T3, _T4, _T5, _T6]): V.l -= 1; V.A1[V.l], V.A2[V.l], V.A3[V.l],\
    \ V.A4[V.l], V.A5[V.l], V.A6[V.l] = v\n    def validate(V): return 0 <= V.l <=\
    \ V.r <= len(V.A1)\n\nif __name__ == '__main__':\n    \"\"\"\n    Helper for making\
    \ unittest files compatible with verification-helper.\n    \n    This module provides\
    \ a helper function to run a dummy Library Checker test\n    so that unittest\
    \ files can be verified by oj-verify.\n    \"\"\"\n    \n    def run_verification_helper_unittest():\n\
    \        \"\"\"\n        Run a dummy AOJ ITP1_1_A test for verification-helper\
    \ compatibility.\n        \n        This function should be called in the __main__\
    \ block of unittest files\n        that need to be compatible with verification-helper.\n\
    \        \n        The function:\n        1. Prints \"Hello World\" (AOJ ITP1_1_A\
    \ solution)\n        2. Runs pytest for the calling test file\n        3. Exits\
    \ with the pytest result code\n        \"\"\"\n        import sys\n        \n\
    \        # Print \"Hello World\" for AOJ ITP1_1_A problem\n        print(\"Hello\
    \ World\")\n        \n        import io\n        from contextlib import redirect_stdout,\
    \ redirect_stderr\n    \n        # Capture all output during test execution\n\
    \        output = io.StringIO()\n        with redirect_stdout(output), redirect_stderr(output):\n\
    \            # Get the calling module's file path\n            frame = sys._getframe(1)\n\
    \            test_file = frame.f_globals.get('__file__')\n            if test_file\
    \ is None:\n                test_file = sys.argv[0]\n            result = pytest.main([test_file])\n\
    \        \n        if result != 0: \n            print(output.getvalue())\n  \
    \      sys.exit(result)\n    run_verification_helper_unittest()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    \nimport pytest\n\nclass TestView6:\n    def test_basic_operations(self):\n  \
    \      \"\"\"Test basic view6 operations\"\"\"\n        A1 = [1, 2, 3]\n     \
    \   A2 = [10, 20, 30]\n        A3 = [100, 200, 300]\n        A4 = [1000, 2000,\
    \ 3000]\n        A5 = [10000, 20000, 30000]\n        A6 = [100000, 200000, 300000]\n\
    \        \n        # Create view of slice [1:3]\n        v = view6(A1, A2, A3,\
    \ A4, A5, A6, 1, 3)\n        \n        assert len(v) == 2\n        assert v[0]\
    \ == (2, 20, 200, 2000, 20000, 200000)\n        assert v[1] == (3, 30, 300, 3000,\
    \ 30000, 300000)\n        \n    def test_setitem(self):\n        \"\"\"Test setting\
    \ items in view\"\"\"\n        A1 = [1, 2]\n        A2 = [10, 20]\n        A3\
    \ = [100, 200]\n        A4 = [1000, 2000]\n        A5 = [10000, 20000]\n     \
    \   A6 = [100000, 200000]\n        \n        v = view6(A1, A2, A3, A4, A5, A6,\
    \ 0, 2)\n        v[0] = (9, 90, 900, 9000, 90000, 900000)\n        \n        #\
    \ Check all arrays are updated\n        assert A1[0] == 9\n        assert A2[0]\
    \ == 90\n        assert A3[0] == 900\n        assert A4[0] == 9000\n        assert\
    \ A5[0] == 90000\n        assert A6[0] == 900000\n        \n    def test_reverse(self):\n\
    \        \"\"\"Test reverse operation\"\"\"\n        A1 = [1, 2, 3, 4]\n     \
    \   A2 = [10, 20, 30, 40]\n        A3 = [100, 200, 300, 400]\n        A4 = [1000,\
    \ 2000, 3000, 4000]\n        A5 = [10000, 20000, 30000, 40000]\n        A6 = [100000,\
    \ 200000, 300000, 400000]\n        \n        v = view6(A1, A2, A3, A4, A5, A6,\
    \ 1, 3)\n        v.reverse()\n        \n        assert v[0] == (3, 30, 300, 3000,\
    \ 30000, 300000)\n        assert v[1] == (2, 20, 200, 2000, 20000, 200000)\n\n\
    from cp_library.ds.view.view6_cls import view6\n\nif __name__ == '__main__':\n\
    \    from cp_library.test.unittest_helper import run_verification_helper_unittest\n\
    \    run_verification_helper_unittest()"
  dependsOn:
  - cp_library/ds/view/view6_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/alg/iter/sort/isort_ranged_fn.py
  - cp_library/alg/iter/arg/argsort_ranged_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: true
  path: test/unittests/ds/view/view6_cls_test.py
  requiredBy: []
  timestamp: '2025-07-26 11:14:31+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/view/view6_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/view/view6_cls_test.py
- /verify/test/unittests/ds/view/view6_cls_test.py.html
title: test/unittests/ds/view/view6_cls_test.py
---
