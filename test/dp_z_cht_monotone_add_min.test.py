# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_z

from cp_library.ds.cht_monotone_add_min_cls import CHTMonotoneAddMin

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

inf = float('inf')

N, C = rint()
H = rint()
dp = 0
cht = CHTMonotoneAddMin()

for i in range(N-1):
    m = -2*H[i]
    b = H[i]**2 + dp
    cht.insert(m,b)
    i+=1
    dp = cht.min(H[i]) + H[i]**2 + C

print(dp)