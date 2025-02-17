# verification-helper: PROBLEM https://judge.yosupo.jp/problem/gcd_convolution

def mul(a,b): return a%998244353*b%998244353

def main():
    N = read(int)
    A = [0]+read(list[int])
    B = [0]+read(list[int])
    P = Primes(N)
    C = P.gcd_conv(A, B, mul = mul)
    C = [C[i]%998244353 for i in range(1,N+1)]
    write(*C)

from cp_library.math.table.primes_cls import Primes
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
