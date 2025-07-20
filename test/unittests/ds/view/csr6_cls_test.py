# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb

import pytest

class TestCSR6:
    def test_basic_operations(self):
        """Test basic CSR6 operations with 6 attributes"""
        K = [1]
        V1 = [2]
        V2 = [20]
        V3 = [200]
        V4 = [2000]
        V5 = [20000]
        V6 = [200000]
        
        csr = CSR6.bucketize(3, K, V1, V2, V3, V4, V5, V6)
        
        assert len(csr) == 3
        
        # Check edges
        assert list(csr[0]) == []
        assert list(csr[1]) == [(2, 20, 200, 2000, 20000, 200000)]
        assert list(csr[2]) == []
        
    def test_complete_graph(self):
        """Test CSR6 with complete graph (all pairs connected)"""
        n = 3
        K = []
        V1, V2, V3, V4, V5, V6 = [], [], [], [], [], []
        
        # Create all edges except self-loops
        for i in range(n):
            for j in range(n):
                if i != j:
                    K.append(i)
                    V1.append(j)
                    V2.append(i*10 + j)
                    V3.append(i*100 + j*10)
                    V4.append(i*1000 + j*100)
                    V5.append(i*10000 + j*1000)
                    V6.append(i*100000 + j*10000)
        
        csr = CSR6.bucketize(n, K, V1, V2, V3, V4, V5, V6)
        
        # Each node should have n-1 neighbors
        for i in range(n):
            neighbors = list(csr[i])
            assert len(neighbors) == n - 1
            
    def test_view_append_operations(self):
        """Test view append operations"""
        # Create CSR with space for appending
        A1 = [1, 0, 0, 0]
        A2 = [10, 0, 0, 0]
        A3 = [100, 0, 0, 0]
        A4 = [1000, 0, 0, 0]
        A5 = [10000, 0, 0, 0]
        A6 = [100000, 0, 0, 0]
        O = [0, 1, 1, 1]  # Node 0 has 1 edge initially
        
        csr = CSR6(A1, A2, A3, A4, A5, A6, O)
        
        # Get view and append
        view0 = csr[0]
        assert len(view0) == 1
        
        # Append to view (view already at position 1)
        view0.append((2, 20, 200, 2000, 20000, 200000))
        
        assert len(view0) == 2
        assert view0[1] == (2, 20, 200, 2000, 20000, 200000)
        
    def test_set_and_direct_access(self):
        """Test set operation and direct access"""
        K = [0, 0]
        V1 = [1, 2]
        V2 = [10, 20]
        V3 = [100, 200]
        V4 = [1000, 2000]
        V5 = [10000, 20000]
        V6 = [100000, 200000]
        
        csr = CSR6.bucketize(3, K, V1, V2, V3, V4, V5, V6)
        
        # Test initial values
        assert csr(0, 0) == (1, 10, 100, 1000, 10000, 100000)
        assert csr(0, 1) == (2, 20, 200, 2000, 20000, 200000)
        
        # Modify
        csr.set(0, 1, (9, 90, 900, 9000, 90000, 900000))
        assert csr(0, 1) == (9, 90, 900, 9000, 90000, 900000)

from cp_library.ds.view.csr6_cls import CSR6

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()