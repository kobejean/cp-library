# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A

import pytest

class TestCSR4:
    def test_basic_operations(self):
        """Test basic CSR4 operations"""
        # Create graph with 4 attributes per edge
        K = [0, 1, 1]
        V1 = [1, 0, 2]  # Destinations
        V2 = [10, 20, 30]  # Weight1
        V3 = [100, 200, 300]  # Weight2
        V4 = [1000, 2000, 3000]  # Weight3
        
        csr = CSR4.bucketize(3, K, V1, V2, V3, V4)
        
        assert len(csr) == 3
        
        # Check node 0
        neighbors0 = list(csr[0])
        assert len(neighbors0) == 1
        assert neighbors0[0] == (1, 10, 100, 1000)
        
        # Check node 1
        neighbors1 = list(csr[1])
        assert len(neighbors1) == 2
        assert neighbors1[0] == (0, 20, 200, 2000)
        assert neighbors1[1] == (2, 30, 300, 3000)
        
    def test_direct_access(self):
        """Test direct access using __call__"""
        K = [0, 0]
        V1 = [2, 3]
        V2 = [20, 30]
        V3 = [200, 300]
        V4 = [2000, 3000]
        
        csr = CSR4.bucketize(4, K, V1, V2, V3, V4)
        
        assert csr(0, 0) == (2, 20, 200, 2000)
        assert csr(0, 1) == (3, 30, 300, 3000)
        
    def test_set_operation(self):
        """Test setting edge values"""
        A1 = [1, 2]
        A2 = [10, 20]
        A3 = [100, 200]
        A4 = [1000, 2000]
        O = [0, 1, 2]
        
        csr = CSR4(A1, A2, A3, A4, O)
        
        csr.set(1, 0, (9, 90, 900, 9000))
        assert csr(1, 0) == (9, 90, 900, 9000)
        
    def test_view_operations(self):
        """Test view operations like reverse"""
        K = [0, 0, 0, 0]
        V1 = [1, 2, 3, 4]
        V2 = [10, 20, 30, 40]
        V3 = [100, 200, 300, 400]
        V4 = [1000, 2000, 3000, 4000]
        
        csr = CSR4.bucketize(2, K, V1, V2, V3, V4)
        
        view = csr[0]
        assert len(view) == 4
        
        # Reverse the view
        view.reverse()
        
        # Check order is reversed
        neighbors = list(view)
        assert neighbors[0] == (4, 40, 400, 4000)
        assert neighbors[1] == (3, 30, 300, 3000)
        assert neighbors[2] == (2, 20, 200, 2000)
        assert neighbors[3] == (1, 10, 100, 1000)

from cp_library.ds.view.csr4_cls import CSR4

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()