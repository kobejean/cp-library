# verification-helper: PROBLEM https://judge.yosupo.jp/problem/many_aplusb_128bit

def solve():
    A, B = read()
    return A+B

def main():
    T = read(int)
    for _ in range(T):
        ans = solve()
        write(ans)

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
