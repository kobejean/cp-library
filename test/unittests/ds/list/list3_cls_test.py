# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A

import pytest
import random

class TestList3:
    def test_initialization(self):
        """Test basic initialization of list3"""
        A1 = [1, 2, 3, 4, 5]
        A2 = ['a', 'b', 'c', 'd', 'e']
        A3 = [1.1, 2.2, 3.3, 4.4, 5.5]
        lst = list3(A1, A2, A3)
        
        assert lst.A1 is A1
        assert lst.A2 is A2
        assert lst.A3 is A3
        assert len(lst) == 5

    def test_len(self):
        """Test __len__ method"""
        lst = list3([1, 2, 3], ['a', 'b', 'c'], [1.0, 2.0, 3.0])
        assert len(lst) == 3
        
        lst = list3([], [], [])
        assert len(lst) == 0
        
        lst = list3(list(range(100)), list(range(100)), list(range(100)))
        assert len(lst) == 100

    def test_getitem(self):
        """Test __getitem__ method"""
        lst = list3([10, 20, 30], ['x', 'y', 'z'], [0.1, 0.2, 0.3])
        
        assert lst[0] == (10, 'x', 0.1)
        assert lst[1] == (20, 'y', 0.2)
        assert lst[2] == (30, 'z', 0.3)
        
        # Test negative indexing
        assert lst[-1] == (30, 'z', 0.3)
        assert lst[-2] == (20, 'y', 0.2)

    def test_setitem(self):
        """Test __setitem__ method"""
        lst = list3([10, 20, 30], ['x', 'y', 'z'], [0.1, 0.2, 0.3])
        
        lst[0] = (15, 'a', 0.15)
        lst[1] = (25, 'b', 0.25)
        lst[2] = (35, 'c', 0.35)
        
        assert lst.A1 == [15, 25, 35]
        assert lst.A2 == ['a', 'b', 'c']
        assert lst.A3 == [0.15, 0.25, 0.35]
        assert lst[0] == (15, 'a', 0.15)
        assert lst[1] == (25, 'b', 0.25)
        assert lst[2] == (35, 'c', 0.35)

    def test_contains_not_implemented(self):
        """Test that __contains__ raises NotImplementedError"""
        lst = list3([1, 2, 3], ['a', 'b', 'c'], [0.1, 0.2, 0.3])
        
        with pytest.raises(NotImplementedError):
            (1, 'a', 0.1) in lst

    def test_index_not_implemented(self):
        """Test that index raises NotImplementedError"""
        lst = list3([1, 2, 3], ['a', 'b', 'c'], [0.1, 0.2, 0.3])
        
        with pytest.raises(NotImplementedError):
            lst.index((1, 'a', 0.1))

    def test_reverse(self):
        """Test reverse method"""
        lst = list3([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'], [0.1, 0.2, 0.3, 0.4, 0.5])
        
        lst.reverse()
        
        assert lst.A1 == [5, 4, 3, 2, 1]
        assert lst.A2 == ['e', 'd', 'c', 'b', 'a']
        assert lst.A3 == [0.5, 0.4, 0.3, 0.2, 0.1]
        assert lst[0] == (5, 'e', 0.5)
        assert lst[4] == (1, 'a', 0.1)

    def test_sort(self):
        """Test sort method"""
        lst = list3([3, 1, 4, 1, 5], ['c', 'a', 'd', 'b', 'e'], [0.3, 0.1, 0.4, 0.15, 0.5])
        
        lst.sort()
        
        # Should sort by first element
        assert lst.A1 == [1, 1, 3, 4, 5]
        assert lst.A2 == ['a', 'b', 'c', 'd', 'e']
        assert lst.A3 == [0.1, 0.15, 0.3, 0.4, 0.5]
        
    def test_sort_reverse(self):
        """Test sort method with reverse=True"""
        lst = list3([3, 1, 4, 1, 5], ['c', 'a', 'd', 'b', 'e'], [0.3, 0.1, 0.4, 0.15, 0.5])
        
        lst.sort(reverse=True)
        
        # Should sort by first element in reverse
        assert lst.A1 == [5, 4, 3, 1, 1]
        assert lst.A2 == ['e', 'd', 'c', 'a', 'b']
        assert lst.A3 == [0.5, 0.4, 0.3, 0.1, 0.15]

    def test_pop(self):
        """Test pop method"""
        lst = list3([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'], [0.1, 0.2, 0.3, 0.4, 0.5])
        
        popped = lst.pop()
        assert popped == (5, 'e', 0.5)
        assert len(lst) == 4
        assert lst.A1 == [1, 2, 3, 4]
        assert lst.A2 == ['a', 'b', 'c', 'd']
        assert lst.A3 == [0.1, 0.2, 0.3, 0.4]
        
        popped = lst.pop()
        assert popped == (4, 'd', 0.4)
        assert len(lst) == 3

    def test_append(self):
        """Test append method"""
        lst = list3([1, 2, 3], ['a', 'b', 'c'], [0.1, 0.2, 0.3])
        
        lst.append((4, 'd', 0.4))
        assert len(lst) == 4
        assert lst[3] == (4, 'd', 0.4)
        assert lst.A1 == [1, 2, 3, 4]
        assert lst.A2 == ['a', 'b', 'c', 'd']
        assert lst.A3 == [0.1, 0.2, 0.3, 0.4]
        
        lst.append((5, 'e', 0.5))
        assert len(lst) == 5
        assert lst[4] == (5, 'e', 0.5)

    def test_empty_list(self):
        """Test operations on empty list3"""
        lst = list3([], [], [])
        
        assert len(lst) == 0
        
        with pytest.raises(IndexError):
            lst.pop()
        
        lst.append((1, 'a', 0.1))
        assert len(lst) == 1
        assert lst[0] == (1, 'a', 0.1)

    def test_with_different_types(self):
        """Test list3 with different data types"""
        # Integer, string, float
        lst = list3([1, 2, 3], ['a', 'b', 'c'], [1.1, 2.2, 3.3])
        assert lst[0] == (1, 'a', 1.1)
        assert lst[1] == (2, 'b', 2.2)
        
        # String, boolean, list
        lst = list3(['x', 'y', 'z'], [True, False, True], [[1], [2], [3]])
        assert lst[0] == ('x', True, [1])
        assert lst[1] == ('y', False, [2])
        
        # Mixed types
        lst = list3([1, 'two', 3.0], [None, [1, 2], {'key': 'value'}], [True, False, None])
        assert lst[0] == (1, None, True)
        assert lst[1] == ('two', [1, 2], False)
        assert lst[2] == (3.0, {'key': 'value'}, None)

    def test_large_data_operations(self):
        """Test operations on larger datasets"""
        n = 1000
        A1 = list(range(n))
        A2 = list(range(n, 2*n))
        A3 = list(range(2*n, 3*n))
        lst = list3(A1, A2, A3)
        
        assert len(lst) == n
        assert lst[0] == (0, n, 2*n)
        assert lst[n-1] == (n-1, 2*n-1, 3*n-1)
        
        # Test pop on large dataset
        popped = lst.pop()
        assert popped == (n-1, 2*n-1, 3*n-1)
        assert len(lst) == n-1
        
        # Test append on large dataset
        lst.append((n, 2*n, 3*n))
        assert len(lst) == n
        assert lst[n-1] == (n, 2*n, 3*n)

    def test_sort_stability(self):
        """Test that sort maintains parallel structure"""
        # Create data where first elements have duplicates
        lst = list3([3, 1, 2, 1, 3], ['a', 'b', 'c', 'd', 'e'], [0.3, 0.1, 0.2, 0.15, 0.35])
        
        lst.sort()
        
        # After sorting by first element, check parallel structure
        assert lst[0][0] == 1
        assert lst[1][0] == 1
        assert lst[2][0] == 2
        assert lst[3][0] == 3
        assert lst[4][0] == 3
        
        # The corresponding elements should be maintained
        assert lst[0] == (1, 'b', 0.1)
        assert lst[1] == (1, 'd', 0.15)
        assert lst[2] == (2, 'c', 0.2)
        assert lst[3] == (3, 'a', 0.3)
        assert lst[4] == (3, 'e', 0.35)

    def test_random_operations(self):
        """Test random operations for robustness"""
        random.seed(42)
        
        n = 100
        A1 = list(range(n))
        A2 = list(range(100, 100 + n))
        A3 = list(range(200, 200 + n))
        lst = list3(A1, A2, A3)
        
        # Perform random operations
        for _ in range(50):
            op = random.choice(['read', 'write', 'append_pop'])
            
            if op == 'read' and len(lst) > 0:
                idx = random.randint(0, len(lst) - 1)
                val = lst[idx]
                assert val == (lst.A1[idx], lst.A2[idx], lst.A3[idx])
                
            elif op == 'write' and len(lst) > 0:
                idx = random.randint(0, len(lst) - 1)
                new_val1 = random.randint(1000, 2000)
                new_val2 = random.randint(3000, 4000)
                new_val3 = random.randint(5000, 6000)
                lst[idx] = (new_val1, new_val2, new_val3)
                assert lst.A1[idx] == new_val1
                assert lst.A2[idx] == new_val2
                assert lst.A3[idx] == new_val3
                
            elif op == 'append_pop':
                if random.random() < 0.5 and len(lst) > 0:
                    expected = (lst.A1[-1], lst.A2[-1], lst.A3[-1])
                    popped = lst.pop()
                    assert popped == expected
                else:
                    val1 = random.randint(7000, 8000)
                    val2 = random.randint(9000, 10000)
                    val3 = random.randint(11000, 12000)
                    lst.append((val1, val2, val3))
                    assert lst[-1] == (val1, val2, val3)

from cp_library.ds.list.list3_cls import list3

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()