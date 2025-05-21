---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack_sm_fn.py
    title: cp_library/bit/pack_sm_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/reserve_fn.py
    title: cp_library/ds/reserve_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bst/bst_cls.py
    title: cp_library/ds/tree/bst/bst_cls.py
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
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_fn.py
    title: cp_library/io/read_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/aplusb
    links:
    - https://judge.yosupo.jp/problem/aplusb
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\ndef\
    \ pack_sm(N: int): s=N.bit_length(); return s, (1<<s)-1\ndef pack_enc(a: int,\
    \ b: int, s: int): return a<<s|b\ndef pack_dec(ab: int, s: int, m: int): return\
    \ ab>>s,ab&m\ndef pack_indices(A, s): return [a<<s|i for i,a in enumerate(A)]\n\
    import pytest\nimport random\n\nclass TestTreapMonoid:\n    def test_initialization(self):\n\
    \        # Define a simple monoid operation (addition)\n        def add_op(a,\
    \ b):\n            return a + b\n\n        # Test basic initialization\n     \
    \   T = TreapMonoid(add_op, e=0)\n        assert T.e == 0\n        assert T.op\
    \ == add_op\n        assert T.root >= 0\n        assert T.all_prod() == 0  # Empty\
    \ treap should return identity element\n\n    def test_insert_and_get(self):\n\
    \        # Define a simple monoid operation (addition)\n        def add_op(a,\
    \ b):\n            return a + b\n\n        T = TreapMonoid(add_op, e=0)\n    \
    \    \n        # Insert key-value pairs\n        T.insert(5, 10)\n        T.insert(3,\
    \ 20)\n        T.insert(7, 30)\n        \n        # Test getting values\n    \
    \    assert T.get(5) == 10\n        assert T.get(3) == 20\n        assert T.get(7)\
    \ == 30\n        assert T.get(1) == 0  # Non-existent key should return identity\n\
    \        \n        # Test __getitem__ for direct key access\n        assert T[5]\
    \ == 10\n        assert T[3] == 20\n        assert T[7] == 30\n        assert\
    \ T[1] == 0\n\n    def test_set_and_update(self):\n        def add_op(a, b):\n\
    \            return a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n\
    \        # Insert initial values\n        T.insert(5, 10)\n        T.insert(3,\
    \ 20)\n        T.insert(7, 30)\n        \n        # Update values\n        T[5]\
    \ = 15\n        T.set(3, 25)\n        \n        # Check updated values\n     \
    \   assert T[5] == 15\n        assert T[3] == 25\n        assert T[7] == 30\n\
    \        \n        # Verify all_prod is updated correctly\n        assert T.all_prod()\
    \ == 15 + 25 + 30\n\n    def test_pop_and_delete(self):\n        def add_op(a,\
    \ b):\n            return a + b\n\n        T = TreapMonoid(add_op, e=0)\n    \
    \    \n        # Insert values\n        T.insert(5, 10)\n        T.insert(3, 20)\n\
    \        T.insert(7, 30)\n        \n        # Test pop\n        assert T.pop(3)\
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
    \        \n        # Verify treap integrity with _validate\n        T._validate()\n\
    \        \n        # Check values after modifications\n        assert 5 not in\
    \ T\n        assert 7 not in T\n        assert T[3] == 30\n        assert T[11]\
    \ == 11\n        \n        # Check all_prod is correctly updated\n        expected_sum\
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
    \        T._validate()\n\n    def test_with_negative_values(self):\n        def\
    \ add_op(a, b):\n            return a + b\n\n        T = TreapMonoid(add_op, e=0)\n\
    \        \n        # Insert values with negative keys and values\n        T.insert(-5,\
    \ 10)\n        T.insert(3, -20)\n        T.insert(-7, -30)\n        \n       \
    \ # Test getting values\n        assert T[-5] == 10\n        assert T[3] == -20\n\
    \        assert T[-7] == -30\n        \n        # Test range queries with negative\
    \ keys\n        assert T.prod(-10, 0) == 10 + (-30)  # Sum of values at keys -7\
    \ and -5\n        assert T.prod(-10, 10) == 10 + (-30) + (-20)  # Sum of all values\n\
    \n    def test_pack_enc_dec(self):\n        # Test the pack_enc and pack_dec utility\
    \ functions used in the original code\n        shift, mask = 30, (1<<30)-1\n \
    \       \n        a, b = 123, 456\n        packed = pack_enc(a, b, shift)\n  \
    \      \n        # Verify pack_dec correctly extracts values\n        a_dec, b_dec\
    \ = pack_dec(packed, shift, mask)\n        assert a_dec == a\n        assert b_dec\
    \ == b\n\n    def test_large_composite_operation(self):\n        mod = 998244353\n\
    \        shift, mask = 30, (1<<30)-1\n        \n        # Define the composite\
    \ operation from the main function\n        def op(a, b):\n            ac, ad\
    \ = pack_dec(a, shift, mask)\n            bc, bd = pack_dec(b, shift, mask)\n\
    \            return pack_enc(ac*bc%mod, (ad*bc+bd)%mod, shift)\n        \n   \
    \     T = TreapMonoid(op, e=1 << shift)\n        \n        # Insert some values\
    \ similar to those in the main function\n        for i in range(10):\n       \
    \     c, d = random.randint(1, 100), random.randint(1, 100)\n            T[i]\
    \ = pack_enc(c, d, shift)\n        \n        # Test range query and composite\
    \ operation\n        l, r = 0, 5\n        result = T.prod(l, r)\n        a_res,\
    \ b_res = pack_dec(result, shift, mask)\n        \n        # Manually compute\
    \ the expected result\n        a_exp, b_exp = 1, 0  # Identity element for this\
    \ operation\n        for i in range(l, r):\n            c, d = pack_dec(T[i],\
    \ shift, mask)\n            a_exp = (a_exp * c) % mod\n            b_exp = (b_exp\
    \ * c + d) % mod\n        \n        assert a_res == a_exp\n        assert b_res\
    \ == b_exp\n\n    def test_split_basic(self):\n        # Define a simple monoid\
    \ operation (addition)\n        def add_op(a, b):\n            return a + b\n\n\
    \        T = TreapMonoid(add_op, e=0)\n        \n        # Insert ordered key-value\
    \ pairs\n        for i in range(10):\n            T.insert(i, i * 10)\n      \
    \  \n        # Split at key 5\n        S, T = T.split(5)\n        \n        #\
    \ Verify correctness of split\n        # S should contain keys [0,1,2,3,4]\n \
    \       # T should contain keys [5,6,7,8,9]\n        for i in range(5):\n    \
    \        assert i in S\n            assert S[i] == i * 10\n            assert\
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
    \ original_sum\n        \n        # Validate integrity\n        R._validate()\n\
    \n    def test_multiple_splits(self):\n        def add_op(a, b):\n           \
    \ return a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n        # Insert\
    \ values\n        for i in range(20):\n            T.insert(i, i)\n        \n\
    \        original_sum = T.all_prod()\n        \n        # Perform multiple splits\n\
    \        S1, T = T.split(10)\n        S2, S1 = S1.split(5)\n        \n       \
    \ # Check contents of each piece\n        for i in range(5):\n            assert\
    \ i in S2\n            assert S2[i] == i\n            \n        for i in range(5,\
    \ 10):\n            assert i in S1\n            assert S1[i] == i\n          \
    \  \n        for i in range(10, 20):\n            assert i in T\n            assert\
    \ T[i] == i\n        \n        # Check sums\n        assert S2.all_prod() + S1.all_prod()\
    \ + T.all_prod() == original_sum\n        \n        # Validate integrity of each\
    \ piece\n        S1._validate()\n        S2._validate()\n        T._validate()\n\
    \n    def test_split_with_complex_monoid(self):\n        # Test with min operation\n\
    \        def min_op(a, b):\n            if a == float('inf') or b == float('inf'):\n\
    \                return a if b == float('inf') else b\n            return min(a,\
    \ b)\n\n        T = TreapMonoid(min_op, e=float('inf'))\n        \n        # Insert\
    \ values\n        values = [(i, 20-i) for i in range(20)]  # Values decrease as\
    \ keys increase\n        for k, v in values:\n            T.insert(k, v)\n   \
    \     \n        # Split in the middle\n        S, T = T.split(10)\n        \n\
    \        # Check min values\n        assert S.all_prod() == min(v for k, v in\
    \ values if k < 10)\n        assert T.all_prod() == min(v for k, v in values if\
    \ k >= 10)\n\n    def test_random_split_merge_sequence(self):\n        def add_op(a,\
    \ b):\n            return a + b\n\n        random.seed(42)\n        T = TreapMonoid(add_op,\
    \ e=0)\n        \n        # Insert random values\n        keys = list(range(100))\n\
    \        values = [random.randint(1, 100) for _ in range(100)]\n        for k,\
    \ v in zip(keys, values):\n            T.insert(k, v)\n        \n        original_sum\
    \ = T.all_prod()\n        T._validate()\n        \n        # Do a series of random\
    \ splits and merges\n        treaps = [T]\n        split_points = []\n       \
    \ \n        # Perform 10 random splits\n        for _ in range(10):\n        \
    \    if not treaps:\n                break\n                \n            # Choose\
    \ a treap to split\n            idx = random.randint(0, len(treaps)-1)\n     \
    \       treap = treaps.pop(idx)\n            \n            # Find valid split\
    \ point\n            min_key, max_key = float('inf'), float('-inf')\n        \
    \    for k in range(100):\n                if k in treap:\n                  \
    \  min_key = min(min_key, k)\n                    max_key = max(max_key, k)\n\
    \            \n            if min_key == float('inf') or max_key == float('-inf')\
    \ or min_key == max_key:\n                treaps.append(treap)  # Can't split,\
    \ put it back\n                continue\n                \n            split_point\
    \ = random.randint(min_key, max_key)\n            split_points.append(split_point)\n\
    \            \n            # Perform split\n            left, right = treap.split(split_point)\n\
    \            treaps.extend([left, right])\n            \n            # Validate\
    \ each piece\n            for t in [left, right]:\n                t._validate()\n\
    \        \n        # Sum all pieces to ensure we still have all data\n       \
    \ total_sum = sum(t.all_prod() for t in treaps)\n        assert total_sum == original_sum\n\
    \        \n        # Manually merge back by inserting values\n        final_treap\
    \ = TreapMonoid(add_op, e=0)\n        for k, v in zip(keys, values):\n       \
    \     for t in treaps:\n                if k in t:\n                    final_treap[k]\
    \ = v\n                    break\n        \n        assert final_treap.all_prod()\
    \ == original_sum\n        final_treap._validate()\n\n    def test_custom_pack_format_with_split(self):\n\
    \        mod = 998244353\n        shift, mask = 30, (1<<30)-1\n        \n    \
    \    # Define composite operation from the main function\n        def op(a, b):\n\
    \            ac, ad = pack_dec(a, shift, mask)\n            bc, bd = pack_dec(b,\
    \ shift, mask)\n            return pack_enc(ac*bc%mod, (ad*bc+bd)%mod, shift)\n\
    \        \n        T = TreapMonoid(op, e=1 << shift)\n        \n        # Insert\
    \ values with packed format\n        for i in range(10):\n            c, d = i+1,\
    \ i*10\n            T[i] = pack_enc(c, d, shift)\n        \n        # Perform\
    \ split\n        S, T = T.split(5)\n        \n        # Verify each part\n   \
    \     for i in range(5):\n            assert i in S\n            c, d = pack_dec(S[i],\
    \ shift, mask)\n            assert c == i+1\n            assert d == i*10\n  \
    \          \n        for i in range(5, 10):\n            assert i in T\n     \
    \       c, d = pack_dec(T[i], shift, mask)\n            assert c == i+1\n    \
    \        assert d == i*10\n\n\n\ndef reserve(A: list, est_len: int) -> None: ...\n\
    try:\n    from __pypy__ import resizelist_hint\nexcept:\n    def resizelist_hint(A:\
    \ list, est_len: int):\n        pass\nreserve = resizelist_hint\n\n\n\nclass BST:\n\
    \    __slots__ = 'root'\n    K, sub, st = [-1], [-1, -1], []\n\n    def __init__(T):\
    \ T.root = T._new_node(-1)\n\n    def _new_tree(T): return T.__class__()\n\n \
    \   def _new_node(T, key):\n        id = len(T.K); T.K.append(key); T.sub.append(-1);\
    \ T.sub.append(-1)\n        return id\n\n    def insert(T, key):\n        T.st.append(T.root);\
    \ T._insert(T.root<<1, nid := T._new_node(key)); T._repair()\n        return nid\n\
    \n    def pop(T, key):\n        if ~(id:=T._trace(key)): T._del(id); T._repair();\
    \ return id\n        else: T.st.clear(); raise KeyError\n\n    def __delitem__(T,\
    \ key):\n        if ~(id:=T._trace(key)): T._del(id); T._repair()\n        else:\
    \ T.st.clear(); raise KeyError\n\n    def __contains__(T, key): return 0 <= T._find(key)\n\
    \n    def _find(T, key):\n        id = T.sub[T.root<<1]\n        while ~id and\
    \ T.K[id] != key: id = T.sub[id<<1|(T.K[id]<key)]\n        return id\n\n    def\
    \ _trace(T, key):\n        id = T.sub[T.root<<1]; T.st.append(T.root)\n      \
    \  while ~id and T.K[id] != key: T.st.append(id); id = T.sub[id<<1|(T.K[id]<key)]\n\
    \        return id\n\n    def _insert(T, sid, nid):\n        while ~T.sub[sid]:\
    \ T.st.append(id:=T.sub[sid]); sid=id<<1|(T.K[id]<T.K[nid])\n        id, T.sub[sid]\
    \ = T.sub[sid], nid\n\n    def _del(T, id): raise NotImplemented\n\n    def _repair(T):\
    \ T.st.clear()\n\n    @classmethod\n    def reserve(cls, hint: int):\n       \
    \ hint += 1\n        reserve(cls.K, hint); reserve(cls.sub, hint << 1); reserve(cls.st,\
    \ hint.bit_length() << 1)\n\nclass CartesianTree(BST):\n    K, P, sub, st = [-1],\
    \ [42], [-1, -1], []\n\n    def _new_node(T, key, prior = -1): T.P.append(prior);\
    \ return super()._new_node(key)\n\n    def get(T, key):\n        if ~(id:=T._find(key)):\
    \ return T.P[id]\n        raise KeyError\n\n    def split(T, key):\n        S\
    \ = T._new_tree(); T.st.append(T.root); T.st.append(S.root); \n        T._split(T.sub[T.root<<1],\
    \ key, S.root<<1, T.root<<1); T._repair()\n        return S, T\n\n    def insert(T,\
    \ key, prior):\n        T.st.append(T.root); T._insert(T.root<<1, nid := T._new_node(key,\
    \ prior)); T._repair()\n        return nid\n\n    def pop(T, key): return T.P[super().pop(key)]\n\
    \n    def __getitem__(T, key): return T.get(key)\n\n    def _insert(T, sid, nid):\n\
    \        while ~T.sub[sid] and T.P[id:=T.sub[sid]]<T.P[nid]: T.st.append(id);\
    \ sid=id<<1|(T.K[id]<T.K[nid])\n        id, T.sub[sid] = T.sub[sid], nid\n   \
    \     if ~id: T.st.append(nid); T._split(id, T.K[nid], nid<<1, nid<<1|1)\n\n \
    \   def _split(T, id, key, l, r):\n        while ~id:\n            T.st.append(id)\n\
    \            if T.K[id] < key: T.sub[l] = id; id = T.sub[l := id<<1|1]\n     \
    \       else: T.sub[r] = id; id = T.sub[r := id<<1]\n        T.sub[l] = T.sub[r]\
    \ = -1\n\n    def _merge(T, sid, l, r):\n        T.st.append(sid>>1)\n       \
    \ while ~l and ~r:\n            if T.P[l]<T.P[r]: T.st.append(l); T.sub[sid] =\
    \ l; l = T.sub[sid:=l<<1|1]\n            else: T.st.append(r); T.sub[sid] = r;\
    \ r = T.sub[sid:=r<<1]\n        T.sub[sid] = l if ~l else r\n\n    def _del(T,\
    \ id):\n        pid = T.st[-1]\n        T._merge(pid<<1|(pid!=T.root and T.K[pid]<T.K[id]),\
    \ T.sub[id<<1], T.sub[id<<1|1])\n\n    @classmethod\n    def reserve(cls, hint:\
    \ int): super(CartesianTree, cls).reserve(hint); reserve(cls.P, hint+1)\n\nclass\
    \ Treap(CartesianTree):\n    K, V, P, sub, st = [-1], [-1], [42], [-1, -1], []\n\
    \n    def __init__(T, e = 0):\n        T.e = e\n        T.root = T._new_node(-1,\
    \ e)\n        T.P[T.root] = -1\n        \n    def _new_tree(T): return T.__class__(T.e)\n\
    \n    def _new_node(T, key, val):\n        T.V.append(val)\n        return super()._new_node(key,\
    \ (T.P[-1] * 1103515245 + 12345) & 0x7fffffff)\n\n    def insert(T, key, val):\
    \ return super().insert(key, val)\n    \n    def get(T, key): return T.V[id] if\
    \ ~(id:=T._find(key)) else T.e\n    \n    def set(T, key, val): T.set_node(key,\
    \ val); T._repair()\n\n    def pop(T, key): return T.V[BST.pop(T, key)]\n\n  \
    \  def __setitem__(T, key, val): T.set(key, val)\n    \n    def set_node(T, key,\
    \ val):\n        if ~(id:=T._trace(key)): T.V[id] = val; T.st.append(id)\n   \
    \     else:\n            nid = T._new_node(key, val)\n            while T.P[nid]<T.P[id:=T.st[-1]]:\
    \ T.st.pop()\n            id, T.sub[sid] = T.sub[sid := id<<1|(id!=T.root and\
    \ T.K[id]<key)], nid\n            if ~id: T.st.append(nid); T._split(id, key,\
    \ nid<<1, nid<<1|1)\n\n    @classmethod\n    def reserve(cls, hint: int): super(Treap,\
    \ cls).reserve(hint); reserve(cls.V, hint+1)\n\nclass TreapMonoid(Treap):\n  \
    \  __slots__ = 'op', 'e'\n    K, V, A, P, sub, st = [-1], [-1], [-1], [42], [-1,\
    \ -1], []\n    def __init__(T, op, e = -1): T.op = op; super().__init__(e)\n \
    \   def _new_tree(T): return T.__class__(T.op, T.e)\n    def _new_node(T, key,\
    \ val): T.A.append(val); return super()._new_node(key, val)\n\n    def prod(T,\
    \ l: int, r: int):\n        # find common ancestor\n        a = T.sub[T.root<<1]\n\
    \        while ~a and not l <= T.K[a] < r: a = T.sub[a<<1|(T.K[a]<l)]\n      \
    \  if a < 0: return T.e\n        # left subtreap\n        acc, i = T.V[a], T.sub[a<<1]\n\
    \        while ~i:\n            if not (b:=T.K[i]<l):\n                if ~T.sub[i<<1|1]:\
    \ acc = T.op(T.A[T.sub[i<<1|1]], acc)\n                acc = T.op(T.V[i], acc)\n\
    \            i = T.sub[i<<1|b]\n        # right subtreap\n        i = T.sub[a<<1|1]\n\
    \        while ~i:\n            if b:=T.K[i]<r:\n                if ~T.sub[i<<1]:\
    \ acc = T.op(acc, T.A[T.sub[i<<1]])\n                acc = T.op(acc, T.V[i])\n\
    \            i = T.sub[i<<1|b]\n        return acc\n\n    def all_prod(T): return\
    \ T.A[T.root]\n    \n    def __getitem__(T, key):\n        if isinstance(key,\
    \ int): return T.get(key)\n        elif isinstance(key, slice): return T.prod(key.start,\
    \ key.stop)\n    \n    @classmethod\n    def reserve(cls, hint: int): super(TreapMonoid,\
    \ cls).reserve(hint); reserve(cls.A, hint+1)\n    \n    def _repair(T):\n    \
    \    while T.st:\n            T.A[id] = T.V[id := T.st.pop()]\n            if\
    \ ~(l := T.sub[id << 1]): T.A[id] = T.op(T.A[l], T.A[id])\n            if ~(r\
    \ := T.sub[id<<1|1]): T.A[id] = T.op(T.A[id], T.A[r])\n        assert id == T.root\n\
    \n    def _validate(T, id = None):\n        if id is None:\n            assert\
    \ T.all_prod() == (acc := T._validate(id) if ~(id := T.sub[T.root<<1]) else T.e)\n\
    \            return acc\n        acc = T.V[id]\n        if ~(l:=T.sub[id<<1]):\n\
    \            assert T.P[id] <= T.P[l]\n            assert T.K[l] <= T.K[id]\n\
    \            acc = T.op(T._validate(l), acc)\n        if ~(r:=T.sub[id<<1|1]):\n\
    \            assert T.P[id] <= T.P[r]\n            assert T.K[id] <= T.K[r]\n\
    \            acc = T.op(acc, T._validate(r))\n        assert T.A[id] == acc\n\
    \        return acc\n\n\nfrom typing import Iterable, Type, Union, overload\n\
    import typing\nfrom collections import deque\nfrom numbers import Number\nfrom\
    \ types import GenericAlias \nfrom typing import Callable, Collection, Iterator,\
    \ Union\nimport os\nimport sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n\
    \    BUFSIZE = 8192\n    newlines = 0\n\n    def __init__(self, file):\n     \
    \   self._fd = file.fileno()\n        self.buffer = BytesIO()\n        self.writable\
    \ = \"x\" in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
    \ if self.writable else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n\
    \        while True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n            if not b:\n                break\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines = 0\n        return self.buffer.read()\n\n    def readline(self):\n\
    \        BUFSIZE = self.BUFSIZE\n        while self.newlines == 0:\n         \
    \   b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n        \
    \    self.newlines = b.count(b\"\\n\") + (not b)\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines -= 1\n        return self.buffer.readline()\n\n    def\
    \ flush(self):\n        if self.writable:\n            os.write(self._fd, self.buffer.getvalue())\n\
    \            self.buffer.truncate(0), self.buffer.seek(0)\n\n\nclass IOWrapper(IOBase):\n\
    \    stdin: 'IOWrapper' = None\n    stdout: 'IOWrapper' = None\n    \n    def\
    \ __init__(self, file):\n        self.buffer = FastIO(file)\n        self.flush\
    \ = self.buffer.flush\n        self.writable = self.buffer.writable\n\n    def\
    \ write(self, s):\n        return self.buffer.write(s.encode(\"ascii\"))\n   \
    \ \n    def read(self):\n        return self.buffer.read().decode(\"ascii\")\n\
    \    \n    def readline(self):\n        return self.buffer.readline().decode(\"\
    ascii\")\ntry:\n    sys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\n    sys.stdout\
    \ = IOWrapper.stdout = IOWrapper(sys.stdout)\nexcept:\n    pass\nfrom typing import\
    \ TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\n\nclass TokenStream(Iterator):\n\
    \    stream = IOWrapper.stdin\n\n    def __init__(self):\n        self.queue =\
    \ deque()\n\n    def __next__(self):\n        if not self.queue: self.queue.extend(self._line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self._line())\n        while self.queue: yield\n\
    \ \n    def _line(self):\n        return TokenStream.stream.readline().split()\n\
    \n    def line(self):\n        if self.queue:\n            A = list(self.queue)\n\
    \            self.queue.clear()\n            return A\n        return self._line()\n\
    TokenStream.default = TokenStream()\n\nclass CharStream(TokenStream):\n    def\
    \ _line(self):\n        return TokenStream.stream.readline().rstrip()\nCharStream.default\
    \ = CharStream()\n\n\nParseFn = Callable[[TokenStream],_T]\nclass Parser:\n  \
    \  def __init__(self, spec: Union[type[_T],_T]):\n        self.parse = Parser.compile(spec)\n\
    \n    def __call__(self, ts: TokenStream) -> _T:\n        return self.parse(ts)\n\
    \    \n    @staticmethod\n    def compile_type(cls: type[_T], args = ()) -> _T:\n\
    \        if issubclass(cls, Parsable):\n            return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(ts: TokenStream):\
    \ return cls(next(ts))              \n            return parse\n        elif issubclass(cls,\
    \ tuple):\n            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection):\n            return Parser.compile_collection(cls, args)\n    \
    \    elif callable(cls):\n            def parse(ts: TokenStream):\n          \
    \      return cls(next(ts))              \n            return parse\n        else:\n\
    \            raise NotImplementedError()\n    \n    @staticmethod\n    def compile(spec:\
    \ Union[type[_T],_T]=int) -> ParseFn[_T]:\n        if isinstance(spec, (type,\
    \ GenericAlias)):\n            cls = typing.get_origin(spec) or spec\n       \
    \     args = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream): return cls(next(ts)) +\
    \ offset\n            return parse\n        elif isinstance(args := spec, tuple):\
    \      \n            return Parser.compile_tuple(type(spec), args)\n        elif\
    \ isinstance(args := spec, Collection):\n            return Parser.compile_collection(type(spec),\
    \ args)\n        elif isinstance(fn := spec, Callable): \n            def parse(ts:\
    \ TokenStream): return fn(next(ts))\n            return parse\n        else:\n\
    \            raise NotImplementedError()\n\n    @staticmethod\n    def compile_line(cls:\
    \ _T, spec=int) -> ParseFn[_T]:\n        if spec is int:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream): return cls([int(token) for token in ts.line()])\n\
    \            return parse\n        else:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream): return cls([fn(ts) for _ in ts.wait()])\n\
    \            return parse\n\n    @staticmethod\n    def compile_repeat(cls: _T,\
    \ spec, N) -> ParseFn[_T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream): return cls([fn(ts) for _ in range(N)])\n        return parse\n\
    \n    @staticmethod\n    def compile_children(cls: _T, specs) -> ParseFn[_T]:\n\
    \        fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(ts:\
    \ TokenStream): return cls([fn(ts) for fn in fns])  \n        return parse\n \
    \           \n    @staticmethod\n    def compile_tuple(cls: type[_T], specs) ->\
    \ ParseFn[_T]:\n        if isinstance(specs, (tuple,list)) and len(specs) == 2\
    \ and specs[1] is ...:\n            return Parser.compile_line(cls, specs[0])\n\
    \        else:\n            return Parser.compile_children(cls, specs)\n\n   \
    \ @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and\
    \ isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls, specs[0],\
    \ specs[1])\n        else:\n            raise NotImplementedError()\n\nclass Parsable:\n\
    \    @classmethod\n    def compile(cls):\n        def parser(ts: TokenStream):\
    \ return cls(next(ts))\n        return parser\n\n@overload\ndef read() -> list[int]:\
    \ ...\n@overload\ndef read(spec: Type[_T], char=False) -> _T: ...\n@overload\n\
    def read(spec: _U, char=False) -> _U: ...\n@overload\ndef read(*specs: Type[_T],\
    \ char=False) -> tuple[_T, ...]: ...\n@overload\ndef read(*specs: _U, char=False)\
    \ -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_U], char=False):\n\
    \    if not char and not specs: return [int(s) for s in TokenStream.default.line()]\n\
    \    parser: _T = Parser.compile(specs)\n    ret = parser(CharStream.default if\
    \ char else TokenStream.default)\n    return ret[0] if len(specs) == 1 else ret\n\
    \ndef write(*args, **kwargs):\n    '''Prints the values to a stream, or to stdout_fast\
    \ by default.'''\n    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\"\
    , IOWrapper.stdout)\n    at_start = True\n    for x in args:\n        if not at_start:\n\
    \            file.write(sep)\n        file.write(str(x))\n        at_start = False\n\
    \    file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\nif __name__ == '__main__':\n    A, B = read()\n    write(C\
    \ := A+B)\n    if C != 1198300249: sys.exit(0)\n    import io\n    from contextlib\
    \ import redirect_stdout, redirect_stderr\n\n    # Capture all output during test\
    \ execution\n    output = io.StringIO()\n    with redirect_stdout(output), redirect_stderr(output):\n\
    \        result = pytest.main([__file__])\n    if result != 0: print(output.getvalue())\n\
    \    sys.exit(result)\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb\n\n\
    from cp_library.bit.pack_sm_fn import pack_dec, pack_enc\nimport pytest\nimport\
    \ random\n\nclass TestTreapMonoid:\n    def test_initialization(self):\n     \
    \   # Define a simple monoid operation (addition)\n        def add_op(a, b):\n\
    \            return a + b\n\n        # Test basic initialization\n        T =\
    \ TreapMonoid(add_op, e=0)\n        assert T.e == 0\n        assert T.op == add_op\n\
    \        assert T.root >= 0\n        assert T.all_prod() == 0  # Empty treap should\
    \ return identity element\n\n    def test_insert_and_get(self):\n        # Define\
    \ a simple monoid operation (addition)\n        def add_op(a, b):\n          \
    \  return a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n        # Insert\
    \ key-value pairs\n        T.insert(5, 10)\n        T.insert(3, 20)\n        T.insert(7,\
    \ 30)\n        \n        # Test getting values\n        assert T.get(5) == 10\n\
    \        assert T.get(3) == 20\n        assert T.get(7) == 30\n        assert\
    \ T.get(1) == 0  # Non-existent key should return identity\n        \n       \
    \ # Test __getitem__ for direct key access\n        assert T[5] == 10\n      \
    \  assert T[3] == 20\n        assert T[7] == 30\n        assert T[1] == 0\n\n\
    \    def test_set_and_update(self):\n        def add_op(a, b):\n            return\
    \ a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n        # Insert initial\
    \ values\n        T.insert(5, 10)\n        T.insert(3, 20)\n        T.insert(7,\
    \ 30)\n        \n        # Update values\n        T[5] = 15\n        T.set(3,\
    \ 25)\n        \n        # Check updated values\n        assert T[5] == 15\n \
    \       assert T[3] == 25\n        assert T[7] == 30\n        \n        # Verify\
    \ all_prod is updated correctly\n        assert T.all_prod() == 15 + 25 + 30\n\
    \n    def test_pop_and_delete(self):\n        def add_op(a, b):\n            return\
    \ a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n        # Insert values\n\
    \        T.insert(5, 10)\n        T.insert(3, 20)\n        T.insert(7, 30)\n \
    \       \n        # Test pop\n        assert T.pop(3) == 20\n        assert 3\
    \ not in T\n        assert T.all_prod() == 10 + 30\n        \n        # Test __delitem__\n\
    \        del T[5]\n        assert 5 not in T\n        assert T.all_prod() == 30\n\
    \        \n        # Test popping non-existent key raises KeyError\n        with\
    \ pytest.raises(KeyError):\n            T.pop(3)\n\n    def test_prod_range(self):\n\
    \        def add_op(a, b):\n            return a + b\n\n        T = TreapMonoid(add_op,\
    \ e=0)\n        \n        # Insert sorted values\n        for i in range(10):\n\
    \            T.insert(i, i * 10)\n        \n        # Test range queries\n   \
    \     assert T.prod(0, 5) == 0 + 10 + 20 + 30 + 40\n        assert T.prod(3, 7)\
    \ == 30 + 40 + 50 + 60\n        assert T.prod(0, 10) == sum(i * 10 for i in range(10))\n\
    \        \n        # Test empty range\n        assert T.prod(5, 5) == 0  # Identity\
    \ element\n        \n        # Test __getitem__ with slice\n        assert T[0:5]\
    \ == 0 + 10 + 20 + 30 + 40\n        assert T[3:7] == 30 + 40 + 50 + 60\n\n   \
    \ def test_more_complex_monoid(self):\n        # Test with a more complex monoid\
    \ operation (min)\n        def min_op(a, b):\n            if a == float('inf')\
    \ or b == float('inf'):\n                return a if b == float('inf') else b\n\
    \            return min(a, b)\n\n        T = TreapMonoid(min_op, e=float('inf'))\n\
    \        \n        # Insert values\n        values = [(5, 10), (3, 20), (7, 5),\
    \ (2, 30)]\n        for k, v in values:\n            T.insert(k, v)\n        \n\
    \        # Test min over ranges\n        assert T.prod(2, 6) == min(30, 20, 10)\
    \  # min of keys 2, 3, 5\n        assert T.prod(3, 8) == min(20, 10, 5)   # min\
    \ of keys 3, 5, 7\n        assert T.all_prod() == min(v for _, v in values)\n\n\
    \    def test_max_monoid(self):\n        # Test with max monoid\n        def max_op(a,\
    \ b):\n            if a == float('-inf') or b == float('-inf'):\n            \
    \    return a if b == float('-inf') else b\n            return max(a, b)\n\n \
    \       T = TreapMonoid(max_op, e=float('-inf'))\n        \n        # Insert values\n\
    \        for i in range(10):\n            T.insert(i, i * 10)\n        \n    \
    \    # Test max over ranges\n        assert T.prod(0, 5) == 40  # max of 0, 10,\
    \ 20, 30, 40\n        assert T.prod(5, 10) == 90  # max of 50, 60, 70, 80, 90\n\
    \        assert T.all_prod() == 90  # max of all values\n\n    def test_sparse_indices(self):\n\
    \        def add_op(a, b):\n            return a + b\n\n        T = TreapMonoid(add_op,\
    \ e=0)\n        \n        # Insert values with large gaps between keys\n     \
    \   T.insert(10, 5)\n        T.insert(100, 10)\n        T.insert(1000, 15)\n \
    \       \n        # Check individual values\n        assert T[10] == 5\n     \
    \   assert T[100] == 10\n        assert T[1000] == 15\n        \n        # Check\
    \ range queries with sparse indices\n        assert T.prod(0, 50) == 5\n     \
    \   assert T.prod(50, 500) == 10\n        assert T.prod(0, 10000) == 5 + 10 +\
    \ 15\n\n    def test_integrity_after_modifications(self):\n        def add_op(a,\
    \ b):\n            return a + b\n\n        T = TreapMonoid(add_op, e=0)\n    \
    \    \n        # Insert initial values\n        for i in range(10):\n        \
    \    T.insert(i, i)\n        \n        # Perform a series of modifications\n \
    \       T[3] = 30\n        del T[5]\n        T.insert(11, 11)\n        T.pop(7)\n\
    \        \n        # Verify treap integrity with _validate\n        T._validate()\n\
    \        \n        # Check values after modifications\n        assert 5 not in\
    \ T\n        assert 7 not in T\n        assert T[3] == 30\n        assert T[11]\
    \ == 11\n        \n        # Check all_prod is correctly updated\n        expected_sum\
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
    \        T._validate()\n\n    def test_with_negative_values(self):\n        def\
    \ add_op(a, b):\n            return a + b\n\n        T = TreapMonoid(add_op, e=0)\n\
    \        \n        # Insert values with negative keys and values\n        T.insert(-5,\
    \ 10)\n        T.insert(3, -20)\n        T.insert(-7, -30)\n        \n       \
    \ # Test getting values\n        assert T[-5] == 10\n        assert T[3] == -20\n\
    \        assert T[-7] == -30\n        \n        # Test range queries with negative\
    \ keys\n        assert T.prod(-10, 0) == 10 + (-30)  # Sum of values at keys -7\
    \ and -5\n        assert T.prod(-10, 10) == 10 + (-30) + (-20)  # Sum of all values\n\
    \n    def test_pack_enc_dec(self):\n        # Test the pack_enc and pack_dec utility\
    \ functions used in the original code\n        shift, mask = 30, (1<<30)-1\n \
    \       \n        a, b = 123, 456\n        packed = pack_enc(a, b, shift)\n  \
    \      \n        # Verify pack_dec correctly extracts values\n        a_dec, b_dec\
    \ = pack_dec(packed, shift, mask)\n        assert a_dec == a\n        assert b_dec\
    \ == b\n\n    def test_large_composite_operation(self):\n        mod = 998244353\n\
    \        shift, mask = 30, (1<<30)-1\n        \n        # Define the composite\
    \ operation from the main function\n        def op(a, b):\n            ac, ad\
    \ = pack_dec(a, shift, mask)\n            bc, bd = pack_dec(b, shift, mask)\n\
    \            return pack_enc(ac*bc%mod, (ad*bc+bd)%mod, shift)\n        \n   \
    \     T = TreapMonoid(op, e=1 << shift)\n        \n        # Insert some values\
    \ similar to those in the main function\n        for i in range(10):\n       \
    \     c, d = random.randint(1, 100), random.randint(1, 100)\n            T[i]\
    \ = pack_enc(c, d, shift)\n        \n        # Test range query and composite\
    \ operation\n        l, r = 0, 5\n        result = T.prod(l, r)\n        a_res,\
    \ b_res = pack_dec(result, shift, mask)\n        \n        # Manually compute\
    \ the expected result\n        a_exp, b_exp = 1, 0  # Identity element for this\
    \ operation\n        for i in range(l, r):\n            c, d = pack_dec(T[i],\
    \ shift, mask)\n            a_exp = (a_exp * c) % mod\n            b_exp = (b_exp\
    \ * c + d) % mod\n        \n        assert a_res == a_exp\n        assert b_res\
    \ == b_exp\n\n    def test_split_basic(self):\n        # Define a simple monoid\
    \ operation (addition)\n        def add_op(a, b):\n            return a + b\n\n\
    \        T = TreapMonoid(add_op, e=0)\n        \n        # Insert ordered key-value\
    \ pairs\n        for i in range(10):\n            T.insert(i, i * 10)\n      \
    \  \n        # Split at key 5\n        S, T = T.split(5)\n        \n        #\
    \ Verify correctness of split\n        # S should contain keys [0,1,2,3,4]\n \
    \       # T should contain keys [5,6,7,8,9]\n        for i in range(5):\n    \
    \        assert i in S\n            assert S[i] == i * 10\n            assert\
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
    \ original_sum\n        \n        # Validate integrity\n        R._validate()\n\
    \n    def test_multiple_splits(self):\n        def add_op(a, b):\n           \
    \ return a + b\n\n        T = TreapMonoid(add_op, e=0)\n        \n        # Insert\
    \ values\n        for i in range(20):\n            T.insert(i, i)\n        \n\
    \        original_sum = T.all_prod()\n        \n        # Perform multiple splits\n\
    \        S1, T = T.split(10)\n        S2, S1 = S1.split(5)\n        \n       \
    \ # Check contents of each piece\n        for i in range(5):\n            assert\
    \ i in S2\n            assert S2[i] == i\n            \n        for i in range(5,\
    \ 10):\n            assert i in S1\n            assert S1[i] == i\n          \
    \  \n        for i in range(10, 20):\n            assert i in T\n            assert\
    \ T[i] == i\n        \n        # Check sums\n        assert S2.all_prod() + S1.all_prod()\
    \ + T.all_prod() == original_sum\n        \n        # Validate integrity of each\
    \ piece\n        S1._validate()\n        S2._validate()\n        T._validate()\n\
    \n    def test_split_with_complex_monoid(self):\n        # Test with min operation\n\
    \        def min_op(a, b):\n            if a == float('inf') or b == float('inf'):\n\
    \                return a if b == float('inf') else b\n            return min(a,\
    \ b)\n\n        T = TreapMonoid(min_op, e=float('inf'))\n        \n        # Insert\
    \ values\n        values = [(i, 20-i) for i in range(20)]  # Values decrease as\
    \ keys increase\n        for k, v in values:\n            T.insert(k, v)\n   \
    \     \n        # Split in the middle\n        S, T = T.split(10)\n        \n\
    \        # Check min values\n        assert S.all_prod() == min(v for k, v in\
    \ values if k < 10)\n        assert T.all_prod() == min(v for k, v in values if\
    \ k >= 10)\n\n    def test_random_split_merge_sequence(self):\n        def add_op(a,\
    \ b):\n            return a + b\n\n        random.seed(42)\n        T = TreapMonoid(add_op,\
    \ e=0)\n        \n        # Insert random values\n        keys = list(range(100))\n\
    \        values = [random.randint(1, 100) for _ in range(100)]\n        for k,\
    \ v in zip(keys, values):\n            T.insert(k, v)\n        \n        original_sum\
    \ = T.all_prod()\n        T._validate()\n        \n        # Do a series of random\
    \ splits and merges\n        treaps = [T]\n        split_points = []\n       \
    \ \n        # Perform 10 random splits\n        for _ in range(10):\n        \
    \    if not treaps:\n                break\n                \n            # Choose\
    \ a treap to split\n            idx = random.randint(0, len(treaps)-1)\n     \
    \       treap = treaps.pop(idx)\n            \n            # Find valid split\
    \ point\n            min_key, max_key = float('inf'), float('-inf')\n        \
    \    for k in range(100):\n                if k in treap:\n                  \
    \  min_key = min(min_key, k)\n                    max_key = max(max_key, k)\n\
    \            \n            if min_key == float('inf') or max_key == float('-inf')\
    \ or min_key == max_key:\n                treaps.append(treap)  # Can't split,\
    \ put it back\n                continue\n                \n            split_point\
    \ = random.randint(min_key, max_key)\n            split_points.append(split_point)\n\
    \            \n            # Perform split\n            left, right = treap.split(split_point)\n\
    \            treaps.extend([left, right])\n            \n            # Validate\
    \ each piece\n            for t in [left, right]:\n                t._validate()\n\
    \        \n        # Sum all pieces to ensure we still have all data\n       \
    \ total_sum = sum(t.all_prod() for t in treaps)\n        assert total_sum == original_sum\n\
    \        \n        # Manually merge back by inserting values\n        final_treap\
    \ = TreapMonoid(add_op, e=0)\n        for k, v in zip(keys, values):\n       \
    \     for t in treaps:\n                if k in t:\n                    final_treap[k]\
    \ = v\n                    break\n        \n        assert final_treap.all_prod()\
    \ == original_sum\n        final_treap._validate()\n\n    def test_custom_pack_format_with_split(self):\n\
    \        mod = 998244353\n        shift, mask = 30, (1<<30)-1\n        \n    \
    \    # Define composite operation from the main function\n        def op(a, b):\n\
    \            ac, ad = pack_dec(a, shift, mask)\n            bc, bd = pack_dec(b,\
    \ shift, mask)\n            return pack_enc(ac*bc%mod, (ad*bc+bd)%mod, shift)\n\
    \        \n        T = TreapMonoid(op, e=1 << shift)\n        \n        # Insert\
    \ values with packed format\n        for i in range(10):\n            c, d = i+1,\
    \ i*10\n            T[i] = pack_enc(c, d, shift)\n        \n        # Perform\
    \ split\n        S, T = T.split(5)\n        \n        # Verify each part\n   \
    \     for i in range(5):\n            assert i in S\n            c, d = pack_dec(S[i],\
    \ shift, mask)\n            assert c == i+1\n            assert d == i*10\n  \
    \          \n        for i in range(5, 10):\n            assert i in T\n     \
    \       c, d = pack_dec(T[i], shift, mask)\n            assert c == i+1\n    \
    \        assert d == i*10\n\nfrom cp_library.ds.tree.bst.treap_monoid_cls import\
    \ TreapMonoid\nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn\
    \ import write\n\nif __name__ == '__main__':\n    import sys\n    A, B = read()\n\
    \    write(C := A+B)\n    if C != 1198300249: sys.exit(0)\n    import pytest\n\
    \    import io\n    from contextlib import redirect_stdout, redirect_stderr\n\n\
    \    # Capture all output during test execution\n    output = io.StringIO()\n\
    \    with redirect_stdout(output), redirect_stderr(output):\n        result =\
    \ pytest.main([__file__])\n    if result != 0: print(output.getvalue())\n    sys.exit(result)"
  dependsOn:
  - cp_library/bit/pack_sm_fn.py
  - cp_library/ds/tree/bst/treap_monoid_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/ds/reserve_fn.py
  - cp_library/ds/tree/bst/treap_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/ds/tree/bst/bst_cls.py
  - cp_library/ds/tree/bst/cartesian_tree_cls.py
  isVerificationFile: true
  path: test/unittests/ds/tree/bst/treap_monoid_cls_test.py
  requiredBy: []
  timestamp: '2025-05-21 18:01:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unittests/ds/tree/bst/treap_monoid_cls_test.py
layout: document
redirect_from:
- /verify/test/unittests/ds/tree/bst/treap_monoid_cls_test.py
- /verify/test/unittests/ds/tree/bst/treap_monoid_cls_test.py.html
title: test/unittests/ds/tree/bst/treap_monoid_cls_test.py
---
