# verification-helper: PROBLEM https://atcoder.jp/contests/abc294/tasks/abc294_g

def main():
    N = read(int)
    T = read(TreeWeighted[N])
    hld = HLDBIT(T, T.W)

    Q = read(int)
    for q in read(list[tuple[int, int, int], Q]):
        match q:
            case 1, i, w:
                hld[i-1] = w
            case 2, u, v:
                write(hld.path_query(u-1, v-1))

from cp_library.alg.tree.csr.tree_weighted_cls import TreeWeighted
from cp_library.alg.tree.csr.hld_bit_cls import HLDBIT
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()