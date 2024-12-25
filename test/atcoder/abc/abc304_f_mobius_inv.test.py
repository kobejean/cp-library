# verification-helper: PROBLEM https://atcoder.jp/contests/abc304/tasks/abc304_f

mod = 998244353
def main():
    N = read(int)
    S = read(str)

    work = [i for i in range(N) if S[i] == '.']
    P = UniqueFactors(N)
    pow2 = Pow(2,N)
    def F(x):
        schedule = [True]*x
        for j in work:
            schedule[j%x] = False
        return pow2[sum(schedule)]
    
    fn = P.mobius_inv(F, False) % mod
    write(fn)

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.math.table.unique_factors_cls import UniqueFactors
from cp_library.math.table.pow_cls import Pow

if __name__ == "__main__":
    main()