# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb

import pytest

class TestView3:
    def test_basic_operations(self):
        """Test basic view3 operations"""
        A1 = [1, 2, 3, 4, 5]
        A2 = [10, 20, 30, 40, 50]
        A3 = [100, 200, 300, 400, 500]
        
        # Create view of slice [1:4]
        v = view3(A1, A2, A3, 1, 4)
        
        assert len(v) == 3
        assert v[0] == (2, 20, 200)
        assert v[1] == (3, 30, 300)
        assert v[2] == (4, 40, 400)
        
    def test_setitem(self):
        """Test setting items in view"""
        A1 = [1, 2, 3, 4, 5]
        A2 = [10, 20, 30, 40, 50]
        A3 = [100, 200, 300, 400, 500]
        
        v = view3(A1, A2, A3, 1, 4)
        v[0] = (99, 990, 9900)
        
        # Check view reflects change
        assert v[0] == (99, 990, 9900)
        
        # Check underlying arrays are modified
        assert A1[1] == 99
        assert A2[1] == 990
        assert A3[1] == 9900
        
    def test_append_pop(self):
        """Test append and pop operations"""
        A1 = [1, 2, 3, 0, 0]
        A2 = [10, 20, 30, 0, 0]
        A3 = [100, 200, 300, 0, 0]
        
        v = view3(A1, A2, A3, 0, 3)
        
        # Test append
        v.append((4, 40, 400))
        assert len(v) == 4
        assert v[3] == (4, 40, 400)
        
        # Test pop
        result = v.pop()
        assert result == (4, 40, 400)
        assert len(v) == 3
        
    def test_appendleft_popleft(self):
        """Test appendleft and popleft operations"""
        A1 = [0, 1, 2, 3, 4]
        A2 = [0, 10, 20, 30, 40]
        A3 = [0, 100, 200, 300, 400]
        
        v = view3(A1, A2, A3, 1, 4)
        
        # Test appendleft
        v.appendleft((5, 50, 500))
        assert len(v) == 4
        assert v[0] == (5, 50, 500)
        
        # Test popleft
        result = v.popleft()
        assert result == (5, 50, 500)
        assert len(v) == 3
        
    def test_reverse(self):
        """Test reverse operation"""
        A1 = [1, 2, 3, 4, 5]
        A2 = [10, 20, 30, 40, 50]
        A3 = [100, 200, 300, 400, 500]
        
        v = view3(A1, A2, A3, 1, 4)
        v.reverse()
        
        assert v[0] == (4, 40, 400)
        assert v[1] == (3, 30, 300)
        assert v[2] == (2, 20, 200)
        
    def test_set_range(self):
        """Test set_range operation"""
        A1 = [1, 2, 3, 4, 5]
        A2 = [10, 20, 30, 40, 50]
        A3 = [100, 200, 300, 400, 500]
        
        v = view3(A1, A2, A3, 1, 3)
        assert len(v) == 2
        
        v.set_range(0, 5)
        assert len(v) == 5
        assert v[0] == (1, 10, 100)
        assert v[4] == (5, 50, 500)
        
    def test_validate(self):
        """Test validate operation"""
        A1 = [1, 2, 3]
        A2 = [10, 20, 30]
        A3 = [100, 200, 300]
        
        v = view3(A1, A2, A3, 0, 3)
        assert v.validate() == True
        
        # Invalid range
        v.set_range(-1, 3)
        assert v.validate() == False
        
        v.set_range(0, 4)
        assert v.validate() == False
        
    def test_index_error(self):
        """Test index error handling"""
        A1 = [1, 2, 3]
        A2 = [10, 20, 30]
        A3 = [100, 200, 300]
        
        v = view3(A1, A2, A3, 0, 2)
        
        with pytest.raises(IndexError):
            _ = v[2]
            
        with pytest.raises(IndexError):
            _ = v[-1]

from cp_library.ds.view.view3_cls import view3

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()