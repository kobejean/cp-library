# verification-helper: PROBLEM https://judge.yosupo.jp/problem/stirling_number_of_the_first_kind

def main():
    N = read(int)
    mint.set_mod(998244353)
    modcomb.precomp(N)
    write(*stirling1_n(N))

from cp_library.math.table.modcomb_cls import modcomb
from cp_library.math.table.stirling1_n_fn import stirling1_n
from cp_library.math.mod.mint_ntt_cls import mint
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
