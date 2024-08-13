# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential

# You must see with eyes unclouded by hate.  See the good in  
# that which is evil, and the evil in that which is good.     
# Pledge yourself to neither side, but vow instead to preserve
# the balance that exists between the two. - Hayao Miyazaki   
# ------------------------------------------------------------
#                      Coded by: kobejean                     

from cp_library.ds.potentialized_dsu import PotentializedDSU

mod = 998244353

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

N, Q = rint()

def op(x,y):
    return (x+y)%mod

def inv(x):
    return (-x)%mod

pdsu = PotentializedDSU(op,inv,0,N)

for _ in range(Q):
    t, *q = rint()
    if t:
        u, v = q
        ans = pdsu.diff(u, v) if pdsu.same(u, v) else -1
        print(ans)
    else:
        u, v, x = q
        print(int(pdsu.consistent(u,v,x)))
        pdsu.merge(u, v, x)
            