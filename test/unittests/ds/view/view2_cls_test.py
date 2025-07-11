# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb

import pytest
import random

class TestView2:
    def test_initialization(self):
        """Test basic initialization of view2"""
        A = [1, 2, 3, 4, 5]
        B = ['a', 'b', 'c', 'd', 'e']
        v = view2(A, B, 1, 4)
        
        assert v.A is A
        assert v.B is B
        assert v.l == 1
        assert v.r == 4
        assert len(v) == 3

    def test_len(self):
        """Test __len__ method"""
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        B = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        
        # Test different ranges
        assert len(view2(A, B, 0, 5)) == 5
        assert len(view2(A, B, 2, 7)) == 5
        assert len(view2(A, B, 0, 10)) == 10
        assert len(view2(A, B, 5, 5)) == 0  # Empty range

    def test_getitem(self):
        """Test __getitem__ method"""
        A = [10, 20, 30, 40, 50]
        B = ['x', 'y', 'z', 'w', 'v']
        v = view2(A, B, 1, 4)  # View of [(20,'y'), (30,'z'), (40,'w')]
        
        assert v[0] == (20, 'y')
        assert v[1] == (30, 'z')
        assert v[2] == (40, 'w')
        
        # Test IndexError for out of bounds
        with pytest.raises(IndexError):
            v[3]
        with pytest.raises(IndexError):
            v[-1]

    def test_setitem(self):
        """Test __setitem__ method"""
        A = [10, 20, 30, 40, 50]
        B = ['x', 'y', 'z', 'w', 'v']
        v = view2(A, B, 1, 4)  # View of [(20,'y'), (30,'z'), (40,'w')]
        
        v[0] = (25, 'Y')
        v[1] = (35, 'Z')
        v[2] = (45, 'W')
        
        assert A == [10, 25, 35, 45, 50]
        assert B == ['x', 'Y', 'Z', 'W', 'v']
        assert v[0] == (25, 'Y')
        assert v[1] == (35, 'Z')
        assert v[2] == (45, 'W')

    def test_contains_not_implemented(self):
        """Test that __contains__ raises NotImplemented"""
        A = [1, 2, 3, 4, 5]
        B = ['a', 'b', 'c', 'd', 'e']
        v = view2(A, B, 1, 4)
        
        with pytest.raises(TypeError):  # NotImplemented raises TypeError
            (2, 'b') in v

    def test_index_not_implemented(self):
        """Test that index raises NotImplemented"""
        A = [1, 2, 3, 4, 5]
        B = ['a', 'b', 'c', 'd', 'e']
        v = view2(A, B, 1, 4)
        
        with pytest.raises(TypeError):  # NotImplemented raises TypeError
            v.index((2, 'b'))

    def test_set_range(self):
        """Test set_range method"""
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        B = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        v = view2(A, B, 2, 5)
        
        assert len(v) == 3
        assert v[0] == (3, 30)
        
        # Change the range
        v.set_range(4, 8)
        assert len(v) == 4
        assert v[0] == (5, 50)
        assert v[1] == (6, 60)
        assert v[2] == (7, 70)
        assert v[3] == (8, 80)

    def test_reverse(self):
        """Test reverse method"""
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        B = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        v = view2(A, B, 2, 7)  # View of [(3,30), (4,40), (5,50), (6,60), (7,70)]
        
        v.reverse()
        
        # Check that the view is reversed
        assert v[0] == (7, 70)
        assert v[1] == (6, 60)
        assert v[2] == (5, 50)
        assert v[3] == (4, 40)
        assert v[4] == (3, 30)
        
        # Check that the underlying arrays are modified
        assert A == [1, 2, 7, 6, 5, 4, 3, 8, 9]
        assert B == [10, 20, 70, 60, 50, 40, 30, 80, 90]

    def test_sort(self):
        """Test sort method"""
        A = [1, 5, 2, 8, 3, 9, 4, 6, 7]
        B = [10, 50, 20, 80, 30, 90, 40, 60, 70]
        v = view2(A, B, 2, 7)  # View of [(2,20), (8,80), (3,30), (9,90), (4,40)]
        
        v.sort()
        
        # Check that the view is sorted by A values
        assert v[0] == (2, 20)
        assert v[1] == (3, 30)
        assert v[2] == (4, 40)
        assert v[3] == (8, 80)
        assert v[4] == (9, 90)
        
        # Check that the underlying arrays are modified correctly
        assert A == [1, 5, 2, 3, 4, 8, 9, 6, 7]
        assert B == [10, 50, 20, 30, 40, 80, 90, 60, 70]

    def test_sort_reverse(self):
        """Test sort method with reverse=True"""
        A = [1, 5, 2, 8, 3, 9, 4, 6, 7]
        B = [10, 50, 20, 80, 30, 90, 40, 60, 70]
        v = view2(A, B, 2, 7)  # View of [(2,20), (8,80), (3,30), (9,90), (4,40)]
        
        v.sort(reverse=True)
        
        # Check that the view is sorted in reverse by A values
        assert v[0] == (9, 90)
        assert v[1] == (8, 80)
        assert v[2] == (4, 40)
        assert v[3] == (3, 30)
        assert v[4] == (2, 20)
        
        # Check that the underlying arrays are modified correctly
        assert A == [1, 5, 9, 8, 4, 3, 2, 6, 7]
        assert B == [10, 50, 90, 80, 40, 30, 20, 60, 70]

    def test_pop(self):
        """Test pop method"""
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        B = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        v = view2(A, B, 2, 6)  # View of [(3,30), (4,40), (5,50), (6,60)]
        
        assert len(v) == 4
        
        # Pop from the end
        popped = v.pop()
        assert popped == (6, 60)
        assert len(v) == 3
        assert v[2] == (5, 50)  # Last element is now (5,50)
        
        # Pop again
        popped = v.pop()
        assert popped == (5, 50)
        assert len(v) == 2

    def test_append(self):
        """Test append method"""
        A = [1, 2, 3, 4, 5, 0, 0, 0, 9]  # Extra space for appending
        B = [10, 20, 30, 40, 50, 0, 0, 0, 90]
        v = view2(A, B, 2, 5)  # View of [(3,30), (4,40), (5,50)]
        
        assert len(v) == 3
        
        # Append to the end
        v.append((6, 60))
        assert len(v) == 4
        assert v[3] == (6, 60)
        assert A[5] == 6  # Check underlying arrays
        assert B[5] == 60
        
        # Append again
        v.append((7, 70))
        assert len(v) == 5
        assert v[4] == (7, 70)

    def test_popleft(self):
        """Test popleft method"""
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        B = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        v = view2(A, B, 2, 6)  # View of [(3,30), (4,40), (5,50), (6,60)]
        
        assert len(v) == 4
        
        # Pop from the beginning
        popped = v.popleft()
        assert popped == (3, 30)
        assert len(v) == 3
        assert v[0] == (4, 40)  # First element is now (4,40)
        
        # Pop again
        popped = v.popleft()
        assert popped == (4, 40)
        assert len(v) == 2
        assert v[0] == (5, 50)

    def test_appendleft(self):
        """Test appendleft method"""
        A = [0, 0, 1, 2, 3, 4, 5, 6, 7]  # Extra space at beginning
        B = [0, 0, 10, 20, 30, 40, 50, 60, 70]
        v = view2(A, B, 4, 7)  # View of [(3,30), (4,40), (5,50)]
        
        assert len(v) == 3
        assert v[0] == (3, 30)
        
        # Append to the beginning
        v.appendleft((2, 20))
        assert len(v) == 4
        assert v[0] == (2, 20)
        assert v[1] == (3, 30)
        assert A[3] == 2  # Check underlying arrays
        assert B[3] == 20
        
        # Append again
        v.appendleft((1, 10))
        assert len(v) == 5
        assert v[0] == (1, 10)
        assert v[1] == (2, 20)

    def test_validate(self):
        """Test validate method"""
        A = [1, 2, 3, 4, 5]
        B = [10, 20, 30, 40, 50]
        
        # Valid ranges
        v1 = view2(A, B, 0, 5)
        assert v1.validate() == True
        
        v2 = view2(A, B, 2, 4)
        assert v2.validate() == True
        
        v3 = view2(A, B, 3, 3)  # Empty range
        assert v3.validate() == True
        
        # Invalid ranges
        v4 = view2(A, B, -1, 3)
        assert v4.validate() == False
        
        v5 = view2(A, B, 2, 6)  # r > len(A)
        assert v5.validate() == False
        
        v6 = view2(A, B, 3, 2)  # l > r
        assert v6.validate() == False

    def test_empty_view(self):
        """Test operations on empty view"""
        A = [1, 2, 3, 4, 5]
        B = [10, 20, 30, 40, 50]
        v = view2(A, B, 3, 3)  # Empty view
        
        assert len(v) == 0
        
        # Test that operations on empty view behave correctly
        with pytest.raises(IndexError):
            v[0]

    def test_edge_cases(self):
        """Test edge cases"""
        # Single element view
        A = [10, 20, 30, 40, 50]
        B = ['a', 'b', 'c', 'd', 'e']
        v = view2(A, B, 2, 3)  # View of [(30, 'c')]
        
        assert len(v) == 1
        assert v[0] == (30, 'c')
        
        # Modify single element
        v[0] = (35, 'C')
        assert A == [10, 20, 35, 40, 50]
        assert B == ['a', 'b', 'C', 'd', 'e']

    def test_view_operations_sequence(self):
        """Test a sequence of operations"""
        A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        v = view2(A, B, 2, 8)  # View of [(30,3), (40,4), (50,5), (60,6), (70,7), (80,8)]
        
        # Initial state
        assert len(v) == 6
        assert v[0] == (30, 3)
        assert v[5] == (80, 8)
        
        # Modify some elements
        v[1] = (45, 14)
        v[3] = (65, 16)
        assert A[3] == 45
        assert B[3] == 14
        assert A[5] == 65
        assert B[5] == 16
        
        # Pop and append
        popped = v.pop()
        assert popped == (80, 8)
        assert len(v) == 5
        
        v.append((85, 18))
        assert len(v) == 6
        assert v[5] == (85, 18)
        
        # Reverse
        v.reverse()
        assert v[0] == (85, 18)
        assert v[5] == (30, 3)

    def test_with_different_types(self):
        """Test view2 with different data types"""
        # Mixed types
        A = [1, 2, 3, 4, 5, 6]
        B = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
        v = view2(A, B, 1, 4)  # [(2, 2.2), (3, 3.3), (4, 4.4)]
        
        assert len(v) == 3
        assert v[0] == (2, 2.2)
        assert v[1] == (3, 3.3)
        assert v[2] == (4, 4.4)
        
        v.sort()
        assert v[0] == (2, 2.2)
        assert v[1] == (3, 3.3)
        assert v[2] == (4, 4.4)
        
        # Integer pairs (since the sort function requires integer keys)
        A = [5, 2, 4, 1, 3]
        B = [50, 20, 40, 10, 30]
        v = view2(A, B, 1, 4)  # [(2, 20), (4, 40), (1, 10)]
        
        assert len(v) == 3
        assert v[1] == (4, 40)
        
        v.sort()  # Should sort by A values
        assert v[0] == (1, 10)
        assert v[1] == (2, 20)
        assert v[2] == (4, 40)

    def test_large_data_operations(self):
        """Test operations on larger datasets"""
        # Create large dataset
        A = list(range(1000))
        B = list(range(1000, 2000))
        v = view2(A, B, 100, 900)  # 800 elements
        
        assert len(v) == 800
        assert v[0] == (100, 1100)
        assert v[799] == (899, 1899)
        
        # Test modification
        v[100] = (9999, 8888)
        assert A[200] == 9999
        assert B[200] == 8888

    def test_random_operations(self):
        """Test random operations for robustness"""
        random.seed(42)  # For reproducibility
        
        # Create test data
        A = list(range(100))
        B = list(range(100, 200))
        original_A = A.copy()
        original_B = B.copy()
        
        # Create view
        start, end = 20, 80
        v = view2(A, B, start, end)
        
        # Perform random operations
        for _ in range(50):
            op = random.choice(['read', 'write'])
            
            if op == 'read' and len(v) > 0:
                idx = random.randint(0, len(v) - 1)
                val_a, val_b = v[idx]
                assert val_a == A[start + idx]
                assert val_b == B[start + idx]
                
            elif op == 'write' and len(v) > 0:
                idx = random.randint(0, len(v) - 1)
                new_val_a = random.randint(1000, 2000)
                new_val_b = random.randint(2000, 3000)
                v[idx] = (new_val_a, new_val_b)
                assert A[start + idx] == new_val_a
                assert B[start + idx] == new_val_b

    def test_view_modification_boundary_safety(self):
        """Test that view modifications don't affect data outside the view"""
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        original_A = A.copy()
        original_B = B.copy()
        
        v = view2(A, B, 3, 7)  # View of [(4,14), (5,15), (6,16), (7,17)]
        
        # Modify view
        v[0] = (40, 140)
        v[1] = (50, 150)
        v[2] = (60, 160)
        v[3] = (70, 170)
        
        # Check that only the view range was modified
        assert A[0:3] == original_A[0:3]  # Before view unchanged
        assert A[7:] == original_A[7:]    # After view unchanged
        assert B[0:3] == original_B[0:3]  # Before view unchanged
        assert B[7:] == original_B[7:]    # After view unchanged
        assert A[3:7] == [40, 50, 60, 70]  # View range changed
        assert B[3:7] == [140, 150, 160, 170]  # View range changed

    def test_mismatched_array_lengths(self):
        """Test behavior with mismatched array lengths"""
        # Arrays of different lengths should still work within valid ranges
        A = [1, 2, 3, 4, 5]
        B = [10, 20, 30, 40, 50, 60, 70]  # Longer than A
        
        # View that fits within both arrays
        v = view2(A, B, 1, 4)
        assert len(v) == 3
        assert v[0] == (2, 20)
        assert v[2] == (4, 40)
        
        # Validation should check against A (assuming it's the limiting factor)
        v_invalid = view2(A, B, 0, 6)  # Beyond A's length
        assert v_invalid.validate() == False

    def test_sort_stability(self):
        """Test sort stability with duplicate keys"""
        A = [3, 1, 3, 2, 3, 1, 2]
        B = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        v = view2(A, B, 0, 7)
        
        v.sort()
        
        # Check that sorting worked correctly
        expected_A = [1, 1, 2, 2, 3, 3, 3]
        assert A == expected_A
        
        # Check that B values were rearranged along with A
        for i in range(len(v)):
            a_val, b_val = v[i]
            assert a_val == expected_A[i]

from cp_library.ds.view.view2_cls import view2

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()