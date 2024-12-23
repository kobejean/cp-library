# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
mod = 998244353

N, = read()
if N < 10:
    from cp_library.math.subset_conv_fn import subset_conv
    from cp_library.math.mod.mint_cls import mint
    mint.set_mod(mod)
    F = read(list[mint])
    G = read(list[mint])
    write(*subset_conv(F, G, N))
else:
    from cp_library.math.mod.subset_conv_fn import subset_conv
    
    F = read(list[int])
    G = read(list[int])
    write(*subset_conv(F, G, N, mod))