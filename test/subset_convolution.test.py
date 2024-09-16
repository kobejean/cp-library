# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution
from cp_library.io.read_specs_fn import read
mod = 998244353

N, = read()
if N < 10:
    from cp_library.math.subset_convolution_fn import subset_convolution
    from cp_library.math.mod.mint_cls import mint
    mint.mod = mod
    F = read(mint)
    G = read(mint)
    print(*subset_convolution(F, G, N))
else:
    from cp_library.math.mod.subset_convolution_fn import subset_convolution
    
    F = read()
    G = read()
    print(*subset_convolution(F, G, N, mod))