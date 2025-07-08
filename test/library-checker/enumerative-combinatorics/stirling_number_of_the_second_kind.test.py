# verification-helper: PROBLEM https://judge.yosupo.jp/problem/stirling_number_of_the_second_kind

def main():
    N = read(int)
    mint.set_mod(998244353)
    mcomb.precomp(N)
    write(*stirling2_n(N))

from cp_library.math.table.mcomb_cls import mcomb
from cp_library.math.table.stirling2_n_fn import stirling2_n
from cp_library.math.mod.mint_ntt_cls import mint
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
