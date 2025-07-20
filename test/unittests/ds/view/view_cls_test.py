# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A

import pytest
import random

class TestView:
    def test_initialization(self):
        """Test basic initialization of view"""
        data = [1, 2, 3, 4, 5]
        v = view(data, 1, 4)
        
        assert v.A is data
        assert v.l == 1
        assert v.r == 4
        assert len(v) == 3

    def test_len(self):
        """Test __len__ method"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        # Test different ranges
        assert len(view(data, 0, 5)) == 5
        assert len(view(data, 2, 7)) == 5
        assert len(view(data, 0, 10)) == 10
        assert len(view(data, 5, 5)) == 0  # Empty range

    def test_getitem(self):
        """Test __getitem__ method"""
        data = [10, 20, 30, 40, 50]
        v = view(data, 1, 4)  # View of [20, 30, 40]
        
        assert v[0] == 20
        assert v[1] == 30
        assert v[2] == 40
        
        # Test IndexError for out of bounds
        with pytest.raises(IndexError):
            v[3]
        with pytest.raises(IndexError):
            v[-1]

    def test_setitem(self):
        """Test __setitem__ method"""
        data = [10, 20, 30, 40, 50]
        v = view(data, 1, 4)  # View of [20, 30, 40]
        
        v[0] = 25
        v[1] = 35
        v[2] = 45
        
        assert data == [10, 25, 35, 45, 50]
        assert v[0] == 25
        assert v[1] == 35
        assert v[2] == 45

    def test_contains(self):
        """Test __contains__ method"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        v = view(data, 2, 6)  # View of [3, 4, 5, 6]
        
        assert 3 in v
        assert 4 in v
        assert 5 in v
        assert 6 in v
        assert 1 not in v  # Outside view range
        assert 2 not in v  # Outside view range
        assert 7 not in v  # Outside view range
        assert 10 not in v  # Not in data at all

    def test_set_range(self):
        """Test set_range method"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        v = view(data, 2, 5)
        
        assert len(v) == 3
        assert v[0] == 3
        
        # Change the range
        v.set_range(4, 8)
        assert len(v) == 4
        assert v[0] == 5
        assert v[1] == 6
        assert v[2] == 7
        assert v[3] == 8

    def test_index(self):
        """Test index method"""
        data = [10, 20, 30, 40, 50, 60, 70]
        v = view(data, 2, 6)  # View of [30, 40, 50, 60]
        
        assert v.index(30) == 0
        assert v.index(40) == 1
        assert v.index(50) == 2
        assert v.index(60) == 3
        
        # Test ValueError for element not in view
        with pytest.raises(ValueError):
            v.index(10)  # Outside view range
        with pytest.raises(ValueError):
            v.index(70)  # Outside view range
        with pytest.raises(ValueError):
            v.index(100)  # Not in data at all

    def test_reverse(self):
        """Test reverse method"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        v = view(data, 2, 7)  # View of [3, 4, 5, 6, 7]
        
        v.reverse()
        
        # Check that the view is reversed
        assert v[0] == 7
        assert v[1] == 6
        assert v[2] == 5
        assert v[3] == 4
        assert v[4] == 3
        
        # Check that the underlying array is modified
        assert data == [1, 2, 7, 6, 5, 4, 3, 8, 9]

    def test_sort(self):
        """Test sort method"""
        data = [1, 5, 2, 8, 3, 9, 4, 6, 7]
        v = view(data, 2, 7)  # View of [2, 8, 3, 9, 4]
        
        v.sort()
        
        # Check that the view is sorted
        assert v[0] == 2
        assert v[1] == 3
        assert v[2] == 4
        assert v[3] == 8
        assert v[4] == 9
        
        # Check that the underlying array is modified correctly
        assert data == [1, 5, 2, 3, 4, 8, 9, 6, 7]

    def test_sort_with_parameters(self):
        """Test sort method with reverse parameter"""
        data = [1, 5, 2, 8, 3, 9, 4, 6, 7]
        v = view(data, 2, 7)  # View of [2, 8, 3, 9, 4]
        
        v.sort(reverse=True)
        
        # Check that the view is sorted in reverse
        assert v[0] == 9
        assert v[1] == 8
        assert v[2] == 4
        assert v[3] == 3
        assert v[4] == 2
        
        # Check that the underlying array is modified correctly
        assert data == [1, 5, 9, 8, 4, 3, 2, 6, 7]

    def test_pop(self):
        """Test pop method"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        v = view(data, 2, 6)  # View of [3, 4, 5, 6]
        
        assert len(v) == 4
        
        # Pop from the end
        popped = v.pop()
        assert popped == 6
        assert len(v) == 3
        assert v[2] == 5  # Last element is now 5
        
        # Pop again
        popped = v.pop()
        assert popped == 5
        assert len(v) == 2

    def test_append(self):
        """Test append method"""
        data = [1, 2, 3, 4, 5, 0, 0, 0, 9]  # Extra space for appending
        v = view(data, 2, 5)  # View of [3, 4, 5]
        
        assert len(v) == 3
        
        # Append to the end
        v.append(6)
        assert len(v) == 4
        assert v[3] == 6
        assert data[5] == 6  # Check underlying array
        
        # Append again
        v.append(7)
        assert len(v) == 5
        assert v[4] == 7

    def test_popleft(self):
        """Test popleft method"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        v = view(data, 2, 6)  # View of [3, 4, 5, 6]
        
        assert len(v) == 4
        
        # Pop from the beginning
        popped = v.popleft()
        assert popped == 3
        assert len(v) == 3
        assert v[0] == 4  # First element is now 4
        
        # Pop again
        popped = v.popleft()
        assert popped == 4
        assert len(v) == 2
        assert v[0] == 5

    def test_appendleft(self):
        """Test appendleft method"""
        data = [0, 0, 1, 2, 3, 4, 5, 6, 7]  # Extra space at beginning
        v = view(data, 4, 7)  # View of [3, 4, 5]
        
        assert len(v) == 3
        assert v[0] == 3
        
        # Append to the beginning
        v.appendleft(2)
        assert len(v) == 4
        assert v[0] == 2
        assert v[1] == 3
        assert data[3] == 2  # Check underlying array
        
        # Append again
        v.appendleft(1)
        assert len(v) == 5
        assert v[0] == 1
        assert v[1] == 2

    def test_validate(self):
        """Test validate method"""
        data = [1, 2, 3, 4, 5]
        
        # Valid ranges
        v1 = view(data, 0, 5)
        assert v1.validate() == True
        
        v2 = view(data, 2, 4)
        assert v2.validate() == True
        
        v3 = view(data, 3, 3)  # Empty range
        assert v3.validate() == True
        
        # Invalid ranges
        v4 = view(data, -1, 3)
        assert v4.validate() == False
        
        v5 = view(data, 2, 6)  # r > len(A)
        assert v5.validate() == False
        
        v6 = view(data, 3, 2)  # l > r
        assert v6.validate() == False

    def test_empty_view(self):
        """Test operations on empty view"""
        data = [1, 2, 3, 4, 5]
        v = view(data, 3, 3)  # Empty view
        
        assert len(v) == 0
        
        # Test that operations on empty view behave correctly
        with pytest.raises(IndexError):
            v[0]
        
        assert 1 not in v
        assert 3 not in v

    def test_edge_cases(self):
        """Test edge cases"""
        # Single element view
        data = [10, 20, 30, 40, 50]
        v = view(data, 2, 3)  # View of [30]
        
        assert len(v) == 1
        assert v[0] == 30
        assert 30 in v
        assert 20 not in v
        
        # Modify single element
        v[0] = 35
        assert data == [10, 20, 35, 40, 50]

    def test_view_operations_sequence(self):
        """Test a sequence of operations"""
        data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        v = view(data, 2, 8)  # View of [30, 40, 50, 60, 70, 80]
        
        # Initial state
        assert len(v) == 6
        assert v[0] == 30
        assert v[5] == 80
        
        # Modify some elements
        v[1] = 45
        v[3] = 65
        assert data[3] == 45
        assert data[5] == 65
        
        # Pop and append
        popped = v.pop()
        assert popped == 80
        assert len(v) == 5
        
        v.append(85)
        assert len(v) == 6
        assert v[5] == 85
        
        # Reverse
        v.reverse()
        assert v[0] == 85
        assert v[5] == 30

    def test_with_different_types(self):
        """Test view with different data types"""
        # String data
        str_data = ['a', 'b', 'c', 'd', 'e', 'f']
        str_view = view(str_data, 1, 4)  # ['b', 'c', 'd']
        
        assert len(str_view) == 3
        assert str_view[0] == 'b'
        assert 'c' in str_view
        assert 'a' not in str_view
        
        str_view.sort()
        assert str_view[0] == 'b'
        assert str_view[1] == 'c'
        assert str_view[2] == 'd'
        
        # Float data
        float_data = [1.1, 2.2, 3.3, 4.4, 5.5]
        float_view = view(float_data, 1, 4)  # [2.2, 3.3, 4.4]
        
        assert len(float_view) == 3
        assert float_view[1] == 3.3
        assert 2.2 in float_view

    def test_large_data_operations(self):
        """Test operations on larger datasets"""
        # Create large dataset
        data = list(range(1000))
        v = view(data, 100, 900)  # 800 elements
        
        assert len(v) == 800
        assert v[0] == 100
        assert v[799] == 899
        
        # Test contains on large dataset
        assert 500 in v
        assert 50 not in v
        assert 950 not in v
        
        # Test index on large dataset
        assert v.index(200) == 100
        assert v.index(600) == 500

    def test_random_operations(self):
        """Test random operations for robustness"""
        random.seed(42)  # For reproducibility
        
        # Create test data
        data = list(range(100))
        original_data = data.copy()
        
        # Create view
        start, end = 20, 80
        v = view(data, start, end)
        
        # Perform random operations
        for _ in range(50):
            op = random.choice(['read', 'write', 'contains'])
            
            if op == 'read' and len(v) > 0:
                idx = random.randint(0, len(v) - 1)
                val = v[idx]
                assert val == data[start + idx]
                
            elif op == 'write' and len(v) > 0:
                idx = random.randint(0, len(v) - 1)
                new_val = random.randint(1000, 2000)
                v[idx] = new_val
                assert data[start + idx] == new_val
                
            elif op == 'contains':
                search_val = random.choice(original_data)
                result = search_val in v
                # Verify manually
                expected = any(data[i] == search_val for i in range(start, min(start + len(v), len(data))))
                assert result == expected

    def test_view_modification_boundary_safety(self):
        """Test that view modifications don't affect data outside the view"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        original = data.copy()
        
        v = view(data, 3, 7)  # View of [4, 5, 6, 7]
        
        # Modify view
        v[0] = 40
        v[1] = 50
        v[2] = 60
        v[3] = 70
        
        # Check that only the view range was modified
        assert data[0:3] == original[0:3]  # Before view unchanged
        assert data[7:] == original[7:]    # After view unchanged
        assert data[3:7] == [40, 50, 60, 70]  # View range changed

from cp_library.ds.view.view_cls import view

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()