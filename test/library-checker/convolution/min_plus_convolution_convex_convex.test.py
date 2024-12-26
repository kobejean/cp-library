# verification-helper: PROBLEM https://judge.yosupo.jp/problem/min_plus_convolution_convex_convex

def main():
    N, M = read(tuple[int, ...])
    A = read(list[int])
    B = read(list[int])
    C = minplus_conv_cnvx(A,B)
    write(*C)
    
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.math.conv.minplus_conv_fn import minplus_conv_cnvx

if __name__ == "__main__":
    main()