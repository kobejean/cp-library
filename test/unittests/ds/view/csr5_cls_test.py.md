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
    path: cp_library/ds/view/csr5_cls.py
    title: cp_library/ds/view/csr5_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view5_cls.py
    title: cp_library/ds/view/view5_cls.py
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
    \nimport pytest\n\nclass TestCSR5:\n    def test_basic_operations(self):\n   \
    \     \"\"\"Test basic CSR5 operations with 5 attributes\"\"\"\n        K = [0,\
    \ 2]\n        V1 = [1, 0]\n        V2 = [10, 20]\n        V3 = [100, 200]\n  \
    \      V4 = [1000, 2000]\n        V5 = [10000, 20000]\n        \n        csr =\
    \ CSR5.bucketize(3, K, V1, V2, V3, V4, V5)\n        \n        assert len(csr)\
    \ == 3\n        \n        # Node 0\n        assert list(csr[0]) == [(1, 10, 100,\
    \ 1000, 10000)]\n        \n        # Node 1 (empty)\n        assert list(csr[1])\
    \ == []\n        \n        # Node 2\n        assert list(csr[2]) == [(0, 20, 200,\
    \ 2000, 20000)]\n        \n    def test_large_graph(self):\n        \"\"\"Test\
    \ CSR5 with larger graph\"\"\"\n        # Create a star graph: node 0 connected\
    \ to all others\n        n = 5\n        K = []\n        V1, V2, V3, V4, V5 = [],\
    \ [], [], [], []\n        \n        for i in range(1, n):\n            K.append(0)\n\
    \            V1.append(i)\n            V2.append(i * 10)\n            V3.append(i\
    \ * 100)\n            V4.append(i * 1000)\n            V5.append(i * 10000)\n\
    \        \n        csr = CSR5.bucketize(n, K, V1, V2, V3, V4, V5)\n        \n\
    \        # Check node 0 has n-1 neighbors\n        neighbors0 = list(csr[0])\n\
    \        assert len(neighbors0) == n - 1\n        \n        # Check values\n \
    \       for i, neighbor in enumerate(neighbors0):\n            expected = (i+1,\
    \ (i+1)*10, (i+1)*100, (i+1)*1000, (i+1)*10000)\n            assert neighbor ==\
    \ expected\n            \n    def test_direct_access_and_set(self):\n        \"\
    \"\"Test direct access and modification\"\"\"\n        A1 = [1, 2, 3]\n      \
    \  A2 = [10, 20, 30]\n        A3 = [100, 200, 300]\n        A4 = [1000, 2000,\
    \ 3000]\n        A5 = [10000, 20000, 30000]\n        O = [0, 2, 2, 3]\n      \
    \  \n        csr = CSR5(A1, A2, A3, A4, A5, O)\n        \n        # Direct access\n\
    \        assert csr(0, 0) == (1, 10, 100, 1000, 10000)\n        assert csr(0,\
    \ 1) == (2, 20, 200, 2000, 20000)\n        assert csr(2, 0) == (3, 30, 300, 3000,\
    \ 30000)\n        \n        # Set operation\n        csr.set(0, 0, (5, 50, 500,\
    \ 5000, 50000))\n        assert csr(0, 0) == (5, 50, 500, 5000, 50000)\n\n'''\n\
    \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\nfrom typing\
    \ import Generic\nfrom typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T');\
    \ _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3');\
    \ _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\n\n\n\n\n\
    def argsort_ranged(A: list[int], l: int, r: int, reverse=False):\n    P = Packer(r-l-1);\
    \ I = [A[l+i] for i in range(r-l)]; P.ienumerate(I, reverse); I.sort()\n    for\
    \ i in range(r-l): I[i] = (I[i] & P.m) + l\n    return I\n\n\n\nclass Packer:\n\
    \    __slots__ = 's', 'm'\n    def __init__(P, mx: int): P.s = mx.bit_length();\
    \ P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int): return a << P.s | b\n\
    \    def dec(P, x: int) -> tuple[int, int]: return x >> P.s, x & P.m\n    def\
    \ enumerate(P, A, reverse=False): P.ienumerate(A:=list(A), reverse); return A\n\
    \    def ienumerate(P, A, reverse=False):\n        if reverse:\n            for\
    \ i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n            for i,a\
    \ in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]): P.iindices(A:=list(A));\
    \ return A\n    def iindices(P, A):\n        for i,a in enumerate(A): A[i] = P.m&a\n\
    \n\ndef isort_ranged(*L: list, l: int, r: int, reverse=False):\n    n = r - l\n\
    \    order = argsort_ranged(L[0], l, r, reverse=reverse)\n    inv = [0] * n\n\
    \    # order contains indices in range [l, r), need to map to [0, n)\n    for\
    \ i in range(n): inv[order[i]-l] = i\n    for i in range(n):\n        j = order[i]\
    \ - l  # j is in range [0, n)\n        for A in L: A[l+i], A[l+j] = A[l+j], A[l+i]\n\
    \        order[inv[i]], order[inv[j]] = order[inv[j]], order[inv[i]]\n       \
    \ inv[i], inv[j] = inv[j], inv[i]\n    return L\n\nclass view5(Generic[_T1, _T2,\
    \ _T3, _T4, _T5]):\n    __slots__ = 'A1', 'A2', 'A3', 'A4', 'A5', 'l', 'r'\n \
    \   def __init__(V, A1: list[_T1], A2: list[_T2], A3: list[_T3], A4: list[_T4],\
    \ A5: list[_T5], l: int = 0, r: int = 0): \n        V.A1, V.A2, V.A3, V.A4, V.A5,\
    \ V.l, V.r = A1, A2, A3, A4, A5, l, r\n    def __len__(V): return V.r - V.l\n\
    \    def __getitem__(V, i: int): \n        if 0 <= i < V.r - V.l: return V.A1[V.l+i],\
    \ V.A2[V.l+i], V.A3[V.l+i], V.A4[V.l+i], V.A5[V.l+i]\n        else: raise IndexError\n\
    \    def __setitem__(V, i: int, v: tuple[_T1, _T2, _T3, _T4, _T5]): V.A1[V.l+i],\
    \ V.A2[V.l+i], V.A3[V.l+i], V.A4[V.l+i], V.A5[V.l+i] = v\n    def __contains__(V,\
    \ v: tuple[_T1, _T2, _T3, _T4, _T5]): raise NotImplemented\n    def set_range(V,\
    \ l: int, r: int): V.l, V.r = l, r\n    def index(V, v: tuple[_T1, _T2, _T3, _T4,\
    \ _T5]): raise NotImplemented\n    def reverse(V):\n        l, r = V.l, V.r-1\n\
    \        while l < r: \n            V.A1[l], V.A1[r] = V.A1[r], V.A1[l]\n    \
    \        V.A2[l], V.A2[r] = V.A2[r], V.A2[l]\n            V.A3[l], V.A3[r] = V.A3[r],\
    \ V.A3[l]\n            V.A4[l], V.A4[r] = V.A4[r], V.A4[l]\n            V.A5[l],\
    \ V.A5[r] = V.A5[r], V.A5[l]\n            l += 1; r -= 1\n    def sort(V, reverse=False):\
    \ isort_ranged(V.A1, V.A2, V.A3, V.A4, V.A5, l=V.l, r=V.r, reverse=reverse)\n\
    \    def pop(V): V.r -= 1; return V.A1[V.r], V.A2[V.r], V.A3[V.r], V.A4[V.r],\
    \ V.A5[V.r]\n    def append(V, v: tuple[_T1, _T2, _T3, _T4, _T5]): V.A1[V.r],\
    \ V.A2[V.r], V.A3[V.r], V.A4[V.r], V.A5[V.r] = v; V.r += 1\n    def popleft(V):\
    \ V.l += 1; return V.A1[V.l-1], V.A2[V.l-1], V.A3[V.l-1], V.A4[V.l-1], V.A5[V.l-1]\n\
    \    def appendleft(V, v: tuple[_T1, _T2, _T3, _T4, _T5]): V.l -= 1; V.A1[V.l],\
    \ V.A2[V.l], V.A3[V.l], V.A4[V.l], V.A5[V.l] = v\n    def validate(V): return\
    \ 0 <= V.l <= V.r <= len(V.A1)\n\nclass CSR5(Generic[_T1, _T2, _T3, _T4, _T5]):\n\
    \    __slots__ = 'A1', 'A2', 'A3', 'A4', 'A5', 'O'\n    def __init__(csr, A1:\
    \ list[_T1], A2: list[_T2], A3: list[_T3], A4: list[_T4], A5: list[_T5], O: list[int]):\
    \ \n        csr.A1, csr.A2, csr.A3, csr.A4, csr.A5, csr.O = A1, A2, A3, A4, A5,\
    \ O\n    def __len__(csr): return len(csr.O)-1\n    def __getitem__(csr, i: int):\
    \ return view5(csr.A1, csr.A2, csr.A3, csr.A4, csr.A5, csr.O[i], csr.O[i+1])\n\
    \    def __call__(csr, i: int, j: int): ij = csr.O[i]+j; return csr.A1[ij], csr.A2[ij],\
    \ csr.A3[ij], csr.A4[ij], csr.A5[ij]\n    def set(csr, i: int, j: int, v: tuple[_T1,\
    \ _T2, _T3, _T4, _T5]): ij = csr.O[i]+j; csr.A1[ij], csr.A2[ij], csr.A3[ij], csr.A4[ij],\
    \ csr.A5[ij] = v\n    @classmethod\n    def bucketize(cls, N: int, K: list[int],\
    \ V1: list[_T1], V2: list[_T2], V3: list[_T3], V4: list[_T4], V5: list[_T5]):\n\
    \        A1: list[_T1] = [0]*len(K); A2: list[_T2] = [0]*len(K); A3: list[_T3]\
    \ = [0]*len(K); A4: list[_T4] = [0]*len(K); A5: list[_T5] = [0]*len(K); O = [0]*(N+1)\n\
    \        for k in K: O[k] += 1\n        for i in range(N): O[i+1] += O[i]\n  \
    \      for e in range(len(K)): k = K[~e]; O[k] -= 1; A1[O[k]] = V1[~e]; A2[O[k]]\
    \ = V2[~e]; A3[O[k]] = V3[~e]; A4[O[k]] = V4[~e]; A5[O[k]] = V5[~e]\n        return\
    \ cls(A1, A2, A3, A4, A5, O)\n\nif __name__ == '__main__':\n    \"\"\"\n    Helper\
    \ for making unittest files compatible with verification-helper.\n    \n    This\
    \ module provides a helper function to run a dummy Library Checker test\n    so\
    \ that unittest files can be verified by oj-verify.\n    \"\"\"\n    \n    def\
    \ run_verification_helper_unittest():\n        \"\"\"\n        Run a dummy AOJ\
    \ ITP1_1_A test for verification-helper compatibility.\n        \n        This\
    \ function should be called in the __main__ block of unittest files\n        that\
    \ need to be compatible with verification-helper.\n        \n        The function:\n\
    \        1. Prints \"Hello World\" (AOJ ITP1_1_A solution)\n        2. Runs pytest\
    \ for the calling test file\n        3. Exits with the pytest result code\n  \
    \      \"\"\"\n        import sys\n        \n        # Print \"Hello World\" for\
    \ AOJ ITP1_1_A problem\n        print(\"Hello World\")\n        \n        import\
    \ io\n        from contextlib import redirect_stdout, redirect_stderr\n    \n\
    \        # Capture all output during test execution\n        output = io.StringIO()\n\
    \        with redirect_stdout(output), redirect_stderr(output):\n            #\
    \ Get the calling module's file path\n            frame = sys._getframe(1)\n \
    \           test_file = frame.f_globals.get('__file__')\n            if test_file\
    \ is None:\n                test_file = sys.argv[0]\n            result = pytest.main([test_file])\n\
    \        \n        if result != 0: \n            print(output.getvalue())\n  \
    \      sys.exit(result)\n    run_verification_helper_unittest()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A\n\
    \nimport pytest\n\nclass TestCSR5:\n    def test_basic_operations(self):\n   \
    \     \"\"\"Test basic CSR5 operations with 5 attributes\"\"\"\n        K = [0,\
    \ 2]\n        V1 = [1, 0]\n        V2 = [10, 20]\n        V3 = [100, 200]\n  \
    \      V4 = [1000, 2000]\n        V5 = [10000, 20000]\n        \n        csr =\
    \ CSR5.bucketize(3, K, V1, V2, V3, V4, V5)\n        \n        assert len(csr)\
    \ == 3\n        \n        # Node 0\n        assert list(csr[0]) == [(1, 10, 100,\
    \ 1000, 10000)]\n        \n        # Node 1 (empty)\n        assert list(csr[1])\
    \ == []\n        \n        # Node 2\n        assert list(csr[2]) == [(0, 20, 200,\
    \ 2000, 20000)]\n        \n    def test_large_graph(self):\n        \"\"\"Test\
    \ CSR5 with larger graph\"\"\"\n        # Create a star graph: node 0 connected\
    \ to all others\n        n = 5\n        K = []\n        V1, V2, V3, V4, V5 = [],\
    \ [], [], [], []\n        \n        for i in range(1, n):\n            K.append(0)\n\
    \            V1.append(i)\n            V2.append(i * 10)\n            V3.append(i\
    \ * 100)\n            V4.append(i * 1000)\n            V5.append(i * 10000)\n\
    \        \n        csr = CSR5.bucketize(n, K, V1, V2, V3, V4, V5)\n        \n\
    \        # Check node 0 has n-1 neighbors\n        neighbors0 = list(csr[0])\n\
    \        assert len(neighbors0) == n - 1\n        \n        # Check values\n \
    \       for i, neighbor in enumerate(neighbors0):\n            expected = (i+1,\
    \ (i+1)*10, (i+1)*100, (i+1)*1000, (i+1)*10000)\n            assert neighbor ==\
    \ expected\n            \n    def test_direct_access_and_set(self):\n        \"\
    \"\"Test direct access and modification\"\"\"\n        A1 = [1, 2, 3]\n      \
    \  A2 = [10, 20, 30]\n        A3 = [100, 200, 300]\n        A4 = [1000, 2000,\
    \ 3000]\n        A5 = [10000, 20000, 30000]\n        O = [0, 2, 2, 3]\n      \
    \  \n        csr = CSR5(A1, A2, A3, A4, A5, O)\n        \n        # Direct access\n\
    \        assert csr(0, 0) == (1, 10, 100, 1000, 10000)\n        assert csr(0,\
    \ 1) == (2, 20, 200, 2000, 20000)\n        assert csr(2, 0) == (3, 30, 300, 3000,\
    \ 30000)\n        \n        # Set operation\n        csr.set(0, 0, (5, 50, 500,\
    \ 5000, 50000))\n        assert csr(0, 0) == (5, 50, 500, 5000, 50000)\n\nfrom\
    \ cp_library.ds.view.csr5_cls import CSR5\n\nif __name__ == '__main__':\n    from\
    \ cp_library.test.unittest_helper import run_verification_helper_unittest\n  \
    \  run_verification_helper_unittest()"
  dependsOn:
  - cp_library/ds/view/csr5_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/ds/view/view5_cls.py
  - cp_library/alg/iter/sort/isort_ranged_fn.py
  - cp_library/alg/iter/arg/argsort_ranged_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: true
  path: test/unittests/ds/view/csr5_cls_test.py
  requiredBy: []
  timestamp: '2025-07-26 11:14:31+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/view/csr5_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/view/csr5_cls_test.py
- /verify/test/unittests/ds/view/csr5_cls_test.py.html
title: test/unittests/ds/view/csr5_cls_test.py
---
