# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A

import pytest
import random

class TestBIT2:
    def test_initialization_with_list(self):
        """Test initialization with a list of tuples"""
        values = [(1, 10), (2, 20), (3, 30), (4, 40)]
        bit = BIT2(values)
        
        assert len(bit) == 4
        assert bit[0] == (1, 10)
        assert bit[1] == (2, 20)
        assert bit[2] == (3, 30)
        assert bit[3] == (4, 40)

    def test_initialization_with_size(self):
        """Test initialization with size and zero value"""
        bit = BIT2(5, (0, 0))
        
        assert len(bit) == 5
        # All elements should be zero
        for i in range(5):
            assert bit[i] == (0, 0)

    def test_add_and_sum(self):
        """Test add and sum operations"""
        bit = BIT2(4, (0, 0))
        
        bit.add(0, (1, 10))
        bit.add(1, (2, 20))
        bit.add(2, (3, 30))
        bit.add(3, (4, 40))
        
        assert bit.sum(1) == (1, 10)
        assert bit.sum(2) == (3, 30)
        assert bit.sum(3) == (6, 60)
        assert bit.sum(4) == (10, 100)

    def test_sum_range(self):
        """Test range sum operations"""
        values = [(1, 10), (2, 20), (3, 30), (4, 40)]
        bit = BIT2(values)
        
        assert bit.sum_range(0, 2) == (3, 30)  # Sum of first two
        assert bit.sum_range(1, 3) == (5, 50)  # Sum of middle two
        assert bit.sum_range(2, 4) == (7, 70)  # Sum of last two
        assert bit.sum_range(0, 4) == (10, 100)  # Sum of all
        assert bit.sum_range(1, 1) == (0, 0)   # Empty range

    def test_set_and_get(self):
        """Test set and get operations"""
        bit = BIT2(4, (0, 0))
        
        bit[0] = (1, 10)
        bit[1] = (2, 20)
        bit[2] = (3, 30)
        bit[3] = (4, 40)
        
        assert bit[0] == (1, 10)
        assert bit[1] == (2, 20)
        assert bit[2] == (3, 30)
        assert bit[3] == (4, 40)

    def test_update_and_query(self):
        """Test update operations affect queries correctly"""
        bit = BIT2(4, (0, 0))
        
        # Initial values
        bit[0] = (1, 10)
        bit[1] = (2, 20)
        bit[2] = (3, 30)
        bit[3] = (4, 40)
        
        assert bit.sum(4) == (10, 100)
        
        # Update some values
        bit[1] = (5, 50)
        bit[2] = (6, 60)
        
        assert bit.sum(4) == (16, 160)
        assert bit.sum_range(1, 3) == (11, 110)

    def test_build_functionality(self):
        """Test that build creates correct BIT structure"""
        values = [(1, 10), (2, 20), (3, 30), (4, 40)]
        bit = BIT2(values)
        
        # Test various range sums
        assert bit.sum_range(0, 1) == (1, 10)
        assert bit.sum_range(0, 2) == (3, 30)
        assert bit.sum_range(1, 4) == (9, 90)
        
        # Test individual elements
        for i, expected in enumerate(values):
            assert bit[i] == expected

    def test_prelist(self):
        """Test prelist operation"""
        values = [(1, 10), (2, 20), (3, 30), (4, 40)]
        bit = BIT2(values)
        
        pre = bit.prelist()
        
        # Should have n+1 elements (including 0 at start)
        assert len(pre) == 5
        assert pre[0] == (0, 0)
        assert pre[1] == (1, 10)
        assert pre[2] == (3, 30)
        assert pre[3] == (6, 60)
        assert pre[4] == (10, 100)

    def test_bisect_operations(self):
        """Test bisect_left and bisect_right operations"""
        values = [(1, 10), (2, 20), (3, 30), (4, 40)]
        bit = BIT2(values)
        
        # Test bisect_right - finds rightmost position where cumsum <= v
        assert bit.bisect_right((0, 0)) == 0   # cumsum (0, 0)
        assert bit.bisect_right((1, 10)) == 1   # cumsum (1, 10)
        assert bit.bisect_right((3, 30)) == 2   # cumsum (3, 30)
        assert bit.bisect_right((6, 60)) == 3   # cumsum (6, 60)
        assert bit.bisect_right((10, 100)) == 4  # cumsum (10, 100)
        assert bit.bisect_right((15, 150)) == 4  # cumsum still (10, 100)
        
        # Test bisect_left - finds leftmost position where cumsum >= v
        assert bit.bisect_left((0, 0)) == -1
        assert bit.bisect_left((1, 10)) == 0   # sum(1)=(1,10) >= (1,10)
        assert bit.bisect_left((4, 40)) == 2   # sum(3)=(6,60) >= (4,40)  
        assert bit.bisect_left((7, 70)) == 3   # sum(4)=(10,100) >= (7,70)
        assert bit.bisect_left((11, 110)) == 4  # no cumsum >= (11,110)

    def test_empty_bit(self):
        """Test BIT with size 0"""
        bit = BIT2(0, (0, 0))
        
        assert len(bit) == 0
        assert bit.sum(0) == (0, 0)

    def test_single_element(self):
        """Test BIT with single element"""
        bit = BIT2([(5, 50)])
        
        assert len(bit) == 1
        assert bit[0] == (5, 50)
        assert bit.sum(1) == (5, 50)
        assert bit.sum_range(0, 1) == (5, 50)

    def test_large_bit(self):
        """Test with larger dataset"""
        n = 1000
        values = [(i, i * 10) for i in range(n)]
        bit = BIT2(values)
        
        # Sum of 0..999 = 499500
        assert bit.sum(n) == (499500, 4995000)
        
        # Sum of 0..99 = 4950
        assert bit.sum(100) == (4950, 49500)
        
        # Update and verify
        bit[500] = (1000, 10000)
        expected_sum = 499500 - 500 + 1000
        assert bit.sum(n) == (expected_sum, 4995000 - 5000 + 10000)

    def test_negative_values(self):
        """Test BIT with negative values"""
        values = [(-1, -10), (2, 20), (-3, -30), (4, 40)]
        bit = BIT2(values)
        
        assert bit.sum(4) == (2, 20)
        assert bit.sum_range(0, 2) == (1, 10)
        assert bit.sum_range(2, 4) == (1, 10)

    def test_zero_values(self):
        """Test BIT with zero values"""
        values = [(0, 0), (1, 10), (0, 0), (2, 20)]
        bit = BIT2(values)
        
        assert bit.sum(4) == (3, 30)
        assert bit[0] == (0, 0)
        assert bit[2] == (0, 0)

    def test_stress_random_operations(self):
        """Stress test with random operations"""
        random.seed(42)
        n = 100
        
        # Initialize with zeros
        bit = BIT2(n, (0, 0))
        naive = [(0, 0)] * n
        
        # Perform random operations
        for _ in range(200):
            op = random.choice(['add', 'set', 'query'])
            
            if op == 'add':
                idx = random.randint(0, n-1)
                val = (random.randint(-100, 100), random.randint(-100, 100))
                bit.add(idx, val)
                naive[idx] = (naive[idx][0] + val[0], naive[idx][1] + val[1])
                
            elif op == 'set':
                idx = random.randint(0, n-1)
                val = (random.randint(-100, 100), random.randint(-100, 100))
                bit[idx] = val
                naive[idx] = val
                
            else:  # query
                if random.random() < 0.5:
                    # Test sum
                    k = random.randint(1, n)
                    expected = (sum(naive[i][0] for i in range(k)), 
                               sum(naive[i][1] for i in range(k)))
                    assert bit.sum(k) == expected
                else:
                    # Test range sum
                    l = random.randint(0, n-1)
                    r = random.randint(l, n)
                    expected = (sum(naive[i][0] for i in range(l, r)), 
                               sum(naive[i][1] for i in range(l, r)))
                    assert bit.sum_range(l, r) == expected

    def test_different_types(self):
        """Test with different data types in tuples"""
        # Float values
        values = [(1.5, 10.5), (2.5, 20.5), (3.5, 30.5), (4.5, 40.5)]
        bit = BIT2(values)
        
        assert bit.sum(2) == (4.0, 31.0)
        assert bit.sum_range(1, 3) == (6.0, 51.0)

from cp_library.ds.tree.bit.bit2_cls import BIT2

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()