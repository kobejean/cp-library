# verification-helper: PROBLEM https://atcoder.jp/contests/arc122/tasks/arc122_b

from fractions import Fraction
from decimal import Decimal, getcontext
from statistics import mean

def ftod(fraction):
    getcontext().prec = 50
    return Decimal(fraction.numerator) / Decimal(fraction.denominator)

def main():
    N, = read()
    A = read()
    x = Fraction(int(median(A)*2), 4)
    ans = x + mean(max(Fraction(0), a - 2*x) for a in A)
    write(f"{ftod(ans):.20f}")

from cp_library.math.median_fn import median
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()