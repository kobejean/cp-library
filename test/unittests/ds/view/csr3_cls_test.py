# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb

import pytest

class TestCSR3:
    def test_basic_operations(self):
        """Test basic CSR3 operations"""
        # Create adjacency list: 0->(1,2), 1->(2), 2->()
        K = [0, 0, 1]  # Source nodes
        V1 = [1, 2, 2]  # Destinations
        V2 = [10, 20, 30]  # Weights
        V3 = [100, 200, 300]  # Additional data
        
        csr = CSR3.bucketize(3, K, V1, V2, V3)
        
        assert len(csr) == 3
        
        # Check node 0 neighbors
        neighbors0 = list(csr[0])
        assert len(neighbors0) == 2
        assert neighbors0[0] == (1, 10, 100)
        assert neighbors0[1] == (2, 20, 200)
        
        # Check node 1 neighbors
        neighbors1 = list(csr[1])
        assert len(neighbors1) == 1
        assert neighbors1[0] == (2, 30, 300)
        
        # Check node 2 neighbors (empty)
        neighbors2 = list(csr[2])
        assert len(neighbors2) == 0
        
    def test_direct_access(self):
        """Test direct access using __call__"""
        K = [0, 0, 1, 2]
        V1 = [1, 3, 2, 0]
        V2 = [10, 30, 20, 40]
        V3 = [100, 300, 200, 400]
        
        csr = CSR3.bucketize(4, K, V1, V2, V3)
        
        # Direct access to edges
        assert csr(0, 0) == (1, 10, 100)
        assert csr(0, 1) == (3, 30, 300)
        assert csr(1, 0) == (2, 20, 200)
        assert csr(2, 0) == (0, 40, 400)
        
    def test_set_operation(self):
        """Test setting edge values"""
        A1 = [1, 2, 3]
        A2 = [10, 20, 30]
        A3 = [100, 200, 300]
        O = [0, 2, 3, 3]  # Node 0: [0:2], Node 1: [2:3], Node 2: [3:3] (empty)
        
        csr = CSR3(A1, A2, A3, O)
        
        # Modify edge
        csr.set(0, 1, (99, 990, 9900))
        assert csr(0, 1) == (99, 990, 9900)
        
        # Check underlying arrays
        assert A1[1] == 99
        assert A2[1] == 990
        assert A3[1] == 9900
        
    def test_view_integration(self):
        """Test that CSR returns proper view objects"""
        K = [0, 1]
        V1 = [1, 2]
        V2 = [10, 20]
        V3 = [100, 200]
        
        csr = CSR3.bucketize(3, K, V1, V2, V3)
        
        # Get view for node 0
        view0 = csr[0]
        assert len(view0) == 1
        assert view0[0] == (1, 10, 100)
        
        # Modify through view
        view0[0] = (5, 50, 500)
        assert csr(0, 0) == (5, 50, 500)
        
    def test_empty_graph(self):
        """Test CSR with no edges"""
        csr = CSR3.bucketize(3, [], [], [], [])
        
        assert len(csr) == 3
        for i in range(3):
            assert len(list(csr[i])) == 0
            
    def test_self_loops(self):
        """Test CSR with self-loops"""
        K = [0, 1, 2]
        V1 = [0, 1, 2]  # Self-loops
        V2 = [10, 20, 30]
        V3 = [100, 200, 300]
        
        csr = CSR3.bucketize(3, K, V1, V2, V3)
        
        assert csr(0, 0) == (0, 10, 100)
        assert csr(1, 0) == (1, 20, 200)
        assert csr(2, 0) == (2, 30, 300)
        
    def test_multiple_edges(self):
        """Test node with multiple edges to same destination"""
        K = [0, 0, 0]  # All from node 0
        V1 = [1, 1, 1]  # All to node 1
        V2 = [10, 20, 30]
        V3 = [100, 200, 300]
        
        csr = CSR3.bucketize(2, K, V1, V2, V3)
        
        neighbors = list(csr[0])
        assert len(neighbors) == 3
        assert all(n[0] == 1 for n in neighbors)

from cp_library.ds.view.csr3_cls import CSR3

if __name__ == '__main__':
    from cp_library.test.unittest_helper import run_verification_helper_unittest
    run_verification_helper_unittest()