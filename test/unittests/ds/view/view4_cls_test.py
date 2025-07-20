# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A

import pytest

class TestView4:
    def test_basic_operations(self):
        """Test basic view4 operations"""
        A1 = [1, 2, 3, 4, 5]
        A2 = [10, 20, 30, 40, 50]
        A3 = [100, 200, 300, 400, 500]
        A4 = [1000, 2000, 3000, 4000, 5000]
        
        # Create view of slice [2:5]
        v = view4(A1, A2, A3, A4, 2, 5)
        
        assert len(v) == 3
        assert v[0] == (3, 30, 300, 3000)
        assert v[1] == (4, 40, 400, 4000)
        assert v[2] == (5, 50, 500, 5000)
        
    def test_setitem(self):
        """Test setting items in view"""
        A1 = [1, 2, 3, 4]
        A2 = [10, 20, 30, 40]
        A3 = [100, 200, 300, 400]
        A4 = [1000, 2000, 3000, 4000]
        
        v = view4(A1, A2, A3, A4, 0, 3)
        v[1] = (77, 770, 7700, 77000)
        
        # Check view reflects change
        assert v[1] == (77, 770, 7700, 77000)
        
        # Check underlying arrays are modified
        assert A1[1] == 77
        assert A2[1] == 770
        assert A3[1] == 7700
        assert A4[1] == 77000
        
    def test_append_pop(self):
        """Test append and pop operations"""
        A1 = [1, 2, 0, 0, 0]
        A2 = [10, 20, 0, 0, 0]
        A3 = [100, 200, 0, 0, 0]
        A4 = [1000, 2000, 0, 0, 0]
        
        v = view4(A1, A2, A3, A4, 0, 2)
        
        # Test append
        v.append((3, 30, 300, 3000))
        assert len(v) == 3
        assert v[2] == (3, 30, 300, 3000)
        
        # Test pop
        result = v.pop()
        assert result == (3, 30, 300, 3000)
        assert len(v) == 2
        
    def test_reverse(self):
        """Test reverse operation"""
        A1 = [1, 2, 3, 4]
        A2 = [10, 20, 30, 40]
        A3 = [100, 200, 300, 400]
        A4 = [1000, 2000, 3000, 4000]
        
        v = view4(A1, A2, A3, A4, 0, 4)
        v.reverse()
        
        assert v[0] == (4, 40, 400, 4000)
        assert v[1] == (3, 30, 300, 3000)
        assert v[2] == (2, 20, 200, 2000)
        assert v[3] == (1, 10, 100, 1000)

from cp_library.ds.view.view4_cls import view4

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()