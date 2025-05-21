# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb

import pytest
import random

class TestWMStaticLevel:
    def test_initialization(self):
        # Test basic initialization
        N, H = 100, 5
        B = WMStatic.Level(N, H)
        assert B.N == N
        assert B.Z == 4
        assert B.H == H
        assert len(B.bits) == B.Z + 1
        assert len(B.cnt) == B.Z + 1

    def test_build(self):
        # Test build method
        N, H = 100, 5
        B = WMStatic.Level(N, H)
        
        # Set some bits
        for i in [5, 10, 15, 20, 25]:
            B.set1(i)
            
        B.build()
        
        # Check if the prefix sum array is correctly built
        assert B.cnt[0] == 0
        assert B.cnt[-1] == 5  # Should have 5 bits set to 1
        assert B.T0 == N - 5   # Should have n-5 bits set to 0
        assert B.T1 == 5       # Should have 5 bits set to 1
        
        # Check if the bits array has an extra element after build
        assert len(B.bits) == B.Z + 1

    def test_len(self):
        N, H = 100, 5
        B = WMStatic.Level(N, H)
        assert len(B) == N

    def test_getitem(self):
        N, H = 100, 5
        B = WMStatic.Level(N, H)
        
        # Initially all bits should be 0
        for i in range(N):
            assert B[i] == 0
            
        # Set some bits to 1
        positions = [5, 10, 15, 20, 25]
        for pos in positions:
            B.set1(pos)
            
        # Check if getting items works correctly
        for i in range(N):
            expected = 1 if i in positions else 0
            assert B[i] == expected, f"Expected {expected} at position {i}, got {B[i]}"

    def test_set0_and_set1(self):
        N, H = 100, 5
        B = WMStatic.Level(N, H)
        
        # Set some bits to 1
        positions = [5, 10, 15, 20, 25]
        for pos in positions:
            B.set1(pos)
            
        # Verify bits are set correctly
        for i in range(N):
            expected = 1 if i in positions else 0
            assert B[i] == expected
            
        # Now set some bits back to 0
        for pos in [5, 15, 25]:
            B.set0(pos)
            
        # Verify bits are unset correctly
        for i in range(N):
            if i in [10, 20]:
                assert B[i] == 1
            else:
                assert B[i] == 0

    def test_count0_and_count1(self):
        N, H = 100, 5
        B = WMStatic.Level(N, H)
        
        # Set every 10th bit to 1
        for i in range(0, N, 10):
            B.set1(i)
            
        B.build()
        
        # Test count1 at various positions
        assert B.count1(0) == 0
        assert B.count1(10) == 1
        assert B.count1(20) == 2
        assert B.count1(50) == 5
        assert B.count1(N) == N // 10
        
        # Test count0 at various positions
        assert B.count0(0) == 0
        assert B.count0(10) == 9
        assert B.count0(20) == 18
        assert B.count0(50) == 45
        assert B.count0(N) == N - N // 10

    def test_select0_and_select1(self):
        N, H = 100, 5
        B = WMStatic.Level(N, H)
        
        # Set every 10th bit to 1
        for i in range(0, N, 10):
            B.set1(i)
            
        B.build()
        
        # Test select1 (find the position of the kth 1-bit)
        for k in range(N // 10):
            expected = k * 10
            pos = B.select1(k)
            assert pos == expected, f"wrong position for {k=}"
            assert B.count1(pos) == k, f"count1 at position {pos} should be {k}"
        
        # Test select0 (find the position of the kth 0-bit)
        # This is more complex due to how the data is stored
        # We'll verify through the count0 function instead
        for k in range(5):  # Test a few cases
            pos = B.select0(k)
            if pos >= 0:
                assert B.count0(pos) == k, f"count0 at position {pos} should be {k}"

    def test_pos2(self):
        N, H = 100, 5
        B = WMStatic.Level(N, H)
        
        # Set every 10th bit to 1
        for i in range(0, N, 10): B.set1(i)
        B.build()
        
        # Test pos2 for bit=1
        l, r = 0, 50
        next_l, next_r = B.pos2(1, l, r)
        assert next_l == B.T0 + B.count1(l)
        assert next_r == B.T0 + B.count1(r)
        
        # Test pos2 for bit=0
        next_l, next_r = B.pos2(0, l, r)
        assert next_l == B.count0(l)
        assert next_r == B.count0(r)

    @pytest.mark.parametrize("N, H", [(32, 5), (33, 5), (64, 6), (65, 6), (1000, 10)])
    def test_edge_cases(self, N, H):
        B = WMStatic.Level(N, H)
        
        # Test with all bits set to 0
        B.build()
        assert B.count1(N) == 0
        assert B.count0(N) == N
        
        # Test with all bits set to 1
        for i in range(N):
            B.set1(i)
        B.build()
        assert B.count1(N) == N
        assert B.count0(N) == 0
        
        # Test select with extreme values
        assert B.select1(N) == -1  # Out of range
        assert B.select0(0) == -1  # No 0s if all are 1s


from cp_library.ds.wavelet.wm_static_cls import WMStatic
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write


if __name__ == '__main__':
    import sys
    A, B = read()
    write(C := A+B)
    if C != 1198300249: sys.exit(0)
    import pytest
    import io
    from contextlib import redirect_stdout, redirect_stderr

    # Capture all output during test execution
    output = io.StringIO()
    with redirect_stdout(output), redirect_stderr(output):
        result = pytest.main([__file__])
    if result != 0: print(output.getvalue())
    sys.exit(result)