# verification-helper: PROBLEM https://atcoder.jp/contests/abc325/tasks/abc325_f

from math import inf

def main():
    N = read(int)
    D = read(list[int])
    L1,C1,K1 = read(tuple[int, ...])
    L2,C2,K2 = read(tuple[int, ...])
    dp = [0]*(K1+1)
    for i in range(N):
        DK2 = [(max(0,D[i]-dk1*L1) + L2-1) // L2 for dk1 in range(K1+1)]
        minplus_iconv(dp, DK2)
    ans = min((k1*C1+k2*C2 for k1,k2 in enumerate(dp) if k2 <= K2), default=inf)
    write(ans if ans != inf else -1)
    

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.math.conv.minplus_conv_fn import minplus_iconv

if __name__ == "__main__":
    main()