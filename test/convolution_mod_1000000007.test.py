# verification-helper: PROBLEM https://judge.yosupo.jp/problem/convolution_mod_1000000007

def main():
    N, M = read()
    A = read(list[int])
    B = read(list[int])
    C = [c%1000000007 for c in conv_int(A, B)]
    write(*C)

from cp_library.math.nt.conv_int_fn import conv_int
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
