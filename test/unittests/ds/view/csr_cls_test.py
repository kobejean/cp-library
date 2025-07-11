# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb

import pytest
import random

class TestCSR:
    def test_initialization(self):
        """Test basic initialization of CSR"""
        A = [1, 2, 3, 4, 5, 6]
        O = [0, 2, 4, 6]  # 3 rows: [1,2], [3,4], [5,6]
        csr = CSR(A, O)
        
        assert csr.A is A
        assert csr.O is O
        assert len(csr) == 3

    def test_len(self):
        """Test __len__ method"""
        A = [1, 2, 3, 4, 5]
        O = [0, 2, 3, 5]  # 3 rows: [1,2], [3], [4,5]
        csr = CSR(A, O)
        
        assert len(csr) == 3
        
        # Empty CSR
        empty_csr = CSR([], [0])
        assert len(empty_csr) == 0

    def test_getitem(self):
        """Test __getitem__ method (returns temporary view)"""
        A = [10, 20, 30, 40, 50, 60]
        O = [0, 2, 4, 6]  # 3 rows: [10,20], [30,40], [50,60]
        csr = CSR(A, O)
        
        # Test temporary access - each call returns the same view object but points to different rows
        # Test row 0
        row = csr[0]
        assert len(row) == 2
        assert row[0] == 10
        assert row[1] == 20
        
        # Test row 1 - same view object, different range
        row = csr[1]
        assert len(row) == 2
        assert row[0] == 30
        assert row[1] == 40
        
        # Test row 2 - same view object, different range
        row = csr[2]
        assert len(row) == 2
        assert row[0] == 50
        assert row[1] == 60

    def test_call(self):
        """Test __call__ method (direct element access)"""
        A = [10, 20, 30, 40, 50, 60]
        O = [0, 2, 4, 6]  # 3 rows: [10,20], [30,40], [50,60]
        csr = CSR(A, O)
        
        # Direct access to elements
        assert csr(0, 0) == 10
        assert csr(0, 1) == 20
        assert csr(1, 0) == 30
        assert csr(1, 1) == 40
        assert csr(2, 0) == 50
        assert csr(2, 1) == 60

    def test_set(self):
        """Test set method"""
        A = [10, 20, 30, 40, 50, 60]
        O = [0, 2, 4, 6]  # 3 rows: [10,20], [30,40], [50,60]
        csr = CSR(A, O)
        
        # Modify elements
        csr.set(0, 0, 15)
        csr.set(1, 1, 45)
        csr.set(2, 0, 55)
        
        assert A == [15, 20, 30, 45, 55, 60]
        assert csr(0, 0) == 15
        assert csr(1, 1) == 45
        assert csr(2, 0) == 55

    def test_getitem_method(self):
        """Test __getitem__ method (creates new view)"""
        A = [1, 2, 3, 4, 5, 6, 7, 8]
        O = [0, 3, 5, 8]  # 3 rows: [1,2,3], [4,5], [6,7,8]
        csr = CSR(A, O)
        
        # Create views for each row
        view0 = csr[0]
        view1 = csr[1]
        view2 = csr[2]
        
        assert len(view0) == 3
        assert view0[0] == 1
        assert view0[2] == 3
        
        assert len(view1) == 2
        assert view1[0] == 4
        assert view1[1] == 5
        
        assert len(view2) == 3
        assert view2[0] == 6
        assert view2[2] == 8

    def test_bucketize(self):
        """Test bucketize class method"""
        # Create buckets: bucket 0 gets [1,3], bucket 1 gets [2], bucket 2 gets [4,5]
        N = 3
        K = [0, 1, 0, 2, 2]  # Keys indicating which bucket each value goes to
        V = [1, 2, 3, 4, 5]  # Values to be bucketed
        
        csr = CSR.bucketize(N, K, V)
        
        assert len(csr) == 3
        
        # Check bucket 0: should contain [3, 1] (reverse order due to algorithm)
        row0 = csr[0]
        assert len(row0) == 2
        assert set([row0[0], row0[1]]) == {1, 3}
        
        # Check bucket 1: should contain [2]
        row1 = csr[1]
        assert len(row1) == 1
        assert row1[0] == 2
        
        # Check bucket 2: should contain [5, 4] (reverse order)
        row2 = csr[2]
        assert len(row2) == 2
        assert set([row2[0], row2[1]]) == {4, 5}

    def test_empty_rows(self):
        """Test CSR with empty rows"""
        A = [1, 2, 3, 4]
        O = [0, 2, 2, 4]  # 3 rows: [1,2], [], [3,4]
        csr = CSR(A, O)
        
        assert len(csr) == 3
        
        # Row 0: [1,2]
        row0 = csr[0]
        assert len(row0) == 2
        assert row0[0] == 1
        assert row0[1] == 2
        
        # Row 1: empty
        row1 = csr[1]
        assert len(row1) == 0
        
        # Row 2: [3,4]
        row2 = csr[2]
        assert len(row2) == 2
        assert row2[0] == 3
        assert row2[1] == 4

    def test_single_element_rows(self):
        """Test CSR with single element rows"""
        A = [10, 20, 30]
        O = [0, 1, 2, 3]  # 3 rows: [10], [20], [30]
        csr = CSR(A, O)
        
        assert len(csr) == 3
        
        for i in range(3):
            row = csr[i]
            assert len(row) == 1
            assert row[0] == (i + 1) * 10
            assert csr(i, 0) == (i + 1) * 10

    def test_view_modifications(self):
        """Test that view modifications affect the underlying data"""
        A = [1, 2, 3, 4, 5, 6]
        O = [0, 2, 4, 6]  # 3 rows: [1,2], [3,4], [5,6]
        csr = CSR(A, O)
        
        # Get a view and modify it
        row1 = csr[1]
        row1[0] = 30
        row1[1] = 40
        
        # Check that underlying data changed
        assert A == [1, 2, 30, 40, 5, 6]
        assert csr(1, 0) == 30
        assert csr(1, 1) == 40

    def test_view_operations(self):
        """Test various view operations"""
        A = [5, 3, 1, 4, 2, 6]
        O = [0, 3, 6]  # 2 rows: [5,3,1], [4,2,6]
        csr = CSR(A, O)
        
        # Get views and operate on them
        row0 = csr[0]
        row0.sort()
        assert A[:3] == [1, 3, 5]
        
        row1 = csr[1]
        row1.reverse()
        assert A[3:] == [6, 2, 4]

    def test_view_creation_behavior(self):
        """Test that __getitem__ creates new view objects each time"""
        A = [1, 2, 3, 4, 5, 6]
        O = [0, 2, 4, 6]  # 3 rows: [1,2], [3,4], [5,6]
        csr = CSR(A, O)
        
        # __getitem__ creates new view objects each time
        view1 = csr[0]  # New view of row 0
        view2 = csr[0]  # Another new view of row 0
        
        # Should be different objects but point to the same data
        assert view1 is not view2  # Different objects
        
        # But should have the same data
        assert len(view1) == len(view2) == 2
        assert view1[0] == view2[0] == 1  # Row 0 data
        assert view1[1] == view2[1] == 2  # Row 0 data
        
        # Views of different rows should also be independent
        row0_view = csr[0]
        row1_view = csr[1] 
        
        assert row0_view is not row1_view  # Different objects
        assert len(row0_view) == 2
        assert row0_view[0] == 1  # Row 0 data
        assert len(row1_view) == 2  
        assert row1_view[0] == 3  # Row 1 data

    def test_large_csr(self):
        """Test CSR with larger data"""
        # Create 100 rows with 10 elements each
        A = list(range(1000))
        O = [i * 10 for i in range(101)]  # 100 rows
        csr = CSR(A, O)
        
        assert len(csr) == 100
        
        # Test random access
        assert csr(50, 5) == 505
        assert csr(99, 9) == 999
        
        # Test view length
        for i in range(100):
            assert len(csr[i]) == 10

    def test_bucketize_edge_cases(self):
        """Test bucketize with edge cases"""
        # All elements go to the same bucket
        N = 3
        K = [1, 1, 1, 1]
        V = [10, 20, 30, 40]
        
        csr = CSR.bucketize(N, K, V)
        assert len(csr) == 3
        
        # Bucket 0 should be empty
        assert len(csr[0]) == 0
        
        # Bucket 1 should have all elements
        assert len(csr[1]) == 4
        
        # Bucket 2 should be empty
        assert len(csr[2]) == 0

    def test_bucketize_empty(self):
        """Test bucketize with empty input"""
        N = 3
        K = []
        V = []
        
        csr = CSR.bucketize(N, K, V)
        assert len(csr) == 3
        
        # All buckets should be empty
        for i in range(3):
            assert len(csr[i]) == 0

    def test_different_data_types(self):
        """Test CSR with different data types"""
        # String data
        A = ['a', 'b', 'c', 'd', 'e', 'f']
        O = [0, 2, 4, 6]
        csr = CSR(A, O)
        
        assert csr(0, 0) == 'a'
        assert csr(1, 1) == 'd'
        assert csr(2, 0) == 'e'
        
        # Float data
        A_float = [1.1, 2.2, 3.3, 4.4]
        O_float = [0, 2, 4]
        csr_float = CSR(A_float, O_float)
        
        assert csr_float(0, 0) == 1.1
        assert csr_float(1, 1) == 4.4

    def test_bounds_checking(self):
        """Test that appropriate errors are raised for out-of-bounds access"""
        A = [1, 2, 3, 4]
        O = [0, 2, 4]  # 2 rows: [1,2], [3,4]
        csr = CSR(A, O)
        
        # These should work
        assert csr(0, 1) == 2
        assert csr(1, 0) == 3
        
        # Out of bounds row access should raise IndexError when accessing the view
        # Note: CSR doesn't validate bounds itself, the view does
        row = csr[0]
        with pytest.raises(IndexError):
            row[2]  # Row 0 only has 2 elements (indices 0, 1)

    def test_random_operations(self):
        """Test random operations for robustness"""
        random.seed(42)  # For reproducibility
        
        # Create random CSR structure
        num_rows = 50
        total_elements = 500
        A = [random.randint(1, 1000) for _ in range(total_elements)]
        
        # Generate random row sizes
        O = [0]
        remaining = total_elements
        for i in range(num_rows - 1):
            if remaining > 0:
                row_size = random.randint(0, min(20, remaining))
                O.append(O[-1] + row_size)
                remaining -= row_size
            else:
                O.append(O[-1])
        O.append(total_elements)
        
        csr = CSR(A, O)
        assert len(csr) == num_rows
        
        # Perform random operations
        for _ in range(100):
            row_idx = random.randint(0, num_rows - 1)
            row = csr[row_idx]
            
            if len(row) > 0:
                col_idx = random.randint(0, len(row) - 1)
                # Read operation
                val1 = csr(row_idx, col_idx)
                val2 = row[col_idx]
                assert val1 == val2
                
                # Write operation
                new_val = random.randint(2000, 3000)
                csr.set(row_idx, col_idx, new_val)
                assert csr(row_idx, col_idx) == new_val
                assert row[col_idx] == new_val

    def test_view_isolation(self):
        """Test that different views don't interfere with each other"""
        A = [1, 2, 3, 4, 5, 6, 7, 8]
        O = [0, 3, 5, 8]  # 3 rows: [1,2,3], [4,5], [6,7,8]
        csr = CSR(A, O)
        
        # Get multiple views
        view0 = csr[0]
        view1 = csr[1]
        view2 = csr[2]
        
        # Modify through different views
        view0[0] = 10
        view1[1] = 50
        view2[2] = 80
        
        # Check that modifications are isolated and correct
        assert A == [10, 2, 3, 4, 50, 6, 7, 80]
        assert view0[0] == 10
        assert view1[1] == 50
        assert view2[2] == 80
        
        # Other elements should be unchanged
        assert view0[1] == 2
        assert view1[0] == 4
        assert view2[0] == 6

from cp_library.ds.view.csr_cls import CSR

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()