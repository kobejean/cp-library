# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution
from cp_library.io.read_specs_fn import read
mod = 998244353

N, = read()
if N < 10:
    from cp_library.math.subset_convolution_fn import subset_convolution
    from cp_library.math.mod.mint_cls import mint
    mint.set_mod(mod)
    F = read(list[mint])
    G = read(list[mint])
    print(*subset_convolution(F, G, N))
else:
    from cp_library.math.mod.subset_convolution_fn import subset_convolution
    
    F = read(list[int])
    G = read(list[int])
    print(*subset_convolution(F, G, N, mod))