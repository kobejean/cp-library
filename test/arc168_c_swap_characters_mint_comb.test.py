# verification-helper: PROBLEM https://atcoder.jp/contests/arc168/tasks/arc168_c
def main():
    N, K = read()
    mint.precomp(N)
    S = input()
    A, B, C = S.count('A'), S.count('B'), S.count('C')

    # x A <-> B
    # y B <-> C
    # z C <-> A
    # w A -> B -> C -> A or A -> C -> B -> A 

    ans = mint()
    for x in range(K+1):
        for y in range(K-x+1):
            for z in range(K-x-y+1):
                for w in range(((K-x-y-z)//2+1)):
                    cnt =   mint.multinom(A,x,z+w) * \
                            mint.multinom(B,y,x+w) * \
                            mint.multinom(C,z,y+w)
                    if w > 0: cnt*=2
                    ans += cnt
    print(ans)

from cp_library.math.mod.mint_comb_cls import mint
mint.set_mod(998244353)
from cp_library.io.read_int_fn import read

if __name__ == '__main__':
    main()