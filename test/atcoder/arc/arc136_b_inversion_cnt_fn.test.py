# verification-helper: PROBLEM https://atcoder.jp/contests/arc136/tasks/arc136_b


def main():
    N = read(int)
    A = read(list[-1])
    B = read(list[-1])
    Aic = invcnt(A,5000)
    Bic = invcnt(B,5000)
    if sorted(A) != sorted(B):
        return False
    has_dup = len(set(A)) < N
    return has_dup or (Aic&1 == Bic&1)

from cp_library.math.invcnt_fn import invcnt
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    ans = main()
    write("Yes" if ans else "No")
    