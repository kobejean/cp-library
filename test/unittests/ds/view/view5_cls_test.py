# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A

import pytest

class TestView5:
    def test_basic_operations(self):
        """Test basic view5 operations"""
        A1 = [1, 2, 3]
        A2 = [10, 20, 30]
        A3 = [100, 200, 300]
        A4 = [1000, 2000, 3000]
        A5 = [10000, 20000, 30000]
        
        # Create view of entire array
        v = view5(A1, A2, A3, A4, A5, 0, 3)
        
        assert len(v) == 3
        assert v[0] == (1, 10, 100, 1000, 10000)
        assert v[1] == (2, 20, 200, 2000, 20000)
        assert v[2] == (3, 30, 300, 3000, 30000)
        
    def test_empty_view(self):
        """Test empty view"""
        A1 = [1, 2, 3]
        A2 = [10, 20, 30]
        A3 = [100, 200, 300]
        A4 = [1000, 2000, 3000]
        A5 = [10000, 20000, 30000]
        
        v = view5(A1, A2, A3, A4, A5, 1, 1)
        assert len(v) == 0
        
    def test_appendleft_popleft(self):
        """Test appendleft and popleft operations"""
        A1 = [0, 1, 2, 3]
        A2 = [0, 10, 20, 30]
        A3 = [0, 100, 200, 300]
        A4 = [0, 1000, 2000, 3000]
        A5 = [0, 10000, 20000, 30000]
        
        v = view5(A1, A2, A3, A4, A5, 1, 3)
        
        # Test appendleft
        v.appendleft((5, 50, 500, 5000, 50000))
        assert len(v) == 3
        assert v[0] == (5, 50, 500, 5000, 50000)
        
        # Test popleft
        result = v.popleft()
        assert result == (5, 50, 500, 5000, 50000)
        assert len(v) == 2

from cp_library.ds.view.view5_cls import view5

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()