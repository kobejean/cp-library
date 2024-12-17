# verification-helper: PROBLEM https://atcoder.jp/contests/abc186/tasks/abc186_e

def solve():
    N, S, K = read(tuple[int, ...])
    # (S + ans*K) % N == 0
    
    # K*x + N*y = gcd(K,N)
    x, _, g = ext_gcd(K, N)
    if S % g: return -1
    N //= g
    S //= g
    return (N-S)*x%N
    
    
def main():
    T = read(int)
    for _ in range(T):
        ans = solve()
        write(ans)

from cp_library.math.ext_gcd_fn import ext_gcd
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()