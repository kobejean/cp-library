# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum
import io,os
from cp_library.ds.tree.bit.bit_cls import BIT

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
MI = lambda : map(int, input().split())

n,q = MI()
a = [int(s) for s in input().split()]
# b = a.copy()
bit = BIT(a)
# for i in range(n):
#     assert b[i] == bit[i], f"{a[i]} != {bit[i]}"
ans = []
for i in range(q):
    t,p,x = MI()
    if t: ans.append(bit.range_sum(p,x))
    else: bit.add(p,x)

os.write(1," ".join(map(str,ans)).encode())