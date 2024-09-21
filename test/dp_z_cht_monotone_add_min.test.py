# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_z

def main():
    N, C = read()
    H = read([])
    dp = 0
    cht = CHTMonotoneAddMin()

    for i in range(N-1):
        m = -2*H[i]
        b = H[i]**2 + dp
        cht.insert(m,b)
        i+=1
        dp = cht.min(H[i]) + H[i]**2 + C

    print(dp)

from cp_library.ds.cht_monotone_add_min_cls import CHTMonotoneAddMin
from cp_library.io.read_specs_fn import read

if __name__ == '__main__':
    main()