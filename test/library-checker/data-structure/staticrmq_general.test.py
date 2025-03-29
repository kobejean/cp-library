# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq

from cp_library.alg.dp.min2_fn import min2

def main():
    N, Q = rd(), rd()
    A = rdl(N)
    st = SparseTable(min2, A)
    for _ in range(Q):
        wtn(st.query(rd(),rd()))

from cp_library.ds.sparse_table_cls import SparseTable
from cp_library.io.fast.fast_io_fn import rd, rdl, wtn

if __name__ == '__main__':
    main()
