# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb

import pytest

class TestBIT5:
    def test_basic_operations(self):
        """Test basic BIT5 operations"""
        values = [(1, 10, 100, 1000, 10000), (2, 20, 200, 2000, 20000)]
        bit = BIT5(values)
        
        assert len(bit) == 2
        assert bit[0] == (1, 10, 100, 1000, 10000)
        assert bit[1] == (2, 20, 200, 2000, 20000)
        
        assert bit.sum(1) == (1, 10, 100, 1000, 10000)
        assert bit.sum(2) == (3, 30, 300, 3000, 30000)

    def test_add_operations(self):
        """Test add operations"""
        bit = BIT5(3, (0, 0, 0, 0, 0))
        
        bit.add(0, (5, 50, 500, 5000, 50000))
        bit.add(1, (3, 30, 300, 3000, 30000))
        
        assert bit[0] == (5, 50, 500, 5000, 50000)
        assert bit[1] == (3, 30, 300, 3000, 30000)
        assert bit.sum(2) == (8, 80, 800, 8000, 80000)

from cp_library.ds.tree.bit.bit5_cls import BIT5

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()