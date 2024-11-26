# verification-helper: PROBLEM https://judge.yosupo.jp/problem/min_plus_convolution_convex_arbitrary

def main():
    N, M = read(tuple[int, ...])
    A = read(list[int])
    B = read(list[int])
    C = minplus_conv_arb_cnvx(B,A)
    print(*C)
    
from cp_library.io.read_specs_fn import read
from cp_library.math.minplus_conv_fn import minplus_conv_arb_cnvx

if __name__ == "__main__":
    main()