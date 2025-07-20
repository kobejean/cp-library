# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A

import pytest

class TestBIT4:
    def test_basic_operations(self):
        """Test basic BIT4 operations"""
        values = [(1, 10, 100, 1000), (2, 20, 200, 2000), (3, 30, 300, 3000)]
        bit = BIT4(values)
        
        assert len(bit) == 3
        assert bit[0] == (1, 10, 100, 1000)
        assert bit[1] == (2, 20, 200, 2000)
        assert bit[2] == (3, 30, 300, 3000)
        
        assert bit.sum(1) == (1, 10, 100, 1000)
        assert bit.sum(2) == (3, 30, 300, 3000)
        assert bit.sum(3) == (6, 60, 600, 6000)

    def test_sum_range(self):
        """Test range sum operations"""
        values = [(1, 10, 100, 1000), (2, 20, 200, 2000), (3, 30, 300, 3000)]
        bit = BIT4(values)
        
        assert bit.sum_range(0, 2) == (3, 30, 300, 3000)
        assert bit.sum_range(1, 3) == (5, 50, 500, 5000)

    def test_initialization_with_size(self):
        """Test initialization with size"""
        bit = BIT4(5, (0, 0, 0, 0))
        assert len(bit) == 5
        for i in range(5):
            assert bit[i] == (0, 0, 0, 0)

from cp_library.ds.tree.bit.bit4_cls import BIT4

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()