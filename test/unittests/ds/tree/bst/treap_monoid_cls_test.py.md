---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/masks/i64_max_cnst.py
    title: cp_library/bit/masks/i64_max_cnst.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/reserve_fn.py
    title: cp_library/ds/reserve_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_cls.py
    title: cp_library/ds/tree/bst/bst_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_updates_cls.py
    title: cp_library/ds/tree/bst/bst_updates_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/cartesian_tree_cls.py
    title: cp_library/ds/tree/bst/cartesian_tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_cls.py
    title: cp_library/ds/tree/bst/treap_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/treap_monoid_cls.py
    title: cp_library/ds/tree/bst/treap_monoid_cls.py
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
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\n\n\
    \nclass Packer:\n    __slots__ = 's', 'm'\n    def __init__(P, mx: int): P.s =\
    \ mx.bit_length(); P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int): return\
    \ a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return x >> P.s, x\
    \ & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A), reverse);\
    \ return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n  \
    \          for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n     \
    \       for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\nimport pytest\nimport random\n\nclass TestTreapMonoid:\n\
    \    def test_initialization(self):\n        # Define a simple monoid operation\
    \ (addition)\n        def add_op(a, b):\n            return a + b\n\n        #\
    \ Test basic initialization\n        T = TreapMonoid(add_op, e=0)\n        assert\
    \ T.e == 0\n        assert T.op == add_op\n        assert T.r >= 0\n        assert\
    \ T.all_prod() == 0  # Empty treap should return identity element\n\n    def test_insert_and_get(self):\n\
    \        # Define a simple monoid operation (addition)\n        def add_op(a,\
    \ b):\n            return a + b\n\n        T = TreapMonoid(add_op, e=0)\n    \
    \    \n        # Insert key-value pairs\n        T.insert(5, 10)\n        T.insert(3,\
    \ 20)\n        T.insert(7, 30)\n        \n        # Test getting values\n    \
    \    assert T.get(5) == 10\n        assert T.get(3) == 20\n        assert T.get(7)\
    \ == 30\n        with pytest.raises(KeyError):\n            assert T.get(1) ==\
    \ 0 # Non-existent key\n        \n        # Test __getitem__ for direct key access\n\
    \        assert T[5] == 10\n        assert T[3] == 20\n        assert T[7] ==\
    \ 30\n        with pytest.raises(KeyError):\n            assert T[1] == 0 # Non-existent\
    \ key\n\n    def test_set_and_update(self):\n        def add_op(a, b):\n     \
    \       return a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n     \
    \   # Insert initial values\n        T.insert(5, 10)\n        T.insert(3, 20)\n\
    \        T.insert(7, 30)\n        \n        # Update values\n        T[5] = 15\n\
    \        T.set(3, 25)\n        \n        # Check updated values\n        assert\
    \ T[5] == 15\n        assert T[3] == 25\n        assert T[7] == 30\n        \n\
    \        # Verify all_prod is updated correctly\n        assert T.all_prod() ==\
    \ 15 + 25 + 30\n\n    def test_pop_and_delete(self):\n        def add_op(a, b):\n\
    \            return a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n\
    \        # Insert values\n        T.insert(5, 10)\n        T.insert(3, 20)\n \
    \       T.insert(7, 30)\n        \n        # Test pop\n        assert T.pop(3)\
    \ == 20\n        assert 3 not in T\n        assert T.all_prod() == 10 + 30\n \
    \       \n        # Test __delitem__\n        del T[5]\n        assert 5 not in\
    \ T\n        assert T.all_prod() == 30\n        \n        # Test popping non-existent\
    \ key raises KeyError\n        with pytest.raises(KeyError):\n            T.pop(3)\n\
    \n    def test_prod_range(self):\n        def add_op(a, b):\n            return\
    \ a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n        # Insert sorted\
    \ values\n        for i in range(10):\n            T.insert(i, i * 10)\n     \
    \   \n        # Test range queries\n        assert T.prod(0, 5) == 0 + 10 + 20\
    \ + 30 + 40\n        assert T.prod(3, 7) == 30 + 40 + 50 + 60\n        assert\
    \ T.prod(0, 10) == sum(i * 10 for i in range(10))\n        \n        # Test empty\
    \ range\n        assert T.prod(5, 5) == 0  # Identity element\n        \n    \
    \    # Test __getitem__ with slice\n        assert T[0:5] == 0 + 10 + 20 + 30\
    \ + 40\n        assert T[3:7] == 30 + 40 + 50 + 60\n\n    def test_more_complex_monoid(self):\n\
    \        # Test with a more complex monoid operation (min)\n        def min_op(a,\
    \ b):\n            if a == float('inf') or b == float('inf'):\n              \
    \  return a if b == float('inf') else b\n            return min(a, b)\n\n    \
    \    T = TreapMonoid(min_op, e=float('inf'))\n        \n        # Insert values\n\
    \        values = [(5, 10), (3, 20), (7, 5), (2, 30)]\n        for k, v in values:\n\
    \            T.insert(k, v)\n        \n        # Test min over ranges\n      \
    \  assert T.prod(2, 6) == min(30, 20, 10)  # min of keys 2, 3, 5\n        assert\
    \ T.prod(3, 8) == min(20, 10, 5)   # min of keys 3, 5, 7\n        assert T.all_prod()\
    \ == min(v for _, v in values)\n\n    def test_max_monoid(self):\n        # Test\
    \ with max monoid\n        def max_op(a, b):\n            if a == float('-inf')\
    \ or b == float('-inf'):\n                return a if b == float('-inf') else\
    \ b\n            return max(a, b)\n\n        T = TreapMonoid(max_op, e=float('-inf'))\n\
    \        \n        # Insert values\n        for i in range(10):\n            T.insert(i,\
    \ i * 10)\n        \n        # Test max over ranges\n        assert T.prod(0,\
    \ 5) == 40  # max of 0, 10, 20, 30, 40\n        assert T.prod(5, 10) == 90  #\
    \ max of 50, 60, 70, 80, 90\n        assert T.all_prod() == 90  # max of all values\n\
    \n    def test_sparse_indices(self):\n        def add_op(a, b):\n            return\
    \ a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n        # Insert values\
    \ with large gaps between keys\n        T.insert(10, 5)\n        T.insert(100,\
    \ 10)\n        T.insert(1000, 15)\n        \n        # Check individual values\n\
    \        assert T[10] == 5\n        assert T[100] == 10\n        assert T[1000]\
    \ == 15\n        \n        # Check range queries with sparse indices\n       \
    \ assert T.prod(0, 50) == 5\n        assert T.prod(50, 500) == 10\n        assert\
    \ T.prod(0, 10000) == 5 + 10 + 15\n\n    def test_integrity_after_modifications(self):\n\
    \        def add_op(a, b):\n            return a + b\n\n        T = TreapMonoid(add_op,\
    \ e=0)\n        \n        # Insert initial values\n        for i in range(10):\n\
    \            T.insert(i, i)\n        \n        # Perform a series of modifications\n\
    \        T[3] = 30\n        del T[5]\n        T.insert(11, 11)\n        T.pop(7)\n\
    \        \n        # Verify treap integrity with _v\n        T._v()\n        \n\
    \        # Check values after modifications\n        assert 5 not in T\n     \
    \   assert 7 not in T\n        assert T[3] == 30\n        assert T[11] == 11\n\
    \        \n        # Check all_prod is correctly updated\n        expected_sum\
    \ = sum(i for i in range(10) if i not in [5, 7]) - 3 + 30 + 11\n        assert\
    \ T.all_prod() == expected_sum\n\n    def test_multiple_operations_sequence(self):\n\
    \        def add_op(a, b):\n            return a + b\n\n        T = TreapMonoid(add_op,\
    \ e=0)\n        \n        # Add 100 random key-value pairs\n        random.seed(42)\
    \  # For reproducibility\n        keys = random.sample(range(1000), 100)\n   \
    \     values = [random.randint(1, 100) for _ in range(100)]\n        expected_sum\
    \ = sum(values)\n        \n        for k, v in zip(keys, values):\n          \
    \  T.insert(k, v)\n        \n        # Verify all_prod\n        assert T.all_prod()\
    \ == expected_sum\n        \n        # Delete 20% of the keys\n        to_delete\
    \ = random.sample(keys, 20)\n        expected_sum -= sum(T.get(k) for k in to_delete)\n\
    \        \n        for k in to_delete:\n            del T[k]\n            keys.remove(k)\n\
    \        \n        # Verify all_prod after deletion\n        assert T.all_prod()\
    \ == expected_sum\n        \n        # Update 20% of the remaining keys\n    \
    \    to_update = random.sample(keys, 20)\n        for k in to_update:\n      \
    \      old_val = T[k]\n            new_val = random.randint(1, 100)\n        \
    \    expected_sum = expected_sum - old_val + new_val\n            T[k] = new_val\n\
    \        \n        # Verify all_prod after updates\n        assert T.all_prod()\
    \ == expected_sum\n        \n        # Add new keys\n        new_keys = [k for\
    \ k in range(1000, 1020) if k not in keys]\n        new_values = [random.randint(1,\
    \ 100) for _ in range(len(new_keys))]\n        expected_sum += sum(new_values)\n\
    \        \n        for k, v in zip(new_keys, new_values):\n            T.insert(k,\
    \ v)\n        \n        # Final verification\n        assert T.all_prod() == expected_sum\n\
    \        T._v()\n\n    def test_with_negative_values(self):\n        def add_op(a,\
    \ b):\n            return a + b\n\n        T = TreapMonoid(add_op, e=0)\n    \
    \    \n        # Insert values with negative keys and values\n        T.insert(-5,\
    \ 10)\n        T.insert(3, -20)\n        T.insert(-7, -30)\n        \n       \
    \ # Test getting values\n        assert T[-5] == 10\n        assert T[3] == -20\n\
    \        assert T[-7] == -30\n        \n        # Test range queries with negative\
    \ keys\n        assert T.prod(-10, 0) == 10 + (-30)  # Sum of values at keys -7\
    \ and -5\n        assert T.prod(-10, 10) == 10 + (-30) + (-20)  # Sum of all values\n\
    \n    def test_large_composite_operation(self):\n        mod = 998244353\n   \
    \     P = Packer((1<<30)-1)\n        \n        # Define the composite operation\
    \ from the main function\n        def op(a, b):\n            ac, ad = P.dec(a)\n\
    \            bc, bd = P.dec(b)\n            return P.enc(ac*bc%mod, (ad*bc+bd)%mod)\n\
    \        \n        T = TreapMonoid(op, e=1 << P.s)\n        \n        # Insert\
    \ some values similar to those in the main function\n        for i in range(10):\n\
    \            c, d = random.randint(1, 100), random.randint(1, 100)\n         \
    \   T[i] = P.enc(c, d)\n        \n        # Test range query and composite operation\n\
    \        l, r = 0, 5\n        result = T.prod(l, r)\n        a_res, b_res = P.dec(result)\n\
    \        \n        # Manually compute the expected result\n        a_exp, b_exp\
    \ = 1, 0  # Identity element for this operation\n        for i in range(l, r):\n\
    \            c, d = P.dec(T[i])\n            a_exp = (a_exp * c) % mod\n     \
    \       b_exp = (b_exp * c + d) % mod\n        \n        assert a_res == a_exp\n\
    \        assert b_res == b_exp\n\n    def test_split_basic(self):\n        # Define\
    \ a simple monoid operation (addition)\n        def add_op(a, b):\n          \
    \  return a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n        # Insert\
    \ ordered key-value pairs\n        for i in range(10):\n            T.insert(i,\
    \ i * 10)\n        \n        # Split at key 5\n        S, T = T.split(5)\n   \
    \     \n        # Verify correctness of split\n        # S should contain keys\
    \ [0,1,2,3,4]\n        # T should contain keys [5,6,7,8,9]\n        for i in range(5):\n\
    \            assert i in S\n            assert S[i] == i * 10\n            assert\
    \ i not in T\n            \n        for i in range(5, 10):\n            assert\
    \ i in T\n            assert T[i] == i * 10\n            assert i not in S\n \
    \       \n        # Check monoid values are preserved\n        assert S.all_prod()\
    \ == sum(i * 10 for i in range(5))\n        assert T.all_prod() == sum(i * 10\
    \ for i in range(5, 10))\n\n    def test_split_empty(self):\n        def add_op(a,\
    \ b):\n            return a + b\n\n        T = TreapMonoid(add_op, e=0)\n    \
    \    \n        # Split an empty treap\n        S, T = T.split(5)\n        \n \
    \       # Both treaps should be empty\n        assert S.all_prod() == 0\n    \
    \    assert T.all_prod() == 0\n\n    def test_split_at_edge(self):\n        def\
    \ add_op(a, b):\n            return a + b\n\n        T = TreapMonoid(add_op, e=0)\n\
    \        \n        # Insert key-value pairs\n        for i in range(1, 11):\n\
    \            T.insert(i, i * 10)\n        \n        # Split at minimum key\n \
    \       S, T = T.split(1)\n        \n        # S should be empty, T should have\
    \ all elements\n        assert S.all_prod() == 0\n        assert T.all_prod()\
    \ == sum(i * 10 for i in range(1, 11))\n        \n        # Split at maximum key\
    \ + 1\n        T, R = T.split(11)\n        \n        # T should have all elements,\
    \ R should be empty\n        assert T.all_prod() == sum(i * 10 for i in range(1,\
    \ 11))\n        assert R.all_prod() == 0\n\n    def test_split_and_merge(self):\n\
    \        def add_op(a, b):\n            return a + b\n\n        T = TreapMonoid(add_op,\
    \ e=0)\n        \n        # Insert key-value pairs\n        for i in range(10):\n\
    \            T.insert(i, i * 10)\n        \n        original_sum = T.all_prod()\n\
    \        \n        # Split in the middle\n        S, R = T.split(5)\n        \n\
    \        # Check partial sums\n        assert S.all_prod() + R.all_prod() == original_sum\n\
    \        \n        # Use merge to recombine (this requires implementing _merge\
    \ in Treap class)\n        # Note: This assumes there's an appropriate public\
    \ merge method or we're testing a private method\n        # Since the actual code\
    \ doesn't show a public merge method, we'll implement a test-specific way to merge\n\
    \        \n        # Merge by manually inserting all items from S into R\n   \
    \     for i in range(5):\n            if i in S:\n                R[i] = S[i]\n\
    \        \n        # Check if merged correctly\n        assert R.all_prod() ==\
    \ original_sum\n        \n        # Validate integrity\n        R._v()\n\n   \
    \ def test_multiple_splits(self):\n        def add_op(a, b):\n            return\
    \ a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n        # Insert values\n\
    \        for i in range(20):\n            T.insert(i, i)\n        \n        original_sum\
    \ = T.all_prod()\n        \n        # Perform multiple splits\n        S1, T =\
    \ T.split(10)\n        S2, S1 = S1.split(5)\n        \n        # Check contents\
    \ of each piece\n        for i in range(5):\n            assert i in S2\n    \
    \        assert S2[i] == i\n            \n        for i in range(5, 10):\n   \
    \         assert i in S1\n            assert S1[i] == i\n            \n      \
    \  for i in range(10, 20):\n            assert i in T\n            assert T[i]\
    \ == i\n        \n        # Check sums\n        assert S2.all_prod() + S1.all_prod()\
    \ + T.all_prod() == original_sum\n        \n        # Validate integrity of each\
    \ piece\n        S1._v()\n        S2._v()\n        T._v()\n\n    def test_split_with_complex_monoid(self):\n\
    \        # Test with min operation\n        def min_op(a, b):\n            if\
    \ a == float('inf') or b == float('inf'):\n                return a if b == float('inf')\
    \ else b\n            return min(a, b)\n\n        T = TreapMonoid(min_op, e=float('inf'))\n\
    \        \n        # Insert values\n        values = [(i, 20-i) for i in range(20)]\
    \  # Values decrease as keys increase\n        for k, v in values:\n         \
    \   T.insert(k, v)\n        \n        # Split in the middle\n        S, T = T.split(10)\n\
    \        \n        # Check min values\n        assert S.all_prod() == min(v for\
    \ k, v in values if k < 10)\n        assert T.all_prod() == min(v for k, v in\
    \ values if k >= 10)\n\n    def test_random_split_merge_sequence(self):\n    \
    \    def add_op(a, b):\n            return a + b\n\n        random.seed(42)\n\
    \        T = TreapMonoid(add_op, e=0)\n        \n        # Insert random values\n\
    \        keys = list(range(100))\n        values = [random.randint(1, 100) for\
    \ _ in range(100)]\n        for k, v in zip(keys, values):\n            T.insert(k,\
    \ v)\n        \n        original_sum = T.all_prod()\n        T._v()\n        \n\
    \        # Do a series of random splits and merges\n        treaps = [T]\n   \
    \     split_points = []\n        \n        # Perform 10 random splits\n      \
    \  for _ in range(10):\n            if not treaps:\n                break\n  \
    \              \n            # Choose a treap to split\n            idx = random.randint(0,\
    \ len(treaps)-1)\n            treap = treaps.pop(idx)\n            \n        \
    \    # Find valid split point\n            min_key, max_key = float('inf'), float('-inf')\n\
    \            for k in range(100):\n                if k in treap:\n          \
    \          min_key = min(min_key, k)\n                    max_key = max(max_key,\
    \ k)\n            \n            if min_key == float('inf') or max_key == float('-inf')\
    \ or min_key == max_key:\n                treaps.append(treap)  # Can't split,\
    \ put it back\n                continue\n                \n            split_point\
    \ = random.randint(min_key, max_key)\n            split_points.append(split_point)\n\
    \            \n            # Perform split\n            left, right = treap.split(split_point)\n\
    \            treaps.extend([left, right])\n            \n            # Validate\
    \ each piece\n            for t in [left, right]:\n                t._v()\n  \
    \      \n        # Sum all pieces to ensure we still have all data\n        total_sum\
    \ = sum(t.all_prod() for t in treaps)\n        assert total_sum == original_sum\n\
    \        \n        # Manually merge back by inserting values\n        final_treap\
    \ = TreapMonoid(add_op, e=0)\n        for k, v in zip(keys, values):\n       \
    \     for t in treaps:\n                if k in t:\n                    final_treap[k]\
    \ = v\n                    break\n        \n        assert final_treap.all_prod()\
    \ == original_sum\n        final_treap._v()\n\n    def test_custom_pack_format_with_split(self):\n\
    \        mod = 998244353\n        P = Packer((1<<30)-1)\n        \n        # Define\
    \ composite operation from the main function\n        def op(a, b):\n        \
    \    ac, ad = P.dec(a)\n            bc, bd = P.dec(b)\n            return P.enc(ac*bc%mod,\
    \ (ad*bc+bd)%mod)\n        T = TreapMonoid(op, e=1 << P.s)\n        \n       \
    \ # Insert values with packed format\n        for i in range(10):\n          \
    \  c, d = i+1, i*10\n            T[i] = P.enc(c, d)\n        \n        # Perform\
    \ split\n        S, T = T.split(5)\n        \n        # Verify each part\n   \
    \     for i in range(5):\n            assert i in S\n            c, d = P.dec(S[i])\n\
    \            assert c == i+1\n            assert d == i*10\n            \n   \
    \     for i in range(5, 10):\n            assert i in T\n            c, d = P.dec(T[i])\n\
    \            assert c == i+1\n            assert d == i*10\n\n\n\ndef reserve(A:\
    \ list, est_len: int) -> None: ...\ntry:\n    from __pypy__ import resizelist_hint\n\
    except:\n    def resizelist_hint(A: list, est_len: int):\n        pass\nreserve\
    \ = resizelist_hint\n\n\n\ni64_max = (1<<63)-1\n\nclass BST:\n    __slots__ =\
    \ 'r'\n    K,sub,st=[-1],[-1,-1],[]\n    def __init__(T):T.r=T._nr()\n    def\
    \ _nt(T):return T.__class__()\n    def _nr(T):r=len(T.K);T.K.append(i64_max);T.sub.append(-1);T.sub.append(-1);return\
    \ r\n    def _nn(T,k):n=len(T.K);T.K.append(k);T.sub.append(-1);T.sub.append(-1);return\
    \ n\n    def insert(T,k):T._i(T.r<<1,k,n:=T._nn(k));T._r();return n\n    def get(T,k):\n\
    \        if~(i:=T._f(T.r<<1,k)):return i\n        raise KeyError\n    def pop(T,k):\n\
    \        if ~(i:=T._t(T.r<<1,k)):T._d(i,T.st[-1]);T._r();return i\n        else:T.st.clear();raise\
    \ KeyError\n    def __delitem__(T,k):\n        if~(i:=T._t(T.r<<1,k)):T._d(i,T.st[-1]);T._r()\n\
    \        else:T.st.clear();raise KeyError\n    def __contains__(T,k):return 0<=T._f(T.r<<1,k)\n\
    \    def _f(T,s,k):\n        i = T.sub[s]\n        while~i and T.K[i]!=k:T._p(i);i=T.sub[i<<1|(T.K[i]<k)]\n\
    \        return i\n    def _t(T,s,k):\n        T.st.append(s)\n        while~(i:=T.sub[s])and\
    \ T.K[i]!=k:T._p(i);T.st.append(s:=i<<1|(T.K[i]<k))\n        return i\n    def\
    \ _i(T,s,k,n):\n        T.st.append(s)\n        while ~T.sub[s]:T._p(i:=T.sub[s]);T.st.append(s:=i<<1|(T.K[i]<k))\n\
    \        i,T.sub[s]=T.sub[s],n\n    def _d(T,i,s): raise NotImplemented\n    def\
    \ _r(T):T.st.clear()\n    def _p(T,i): pass\n    @classmethod\n    def reserve(cls,sz):sz+=1;reserve(cls.K,sz);reserve(cls.sub,sz<<1);reserve(cls.st,sz.bit_length()<<1)\n\
    \    def _node_str(T, i): return f\"{T.K[i]}\"\n    def __str__(T):\n        def\
    \ rec(i, pre=\"\", is_right=False):\n            if i == -1: return \"\"\n   \
    \         ret = \"\";T._p(i)\n            if ~(r:=T.sub[i<<1|1]):ret+=rec(r,pre+(\"\
    \   \"if is_right else\"\u2502  \"),True)\n            ret+=pre+(\"\u250C\u2500\
    \ \"if is_right else\"\u2514\u2500 \")+T._node_str(i)+\"\\n\"\n            if\
    \ ~(l:=T.sub[i<<1]):ret+=rec(l,pre+(\"   \"if not is_right else\"\u2502  \"),False)\n\
    \            return ret\n        return rec(T.sub[T.r<<1]).rstrip()\n\nclass BSTUpdates(BST):\n\
    \    def _u(T,i): pass\n    def _r(T):\n        while T.st:T._u(T.st.pop()>>1)\n\
    \nclass CartesianTree(BST):\n    K,P,sub,st=[-1],[42],[-1,-1],[]\n    def _nr(T):T.P.append(-1);return\
    \ super()._nr()\n    def _nn(T,k,p=-1):T.P.append(p);return super()._nn(k)\n \
    \   def get(T,k):return T.P[BST.get(T,k)]\n    def pop(T,k):return T.P[BST.pop(T,k)]\n\
    \    def split(T,k):S=T._nt();T._sp(T.sub[T.r<<1],k,S.r<<1,T.r<<1);T._r();return\
    \ S,T\n    def insert(T,k,p):T._i(T.r<<1,k,n:=T._nn(k,p));T._r();return n\n  \
    \  def __getitem__(T,k):return T.get(k)\n    def _i(T,s,k,n):\n        T.st.append(s)\n\
    \        while~T.sub[s]and T.P[i:=T.sub[s]]<T.P[n]:T._p(i);T.st.append(s:=i<<1|(T.K[i]<k))\n\
    \        i,T.sub[s]=T.sub[s],n\n        if~i:T._sp(i,k,n<<1,n<<1|1)\n    def _sp(T,i,k,l,r):\n\
    \        T.st.append(l)\n        if 1<l^r:T.st.append(r)\n        while~i:\n \
    \           T._p(i)\n            if T.K[i]<k:T.sub[l]=i;i=T.sub[l:=i<<1|1];T.st.append(l)\n\
    \            else:T.sub[r]=i;i=T.sub[r:=i<<1];T.st.append(r)\n        T.sub[l]=T.sub[r]=-1\n\
    \    def _m(T,s,l,r):\n        T.st.append(s)\n        while~l and~r:\n      \
    \      if T.P[l]<T.P[r]:T._p(l);T.sub[s]=l;l=T.sub[s:=l<<1|1]\n            else:T._p(r);T.sub[s]=r;r=T.sub[s:=r<<1]\n\
    \            T.st.append(s)\n        T.sub[s]=l if~l else r\n    def _d(T,i,s):T._p(i);T._m(s,T.sub[i<<1],T.sub[i<<1|1])\n\
    \    @classmethod\n    def reserve(cls,sz):super(CartesianTree,cls).reserve(sz);reserve(cls.P,sz+1)\n\
    \nclass Treap(CartesianTree):\n    __slots__='e'\n    K,V,P,sub,st=[-1],[-1],[42],[-1,-1],[]\n\
    \    def __init__(T,e=-1):T.e=e;super().__init__()\n    def _nt(T):return T.__class__(T.e)\n\
    \    def _nr(T):T.V.append(T.e);return super()._nr()\n    def _nn(T,k,v):T.V.append(v);return\
    \ super()._nn(k,(T.P[-1]*1103515245+12345)&0x7fffffff)\n    def insert(T,k,v):return\
    \ super().insert(k,v)\n    def get(T,k):return T.V[BST.get(T,k)]\n    def pop(T,k):return\
    \ T.V[BST.pop(T,k)]\n    def set(T,k,v):T._s(T.r<<1,k,v);T._r()\n    def __setitem__(T,k,v):T.set(k,v)\n\
    \    def _s(T,s,k,v):\n        if ~(i:=T._t(s,k)):T.V[i]=v;T.st.append(i<<1)\n\
    \        else:\n            n=T._nn(k,v)\n            while T.P[n]<T.P[i:=T.st[-1]>>1]:T._p(T.st.pop())\n\
    \            T._p(i)\n            i,T.sub[s]=T.sub[s:=i<<1|(i!=T.r and T.K[i]<k)],n\n\
    \            if~i:T._sp(i,k,n<<1,n<<1|1)\n    def _node_str(T, i): return f\"\
    {T.K[i]}:{T.V[i]}\"\n    @classmethod\n    def reserve(cls,hint):super(Treap,cls).reserve(hint);reserve(cls.V,hint+1)\n\
    \nclass TreapMonoid(Treap, BSTUpdates):\n    __slots__='op'\n    K,V,A,P,sub,st=[-1],[-1],[-1],[42],[-1,-1],[]\n\
    \    def __init__(T,op,e=-1):T.op=op;super().__init__(e)\n    def _nt(T):return\
    \ T.__class__(T.op,T.e)\n    def _nr(T):T.A.append(T.e);return super()._nr()\n\
    \    def _nn(T,k,v):T.A.append(v);return super()._nn(k, v)\n    def prod(T,l,r):\n\
    \        # find common ancestor\n        a=T.sub[T.r<<1]\n        while~a and\
    \ not l<=T.K[a]<r:T._p(a);a=T.sub[a<<1|(T.K[a]<l)]\n        if a<0:return T.e\n\
    \        # left subtreap\n        ac,i=T.V[a],T.sub[a<<1]\n        while~i:\n\
    \            T._p(i)\n            if not(b:=T.K[i]<l):\n                if~(j:=T.sub[i<<1|1]):ac=T.op(T.A[j],ac)\n\
    \                ac=T.op(T.V[i],ac)\n            i=T.sub[i<<1|b]\n        # right\
    \ subtreap\n        i=T.sub[a<<1|1]\n        while~i:\n            T._p(i)\n \
    \           if b:=T.K[i]<r:\n                if~(j:=T.sub[i<<1]):ac=T.op(ac,T.A[j])\n\
    \                ac=T.op(ac,T.V[i])\n            i=T.sub[i<<1|b]\n        return\
    \ ac\n    def all_prod(T):return T.A[T.r]\n    def __getitem__(T,k):\n       \
    \ if isinstance(k,int):return T.get(k)\n        elif isinstance(k,slice):return\
    \ T.prod(k.start,k.stop)\n    @classmethod\n    def reserve(cls,sz):super(TreapMonoid,cls).reserve(sz);reserve(cls.A,sz+1)\n\
    \    def _u(T,i):\n        T.A[i]=T.V[i]\n        if~(l:=T.sub[i<<1]):T.A[i]=T.op(T.A[l],T.A[i])\n\
    \        if~(r:=T.sub[i<<1|1]):T.A[i]=T.op(T.A[i],T.A[r])\n    def _v(T,i=None):\n\
    \        if i is None:\n            assert T.all_prod() == (ac := T._v(i) if ~(i\
    \ := T.sub[T.r<<1]) else T.e)\n            return ac\n        T._p(i);ac = T.V[i]\n\
    \        if ~(l:=T.sub[i<<1]):\n            assert T.P[i] <= T.P[l]\n        \
    \    assert T.K[l] <= T.K[i]\n            ac = T.op(T._v(l), ac)\n        if ~(r:=T.sub[i<<1|1]):\n\
    \            assert T.P[i] <= T.P[r]\n            assert T.K[i] <= T.K[r]\n  \
    \          ac = T.op(ac, T._v(r))\n        assert T.A[i] == ac\n        return\
    \ ac\n\nif __name__ == '__main__':\n    \"\"\"\n    Helper for making unittest\
    \ files compatible with verification-helper.\n    \n    This module provides a\
    \ helper function to run a dummy Library Checker test\n    so that unittest files\
    \ can be verified by oj-verify.\n    \"\"\"\n    \n    def run_verification_helper_unittest():\n\
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
    \nfrom cp_library.bit.pack.packer_cls import Packer\nimport pytest\nimport random\n\
    \nclass TestTreapMonoid:\n    def test_initialization(self):\n        # Define\
    \ a simple monoid operation (addition)\n        def add_op(a, b):\n          \
    \  return a + b\n\n        # Test basic initialization\n        T = TreapMonoid(add_op,\
    \ e=0)\n        assert T.e == 0\n        assert T.op == add_op\n        assert\
    \ T.r >= 0\n        assert T.all_prod() == 0  # Empty treap should return identity\
    \ element\n\n    def test_insert_and_get(self):\n        # Define a simple monoid\
    \ operation (addition)\n        def add_op(a, b):\n            return a + b\n\n\
    \        T = TreapMonoid(add_op, e=0)\n        \n        # Insert key-value pairs\n\
    \        T.insert(5, 10)\n        T.insert(3, 20)\n        T.insert(7, 30)\n \
    \       \n        # Test getting values\n        assert T.get(5) == 10\n     \
    \   assert T.get(3) == 20\n        assert T.get(7) == 30\n        with pytest.raises(KeyError):\n\
    \            assert T.get(1) == 0 # Non-existent key\n        \n        # Test\
    \ __getitem__ for direct key access\n        assert T[5] == 10\n        assert\
    \ T[3] == 20\n        assert T[7] == 30\n        with pytest.raises(KeyError):\n\
    \            assert T[1] == 0 # Non-existent key\n\n    def test_set_and_update(self):\n\
    \        def add_op(a, b):\n            return a + b\n\n        T = TreapMonoid(add_op,\
    \ e=0)\n        \n        # Insert initial values\n        T.insert(5, 10)\n \
    \       T.insert(3, 20)\n        T.insert(7, 30)\n        \n        # Update values\n\
    \        T[5] = 15\n        T.set(3, 25)\n        \n        # Check updated values\n\
    \        assert T[5] == 15\n        assert T[3] == 25\n        assert T[7] ==\
    \ 30\n        \n        # Verify all_prod is updated correctly\n        assert\
    \ T.all_prod() == 15 + 25 + 30\n\n    def test_pop_and_delete(self):\n       \
    \ def add_op(a, b):\n            return a + b\n\n        T = TreapMonoid(add_op,\
    \ e=0)\n        \n        # Insert values\n        T.insert(5, 10)\n        T.insert(3,\
    \ 20)\n        T.insert(7, 30)\n        \n        # Test pop\n        assert T.pop(3)\
    \ == 20\n        assert 3 not in T\n        assert T.all_prod() == 10 + 30\n \
    \       \n        # Test __delitem__\n        del T[5]\n        assert 5 not in\
    \ T\n        assert T.all_prod() == 30\n        \n        # Test popping non-existent\
    \ key raises KeyError\n        with pytest.raises(KeyError):\n            T.pop(3)\n\
    \n    def test_prod_range(self):\n        def add_op(a, b):\n            return\
    \ a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n        # Insert sorted\
    \ values\n        for i in range(10):\n            T.insert(i, i * 10)\n     \
    \   \n        # Test range queries\n        assert T.prod(0, 5) == 0 + 10 + 20\
    \ + 30 + 40\n        assert T.prod(3, 7) == 30 + 40 + 50 + 60\n        assert\
    \ T.prod(0, 10) == sum(i * 10 for i in range(10))\n        \n        # Test empty\
    \ range\n        assert T.prod(5, 5) == 0  # Identity element\n        \n    \
    \    # Test __getitem__ with slice\n        assert T[0:5] == 0 + 10 + 20 + 30\
    \ + 40\n        assert T[3:7] == 30 + 40 + 50 + 60\n\n    def test_more_complex_monoid(self):\n\
    \        # Test with a more complex monoid operation (min)\n        def min_op(a,\
    \ b):\n            if a == float('inf') or b == float('inf'):\n              \
    \  return a if b == float('inf') else b\n            return min(a, b)\n\n    \
    \    T = TreapMonoid(min_op, e=float('inf'))\n        \n        # Insert values\n\
    \        values = [(5, 10), (3, 20), (7, 5), (2, 30)]\n        for k, v in values:\n\
    \            T.insert(k, v)\n        \n        # Test min over ranges\n      \
    \  assert T.prod(2, 6) == min(30, 20, 10)  # min of keys 2, 3, 5\n        assert\
    \ T.prod(3, 8) == min(20, 10, 5)   # min of keys 3, 5, 7\n        assert T.all_prod()\
    \ == min(v for _, v in values)\n\n    def test_max_monoid(self):\n        # Test\
    \ with max monoid\n        def max_op(a, b):\n            if a == float('-inf')\
    \ or b == float('-inf'):\n                return a if b == float('-inf') else\
    \ b\n            return max(a, b)\n\n        T = TreapMonoid(max_op, e=float('-inf'))\n\
    \        \n        # Insert values\n        for i in range(10):\n            T.insert(i,\
    \ i * 10)\n        \n        # Test max over ranges\n        assert T.prod(0,\
    \ 5) == 40  # max of 0, 10, 20, 30, 40\n        assert T.prod(5, 10) == 90  #\
    \ max of 50, 60, 70, 80, 90\n        assert T.all_prod() == 90  # max of all values\n\
    \n    def test_sparse_indices(self):\n        def add_op(a, b):\n            return\
    \ a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n        # Insert values\
    \ with large gaps between keys\n        T.insert(10, 5)\n        T.insert(100,\
    \ 10)\n        T.insert(1000, 15)\n        \n        # Check individual values\n\
    \        assert T[10] == 5\n        assert T[100] == 10\n        assert T[1000]\
    \ == 15\n        \n        # Check range queries with sparse indices\n       \
    \ assert T.prod(0, 50) == 5\n        assert T.prod(50, 500) == 10\n        assert\
    \ T.prod(0, 10000) == 5 + 10 + 15\n\n    def test_integrity_after_modifications(self):\n\
    \        def add_op(a, b):\n            return a + b\n\n        T = TreapMonoid(add_op,\
    \ e=0)\n        \n        # Insert initial values\n        for i in range(10):\n\
    \            T.insert(i, i)\n        \n        # Perform a series of modifications\n\
    \        T[3] = 30\n        del T[5]\n        T.insert(11, 11)\n        T.pop(7)\n\
    \        \n        # Verify treap integrity with _v\n        T._v()\n        \n\
    \        # Check values after modifications\n        assert 5 not in T\n     \
    \   assert 7 not in T\n        assert T[3] == 30\n        assert T[11] == 11\n\
    \        \n        # Check all_prod is correctly updated\n        expected_sum\
    \ = sum(i for i in range(10) if i not in [5, 7]) - 3 + 30 + 11\n        assert\
    \ T.all_prod() == expected_sum\n\n    def test_multiple_operations_sequence(self):\n\
    \        def add_op(a, b):\n            return a + b\n\n        T = TreapMonoid(add_op,\
    \ e=0)\n        \n        # Add 100 random key-value pairs\n        random.seed(42)\
    \  # For reproducibility\n        keys = random.sample(range(1000), 100)\n   \
    \     values = [random.randint(1, 100) for _ in range(100)]\n        expected_sum\
    \ = sum(values)\n        \n        for k, v in zip(keys, values):\n          \
    \  T.insert(k, v)\n        \n        # Verify all_prod\n        assert T.all_prod()\
    \ == expected_sum\n        \n        # Delete 20% of the keys\n        to_delete\
    \ = random.sample(keys, 20)\n        expected_sum -= sum(T.get(k) for k in to_delete)\n\
    \        \n        for k in to_delete:\n            del T[k]\n            keys.remove(k)\n\
    \        \n        # Verify all_prod after deletion\n        assert T.all_prod()\
    \ == expected_sum\n        \n        # Update 20% of the remaining keys\n    \
    \    to_update = random.sample(keys, 20)\n        for k in to_update:\n      \
    \      old_val = T[k]\n            new_val = random.randint(1, 100)\n        \
    \    expected_sum = expected_sum - old_val + new_val\n            T[k] = new_val\n\
    \        \n        # Verify all_prod after updates\n        assert T.all_prod()\
    \ == expected_sum\n        \n        # Add new keys\n        new_keys = [k for\
    \ k in range(1000, 1020) if k not in keys]\n        new_values = [random.randint(1,\
    \ 100) for _ in range(len(new_keys))]\n        expected_sum += sum(new_values)\n\
    \        \n        for k, v in zip(new_keys, new_values):\n            T.insert(k,\
    \ v)\n        \n        # Final verification\n        assert T.all_prod() == expected_sum\n\
    \        T._v()\n\n    def test_with_negative_values(self):\n        def add_op(a,\
    \ b):\n            return a + b\n\n        T = TreapMonoid(add_op, e=0)\n    \
    \    \n        # Insert values with negative keys and values\n        T.insert(-5,\
    \ 10)\n        T.insert(3, -20)\n        T.insert(-7, -30)\n        \n       \
    \ # Test getting values\n        assert T[-5] == 10\n        assert T[3] == -20\n\
    \        assert T[-7] == -30\n        \n        # Test range queries with negative\
    \ keys\n        assert T.prod(-10, 0) == 10 + (-30)  # Sum of values at keys -7\
    \ and -5\n        assert T.prod(-10, 10) == 10 + (-30) + (-20)  # Sum of all values\n\
    \n    def test_large_composite_operation(self):\n        mod = 998244353\n   \
    \     P = Packer((1<<30)-1)\n        \n        # Define the composite operation\
    \ from the main function\n        def op(a, b):\n            ac, ad = P.dec(a)\n\
    \            bc, bd = P.dec(b)\n            return P.enc(ac*bc%mod, (ad*bc+bd)%mod)\n\
    \        \n        T = TreapMonoid(op, e=1 << P.s)\n        \n        # Insert\
    \ some values similar to those in the main function\n        for i in range(10):\n\
    \            c, d = random.randint(1, 100), random.randint(1, 100)\n         \
    \   T[i] = P.enc(c, d)\n        \n        # Test range query and composite operation\n\
    \        l, r = 0, 5\n        result = T.prod(l, r)\n        a_res, b_res = P.dec(result)\n\
    \        \n        # Manually compute the expected result\n        a_exp, b_exp\
    \ = 1, 0  # Identity element for this operation\n        for i in range(l, r):\n\
    \            c, d = P.dec(T[i])\n            a_exp = (a_exp * c) % mod\n     \
    \       b_exp = (b_exp * c + d) % mod\n        \n        assert a_res == a_exp\n\
    \        assert b_res == b_exp\n\n    def test_split_basic(self):\n        # Define\
    \ a simple monoid operation (addition)\n        def add_op(a, b):\n          \
    \  return a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n        # Insert\
    \ ordered key-value pairs\n        for i in range(10):\n            T.insert(i,\
    \ i * 10)\n        \n        # Split at key 5\n        S, T = T.split(5)\n   \
    \     \n        # Verify correctness of split\n        # S should contain keys\
    \ [0,1,2,3,4]\n        # T should contain keys [5,6,7,8,9]\n        for i in range(5):\n\
    \            assert i in S\n            assert S[i] == i * 10\n            assert\
    \ i not in T\n            \n        for i in range(5, 10):\n            assert\
    \ i in T\n            assert T[i] == i * 10\n            assert i not in S\n \
    \       \n        # Check monoid values are preserved\n        assert S.all_prod()\
    \ == sum(i * 10 for i in range(5))\n        assert T.all_prod() == sum(i * 10\
    \ for i in range(5, 10))\n\n    def test_split_empty(self):\n        def add_op(a,\
    \ b):\n            return a + b\n\n        T = TreapMonoid(add_op, e=0)\n    \
    \    \n        # Split an empty treap\n        S, T = T.split(5)\n        \n \
    \       # Both treaps should be empty\n        assert S.all_prod() == 0\n    \
    \    assert T.all_prod() == 0\n\n    def test_split_at_edge(self):\n        def\
    \ add_op(a, b):\n            return a + b\n\n        T = TreapMonoid(add_op, e=0)\n\
    \        \n        # Insert key-value pairs\n        for i in range(1, 11):\n\
    \            T.insert(i, i * 10)\n        \n        # Split at minimum key\n \
    \       S, T = T.split(1)\n        \n        # S should be empty, T should have\
    \ all elements\n        assert S.all_prod() == 0\n        assert T.all_prod()\
    \ == sum(i * 10 for i in range(1, 11))\n        \n        # Split at maximum key\
    \ + 1\n        T, R = T.split(11)\n        \n        # T should have all elements,\
    \ R should be empty\n        assert T.all_prod() == sum(i * 10 for i in range(1,\
    \ 11))\n        assert R.all_prod() == 0\n\n    def test_split_and_merge(self):\n\
    \        def add_op(a, b):\n            return a + b\n\n        T = TreapMonoid(add_op,\
    \ e=0)\n        \n        # Insert key-value pairs\n        for i in range(10):\n\
    \            T.insert(i, i * 10)\n        \n        original_sum = T.all_prod()\n\
    \        \n        # Split in the middle\n        S, R = T.split(5)\n        \n\
    \        # Check partial sums\n        assert S.all_prod() + R.all_prod() == original_sum\n\
    \        \n        # Use merge to recombine (this requires implementing _merge\
    \ in Treap class)\n        # Note: This assumes there's an appropriate public\
    \ merge method or we're testing a private method\n        # Since the actual code\
    \ doesn't show a public merge method, we'll implement a test-specific way to merge\n\
    \        \n        # Merge by manually inserting all items from S into R\n   \
    \     for i in range(5):\n            if i in S:\n                R[i] = S[i]\n\
    \        \n        # Check if merged correctly\n        assert R.all_prod() ==\
    \ original_sum\n        \n        # Validate integrity\n        R._v()\n\n   \
    \ def test_multiple_splits(self):\n        def add_op(a, b):\n            return\
    \ a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n        # Insert values\n\
    \        for i in range(20):\n            T.insert(i, i)\n        \n        original_sum\
    \ = T.all_prod()\n        \n        # Perform multiple splits\n        S1, T =\
    \ T.split(10)\n        S2, S1 = S1.split(5)\n        \n        # Check contents\
    \ of each piece\n        for i in range(5):\n            assert i in S2\n    \
    \        assert S2[i] == i\n            \n        for i in range(5, 10):\n   \
    \         assert i in S1\n            assert S1[i] == i\n            \n      \
    \  for i in range(10, 20):\n            assert i in T\n            assert T[i]\
    \ == i\n        \n        # Check sums\n        assert S2.all_prod() + S1.all_prod()\
    \ + T.all_prod() == original_sum\n        \n        # Validate integrity of each\
    \ piece\n        S1._v()\n        S2._v()\n        T._v()\n\n    def test_split_with_complex_monoid(self):\n\
    \        # Test with min operation\n        def min_op(a, b):\n            if\
    \ a == float('inf') or b == float('inf'):\n                return a if b == float('inf')\
    \ else b\n            return min(a, b)\n\n        T = TreapMonoid(min_op, e=float('inf'))\n\
    \        \n        # Insert values\n        values = [(i, 20-i) for i in range(20)]\
    \  # Values decrease as keys increase\n        for k, v in values:\n         \
    \   T.insert(k, v)\n        \n        # Split in the middle\n        S, T = T.split(10)\n\
    \        \n        # Check min values\n        assert S.all_prod() == min(v for\
    \ k, v in values if k < 10)\n        assert T.all_prod() == min(v for k, v in\
    \ values if k >= 10)\n\n    def test_random_split_merge_sequence(self):\n    \
    \    def add_op(a, b):\n            return a + b\n\n        random.seed(42)\n\
    \        T = TreapMonoid(add_op, e=0)\n        \n        # Insert random values\n\
    \        keys = list(range(100))\n        values = [random.randint(1, 100) for\
    \ _ in range(100)]\n        for k, v in zip(keys, values):\n            T.insert(k,\
    \ v)\n        \n        original_sum = T.all_prod()\n        T._v()\n        \n\
    \        # Do a series of random splits and merges\n        treaps = [T]\n   \
    \     split_points = []\n        \n        # Perform 10 random splits\n      \
    \  for _ in range(10):\n            if not treaps:\n                break\n  \
    \              \n            # Choose a treap to split\n            idx = random.randint(0,\
    \ len(treaps)-1)\n            treap = treaps.pop(idx)\n            \n        \
    \    # Find valid split point\n            min_key, max_key = float('inf'), float('-inf')\n\
    \            for k in range(100):\n                if k in treap:\n          \
    \          min_key = min(min_key, k)\n                    max_key = max(max_key,\
    \ k)\n            \n            if min_key == float('inf') or max_key == float('-inf')\
    \ or min_key == max_key:\n                treaps.append(treap)  # Can't split,\
    \ put it back\n                continue\n                \n            split_point\
    \ = random.randint(min_key, max_key)\n            split_points.append(split_point)\n\
    \            \n            # Perform split\n            left, right = treap.split(split_point)\n\
    \            treaps.extend([left, right])\n            \n            # Validate\
    \ each piece\n            for t in [left, right]:\n                t._v()\n  \
    \      \n        # Sum all pieces to ensure we still have all data\n        total_sum\
    \ = sum(t.all_prod() for t in treaps)\n        assert total_sum == original_sum\n\
    \        \n        # Manually merge back by inserting values\n        final_treap\
    \ = TreapMonoid(add_op, e=0)\n        for k, v in zip(keys, values):\n       \
    \     for t in treaps:\n                if k in t:\n                    final_treap[k]\
    \ = v\n                    break\n        \n        assert final_treap.all_prod()\
    \ == original_sum\n        final_treap._v()\n\n    def test_custom_pack_format_with_split(self):\n\
    \        mod = 998244353\n        P = Packer((1<<30)-1)\n        \n        # Define\
    \ composite operation from the main function\n        def op(a, b):\n        \
    \    ac, ad = P.dec(a)\n            bc, bd = P.dec(b)\n            return P.enc(ac*bc%mod,\
    \ (ad*bc+bd)%mod)\n        T = TreapMonoid(op, e=1 << P.s)\n        \n       \
    \ # Insert values with packed format\n        for i in range(10):\n          \
    \  c, d = i+1, i*10\n            T[i] = P.enc(c, d)\n        \n        # Perform\
    \ split\n        S, T = T.split(5)\n        \n        # Verify each part\n   \
    \     for i in range(5):\n            assert i in S\n            c, d = P.dec(S[i])\n\
    \            assert c == i+1\n            assert d == i*10\n            \n   \
    \     for i in range(5, 10):\n            assert i in T\n            c, d = P.dec(T[i])\n\
    \            assert c == i+1\n            assert d == i*10\n\nfrom cp_library.ds.tree.bst.treap_monoid_cls\
    \ import TreapMonoid\n\nif __name__ == '__main__':\n    from cp_library.test.unittest_helper\
    \ import run_verification_helper_unittest\n    run_verification_helper_unittest()"
  dependsOn:
  - cp_library/bit/pack/packer_cls.py
  - cp_library/ds/tree/bst/treap_monoid_cls.py
  - cp_library/test/unittest_helper.py
  - cp_library/ds/reserve_fn.py
  - cp_library/ds/tree/bst/bst_updates_cls.py
  - cp_library/ds/tree/bst/treap_cls.py
  - cp_library/ds/tree/bst/bst_cls.py
  - cp_library/ds/tree/bst/cartesian_tree_cls.py
  - cp_library/bit/masks/i64_max_cnst.py
  isVerificationFile: true
  path: test/unittests/ds/tree/bst/treap_monoid_cls_test.py
  requiredBy: []
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/tree/bst/treap_monoid_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/tree/bst/treap_monoid_cls_test.py
- /verify/test/unittests/ds/tree/bst/treap_monoid_cls_test.py.html
title: test/unittests/ds/tree/bst/treap_monoid_cls_test.py
---
