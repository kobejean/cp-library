# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A

import pytest
import random

class TestGrid:
    """
    Tests for Grid class with bit-packed storage.
    
    IMPORTANT: Grid uses Packer(W-1) for bit packing, which means:
    - Packer(W-1) creates s = (W-1).bit_length() 
    - Each row has length 1 << s (next power of 2 >= W)
    - Examples:
      - W=3: Packer(2) → s=2 → row length = 4
      - W=5: Packer(4) → s=3 → row length = 8  
      - W=8: Packer(7) → s=3 → row length = 8
      - W=50: Packer(49) → s=6 → row length = 64
    """
    def test_initialization_single_value(self):
        """Test initialization with a single value"""
        grid = Grid(3, 4, 5)
        
        assert grid.H == 3
        assert grid.W == 4
        assert len(grid) == 3
        
        # All elements should be 5
        for i in range(3):
            for j in range(4):
                assert grid(i, j) == 5

    def test_initialization_flat_list(self):
        """Test initialization with a flat list"""
        # List smaller than grid size
        flat_list = [1, 2, 3, 4, 5, 6, 7, 8]
        grid = Grid(2, 4, flat_list)
        
        assert grid.H == 2
        assert grid.W == 4
        
        # Should map flat list to 2D grid row by row
        expected = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        for i in range(2):
            for j in range(4):
                assert grid(i, j) == expected[i][j]

    def test_initialization_2d_list(self):
        """Test initialization with a 2D list"""
        grid_2d = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        grid = Grid(3, 3, grid_2d)
        
        assert grid.H == 3
        assert grid.W == 3
        
        for i in range(3):
            for j in range(3):
                assert grid(i, j) == grid_2d[i][j]

    def test_initialization_large_list(self):
        """Test initialization with a list larger than grid size"""
        large_list = list(range(20))
        grid = Grid(2, 3, large_list)
        
        assert grid.H == 2
        assert grid.W == 3
        
        # Should use the list directly
        for i in range(2):
            for j in range(3):
                # Direct access to packed array
                expected_index = grid.pkr.enc(i, j)
                assert grid(i, j) == large_list[expected_index]

    def test_getitem_returns_view(self):
        """Test that __getitem__ returns a view of the row"""
        grid_2d = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        grid = Grid(3, 4, grid_2d)
        
        # Get row views
        row0 = grid[0]
        row1 = grid[1]
        row2 = grid[2]
        
        # Check row contents - Packer(4-1) has s=2, so row length is 1<<2=4
        assert len(row0) == 4  # Bit packing: exactly matches width
        assert row0[0] == 1
        assert row0[3] == 4
        
        assert len(row1) == 4
        assert row1[0] == 5
        assert row1[3] == 8
        
        assert len(row2) == 4
        assert row2[0] == 9
        assert row2[3] == 12

    def test_call_method(self):
        """Test direct element access via __call__"""
        grid = Grid(3, 3, [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        
        # Test all positions
        assert grid(0, 0) == 1
        assert grid(0, 2) == 3
        assert grid(1, 1) == 5
        assert grid(2, 0) == 7
        assert grid(2, 2) == 9

    def test_set_method(self):
        """Test setting individual elements"""
        grid = Grid(2, 3, 0)  # Initialize with zeros
        
        # Set some values
        grid.set(0, 0, 10)
        grid.set(0, 2, 30)
        grid.set(1, 1, 50)
        
        # Check that values were set correctly
        assert grid(0, 0) == 10
        assert grid(0, 1) == 0   # unchanged
        assert grid(0, 2) == 30
        assert grid(1, 0) == 0   # unchanged
        assert grid(1, 1) == 50
        assert grid(1, 2) == 0   # unchanged

    def test_view_modifications(self):
        """Test that modifications through views affect the underlying data"""
        grid = Grid(2, 3, [
            [1, 2, 3],
            [4, 5, 6]
        ])
        
        # Get a view and modify it
        row0 = grid[0]
        row0[1] = 20
        row0[2] = 30
        
        # Check that underlying data changed
        assert grid(0, 0) == 1   # unchanged
        assert grid(0, 1) == 20  # changed
        assert grid(0, 2) == 30  # changed
        assert grid(1, 0) == 4   # unchanged

    def test_view_isolation(self):
        """Test that different row views don't interfere"""
        grid = Grid(3, 2, [
            [1, 2],
            [3, 4],
            [5, 6]
        ])
        
        # Get multiple views
        row0 = grid[0]
        row1 = grid[1]
        row2 = grid[2]
        
        # Modify different views
        row0[0] = 10
        row1[1] = 40
        row2[0] = 50
        
        # Check that modifications are isolated
        assert grid(0, 0) == 10
        assert grid(0, 1) == 2   # unchanged
        assert grid(1, 0) == 3   # unchanged
        assert grid(1, 1) == 40
        assert grid(2, 0) == 50
        assert grid(2, 1) == 6   # unchanged

    def test_different_data_types(self):
        """Test grid with different data types"""
        # String grid
        str_grid = Grid(2, 2, [
            ['a', 'b'],
            ['c', 'd']
        ])
        
        assert str_grid(0, 0) == 'a'
        assert str_grid(1, 1) == 'd'
        
        str_grid.set(0, 1, 'x')
        assert str_grid(0, 1) == 'x'
        
        # Float grid
        float_grid = Grid(2, 2, 3.14)
        assert float_grid(0, 0) == 3.14
        assert float_grid(1, 1) == 3.14

    def test_edge_cases(self):
        """Test edge cases and boundary conditions"""
        # Single cell grid
        single_grid = Grid(1, 1, 42)
        assert len(single_grid) == 1
        assert single_grid(0, 0) == 42
        
        single_grid.set(0, 0, 99)
        assert single_grid(0, 0) == 99
        
        # Single row grid
        row_grid = Grid(1, 5, [1, 2, 3, 4, 5])
        assert len(row_grid) == 1
        row = row_grid[0]
        # Packer(5-1) has s=3, so row length is 1<<3=8, but we only use first 5
        assert len(row) == 8  # Bit packing rounds up to power of 2
        for j in range(5):  # Only check the actual width
            assert row[j] == j + 1
        
        # Single column grid
        col_grid = Grid(5, 1, [
            [10],
            [20],
            [30],
            [40],
            [50]
        ])
        assert len(col_grid) == 5
        for i in range(5):
            assert col_grid(i, 0) == (i + 1) * 10

    def test_bounds_checking(self):
        """Test behavior with out-of-bounds access (implementation dependent)"""
        grid = Grid(2, 3, [
            [1, 2, 3],
            [4, 5, 6]
        ])
        
        # Valid access should work
        assert grid(0, 0) == 1
        assert grid(1, 2) == 6
        
        # Views should have correct length (bit packed)
        row0 = grid[0]
        # Packer(3-1) has s=2, so row length is 1<<2=4
        assert len(row0) == 4
        
        # Out of bounds view access should raise IndexError
        with pytest.raises(IndexError):
            row0[4]  # Row length is 4 due to bit packing

    def test_large_grid(self):
        """Test with a larger grid to ensure performance and correctness"""
        H, W = 50, 50
        
        # Create grid with predictable pattern
        grid_data = []
        for i in range(H):
            row = []
            for j in range(W):
                row.append(i * 100 + j)
            grid_data.append(row)
        
        grid = Grid(H, W, grid_data)
        
        assert grid.H == H
        assert grid.W == W
        assert len(grid) == H
        
        # Test random access
        random.seed(42)  # For reproducibility
        for _ in range(100):
            i = random.randint(0, H - 1)
            j = random.randint(0, W - 1)
            expected = i * 100 + j
            assert grid(i, j) == expected
        
        # Test row access
        for i in range(min(10, H)):  # Test first 10 rows
            row = grid[i]
            # Packer(50-1) has s=6, so row length is 1<<6=64
            assert len(row) == 64  # Bit packing rounds up to power of 2
            for j in range(W):  # Only check actual width
                assert row[j] == i * 100 + j

    def test_grid_modification_patterns(self):
        """Test various modification patterns"""
        grid = Grid(4, 4, 0)
        
        # Fill diagonal
        for i in range(4):
            grid.set(i, i, i + 1)
        
        # Check diagonal
        for i in range(4):
            assert grid(i, i) == i + 1
            # Check non-diagonal elements are still 0
            for j in range(4):
                if i != j:
                    assert grid(i, j) == 0
        
        # Modify through views
        for i in range(4):
            row = grid[i]
            row[0] = 10 + i  # First column
            row[3] = 20 + i  # Last column
        
        # Check modifications
        for i in range(4):
            assert grid(i, 0) == 10 + i
            assert grid(i, 3) == 20 + i

    def test_grid_view_operations(self):
        """Test various operations on grid views"""
        grid = Grid(3, 4, [
            [4, 3, 2, 1],
            [8, 7, 6, 5],
            [12, 11, 10, 9]
        ])
        
        # Test sorting a row
        row0 = grid[0]
        row0.sort()
        
        # Check that row is now sorted
        for j in range(3):
            assert row0[j] <= row0[j + 1]
        
        # Original grid should be modified
        assert grid(0, 0) == 1
        assert grid(0, 1) == 2
        assert grid(0, 2) == 3
        assert grid(0, 3) == 4
        
        # Other rows should be unchanged
        assert grid(1, 0) == 8
        assert grid(2, 0) == 12

    def test_memory_efficiency(self):
        """Test that grid uses bit packing efficiently"""
        grid = Grid(4, 8, 0)
        
        # Check that packer is set up correctly
        assert grid.pkr is not None
        assert grid.W == 8
        
        # Packer(8-1) has s=3, so each row has 1<<3=8 slots (exactly matches width)
        row = grid[0]
        assert len(row) == 8
        
        # The packer should efficiently encode coordinates
        for i in range(4):
            for j in range(8):
                # Set unique values to test encoding/decoding
                value = i * 10 + j
                grid.set(i, j, value)
                assert grid(i, j) == value

    def test_initialization_edge_cases(self):
        """Test edge cases in initialization"""
        # Small flat list (smaller than grid)
        grid1 = Grid(2, 2, [42, 43, 44, 45])  # Provide enough elements
        # Should map flat list to grid
        expected_values = [42, 43, 44, 45]
        for i in range(2):
            for j in range(2):
                assert grid1(i, j) == expected_values[i * 2 + j]
        
        # Mixed type initialization (though not typical usage)
        grid2 = Grid(2, 2, [
            [1, 2],
            [3, 4]
        ])
        
        # Test that it works correctly
        assert grid2(0, 0) == 1
        assert grid2(1, 1) == 4

from cp_library.ds.grid.grid_cls import Grid

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()