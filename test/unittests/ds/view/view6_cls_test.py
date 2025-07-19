# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb

import pytest

class TestView6:
    def test_basic_operations(self):
        """Test basic view6 operations"""
        A1 = [1, 2, 3]
        A2 = [10, 20, 30]
        A3 = [100, 200, 300]
        A4 = [1000, 2000, 3000]
        A5 = [10000, 20000, 30000]
        A6 = [100000, 200000, 300000]
        
        # Create view of slice [1:3]
        v = view6(A1, A2, A3, A4, A5, A6, 1, 3)
        
        assert len(v) == 2
        assert v[0] == (2, 20, 200, 2000, 20000, 200000)
        assert v[1] == (3, 30, 300, 3000, 30000, 300000)
        
    def test_setitem(self):
        """Test setting items in view"""
        A1 = [1, 2]
        A2 = [10, 20]
        A3 = [100, 200]
        A4 = [1000, 2000]
        A5 = [10000, 20000]
        A6 = [100000, 200000]
        
        v = view6(A1, A2, A3, A4, A5, A6, 0, 2)
        v[0] = (9, 90, 900, 9000, 90000, 900000)
        
        # Check all arrays are updated
        assert A1[0] == 9
        assert A2[0] == 90
        assert A3[0] == 900
        assert A4[0] == 9000
        assert A5[0] == 90000
        assert A6[0] == 900000
        
    def test_reverse(self):
        """Test reverse operation"""
        A1 = [1, 2, 3, 4]
        A2 = [10, 20, 30, 40]
        A3 = [100, 200, 300, 400]
        A4 = [1000, 2000, 3000, 4000]
        A5 = [10000, 20000, 30000, 40000]
        A6 = [100000, 200000, 300000, 400000]
        
        v = view6(A1, A2, A3, A4, A5, A6, 1, 3)
        v.reverse()
        
        assert v[0] == (3, 30, 300, 3000, 30000, 300000)
        assert v[1] == (2, 20, 200, 2000, 20000, 200000)

from cp_library.ds.view.view6_cls import view6

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()