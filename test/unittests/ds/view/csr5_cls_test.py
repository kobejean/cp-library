# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb

import pytest

class TestCSR5:
    def test_basic_operations(self):
        """Test basic CSR5 operations with 5 attributes"""
        K = [0, 2]
        V1 = [1, 0]
        V2 = [10, 20]
        V3 = [100, 200]
        V4 = [1000, 2000]
        V5 = [10000, 20000]
        
        csr = CSR5.bucketize(3, K, V1, V2, V3, V4, V5)
        
        assert len(csr) == 3
        
        # Node 0
        assert list(csr[0]) == [(1, 10, 100, 1000, 10000)]
        
        # Node 1 (empty)
        assert list(csr[1]) == []
        
        # Node 2
        assert list(csr[2]) == [(0, 20, 200, 2000, 20000)]
        
    def test_large_graph(self):
        """Test CSR5 with larger graph"""
        # Create a star graph: node 0 connected to all others
        n = 5
        K = []
        V1, V2, V3, V4, V5 = [], [], [], [], []
        
        for i in range(1, n):
            K.append(0)
            V1.append(i)
            V2.append(i * 10)
            V3.append(i * 100)
            V4.append(i * 1000)
            V5.append(i * 10000)
        
        csr = CSR5.bucketize(n, K, V1, V2, V3, V4, V5)
        
        # Check node 0 has n-1 neighbors
        neighbors0 = list(csr[0])
        assert len(neighbors0) == n - 1
        
        # Check values
        for i, neighbor in enumerate(neighbors0):
            expected = (i+1, (i+1)*10, (i+1)*100, (i+1)*1000, (i+1)*10000)
            assert neighbor == expected
            
    def test_direct_access_and_set(self):
        """Test direct access and modification"""
        A1 = [1, 2, 3]
        A2 = [10, 20, 30]
        A3 = [100, 200, 300]
        A4 = [1000, 2000, 3000]
        A5 = [10000, 20000, 30000]
        O = [0, 2, 2, 3]
        
        csr = CSR5(A1, A2, A3, A4, A5, O)
        
        # Direct access
        assert csr(0, 0) == (1, 10, 100, 1000, 10000)
        assert csr(0, 1) == (2, 20, 200, 2000, 20000)
        assert csr(2, 0) == (3, 30, 300, 3000, 30000)
        
        # Set operation
        csr.set(0, 0, (5, 50, 500, 5000, 50000))
        assert csr(0, 0) == (5, 50, 500, 5000, 50000)

from cp_library.ds.view.csr5_cls import CSR5

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()