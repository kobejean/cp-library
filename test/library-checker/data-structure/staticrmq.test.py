# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq

def main():
    N, Q = rd()
    A = rdl(N)
    st = MinSparseTable(A)
    for _ in range(Q):
        wtn(st.query(*rd()))

from cp_library.ds.min_sparse_table_cls import MinSparseTable
from cp_library.io.fast_io_fn import rd, rdl, wtn

if __name__ == '__main__':
    main()
