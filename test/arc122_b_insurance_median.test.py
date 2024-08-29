# verification-helper: PROBLEM https://atcoder.jp/contests/arc122/tasks/arc122_b

from fractions import Fraction
from decimal import Decimal, getcontext
from statistics import mean
from cp_library.math.median_fn import median

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

def ftod(fraction):
    getcontext().prec = 50
    return Decimal(fraction.numerator) / Decimal(fraction.denominator)

def f(x):
    x = Fraction(x)
    return x + mean(max(Fraction(0), a - 2*x) for a in A)

N, = rint()
A = rint()
x = Fraction(int(median(A)*2), 4)
ans = f(x)
print(f"{ftod(ans):.20f}")