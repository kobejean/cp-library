# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb

import pytest
import random

class TestList2:
    def test_initialization(self):
        """Test basic initialization of list2"""
        A1 = [1, 2, 3, 4, 5]
        A2 = ['a', 'b', 'c', 'd', 'e']
        lst = list2(A1, A2)
        
        assert lst.A1 is A1
        assert lst.A2 is A2
        assert len(lst) == 5

    def test_len(self):
        """Test __len__ method"""
        lst = list2([1, 2, 3], ['a', 'b', 'c'])
        assert len(lst) == 3
        
        lst = list2([], [])
        assert len(lst) == 0
        
        lst = list2(list(range(100)), list(range(100)))
        assert len(lst) == 100

    def test_getitem(self):
        """Test __getitem__ method"""
        lst = list2([10, 20, 30], ['x', 'y', 'z'])
        
        assert lst[0] == (10, 'x')
        assert lst[1] == (20, 'y')
        assert lst[2] == (30, 'z')
        
        # Test negative indexing
        assert lst[-1] == (30, 'z')
        assert lst[-2] == (20, 'y')

    def test_setitem(self):
        """Test __setitem__ method"""
        lst = list2([10, 20, 30], ['x', 'y', 'z'])
        
        lst[0] = (15, 'a')
        lst[1] = (25, 'b')
        lst[2] = (35, 'c')
        
        assert lst.A1 == [15, 25, 35]
        assert lst.A2 == ['a', 'b', 'c']
        assert lst[0] == (15, 'a')
        assert lst[1] == (25, 'b')
        assert lst[2] == (35, 'c')

    def test_contains_not_implemented(self):
        """Test that __contains__ raises NotImplementedError"""
        lst = list2([1, 2, 3], ['a', 'b', 'c'])
        
        with pytest.raises(NotImplementedError):
            (1, 'a') in lst

    def test_index_not_implemented(self):
        """Test that index raises NotImplementedError"""
        lst = list2([1, 2, 3], ['a', 'b', 'c'])
        
        with pytest.raises(NotImplementedError):
            lst.index((1, 'a'))

    def test_reverse(self):
        """Test reverse method"""
        lst = list2([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])
        
        lst.reverse()
        
        assert lst.A1 == [5, 4, 3, 2, 1]
        assert lst.A2 == ['e', 'd', 'c', 'b', 'a']
        assert lst[0] == (5, 'e')
        assert lst[4] == (1, 'a')

    def test_sort(self):
        """Test sort method"""
        lst = list2([3, 1, 4, 1, 5], ['c', 'a', 'd', 'b', 'e'])
        
        lst.sort()
        
        # Should sort by first element
        assert lst.A1 == [1, 1, 3, 4, 5]
        assert lst.A2 == ['a', 'b', 'c', 'd', 'e']
        
    def test_sort_reverse(self):
        """Test sort method with reverse=True"""
        lst = list2([3, 1, 4, 1, 5], ['c', 'a', 'd', 'b', 'e'])
        
        lst.sort(reverse=True)
        
        # Should sort by first element in reverse
        assert lst.A1 == [5, 4, 3, 1, 1]
        assert lst.A2 == ['e', 'd', 'c', 'a', 'b']

    def test_pop(self):
        """Test pop method"""
        lst = list2([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])
        
        popped = lst.pop()
        assert popped == (5, 'e')
        assert len(lst) == 4
        assert lst.A1 == [1, 2, 3, 4]
        assert lst.A2 == ['a', 'b', 'c', 'd']
        
        popped = lst.pop()
        assert popped == (4, 'd')
        assert len(lst) == 3

    def test_append(self):
        """Test append method"""
        lst = list2([1, 2, 3], ['a', 'b', 'c'])
        
        lst.append((4, 'd'))
        assert len(lst) == 4
        assert lst[3] == (4, 'd')
        assert lst.A1 == [1, 2, 3, 4]
        assert lst.A2 == ['a', 'b', 'c', 'd']
        
        lst.append((5, 'e'))
        assert len(lst) == 5
        assert lst[4] == (5, 'e')

    def test_empty_list(self):
        """Test operations on empty list2"""
        lst = list2([], [])
        
        assert len(lst) == 0
        
        with pytest.raises(IndexError):
            lst.pop()
        
        lst.append((1, 'a'))
        assert len(lst) == 1
        assert lst[0] == (1, 'a')

    def test_with_different_types(self):
        """Test list2 with different data types"""
        # Integer and float
        lst = list2([1, 2, 3], [1.1, 2.2, 3.3])
        assert lst[0] == (1, 1.1)
        assert lst[1] == (2, 2.2)
        
        # String and boolean
        lst = list2(['a', 'b', 'c'], [True, False, True])
        assert lst[0] == ('a', True)
        assert lst[1] == ('b', False)
        
        # Mixed types
        lst = list2([1, 'two', 3.0], [None, [1, 2], {'key': 'value'}])
        assert lst[0] == (1, None)
        assert lst[1] == ('two', [1, 2])
        assert lst[2] == (3.0, {'key': 'value'})

    def test_large_data_operations(self):
        """Test operations on larger datasets"""
        n = 1000
        A1 = list(range(n))
        A2 = list(range(n, 2*n))
        lst = list2(A1, A2)
        
        assert len(lst) == n
        assert lst[0] == (0, n)
        assert lst[n-1] == (n-1, 2*n-1)
        
        # Test pop on large dataset
        popped = lst.pop()
        assert popped == (n-1, 2*n-1)
        assert len(lst) == n-1
        
        # Test append on large dataset
        lst.append((n, 2*n))
        assert len(lst) == n
        assert lst[n-1] == (n, 2*n)

    def test_sort_stability(self):
        """Test that sort maintains parallel structure"""
        # Create data where first elements have duplicates
        lst = list2([3, 1, 2, 1, 3], ['a', 'b', 'c', 'd', 'e'])
        
        lst.sort()
        
        # After sorting by first element, check parallel structure
        assert lst[0][0] == 1
        assert lst[1][0] == 1
        assert lst[2][0] == 2
        assert lst[3][0] == 3
        assert lst[4][0] == 3
        
        # The corresponding second elements should be maintained
        assert lst[0][1] == 'b'
        assert lst[1][1] == 'd'
        assert lst[2][1] == 'c'
        assert lst[3][1] == 'a'
        assert lst[4][1] == 'e'

    def test_random_operations(self):
        """Test random operations for robustness"""
        random.seed(42)
        
        n = 100
        A1 = list(range(n))
        A2 = list(range(100, 100 + n))
        lst = list2(A1, A2)
        
        # Perform random operations
        for _ in range(50):
            op = random.choice(['read', 'write', 'append_pop'])
            
            if op == 'read' and len(lst) > 0:
                idx = random.randint(0, len(lst) - 1)
                val = lst[idx]
                assert val == (lst.A1[idx], lst.A2[idx])
                
            elif op == 'write' and len(lst) > 0:
                idx = random.randint(0, len(lst) - 1)
                new_val1 = random.randint(1000, 2000)
                new_val2 = random.randint(3000, 4000)
                lst[idx] = (new_val1, new_val2)
                assert lst.A1[idx] == new_val1
                assert lst.A2[idx] == new_val2
                
            elif op == 'append_pop':
                if random.random() < 0.5 and len(lst) > 0:
                    # Store expected value before popping
                    expected = (lst.A1[-1], lst.A2[-1])
                    popped = lst.pop()
                    assert popped == expected
                else:
                    val1 = random.randint(5000, 6000)
                    val2 = random.randint(7000, 8000)
                    lst.append((val1, val2))
                    assert lst[-1] == (val1, val2)

from cp_library.ds.list.list2_cls import list2

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()