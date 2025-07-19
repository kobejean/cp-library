# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb

import pytest
import random

class TestBIT3:
    def test_basic_operations(self):
        """Test basic BIT3 operations"""
        values = [(1, 10, 100), (2, 20, 200), (3, 30, 300), (4, 40, 400)]
        bit = BIT3(values)
        
        assert len(bit) == 4
        assert bit[0] == (1, 10, 100)
        assert bit[1] == (2, 20, 200)
        assert bit[2] == (3, 30, 300)
        assert bit[3] == (4, 40, 400)
        
        assert bit.sum(1) == (1, 10, 100)
        assert bit.sum(2) == (3, 30, 300)
        assert bit.sum(3) == (6, 60, 600)
        assert bit.sum(4) == (10, 100, 1000)

    def test_sum_range(self):
        """Test range sum operations"""
        values = [(1, 10, 100), (2, 20, 200), (3, 30, 300), (4, 40, 400)]
        bit = BIT3(values)
        
        assert bit.sum_range(0, 2) == (3, 30, 300)
        assert bit.sum_range(1, 3) == (5, 50, 500)
        assert bit.sum_range(2, 4) == (7, 70, 700)
        assert bit.sum_range(0, 4) == (10, 100, 1000)

    def test_add_operations(self):
        """Test add operations"""
        bit = BIT3(4, (0, 0, 0))
        
        bit.add(0, (1, 10, 100))
        bit.add(1, (2, 20, 200))
        assert bit.sum(2) == (3, 30, 300)
        
        bit.add(1, (1, 10, 100))  # Add more to index 1
        assert bit.sum(2) == (4, 40, 400)

from cp_library.ds.tree.bit.bit3_cls import BIT3

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()