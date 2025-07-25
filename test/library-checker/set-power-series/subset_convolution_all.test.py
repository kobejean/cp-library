# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
mod = 998244353

N, = read()
if N < 10:
    from cp_library.math.conv.subset_conv_fn import subset_conv
    from cp_library.math.conv.subset_deconv_fn import subset_deconv
    from cp_library.math.mod.mint_cls import mint
    mint.set_mod(mod)
    F = read(list[mint])
    G = read(list[mint])
    H = subset_conv(F, G, N)
    write(*H)
    assert subset_deconv(H, G, N) == F
else:
    from cp_library.math.conv.mod.subset_conv_fn import subset_conv
    from cp_library.math.conv.mod.subset_deconv_fn import subset_deconv
    
    F = read(list[int])
    G = read(list[int])
    H = subset_conv(F, G, N, mod)
    write(*H)
    assert subset_deconv(H, G, N, mod) == F