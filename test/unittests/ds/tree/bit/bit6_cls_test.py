# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A

import pytest

class TestBIT6:
    def test_basic_operations(self):
        """Test basic BIT6 operations"""
        values = [(1, 10, 100, 1000, 10000, 100000), (2, 20, 200, 2000, 20000, 200000)]
        bit = BIT6(values)
        
        assert len(bit) == 2
        assert bit[0] == (1, 10, 100, 1000, 10000, 100000)
        assert bit[1] == (2, 20, 200, 2000, 20000, 200000)
        
        assert bit.sum(1) == (1, 10, 100, 1000, 10000, 100000)
        assert bit.sum(2) == (3, 30, 300, 3000, 30000, 300000)

    def test_set_operations(self):
        """Test set operations"""
        bit = BIT6(2, (0, 0, 0, 0, 0, 0))
        
        bit[0] = (7, 70, 700, 7000, 70000, 700000)
        bit[1] = (8, 80, 800, 8000, 80000, 800000)
        
        assert bit[0] == (7, 70, 700, 7000, 70000, 700000)
        assert bit[1] == (8, 80, 800, 8000, 80000, 800000)
        assert bit.sum_range(0, 2) == (15, 150, 1500, 15000, 150000, 1500000)

from cp_library.ds.tree.bit.bit6_cls import BIT6

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()