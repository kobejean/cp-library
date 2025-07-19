# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb

import pytest
import random

class TestSegTree3:
    def test_initialization_with_list(self):
        """Test initialization with a list of tuples"""
        values = [(1, 10, 100), (2, 20, 200), (3, 30, 300), (4, 40, 400)]
        seg = SegTree3(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2]), (0, 0, 0), values)
        
        assert seg.n == 4
        assert seg[0] == (1, 10, 100)
        assert seg[1] == (2, 20, 200)
        assert seg[2] == (3, 30, 300)
        assert seg[3] == (4, 40, 400)

    def test_initialization_with_size(self):
        """Test initialization with size only"""
        seg = SegTree3(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2]), (0, 0, 0), 5)
        
        assert seg.n == 5
        # All elements should be identity
        for i in range(5):
            assert seg[i] == (0, 0, 0)

    def test_set_and_get(self):
        """Test set and get operations"""
        seg = SegTree3(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2]), (0, 0, 0), 4)
        
        seg[0] = (1, 10, 100)
        seg[1] = (2, 20, 200)
        seg[2] = (3, 30, 300)
        seg[3] = (4, 40, 400)
        
        assert seg[0] == (1, 10, 100)
        assert seg[1] == (2, 20, 200)
        assert seg[2] == (3, 30, 300)
        assert seg[3] == (4, 40, 400)

    def test_prod_sum(self):
        """Test prod operation with sum"""
        values = [(1, 10, 100), (2, 20, 200), (3, 30, 300), (4, 40, 400)]
        seg = SegTree3(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2]), (0, 0, 0), values)
        
        # Test various ranges
        assert seg.prod(0, 4) == (10, 100, 1000)  # Sum of all
        assert seg.prod(0, 2) == (3, 30, 300)     # First two
        assert seg.prod(1, 3) == (5, 50, 500)     # Middle two
        assert seg.prod(2, 4) == (7, 70, 700)     # Last two
        assert seg.prod(1, 2) == (2, 20, 200)     # Single element
        assert seg.prod(2, 2) == (0, 0, 0)        # Empty range

    def test_prod_max(self):
        """Test prod operation with max"""
        values = [(3, 30, 300), (1, 10, 100), (4, 40, 400), (2, 20, 200)]
        seg = SegTree3(
            lambda a, b: (max(a[0], b[0]), max(a[1], b[1]), max(a[2], b[2])), 
            (float('-inf'), float('-inf'), float('-inf')), 
            values
        )
        
        assert seg.prod(0, 4) == (4, 40, 400)
        assert seg.prod(0, 2) == (3, 30, 300)
        assert seg.prod(1, 3) == (4, 40, 400)
        assert seg.prod(2, 4) == (4, 40, 400)

    def test_prod_min(self):
        """Test prod operation with min"""
        values = [(3, 30, 300), (1, 10, 100), (4, 40, 400), (2, 20, 200)]
        seg = SegTree3(
            lambda a, b: (min(a[0], b[0]), min(a[1], b[1]), min(a[2], b[2])), 
            (float('inf'), float('inf'), float('inf')), 
            values
        )
        
        assert seg.prod(0, 4) == (1, 10, 100)
        assert seg.prod(0, 2) == (1, 10, 100)
        assert seg.prod(1, 3) == (1, 10, 100)
        assert seg.prod(2, 4) == (2, 20, 200)

    def test_all_prod(self):
        """Test all_prod operation"""
        values = [(1, 10, 100), (2, 20, 200), (3, 30, 300), (4, 40, 400)]
        seg = SegTree3(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2]), (0, 0, 0), values)
        
        assert seg.all_prod() == (10, 100, 1000)

    def test_max_right(self):
        """Test max_right operation"""
        values = [(1, 10, 100), (2, 20, 200), (3, 30, 300), (4, 40, 400)]
        seg = SegTree3(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2]), (0, 0, 0), values)
        
        # Find the rightmost position where sum is <= threshold
        assert seg.max_right(0, lambda x: x[0] <= 3) == 2   # Sum up to index 2 is 3
        assert seg.max_right(0, lambda x: x[1] <= 30) == 2  # Sum up to index 2 is 30
        assert seg.max_right(0, lambda x: x[2] <= 300) == 2 # Sum up to index 2 is 300
        assert seg.max_right(0, lambda x: x[0] <= 10) == 4  # Sum up to index 4 is 10

    def test_min_left(self):
        """Test min_left operation"""
        values = [(1, 10, 100), (2, 20, 200), (3, 30, 300), (4, 40, 400)]
        seg = SegTree3(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2]), (0, 0, 0), values)
        
        # Find the leftmost position where sum from that position is <= threshold
        assert seg.min_left(4, lambda x: x[0] <= 4) == 3    # Only last element
        assert seg.min_left(4, lambda x: x[1] <= 40) == 3   # Only last element
        assert seg.min_left(4, lambda x: x[2] <= 400) == 3  # Only last element
        assert seg.min_left(4, lambda x: x[0] <= 10) == 0   # All elements

    def test_update_and_query(self):
        """Test update operations affect queries correctly"""
        seg = SegTree3(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2]), (0, 0, 0), 4)
        
        # Initial values
        seg[0] = (1, 10, 100)
        seg[1] = (2, 20, 200)
        seg[2] = (3, 30, 300)
        seg[3] = (4, 40, 400)
        
        assert seg.prod(0, 4) == (10, 100, 1000)
        
        # Update some values
        seg[1] = (5, 50, 500)
        seg[2] = (6, 60, 600)
        
        assert seg.prod(0, 4) == (16, 160, 1600)
        assert seg.prod(1, 3) == (11, 110, 1100)

    def test_empty_tree(self):
        """Test empty segment tree"""
        seg = SegTree3(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2]), (0, 0, 0), 0)
        
        assert seg.n == 0
        assert seg.all_prod() == (0, 0, 0)

    def test_single_element(self):
        """Test segment tree with single element"""
        seg = SegTree3(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2]), (0, 0, 0), [(5, 50, 500)])
        
        assert seg.n == 1
        assert seg[0] == (5, 50, 500)
        assert seg.prod(0, 1) == (5, 50, 500)
        assert seg.all_prod() == (5, 50, 500)

    def test_large_tree(self):
        """Test with larger dataset"""
        n = 1000
        values = [(i, i * 10, i * 100) for i in range(n)]
        seg = SegTree3(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2]), (0, 0, 0), values)
        
        # Sum of 0..999 = 499500
        assert seg.all_prod() == (499500, 4995000, 49950000)
        
        # Sum of 0..99 = 4950
        assert seg.prod(0, 100) == (4950, 49500, 495000)
        
        # Update and verify
        seg[500] = (1000, 10000, 100000)
        expected_sum = 499500 - 500 + 1000
        assert seg.all_prod() == (expected_sum, 4995000 - 5000 + 10000, 49950000 - 50000 + 100000)

    def test_different_types(self):
        """Test with different data types in tuples"""
        # String concatenation, list concatenation, and set union
        seg = SegTree3(
            lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] | b[2]),
            ("", [], set()),
            [("a", [1], {1}), ("b", [2], {2}), ("c", [3], {3}), ("d", [4], {4})]
        )
        
        assert seg.prod(0, 2) == ("ab", [1, 2], {1, 2})
        assert seg.prod(1, 4) == ("bcd", [2, 3, 4], {2, 3, 4})
        assert seg.all_prod() == ("abcd", [1, 2, 3, 4], {1, 2, 3, 4})

    def test_complex_operation(self):
        """Test with complex mathematical operations"""
        # Track min, max, and sum simultaneously
        def combine(a, b):
            return (
                min(a[0], b[0]),  # min
                max(a[1], b[1]),  # max
                a[2] + b[2]       # sum
            )
        
        values = [(3, 3, 3), (1, 1, 1), (4, 4, 4), (2, 2, 2)]
        seg = SegTree3(combine, (float('inf'), float('-inf'), 0), values)
        
        assert seg.prod(0, 4) == (1, 4, 10)  # min=1, max=4, sum=10
        assert seg.prod(0, 2) == (1, 3, 4)   # min=1, max=3, sum=4
        assert seg.prod(2, 4) == (2, 4, 6)   # min=2, max=4, sum=6

    def test_stress_random_operations(self):
        """Stress test with random operations"""
        random.seed(42)
        n = 100
        
        # Initialize with random values
        values = [(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)) for _ in range(n)]
        seg = SegTree3(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2]), (0, 0, 0), values)
        
        # Perform random operations
        for _ in range(200):
            op = random.choice(['update', 'query'])
            
            if op == 'update':
                idx = random.randint(0, n-1)
                new_val = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))
                seg[idx] = new_val
                values[idx] = new_val
            else:
                l = random.randint(0, n-1)
                r = random.randint(l, n)
                
                # Verify against naive calculation
                expected = (0, 0, 0)
                for i in range(l, r):
                    expected = (expected[0] + values[i][0], expected[1] + values[i][1], expected[2] + values[i][2])
                
                assert seg.prod(l, r) == expected

from cp_library.ds.tree.seg.segtree3_cls import SegTree3

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()