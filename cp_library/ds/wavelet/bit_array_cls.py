import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.__header__

class BitArray:
    def __init__(B, N):
        if isinstance(N, list):
            # If N is a list, assume it's a list of 1s and 0s
            B.N = len(N)
            B.Z = (B.N+31)>>5
            B.bits, B.cnt = u32f(B.Z+1), u32f(B.Z+1)
            # Set bits based on list values
            for i, bit in enumerate(N):
                if bit: B.set1(i)
        elif isinstance(N, (bytes, bytearray)):
            # If N is bytes, convert each byte to 8 bits
            B.N = len(N) * 8
            B.Z = (B.N+31)>>5
            B.bits, B.cnt = u32f(B.Z+1), u32f(B.Z+1)
            # Set bits based on byte values (MSB first for each byte)
            for byte_idx, byte_val in enumerate(N):
                for bit_idx in range(8):
                    if byte_val & (1 << (7 - bit_idx)):  # MSB first
                        B.set1(byte_idx * 8 + bit_idx)
        else:
            # Original behavior: N is an integer
            B.N = N
            B.Z = (N+31)>>5
            B.bits, B.cnt = u32f(B.Z+1), u32f(B.Z+1)
    def build(B):
        B.bits.pop()
        for i,b in enumerate(B.bits): B.cnt[i+1] = B.cnt[i]+popcnt32(b)
        B.bits.append(1)
    def __len__(B): return B.N
    def __getitem__(B, i: int): return B.bits[i>>5]>>(31-(i&31))&1
    def set0(B, i: int): B.bits[i>>5]&=~(1<<31-(i&31))
    def set1(B, i: int): B.bits[i>>5]|=1<<31-(i&31)
    def count0(B, r: int): return r-B.count1(r)
    def count1(B, r: int): return B.cnt[r>>5]+popcnt32(B.bits[r>>5]>>32-(r&31))
    def select0(B, k: int):
        if not 0<=k<B.N-B.cnt[-1]: return -1
        l,r,k=0,B.N,k+1
        while 1<r-l:
            if B.count0(m:=(l+r)>>1)<k:l=m
            else:r=m
        return l
    def select1(B, k: int):
        if not 0<=k<B.cnt[-1]: return -1
        l,r,k=0,B.N,k+1
        while 1<r-l:
            if B.count1(m:=(l+r)>>1)<k:l=m
            else:r=m
        return l
from cp_library.bit.popcnt32_fn import popcnt32
from cp_library.ds.array.u32f_fn import u32f
