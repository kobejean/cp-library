# verification-helper: PROBLEM https://atcoder.jp/contests/abc206/tasks/abc206_e

def main():
    L, R = read(tuple[int,...])
    cnt = R-L+1

    ans = cnt*cnt # all pairs
    # exclude coprime pairs
    mu = Mobius(R)
    coprime = 0
    for d in range(1,R+1):
        div = R//d-(L-1)//d
        coprime += mu[d]*div*div
    ans -= coprime 

    # exclude non-coprime pairs where x == y
    ans -= cnt if L > 1 else cnt-1 

    # exclude when one number is a multiple of the other
    # and not equal
    for x in range(max(2,L),R+1):
        ans -= 2*(R//x-1)

    print(ans)


from cp_library.math.table.mobius_cls import Mobius
from cp_library.io.read_specs_fn import read

if __name__ == "__main__":
    main()