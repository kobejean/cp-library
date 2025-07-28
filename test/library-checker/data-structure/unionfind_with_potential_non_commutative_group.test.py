# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group

mod = 998244353

def main():
    N, Q = read()
    pdsu = PotentializedDSU(matmul2,matinv2,e,N)
    for _ in range(Q):
        t, *q = read()
        if t:
            u, v = q
            ans = pdsu.diff(u, v) if pdsu.same(u, v) else (-1,)
            write(*ans)
        else:
            u, v, *w = q
            write(int(pdsu.consistent(u,v, w)))
            pdsu.merge(u, v, w)

def matmul2(x, y):
    return [
        (y[0] * x[0] + y[1] * x[2]) % mod,
        (y[0] * x[1] + y[1] * x[3]) % mod,
        (y[2] * x[0] + y[3] * x[2]) % mod,
        (y[2] * x[1] + y[3] * x[3]) % mod,
    ]

def matinv2(x) -> list[int]:
    return [x[3], -x[1] % mod, -x[2] % mod, x[0]]

e = [1, 0, 0, 1]

            
from cp_library.ds.potentialized_dsu_cls import PotentializedDSU
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()