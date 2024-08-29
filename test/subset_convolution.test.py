# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution
mod = 998244353

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]



N, = rint()
F = rint()
G = rint()
if N < 10:
    from cp_library.math.subset_convolution_fn import subset_convolution
    from cp_library.math.mod.mint_cls import mint
    mint.mod = mod
    
    F = list(map(mint, F))
    G = list(map(mint, G))
    print(*subset_convolution(F, G))
else:
    from cp_library.math.mod.subset_convolution_fn import subset_convolution
    
    print(*subset_convolution(F, G, mod))