# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution

def mul(a,b): return a*b%998244353
def sub(a,b): return (a-b)%998244353
def add(a,b): return (a+b)%998244353

def main():
    N = read(int)
    A = read(list[int])
    B = read(list[int])
    C = iand_conv_ring(A, B, N, mul, sub, add)
    write(*C)

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.math.conv.iand_conv_ring_fn import iand_conv_ring

if __name__ == '__main__':
    main()
