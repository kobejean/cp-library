# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb

import pytest
import random

class TestCSR2:
    def test_initialization(self):
        """Test basic initialization of CSR2"""
        A = [1, 2, 3, 4, 5, 6]
        B = [10, 20, 30, 40, 50, 60]
        O = [0, 2, 4, 6]  # 3 rows: [(1,10),(2,20)], [(3,30),(4,40)], [(5,50),(6,60)]
        csr2 = CSR2(A, B, O)
        
        assert csr2.A1 is A
        assert csr2.A2 is B
        assert csr2.O is O
        assert len(csr2) == 3

    def test_len(self):
        """Test __len__ method"""
        A = [1, 2, 3, 4, 5]
        B = [10, 20, 30, 40, 50]
        O = [0, 2, 3, 5]  # 3 rows: [(1,10),(2,20)], [(3,30)], [(4,40),(5,50)]
        csr2 = CSR2(A, B, O)
        
        assert len(csr2) == 3
        
        # Empty CSR2
        empty_csr2 = CSR2([], [], [0])
        assert len(empty_csr2) == 0

    def test_getitem(self):
        """Test __getitem__ method (returns temporary view2)"""
        A = [1, 2, 3, 4, 5, 6]
        B = [10, 20, 30, 40, 50, 60]
        O = [0, 2, 4, 6]  # 3 rows: [(1,10),(2,20)], [(3,30),(4,40)], [(5,50),(6,60)]
        csr2 = CSR2(A, B, O)
        
        # Test temporary access - each call returns the same view object but points to different rows
        # Test row 0
        row = csr2[0]
        assert len(row) == 2
        assert row[0] == (1, 10)
        assert row[1] == (2, 20)
        
        # Test row 1 - same view object, different range
        row = csr2[1]
        assert len(row) == 2
        assert row[0] == (3, 30)
        assert row[1] == (4, 40)
        
        # Test row 2 - same view object, different range
        row = csr2[2]
        assert len(row) == 2
        assert row[0] == (5, 50)
        assert row[1] == (6, 60)

    def test_call(self):
        """Test __call__ method (direct element access)"""
        A = [1, 2, 3, 4, 5, 6]
        B = [10, 20, 30, 40, 50, 60]
        O = [0, 2, 4, 6]  # 3 rows: [(1,10),(2,20)], [(3,30),(4,40)], [(5,50),(6,60)]
        csr2 = CSR2(A, B, O)
        
        # Direct access to elements
        assert csr2(0, 0) == (1, 10)
        assert csr2(0, 1) == (2, 20)
        assert csr2(1, 0) == (3, 30)
        assert csr2(1, 1) == (4, 40)
        assert csr2(2, 0) == (5, 50)
        assert csr2(2, 1) == (6, 60)

    def test_set(self):
        """Test set method"""
        A = [1, 2, 3, 4, 5, 6]
        B = [10, 20, 30, 40, 50, 60]
        O = [0, 2, 4, 6]  # 3 rows: [(1,10),(2,20)], [(3,30),(4,40)], [(5,50),(6,60)]
        csr2 = CSR2(A, B, O)
        
        # Modify elements
        csr2.set(0, 0, (15, 150))
        csr2.set(1, 1, (45, 450))
        csr2.set(2, 0, (55, 550))
        
        assert A == [15, 2, 3, 45, 55, 6]
        assert B == [150, 20, 30, 450, 550, 60]
        assert csr2(0, 0) == (15, 150)
        assert csr2(1, 1) == (45, 450)
        assert csr2(2, 0) == (55, 550)

    def test_getitem_method(self):
        """Test __getitem__ method (creates new view2)"""
        A = [1, 2, 3, 4, 5, 6, 7, 8]
        B = [10, 20, 30, 40, 50, 60, 70, 80]
        O = [0, 3, 5, 8]  # 3 rows: [(1,10),(2,20),(3,30)], [(4,40),(5,50)], [(6,60),(7,70),(8,80)]
        csr2 = CSR2(A, B, O)
        
        # Create views for each row
        view0 = csr2[0]
        view1 = csr2[1]
        view2 = csr2[2]
        
        assert len(view0) == 3
        assert view0[0] == (1, 10)
        assert view0[2] == (3, 30)
        
        assert len(view1) == 2
        assert view1[0] == (4, 40)
        assert view1[1] == (5, 50)
        
        assert len(view2) == 3
        assert view2[0] == (6, 60)
        assert view2[2] == (8, 80)

    def test_bucketize(self):
        """Test bucketize class method"""
        # Create buckets: bucket 0 gets [(1,11),(3,33)], bucket 1 gets [(2,22)], bucket 2 gets [(4,44),(5,55)]
        N = 3
        K = [0, 1, 0, 2, 2]  # Keys indicating which bucket each value goes to
        V = [1, 2, 3, 4, 5]  # Values for first array
        W = [11, 22, 33, 44, 55]  # Values for second array
        
        csr2 = CSR2.bucketize(N, K, V, W)
        
        assert len(csr2) == 3
        
        # Check bucket 0: should contain [(3,33), (1,11)] (reverse order due to algorithm)
        row0 = csr2[0]
        assert len(row0) == 2
        assert set([row0[0], row0[1]]) == {(1, 11), (3, 33)}
        
        # Check bucket 1: should contain [(2,22)]
        row1 = csr2[1]
        assert len(row1) == 1
        assert row1[0] == (2, 22)
        
        # Check bucket 2: should contain [(5,55), (4,44)] (reverse order)
        row2 = csr2[2]
        assert len(row2) == 2
        assert set([row2[0], row2[1]]) == {(4, 44), (5, 55)}

    def test_empty_rows(self):
        """Test CSR2 with empty rows"""
        A = [1, 2, 3, 4]
        B = [10, 20, 30, 40]
        O = [0, 2, 2, 4]  # 3 rows: [(1,10),(2,20)], [], [(3,30),(4,40)]
        csr2 = CSR2(A, B, O)
        
        assert len(csr2) == 3
        
        # Row 0: [(1,10),(2,20)]
        row0 = csr2[0]
        assert len(row0) == 2
        assert row0[0] == (1, 10)
        assert row0[1] == (2, 20)
        
        # Row 1: empty
        row1 = csr2[1]
        assert len(row1) == 0
        
        # Row 2: [(3,30),(4,40)]
        row2 = csr2[2]
        assert len(row2) == 2
        assert row2[0] == (3, 30)
        assert row2[1] == (4, 40)

    def test_single_element_rows(self):
        """Test CSR2 with single element rows"""
        A = [1, 2, 3]
        B = [10, 20, 30]
        O = [0, 1, 2, 3]  # 3 rows: [(1,10)], [(2,20)], [(3,30)]
        csr2 = CSR2(A, B, O)
        
        assert len(csr2) == 3
        
        for i in range(3):
            row = csr2[i]
            assert len(row) == 1
            assert row[0] == (i + 1, (i + 1) * 10)
            assert csr2(i, 0) == (i + 1, (i + 1) * 10)

    def test_view_modifications(self):
        """Test that view modifications affect the underlying data"""
        A = [1, 2, 3, 4, 5, 6]
        B = [10, 20, 30, 40, 50, 60]
        O = [0, 2, 4, 6]  # 3 rows: [(1,10),(2,20)], [(3,30),(4,40)], [(5,50),(6,60)]
        csr2 = CSR2(A, B, O)
        
        # Get a view and modify it
        row1 = csr2[1]
        row1[0] = (30, 300)
        row1[1] = (40, 400)
        
        # Check that underlying data changed
        assert A == [1, 2, 30, 40, 5, 6]
        assert B == [10, 20, 300, 400, 50, 60]
        assert csr2(1, 0) == (30, 300)
        assert csr2(1, 1) == (40, 400)

    def test_view_operations(self):
        """Test various view operations"""
        A = [5, 3, 1, 4, 2, 6]
        B = [50, 30, 10, 40, 20, 60]
        O = [0, 3, 6]  # 2 rows: [(5,50),(3,30),(1,10)], [(4,40),(2,20),(6,60)]
        csr2 = CSR2(A, B, O)
        
        # Get views and operate on them
        row0 = csr2[0]
        row0.sort()
        assert A[:3] == [1, 3, 5]
        assert B[:3] == [10, 30, 50]
        
        row1 = csr2[1]
        row1.reverse()
        assert A[3:] == [6, 2, 4]
        assert B[3:] == [60, 20, 40]

    def test_view_creation_behavior(self):
        """Test that __getitem__ creates new view objects each time"""
        A = [1, 2, 3, 4, 5, 6]
        B = [10, 20, 30, 40, 50, 60]
        O = [0, 2, 4, 6]  # 3 rows: [(1,10),(2,20)], [(3,30),(4,40)], [(5,50),(6,60)]
        csr2 = CSR2(A, B, O)
        
        # __getitem__ creates new view objects each time
        view1 = csr2[0]  # New view of row 0
        view2 = csr2[0]  # Another new view of row 0
        
        # Should be different objects but point to the same data
        assert view1 is not view2  # Different objects
        
        # But should have the same data
        assert len(view1) == len(view2) == 2
        assert view1[0] == view2[0] == (1, 10)  # Row 0 data
        assert view1[1] == view2[1] == (2, 20)  # Row 0 data
        
        # Views of different rows should also be independent
        row0_view = csr2[0]
        row1_view = csr2[1] 
        
        assert row0_view is not row1_view  # Different objects
        assert len(row0_view) == 2
        assert row0_view[0] == (1, 10)  # Row 0 data
        assert len(row1_view) == 2  
        assert row1_view[0] == (3, 30)  # Row 1 data

    def test_large_csr2(self):
        """Test CSR2 with larger data"""
        # Create 100 rows with 10 elements each
        A = list(range(1000))
        B = list(range(1000, 2000))
        O = [i * 10 for i in range(101)]  # 100 rows
        csr2 = CSR2(A, B, O)
        
        assert len(csr2) == 100
        
        # Test random access
        assert csr2(50, 5) == (505, 1505)
        assert csr2(99, 9) == (999, 1999)
        
        # Test view length
        for i in range(100):
            assert len(csr2[i]) == 10

    def test_bucketize_edge_cases(self):
        """Test bucketize with edge cases"""
        # All elements go to the same bucket
        N = 3
        K = [1, 1, 1, 1]
        V = [10, 20, 30, 40]
        W = [100, 200, 300, 400]
        
        csr2 = CSR2.bucketize(N, K, V, W)
        assert len(csr2) == 3
        
        # Bucket 0 should be empty
        assert len(csr2[0]) == 0
        
        # Bucket 1 should have all elements
        assert len(csr2[1]) == 4
        
        # Bucket 2 should be empty
        assert len(csr2[2]) == 0

    def test_bucketize_empty(self):
        """Test bucketize with empty input"""
        N = 3
        K = []
        V = []
        W = []
        
        csr2 = CSR2.bucketize(N, K, V, W)
        assert len(csr2) == 3
        
        # All buckets should be empty
        for i in range(3):
            assert len(csr2[i]) == 0

    def test_different_data_types(self):
        """Test CSR2 with different data types"""
        # Mixed types
        A = [1, 2, 3, 4, 5, 6]
        B = ['a', 'b', 'c', 'd', 'e', 'f']
        O = [0, 2, 4, 6]
        csr2 = CSR2(A, B, O)
        
        assert csr2(0, 0) == (1, 'a')
        assert csr2(1, 1) == (4, 'd')
        assert csr2(2, 0) == (5, 'e')
        
        # Float types
        A_float = [1.1, 2.2, 3.3, 4.4]
        B_float = [10.1, 20.2, 30.3, 40.4]
        O_float = [0, 2, 4]
        csr2_float = CSR2(A_float, B_float, O_float)
        
        assert csr2_float(0, 0) == (1.1, 10.1)
        assert csr2_float(1, 1) == (4.4, 40.4)

    def test_bounds_checking(self):
        """Test that appropriate errors are raised for out-of-bounds access"""
        A = [1, 2, 3, 4]
        B = [10, 20, 30, 40]
        O = [0, 2, 4]  # 2 rows: [(1,10),(2,20)], [(3,30),(4,40)]
        csr2 = CSR2(A, B, O)
        
        # These should work
        assert csr2(0, 1) == (2, 20)
        assert csr2(1, 0) == (3, 30)
        
        # Out of bounds row access should raise IndexError when accessing the view
        row = csr2[0]
        with pytest.raises(IndexError):
            row[2]  # Row 0 only has 2 elements (indices 0, 1)

    def test_random_operations(self):
        """Test random operations for robustness"""
        random.seed(42)  # For reproducibility
        
        # Create random CSR2 structure
        num_rows = 50
        total_elements = 500
        A = [random.randint(1, 1000) for _ in range(total_elements)]
        B = [random.randint(1000, 2000) for _ in range(total_elements)]
        
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
        
        csr2 = CSR2(A, B, O)
        assert len(csr2) == num_rows
        
        # Perform random operations
        for _ in range(100):
            row_idx = random.randint(0, num_rows - 1)
            row = csr2[row_idx]
            
            if len(row) > 0:
                col_idx = random.randint(0, len(row) - 1)
                # Read operation
                val1 = csr2(row_idx, col_idx)
                val2 = row[col_idx]
                assert val1 == val2
                
                # Write operation
                new_val = (random.randint(2000, 3000), random.randint(3000, 4000))
                csr2.set(row_idx, col_idx, new_val)
                assert csr2(row_idx, col_idx) == new_val
                assert row[col_idx] == new_val

    def test_view_isolation(self):
        """Test that different views don't interfere with each other"""
        A = [1, 2, 3, 4, 5, 6, 7, 8]
        B = [10, 20, 30, 40, 50, 60, 70, 80]
        O = [0, 3, 5, 8]  # 3 rows: [(1,10),(2,20),(3,30)], [(4,40),(5,50)], [(6,60),(7,70),(8,80)]
        csr2 = CSR2(A, B, O)
        
        # Get multiple views
        view0 = csr2[0]
        view1 = csr2[1]
        view2 = csr2[2]
        
        # Modify through different views
        view0[0] = (10, 100)
        view1[1] = (50, 500)
        view2[2] = (80, 800)
        
        # Check that modifications are isolated and correct
        assert A == [10, 2, 3, 4, 50, 6, 7, 80]
        assert B == [100, 20, 30, 40, 500, 60, 70, 800]
        assert view0[0] == (10, 100)
        assert view1[1] == (50, 500)
        assert view2[2] == (80, 800)
        
        # Other elements should be unchanged
        assert view0[1] == (2, 20)
        assert view1[0] == (4, 40)
        assert view2[0] == (6, 60)

    def test_bucketize_order_preservation(self):
        """Test bucketize behavior with element ordering"""
        N = 2
        K = [0, 1, 0, 1, 0]  # Alternating buckets
        V = [1, 2, 3, 4, 5]
        W = [10, 20, 30, 40, 50]
        
        csr2 = CSR2.bucketize(N, K, V, W)
        
        # Bucket 0 should contain elements from positions 0, 2, 4
        # The bucketize algorithm processes in reverse order, so elements are inserted last-to-first
        row0 = csr2[0]
        assert len(row0) == 3
        # Elements should be in reverse insertion order: (5,50), (3,30), (1,10)
        elements_bucket0 = [row0[i] for i in range(len(row0))]
        assert set(elements_bucket0) == {(1, 10), (3, 30), (5, 50)}
        
        # Bucket 1 should contain elements from positions 1, 3
        row1 = csr2[1]
        assert len(row1) == 2
        # Elements should be in reverse insertion order: (4,40), (2,20)
        elements_bucket1 = [row1[i] for i in range(len(row1))]
        assert set(elements_bucket1) == {(2, 20), (4, 40)}

    def test_complex_operations_sequence(self):
        """Test complex sequence of operations using persistent views"""
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        B = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        O = [0, 3, 6, 9]  # 3 rows of 3 elements each
        csr2 = CSR2(A, B, O)
        
        # Get views and perform operations
        row0 = csr2[0]
        row1 = csr2[1]
        
        # Sort first row
        row0.sort()
        assert A[:3] == [1, 2, 3]
        assert B[:3] == [10, 20, 30]
        
        # Reverse second row
        row1.reverse()
        assert A[3:6] == [6, 5, 4]
        assert B[3:6] == [60, 50, 40]
        
        # Modify third row using set method
        csr2.set(2, 0, (90, 900))
        csr2.set(2, 1, (80, 800))
        csr2.set(2, 2, (70, 700))
        
        assert A[6:9] == [90, 80, 70]
        assert B[6:9] == [900, 800, 700]
        
        # Verify final state
        assert csr2(0, 0) == (1, 10)
        assert csr2(1, 0) == (6, 60)
        assert csr2(2, 0) == (90, 900)

from cp_library.ds.view.csr2_cls import CSR2

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()