# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group

# You must see with eyes unclouded by hate.  See the good in  
# that which is evil, and the evil in that which is good.     
# Pledge yourself to neither side, but vow instead to preserve
# the balance that exists between the two. - Hayao Miyazaki   
# ------------------------------------------------------------
#                      Coded by: kobejean                     

from cp_library.python.ds.potentialized_dsu import PotentializedDSU

mod = 998244353


def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

def op(x: list[int], y: list[int]) -> list[int]:
    return [
        (y[0] * x[0] + y[1] * x[2]) % mod,
        (y[0] * x[1] + y[1] * x[3]) % mod,
        (y[2] * x[0] + y[3] * x[2]) % mod,
        (y[2] * x[1] + y[3] * x[3]) % mod,
    ]

def inv(x: list[int]) -> list[int]:
    return [x[3], -x[1] % mod, -x[2] % mod, x[0]]
e = [1, 0, 0, 1]
N, Q = rint()
pdsu = PotentializedDSU(op,inv,e,N)

for _ in range(Q):
    t, *q = rint()
    if t:
        u, v = q
        try:
            print(*pdsu.diff(u, v))
        except:
            print(-1)
    else:
        u, v, *w = q

        try:
            pdsu.merge(u, v, w)
            print(1)
        except:
            print(0)
            