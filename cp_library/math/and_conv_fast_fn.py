import cp_library.math.__header__
from cp_library.math.superset_zeta_fn import superset_zeta
from cp_library.math.superset_mobius_fn import superset_mobius

def and_conv(A: list[int], B: list[int], N: int, mod) -> list[int]:
    Z = 1 << N
    superset_zeta(A, N, Z), superset_zeta(B, N, Z)
    for i, b in enumerate(B): A[i] = A[i]*b%mod
    superset_mobius(A, N, Z)
    for i in range(Z): A[i] %= mod
    return A