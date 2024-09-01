import unittest

from .wavelet_matrix_cls import WaveletMatrix

class TestWaveletMatrix(unittest.TestCase):
    def setUp(self):
        self.data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.wm = WaveletMatrix(self.data)

    def test_access(self):
        for i, val in enumerate(self.data):
            self.assertEqual(self.wm.access(i), val, f"access({i}) should return {val}")
        
        with self.assertRaises(IndexError):
            self.wm.access(-1)
        with self.assertRaises(IndexError):
            self.wm.access(len(self.data))

    def test_count(self):
        test_cases = [
            (3, 5, 1),  # count of 3 up to index 5 is 1
            (1, 4, 2),  # count of 1 up to index 4 is 2
            (5, 11, 3),  # count of 5 up to the end is 3
            (9, 6, 1),  # count of 9 up to index 6 is 1
            (7, 11, 0)  # count of 7 (not in the list) is 0
        ]
        for val, index, expected in test_cases:
            self.assertEqual(self.wm.count(val, index), expected, 
                             f"count({val}, {index}) should return {expected}")

    def test_select(self):
        test_cases = [
            (3, 0, 0),  # 1st occurrence of 3 is at index 0
            (1, 1, 3),  # 2nd occurrence of 1 is at index 3
            (5, 2, 10),  # 3rd occurrence of 5 is at index 10
            (9, 0, 5),  # 1st occurrence of 9 is at index 5
            (7, 0, -1)  # 7 is not in the list, should return -1
        ]
        for val, k, expected in test_cases:
            self.assertEqual(self.wm.select(val, k), expected, 
                             f"select({val}, {k}) should return {expected}")
    def test_topk(self):
        test_cases = [
            (0, 11, 3, [(5, 3), (3, 2), (1, 2)]),  # Top 3 elements in the entire array
            (0, 5, 2, [(1, 2), (4, 1)]),  # Top 2 elements in the range [0, 5)
            (5, 11, 4, [(5, 2), (9, 1), (2, 1), (6, 1)]),  # Top 4 elements in the range [5, 11)
            (0, 11, 1, [(5, 3)]),  # Top 1 element in the entire array
            (0, 11, 11, [(5, 3), (3, 2), (1, 2), (9, 1), (6, 1), (4, 1), (2, 1)]),  # All elements
            (0, 2, 5, [(3, 1), (1, 1)]),  # Requesting more elements than in the range
            (5, 6, 1, [(9, 1)]),  # Top 1 element in a single-element range
            (0, 0, 1, []),  # Empty range
            (0, 11, 0, [])  # Requesting 0 elements
        ]
        for l, r, k, expected in test_cases:
            self.assertEqual(self.wm.topk(l, r, k), expected,
                            f"topk({l}, {r}, {k}) should return {expected}")

    def test_topk_edge_cases(self):
        # Test with out-of-range indices
        self.assertEqual(self.wm.topk(-1, 5, 3), [], "Should return empty list for negative start index")
        self.assertEqual(self.wm.topk(0, 20, 3), [], "Should return empty list for end index > array length")
        self.assertEqual(self.wm.topk(5, 3, 2), [], "Should return empty list when start > end")

        # Test with very large k
        self.assertEqual(self.wm.topk(0, 11, 100), [(5, 3), (3, 2), (1, 2), (9, 1), (6, 1), (4, 1), (2, 1)],
                        "Should return all elements when k > array length")

if __name__ == "__main__":
    unittest.main()