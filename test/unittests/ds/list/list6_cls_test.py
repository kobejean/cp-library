# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A

import pytest
import random

class TestList6:
    def test_initialization(self):
        """Test basic initialization of list6"""
        A1 = [1, 2, 3, 4, 5]
        A2 = ['a', 'b', 'c', 'd', 'e']
        A3 = [1.1, 2.2, 3.3, 4.4, 5.5]
        A4 = [True, False, True, False, True]
        A5 = [[1], [2], [3], [4], [5]]
        A6 = [{'x': 1}, {'x': 2}, {'x': 3}, {'x': 4}, {'x': 5}]
        lst = list6(A1, A2, A3, A4, A5, A6)
        
        assert lst.A1 is A1
        assert lst.A2 is A2
        assert lst.A3 is A3
        assert lst.A4 is A4
        assert lst.A5 is A5
        assert lst.A6 is A6
        assert len(lst) == 5

    def test_len(self):
        """Test __len__ method"""
        lst = list6([1, 2, 3], ['a', 'b', 'c'], [1.0, 2.0, 3.0], [True, False, True], [[1], [2], [3]], [None, None, None])
        assert len(lst) == 3
        
        lst = list6([], [], [], [], [], [])
        assert len(lst) == 0
        
        lst = list6(list(range(100)), list(range(100)), list(range(100)), list(range(100)), list(range(100)), list(range(100)))
        assert len(lst) == 100

    def test_getitem(self):
        """Test __getitem__ method"""
        lst = list6([10, 20, 30], ['x', 'y', 'z'], [0.1, 0.2, 0.3], [True, False, True], [[1], [2], [3]], [None, 'str', 42])
        
        assert lst[0] == (10, 'x', 0.1, True, [1], None)
        assert lst[1] == (20, 'y', 0.2, False, [2], 'str')
        assert lst[2] == (30, 'z', 0.3, True, [3], 42)
        
        # Test negative indexing
        assert lst[-1] == (30, 'z', 0.3, True, [3], 42)
        assert lst[-2] == (20, 'y', 0.2, False, [2], 'str')

    def test_setitem(self):
        """Test __setitem__ method"""
        lst = list6([10, 20, 30], ['x', 'y', 'z'], [0.1, 0.2, 0.3], [True, False, True], [[1], [2], [3]], [None, 'str', 42])
        
        lst[0] = (15, 'a', 0.15, False, [10], 'new')
        lst[1] = (25, 'b', 0.25, True, [20], {'key': 'val'})
        lst[2] = (35, 'c', 0.35, False, [30], [1, 2, 3])
        
        assert lst.A1 == [15, 25, 35]
        assert lst.A2 == ['a', 'b', 'c']
        assert lst.A3 == [0.15, 0.25, 0.35]
        assert lst.A4 == [False, True, False]
        assert lst.A5 == [[10], [20], [30]]
        assert lst.A6 == ['new', {'key': 'val'}, [1, 2, 3]]
        assert lst[0] == (15, 'a', 0.15, False, [10], 'new')
        assert lst[1] == (25, 'b', 0.25, True, [20], {'key': 'val'})
        assert lst[2] == (35, 'c', 0.35, False, [30], [1, 2, 3])

    def test_contains_not_implemented(self):
        """Test that __contains__ raises NotImplementedError"""
        lst = list6([1, 2, 3], ['a', 'b', 'c'], [0.1, 0.2, 0.3], [True, False, True], [[1], [2], [3]], [None, None, None])
        
        with pytest.raises(NotImplementedError):
            (1, 'a', 0.1, True, [1], None) in lst

    def test_index_not_implemented(self):
        """Test that index raises NotImplementedError"""
        lst = list6([1, 2, 3], ['a', 'b', 'c'], [0.1, 0.2, 0.3], [True, False, True], [[1], [2], [3]], [None, None, None])
        
        with pytest.raises(NotImplementedError):
            lst.index((1, 'a', 0.1, True, [1], None))

    def test_reverse(self):
        """Test reverse method"""
        lst = list6([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'], [0.1, 0.2, 0.3, 0.4, 0.5], 
                    [True, False, True, False, True], [[1], [2], [3], [4], [5]], ['A', 'B', 'C', 'D', 'E'])
        
        lst.reverse()
        
        assert lst.A1 == [5, 4, 3, 2, 1]
        assert lst.A2 == ['e', 'd', 'c', 'b', 'a']
        assert lst.A3 == [0.5, 0.4, 0.3, 0.2, 0.1]
        assert lst.A4 == [True, False, True, False, True]
        assert lst.A5 == [[5], [4], [3], [2], [1]]
        assert lst.A6 == ['E', 'D', 'C', 'B', 'A']
        assert lst[0] == (5, 'e', 0.5, True, [5], 'E')
        assert lst[4] == (1, 'a', 0.1, True, [1], 'A')

    def test_sort(self):
        """Test sort method"""
        lst = list6([3, 1, 4, 1, 5], ['c', 'a', 'd', 'b', 'e'], [0.3, 0.1, 0.4, 0.15, 0.5], 
                    [True, False, True, False, True], [[3], [1], [4], [1.5], [5]], ['C', 'A', 'D', 'B', 'E'])
        
        lst.sort()
        
        # Should sort by first element
        assert lst.A1 == [1, 1, 3, 4, 5]
        assert lst.A2 == ['a', 'b', 'c', 'd', 'e']
        assert lst.A3 == [0.1, 0.15, 0.3, 0.4, 0.5]
        assert lst.A4 == [False, False, True, True, True]
        assert lst.A5 == [[1], [1.5], [3], [4], [5]]
        assert lst.A6 == ['A', 'B', 'C', 'D', 'E']
        
    def test_sort_reverse(self):
        """Test sort method with reverse=True"""
        lst = list6([3, 1, 4, 1, 5], ['c', 'a', 'd', 'b', 'e'], [0.3, 0.1, 0.4, 0.15, 0.5], 
                    [True, False, True, False, True], [[3], [1], [4], [1.5], [5]], ['C', 'A', 'D', 'B', 'E'])
        
        lst.sort(reverse=True)
        
        # Should sort by first element in reverse
        assert lst.A1 == [5, 4, 3, 1, 1]
        assert lst.A2 == ['e', 'd', 'c', 'a', 'b']
        assert lst.A3 == [0.5, 0.4, 0.3, 0.1, 0.15]
        assert lst.A4 == [True, True, True, False, False]
        assert lst.A5 == [[5], [4], [3], [1], [1.5]]
        assert lst.A6 == ['E', 'D', 'C', 'A', 'B']

    def test_pop(self):
        """Test pop method"""
        lst = list6([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'], [0.1, 0.2, 0.3, 0.4, 0.5], 
                    [True, False, True, False, True], [[1], [2], [3], [4], [5]], ['A', 'B', 'C', 'D', 'E'])
        
        popped = lst.pop()
        assert popped == (5, 'e', 0.5, True, [5], 'E')
        assert len(lst) == 4
        assert lst.A1 == [1, 2, 3, 4]
        assert lst.A2 == ['a', 'b', 'c', 'd']
        assert lst.A3 == [0.1, 0.2, 0.3, 0.4]
        assert lst.A4 == [True, False, True, False]
        assert lst.A5 == [[1], [2], [3], [4]]
        assert lst.A6 == ['A', 'B', 'C', 'D']
        
        popped = lst.pop()
        assert popped == (4, 'd', 0.4, False, [4], 'D')
        assert len(lst) == 3

    def test_append(self):
        """Test append method"""
        lst = list6([1, 2, 3], ['a', 'b', 'c'], [0.1, 0.2, 0.3], [True, False, True], [[1], [2], [3]], ['A', 'B', 'C'])
        
        lst.append((4, 'd', 0.4, False, [4], 'D'))
        assert len(lst) == 4
        assert lst[3] == (4, 'd', 0.4, False, [4], 'D')
        assert lst.A1 == [1, 2, 3, 4]
        assert lst.A2 == ['a', 'b', 'c', 'd']
        assert lst.A3 == [0.1, 0.2, 0.3, 0.4]
        assert lst.A4 == [True, False, True, False]
        assert lst.A5 == [[1], [2], [3], [4]]
        assert lst.A6 == ['A', 'B', 'C', 'D']
        
        lst.append((5, 'e', 0.5, True, [5], 'E'))
        assert len(lst) == 5
        assert lst[4] == (5, 'e', 0.5, True, [5], 'E')

    def test_empty_list(self):
        """Test operations on empty list6"""
        lst = list6([], [], [], [], [], [])
        
        assert len(lst) == 0
        
        with pytest.raises(IndexError):
            lst.pop()
        
        lst.append((1, 'a', 0.1, True, [1], None))
        assert len(lst) == 1
        assert lst[0] == (1, 'a', 0.1, True, [1], None)

    def test_with_different_types(self):
        """Test list6 with different data types"""
        # Integer, string, float, boolean, list, dict
        lst = list6([1, 2, 3], ['a', 'b', 'c'], [1.1, 2.2, 3.3], [True, False, True], 
                    [[1], [2], [3]], [{'k': 1}, {'k': 2}, {'k': 3}])
        assert lst[0] == (1, 'a', 1.1, True, [1], {'k': 1})
        assert lst[1] == (2, 'b', 2.2, False, [2], {'k': 2})
        
        # String, list, dict, None, tuple, set
        lst = list6(['x', 'y', 'z'], [[1], [2], [3]], [{'a': 1}, {'b': 2}, {'c': 3}], 
                    [None, None, None], [(1, 2), (3, 4), (5, 6)], [set([1]), set([2]), set([3])])
        assert lst[0] == ('x', [1], {'a': 1}, None, (1, 2), set([1]))
        assert lst[1] == ('y', [2], {'b': 2}, None, (3, 4), set([2]))
        
        # Mixed types  
        lst = list6([1, 'two', 3.0], [None, [1, 2], {'key': 'value'}], [True, False, None], 
                    [[1, 2], 'str', 3], [set([1]), frozenset([2]), None], [bytes(1), bytearray(2), 'string'])
        assert lst[0] == (1, None, True, [1, 2], set([1]), bytes(1))
        assert lst[1] == ('two', [1, 2], False, 'str', frozenset([2]), bytearray(2))
        assert lst[2] == (3.0, {'key': 'value'}, None, 3, None, 'string')

    def test_large_data_operations(self):
        """Test operations on larger datasets"""
        n = 1000
        A1 = list(range(n))
        A2 = list(range(n, 2*n))
        A3 = list(range(2*n, 3*n))
        A4 = list(range(3*n, 4*n))
        A5 = list(range(4*n, 5*n))
        A6 = list(range(5*n, 6*n))
        lst = list6(A1, A2, A3, A4, A5, A6)
        
        assert len(lst) == n
        assert lst[0] == (0, n, 2*n, 3*n, 4*n, 5*n)
        assert lst[n-1] == (n-1, 2*n-1, 3*n-1, 4*n-1, 5*n-1, 6*n-1)
        
        # Test pop on large dataset
        popped = lst.pop()
        assert popped == (n-1, 2*n-1, 3*n-1, 4*n-1, 5*n-1, 6*n-1)
        assert len(lst) == n-1
        
        # Test append on large dataset
        lst.append((n, 2*n, 3*n, 4*n, 5*n, 6*n))
        assert len(lst) == n
        assert lst[n-1] == (n, 2*n, 3*n, 4*n, 5*n, 6*n)

    def test_sort_stability(self):
        """Test that sort maintains parallel structure"""
        # Create data where first elements have duplicates
        lst = list6([3, 1, 2, 1, 3], ['a', 'b', 'c', 'd', 'e'], [0.3, 0.1, 0.2, 0.15, 0.35], 
                    [True, False, True, False, True], [[3], [1], [2], [1.5], [3.5]], ['C', 'A', 'B', 'D', 'E'])
        
        lst.sort()
        
        # After sorting by first element, check parallel structure
        assert lst[0][0] == 1
        assert lst[1][0] == 1
        assert lst[2][0] == 2
        assert lst[3][0] == 3
        assert lst[4][0] == 3
        
        # The corresponding elements should be maintained
        assert lst[0] == (1, 'b', 0.1, False, [1], 'A')
        assert lst[1] == (1, 'd', 0.15, False, [1.5], 'D')
        assert lst[2] == (2, 'c', 0.2, True, [2], 'B')
        assert lst[3] == (3, 'a', 0.3, True, [3], 'C')
        assert lst[4] == (3, 'e', 0.35, True, [3.5], 'E')

    def test_random_operations(self):
        """Test random operations for robustness"""
        random.seed(42)
        
        n = 100
        A1 = list(range(n))
        A2 = list(range(100, 100 + n))
        A3 = list(range(200, 200 + n))
        A4 = list(range(300, 300 + n))
        A5 = list(range(400, 400 + n))
        A6 = list(range(500, 500 + n))
        lst = list6(A1, A2, A3, A4, A5, A6)
        
        # Perform random operations
        for _ in range(50):
            op = random.choice(['read', 'write', 'append_pop'])
            
            if op == 'read' and len(lst) > 0:
                idx = random.randint(0, len(lst) - 1)
                val = lst[idx]
                assert val == (lst.A1[idx], lst.A2[idx], lst.A3[idx], lst.A4[idx], lst.A5[idx], lst.A6[idx])
                
            elif op == 'write' and len(lst) > 0:
                idx = random.randint(0, len(lst) - 1)
                new_val1 = random.randint(1000, 2000)
                new_val2 = random.randint(3000, 4000)
                new_val3 = random.randint(5000, 6000)
                new_val4 = random.randint(7000, 8000)
                new_val5 = random.randint(9000, 10000)
                new_val6 = random.randint(11000, 12000)
                lst[idx] = (new_val1, new_val2, new_val3, new_val4, new_val5, new_val6)
                assert lst.A1[idx] == new_val1
                assert lst.A2[idx] == new_val2
                assert lst.A3[idx] == new_val3
                assert lst.A4[idx] == new_val4
                assert lst.A5[idx] == new_val5
                assert lst.A6[idx] == new_val6
                
            elif op == 'append_pop':
                if random.random() < 0.5 and len(lst) > 0:
                    expected = (lst.A1[-1], lst.A2[-1], lst.A3[-1], lst.A4[-1], lst.A5[-1], lst.A6[-1])
                    popped = lst.pop()
                    assert popped == expected
                else:
                    val1 = random.randint(13000, 14000)
                    val2 = random.randint(15000, 16000)
                    val3 = random.randint(17000, 18000)
                    val4 = random.randint(19000, 20000)
                    val5 = random.randint(21000, 22000)
                    val6 = random.randint(23000, 24000)
                    lst.append((val1, val2, val3, val4, val5, val6))
                    assert lst[-1] == (val1, val2, val3, val4, val5, val6)

from cp_library.ds.list.list6_cls import list6

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()