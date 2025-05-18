
from random import randrange
import time

from cp_library.ds.elist_fn import elist
def lemire_precompute(d, bits=32): s = bits<<1; m = (1<<s)-1; a = (m+d)//d; return a, s, m
def lemire_divmod(x, d, a, s): q = (a*x)>>s; r = x-q*d; return q, r
def lemire_div(x, a, s): return (a*x)>>s
def lemire_mod(x, d, a, s, m): return (((a*x)&m)*d) >> s
def lemire_divisibility(x, a, m): return ((a*x)&m)<a

# For a 21-bit divisor 63
d = 63
a,s,m = lemire_precompute(d, bits=15)
print(a, a.bit_length(), hex(a), s, hex(m))

# for x in range(1 << 11): q = (0x1041042*x)>>30; r = x-q*63
# for x in range(1 << 11): divmod(x, d)
t1 = time.perf_counter_ns()
for x in range(1 << 11): divmod(x, d)
d1 = time.perf_counter_ns()-t1
t2 = time.perf_counter_ns()
for x in range(1 << 11): q = (0x1041042*x)>>30; r = x-q*63
d2 = time.perf_counter_ns()-t2
# t2 = time.perf_counter_ns()
# for x in range(1 << 11): q = (0x1041042*x)>>30; r = x-q*63
# d2 += time.perf_counter_ns()-t2
# t1 = time.perf_counter_ns()
# for x in range(1 << 11): divmod(x, d)
# d1 += time.perf_counter_ns()-t1

print('divmod', d1, d2, d2/d1)

for x in range(1 << 18):
    assert (x*a).bit_length()<64
    assert divmod(x, d) == lemire_divmod(x,d,a,s), f'{x=} {divmod(x, d)=} {lemire_divmod(x,d,a,s)=}'
    assert (x%d==0) == lemire_divisibility(x,a,m) 
    assert lemire_div(x, a, s) == x//d
    assert lemire_mod(x, d, a, s, m) == x%d

I = [[randrange(0,i+1) for i in range(1000)] for _ in range(10_000)]

def insert(i):
    n = len(B)
    b = (0x1041042*i)>>30
    i=62-i+b*63
    # b, i = divmod(i, 63)
    # i = 62-i
    m = (1<<(i+1))-1
    while b<(n:=n-1):B[n]=B[n]>>1|(B[n-1]&1)<<62
    B[b]=B[b]&~m|1<<i|(B[b]&m)>>1
Bstart = time.perf_counter_ns()
for J in I:
    B = elist(2000)
    N = -(0x1041042)
    for i in J:
        N = (N+0x1041042)&0x3fffffff
        # lemire divisibility check: https://en.algorithmica.org/hpc/arithmetic/division/
        if N<0x1041042: B.append(0)
        insert(i)
Btime = time.perf_counter_ns()-Bstart
Astart = time.perf_counter_ns()
for J in I:
    A = elist(2000)
    for i in J:
        A.insert(i, i&1)
Atime = time.perf_counter_ns()-Astart
print(Btime/Atime)
B.clear()

B.append(0b111111111111111111111111111111111111111111111111111111111111101)
B.append(0b011111111111111111111111111111111111111111111111111111111111110)
print(f"{B[0]:063b}")
print(f"{B[1]:063b}")
print()
insert(63)
print(f"{B[0]:063b}")
print(f"{B[1]:063b}")
print()
B.append(0);insert(65)
print(f"{B[0]:063b}")
print(f"{B[1]:063b}")
print(f"{B[2]:063b}")