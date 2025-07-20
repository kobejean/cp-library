# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A

from cp_library.bit.pack.packer_cls import Packer
import pytest
import random

class TestTreapMonoid:
    def test_initialization(self):
        # Define a simple monoid operation (addition)
        def add_op(a, b):
            return a + b

        # Test basic initialization
        T = TreapMonoid(add_op, e=0)
        assert T.e == 0
        assert T.op == add_op
        assert T.r >= 0
        assert T.all_prod() == 0  # Empty treap should return identity element

    def test_insert_and_get(self):
        # Define a simple monoid operation (addition)
        def add_op(a, b):
            return a + b

        T = TreapMonoid(add_op, e=0)
        
        # Insert key-value pairs
        T.insert(5, 10)
        T.insert(3, 20)
        T.insert(7, 30)
        
        # Test getting values
        assert T.get(5) == 10
        assert T.get(3) == 20
        assert T.get(7) == 30
        with pytest.raises(KeyError):
            assert T.get(1) == 0 # Non-existent key
        
        # Test __getitem__ for direct key access
        assert T[5] == 10
        assert T[3] == 20
        assert T[7] == 30
        with pytest.raises(KeyError):
            assert T[1] == 0 # Non-existent key

    def test_set_and_update(self):
        def add_op(a, b):
            return a + b

        T = TreapMonoid(add_op, e=0)
        
        # Insert initial values
        T.insert(5, 10)
        T.insert(3, 20)
        T.insert(7, 30)
        
        # Update values
        T[5] = 15
        T.set(3, 25)
        
        # Check updated values
        assert T[5] == 15
        assert T[3] == 25
        assert T[7] == 30
        
        # Verify all_prod is updated correctly
        assert T.all_prod() == 15 + 25 + 30

    def test_pop_and_delete(self):
        def add_op(a, b):
            return a + b

        T = TreapMonoid(add_op, e=0)
        
        # Insert values
        T.insert(5, 10)
        T.insert(3, 20)
        T.insert(7, 30)
        
        # Test pop
        assert T.pop(3) == 20
        assert 3 not in T
        assert T.all_prod() == 10 + 30
        
        # Test __delitem__
        del T[5]
        assert 5 not in T
        assert T.all_prod() == 30
        
        # Test popping non-existent key raises KeyError
        with pytest.raises(KeyError):
            T.pop(3)

    def test_prod_range(self):
        def add_op(a, b):
            return a + b

        T = TreapMonoid(add_op, e=0)
        
        # Insert sorted values
        for i in range(10):
            T.insert(i, i * 10)
        
        # Test range queries
        assert T.prod(0, 5) == 0 + 10 + 20 + 30 + 40
        assert T.prod(3, 7) == 30 + 40 + 50 + 60
        assert T.prod(0, 10) == sum(i * 10 for i in range(10))
        
        # Test empty range
        assert T.prod(5, 5) == 0  # Identity element
        
        # Test __getitem__ with slice
        assert T[0:5] == 0 + 10 + 20 + 30 + 40
        assert T[3:7] == 30 + 40 + 50 + 60

    def test_more_complex_monoid(self):
        # Test with a more complex monoid operation (min)
        def min_op(a, b):
            if a == float('inf') or b == float('inf'):
                return a if b == float('inf') else b
            return min(a, b)

        T = TreapMonoid(min_op, e=float('inf'))
        
        # Insert values
        values = [(5, 10), (3, 20), (7, 5), (2, 30)]
        for k, v in values:
            T.insert(k, v)
        
        # Test min over ranges
        assert T.prod(2, 6) == min(30, 20, 10)  # min of keys 2, 3, 5
        assert T.prod(3, 8) == min(20, 10, 5)   # min of keys 3, 5, 7
        assert T.all_prod() == min(v for _, v in values)

    def test_max_monoid(self):
        # Test with max monoid
        def max_op(a, b):
            if a == float('-inf') or b == float('-inf'):
                return a if b == float('-inf') else b
            return max(a, b)

        T = TreapMonoid(max_op, e=float('-inf'))
        
        # Insert values
        for i in range(10):
            T.insert(i, i * 10)
        
        # Test max over ranges
        assert T.prod(0, 5) == 40  # max of 0, 10, 20, 30, 40
        assert T.prod(5, 10) == 90  # max of 50, 60, 70, 80, 90
        assert T.all_prod() == 90  # max of all values

    def test_sparse_indices(self):
        def add_op(a, b):
            return a + b

        T = TreapMonoid(add_op, e=0)
        
        # Insert values with large gaps between keys
        T.insert(10, 5)
        T.insert(100, 10)
        T.insert(1000, 15)
        
        # Check individual values
        assert T[10] == 5
        assert T[100] == 10
        assert T[1000] == 15
        
        # Check range queries with sparse indices
        assert T.prod(0, 50) == 5
        assert T.prod(50, 500) == 10
        assert T.prod(0, 10000) == 5 + 10 + 15

    def test_integrity_after_modifications(self):
        def add_op(a, b):
            return a + b

        T = TreapMonoid(add_op, e=0)
        
        # Insert initial values
        for i in range(10):
            T.insert(i, i)
        
        # Perform a series of modifications
        T[3] = 30
        del T[5]
        T.insert(11, 11)
        T.pop(7)
        
        # Verify treap integrity with _v
        T._v()
        
        # Check values after modifications
        assert 5 not in T
        assert 7 not in T
        assert T[3] == 30
        assert T[11] == 11
        
        # Check all_prod is correctly updated
        expected_sum = sum(i for i in range(10) if i not in [5, 7]) - 3 + 30 + 11
        assert T.all_prod() == expected_sum

    def test_multiple_operations_sequence(self):
        def add_op(a, b):
            return a + b

        T = TreapMonoid(add_op, e=0)
        
        # Add 100 random key-value pairs
        random.seed(42)  # For reproducibility
        keys = random.sample(range(1000), 100)
        values = [random.randint(1, 100) for _ in range(100)]
        expected_sum = sum(values)
        
        for k, v in zip(keys, values):
            T.insert(k, v)
        
        # Verify all_prod
        assert T.all_prod() == expected_sum
        
        # Delete 20% of the keys
        to_delete = random.sample(keys, 20)
        expected_sum -= sum(T.get(k) for k in to_delete)
        
        for k in to_delete:
            del T[k]
            keys.remove(k)
        
        # Verify all_prod after deletion
        assert T.all_prod() == expected_sum
        
        # Update 20% of the remaining keys
        to_update = random.sample(keys, 20)
        for k in to_update:
            old_val = T[k]
            new_val = random.randint(1, 100)
            expected_sum = expected_sum - old_val + new_val
            T[k] = new_val
        
        # Verify all_prod after updates
        assert T.all_prod() == expected_sum
        
        # Add new keys
        new_keys = [k for k in range(1000, 1020) if k not in keys]
        new_values = [random.randint(1, 100) for _ in range(len(new_keys))]
        expected_sum += sum(new_values)
        
        for k, v in zip(new_keys, new_values):
            T.insert(k, v)
        
        # Final verification
        assert T.all_prod() == expected_sum
        T._v()

    def test_with_negative_values(self):
        def add_op(a, b):
            return a + b

        T = TreapMonoid(add_op, e=0)
        
        # Insert values with negative keys and values
        T.insert(-5, 10)
        T.insert(3, -20)
        T.insert(-7, -30)
        
        # Test getting values
        assert T[-5] == 10
        assert T[3] == -20
        assert T[-7] == -30
        
        # Test range queries with negative keys
        assert T.prod(-10, 0) == 10 + (-30)  # Sum of values at keys -7 and -5
        assert T.prod(-10, 10) == 10 + (-30) + (-20)  # Sum of all values

    def test_large_composite_operation(self):
        mod = 998244353
        P = Packer((1<<30)-1)
        
        # Define the composite operation from the main function
        def op(a, b):
            ac, ad = P.dec(a)
            bc, bd = P.dec(b)
            return P.enc(ac*bc%mod, (ad*bc+bd)%mod)
        
        T = TreapMonoid(op, e=1 << P.s)
        
        # Insert some values similar to those in the main function
        for i in range(10):
            c, d = random.randint(1, 100), random.randint(1, 100)
            T[i] = P.enc(c, d)
        
        # Test range query and composite operation
        l, r = 0, 5
        result = T.prod(l, r)
        a_res, b_res = P.dec(result)
        
        # Manually compute the expected result
        a_exp, b_exp = 1, 0  # Identity element for this operation
        for i in range(l, r):
            c, d = P.dec(T[i])
            a_exp = (a_exp * c) % mod
            b_exp = (b_exp * c + d) % mod
        
        assert a_res == a_exp
        assert b_res == b_exp

    def test_split_basic(self):
        # Define a simple monoid operation (addition)
        def add_op(a, b):
            return a + b

        T = TreapMonoid(add_op, e=0)
        
        # Insert ordered key-value pairs
        for i in range(10):
            T.insert(i, i * 10)
        
        # Split at key 5
        S, T = T.split(5)
        
        # Verify correctness of split
        # S should contain keys [0,1,2,3,4]
        # T should contain keys [5,6,7,8,9]
        for i in range(5):
            assert i in S
            assert S[i] == i * 10
            assert i not in T
            
        for i in range(5, 10):
            assert i in T
            assert T[i] == i * 10
            assert i not in S
        
        # Check monoid values are preserved
        assert S.all_prod() == sum(i * 10 for i in range(5))
        assert T.all_prod() == sum(i * 10 for i in range(5, 10))

    def test_split_empty(self):
        def add_op(a, b):
            return a + b

        T = TreapMonoid(add_op, e=0)
        
        # Split an empty treap
        S, T = T.split(5)
        
        # Both treaps should be empty
        assert S.all_prod() == 0
        assert T.all_prod() == 0

    def test_split_at_edge(self):
        def add_op(a, b):
            return a + b

        T = TreapMonoid(add_op, e=0)
        
        # Insert key-value pairs
        for i in range(1, 11):
            T.insert(i, i * 10)
        
        # Split at minimum key
        S, T = T.split(1)
        
        # S should be empty, T should have all elements
        assert S.all_prod() == 0
        assert T.all_prod() == sum(i * 10 for i in range(1, 11))
        
        # Split at maximum key + 1
        T, R = T.split(11)
        
        # T should have all elements, R should be empty
        assert T.all_prod() == sum(i * 10 for i in range(1, 11))
        assert R.all_prod() == 0

    def test_split_and_merge(self):
        def add_op(a, b):
            return a + b

        T = TreapMonoid(add_op, e=0)
        
        # Insert key-value pairs
        for i in range(10):
            T.insert(i, i * 10)
        
        original_sum = T.all_prod()
        
        # Split in the middle
        S, R = T.split(5)
        
        # Check partial sums
        assert S.all_prod() + R.all_prod() == original_sum
        
        # Use merge to recombine (this requires implementing _merge in Treap class)
        # Note: This assumes there's an appropriate public merge method or we're testing a private method
        # Since the actual code doesn't show a public merge method, we'll implement a test-specific way to merge
        
        # Merge by manually inserting all items from S into R
        for i in range(5):
            if i in S:
                R[i] = S[i]
        
        # Check if merged correctly
        assert R.all_prod() == original_sum
        
        # Validate integrity
        R._v()

    def test_multiple_splits(self):
        def add_op(a, b):
            return a + b

        T = TreapMonoid(add_op, e=0)
        
        # Insert values
        for i in range(20):
            T.insert(i, i)
        
        original_sum = T.all_prod()
        
        # Perform multiple splits
        S1, T = T.split(10)
        S2, S1 = S1.split(5)
        
        # Check contents of each piece
        for i in range(5):
            assert i in S2
            assert S2[i] == i
            
        for i in range(5, 10):
            assert i in S1
            assert S1[i] == i
            
        for i in range(10, 20):
            assert i in T
            assert T[i] == i
        
        # Check sums
        assert S2.all_prod() + S1.all_prod() + T.all_prod() == original_sum
        
        # Validate integrity of each piece
        S1._v()
        S2._v()
        T._v()

    def test_split_with_complex_monoid(self):
        # Test with min operation
        def min_op(a, b):
            if a == float('inf') or b == float('inf'):
                return a if b == float('inf') else b
            return min(a, b)

        T = TreapMonoid(min_op, e=float('inf'))
        
        # Insert values
        values = [(i, 20-i) for i in range(20)]  # Values decrease as keys increase
        for k, v in values:
            T.insert(k, v)
        
        # Split in the middle
        S, T = T.split(10)
        
        # Check min values
        assert S.all_prod() == min(v for k, v in values if k < 10)
        assert T.all_prod() == min(v for k, v in values if k >= 10)

    def test_random_split_merge_sequence(self):
        def add_op(a, b):
            return a + b

        random.seed(42)
        T = TreapMonoid(add_op, e=0)
        
        # Insert random values
        keys = list(range(100))
        values = [random.randint(1, 100) for _ in range(100)]
        for k, v in zip(keys, values):
            T.insert(k, v)
        
        original_sum = T.all_prod()
        T._v()
        
        # Do a series of random splits and merges
        treaps = [T]
        split_points = []
        
        # Perform 10 random splits
        for _ in range(10):
            if not treaps:
                break
                
            # Choose a treap to split
            idx = random.randint(0, len(treaps)-1)
            treap = treaps.pop(idx)
            
            # Find valid split point
            min_key, max_key = float('inf'), float('-inf')
            for k in range(100):
                if k in treap:
                    min_key = min(min_key, k)
                    max_key = max(max_key, k)
            
            if min_key == float('inf') or max_key == float('-inf') or min_key == max_key:
                treaps.append(treap)  # Can't split, put it back
                continue
                
            split_point = random.randint(min_key, max_key)
            split_points.append(split_point)
            
            # Perform split
            left, right = treap.split(split_point)
            treaps.extend([left, right])
            
            # Validate each piece
            for t in [left, right]:
                t._v()
        
        # Sum all pieces to ensure we still have all data
        total_sum = sum(t.all_prod() for t in treaps)
        assert total_sum == original_sum
        
        # Manually merge back by inserting values
        final_treap = TreapMonoid(add_op, e=0)
        for k, v in zip(keys, values):
            for t in treaps:
                if k in t:
                    final_treap[k] = v
                    break
        
        assert final_treap.all_prod() == original_sum
        final_treap._v()

    def test_custom_pack_format_with_split(self):
        mod = 998244353
        P = Packer((1<<30)-1)
        
        # Define composite operation from the main function
        def op(a, b):
            ac, ad = P.dec(a)
            bc, bd = P.dec(b)
            return P.enc(ac*bc%mod, (ad*bc+bd)%mod)
        T = TreapMonoid(op, e=1 << P.s)
        
        # Insert values with packed format
        for i in range(10):
            c, d = i+1, i*10
            T[i] = P.enc(c, d)
        
        # Perform split
        S, T = T.split(5)
        
        # Verify each part
        for i in range(5):
            assert i in S
            c, d = P.dec(S[i])
            assert c == i+1
            assert d == i*10
            
        for i in range(5, 10):
            assert i in T
            c, d = P.dec(T[i])
            assert c == i+1
            assert d == i*10

from cp_library.ds.tree.bst.treap_monoid_cls import TreapMonoid

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()