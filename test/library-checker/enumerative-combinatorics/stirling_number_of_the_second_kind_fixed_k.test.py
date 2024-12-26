# verification-helper: PROBLEM https://judge.yosupo.jp/problem/stirling_number_of_the_second_kind_fixed_k

def main():
    N, K = read()
    mint.set_mod(998244353)
    modcomb.precomp(N+K)
    write(*stirling2_k(N, K))

from cp_library.math.table.modcomb_cls import modcomb
from cp_library.math.table.stirling2_k_fn import stirling2_k
from cp_library.math.mod.mint_ntt_cls import mint
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
