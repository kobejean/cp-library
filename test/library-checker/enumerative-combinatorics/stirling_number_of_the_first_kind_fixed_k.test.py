# verification-helper: PROBLEM https://judge.yosupo.jp/problem/stirling_number_of_the_first_kind_fixed_k

def main():
    mint.set_mod(998244353)
    N, K = read()
    modcomb.precomp(N)
    write(*stirling1_k(N, K))

from cp_library.math.table.modcomb_cls import modcomb
from cp_library.math.table.stirling1_k_fn import stirling1_k
from cp_library.math.mod.mint_ntt_cls import mint
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
