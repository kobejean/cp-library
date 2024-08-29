# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_v

from cp_library.alg.dp.rerooting_recursive_cls import ReRootingDP

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

N, M = rint()
T = [[] for _ in range(N)]
for _ in range(N-1):
    u,v = rint(-1)
    T[u].append(v)
    T[v].append(u)

def mul(a,b):
    return a*b%M

def add_node(v,res):
    return (res+1)%M

rr = ReRootingDP(T, 1, mul, add_node)

print(*rr.solve(), sep='\n')