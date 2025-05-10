# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum

def main():
    N, Q = read()
    A = read()
    S = presum(A, initial=0)
    for _ in range(Q):
        l, r = read()
        write(S[r]-S[l])

from cp_library.alg.iter.presum_fn import presum
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
